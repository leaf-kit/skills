#!/usr/bin/env bash
# 트렌딩(github.com/trending 등)에서 발견한 저장소 1개를 월별 로그에 추가한다.
#
# collect.sh/classify.sh는 토픽 검색 + 기준점 저장소를 월 1회 정기적으로 훑는다.
# 이 스크립트는 그 사이에 개별적으로 발견한 저장소를 발견한 날짜(found_at)와
# 함께 월별 TSV에 덧붙인다. 기존 줄은 지우지 않는다 — 같은 달이면 계속 쌓는다.
#
# 분류 코드는 손으로 판단해서 인자로 넣는다(taxonomy.json의 축과 타이브레이크
# 규칙을 따른다). 이 스크립트가 분류를 대신 정하지 않는다.
#
# 사용법: ./add.sh <owner/repo> <category_code> [YYYY-MM] [source]
#   예:   ./add.sh cursor/plugins G4 2026-10 github.com/trending
# 출력:   <YYYY-MM>.tsv (이 디렉터리 기준)
# 요구사항: gh CLI 인증 완료, python3 (taxonomy.json 조회용)

set -euo pipefail

REPO="${1:?사용법: ./add.sh <owner/repo> <category_code> [YYYY-MM] [source]}"
CODE="${2:?분류 코드가 필요하다 (예: G4). ../taxonomy.json 의 categories 를 참고해라}"
MONTH="${3:-$(date +%Y-%m)}"
SOURCE="${4:-github.com/trending}"
DIR="$(cd "$(dirname "$0")" && pwd)"
OUT="${DIR}/${MONTH}.tsv"
TODAY="$(date +%Y-%m-%d)"

[ -f "$OUT" ] || printf 'stars\tfull_name\tcreated_at\tpushed_at\tskill_md_count\thas_skills_dir\ttruncated\tcategory_code\tcategory\tsubcategory\tdescription\tsource\tfound_at\n' > "$OUT"

if awk -F'\t' -v r="$REPO" 'NR>1 && $2==r { found=1 } END { exit !found }' "$OUT"; then
  echo "이미 있음: ${REPO} (${OUT}) — 중복으로 추가하지 않는다" >&2
  exit 1
fi

CAT_PAIR="$(python3 -c "
import json, sys
t = json.load(open('${DIR}/../taxonomy.json'))
cat = t['categories'].get('${CODE}')
if not cat:
    sys.exit('알 수 없는 분류 코드: ${CODE}')
print(cat[0] + '\t' + cat[1])
")" || { echo "분류 코드 조회 실패: ${CODE}" >&2; exit 1; }

IFS=$'\t' read -r CAT_LABEL SUBCAT_LABEL <<< "$CAT_PAIR"

echo "조회: ${REPO}" >&2
meta="$(gh api "repos/${REPO}" --jq '[.stargazers_count, .full_name, .created_at, .pushed_at, ((.description // "") | gsub("[\t\n]"; " "))] | @tsv')"

tree="$(gh api "repos/${REPO}/git/trees/HEAD?recursive=1" 2>/dev/null || echo '{}')"
[ "$tree" = "{}" ] && { echo "파일 트리 조회 실패: ${REPO}" >&2; exit 1; }

skill_md=$(printf '%s' "$tree" | jq '[.tree[]? | select(.path | test("(^|/)SKILL\\.md$"))] | length')
skills_dir=$(printf '%s' "$tree" | jq '[.tree[]? | select(.type == "tree") | select(.path | test("(^|/)skills$"))] | length > 0')
truncated=$(printf '%s' "$tree" | jq '.truncated // false')

[ "$skill_md" -lt 1 ] && echo "경고: SKILL.md가 0개다. 스킬 생태계에 속하는지 다시 확인해라 (규격 파일명 미준수 사례가 있다)." >&2

# meta는 stars,full_name,created_at,pushed_at,description 순이다. 출력 스키마는
# description을 끝이 아니라 중간에 두므로 awk로 재배열해서 붙인다.
printf '%s\t%s\t%s\t%s\n' "$meta" "$skill_md" "$skills_dir" "$truncated" | \
  awk -F'\t' -v code="$CODE" -v cat="$CAT_LABEL" -v subcat="$SUBCAT_LABEL" -v src="$SOURCE" -v found="$TODAY" \
    'BEGIN{OFS="\t"} { print $1,$2,$3,$4,$6,$7,$8,code,cat,subcat,$5,src,found }' >> "$OUT"

echo "추가됨: ${REPO} → ${OUT}" >&2
tail -n 1 "$OUT" >&2
