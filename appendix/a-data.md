# 부록 A. 데이터 수집 스크립트와 재현 방법

이 책의 모든 숫자는 이 부록의 절차로 다시 만들 수 있다. **숫자가 책과 다르면 오류가 아니라 날짜 차이다.**

## 요구사항

| 항목 | 내용 |
|---|---|
| `gh` CLI | 인증 완료 (`gh auth status`) |
| `jq` | `gh` 설치에 포함 |
| Python 3 | 가공, 분석에 쓴다 (수집 자체는 셸만으로 된다) |

인증이 필요한 이유는 두 가지다. 미인증 요청은 시간당 60회로 제한되고, 수집에 수백 회가 필요하다.

```bash
gh auth login
gh auth status
```

## 절차

```bash
cd data

# 1. 스타수 수집 — 토픽 6개 검색 + 기준점 21개 직접 조회
./collect.sh                     # 오늘 날짜로
./collect.sh 2026-10-04          # 날짜 지정

# 2. 스킬 저장소 판정 — 상위 N개의 파일 트리 조회
./classify.sh snapshots/2026-10/stars.tsv 150
```

소요 시간은 1단계가 몇 분, 2단계가 상위 150개에 10분 내외다.

**이전 수집분을 지우지 않는다.** `snapshots/<YYYY-MM>/stars.tsv`가 나란히 남아야 변동을 볼 수 있다.

## collect.sh — 무엇을 모으나

### 토픽 6개

```
agent-skills
claude-skills
claude-code-skills
claude-agent-skills
claude-code-plugins
skills
```

토픽마다 스타수 내림차순 100개까지 가져온다.

**`skills` 토픽을 넣은 것이 중요한 결정이었다.** 범위가 가장 넓고 오탐도 가장 많지만, 빼면 `obra/superpowers`가 목록에서 사라진다. 전체 1위 저장소다. 넣고 거르는 쪽을 택했다([5.1](../part5/01-collection.md)).

### 기준점 저장소 21개

토픽을 달지 않았지만 생태계의 기준이 되는 저장소를 직접 지정한다.

```
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
```

빅테크 공식 저장소는 토픽 관리에 소홀한 경우가 많다. 토픽만 믿으면 정작 중요한 것이 빠진다.

**이 목록에 빠진 것이 있다.** 리뷰 대상 중 `NVIDIA/SkillSpector`, `NVIDIA/skills`, `dotnet/skills`, `android/skills`, `trailofbits/skills`, `agentskills/agentskills`는 토픽 검색으로만 들어왔다. 토픽이 바뀌면 빠질 수 있으므로 다음 갱신 때 기준점 목록에 추가하는 것이 안전하다.

### 출력 — `snapshots/<YYYY-MM>/stars.tsv`

| 열 | 내용 |
|---|---|
| `stars` | 스타 수 (수집 시점) |
| `full_name` | `owner/repo` |
| `created_at` | 생성 시각 (ISO 8601) |
| `pushed_at` | 마지막 푸시 시각 (ISO 8601) |
| `description` | 저장소 설명. 탭, 줄바꿈은 공백으로 치환 |

`full_name` 기준 중복 제거 후 `stars` 내림차순 정렬이다.

2026-10-04 수집분은 **458개 저장소**다.

## classify.sh — 무엇을 판정하나

저장소마다 파일 트리를 조회해서 세 가지를 기록한다.

| 열 | 내용 |
|---|---|
| `skill_md_count` | `SKILL.md` 파일 개수. `-1`은 트리 조회 실패 |
| `has_skills_dir` | `skills/` 디렉터리 존재 여부 |
| `truncated` | 트리가 커서 깃허브가 응답을 잘랐는지 |

`truncated`가 `true`면 `skill_md_count`가 과소 집계일 수 있다. 판정 신뢰도 표시로 쓴다.

### 2026-10-04 판정 결과

```
판정 대상 150개 / SKILL.md 보유 126개 / 미보유 24개 / 조회 실패 0개
```

### `SKILL.md` 개수 분포

| 개수 | 저장소 수 |
|---|---|
| 1개 | 29 |
| 2~10개 | 29 |
| 11~100개 | 55 |
| 100개 초과 | 13 |

중앙값 12개다.

## 가공 예시

TSV이므로 `awk`나 Python으로 바로 다룬다.

### 상위 N개 보기

```bash
awk -F'\t' 'NR>1 && NR<=31 {printf "%3d. %8d  %-45s %s\n", NR-1, $1, $2, substr($5,1,50)}' \
  snapshots/2026-10/stars.tsv
```

### 성장 속도 (일평균)

```bash
awk -F'\t' 'NR>1 {
  split($3, d, "T"); split(d[1], p, "-");
  days = (2026 - p[1])*365 + (10 - p[2])*30 + (4 - p[3]);
  if (days < 1) days = 1;
  printf "%8d\t%6d\t%7.1f\t%s\n", $1, days, $1/days, $2
}' snapshots/2026-10/stars.tsv | sort -t$'\t' -k3,3nr | head -25
```

경과일 계산이 근사다(월 30일 고정). **경과일 90일 미만 저장소의 일평균은 순위 근거로 쓰지 않는다**([9.1](../part9/01-star-traps.md)).

### 생성 연월 분포

```bash
awk -F'\t' 'NR>1 {k[substr($3,1,7)]++} END {for (m in k) printf "%s  %d\n", m, k[m]}' \
  snapshots/2026-10/stars.tsv | sort
```

### 푸시 최신성

```bash
awk -F'\t' 'NR>1 {
  d=substr($4,1,7)
  if(d>="2026-09") a++; else if(d>="2026-07") b++; else if(d>="2026-04") c++; else e++
} END {printf "2026-09 이후: %d / 2026-07~08: %d / 2026-04~06: %d / 그 이전: %d\n", a,b,c,e}' \
  snapshots/2026-10/stars.tsv
```

### CJK 설명 저장소

바이트 범위 비교는 로케일에 따라 잘못 동작한다. Python을 쓴다.

```python
import csv, re
cjk = re.compile(r'[぀-ヿ一-鿿가-힯]')
rows = []
with open('snapshots/2026-10/stars.tsv') as f:
    r = csv.reader(f, delimiter='\t'); next(r)
    for row in r:
        if len(row) >= 5 and cjk.search(row[4]):
            rows.append((int(row[0]), row[1]))
rows.sort(reverse=True)
print(f"{len(rows)}개 / 458개")
```

2026-10-04 기준 **54개**(11.8%)다([7.5](../part7/05-regional.md)).

### 라이선스 분포

```python
import csv, subprocess, concurrent.futures as cf
from collections import Counter

names = []
with open('snapshots/2026-10/classified.tsv') as f:
    r = csv.reader(f, delimiter='\t'); next(r)
    for row in r:
        if int(row[2]) >= 1: names.append(row[1])
        if len(names) >= 60: break

def lic(n):
    out = subprocess.run(['gh','api',f'repos/{n}','--jq','.license.spdx_id // "NONE"'],
                         capture_output=True, text=True, timeout=30)
    return (n, out.stdout.strip() or 'NONE')

with cf.ThreadPoolExecutor(8) as ex:
    res = list(ex.map(lic, names))
for k, v in Counter(l for _, l in res).most_common():
    print(f"{v:3d}  {k}")
```

2026-10-04 기준 결과다([9.4](../part9/04-licensing.md)).

| 라이선스 | 저장소 수 |
|---|---|
| MIT | 37 |
| Apache-2.0 | 12 |
| NOASSERTION | 5 |
| 없음(NONE) | 4 |
| AGPL-3.0 | 2 |

## 개별 저장소 조사

리뷰할 때 쓴 명령들이다.

### 메타데이터

```bash
gh api repos/OWNER/REPO --jq \
  '"스타 \(.stargazers_count) | 생성 \(.created_at[0:10]) | 푸시 \(.pushed_at[0:10]) | 라이선스 \(.license.spdx_id // "없음")"'
```

### 스킬 목록

```bash
gh api "repos/OWNER/REPO/git/trees/HEAD?recursive=1" --jq \
  '.tree[] | select(.path | test("SKILL\\.md$")) | .path'
```

**`SKILL.md`가 0개로 나와도 포기하지 않는다.** 파일명 변형을 확인한다.

```bash
gh api "repos/OWNER/REPO/git/trees/HEAD?recursive=1" --jq \
  '.tree[] | select(.path | test("skill"; "i")) | .path'
```

`Graphify-Labs/graphify`(123,488)가 `graphify/skill-<도구>.md`를 쓴다. 이 점검 없이는 전체 8위 저장소를 놓친다([8.9](../part8/09-code-understanding.md)).

### 번들 크기 측정

```bash
gh api "repos/anthropics/skills/git/trees/HEAD?recursive=1" --jq \
  '.tree[] | select(.type=="blob") | select(.path | startswith("skills/")) | "\(.size)\t\(.path)"' > sk.tsv

awk -F'\t' '{split($2,p,"/"); s=p[2]; tot[s]+=$1; if($2 ~ /SKILL\.md$/) main[s]=$1; n[s]++}
END {for (x in tot) printf "%-24s %9d %9d %6.1fx %6d\n", x, main[x], tot[x], tot[x]/main[x], n[x]}' \
  sk.tsv | sort -k2 -nr
```

[1.3](../part1/03-progressive-disclosure.md)과 [6.1](../part6/01-anthropic-skills.md)의 465배 표가 이 명령의 출력이다.

### 본문 줄 수

```bash
gh api "repos/OWNER/REPO/contents/skills/NAME/SKILL.md" --jq '.content' | base64 -d | wc -l
```

**줄 수와 바이트를 같이 본다.** `claude-api`는 603줄 101,724바이트로 줄당 169바이트이고, `skill-creator`는 485줄 33,168바이트로 줄당 68바이트다. 줄 수가 비슷해도 실제 크기는 3배 차이 난다.

### 파일 내용 비교

같은 스킬이 복사됐는지 확인한다.

```bash
A=$(gh api repos/anthropics/skills/contents/skills/brand-guidelines/SKILL.md --jq '.content' | base64 -d | md5)
B=$(gh api repos/ComposioHQ/awesome-claude-skills/contents/brand-guidelines/SKILL.md --jq '.content' | base64 -d | md5)
[ "$A" = "$B" ] && echo "동일" || echo "다름"
```

[9.4](../part9/04-licensing.md)에서 `ComposioHQ`가 공식 스킬을 바이트 단위로 복사하고 `LICENSE.txt`를 함께 옮긴 것을 이 방법으로 확인했다.

### 평가 디렉터리 확인

```bash
gh api "repos/OWNER/REPO/git/trees/HEAD?recursive=1" --jq \
  '.tree[] | select(.path | test("(eval|test|benchmark)"; "i")) | .path'
```

**"평가가 없다"고 쓰기 전에 반드시 돌린다.** 저장소 설명과 `README`에 평가 언급이 없어도 디렉터리가 있는 경우가 있다 — `obra/superpowers`의 `tests/`와 `addyosmani/agent-skills`의 `evals/`가 그렇다([9.6](../part9/06-update-policy.md)).

## 알려진 한계

정직하게 적어 둔다.

| 한계 | 내용 |
|---|---|
| 토픽 의존 | 토픽을 안 단 저장소는 기준점 목록에 없으면 빠진다 |
| 상위 150개만 판정 | 그 아래는 기계 판정이 없다 |
| 기본 브랜치의 현재 상태만 | 과거 구조는 잡히지 않는다 |
| `truncated` 저장소 | `skill_md_count`가 과소 집계일 수 있다 |
| 파일명 변형 | `SKILL.md`가 아닌 스킬 파일은 0으로 집계된다 |
| 경과일 근사 | 월 30일 고정 계산이다 |
| 라이선스 | 깃허브 식별 결과이고 원문 검토가 아니다 |
| **보안 스캔 없음** | 리뷰 대상에 `SkillSpector`를 돌리지 않았다 |

마지막 줄이 가장 큰 공백이다. 스킬 26.1%에 취약점이 있다는 통계가 있는 생태계에서([9.3](../part9/03-supply-chain.md)) 리뷰서가 스캔을 하지 않은 것은 한계다. 다음 갱신의 과제로 남겼다([9.6](../part9/06-update-policy.md)).

## 수집 현황

| 날짜 | 수집 저장소 | 판정 대상 | SKILL.md 보유 |
|---|---|---|---|
| 2026-10-04 | 458 | 상위 150 | 126 |

---

다음: [부록 B 저장소 색인](b-index.md)
