#!/usr/bin/env bash
# 스킬 저장소 스타수 수집 스크립트
#
# 이 책의 모든 순위는 이 스크립트의 출력에서 나온다. 숫자를 손으로 적지 않는다.
# 요구사항: gh CLI 인증 완료 (gh auth status)
#
# 사용법:
#   ./collect.sh                 # 이번 달 스냅샷으로 수집
#   ./collect.sh 2026-11         # 스냅샷 월 지정 (YYYY-MM)
#
# 출력: snapshots/<YYYY-MM>/stars.tsv
#       (stars, full_name, created_at, pushed_at, description)
#
# 같은 달에 다시 돌리면 덮어쓴다. 월 단위로 하나만 남긴다.

set -euo pipefail

SNAP="${1:-$(date +%Y-%m)}"
DIR="$(dirname "$0")/snapshots/${SNAP}"
mkdir -p "$DIR"
OUT="${DIR}/stars.tsv"
TODAY="$(date +%Y-%m-%d)"
TMP="$(mktemp)"
trap 'rm -f "$TMP"' EXIT

# 1) 토픽 기반 수집 — 스킬 생태계가 실제로 쓰는 토픽
TOPICS=(
  agent-skills
  claude-skills
  claude-code-skills
  claude-agent-skills
  claude-code-plugins
  skills
)

# 2) 직접 지정 — 토픽을 달지 않았지만 생태계의 기준점이 되는 저장소
PINNED=(
  anthropics/skills
  anthropics/claude-code
  anthropics/claude-plugins-official
  anthropics/defending-code-reference-harness
  anthropics/launch-your-agent
  openai/skills
  google/skills
  google/agents-cli
  microsoft/skills
  microsoft/SkillOpt
  microsoft/skill-recorder
  microsoft/azure-skills
  cloudflare/skills
  cloudflare/security-audit-skill
  cloudflare/agent-skills-discovery-rfc
  github/awesome-copilot
  github/copilot-plugins
  alibaba/skill-up
  alibaba/open-code-review
  vercel/vercel-plugin
  obra/superpowers
)

echo "수집 시작: 스냅샷 ${SNAP} (${TODAY})" >&2

for t in "${TOPICS[@]}"; do
  echo "  topic:${t}" >&2
  gh search repos --topic="$t" --sort=stars --limit=100 \
    --json fullName,stargazersCount,createdAt,pushedAt,description \
    --jq '.[] | [.stargazersCount, .fullName, .createdAt, .pushedAt, ((.description // "") | gsub("[\t\n]"; " "))] | @tsv' \
    >> "$TMP" 2>/dev/null || echo "    (실패: topic:${t})" >&2
done

for r in "${PINNED[@]}"; do
  echo "  repo:${r}" >&2
  gh api "repos/${r}" \
    --jq '[.stargazers_count, .full_name, .created_at, .pushed_at, ((.description // "") | gsub("[\t\n]"; " "))] | @tsv' \
    >> "$TMP" 2>/dev/null || echo "    (실패: ${r})" >&2
done

# full_name(2번 필드) 기준 중복 제거 후 스타수 내림차순
{
  printf 'stars\tfull_name\tcreated_at\tpushed_at\tdescription\n'
  sort -u -t$'\t' -k2,2 "$TMP" | sort -t$'\t' -k1,1nr
} > "$OUT"

N=$(($(wc -l < "$OUT") - 1))
cat > "${DIR}/meta.json" <<JSON
{
  "snapshot": "${SNAP}",
  "collected_at": "${TODAY}",
  "collector": "collect.sh",
  "counts": { "collected": ${N} }
}
JSON
echo "완료: ${OUT} (${N}개 저장소)" >&2
echo "다음: ./classify.sh ${SNAP} 150" >&2
