# 트렌딩 보강 수집

`../collect.sh`와 `../classify.sh`는 토픽 6개 + 기준점 저장소를 **월 1회** 정기적으로 훑는다. 이 디렉터리는 그 사이에 [github.com/trending](https://github.com/trending) 등에서 개별적으로 발견한 저장소를 **계속** 쌓아 두는 곳이다.

## 왜 따로 두는가

본문 숫자(458개, 126개)는 `collect.sh`/`classify.sh`의 토픽 검색 + 고정 저장소 목록으로만 만든다. 트렌딩 페이지는 검색 방식이 다르고(사람이 매일 바뀌는 목록에서 고른다), 상위 150위를 전체 재정렬 없이 건드리면 "458개"가 재현 불가능해진다.

그래서 여기 쌓인 것은 **정식 데이터셋에 아직 안 들어간 후보**다. 다음 분기 정식 재수집에서 `collect.sh`의 기준점 저장소 목록(`PINNED`)에 옮기고, `taxonomy.json`에 정식 배정하면 본문 숫자에 들어간다.

## 파일 규칙

```
data/trending/
├── add.sh        저장소 1개를 월별 TSV에 추가하는 스크립트
├── 2026-10.tsv    2026년 10월에 발견한 것 (계속 누적)
└── 2026-11.tsv    새 달이 되면 새 파일 (만들어지면)
```

- **월 1개 파일.** 같은 달에 여러 번 찾으면 같은 파일에 행을 추가한다. 새 달이 되면 새 파일을 만든다 — `collect.sh`의 스냅샷 월 규칙과 같다.
- **지우지 않는다.** 기존 행을 고치거나 지우지 않는다. 틀렸으면 새 행으로 정정하고 이유를 남긴다.
- **숫자는 스크립트에서만 나온다.** 아래 `add.sh`를 쓴다. 손으로 TSV 줄을 쓰지 않는다.

## 사용법

```bash
./add.sh <owner/repo> <category_code> [YYYY-MM] [source]

# 예
./add.sh cursor/plugins G4 2026-10 github.com/trending
```

`category_code`는 `../taxonomy.json`의 `categories`를 보고 사람이 판단해서 넣는다 — 스크립트가 분류를 대신 정하지 않는다. 분류 축과 타이브레이크 규칙은 [11.1](../../part11/01-taxonomy.md)에 있다.

스크립트가 하는 일:

1. `gh api repos/<repo>`로 스타수, 생성일, 마지막 푸시, 설명을 가져온다.
2. `git/trees/HEAD?recursive=1`로 파일 트리를 조회해서 `SKILL.md` 개수와 `skills/` 디렉터리 존재 여부를 기계적으로 확인한다(`classify.sh`와 같은 방식).
3. 이미 있는 저장소면 중복 추가를 막는다.
4. 결과를 `<YYYY-MM>.tsv`에 한 줄 추가한다. `found_at` 열에 발견한 날짜가 남는다.

**스크립트가 하지 않는 일.** 폐기 여부, README 첫 문단 확인, 설명 작성은 사람이 한다. 추가한 뒤에는 [`../README.md`의 갱신 점검표](../README.md) B항(폐기·이전 표시)을 직접 확인하고, 상세 설명은 책 쪽 [`trending/`](../../trending/README.md)에 쓴다.

## 스키마

| 열 | 내용 |
|---|---|
| `stars`, `full_name`, `created_at`, `pushed_at`, `description` | `stars.tsv`와 같음 |
| `skill_md_count`, `has_skills_dir`, `truncated` | `classified.tsv`와 같음 |
| `category_code`, `category`, `subcategory` | `categories.tsv`와 같음, 사람이 판단 |
| `source` | 어디서 발견했는지 (예: `github.com/trending`) |
| `found_at` | 발견한 날짜. 수집일이 아니라 **발견일**이다 — 저장소 스타수는 그 순간의 값이다 |

## 정식 데이터셋으로 옮기는 기준

| 조건 | 처리 |
|---|---|
| 다음 분기 정식 재수집 때 여전히 존재하고 활성 | `collect.sh`의 `PINNED`에 추가, `taxonomy.json`에 정식 배정 |
| 그 사이 폐기·아카이브됨 | 이 로그에 남기고 책 쪽에 "폐기됨"으로 표시, 정식 데이터셋에는 넣지 않는다 |
| 찾고 보니 스킬 저장소가 아니었음 (오탐) | 지우지 않고 행 끝에 사유를 덧붙인 정정 행을 추가한다 |
