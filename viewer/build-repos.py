#!/usr/bin/env python3
"""원고에 나오는 `owner/repo` 를 모아 깃허브에 실재하는 것만 viewer/repos.json 에 적는다.

뷰어는 이 파일에 있는 이름만 링크로 건다. 정규식으로만 거르면 생김새가 같은 것들이
섞인다. 저장소 안의 경로(data/collect.sh), 디렉터리 이름(references/), 도메인
(agentskills.io/specification), 본문에서 줄인 이름(efij/awesome-...)이 전부
owner/repo 모양이다. 죽은 링크는 맨 텍스트보다 나쁘므로 실재 확인을 거친다.

이름이 바뀐 저장소는 깃허브가 알려주는 현재 이름으로 건다. 원고의 표기는 그대로 둔다.

    ./viewer/build-repos.py          원고를 훑어 다시 만든다
    ./viewer/build-repos.py --check  바뀐 게 있는지만 본다

gh CLI 로그인이 필요하다. 로그인 상태면 시간당 5000번까지 확인할 수 있다.
"""

import json
import re
import subprocess
import sys
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
OUT = ROOT / "viewer" / "repos.json"

# 원고에서 코드 조각만 본다. 맨 문장에서 긁으면 사람 이름과 날짜가 섞인다.
RE_CODE = re.compile(r"`([^`\n]+)`")
RE_REPO = re.compile(r"^[A-Za-z0-9][A-Za-z0-9-]*/[A-Za-z0-9._-]+$")
RE_FILE = re.compile(
    r"\.(md|sh|py|json|jsonl|tsv|csv|txt|ya?ml|toml|js|ts|html|css|lock|cfg|ini|png|svg)$",
    re.I,
)
RE_NOTREPO = re.compile(
    r"^(data|script|scripts|references|assets|evals|docs|doc|src|test|tests|spec|"
    r"hooks|plugins|commands|agents|skills|template|templates|output-styles|"
    r"external_plugins|examples|config)/",
    re.I,
)


def candidates():
    """원고 전체에서 저장소로 보이는 코드 조각을 모은다."""
    found = set()
    for path in sorted(ROOT.glob("**/*.md")):
        if ".git" in path.parts:
            continue
        for m in RE_CODE.finditer(path.read_text(encoding="utf-8")):
            s = m.group(1).strip()
            if "..." in s or re.search(r"[<>\s]", s):
                continue
            if not RE_REPO.match(s) or RE_FILE.search(s) or RE_NOTREPO.match(s):
                continue
            found.add(s)
    return sorted(found)


def resolve(name):
    """실재하면 현재 이름을, 없으면 None 을 낸다."""
    r = subprocess.run(
        ["gh", "api", f"repos/{name}", "--jq", ".full_name"],
        capture_output=True,
        text=True,
    )
    if r.returncode != 0:
        return None
    full = r.stdout.strip()
    return full or None


def main():
    check = "--check" in sys.argv
    names = candidates()
    print(f"후보 {len(names)}개를 확인한다", file=sys.stderr)

    with ThreadPoolExecutor(max_workers=8) as pool:
        resolved = list(pool.map(resolve, names))

    repos, dead = {}, []
    for name, full in zip(names, resolved):
        if full:
            repos[name] = full
        else:
            dead.append(name)

    print(f"실재 {len(repos)}개, 없음 {len(dead)}개", file=sys.stderr)
    for d in dead:
        print(f"  링크 안 검 — {d}", file=sys.stderr)

    data = {"repos": repos}
    text = json.dumps(data, ensure_ascii=False, indent=0, sort_keys=True) + "\n"

    if check:
        old = OUT.read_text(encoding="utf-8") if OUT.exists() else ""
        print("바뀐 것 없음" if old == text else "바뀌었다. 인자 없이 다시 돌린다.")
        return 0 if old == text else 1

    OUT.write_text(text, encoding="utf-8")
    print(f"{OUT.relative_to(ROOT)} 에 {len(repos)}개를 적었다", file=sys.stderr)
    return 0


if __name__ == "__main__":
    sys.exit(main())
