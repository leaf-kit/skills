# 7.2 addyosmani/agent-skills

| 항목 | 값 |
|---|---|
| 스타 | 100,755 |
| 생성 | 2026-02-15 |
| 마지막 푸시 | 2026-10-03 |
| 라이선스 | MIT |
| `SKILL.md` | 25개 |
| 일평균 | 440 |
| 유형 | 방법론형 |
| 확인 수준 | **정밀 리뷰** |

(수집 날짜: 2026-10-04)

트랙 A 4위다. 설명이 "AI 코딩 에이전트를 위한 **프로덕션 급** 엔지니어링 스킬"이다.

`obra/superpowers`(294,779)와 같은 유형이고 같은 영역을 다룬다. 두 저장소를 비교하면 방법론형 설계의 선택지가 보인다.

## 스킬 25개

```
api-and-interface-design          incremental-implementation
browser-testing-with-devtools     interview-me
ci-cd-and-automation              observability-and-instrumentation
code-review-and-quality           performance-optimization
code-simplification               planning-and-task-breakdown
constraint-driven-development     security-and-hardening
context-engineering               shipping-and-launch
debugging-and-error-recovery      source-driven-development
deprecation-and-migration         spec-driven-development
documentation-and-adrs            test-driven-development
doubt-driven-development          using-agent-skills
frontend-ui-engineering
git-workflow-and-versioning
idea-refine
```

## superpowers와의 차이

두 저장소의 이름 짓기 방식이 다르다.

| | `obra/superpowers` | `addyosmani/agent-skills` |
|---|---|---|
| 스킬 수 | 15 | 25 |
| 이름 형태 | 동명사 (`brainstorming`) | **명사구** (`api-and-interface-design`) |
| 축 | 활동 | **영역** |
| 예 | `writing-plans` | `planning-and-task-breakdown` |
| 예 | `systematic-debugging` | `debugging-and-error-recovery` |
| 예 | `requesting-code-review` + `receiving-code-review` | `code-review-and-quality` |

**`superpowers`는 순서를 담고, 이쪽은 영역을 담는다.**

`superpowers`의 `writing-plans` → `executing-plans`는 선후가 있다. 이쪽의 `planning-and-task-breakdown`은 단계가 아니라 주제다. `and`로 묶인 이름이 많은 것(`and-interface-design`, `and-automation`, `and-quality`, `and-error-recovery`, `and-adrs`, `and-versioning`, `and-instrumentation`, `and-hardening`)이 그 증거다.

### 어느 쪽이 나은가

트레이드오프가 있다.

**영역 중심의 장점:** 커버리지가 넓다. 25개가 `superpowers`의 15개보다 더 많은 주제를 덮는다. 성능 최적화, 관측성, 보안 강화, 문서화, ADR, 폐기, 마이그레이션은 `superpowers`에 없다.

**영역 중심의 단점:** 트리거 경계가 흐려진다. `code-review-and-quality` 하나가 `superpowers`의 두 스킬(요청/수신)을 덮으면, 리뷰를 요청하는 상황과 받는 상황에 같은 본문이 읽힌다. 그리고 `and`로 두 주제를 묶으면 `description`이 두 범위를 다 잡아야 한다([2.6](../part2/06-promotion.md)의 쪼갤 시점).

**활동 중심의 장점:** 트리거가 선명하고 순서가 지시에 들어 있다.

**활동 중심의 단점:** 활동으로 안 잡히는 영역이 빠진다. "보안 강화"는 활동이 아니라 관심사다.

25개가 100,755스타, 15개가 294,779스타다. 이것만으로 설계 우열을 말할 수 없다 — 생성일이 넉 달 차이이고(`superpowers` 2025-10-09, 이쪽 2026-02-15), 저자의 인지도도 다르다.

## 눈에 띄는 스킬 세 개

### doubt-driven-development

이름이 도발적이다. TDD, 명세 주도, 소스 주도, 제약 주도와 나란히 **의심 주도**가 있다.

```
constraint-driven-development
doubt-driven-development
source-driven-development
spec-driven-development
test-driven-development
```

`-driven-development` 접미사가 다섯 개다. **같은 형식으로 다섯 가지 개발 방식을 제공한다.**

이게 방법론형 번들에서 위험한 지점이다. [4.3](../part4/03-scale.md)에서 "방법론형은 마켓플레이스로 모이지 않는다. 방법론은 충돌하기 때문이다"라고 했다. 다섯 개의 `-driven-development`가 한 저장소에 있으면 **어느 것을 따를지 결정할 근거**가 필요하다.

`superpowers`는 `test-driven-development` 하나만 둔다. 선택을 저자가 했다. 이쪽은 선택지를 제공한다. 선택지를 주는 쪽이 유연하지만, 트리거 단계에서 다섯 개가 경쟁한다.

**이 저장소는 그 경쟁을 기계로 검사한다.** 아래 "평가 체계" 절에서 다룬다. 생태계에서 이 문제를 CI로 막는 유일한 저장소다.

### interview-me

사용자를 인터뷰하는 스킬로 읽힌다. [3.1](../part3/01-capture-intent.md)에서 다룬 의도 포착 — 에이전트가 사용자에게 물어서 요구를 끌어내는 일 — 을 스킬로 만든 것이다.

이 방향이 중요하다. 대부분의 스킬은 "에이전트가 무엇을 하는가"를 적는데, 이건 "**에이전트가 무엇을 묻는가**"를 적는다. 재료가 없을 때 조건을 늘리는 대신 재료를 묻는 전환([2.3](../part2/03-length-myth.md))이 스킬 형태로 구현된 사례다.

### context-engineering

컨텍스트 관리 자체를 스킬로 만들었다. 점진적 공개와 컨텍스트 비용([1.3](../part1/03-progressive-disclosure.md))을 다루는 영역이다.

메모리, 컨텍스트 저장소가 생태계에 여섯 개 넘게 있는 상황에서([5.3](../part5/03-rest.md)) 이 스킬은 다른 접근이다. 저장소를 따로 만드는 대신 번들 안의 한 스킬로 다룬다. `mksglu/context-mode`(25,190)가 같은 문제로 저장소 하나를 쓰는 것과 비교된다.

### using-agent-skills

`superpowers`의 `using-superpowers`와 같은 역할이다. **번들의 진입점을 스킬로 만들었다.** 두 저장소가 독립적으로 같은 설계에 도달했다.

25개가 각자 트리거를 경쟁하는 대신 하나가 조율한다. 번들 규모에서 반복적으로 나타나는 해법이고, `google/skills`가 `finding-google-skills`를 둔 것도 같은 방향이다.

## 평가 체계 — 카탈로그 전체를 검사한다

이 저장소의 가장 큰 기여다. `evals/` 디렉터리에 스킬 25개 전부에 대응하는 케이스 파일이 있다.

```
evals/
├── README.md
├── cases/          (스킬당 1개, 25개)
│   ├── code-simplification.json
│   ├── doubt-driven-development.json
│   └── ...
└── fixtures/       (스킬별 입력 자료)
    ├── api-and-interface-design/service-brief.md
    └── browser-testing-with-devtools/{index.html, server.js, README.md}
```

### 선행 연구를 밝혔다

`evals/README.md`가 무엇을 가져왔고 무엇을 추가했는지 적는다.

> `SKILL.md` 스킬을 평가하는 단일한 커뮤니티 표준은 없지만 두 접근이 앞선다.
>
> - **Anthropic의 skill-creator v2**는 스킬별 `evals.json`(프롬프트 + `expectations[]`, 트랜스크립트로 채점)과 설명의 트리거 정확도 테스트를 정의한다. 우리는 그 `evals.json` 스키마를 행동 계층에 채택하고 `kind` 필드 하나를 추가했다.
> - **Superpowers**(obra)는 bash + `claude -p` + 프롬프트 픽스처 + 채점 스크립트로 스킬을 테스트한다. 우리 행동 러너도 같은 헤드리스 `claude` 패턴을 따른다.
>
> **둘 다 제공하지 않는 것**은 다중 스킬 **카탈로그**에 대한 결정적이고 CI에서 안전한 검사다 — 각 스킬의 설명이 사용자가 실제로 쓰는 어휘를 담고 있는가, 그리고 두 스킬의 설명이 충돌하는가. 그게 Tier 2이고 이 저장소의 추가분이다.

생태계에 공통 평가 표준이 없다는 사실을 명시하고, 기존 접근 둘을 인용하고, 자기 기여를 한 문장으로 특정했다. **리뷰 대상 저장소 중에 이렇게 쓴 곳이 없다.**

### 3단 체계

| 티어 | 검사 내용 | 실행 | 비용 |
|---|---|---|---|
| 1. 구조 | 프런트매터, 이름, 필수 절, 명령 일치 | CI | 무료 |
| 2. **트리거, 라우팅** | 양성 프롬프트가 해당 스킬을 top-k에 올리는가 / 음성 프롬프트는 안 올리는가 / **두 설명이 근접 충돌하지 않는가** | CI | 무료 |
| 3. 행동 | 스킬을 따른 에이전트가 `expectations[]`를 만족하는가 | 필요시 | 토큰 |

Tier 2가 핵심이다. 설명에 대한 **어간 추출 TF-IDF**로 라우팅을 근사한다. README가 한계를 직접 적는다.

> Tier 2는 라우팅의 **어휘적 근사**다. 의미를 판단할 수 없다 — 그건 Tier 3의 일이다. 하지만 실제 트리거 버그를 지배하는 두 실패 모드를 잡는다. 사용자가 쓰는 어휘가 설명에 없는 경우(거짓 음성), 그리고 지나치게 넓은 설명이 올바른 스킬을 앞지르는 경우(거짓 양성). **Tier 2 실패는 보통 설명을 고치라는 뜻이고, 평가를 고치라는 뜻이 아니다.**

이 책 [3.2](../part3/02-description.md)에서 "과소와 과잉을 따로 본다"고 한 것, [1.5](../part1/05-triggering.md)에서 "경쟁 스킬에 밀림"을 실패 유형으로 꼽은 것이 전부 여기서 측정된다.

그리고 **비용 구조가 영리하다.** 의미 판단은 토큰을 쓰고 느리므로 필요할 때만 돌린다. 어휘 수준의 충돌 검사는 결정적이고 공짜라서 모든 커밋에서 돈다. 트리거 버그의 대부분이 어휘 문제이므로, 공짜 검사가 대부분을 잡는다.

### 음성 케이스에 `owner`가 있다

`code-simplification.json`의 일부다.

```json
{
  "skill_name": "code-simplification",
  "trigger": {
    "positive": [
      {"prompt": "This function works but it is way too clever, simplify it without changing behavior", "top_k": 3},
      {"prompt": "Reduce the complexity of this module so juniors can maintain it", "top_k": 3},
      {"prompt": "Clean up this working code, it has grown hard to follow", "top_k": 3}
    ],
    "negative": [
      {"prompt": "Add a feature flag system to the app", "owner": "incremental-implementation"},
      {"prompt": "Diagnose why the build broke overnight", "owner": "debugging-and-error-recovery"}
    ]
  },
  "evals": [...]
}
```

음성 케이스마다 **`owner` 필드로 어느 형제 스킬이 처리해야 하는지를 명시한다.**

이게 [2.5](../part2/05-examples.md)에서 "좋은 반례는 키워드가 겹치는데 실제로는 다른 처리가 필요한 경우"라고 한 것의 구현이다. "피보나치 함수 써 줘" 같은 무관한 반례는 아무것도 측정하지 않는다. `owner`가 지정된 반례는 **경계를 측정한다.**

그리고 앞서 제기한 다섯 개 `-driven-development` 충돌 우려가 이 구조로 해소된다. `google/skills`가 `description` 안에 산문으로 교차 참조를 적은 것([6.4](../part6/04-google.md))과 비교하면, 이쪽은 **기계가 검증하는 형태**로 적었다.

| 접근 | 교차 참조 | 검증 |
|---|---|---|
| `google/skills` | `description`에 산문으로 | 없음 |
| `addyosmani/agent-skills` | `evals/cases/*.json`의 `owner` | **CI** |

### 라우팅 하한을 강제한다

```bash
node scripts/run-evals.js --min-rank1 95
```

양성 프롬프트가 해당 스킬을 1순위에 올리는 비율의 하한을 95%로 둔다. `dotnet/skills`의 검정력 하한([6.5](../part6/05-microsoft.md))과 같은 종류의 장치다 — **기준을 숫자로 못 박고 CI가 막는다.**

## 유지 상태

마지막 푸시가 2026-10-03으로 수집 시점 하루 전이다. 상위권 개인 저장소 중 가장 활발한 쪽에 속한다.

| 저장소 | 마지막 푸시 |
|---|---|
| `addyosmani/agent-skills` | 2026-10-03 |
| `DietrichGebert/ponytail` | 2026-10-03 |
| `obra/superpowers` | 2026-09-27 |

(수집 날짜: 2026-10-04)

## 평가

### 강점

**커버리지가 넓다.** 25개가 성능, 관측성, 보안, 문서화, 마이그레이션까지 덮는다. `superpowers`에 없는 영역이 있다.

**진입점 스킬을 뒀다.** `using-agent-skills`가 번들을 조율한다.

**`interview-me`가 드문 설계다.** 에이전트가 무엇을 묻는지를 스킬로 만들었다. 재료 확보 문제를 정면으로 다룬다.

**카탈로그 수준 평가가 생태계 유일이다.** 스킬 25개 전부에 케이스 파일이 있고, 트리거 충돌을 CI에서 결정적으로 검사한다. 음성 케이스의 `owner` 필드는 형제 스킬 간 경계를 기계 검증 가능하게 만든 설계다.

**선행 연구를 밝히고 자기 기여를 특정했다.** Anthropic과 Superpowers의 접근을 인용하고 무엇을 채택했는지, 무엇이 자기 추가분인지 적었다. 리뷰 대상 저장소 중 유일하다.

**비용 계층을 나눴다.** 무료, 결정적 검사(Tier 1, 2)를 CI에 두고, 토큰을 쓰는 검사(Tier 3)는 필요시로 뺐다. 평가를 돌리는 비용 때문에 평가를 안 돌리는 상황을 구조로 막았다.

**갱신된다.** 수집 시점 하루 전 푸시다.

**MIT다.**

### 한계

**`and`로 묶인 이름이 많다.** 한 스킬이 두 주제를 담으면 트리거 범위가 넓어지고 본문이 길어진다. `code-review-and-quality`는 리뷰 요청, 리뷰 수신, 품질 기준을 다 덮을 수 있다. Tier 2가 다른 스킬과의 충돌은 잡지만, 한 스킬 안에서 두 주제가 섞인 것은 잡지 않는다.

**기준선 비교는 없다.** Tier 3는 "스킬을 따른 에이전트가 `expectations[]`를 만족하는가"를 본다. 스킬이 없을 때보다 나은지는 측정하지 않는다. `DietrichGebert/ponytail`이 `baseline.js`, `caveman.js`, `ponytail.js` 세 팔을 비교하는 것, `dotnet/skills`가 `BaselineStore`, `Comparator`를 두는 것과 다른 층위다.

세 저장소를 나란히 놓으면 평가가 세 방향으로 갈려 있는 것이 보인다.

| 저장소 | 강한 쪽 | 없는 쪽 |
|---|---|---|
| `addyosmani/agent-skills` | **트리거, 라우팅 충돌** (CI) | 기준선 비교 |
| `DietrichGebert/ponytail` | **기준선, 대조군, 다중 모델** | 카탈로그 라우팅 검사 |
| `dotnet/skills` | **평가 자체의 품질 게이트, 검정력** | 트리거 라우팅 검사 |

**세 가지를 다 갖춘 저장소는 수집 데이터에 없다.** [9.2](../part9/02-measuring-quality.md)에서 세 접근을 합치는 방법을 다룬다.

**"프로덕션 급"의 범위.** 설명이 `Production-grade engineering skills`다. 트리거와 구조는 검증되지만 "프로덕션 급 품질"은 Tier 3의 `expectations[]` 만족으로 측정된다 — 즉 스킬이 약속한 것을 지키는지를 재고, 그 약속이 좋은 약속인지는 재지 않는다. 방법론형의 구조적 한계다([4.2](../part4/02-three-types.md)).

### 누가 읽어야 하나

| 목적 | 볼 것 |
|---|---|
| **카탈로그 평가 설계** | `evals/README.md` — 생태계 유일 자료 |
| **트리거 충돌 검사** | `evals/cases/*.json`의 `negative[].owner` |
| 평가 비용 계층화 | `evals/README.md`의 3단 표 |
| 영역 중심 번들 설계 | 25개 이름의 구성 축 |
| 의도 포착을 스킬로 | `interview-me` |
| 컨텍스트 관리 | `context-engineering` |
| 번들 진입점 | `using-agent-skills` |

## 두 번들을 같이 쓸 수 있나

실무 질문이다. `superpowers`(15개)와 `agent-skills`(25개)를 같이 설치하면 어떻게 되는가.

**겹치는 영역에서 트리거가 경쟁한다.** 양쪽에 `test-driven-development`가 있고, 계획, 디버깅, 리뷰 영역이 겹친다. 어느 쪽이 불릴지 예측할 수 없다.

그리고 두 번들이 서로 다른 방법론을 전제한다. `superpowers`는 워크트리와 서브에이전트 주도 개발을 전제하고, 이쪽은 다섯 가지 개발 방식 중 선택을 요구한다. **같이 설치하면 방법론이 충돌한다.**

둘 중 하나를 고르는 쪽이 맞다. 고르는 기준은 이렇다.

| 상황 | 선택 |
|---|---|
| 일하는 순서를 정해 주길 원한다 | `superpowers` |
| 영역별 참고 자료를 원한다 | `agent-skills` |
| TDD를 쓴다 | 양쪽 다 가능 |
| 자기 방법론이 이미 있다 | `agent-skills`에서 필요한 스킬만 |

마지막 줄이 실용적이다. 둘 다 MIT이므로 필요한 스킬만 복사해 쓸 수 있다. 번들 전체를 설치할 의무가 없다.

---

다음 장: [7.3 단일 목적 스킬의 힘](03-single-purpose.md)
