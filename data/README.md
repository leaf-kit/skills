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
