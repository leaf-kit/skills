#!/usr/bin/env python3
"""만들려는 스킬과 비슷한 것이 이미 있는지 본다.

이 스크립트가 있는 이유는 하나다. **찾는 비용이 만드는 비용보다 커서
다들 만든다.** 이 저장소의 분류 데이터로 그 비용을 낮춘다.

하는 일과 하지 않는 일을 구분한다.
  하는 일   - 소분류 이름과 저장소 설명에서 키워드가 겹치는 후보를 찾는다
  안 하는 일 - "중복이다/아니다"를 판정하지 않는다. 판정은 사람이 한다

사용법:
    ./check_duplicate.py "PR 디프에서 우리 팀 컨벤션 위반을 찾는다"
    ./check_duplicate.py --json "..."       JSON 으로 받는다
    ./check_duplicate.py --top 8 "..."      후보 개수를 바꾼다
"""
import argparse
import csv
import json
import pathlib
import re
import sys

HERE = pathlib.Path(__file__).resolve().parent
ROOT = HERE.parent.parent.parent          # skills/skill-creator-meta/scripts -> repo root
DATA = ROOT / "data"
SNAP = DATA / "snapshots"

CHAPTER = {"A": "part11/02-code.md", "B": "part11/03-writing.md",
           "C": "part11/04-visual.md", "D": "part11/05-platform.md",
           "E": "part11/06-work.md", "F": "part11/07-agent.md",
           "G": "part11/08-meta.md", "H": "part11/09-boundary.md"}

# 어느 요청에나 들어가서 변별력이 없는 말. 점수에서 뺀다.
STOP = {
    "스킬", "에이전트", "클로드", "claude", "skill", "agent", "ai",
    "하는", "하기", "한다", "해주는", "만드는", "만들기", "위한", "자동",
    "자동화", "도구", "작업", "기능", "사용", "사용자", "내용", "파일",
    "the", "for", "and", "with", "that", "this", "from", "into", "a", "an",
}

# 0단계의 다섯 관문. 스크립트가 판단할 수 없으므로 질문으로 돌려준다.
GATES = [
    ("한 번만 쓸 일인가?", "그렇다면 스킬이 아니라 그냥 프롬프트로 쓴다."),
    ("조건 없이 항상 적용되는가?",
     "그렇다면 CLAUDE.md 같은 지침 파일에 둔다. 스킬은 안 불리는 날에 빠진다."),
    ("안 돌면 사고가 나는가?",
     "그렇다면 훅으로 간다. 훅은 판단 없이 항상 실행된다."),
    ("외부 시스템에 붙어야 하는가?",
     "그렇다면 MCP 서버 쪽을 먼저 본다. 스킬은 권한을 들고 있지 않다."),
    ("아래 후보 중 70% 이상 맞는 것이 있는가?",
     "그렇다면 포크해서 고친다. 새로 만들면 생태계에 중복이 하나 늘어난다."),
]


# 조사를 떼지 않으면 "보안을"이 "보안"과 안 맞는다. 긴 것부터 떼야
# "에서"가 "서"보다 먼저 걸린다.
PARTICLE = ("으로써", "로부터", "에서는", "에게서", "이라는", "라는",
            "에서", "에게", "으로", "까지", "부터", "처럼", "보다", "마다",
            "이나", "과의", "와의", "의", "을", "를", "은", "는", "이", "가",
            "에", "도", "만", "로", "과", "와", "및")

# 요청에 쓰는 말과 저장소 설명에 쓰는 말이 다르다. 한국어 요청을 영문
# 설명과 맞추려면 이 다리가 필요하다.
BRIDGE = {
    "코드": ["code"], "리뷰": ["review", "reviewer"], "보안": ["security", "sec",
    "vuln", "audit"], "테스트": ["test", "testing"], "문서": ["doc", "docs",
    "document"], "번역": ["translat", "i18n"], "글쓰기": ["writing", "writer"],
    "교정": ["edit", "proofread"], "회의록": ["meeting", "note"],
    "노션": ["notion"], "슬라이드": ["slide", "pptx", "powerpoint", "deck"],
    "디자인": ["design", "ui", "ux"], "다이어그램": ["diagram", "mermaid",
    "drawio"], "차트": ["chart", "plot", "graph"], "이미지": ["image", "img"],
    "데이터": ["data", "dataset"], "검색": ["search", "retriev"],
    "브라우저": ["browser", "playwright", "puppeteer"],
    "배포": ["deploy", "release", "ci"], "인프라": ["infra", "terraform", "k8s"],
    "클라우드": ["cloud", "aws", "gcp", "azure"], "기획": ["product", "spec",
    "prd"], "마케팅": ["marketing", "ads", "seo"], "영업": ["sales", "crm"],
    "법률": ["legal", "contract"], "재무": ["finance", "account"],
    "채용": ["hiring", "recruit", "resume"], "학습": ["learn", "study",
    "tutor"], "연구": ["research", "paper"], "커밋": ["commit", "git"],
    "디프": ["diff", "patch"], "컨벤션": ["convention", "style", "lint"],
    "리팩터링": ["refactor"], "성능": ["perf", "performance", "benchmark"],
    "취약점": ["vuln", "cve", "exploit"], "메모리": ["memory", "context"],
    "스킬": ["skill"], "마켓플레이스": ["marketplace", "registry", "awesome"],
    "게임": ["game", "unity", "godot"], "자료구조": ["algorithm"],
    "프롬프트": ["prompt"], "평가": ["eval", "benchmark"],
}


def tokens(text):
    """한글 2자 이상, 영문 3자 이상만 남긴다. 한글은 조사를 뗀다."""
    raw = re.findall(r"[가-힣]{2,}|[A-Za-z][A-Za-z0-9+#.-]{2,}", text.lower())
    out = []
    for t in raw:
        t = t.strip(".-")
        if re.fullmatch(r"[가-힣]+", t):
            for p in PARTICLE:
                if len(t) - len(p) >= 2 and t.endswith(p):
                    t = t[: -len(p)]
                    break
        if t and t not in STOP and len(t) >= 2:
            out.append(t)
    # 중복 제거하되 순서는 유지한다
    return list(dict.fromkeys(out))


def expand(toks):
    """소분류 이름, 영문 설명 양쪽에 걸리도록 키를 넓힌다."""
    keys = set(toks)
    for t in toks:
        keys.update(BRIDGE.get(t, []))
        # 어간이 길면 앞 2글자로 부분일치를 허용한다 ("리팩터링" -> "리팩")
        if re.fullmatch(r"[가-힣]{3,}", t):
            keys.add(t[:2])
    return keys


def latest():
    if not SNAP.exists():
        sys.exit(f"없음: {SNAP}\n저장소 루트에서 실행했는지 확인한다.")
    dirs = sorted(d for d in SNAP.iterdir() if d.is_dir())
    if not dirs:
        sys.exit("스냅샷이 없다. data/collect.sh 를 먼저 돌린다.")
    return dirs[-1]


def load(snap):
    rows = list(csv.DictReader(open(snap / "categories.tsv", encoding="utf-8"),
                               delimiter="\t"))
    desc, pushed = {}, {}
    with open(snap / "stars.tsv", encoding="utf-8") as f:
        r = csv.reader(f, delimiter="\t")
        next(r, None)
        for x in r:
            if len(x) >= 5:
                desc[x[1]] = x[4]
                pushed[x[1]] = x[3][:10]
    return rows, desc, pushed


def score(keys, haystack, weight):
    hay = haystack.lower()
    hit = sorted(k for k in keys if k in hay)
    return len(hit) * weight, hit


def main():
    ap = argparse.ArgumentParser(add_help=True)
    ap.add_argument("request", nargs="+", help="만들려는 스킬을 한 문장으로")
    ap.add_argument("--top", type=int, default=6)
    ap.add_argument("--json", action="store_true")
    a = ap.parse_args()

    request = " ".join(a.request)
    toks = tokens(request)
    if not toks:
        sys.exit("키워드를 못 찾았다. 하려는 일을 명사로 다시 적어 본다.\n"
                 '예: "PR 디프에서 팀 컨벤션 위반을 찾는다"')
    keys = expand(toks)

    snap = latest()
    rows, desc, pushed = load(snap)

    # 소분류 단위
    cats, seen = [], set()
    for r in rows:
        code = r["code"]
        if code in seen:
            continue
        seen.add(code)
        s, hit = score(keys, f"{r['category']} {r['subcategory']}", 3)
        if s:
            cats.append({"code": code, "category": r["category"],
                          "subcategory": r["subcategory"], "score": s,
                          "matched": hit,
                          "chapter": CHAPTER.get(code[0], "")})
    cats.sort(key=lambda x: -x["score"])

    # 저장소 단위.
    # 설명만 보면 한국어 요청과 영문 설명이 안 맞아서 거의 다 0점이 된다.
    # 그래서 "같은 소분류에 있다"는 사실 자체를 점수로 물려받는다.
    catscore = {c["code"]: c["score"] for c in cats}
    repos = []
    for r in rows:
        name = r["full_name"]
        d = desc.get(name, "")
        s, hit = score(keys, f"{name} {d}", 2)
        inherited = catscore.get(r["code"], 0)
        if not (s or inherited):
            continue
        why = []
        if inherited:
            why.append("같은 소분류")
        if hit:
            why.append("설명에 " + ", ".join(hit))
        repos.append({"repo": name, "code": r["code"],
                      "subcategory": r["subcategory"],
                      "stars": int(r["stars"]), "pushed": pushed.get(name, "?"),
                      "skill_md": r["skill_md"], "score": s + inherited,
                      "why": " + ".join(why), "desc": d[:110]})
    repos.sort(key=lambda x: (-x["score"], -x["stars"]))
    total_candidates = len(repos)
    repos = repos[:a.top]

    result = {
        "request": request,
        "snapshot": snap.name,
        "keywords": toks,
        "categories": cats[:5],
        "candidates": repos,
        "candidates_total": total_candidates,
        "gates": [{"question": q, "if_yes": w} for q, w in GATES],
        "note": "키워드 겹침이다. 겹친다고 중복이 아니고 안 겹친다고 신규가 아니다. "
                "후보의 소분류 장을 직접 읽고 판단한다.",
        "limit": "이 스냅샷에 들어온 저장소만 본다. SKILL.md 를 표준 경로에 "
                 "두지 않은 저장소는 수집에서 빠졌을 수 있다.",
    }

    if a.json:
        print(json.dumps(result, ensure_ascii=False, indent=2))
        return

    print(f"요청: {request}")
    print(f"스냅샷: {snap.name}   키워드: {', '.join(toks)}")
    print()

    if cats[:5]:
        print("■ 겹치는 소분류")
        for c in cats[:5]:
            print(f"  {c['code']}  {c['category']} / {c['subcategory']}"
                  f"   → {c['chapter']}")
    else:
        print("■ 겹치는 소분류 없음")
        print("  소분류 이름과 안 겹칠 뿐이다. 아래 후보를 먼저 보고,")
        print("  그래도 없으면 skill-selector 의 query.py --list 로 전체를 훑는다.")
    print()

    if repos:
        print(f"■ 먼저 볼 저장소 (후보 {total_candidates}개 중 {len(repos)}개)")
        for r in repos:
            print(f"  {r['repo']}  ({r['stars']:,}★, SKILL.md {r['skill_md']}개,"
                  f" 마지막 푸시 {r['pushed']})")
            print(f"      {r['code']} {r['subcategory']}  |  {r['why']}")
            if r["desc"]:
                print(f"      {r['desc']}")
        if total_candidates > len(repos):
            print(f"  ... --top {min(total_candidates, 20)} 로 더 본다")
    else:
        print("■ 후보 없음")
        print("  키워드가 소분류 이름과도, 저장소 설명과도 안 걸렸다.")
        print("  '없다'로 결론 내지 말고 query.py --list 로 36개 소분류를 직접 훑는다.")
    print()

    print("■ 만들기 전에 답할 다섯 가지")
    for i, (q, w) in enumerate(GATES, 1):
        print(f"  {i}. {q}")
        print(f"     '예'라면 → {w}")
    print()
    print(f"※ {result['note']}")
    print(f"※ {result['limit']}")


if __name__ == "__main__":
    main()
