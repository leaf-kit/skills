#!/usr/bin/env bash
# 스킬 저장소 판정 스크립트
#
# collect.sh가 모은 목록은 토픽 기반이라 오탐이 섞인다. 일반 프레임워크나
# 면접 자료 저장소도 "skills" 토픽을 달 수 있다. 이 스크립트는 각 저장소의
# 파일 트리를 실제로 조회해서 스킬 저장소인지 기계적으로 판정한다.
#
# 판정 신호 3개:
#   skill_md_count  — SKILL.md 파일 개수 (스킬을 직접 담고 있다는 증거)
#   has_skills_dir  — skills/ 또는 .claude/skills/ 디렉터리 존재
#   truncated       — 트리가 너무 커서 깃허브가 응답을 잘랐는지 (판정 신뢰도)
#
# 사용법: ./classify.sh <YYYY-MM> [상위 N개]
# 입력:   snapshots/<YYYY-MM>/stars.tsv
# 출력:   snapshots/<YYYY-MM>/classified.tsv

set -euo pipefail

SNAP="${1:?사용법: ./classify.sh <YYYY-MM> [N]}"
LIMIT="${2:-150}"
DIR="$(dirname "$0")/snapshots/${SNAP}"
SRC="${DIR}/stars.tsv"
OUT="${DIR}/classified.tsv"
[ -f "$SRC" ] || { echo "없음: $SRC — 먼저 ./collect.sh ${SNAP}" >&2; exit 1; }

printf 'stars\tfull_name\tskill_md_count\thas_skills_dir\ttruncated\tdescription\n' > "$OUT"

n=0
while IFS=$'\t' read -r stars name created pushed desc; do
  n=$((n + 1))
  [ "$n" -gt "$LIMIT" ] && break

  tree="$(gh api "repos/${name}/git/trees/HEAD?recursive=1" 2>/dev/null || echo '{}')"

  if [ "$tree" = "{}" ]; then
    printf '%s\t%s\t-1\t-1\t-1\t%s\n' "$stars" "$name" "$desc" >> "$OUT"
    echo "  [조회 실패] $name" >&2
    continue
  fi

  skill_md=$(printf '%s' "$tree" | jq '[.tree[]? | select(.path | test("(^|/)SKILL\\.md$"))] | length')
  skills_dir=$(printf '%s' "$tree" | jq '[.tree[]? | select(.type == "tree") | select(.path | test("(^|/)skills$"))] | length > 0')
  truncated=$(printf '%s' "$tree" | jq '.truncated // false')

  printf '%s\t%s\t%s\t%s\t%s\t%s\n' "$stars" "$name" "$skill_md" "$skills_dir" "$truncated" "$desc" >> "$OUT"
  echo "  [$n/$LIMIT] $name — SKILL.md ${skill_md}개, skills/ ${skills_dir}" >&2
done < <(tail -n +2 "$SRC")

echo "완료: ${OUT}" >&2
