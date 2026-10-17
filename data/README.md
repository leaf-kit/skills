# 데이터

이 책의 모든 순위와 숫자는 이 디렉터리의 출력에서 나온다. 본문에 숫자를 손으로 적지 않는다.

**스냅샷은 월 단위로 쌓는다.** 이 생태계는 전체가 1년 안쪽이고 하루에 1,000개 넘게 스타가 붙는 저장소가 있다. 한 시점의 순위만으로는 "지금 올라오는 것"과 "한때 터진 것"을 구분할 수 없다.

## 구조

```
data/
├── collect.sh                 수집
├── classify.sh                스킬 저장소 판정
├── compare.py                 스냅샷 비교 (순위 변동)
├── taxonomy.json              분류 체계와 저장소 배정
├── latest -> snapshots/2026-10
└── snapshots/
    └── 2026-10/
        ├── stars.tsv          수집 원본
        ├── classified.tsv     판정 결과
        ├── categories.tsv     MECE 분류 결과
        └── meta.json          수집 메타
```

**스냅샷 디렉터리 이름이 날짜를 담으므로 파일명에는 날짜를 쓰지 않는다.** 정확한 수집일은 `meta.json`의 `collected_at`에 있다.

`latest` 심링크는 항상 최신 스냅샷을 가리킨다. 본문은 날짜가 박힌 경로를 쓰고, 스크립트는 `latest`를 쓴다.

## 수집 절차

```bash
gh auth login                 # 인증 필요

./collect.sh                  # 이번 달 스냅샷으로 수집
./collect.sh 2026-11          # 월 지정

./classify.sh 2026-11 150     # 상위 150개 판정
```

같은 달에 다시 돌리면 덮어쓴다. **월 단위로 하나만 남긴다.**

소요 시간은 수집이 몇 분, 판정이 상위 150개에 10분 내외다.

## 순위 변동 비교

스냅샷이 둘 이상 쌓이면 비교할 수 있다.

```bash
./compare.py 2026-10 2026-11
./compare.py 2026-10 2026-11 --top 50
./compare.py 2026-10 2026-11 --md > ../part5/05-changes.md
```

내는 것은 다섯 가지다.

| 항목 | 왜 보나 |
|---|---|
| 신규 진입 | 새로 올라온 영역이 어디인가 |
| 이탈 | 식은 영역이 어디인가 |
| 순위 상승 / 하락 | 절대 스타수로는 안 보이는 흐름 |
| 성장 속도 (일평균) | **지금** 주목받는 것 |
| **갱신이 멈춘 상위 저장소** | 마지막 푸시가 이전 수집일보다 오래된 것 |

마지막 항목이 실무적으로 가장 중요하다. 지식형 스킬은 수명이 짧아서 갱신이 멈추면 **없는 것보다 나빠진다** — 틀린 답을 자신 있게 낸다([4.2](../part4/02-three-types.md)).

## 스키마

### `stars.tsv`

| 열 | 내용 |
|---|---|
| `stars` | 스타 수 (수집 시점) |
| `full_name` | `owner/repo` |
| `created_at` | 저장소 생성 시각 (ISO 8601) |
| `pushed_at` | 마지막 푸시 시각 (ISO 8601) |
| `description` | 저장소 설명. 탭과 줄바꿈은 공백으로 치환 |

`full_name` 기준 중복 제거 후 `stars` 내림차순이다.

### `classified.tsv`

| 열 | 내용 |
|---|---|
| `stars`, `full_name`, `description` | 위와 같음 |
| `skill_md_count` | `SKILL.md` 파일 개수. `-1`은 트리 조회 실패 |
| `has_skills_dir` | `skills/` 디렉터리 존재 여부 |
| `truncated` | 트리가 커서 깃허브가 응답을 잘랐는지 |

`truncated`가 `true`면 `skill_md_count`가 과소 집계일 수 있다.

### `categories.tsv`

| 열 | 내용 |
|---|---|
| `code` | 범주 코드 (`A1` ~ `H`) |
| `category` | 대분류 |
| `subcategory` | 소분류 |
| `stars`, `full_name`, `skill_md` | 위와 같음 |

분류 축과 배정 규칙은 `taxonomy.json`과 [11.1](../part11/01-taxonomy.md)에 있다.

### `meta.json`

```json
{
  "snapshot": "2026-10",
  "collected_at": "2026-10-04",
  "counts": { "collected": 458, "classified": 150,
              "with_skill_md": 126, "categorized": 126 }
}
```

### `taxonomy.json`

분류 체계(37개 범주)와 저장소별 배정(126개)을 담는다. 다음 스냅샷에서 재사용하고, 새 저장소만 추가 배정하면 된다.

```bash
# 새 스냅샷에서 아직 배정 안 된 저장소 찾기
python3 -c "
import json,csv
t=json.load(open('taxonomy.json'))['assignments']
rows=[r for r in csv.DictReader(open('snapshots/2026-11/classified.tsv'),delimiter='\t')
      if int(r['skill_md_count'])>=1]
new=[r['full_name'] for r in rows if r['full_name'] not in t]
print(f'신규 배정 필요: {len(new)}개'); [print(' ',n) for n in new]
"
```

## 수집 현황

| 스냅샷 | 수집일 | 수집 | 판정 | SKILL.md 보유 | 분류 |
|---|---|---|---|---|---|
| 2026-10 | 2026-10-04 | 458 | 상위 150 | 126 | 126 |

## 트렌딩 보강 수집 (2026-10-17)

`collect.sh`의 토픽 검색 + 기준점 저장소 방식과 별도로, [github.com/trending](https://github.com/trending)에서 오늘 주목받는 저장소 중 에이전트 스킬 생태계에 속하는 것을 추가로 확인했다. 출력: [`snapshots/2026-10/trending-additions-2026-10-17.tsv`](snapshots/2026-10/trending-additions-2026-10-17.tsv).

**이 파일은 `stars.tsv`/`classified.tsv`/`categories.tsv`에 합치지 않았다.** 이유는 두 가지다.

1. 수집 방법이 다르다. `collect.sh`는 토픽 검색과 고정 저장소 목록을 쓰고, 이번 건은 트렌딩 페이지에서 사람이 골라 `gh api`로 각각 조회했다. 섞으면 "458개"라는 숫자가 재현 불가능해진다.
2. `classified.tsv`는 전체 458개를 스타수로 다시 정렬한 **상위 150위**다. 이번에 찾은 3개는 전부 5,445(현재 150위 컷오프)보다 훨씬 위라서, 엄밀히 합치려면 상위 150위를 처음부터 다시 뽑아야 한다. 그 작업은 다음 정식 재수집(`collect.sh` + `classify.sh`)으로 미룬다.

새로 확인한 저장소 3개다. 전부 `SKILL.md`와 `skills/` 디렉터리를 실제로 가지고 있는지 파일 트리로 확인했고, 폐기·아카이브 표시가 없는지 README 첫 문단도 확인했다(**정밀 리뷰는 아니다** — 분류만 했다).

| 스타 | 저장소 | 분류 | SKILL.md | 비고 |
|---|---|---|---|---|
| 281,670 | `affaan-m/ECC` | H 경계 — 스킬이 부속인 저장소 | 1,062개 | 에이전트 하니스가 본체, 스킬은 부속 기능 중 하나 |
| 53,611 | `HKUDS/CLI-Anything` | G1 스킬 생성과 변환 | 151개 | 기존 CLI 도구마다 스킬을 생성해 "agent-native"로 바꾸는 도구 |
| 12,046 | `cursor/plugins` | G4 수집과 큐레이션 | 165개 | Cursor 공식 플러그인 모음, 플러그인마다 스킬 포함 |

(수집 날짜: 2026-10-17)

**기존에 추적 중이던 저장소 5개도 트렌딩에 다시 떴다.** 2026-10-04 스냅샷과 비교한 스타수 변동이다. 참고용이며 `stars.tsv`는 고치지 않았다 — 458개 전체를 다시 조회해야 비교가 공정하기 때문이다.

| 저장소 | 2026-10-04 | 2026-10-17 | 변동 |
|---|---|---|---|
| `obra/superpowers` | 294,779 | 300,776 | +5,997 |
| `ruvnet/ruflo` | 73,778 | 75,719 | +1,941 |
| `K-Dense-AI/scientific-agent-skills` | 47,467 | 51,674 | +4,207 |
| `anthropics/claude-plugins-official` | 37,338 | 40,811 | +3,473 |
| `mksglu/context-mode` | 25,190 | 30,302 | +5,112 |

다음 정식 재수집(월 1회 데이터, 분기 1회 리뷰 — [9.6](../part9/06-update-policy.md))에서 이 3개를 포함해 상위 150위를 다시 뽑고, `taxonomy.json`에 정식 배정한다.

## 주의

**`skill_md_count`는 품질 지표가 아니다.** 선별에만 쓴다. 최대값 8,212개와 최소값 1개의 차이는 저장소 성격의 차이이지 품질의 차이가 아니다([4.3](../part4/03-scale.md)).

**0개로 집계돼도 스킬이 없다는 뜻이 아니다.** 세 경우가 있다.

| 경우 | 사례 |
|---|---|
| 실제로 스킬이 없다 (큐레이션, 규격, 도구) | `agentskills/agentskills` |
| 사람의 역량을 뜻하는 "skill"이 걸렸다 | `Snailclimb/JavaGuide` |
| **파일명이 규격을 따르지 않는다** | `Graphify-Labs/graphify` — 실제 12개 |

세 번째는 기계 판정으로 잡히지 않는다([8.9](../part8/09-code-understanding.md)).

**트리 조회는 기본 브랜치의 현재 상태만 본다.** 과거 구조는 잡히지 않는다.

**이전 스냅샷을 지우지 않는다.** 비교가 불가능해진다.
