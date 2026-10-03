# 8.3 빌더, 메타

스킬을 대상으로 하는 저장소들이다. [4.4](../part4/04-meta-skills.md)에서 분류한 네 갈래 — 만들기, 최적화, 변환, 측정 — 를 저장소별로 본다.

| 스타 | 저장소 | 갈래 | 라이선스 | 생성 | 푸시 |
|---|---|---|---|---|---|
| 25,877 | `agentskills/agentskills` | **규격** | Apache-2.0 | 2025-12-16 | 2026-08-09 |
| 25,269 | `titanwings/distilly` | 변환 | MIT | 2026-03-30 | 2026-09-22 |
| 19,226 | `NVIDIA/SkillSpector` | 측정(보안) | Apache-2.0 | 2026-03-21 | 2026-10-02 |
| 17,979 | `microsoft/SkillOpt` | 최적화 | — | 2026-05-08 | 2026-09-30 |
| 15,097 | `yusufkaraaslan/Skill_Seekers` | 변환 | MIT | 2025-10-17 | 2026-09-30 |
| 14,009 | `nidhinjs/prompt-master` | 만들기(프롬프트) | — | — | — |
| 7,532 | `refly-ai/refly` | 만들기 | NOASSERTION | 2024-02-19 | 2026-07-29 |
| 4,185 | `microsoft/skill-recorder` | 변환 | — | — | — |
| 3,127 | `rebelytics/one-skill-to-rule-them-all` | 만들기+최적화 | **CC-BY-4.0** | 2026-02-15 | 2026-10-02 |
| 1,131 | `alibaba/skill-up` | 최적화+측정 | — | — | 2026-09-30 |
| 2 | `taneltaluri/evolve-skill` | 측정 | — | — | — |

여기에 번들 안의 메타스킬이 있다. `anthropics/skills`의 `skill-creator`, `openai/skills`의 `.system/skill-creator`, `skill-installer`, `plugin-creator`, `dotnet/skills`의 `create-skill`, `create-skill-test`, `improve-skill-quality`, `obra/superpowers`의 `writing-skills`다.

(수집 날짜: 2026-10-04. 확인 수준: `agentskills/agentskills` 정밀 리뷰, 나머지 요약 리뷰)

## agentskills/agentskills — 규격 저장소

| 항목 | 값 |
|---|---|
| 스타 | 25,877 |
| `SKILL.md` | **0개** |
| 라이선스 | Apache-2.0 |
| 푸시 | 2026-08-09 |

```
agentskills/agentskills/
├── docs/              규격 문서
├── skills-ref/        참조 구현 (검증 라이브러리)
├── AGENTS.md  CLAUDE.md
├── CONTRIBUTING.md
└── package.json
```

**스킬을 하나도 담지 않은 스킬 저장소다.** [5.1](../part5/01-collection.md)에서 기계 판정이 실패하는 사례로 든 저장소다 — `SKILL.md` 개수로 선별하면 규격을 정의한 저장소가 빠진다.

### 생태계에서의 위치

`anthropics/skills`의 `spec/agent-skills-spec.md`가 87바이트이고 내용이 이렇다([6.1](../part6/01-anthropic-skills.md)).

```markdown
# Agent Skills Spec

The spec is now located at <https://agentskills.io/specification>
```

**규격이 한 회사 저장소에서 중립 저장소로 나갔다.** 그 중립 저장소가 이것이다.

효과가 실제로 확인된다. `openai/skills`, `google/skills`, `microsoft/skills`, `dotnet/skills`, `android/skills`, `cloudflare/skills`, `NVIDIA/skills`가 같은 형식을 쓴다. `openai/skills`의 README가 "Agent Skills open standard"로 `agentskills.io`를 링크한다.

### skills-ref — 검증 라이브러리

```bash
skills-ref validate ./my-skill
```

프런트매터 유효성과 이름 규칙을 검사한다([1.2](../part1/02-anatomy.md)). `name`이 디렉터리 이름과 다른 실수가 가장 흔하고, 이게 잡아 준다.

**기능 검증은 하지 않는다.** 형식만 본다. 규격 저장소가 할 수 있는 일의 한계이기도 하다 — 규격은 모양을 정하고 품질은 정하지 않는다.

### 푸시가 두 달 전이다

2026-08-09이다. 규격 저장소로서는 안정의 신호로 읽을 수도 있다. 규격이 자주 바뀌면 그게 문제다.

다만 생태계가 빠르게 움직인다. `allowed-tools`가 실험적 필드로 남아 있고([1.2](../part1/02-anatomy.md)), 디스커버리는 네 가지 접근이 각자 돌아간다([6.8](../part6/08-others.md)). **규격이 다루지 않는 영역에서 관례가 먼저 자리 잡고 있다.**

## 변환 — 가장 스타가 많은 갈래

| 저장소 | 입력 | 결과물 유형 | 스타 |
|---|---|---|---|
| `virgiliojr94/book-to-skill` | 기술서 PDF | 지식형 | 33,430 |
| `titanwings/distilly` | **사람의 사고방식** | 방법론형 | 25,269 |
| `yusufkaraaslan/Skill_Seekers` | 문서 사이트, 저장소, PDF | 지식형 | 15,097 |
| `microsoft/skill-recorder` | 화면 작업 녹화 | 실행형 | 4,185 |

**빈 파일에서 시작하는 것이 어렵고 변환은 쉽다.** 그래서 이 갈래에 스타가 몰린다.

### distilly — 사람을 입력으로 받는다

설명이 이렇다.

> Distilly — 그들이 생각하는 방식을 어떤 에이전트나 봇에서도 재사용 가능한 스킬로 증류한다. 이전 이름: Colleague Skill(原同事 Skill).

**입력이 문서가 아니라 사람의 사고방식이다.** 이전 이름이 "동료 스킬"이었다.

[7.5](../part7/05-regional.md)에서 본 중국어권의 페르소나 스킬 범주와 같은 계열이다. `tmstack/awesome-persona-skills`(4,068)가 "동료.skill, 상사.skill, 전 연인.skill"을 모았다. `HKUSTDial/Supervisor-Skills`(7,864)가 박사 지도교수 10년 경험을 스킬로 만들었다.

위험이 분명하다. **"그들이 생각하는 방식"이 정확히 담겼는지 확인할 방법이 없다.** 사람의 판단을 스킬로 옮기면, 원본과 비교할 기준이 없다. 그리고 결과물은 방법론형이라 평가가 가장 어렵다([4.2](../part4/02-three-types.md)).

### Skill_Seekers — 충돌 탐지를 포함한다

설명이 "문서 사이트, 깃허브 저장소, PDF를 Claude AI 스킬로 변환 — **자동 충돌 탐지** 포함"이다.

충돌 탐지가 중요하다. 문서 여러 개를 스킬로 변환하면 스킬 여러 개가 생기고, 그 `description`들이 서로 겹친다([1.5](../part1/05-triggering.md)의 경쟁 스킬 문제).

`addyosmani/agent-skills`가 같은 문제를 CI에서 TF-IDF로 검사한다([7.2](../part7/02-addyosmani.md)). 이쪽은 생성 단계에서 검사한다. **생성 시점에 막는 쪽이 더 싸다.**

### 변환의 구조적 문제 — 선별을 건너뛴다

[4.4](../part4/04-meta-skills.md)에서 적은 것을 다시 확인한다.

좋은 스킬은 "항상 필요한 것"과 "조건부인 것"을 가르는 작업의 결과다([1.3](../part1/03-progressive-disclosure.md)). 책 300쪽을 자동 변환하면 300쪽이 참조 파일이 되고, 그 가르기 작업이 안 일어난다.

`microsoft/skill-recorder`가 유일하게 다른 입력을 쓴다. 작업 **과정**을 녹화한다. 문서에서 뽑으면 "적혀 있는 것"이 들어가고, 작업에서 뽑으면 "실제로 하는 것"이 들어간다. [3.1](../part3/01-capture-intent.md)에서 "가장 좋은 재료는 이미 한 작업의 기록"이라고 한 것과 맞는다.

스타는 4,185로 이 갈래에서 가장 적다. **입력을 구하기 어려운 쪽이 결과가 좋고 스타는 적다.** PDF는 흔하고 작업 녹화는 직접 해야 한다.

## 최적화 — 빅테크 세 곳이 각자 만들었다

| 저장소 | 스타 | 주체 |
|---|---|---|
| `microsoft/SkillOpt` | 17,979 | Microsoft |
| `alibaba/skill-up` | 1,131 | Alibaba |
| `anthropics/skills`의 `skill-creator` | — | Anthropic (번들 내) |

`SkillOpt`의 설명이 "재사용 가능한 자연어 스킬을 훈련하는 **텍스트 공간** 최적화기"다. 모델 가중치를 건드리지 않고 지시문 텍스트를 개선한다.

`skill-up`은 "평가와 진화 도구"다. 평가와 개선을 묶었다.

`skill-creator`의 `description` 최적화 루프는 구조가 지도학습과 닮았다. 질의 집합을 훈련 60% / 검증 40%로 나누고 **검증 점수로** 최종안을 고른다([3.2](../part3/02-description.md)).

### 공통 함정 — 과적합

검증 점수로 고르는 이유가 이 갈래의 핵심 문제를 드러낸다. **평가 집합에 맞추는 것과 실제로 좋아지는 것은 다르다.**

자동 루프를 돌리면 이 문제가 커진다. 사람이 중간에서 보지 않으면 과적합이 진행되는 것을 모른다. `skill-creator`가 "출력물을 사람에게 먼저 보인다"를 절차에 못 박은 이유다([3.8](../part3/08-iterate-and-ship.md)).

### one-skill-to-rule-them-all — 작업을 관찰한다

| 항목 | 값 |
|---|---|
| 스타 | 3,127 |
| 라이선스 | **CC-BY-4.0** |
| 푸시 | 2026-10-02 |

설명이 길고 구조가 분명하다.

> 모든 스킬을 만들고 개선하는 메타스킬, **자기 자신을 포함해서.** 당신의 작업 세션(자율 또는 사람 주도)을 관찰하고, **패턴, 수정, 판단 결정을 포착해서** 스킬 개선과 새 스킬 후보로 바꿔 **당신의 리뷰를 받는다.** Augmented Expertise 방법론의 실천적 적용. 오픈소스: CC BY 4.0.

세 가지가 설계로 들어 있다.

**"수정"을 포착한다.** `captures patterns, corrections and judgement calls`다. [3.1](../part3/01-capture-intent.md)에서 "사용자가 고쳐 준 지점이 가장 값이 나간다"고 한 것과 같다. 사용자가 돌려세운 지점이 "기본 동작이 틀린 지점"이고, 스킬의 존재 이유가 보통 거기에 있다.

**리뷰를 요구한다.** `for your review`다. 자동 생성하고 끝내지 않는다. 메타스킬의 과적합 함정을 사람 검토로 막는 구조다.

**자기 자신을 포함한다.** 재귀가 명시돼 있다. [4.4](../part4/04-meta-skills.md)에서 지적한 자기 적용 문제가 여기 있다 — 스킬 A를 고치는 메타스킬 M이 자기를 고치면, M이 나아졌는지 판정할 기준이 M 안에 있다. 외부 기준이 없으면 평가가 순환한다.

`microsoft/skill-recorder`와 입력이 같다(작업 관찰). 다른 점은 이쪽이 **스킬을 만드는 것이 아니라 개선한다**는 것이다. 이미 있는 스킬에 작업 기록을 반영한다.

라이선스가 CC-BY-4.0이다. `trailofbits/skills`의 CC-BY-SA-4.0과 달리 share-alike가 없어서 더 자유롭다([9.4](../part9/04-licensing.md)).

## 측정 — 가장 비어 있는 갈래

| 저장소 | 스타 | 측정 대상 |
|---|---|---|
| `NVIDIA/SkillSpector` | 19,226 | **보안** (71패턴, 17범주) |
| `taneltaluri/evolve-skill` | **2** | 품질 (3단 게이트) |

`SkillSpector`는 보안을 측정한다. 품질은 측정하지 않는다.

`evolve-skill`은 품질을 측정한다고 주장하고 스타가 2개다. 설명이 "측정 규율 기반 최적화기 — 3단 게이트"다.

**이 대비가 생태계의 공백을 그대로 보여 준다.**

| 측정 대상 | 도구 | 스타 |
|---|---|---|
| 형식 | `skills-ref`, `.schemas/` | 번들 내 |
| 보안 | `NVIDIA/SkillSpector` | 19,226 |
| 트리거 라우팅 | `addyosmani/agent-skills`의 Tier 2 | 번들 내 |
| 기준선 대비 기여 | `dotnet/skills`, `ponytail` | 번들 내 |
| **범용 품질 벤치마크** | **없음** | — |

**스킬을 평가하는 공통 벤치마크가 없다.** 그래서 이 책도 순위 축으로 스타수를 쓸 수밖에 없었다([0.2](../part0/02-why-stars.md)).

도구가 없는 것이 아니라 **흩어져 있다.** 세 저장소가 각각 다른 축을 재고, 셋을 다 갖춘 곳이 없다([5.4](../part5/04-patterns.md)). [9.2](../part9/02-measuring-quality.md)에서 세 축을 합치는 방법을 다룬다.

## 만들기 — refly와 prompt-master

### refly-ai/refly

| 항목 | 값 |
|---|---|
| 스타 | 7,532 |
| 생성 | **2024-02-19** |
| 푸시 | 2026-07-29 |
| 라이선스 | NOASSERTION |

생성일이 2024-02-19다. **스킬 규격 공개(2025-09-22)보다 1년 7개월 빠르다.** 다른 제품으로 시작해서 스킬 빌더로 방향을 바꾼 것으로 보인다.

설명의 마지막 문장이 주장을 담는다.

> Skills are infrastructure, not prompts.

스킬을 프롬프트가 아니라 인프라로 본다는 선언이다. 이 책 [1.1](../part1/01-from-prompt-to-skill.md)에서 "스킬은 저장된 프롬프트가 아니다"라고 한 것과 같은 방향이고, 근거도 비슷하다 — 코드를 묶을 수 있고, 버전 관리가 되고, 평가할 수 있다.

푸시가 2026-07-29로 두 달 넘게 지났다. 라이선스가 `NOASSERTION`이다 — 깃허브가 식별하지 못했다는 뜻이고, 쓰기 전에 원문을 확인해야 한다.

### nidhinjs/prompt-master

| 스타 | 설명 |
|---|---|
| 14,009 | 어떤 AI 도구에도 정확한 프롬프트를 써 주는 Claude 스킬 |

**프롬프트를 쓰는 스킬이다.** 이 책 2부의 내용을 스킬로 만든 것에 해당한다.

재귀적이지만 타당하다. 프롬프트를 잘 쓰는 일이 반복 작업이고, 반복되면 스킬로 올라간다([2.6](../part2/06-promotion.md)).

## 도메인 요약

### 강점

**규격이 중립 저장소로 나갔다.** `agentskills/agentskills`가 그 역할을 하고, 빅테크 일곱 곳이 같은 형식을 쓴다.

**빅테크 세 곳이 최적화 도구를 만들었다.** 스킬을 자동으로 개선하는 일이 공통 과제가 됐다는 신호다.

**작업 관찰 기반 접근이 나왔다.** `skill-recorder`와 `one-skill-to-rule-them-all`이 문서가 아니라 실제 작업을 입력으로 쓴다. 가장 좋은 재료를 쓰는 방향이다.

**보안 측정 도구가 작동한다.** `NVIDIA/SkillSpector`가 71개 패턴으로 스캔하고 서명 파이프라인을 돌린다.

### 한계

**범용 품질 벤치마크가 없다.** 가장 큰 공백이다. 측정 도구들이 서로 다른 축을 재고 흩어져 있다.

**변환 도구가 선별을 건너뛴다.** 스타가 가장 많은 갈래인데, 자동 변환은 "항상 필요한 것"과 "조건부인 것"을 가르지 않는다. 변환 후 사람이 깎아야 한다.

**메타스킬에 평가가 없는 경우가 많다.** "스킬을 개선한다"는 주장은 개선 전후 비교 없이 확인되지 않는다. 메타스킬은 평가를 포함할 책임이 가장 큰 범주다.

**자기 적용 문제가 해결되지 않았다.** 자기를 개선하는 메타스킬의 평가는 순환한다. `one-skill-to-rule-them-all`이 사람 리뷰를 절차에 넣어 완화하지만, 구조적 해결은 아니다.

**라이선스가 제각각이다.** MIT, Apache-2.0, CC-BY-4.0, NOASSERTION이 섞여 있다. 메타스킬로 만든 스킬의 라이선스가 무엇이 되는지도 분명하지 않다.

### 골라 쓰는 기준

| 상황 | 추천 |
|---|---|
| 스킬을 처음 만든다 | `anthropics/skills`의 `skill-creator` |
| 규격 준수를 검증한다 | `agentskills/agentskills`의 `skills-ref` |
| 문서를 스킬로 바꾼다 | `Skill_Seekers` (충돌 탐지 포함) → **직접 깎는다** |
| 작업 기록에서 스킬을 만든다 | `microsoft/skill-recorder` |
| 기존 스킬을 개선한다 | `one-skill-to-rule-them-all` (사람 리뷰 포함) |
| `description` 트리거를 올린다 | `skill-creator`의 최적화 루프 |
| 설치할 스킬을 검사한다 | `NVIDIA/SkillSpector` |
| **평가 설계를 배운다** | `dotnet/skills`, `addyosmani/agent-skills` (메타스킬이 아니라 실제 사례) |

마지막 줄이 중요하다. 평가를 **대신 해 주는 도구**보다 평가를 **제대로 한 저장소**를 읽는 것이 빠르다.

---

다음 장: [8.4 메모리, 컨텍스트](04-memory.md)
