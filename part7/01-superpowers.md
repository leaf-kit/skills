# 7.1 obra/superpowers

| 항목 | 값 |
|---|---|
| 스타 | 294,779 |
| 생성 | 2025-10-09 |
| 마지막 푸시 | 2026-09-27 |
| 라이선스 | MIT |
| `SKILL.md` | 15개 |
| 일평균 | 819 |
| 유형 | 방법론형 |
| 확인 수준 | **정밀 리뷰** |

(수집 날짜: 2026-10-04)

전체 1위다. 규격을 만든 `anthropics/skills`(179,497)를 1.6배 앞선다. 생성일이 2025-10-09로 규격 공개(2025-09-22) 17일 뒤다.

README 첫 문장이 범위를 선언한다.

> Superpowers는 코딩 에이전트를 위한 **완전한 소프트웨어 개발 방법론**이고, 조합 가능한 스킬 묶음과 에이전트가 그 스킬들을 쓰게 만드는 초기 지침 위에 세워졌다.

## 스킬 15개 — 이름이 전부 활동이다

```
brainstorming
writing-plans
executing-plans
test-driven-development
systematic-debugging
verification-before-completion
requesting-code-review
receiving-code-review
subagent-driven-development
dispatching-parallel-agents
using-git-worktrees
finishing-a-development-branch
writing-skills
using-superpowers
diagnosing-superpowers
```

**도메인 이름이 하나도 없다.** `pdf`, `xlsx`, `azure-cost` 같은 대상 중심 이름이 아니라 전부 **동명사 — 하는 일**이다.

이것이 방법론형의 식별 표지다([4.2](../part4/02-three-types.md)). 실행형은 대상으로 이름을 짓고(`pdf`, `docx`), 지식형은 영역으로 짓고(`claude-api`, `azure-cost`), 방법론형은 활동으로 짓는다.

### 개발 사이클을 덮는다

| 단계 | 스킬 |
|---|---|
| 발상 | `brainstorming` |
| 계획 | `writing-plans`, `executing-plans` |
| 구현 | `test-driven-development`, `subagent-driven-development` |
| 디버깅 | `systematic-debugging` |
| 검증 | `verification-before-completion` |
| 리뷰 | `requesting-code-review`, `receiving-code-review` |
| 병렬화 | `dispatching-parallel-agents`, `using-git-worktrees` |
| 마무리 | `finishing-a-development-branch` |
| 자기 참조 | `writing-skills`, `using-superpowers`, `diagnosing-superpowers` |

15개가 겹치지 않고 사이클을 덮는다. 번들 설계의 조건 세 가지([4.3](../part4/03-scale.md)) 중 "경계가 겹치지 않는다"를 지켰다. `requesting-code-review`와 `receiving-code-review`를 나눈 것이 그 증거다 — 리뷰를 요청하는 상황과 받는 상황은 다른 트리거다.

### 자기 참조 스킬 세 개

| 스킬 | 역할 |
|---|---|
| `using-superpowers` | 이 번들을 쓰는 법 |
| `writing-skills` | 스킬을 쓰는 법 |
| `diagnosing-superpowers` | **이 번들이 제대로 작동하는지 진단** |

세 번째가 생태계에서 드물다. 번들이 기대대로 작동하지 않을 때 **진단하는 절차 자체를 스킬로 만들었다.**

방법론형의 전형적 실패가 "따르지 않는다"이고, 그건 "반쯤 따른" 상태가 가능하기 때문이다([4.2](../part4/02-three-types.md)). 실행형은 스크립트가 돌거나 안 돌지만 방법론형은 중간 상태가 있다. 그 중간 상태를 사용자가 발견하기 어려우므로, 진단 스킬이 그 역할을 맡는다.

`using-superpowers`가 있는 것도 설계다. README가 "에이전트가 그 스킬들을 쓰게 만드는 초기 지침"을 언급하는데, 그게 이 스킬이다. **번들의 진입점을 스킬로 만들었다.** 15개가 각자 트리거를 경쟁하는 대신 하나가 조율한다.

## 16개 하네스를 지원한다

루트에 하네스별 디렉터리가 있다.

```
.agents/  .claude-plugin/  .codex-plugin/  .cursor-plugin/
.devin-plugin/  .hermes-plugin/  .kimi-plugin/  .muse-plugin/
.opencode/  .pi/
AGENTS.md  GEMINI.md  gemini-extension.json
```

README 목차의 설치 절은 16개를 열거한다.

```
Claude Code, Antigravity, Codex App, Codex CLI, Cursor,
Devin CLI, Factory Droid, Gemini CLI, GitHub Copilot CLI,
Grok Build CLI, Kimi Code, OpenCode, Pi, Qwen Code,
Hermes Agent, Muse
```

**스킬 저장소를 도구별로 분류하는 축이 무의미하다**는 [4.1](../part4/01-taxonomy.md)의 관찰이 극단적으로 확인된다. 이 저장소 하나가 16개 도구를 대상으로 한다.

`DietrichGebert/ponytail`도 같은 전략을 쓴다(12개 넘는 하네스 디렉터리). 상위권 개인 저장소 두 곳이 같은 선택을 했다. **하네스 지원 범위가 스타수를 끌어올리는 요인**으로 보인다. 어느 도구를 쓰든 설치할 수 있으면 잠재 사용자가 그만큼 넓다.

## 테스트를 갖췄다

```
tests/
├── claude-code/
│   ├── run-skill-tests.sh
│   ├── test-executing-plans-scripts.sh
│   ├── test-subagent-driven-development.sh
│   ├── test-subagent-driven-development-integration.sh
│   ├── test-sdd-workspace.sh
│   ├── test-helpers.sh
│   └── analyze-token-usage.py
├── brainstorm-server/     (12개 테스트 파일)
└── antigravity/
```

**스킬에 대한 통합 테스트가 있다.** 생태계에서 드물다([5.4](../part5/04-patterns.md)).

주목할 것은 `analyze-token-usage.py`다. 토큰 사용량을 분석한다. [3.7](../part3/07-evals.md)에서 평가에 통과율, 시간, 토큰 세 지표를 같이 기록하라고 한 것 중 세 번째를 측정하는 도구다.

**다만 기준선 비교는 확인되지 않았다.** 테스트는 "스킬이 지시한 대로 동작하는가"를 확인하고, "스킬이 없을 때보다 나은가"는 확인하지 않는다. `dotnet/skills`의 `BaselineStore`, `Comparator`와 다른 층위다([6.5](../part6/05-microsoft.md)).

방법론형에서 기준선 비교가 어려운 것은 사실이다. 출력이 주관적이라 어서션을 쓰기 어렵다. 그럼에도 `DietrichGebert/ponytail`은 그걸 했다 — `baseline.js`, `caveman.js`, `ponytail.js` 세 팔을 세 모델에서 돌린다([5.2](../part5/02-top50.md)). 같은 유형의 저장소에서 더 엄격한 방법이 가능하다는 뜻이다.

## 훅을 같이 쓴다

```
hooks/
├── hooks.json
├── hooks-cursor.json
├── run-hook.cmd
└── session-start
```

`session-start` 훅이 있다. [1.4](../part1/04-boundaries.md)에서 구분한 대로 훅은 **판단 없이 항상 실행된다.**

이게 방법론형 번들의 핵심 문제를 푼다. 스킬은 에이전트가 필요하다고 판단해야 불리는데, 방법론은 **처음에 알려 줘야** 적용된다. 세션 시작 훅으로 "이 저장소에는 이런 방법론이 있다"를 주입하면, 과소 트리거 문제가 완화된다([1.5](../part1/05-triggering.md)).

README가 "에이전트가 그 스킬들을 쓰게 만드는 초기 지침"이라고 적은 것이 이 구조다. **스킬만으로는 방법론을 적용시킬 수 없다는 인식**이 설계에 들어 있다.

## 상업 서비스를 명시했다

README 목차에 `Commercial Services`가 있다. 오픈소스 스킬 저장소에서 수익화를 명시한 드문 사례다.

MIT 라이선스이므로 누구나 쓸 수 있고, 그 위에 서비스를 판다. 생태계의 유지 문제와 연결된다 — 스타 29만 저장소를 무보수로 유지하는 것은 지속되지 않는다. [10.3](../part10/03-publishing.md)에서 유지 비용을 다룬다.

## 왜 1위인가

네 가지로 정리된다.

**1. 범위가 가장 크다.** "완전한 소프트웨어 개발 방법론"이다. PDF 처리나 다이어그램 생성은 특정 작업이고, 이건 일하는 방식 전체다. 잠재 사용자가 모든 개발자다.

**2. 설명이 한 문장이다.** "코딩 에이전트를 위한 완전한 소프트웨어 개발 방법론." 스킬 15개가 들어 있지만 전달할 때는 한 문장이다. `google/skills`(155개)가 "Google 제품을 위한 에이전트 스킬"인 것과 비교하면, 범위가 더 넓은데 설명이 더 선명하다.

**3. 16개 하네스를 지원한다.** 어느 도구를 쓰든 설치된다.

**4. 검증이 어려운 유형이다.** 방법론형은 출력이 주관적이라 "이게 정말 나은가"를 확인하기 어렵다. 확인이 어려우면 반박도 어렵다. 스타수가 품질이 아니라 주목을 재는 지표라는 사실과 맞물린다([0.2](../part0/02-why-stars.md)).

네 번째를 비판으로만 읽을 필요는 없다. 방법론은 본래 측정하기 어렵다. 다만 **29만 스타가 이 방법론이 효과적이라는 증거는 아니다.** 효과를 재려면 기준선 비교가 필요하고, 그건 이 저장소에 없다.

## 평가

### 강점

**번들 설계가 모범적이다.** 15개가 겹치지 않고 사이클을 덮는다. `requesting-`/`receiving-code-review` 분리처럼 트리거가 다른 것을 쪼갰다.

**진입점과 진단을 스킬로 만들었다.** `using-superpowers`가 조율하고 `diagnosing-superpowers`가 진단한다. 번들 규모에서 트리거 경쟁을 관리하는 방법이다.

**훅으로 과소 트리거를 보완했다.** 방법론은 알려 줘야 적용된다는 인식이 구조에 있다.

**테스트가 있다.** 통합 테스트와 토큰 사용량 분석까지 갖췄다. 생태계 다수가 아무것도 없는 상태다.

**16개 하네스를 지원한다.** 도구 중립성을 실제로 구현했다.

**MIT다.** 포크, 개조, 재배포가 자유롭다. 실제로 `jnMetaCode/superpowers-zh`(8,256)라는 중국어 확장판이 나왔다([7.5](05-regional.md)).

### 한계

**기준선 비교가 없다.** 방법론이 효과적이라는 주장을 뒷받침하는 측정이 없다. 같은 유형의 `ponytail`이 세 팔 비교를 세 모델에서 돌리는 것과 대조된다.

**방법론이 충돌할 수 있다.** 15개가 특정한 일하는 방식을 전제한다. TDD를 쓰지 않는 팀, 워크트리를 쓰지 않는 팀에는 일부가 맞지 않는다. 방법론형은 수천 개를 모아 둘 수 없는 유형이고([4.3](../part4/03-scale.md)), 그 이유가 충돌이다. 사용자가 15개 중 일부만 쓰려 할 때의 경로가 분명하지 않다.

**검증 비용이 크다.** 15개 스킬에 훅과 스크립트가 붙고 16개 하네스 디렉터리가 있다. 설치 전에 다 읽기 어렵다. `NVIDIA/SkillSpector`의 통계(스킬 26.1%에 취약점)를 감안하면, 규모가 큰 번들은 검증 비용이 그만큼 크다([9.3](../part9/03-supply-chain.md)). MIT 저장소이고 저자가 알려져 있다는 점이 완화 요인이다.

### 누가 읽어야 하나

| 목적 | 볼 것 |
|---|---|
| 방법론형 설계를 배운다 | 스킬 15개의 이름과 경계 |
| 번들의 트리거 관리 | `using-superpowers`, `diagnosing-superpowers` |
| 과소 트리거 보완 | `hooks/session-start` |
| 스킬 테스트 작성 | `tests/claude-code/run-skill-tests.sh` |
| 토큰 비용 측정 | `tests/claude-code/analyze-token-usage.py` |
| 다중 하네스 배포 | 루트의 하네스별 디렉터리 구성 |

---

다음 장: [7.2 addyosmani/agent-skills](02-addyosmani.md)
