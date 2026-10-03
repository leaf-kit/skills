# 7.5 지역 생태계

수집한 458개 중 **54개(11.8%)가 CJK 설명을 쓴다.** 중국어, 한국어, 일본어권 저장소가 생태계의 1할을 넘는다.

이 장은 그 저장소들이 영어권과 무엇이 다른지를 본다.

## 주요 저장소

| 스타 | 저장소 | 언어 | 성격 |
|---|---|---|---|
| 69,766 | `code-yeongyu/oh-my-openagent` | — | 키워드 기반 에이전트 제어 |
| 26,312 | `JimLiu/baoyu-skills` | 중국어 | 개인 스킬 묶음 |
| 21,127 | `KKKKhazix/khazix-skills` | 중국어 | AI 스킬 모음 |
| 17,053 | `tradecatlabs/vibe-coding-cn` | 중국어 | Vibe Coding 교재 |
| 16,929 | `wanshuiyin/Auto-claude-code-research-in-sleep` | 중국어 | 마크다운 전용 자동 연구(189개) |
| 12,719 | `ConardLi/garden-skills` | 중국어 | 개인 스킬 모음 |
| 8,256 | `jnMetaCode/superpowers-zh` | 중국어 | **`superpowers` 중국어 확장판** |
| 7,864 | `HKUSTDial/Supervisor-Skills` | 중국어 | 박사 지도 경험을 스킬로 |
| 7,505 | `anbeime/skill` | 중국어 | 스킬 상점(자동 수집) |
| 7,254 | `WenyuChiou/awesome-agentic-ai-zh` | 3개 언어 | 학습 로드맵 |
| 7,233 | `zenstory-ai/oh-story-claudecode` | 중국어 | 웹소설 집필 |
| 6,162 | `jihe520/MathModelAgent` | 중국어 | 수학 모델링 |
| **5,835** | **`epoko77-ai/im-not-ai`** | **한국어** | **한국어 AI 글 윤문** |
| 5,144 | `libukai/awesome-agent-skills` | 중국어 | 큐레이션 |
| 5,037 | `didilili/ai-agents-from-zero` | 중국어 | 에이전트 입문 교재 |
| 4,068 | `tmstack/awesome-persona-skills` | 중국어 | 페르소나 스킬 |
| 3,937 | `KKKKhazix/human-writing` | 중국어 | **중국어 AI 글 사람화** |
| 3,400 | `jangviktor-web/nihaixia` | 중국어 | 한의학 에이전트 |
| 2,469 | `zenstory-ai/drama-skills` | 중국어 | AI 단편극, 만화 제작 |

(수집 날짜: 2026-10-04. 확인 수준: `epoko77-ai/im-not-ai` 정밀 리뷰, 나머지 요약 리뷰)

## 같은 문제가 언어별로 다시 풀린다

가장 중요한 발견이다. **AI가 쓴 글을 사람 글처럼 고치는 스킬이 세 언어로 각각 존재한다.**

| 저장소 | 언어 | 스타 | 생성 |
|---|---|---|---|
| `blader/humanizer` | 영어 | 53,730 | 2026-01-18 |
| `epoko77-ai/im-not-ai` | 한국어 | 5,835 | 2026-04-24 |
| `KKKKhazix/human-writing` | 중국어 | 3,937 | 2026-08-05 |

생성 순서가 영어 → 한국어 → 중국어다.

### 왜 번역으로 안 되는가

AI 글의 흔적이 **언어마다 다르다.**

`blader/humanizer`가 잡는 영어 패턴이다.

```
not-X-but-Y contrasts, one-line closers, staged openers,
forced triads, dashes everywhere, inflated claims,
sales language, stock AI words, bold labels, filler
```

`epoko77-ai/im-not-ai`의 설명이 잡는 한국어 패턴이다.

> detects and rewrites **translationese**, **mechanical parallelism**, and 71 other AI tells

`translationese`(번역체)가 영어 목록에 없다. 있을 수 없다 — 영어 원문에 번역체가 생기지 않는다. 한국어 AI 글에서는 "~에 대한 이해를 높이다", "~라고 할 수 있다" 같은 번역체 명사구가 주된 흔적이다.

반대로 `dashes everywhere`(엠 대시 남용)는 한국어에서 문제가 되지 않는다. 한국어 글에서 엠 대시를 쓰는 관습이 약하다.

**겹치는 것도 있다.** `forced triads`(억지 삼단 나열)와 `mechanical parallelism`(기계적 대구)은 같은 문제다. `blader/humanizer`의 `not-X-but-Y contrasts`가 한국어의 "A가 아니라 B입니다" 구조와 대응한다.

그래서 세 저장소의 관계는 번역이 아니다. **공통 패턴 일부 + 언어별 고유 패턴**이고, 고유 패턴 때문에 각 언어에서 다시 만들어야 한다.

### 71개라는 숫자

`im-not-ai`의 설명이 "71가지 다른 AI 흔적"을 잡는다고 적는다. `blader/humanizer`는 열 가지를 나열한다.

숫자가 많은 쪽이 낫다는 뜻은 아니다. 패턴을 세분하면 개수가 늘어난다. 다만 **71개를 한 파일에 넣으면 비용이 크다.** `humanizer`가 397줄 32KB를 한 파일에 둔 문제([7.3](03-single-purpose.md))가 더 커진다.

`im-not-ai`는 다르게 풀었다. 아래에서 본다.

## im-not-ai — 한국어 저장소 정밀 리뷰

| 항목 | 값 |
|---|---|
| 스타 | 5,835 |
| 생성 | 2026-04-24 |
| 푸시 | 2026-09-26 |
| 라이선스 | MIT |
| `SKILL.md` | 7개 (하네스 사본 포함, 실질 4개) |

### 스킬을 역할로 쪼갰다

```
skills/humanize/SKILL.md            범용
skills/humanize-korean/SKILL.md     한국어 특화
skills/humanize-scan/SKILL.md       탐지만
skills/humanize-redo/SKILL.md       다시 하기
extras/skills/commit-ko/SKILL.md    한국어 커밋 메시지
```

**`humanize-scan`이 별도 스킬인 점이 설계의 핵심이다.**

글을 고치는 일과 문제를 찾는 일을 분리했다. 사용자가 "어디가 문제인지만 알려 줘"라고 할 때와 "고쳐 줘"라고 할 때는 다른 요청이다. 하나로 합치면 탐지만 원하는 사용자가 고쳐진 글을 받는다.

이것이 교정 스킬에서 과잉 적용을 막는 구조적 장치다([3.3](../part3/03-body.md)). 사용자가 탐지 경로를 고를 수 있으면, 스킬이 멋대로 고치는 일이 줄어든다.

`humanize-redo`도 흥미롭다. 결과가 마음에 안 들 때 다시 하는 경로를 스킬로 뒀다. 사용자가 "다시 해 줘"라고 하면 같은 스킬이 같은 방식으로 다시 할 가능성이 높은데, 별도 스킬이면 다른 전략을 쓸 수 있다.

### 범용과 언어 특화를 나눴다

`humanize`와 `humanize-korean`이 따로 있다. [3.4](../part3/04-references.md)에서 다룬 도메인별 분리를 **언어로** 적용한 것이다.

```
cloud-deploy/              →  humanize/
├── SKILL.md (공통)            ├── SKILL.md (공통 패턴)
└── references/               └── humanize-korean (한국어 고유)
    ├── aws.md
    └── gcp.md
```

영어 글을 고칠 때 번역체 패턴 71개를 읽지 않는다. 비용이 줄고, 예시가 범위를 좁히는 문제도 해결된다([2.5](../part2/05-examples.md)).

### 저장소 운영 수준

```
.claude-plugin/  .githooks/  .github/
codex/  copilot/  GEMINI.md  gemini-extension.json
agents/  assets/  commands/  docs/  extras/  scripts/  skills/  tests/
CLAUDE.md  CONTRIBUTORS.md  INSTALL.md  RELEASING.md
install.sh  uninstall.sh  update.sh  plugin.json
README.md (한국어)  README.en.md (영어)
```

**`uninstall.sh`가 있다.** 설치 스크립트를 제공하는 저장소는 많은데, 제거 스크립트를 제공하는 경우는 드물다. 스킬이 여러 디렉터리에 복사되는 구조에서 수동 제거는 번거롭고, 남은 파일이 트리거 충돌을 일으킨다.

`RELEASING.md`와 `.githooks/`가 있다. 릴리스 절차와 깃 훅을 문서화했다. 개인 저장소에서 드문 수준이다.

`tests/`도 있다. 다만 기준선 비교인지는 확인하지 못했다. `[확인 필요: tests/ 내용이 기준선 비교를 포함하는지]`

### 4개 하네스를 지원한다

`skills/`(Claude Code), `codex/`, `copilot/`, `GEMINI.md`다. 상위권 저장소들의 공통 전략이고([7.1](01-superpowers.md), [7.3](03-single-purpose.md)), 5천 스타 규모에서도 같은 선택을 한다.

### 왜 영어판의 10분의 1인가

`blader/humanizer`(53,730)의 11%다.

설계는 더 정교하다. 스킬을 역할로 쪼갰고, 범용/언어 특화를 나눴고, 제거 스크립트와 릴리스 절차가 있고, 4개 하네스를 지원한다. `humanizer`는 파일 하나다.

차이는 **대상 인구**다. 깃허브에서 한국어로 글을 쓰는 사용자가 영어로 쓰는 사용자보다 적다.

[6.2](../part6/02-anthropic-others.md)에서 본 것과 같은 구조다. `anthropics/k12-teacher-skills`(544)가 평가 루브릭을 포함하고 도메인 전문가와 공동 개발했는데도 스타가 544개인 이유와 같다. **스타수는 품질이 아니라 대상 인구를 따라간다.**

## superpowers-zh — 현지화가 포크로 일어난다

| 항목 | 값 |
|---|---|
| 스타 | 8,256 |
| 설명 | "AI 프로그래밍 초능력 · 중국어 확장판 — superpowers(250k+ ⭐) 완전 한화" |
| `SKILL.md` | 21개 (원본 15개보다 많다) |

**원본보다 스킬이 6개 많다.** 단순 번역이 아니라 확장이다.

이것이 가능한 이유는 `obra/superpowers`가 MIT이기 때문이다([7.1](01-superpowers.md)). 그리고 스킬이 **소프트웨어가 아니라 마크다운**이라서 번역 비용이 낮다. 코드를 포크하면 유지보수가 갈라지지만, 마크다운을 번역하면 그냥 다른 문서가 된다.

`anthropics/skills`가 `Proprietary`인 것과 대조된다([6.1](../part6/01-anthropic-skills.md)). 공식 스킬의 중국어판, 한국어판 포크가 수집 데이터에 보이지 않는 것은 라이선스와 무관하지 않을 수 있다. `[확인 필요: 공식 스킬 라이선스가 포크를 제약하는 범위]`

## 영어권에 없는 범주

중국어권 저장소에서만 보이는 유형들이다.

### 페르소나 스킬

`tmstack/awesome-persona-skills`(4,068)의 설명이 이렇다.

> 同事.skill、老板.skill、前任.skill、自己.skill、永生.skill、女...

동료, 상사, 전 연인, 자기 자신, 영생을 스킬로 만든 목록이다. `xixu-me/awesome-persona-distill-skills`(4,672)도 같은 범주다 — "페르소나를 중심에 둔 에이전트 스킬 큐레이션"이다.

두 저장소가 **같은 날(2026-04-06) 생성됐다.** [7.4](04-awesome-lists.md)에서 다룬 큐레이션 중복의 사례이고, 범주 자체가 짧은 기간에 유행했다는 신호다.

영어권 수집 목록에 이 범주가 보이지 않는다. 역할극 스킬 자체는 있을 수 있지만, 이 정도 규모로 묶인 저장소는 없다.

### 창작 스킬

| 저장소 | 스타 | 대상 |
|---|---|---|
| `zenstory-ai/oh-story-claudecode` | 7,233 | 중국 웹소설(网文) |
| `zenstory-ai/drama-skills` | 2,469 | AI 단편극, 만화 |

중국 웹소설은 분량과 연재 구조가 고유한 장르다. 영어권 소설 집필 스킬로 대체되지 않는다.

### 교육 과정

| 저장소 | 스타 |
|---|---|
| `tradecatlabs/vibe-coding-cn` | 17,053 |
| `didilili/ai-agents-from-zero` | 5,037 |
| `WenyuChiou/awesome-agentic-ai-zh` | 7,254 |

"입문부터 숙달까지" 형태의 교재가 스킬 저장소로 분류된다. 영어권에서는 이런 내용이 블로그나 유료 강의로 가는데, 중국어권에서는 깃허브 저장소가 된다.

### 도메인 전문성 증류

| 저장소 | 스타 | 대상 |
|---|---|---|
| `HKUSTDial/Supervisor-Skills` | 7,864 | 박사 지도 10년 경험 |
| `jangviktor-web/nihaixia` | 3,400 | 한의학(倪海厦 교학 자료) |

**특정 인물이나 분야의 전문성을 스킬로 증류한다.** `Supervisor-Skills`의 설명이 "박사 지도교수 10년 연구 경험을 바로 호출할 수 있는 AI 기능으로 정련했다"다.

[4.4](../part4/04-meta-skills.md)에서 다룬 변환형 메타스킬과 같은 방향이지만, 입력이 책이나 문서가 아니라 **한 사람의 경험**이다. `titanwings/distilly`(25,269)가 "그들이 생각하는 방식을 재사용 가능한 스킬로 증류한다"고 한 것과 같은 개념이다.

이 범주의 위험은 검증 불가능성이다. "10년 경험"이 정확히 담겼는지 확인할 방법이 없다. 그리고 지식형이므로 수명이 짧다([4.2](../part4/02-three-types.md)).

## 지역 생태계에서 읽히는 것

### 규격이 언어 장벽을 낮췄다

스킬은 마크다운이다. 코드가 아니므로 번역이 쉽고, 포크가 가볍다. 54개 저장소가 11.8%를 차지하는 이유다.

반대로 **소프트웨어 생태계에서는 이런 비율이 나오기 어렵다.** 라이브러리를 번역할 수는 없다. 문서만 번역된다.

### 같은 문제가 언어마다 다시 풀린다

AI 글 교정이 세 언어로 각각 있다. 번역으로 해결되지 않는 영역이 있기 때문이다.

이것이 [9.5 중복과 포화](../part9/05-saturation.md)에서 다룰 중복과 **다른 종류의 중복**이다. 메모리 스킬 일곱 개는 같은 문제를 같은 조건에서 푸는 중복이고, 언어별 교정 스킬은 조건이 다른 재구현이다. 전자는 낭비이고 후자는 필요하다.

### 대상 인구가 스타수를 정한다

| 저장소 | 설계 수준 | 스타 |
|---|---|---|
| `blader/humanizer` | 단일 파일, 점진적 공개 없음 | 53,730 |
| `epoko77-ai/im-not-ai` | 역할별 분리, 제거 스크립트, 4개 하네스 | 5,835 |

**설계가 더 정교한 쪽이 10분의 1이다.** 스타수를 품질 지표로 쓸 수 없는 또 하나의 사례다([0.2](../part0/02-why-stars.md)).

한국어, 중국어권 저장소를 찾으려면 스타수 순위를 내려가야 한다. 이 책이 54개를 따로 센 이유다 — 영어권 상위 30개만 보면 생태계의 1할이 안 보인다.

---

다음 장: [7.6 개인이 빅테크를 앞지르는 이유](06-why-individuals-win.md)
