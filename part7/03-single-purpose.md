# 7.3 단일 목적 스킬의 힘

한 문제만 푸는 스킬이 번들과 겨룬다. 이 장은 그게 어떻게 가능한지를 세 저장소로 본다.

| 저장소 | 스타 | SKILL.md | 생성 | 푸시 | 라이선스 |
|---|---|---|---|---|---|
| `DietrichGebert/ponytail` | 152,859 | 번들(하네스별 사본 다수) | 2026-06-12 | 2026-10-03 | MIT |
| `blader/humanizer` | 53,730 | **1** | 2026-01-18 | 2026-09-28 | MIT |
| `ayghri/i-have-adhd` | 53,115 | 2 (사본 포함) | 2026-05-13 | 2026-09-19 | MIT |

(수집 날짜: 2026-10-04. 확인 수준: 정밀 리뷰)

셋 다 **출력의 성격을 바꾸는 스킬**이다. 특정 작업을 수행하는 게 아니라 에이전트가 일하는 태도를 바꾼다.

## ponytail — 112일에 15만 스타

생태계에서 가장 빠르게 성장한 저장소다. 일평균 1,364개로 2위(`superpowers`, 819)의 1.7배다([0.2](../part0/02-why-stars.md)).

README 부제가 이렇다.

> 그는 아무 말도 하지 않는다. 한 줄을 쓴다. 그게 작동한다.

### description — 5요소를 다 갖춘 사례

전문이다. 줄바꿈만 정리했다.

> Forces the laziest solution that actually works, simplest, shortest, most minimal. Channels a senior dev who has seen everything: question whether the task needs to exist at all (YAGNI), reach for the standard library before custom code, native platform features before dependencies, one line before fifty. **Supports intensity levels: lite, full (default), ultra.** Use on ANY coding task: writing, adding, refactoring, fixing, reviewing, or designing code, and choosing libraries or dependencies. Also use whenever the user says **"ponytail", "be lazy", "lazy mode", "simplest solution", "minimal solution", "yagni", "do less", or "shortest path"**, or complains about **over-engineering, bloat, boilerplate, or unnecessary dependencies**. **Do NOT use for** non-coding requests (general knowledge, prose, translation, ...)

[3.2](../part3/02-description.md)에서 처방한 다섯 요소가 전부 있다.

| 요소 | 해당 부분 |
|---|---|
| 무엇을 하는가 | 작동하는 가장 게으른 해법을 강제한다 |
| 어떻게 판단하는가 | YAGNI, 표준 라이브러리 우선, 네이티브 기능 우선, 한 줄 우선 |
| 언제 쓰는가 | **모든** 코딩 작업 — 작성, 추가, 리팩터, 수정, 리뷰, 설계, 의존성 선택 |
| 키워드 | "ponytail", "be lazy", "lazy mode", "simplest solution", "yagni", "do less", "shortest path" |
| 제외 조건 | 비코딩 요청(일반 지식, 산문, 번역) |

두 가지가 특히 영리하다.

**불만 표현을 트리거로 썼다.** `complains about over-engineering, bloat, boilerplate, unnecessary dependencies`다. 사용자가 스킬 이름을 모르고 "이거 왜 이렇게 복잡해?"라고만 해도 걸린다. [1.5](../part1/05-triggering.md)에서 "사용자가 실제로 쓰는 말"을 모으라고 한 것의 가장 좋은 사례다 — 요청이 아니라 **불만**을 키워드로 넣었다.

**강도 수준을 `description`에 넣었다.** `lite, full (default), ultra`다. 스킬이 한 가지 세기로만 작동하지 않고, 사용자가 조절할 수 있다는 사실을 트리거 단계에서 알린다.

### 엔지니어링 수준

112일에 15만 스타가 붙은 이유를 설명할 때 이 부분을 빼기 어렵다.

```
.agents/  .claude-plugin/  .clinerules/  .codex-plugin/  .cursor/
.devin-plugin/  .grok-plugin/  .kiro/  .openclaw/  .opencode/
.qoder-plugin/  .qoder/  .windsurf/
benchmarks/  commands/  docs/  examples/  hooks/
ponytail-mcp/  scripts/  skills/  tests/  assets/
AGENTS.md  README.md  README.ko.md  README.es.md
gemini-extension.json  opencode.json  plugin.json  plugin.yaml
package.json  after-install.md  CONTRIBUTING.md
```

[1.4](../part1/04-boundaries.md)에서 구분한 다섯 수단을 한 저장소에서 다 쓴다 — 스킬, MCP 서버(`ponytail-mcp/`), 훅(`hooks/`), 플러그인(`plugin.json`), 명령(`commands/`).

README 배지가 "works with 20 agents"다. npm 패키지로도 배포하고 릴리스 버전을 관리한다.

### 벤치마크 — 세 팔 비교

```
benchmarks/
├── agentic/{run.py, judge.py, tasks.py, complete.py}
├── arms/
│   ├── baseline.js          기준선 (스킬 없음)
│   ├── caveman.js           조악한 대조군
│   ├── caveman-SKILL.md
│   └── ponytail.js          스킬 적용
├── behavior.{js,yaml}
├── correctness.{js,test.js}
├── loc.{js,test.js}
├── promptfooconfig.gemini.yaml
├── promptfooconfig.gpt.yaml
└── promptfooconfig.gpt-newest.yaml
```

**`caveman` 팔이 이 설계의 핵심이다.**

[3.7](../part3/07-evals.md)에서 "기준선 없는 평가는 평가가 아니다"라고 했다. 그런데 기준선 하나만 두면 남는 질문이 있다 — 스킬이 좋아서 결과가 나아진 것인가, 아니면 **아무 스킬이나 붙여도 달라지는 것인가.**

조악한 대조군을 두면 그 질문에 답한다. `caveman-SKILL.md`는 같은 방향의 지시를 조악하게 쓴 스킬로 읽힌다. `ponytail`이 `caveman`보다 나으면 설계가 기여한 것이고, 비슷하면 "간결하게 쓰라고 말하기만 해도 되는" 것이다.

`loc.js`도 중요하다. 코드 줄 수를 측정한다. "가장 게으른 해법"이라는 주장을 **직접 셀 수 있는 숫자**로 잰다([2.1](../part2/01-criteria.md)의 검증 가능성). 방법론형 스킬의 주관성 문제를 측정 가능한 대리 지표로 우회했다.

세 모델(Gemini, GPT, GPT-newest)에서 돌리는 것도 드물다. 한 모델에서만 재면 그 모델에 과적합된 스킬인지 알 수 없다.

### 한국어 README가 있다

`README.ko.md`와 `README.es.md`가 있다. 현지화가 시작됐다는 증거다([5.4](../part5/04-patterns.md)). 마크다운이므로 번역 비용이 낮다.

## humanizer — 파일 하나로 5만 스타

| 항목 | 값 |
|---|---|
| `SKILL.md` | 1개 (루트) |
| 크기 | 32,348바이트 |
| 줄 수 | 397 |
| 번들 | 없음 |

`description`이 이렇다.

> Rewrite AI-sounding text so it reads like the writer **without changing what it says.** Use when editing or reviewing prose for AI tells: not-X-but-Y contrasts, one-line closers, staged openers, forced triads, dashes everywhere, inflated claims, sales language, stock AI words, bold labels, or filler. **Based on Wikipedia's "Signs of AI writing."**

세 가지가 눈에 띈다.

**제약을 먼저 적었다.** "말하는 내용을 바꾸지 않고"다. 교정 스킬의 가장 큰 위험이 내용을 바꾸는 것인데, 그 금지선이 `description`에 있다.

**패턴 이름을 열 개 나열했다.** `not-X-but-Y contrasts`, `one-line closers`, `staged openers`, `forced triads`가 트리거 키워드다. 사용자가 "이 글 대구가 너무 많아"라고 하면 걸린다.

**외부 근거를 밝혔다.** 위키백과의 "Signs of AI writing"에 기반했다. 판정 기준이 주관적인 영역에서 외부 근거를 대는 방식이고, [3.4](../part3/04-references.md)에서 다룬 "주관적 판단임을 인정한다"와 같은 방향이다. 저자의 취향이 아니라 공개된 목록을 쓴다는 선언이다.

### 점진적 공개를 쓰지 않았다

397줄 32KB가 한 파일에 들어 있다. 트리거될 때마다 32KB가 전부 읽힌다.

`cloudflare/security-audit-skill`과 비교하면 차이가 선명하다([6.6](../part6/06-cloudflare.md)). 그쪽도 단일 스킬인데 참조 파일 14개로 쪼갰다. 공격 분류별로 나눠서, 웹 감사에서 메모리 안전성 문서를 읽지 않는다.

`humanizer`의 패턴 목록을 `references/`로 내리면 비용이 크게 줄 여지가 있다. 모든 교정 작업에 열 가지 패턴 전부가 필요하지는 않다.

**다만 반론이 가능하다.** 글 교정은 문장을 훑으면서 여러 패턴을 동시에 보는 작업이다. 조건부로 읽는 구조가 맞지 않을 수 있다. 어느 쪽인지는 측정해야 알 수 있고, 이 저장소에는 측정이 없다.

### 평가가 없다

주관적 영역이라 어렵지만 불가능하지 않다. [3.7](../part3/07-evals.md)에서 다룬 금지선 어서션이 쓸 수 있다.

```
"원문의 사실 내용이 바뀌지 않았다"
"원문에 없던 주장을 추가하지 않았다"
"사용자 특유의 말투를 격식체로 통일하지 않았다"
```

첫 번째가 `description`이 선언한 제약("말하는 내용을 바꾸지 않고")을 그대로 측정한다. **스킬이 자기 약속을 지키는지 재는 어서션**이고, 만들기 어렵지 않다.

## i-have-adhd — 출력 형식을 바꾸는 스킬

| 항목 | 값 |
|---|---|
| 스타 | 53,115 |
| 구조 | `skills/i-have-adhd/` + `.cursor/skills/i-have-adhd/` |

설명이 "코딩 에이전트가 **답을 묻어 버리지 않게** 하는 스킬. ADHD 친화적 출력."이다.

### 푸는 문제

에이전트의 출력은 보통 과정을 먼저 쓰고 결론을 나중에 쓴다. 긴 설명 끝에 답이 있으면 찾기 어렵다.

이 스킬은 **결론을 앞에 놓게** 만든다. 작업을 바꾸는 게 아니라 전달 방식을 바꾼다.

### 왜 5만 스타인가

세 가지로 보인다.

**결핍이 보편적이다.** 긴 출력에서 답을 못 찾는 경험은 거의 모든 사용자가 한다. 특정 도메인이나 도구에 묶이지 않는다.

**이름이 설명을 대신한다.** `i-have-adhd`는 기능이 아니라 사용자의 상태를 이름으로 썼다. "나는 이런 사람이다"로 말하면 설명이 필요 없다.

**효과가 즉시 보인다.** 출력 형식이 바뀌는 것은 첫 응답에서 확인된다. 방법론형 스킬의 효과는 몇 주 뒤에 알게 되는데, 이건 바로 안다. **확인이 쉬우면 추천하기도 쉽다.**

### 다중 하네스 설치

`skills/`와 `.cursor/skills/`에 같은 스킬이 있다. 작은 저장소도 다중 하네스를 지원한다. 상위권 저장소들의 공통 전략이다.

## 세 저장소에서 읽히는 것

### 단일 목적이 번들을 이기는 조건

| 조건 | `ponytail` | `humanizer` | `i-have-adhd` |
|---|---|---|---|
| 결핍이 보편적인가 | ○ 모든 코딩 | ○ 모든 글 | ○ 모든 출력 |
| 한 문장으로 설명되나 | ○ | ○ | ○ (이름만으로) |
| 효과가 즉시 보이나 | ○ (줄 수) | ○ (문장) | ○ (형식) |
| 도메인에 묶이나 | ✕ | ✕ | ✕ |

네 조건이 다 겹친다. **보편적 결핍 + 한 문장 설명 + 즉시 확인 가능 + 도메인 비의존**이 단일 목적 스킬이 터지는 조합이다.

빅테크 공식 번들이 이 조건을 못 맞춘다. `google/skills`는 Google Cloud 사용자만, `microsoft/skills`는 Azure 사용자만 해당한다([6.8](../part6/08-others.md)).

### 태도를 바꾸는 스킬이라는 범주

셋 다 특정 작업을 수행하지 않는다. 에이전트가 **어떻게 하는가**를 바꾼다.

| 저장소 | 바꾸는 것 |
|---|---|
| `ponytail` | 해법의 복잡도 |
| `humanizer` | 글의 문체 |
| `i-have-adhd` | 출력의 구조 |

[4.2](../part4/02-three-types.md)의 세 유형으로는 방법론형이지만, 개발 방법론(`superpowers`)과 성격이 다르다. 개발 방법론은 순서를 정하고, 이것들은 **기본값을 바꾼다.**

이 범주가 생태계 상위권에 몰려 있다. `Leonxlnx/taste-skill`(92,250, "AI에게 좋은 취향을 준다"), `ayghri/i-have-adhd`(53,105)가 같은 성격이다.

### 평가 수준이 갈린다

| 저장소 | 평가 |
|---|---|
| `ponytail` | 세 팔 비교 + 세 모델 + 줄 수 측정 |
| `humanizer` | 없음 |
| `i-have-adhd` | 확인되지 않음 |

같은 범주에서 한 저장소만 측정한다. 그리고 그 저장소가 가장 빠르게 성장했다 — 다만 **인과를 주장할 수 없다.** 벤치마크를 읽고 스타를 누르는 사람은 드물다. 벤치마크가 있다는 사실은 저자가 엄격하다는 신호이고, 그 엄격함이 스킬 품질에도 적용됐을 가능성이 높다는 정도로 읽는 것이 맞다.

---

다음 장: [7.4 큐레이션 저장소의 경제학](04-awesome-lists.md)
