#!/usr/bin/env python3
"""이 저장소의 분류 데이터를 조회한다.

스타수로 정렬하지 않는다. 이 저장소의 전제가 "스타수는 품질이 아니라
주목을 잰다"이기 때문이다. 기본 정렬은 카테고리 순이고, 스타수는
참고값으로만 보여 준다.

사용법:
    ./query.py --list                     대분류와 소분류 전체
    ./query.py --category A3              한 소분류의 저장소
    ./query.py --search "코드 리뷰"        키워드로 소분류 찾기
    ./query.py --repo trailofbits/skills  저장소 하나 조회
    ./query.py --stale                    갱신이 멈춘 저장소
"""
import argparse
import csv
import json
import pathlib
import sys

HERE = pathlib.Path(__file__).resolve().parent
ROOT = HERE.parent.parent.parent          # skills/skill-selector/scripts -> repo root
DATA = ROOT / "data"
SNAP = DATA / "snapshots"

CHAPTER = {"A": "part11/02-code.md", "B": "part11/03-writing.md",
           "C": "part11/04-visual.md", "D": "part11/05-platform.md",
           "E": "part11/06-work.md", "F": "part11/07-agent.md",
           "G": "part11/08-meta.md", "H": "part11/09-boundary.md"}


def latest():
    if not SNAP.exists():
        sys.exit(f"없음: {SNAP}")
    dirs = sorted(d for d in SNAP.iterdir() if d.is_dir())
    if not dirs:
        sys.exit("스냅샷이 없다")
    return dirs[-1]


def load(snap):
    cats = list(csv.DictReader(open(snap / "categories.tsv", encoding="utf-8"),
                               delimiter="\t"))
    stars = {}
    with open(snap / "stars.tsv", encoding="utf-8") as f:
        r = csv.reader(f, delimiter="\t")
        next(r)
        for x in r:
            if len(x) >= 5:
                stars[x[1]] = {"created": x[2][:10], "pushed": x[3][:10],
                               "desc": x[4]}
    meta = {}
    mp = snap / "meta.json"
    if mp.exists():
        meta = json.loads(mp.read_text(encoding="utf-8"))
    return cats, stars, meta


def show(rows, stars, note=True):
    for r in rows:
        s = stars.get(r["full_name"], {})
        print(f"  [{r['code']}] {int(r['stars']):>7,}★  {r['full_name']}")
        print(f"        {r['category']} / {r['subcategory']}"
              f"   SKILL.md {r['skill_md']}   푸시 {s.get('pushed','?')}")
        if s.get("desc"):
            print(f"        {s['desc'][:92]}")
    if rows and note:
        ch = CHAPTER.get(rows[0]["code"][0])
        if ch:
            print(f"\n  → 리뷰: {ch}")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--list", action="store_true")
    ap.add_argument("--category")
    ap.add_argument("--search")
    ap.add_argument("--repo")
    ap.add_argument("--stale", action="store_true")
    a = ap.parse_args()

    snap = latest()
    cats, stars, meta = load(snap)
    collected = meta.get("collected_at", snap.name)
    print(f"스냅샷 {snap.name} (수집일 {collected}) — 스타수는 이 시점 값이다.\n")

    if a.list or not any([a.category, a.search, a.repo, a.stale]):
        seen = {}
        for r in cats:
            seen.setdefault(r["code"], [r["category"], r["subcategory"], 0])
            seen[r["code"]][2] += 1
        for code in sorted(seen):
            cat, sub, n = seen[code]
            print(f"  {code:<3} {cat:<16} {sub:<22} {n:>3}개")
        print(f"\n  합계 {len(cats)}개 / 전체 지도: part11/01-taxonomy.md")
        return

    if a.category:
        rows = [r for r in cats if r["code"] == a.category.upper()]
        if not rows:
            print(f"  '{a.category}' 범주가 없다. --list 로 확인한다.")
            return
        show(rows, stars)
        return

    if a.search:
        q = a.search.lower()
        rows = [r for r in cats
                if q in r["subcategory"].lower() or q in r["category"].lower()
                or q in r["full_name"].lower()
                or q in stars.get(r["full_name"], {}).get("desc", "").lower()]
        if not rows:
            print(f"  '{a.search}' 로 찾은 것이 없다.")
            print("  수집 데이터에 없을 수 있다. 150위 밖은 기계 판정을 하지 않았다.")
            return
        print(f"  {len(rows)}개\n")
        show(rows, stars, note=False)
        return

    if a.repo:
        rows = [r for r in cats if a.repo.lower() in r["full_name"].lower()]
        if not rows:
            print(f"  '{a.repo}' 가 분류 데이터에 없다.")
            print("  150위 밖이거나 SKILL.md 가 0개로 집계된 저장소일 수 있다.")
            return
        show(rows, stars)
        return

    if a.stale:
        rows = [r for r in cats
                if stars.get(r["full_name"], {}).get("pushed", "9") < collected[:7]]
        rows.sort(key=lambda r: stars[r["full_name"]]["pushed"])
        print(f"  수집일({collected}) 기준 한 달 이상 갱신이 없는 저장소 {len(rows)}개")
        print("  지식형이면 사실이 낡았을 수 있다. part4/02-three-types.md 참조\n")
        for r in rows:
            print(f"  {stars[r['full_name']]['pushed']}  [{r['code']}] "
                  f"{int(r['stars']):>7,}★  {r['full_name']}")


if __name__ == "__main__":
    main()
