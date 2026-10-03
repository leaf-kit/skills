#!/usr/bin/env python3
"""스킬 하나를 검사한다. 규격과 이 저장소의 원칙을 같이 본다.

`skills-ref validate` 는 규격만 본다. 규격을 통과한 스킬이 안 불리거나
과하게 작동하는 일이 그래서 생긴다. 이 스크립트는 규격 위반을 ERROR 로,
이 저장소가 측정에서 확인한 설계 문제를 WARN 으로 낸다.

**WARN 은 전부 고쳐야 하는 목록이 아니다.** 각 항목에 "왜"가 붙어 있으니
읽고 판단한다. 근거를 적을 수 있으면 무시해도 된다.

사용법:
    ./validate_skill.py ~/.claude/skills/my-skill
    ./validate_skill.py --json <경로>
    ./validate_skill.py <경로1> <경로2> ...
"""
import argparse
import json
import pathlib
import re
import sys

NAME_RE = re.compile(r"^[a-z0-9]+(-[a-z0-9]+)*$")
FM_RE = re.compile(r"\A---\r?\n(.*?)\r?\n---\r?\n?", re.S)
KNOWN = {"name", "description", "license", "compatibility", "metadata",
         "allowed-tools", "version"}

# 규격이 정한 상한
MAX_NAME, MAX_DESC, MAX_COMPAT = 64, 1024, 500
# 이 저장소가 쓰는 본문 분량 기준
BODY_SOFT, BODY_HARD = 300, 500


def parse_fm(text):
    """프런트매터를 읽는다. 중첩은 안 본다. 스킬 프런트매터는 평평하다."""
    m = FM_RE.match(text)
    if not m:
        return None, text, None
    fm, body = {}, text[m.end():]
    key = None
    for line in m.group(1).splitlines():
        if not line.strip() or line.lstrip().startswith("#"):
            continue
        if line[0] not in " \t" and ":" in line:
            key, _, val = line.partition(":")
            key = key.strip()
            fm[key] = val.strip().strip('"\'')
        elif key:                              # 여러 줄로 이어진 값
            fm[key] = (fm[key] + " " + line.strip()).strip()
    return fm, body, m.group(1)


def body_tokens(body):
    """토큰 근사. 한글은 글자당 약 1.4, 그 밖은 4글자당 1로 센다."""
    ko = len(re.findall(r"[가-힣]", body))
    rest = len(body) - ko
    return int(ko * 1.4 + rest / 4)


def check(path):
    e, w, info = [], [], {}
    d = pathlib.Path(path).expanduser().resolve()
    info["path"] = str(d)

    if not d.is_dir():
        return [f"디렉터리가 아니다: {d}"], [], info
    sk = d / "SKILL.md"
    if not sk.is_file():
        return [f"SKILL.md 가 없다: {sk}"], [], info

    text = sk.read_text(encoding="utf-8")
    fm, body, _ = parse_fm(text)
    if fm is None:
        return ["프런트매터가 없다. 파일 첫 줄이 --- 여야 한다."], [], info

    # ---------- 규격 ----------
    name = fm.get("name", "")
    if not name:
        e.append("name 이 없다.")
    else:
        if not NAME_RE.match(name):
            e.append(f"name 은 소문자, 숫자, 하이픈만 쓴다: {name!r}")
        if len(name) > MAX_NAME:
            e.append(f"name 이 {len(name)}자다. {MAX_NAME}자 이하여야 한다.")
        if name != d.name:
            e.append(f"name({name!r}) 과 디렉터리 이름({d.name!r}) 이 다르다. "
                     "같아야 로드된다.")
    info["name"] = name

    desc = fm.get("description", "")
    if not desc:
        e.append("description 이 없다. 이게 없으면 스킬이 불리지 않는다.")
    elif len(desc) > MAX_DESC:
        e.append(f"description 이 {len(desc)}자다. {MAX_DESC}자 이하여야 한다.")
    info["description_len"] = len(desc)

    compat = fm.get("compatibility", "")
    if len(compat) > MAX_COMPAT:
        e.append(f"compatibility 가 {len(compat)}자다. {MAX_COMPAT}자 이하여야 한다.")

    for k in fm:
        if k not in KNOWN:
            w.append(f"[규격] 알 수 없는 프런트매터 키 {k!r} 다. "
                     "오타이거나 metadata 아래로 들어가야 한다.")

    # ---------- description 다섯 요소 ----------
    if desc:
        if len(desc) < 80:
            w.append(f"[트리거] description 이 {len(desc)}자다. 짧으면 "
                     "걸릴 표현이 부족하다. 사용자가 쓸 말을 더 넣는다.")
        if not re.search(r"[가-힣]", desc) or not re.search(r"[A-Za-z]{3}", desc):
            w.append("[트리거] 키워드가 한쪽 언어뿐이다. 사용자는 두 언어를 "
                     "섞어 쓴다. 한국어와 영어 키워드를 같이 넣는다.")
        if not re.search(r"쓰지 않는|쓰지는 않|적용하지 않|대상이 아니|"
                         r"반대로|제외|해당하지 않|아닌 경우|do not use|"
                         r"not for|except when", desc):
            w.append("[트리거] 제외 조건이 안 보인다. 가장 많이 빠지는 요소다. "
                     '"반대로 ~에는 쓰지 않는다" 를 넣으면 과잉 트리거가 줄고 '
                     "형제 스킬과 경계가 생긴다.")
        hype = [x for x in ("가장 강력", "완벽", "혁신", "최고의", "모든 것을",
                            "다양한 작업", "powerful", "ultimate", "perfectly",
                            "comprehensive", "best-in-class") if x in desc]
        if hype:
            w.append(f"[트리거] 과장 표현이 있다: {', '.join(hype)}. 트리거에 "
                     "기여하지 않고 범위를 넓혀 과잉 트리거를 부른다.")
        if re.search(r"먼저.*그다음|1\.\s|단계로|step 1|first,.*then", desc,
                     re.I):
            w.append("[트리거] description 에 절차가 들어간 것 같다. 이 필드는 "
                     "'언제' 쓰는지를 적는 자리다. '어떻게' 는 본문에 둔다.")

    # ---------- 본문 ----------
    lines = body.strip().splitlines()
    nlines = len(lines)
    info["body_lines"] = nlines
    info["body_tokens_approx"] = body_tokens(body)

    if nlines < 10:
        w.append(f"[본문] {nlines}줄이다. 절차나 판단 기준이 들어갈 자리가 "
                 "없다. description 만으로 되는 일이면 스킬이 아닐 수 있다.")
    if nlines > BODY_HARD:
        w.append(f"[본문] {nlines}줄이다. {BODY_HARD}줄을 넘으면 스킬 둘이 "
                 "섞여 있을 가능성이 높다. 조건부로 읽는 부분을 references/ 로 "
                 "내린다.")
    elif nlines > BODY_SOFT:
        w.append(f"[본문] {nlines}줄이다. {BODY_HARD}줄에 가까워지고 있다. "
                 "조건부로 읽는 내용이 있으면 references/ 로 내린다.")
    if info["body_tokens_approx"] > 5000:
        w.append(f"[본문] 토큰이 약 {info['body_tokens_approx']}개다. 줄 수와 "
                 "토큰은 다르다. 긴 산문을 줄바꿈 없이 쓰면 줄 수는 적고 "
                 "토큰은 많다.")

    guard = re.search(r"과하게|과잉|하지 않는 것|대상이 아니|건드리지|"
                      r"애매하면|확실하지 않으면|do not|out of scope", body)
    if not guard:
        w.append("[과잉 적용] 과잉 적용을 막는 절이 안 보인다. '하라' 는 지시만 "
                 "있으면 에이전트는 무언가 해야 한다고 판단한다. 대상이 아닌 "
                 "것을 셋 이상 적고, 애매할 때 어느 쪽으로 갈지 적는다.")
    elif not re.search(r"비용|더 나쁘|더 크|보다 작|보다 낫|쪽이 낫", body):
        w.append("[과잉 적용] 대상 제외는 있는데 두 방향 실패의 비용 비교가 "
                 "없다. '놓치는 것' 과 '멀쩡한 것을 건드리는 것' 중 어느 쪽이 "
                 "더 나쁜지 한 줄로 적는다. 측정에서 이 한 줄이 가장 큰 차이를 "
                 "만들었다.")

    caps = re.findall(r"\b(?:ALWAYS|NEVER|MUST|CRITICAL|IMPORTANT|DO NOT)\b",
                      body)
    if len(caps) >= 3:
        w.append(f"[본문] 대문자 강조가 {len(caps)}번 나온다. 대문자를 쓰는 "
                 "자리마다 '왜' 가 빠져 있을 수 있다. 금지 목록은 충돌 상황에서 "
                 "무엇을 포기할지 알려 주지 않는다.")

    # ---------- 번들 ----------
    refs = sorted(p for p in (d / "references").glob("**/*")
                  if p.is_file()) if (d / "references").is_dir() else []
    scripts = sorted(p for p in (d / "scripts").glob("**/*")
                     if p.is_file() and p.suffix in (".py", ".sh", ".js", ".ts")
                     ) if (d / "scripts").is_dir() else []
    info["references"] = [p.name for p in refs]
    info["scripts"] = [p.name for p in scripts]

    for p in refs:
        if p.name not in body:
            w.append(f"[번들] references/{p.name} 를 본문에서 가리키지 않는다. "
                     "안 불리는 파일이다.")
        else:
            # 읽기 조건이 같은 줄이나 앞 줄에 있는지 본다
            ctx = ""
            for i, ln in enumerate(lines):
                if p.name in ln:
                    ctx = " ".join(lines[max(0, i - 2):i + 1])
                    break
            if not re.search(r"면|때|경우|할 때|나오면|필요하면|if |when ", ctx):
                w.append(f"[번들] references/{p.name} 에 읽기 조건이 없다. "
                         '"자세한 내용은 참고한다" 로 끝나면 항상 읽거나 한 번도 '
                         '안 읽는다. "~가 나오면 펼친다" 로 적는다.')

    for p in scripts:
        if p.name not in body:
            w.append(f"[번들] scripts/{p.name} 를 본문에서 가리키지 않는다. "
                     "에이전트가 실행할 이유를 못 찾는다.")
        src = p.read_text(encoding="utf-8", errors="replace")
        if p.suffix == ".py" and not re.search(
                r"근사|추정|놓칠|한계|limit|approx|note", src):
            w.append(f"[스크립트] scripts/{p.name} 에 한계를 적은 흔적이 없다. "
                     "근사를 근사라고 출력하지 않으면 에이전트가 사실로 보고한다.")

    # ---------- 평가 ----------
    evals = d / "evals"
    has_eval = evals.is_dir() and any(evals.iterdir())
    info["has_evals"] = has_eval
    if not has_eval:
        w.append("[평가] evals/ 가 없다. 평가 없이는 설계 의도와 실제 기여가 "
                 "다른 것을 알 수 없다. 최소한 성공 1개, 재료 부족 1개, "
                 "개입하면 안 되는 입력 1개를 만든다.")
    else:
        # 팔 구성은 파일 내용보다 디렉터리 이름에 드러나는 일이 많다
        # (without_skill/, baseline/). 경로 이름도 같이 본다.
        paths = [p for p in evals.glob("**/*")]
        blob = "\n".join([str(p.relative_to(evals)) for p in paths] + [
            p.read_text(encoding="utf-8", errors="replace")
            for p in paths
            if p.is_file() and p.suffix in (".md", ".json", ".yaml", ".yml",
                                            ".txt")])
        if blob:
            neg = len(re.findall(r"않는다|안 한다|없다|말아야|does not|no \w+",
                                 blob))
            pos = len(re.findall(r"한다\b|포함한다|적는다|출력한다|제시한다|"
                                 r"includes|contains|reports", blob))
            if neg and pos * 3 < neg:
                w.append(f"[평가] 어서션이 부정형에 쏠려 있다 (부정 {neg} 대 "
                         f"양성 {pos}). 부정형만 있으면 '아무것도 안 함' 이 "
                         "만점이다. 양성 어서션을 섞는다.")
            if not re.search(r"기준선|baseline|without_skill|대조군", blob):
                w.append("[평가] 기준선 비교가 안 보인다. 스킬을 끈 팔과 "
                         "비교하지 않으면 스킬이 기여했는지 모른다.")
            if not re.search(r"조악한|caveman|두 줄|최소 스킬|minimal arm", blob):
                w.append("[평가] 조악한 대조군이 안 보인다. 두 줄짜리 스킬로 "
                         "같은 결과가 나오면 본문과 스크립트는 과잉이다. "
                         "비용은 토큰 세 번이다.")
            # 자극 하나당 디렉터리 하나로 보는 근사다. fixtures/ 처럼
            # 자극이 아닌 디렉터리는 뺀다.
            stim = len([p for p in evals.iterdir() if p.is_dir()
                        and p.name not in ("fixtures", "results", "scripts",
                                           "prompts", "__pycache__")])
            if 0 < stim < 5:
                w.append(f"[평가] 자극이 {stim}개로 보인다 (디렉터리 수로 센 "
                         "근사다). 5개 미만이면 검정력이 부족하다. 결과에 이 "
                         "사실을 적는다. 합격도 실패도 아니다.")

    # ---------- 라이선스 ----------
    has_fm_lic = bool(fm.get("license"))
    has_file_lic = any((d / n).is_file()
                       for n in ("LICENSE", "LICENSE.txt", "LICENSE.md"))
    info["license"] = {"frontmatter": has_fm_lic, "file": has_file_lic}
    if not has_fm_lic:
        w.append("[라이선스] 프런트매터에 license 가 없다.")
    if not has_file_lic:
        w.append("[라이선스] 스킬 디렉터리에 LICENSE 파일이 없다. 스킬은 "
                 "디렉터리 단위로 복사되므로 저장소 루트에만 두면 떨어진다.")

    # ---------- 이 저장소의 문체 규칙 ----------
    mid = len(re.findall(r"(?<!\s)·(?!\s)", text))
    if mid:
        w.append(f"[문체] 가운데점이 {mid}개 있다. 쉼표로 바꾼다. "
                 "인용문 안이나 고유명사의 일부면 그대로 둔다.")

    # CommonMark 플랭킹 때문에 안 열리는 ** 를 찾는다.
    # 정규식으로는 여는 구분자와 닫는 구분자를 구별할 수 없어서 거짓 양성이
    # 많이 난다. 실제로 렌더링해서 <strong> 수를 센다.
    broken = bold_check(text)
    if broken is None:
        w.append("[문체] ** 강조 검사를 건너뛰었다. markdown-it-py 가 없다. "
                 "`pip install markdown-it-py` 로 넣으면 검사한다.")
    elif broken:
        w.append(f"[문체] 렌더링되지 않는 ** 강조가 {len(broken)}곳 있다 "
                 f"(줄 {', '.join(str(n) for n, _ in broken[:8])}). 닫는 ** 앞이 "
                 "구두점이고 뒤에 한글 조사가 붙으면 강조가 안 열린다. 조사를 "
                 "강조 안으로 넣거나 구두점을 밖으로 뺀다.")

    return e, w, info


def bold_check(text):
    """실제로 렌더링해서 안 열리는 ** 를 찾는다. 못 하면 None 을 낸다."""
    try:
        from markdown_it import MarkdownIt
    except ImportError:
        return None
    md = MarkdownIt("commonmark")
    out, fence = [], False
    for i, ln in enumerate(text.splitlines(), 1):
        if ln.lstrip().startswith("```"):
            fence = not fence
            continue
        if fence or ln.startswith("    ") or "**" not in ln:
            continue
        # 표는 셀 단위로 본다. 셀 경계를 넘는 강조는 어차피 안 열린다.
        cells = ln.split("|") if ln.strip().startswith("|") else [ln]
        for cell in cells:
            pairs = cell.count("**") // 2
            if pairs and md.render(cell.strip()).count("<strong>") < pairs:
                out.append((i, cell.strip()[:80]))
    return out


def main():
    ap = argparse.ArgumentParser(add_help=True)
    ap.add_argument("paths", nargs="+")
    ap.add_argument("--json", action="store_true")
    a = ap.parse_args()

    out, bad = [], 0
    for p in a.paths:
        e, w, info = check(p)
        out.append({"path": info.get("path", p), "errors": e, "warnings": w,
                    "info": info})
        if e:
            bad += 1

    if a.json:
        print(json.dumps({"results": out, "note":
                          "ERROR 는 규격 위반이다. WARN 은 이 저장소가 측정에서 "
                          "확인한 설계 문제이고, 근거를 적을 수 있으면 무시해도 "
                          "된다."}, ensure_ascii=False, indent=2))
        return 1 if bad else 0

    for r in out:
        i = r["info"]
        print(f"\n=== {i.get('name') or r['path']} ===")
        if "body_lines" in i:
            print(f"본문 {i['body_lines']}줄, 토큰 약 {i['body_tokens_approx']}개"
                  f" | description {i['description_len']}자"
                  f" | references {len(i.get('references', []))}개"
                  f" | scripts {len(i.get('scripts', []))}개"
                  f" | evals {'있음' if i.get('has_evals') else '없음'}")
        for x in r["errors"]:
            print(f"  ERROR  {x}")
        for x in r["warnings"]:
            print(f"  WARN   {x}")
        if not r["errors"] and not r["warnings"]:
            print("  통과. 남은 것은 평가 결과를 읽는 일이다.")

    print("\nERROR 는 규격 위반이라 고쳐야 한다.")
    print("WARN 은 전부 고쳐야 하는 목록이 아니다. 근거를 적을 수 있으면 "
          "무시해도 된다.")
    return 1 if bad else 0


if __name__ == "__main__":
    sys.exit(main())
