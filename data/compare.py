#!/usr/bin/env python3
"""스냅샷 두 개를 비교해 순위 변동을 낸다.

이 생태계는 전체가 1년 안쪽이고 하루에 1,000개 넘게 스타가 붙는 저장소가 있다.
한 시점의 순위만으로는 "지금 올라오는 것"과 "한때 터진 것"을 구분할 수 없다.
두 스냅샷을 비교해야 그게 보인다.

사용법:
    ./compare.py 2026-10 2026-11
    ./compare.py 2026-10 2026-11 --top 50
    ./compare.py 2026-10 2026-11 --md > ../part5/05-changes.md

출력:
    신규 진입 / 이탈 / 순위 상승 / 순위 하락 / 성장 속도 상위
"""
import argparse
import csv
import json
import pathlib
import sys
from datetime import date

ROOT = pathlib.Path(__file__).parent
SNAPDIR = ROOT / "snapshots"


def load(snap):
    d = SNAPDIR / snap
    src = d / "stars.tsv"
    if not src.exists():
        sys.exit(f"없음: {src}")
    rows = {}
    with open(src, encoding="utf-8") as f:
        r = csv.reader(f, delimiter="\t")
        next(r)
        for i, x in enumerate(r, 1):
            if len(x) < 5:
                continue
            rows[x[1]] = {
                "rank": i,
                "stars": int(x[0]),
                "created": x[2][:10],
                "pushed": x[3][:10],
                "desc": x[4],
            }
    meta = {}
    mp = d / "meta.json"
    if mp.exists():
        meta = json.loads(mp.read_text(encoding="utf-8"))
    return rows, meta


def days_between(a, b):
    ya, ma, da = (int(v) for v in a.split("-"))
    yb, mb, db = (int(v) for v in b.split("-"))
    return max((date(yb, mb, db) - date(ya, ma, da)).days, 1)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("old")
    ap.add_argument("new")
    ap.add_argument("--top", type=int, default=30, help="비교할 상위 N개 (기본 30)")
    ap.add_argument("--md", action="store_true", help="마크다운 표로 출력")
    a = ap.parse_args()

    old, om = load(a.old)
    new, nm = load(a.new)

    od = om.get("collected_at", a.old + "-01")
    nd = nm.get("collected_at", a.new + "-01")
    span = days_between(od, nd)

    entered = [n for n in new if n not in old and new[n]["rank"] <= a.top]
    left = [n for n in old if n not in new and old[n]["rank"] <= a.top]

    moved = []
    for n in new:
        if n in old:
            moved.append((old[n]["rank"] - new[n]["rank"], n))
    moved.sort(reverse=True)

    growth = []
    for n in new:
        if n in old:
            gained = new[n]["stars"] - old[n]["stars"]
            growth.append((gained / span, gained, n))
    growth.sort(reverse=True)

    # 유지가 끊긴 저장소 — 지식형이면 특히 중요하다
    stale = [
        (new[n]["stars"], n, new[n]["pushed"])
        for n in new
        if new[n]["rank"] <= a.top and new[n]["pushed"] < od
    ]
    stale.sort(reverse=True)

    P = print
    if a.md:
        P(f"# 순위 변동 — {a.old} → {a.new}\n")
        P(f"| 항목 | 값 |\n|---|---|")
        P(f"| 이전 수집 | {od} |")
        P(f"| 이번 수집 | {nd} |")
        P(f"| 간격 | {span}일 |")
        P(f"| 수집 저장소 | {len(old)} → {len(new)} |\n")
        P(f"## 신규 진입 (상위 {a.top})\n")
        P("| 순위 | 스타 | 저장소 |\n|---|---|---|")
        for n in sorted(entered, key=lambda x: new[x]["rank"]):
            P(f"| {new[n]['rank']} | {new[n]['stars']:,} | `{n}` |")
        P(f"\n## 이탈 (상위 {a.top}에서)\n")
        P("| 이전 순위 | 저장소 |\n|---|---|")
        for n in sorted(left, key=lambda x: old[x]["rank"]):
            P(f"| {old[n]['rank']} | `{n}` |")
        P("\n## 순위 상승\n")
        P("| 변동 | 저장소 | 스타 |\n|---|---|---|")
        for d, n in moved[:10]:
            if d > 0:
                P(f"| +{d} | `{n}` | {old[n]['stars']:,} → {new[n]['stars']:,} |")
        P("\n## 순위 하락\n")
        P("| 변동 | 저장소 | 스타 |\n|---|---|---|")
        for d, n in moved[-10:]:
            if d < 0:
                P(f"| {d} | `{n}` | {old[n]['stars']:,} → {new[n]['stars']:,} |")
        P(f"\n## 성장 속도 상위 (일평균)\n")
        P("| 일평균 | 증가 | 저장소 |\n|---|---|---|")
        for rate, gained, n in growth[:15]:
            P(f"| {rate:,.0f} | +{gained:,} | `{n}` |")
        if stale:
            P(f"\n## 갱신이 멈춘 상위 저장소\n")
            P(f"마지막 푸시가 이전 수집일({od})보다 오래됐다. "
              f"지식형이면 사실이 낡았을 수 있다.\n")
            P("| 스타 | 저장소 | 마지막 푸시 |\n|---|---|---|")
            for s, n, p in stale[:15]:
                P(f"| {s:,} | `{n}` | {p} |")
    else:
        P(f"=== {a.old}({od}) → {a.new}({nd}), {span}일 ===")
        P(f"수집: {len(old)} → {len(new)}\n")
        P(f"[신규 진입 상위 {a.top}] {len(entered)}개")
        for n in sorted(entered, key=lambda x: new[x]["rank"]):
            P(f"  {new[n]['rank']:>3}. {new[n]['stars']:>8,}  {n}")
        P(f"\n[이탈] {len(left)}개")
        for n in sorted(left, key=lambda x: old[x]["rank"]):
            P(f"  {old[n]['rank']:>3}. {n}")
        P("\n[순위 상승 10]")
        for d, n in moved[:10]:
            if d > 0:
                P(f"  +{d:>3}  {n}")
        P("\n[순위 하락 10]")
        for d, n in moved[-10:]:
            if d < 0:
                P(f"  {d:>4}  {n}")
        P("\n[성장 속도 상위 15 — 일평균]")
        for rate, gained, n in growth[:15]:
            P(f"  {rate:>8,.0f}/일  +{gained:>8,}  {n}")
        if stale:
            P(f"\n[갱신 멈춤 — 마지막 푸시가 {od} 이전]")
            for s, n, p in stale[:15]:
                P(f"  {s:>8,}  {p}  {n}")


if __name__ == "__main__":
    main()
