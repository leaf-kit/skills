# 6.8 NVIDIA, Alibaba, AWS, Vercel

| 저장소 | 스타 | 생성 | 푸시 | 라이선스 | SKILL.md |
|---|---|---|---|---|---|
| `alibaba/open-code-review` | 43,474 | 2026-05-18 | 2026-10-01 | Apache-2.0 | 4 |
| `NVIDIA/SkillSpector` | 19,226 | 2026-03-21 | 2026-10-02 | Apache-2.0 | — |
| `NVIDIA/skills` | 3,512 | 2026-02-25 | 2026-10-02 | — | 399 |
| `timescale/pg-aiguide` | 1,854 | — | 2026-10-01 | — | — |
| `alibaba/skill-up` | 1,131 | — | 2026-09-30 | — | — |
| `vercel/vercel-plugin` | 296 | — | 2026-10-02 | — | — |
| `aws-samples/sample-well-architected-skills-and-steering` | 272 | — | 2026-09-24 | — | — |

(수집 날짜: 2026-10-04. 확인 수준: `NVIDIA/SkillSpector`, `alibaba/open-code-review` 정밀 리뷰, 나머지 요약 리뷰)

## NVIDIA — 생태계에 숫자를 준 저장소

`NVIDIA/SkillSpector`(19,226)는 이 책의 여러 장이 의존하는 자료다. **스킬이 안전한지 묻는 도구**이고, 그 질문에 대한 통계를 제공한다.

### 26.1%와 5.2%

README에 이렇게 적혀 있다.

> AI 에이전트 스킬(Claude Code, Codex CLI, Gemini CLI 등이 쓴다)은 **암묵적 신뢰로 실행되고 검증이 거의 없다.** 연구 데이터셋에서 분석한 31,132개 스킬 부분집합에서 **26.1%의 스킬이 취약점을 포함**하고 **5.2%가 악의적 의도로 보인다.**

이 책 전체에서 가장 중요한 숫자다.

| 항목 | 값 |
|---|---|
| 분석한 스킬 수 | 31,132 |
| 취약점 포함 | 26.1% |
| 악의적 의도로 보임 | 5.2% |

(출처: `NVIDIA/SkillSpector` README, 2026-10-04 확인)

**네 개 중 하나에 취약점이 있고, 스무 개 중 하나가 악성으로 보인다.**

이 수치의 무게는 설치 비용과 함께 봐야 한다. 스킬 설치는 마크다운 파일을 디렉터리에 넣는 일이다. npm 패키지보다 쉽고, 검증 절차가 없다. 그리고 설치된 스킬은 에이전트가 읽고 **그대로 따르는 지시문**이다.

[9.3 공급망 위험](../part9/03-supply-chain.md)이 이 숫자를 중심으로 쓰인다.

### 71개 패턴, 17개 범주

탐지 대상이다.

```
프롬프트 인젝션, 데이터 유출, 권한 상승, 공급망,
과도한 행위 권한(excessive agency), 출력 처리,
시스템 프롬프트 유출, 메모리 오염(memory poisoning),
도구 오용, 악성 에이전트, 거부 우회(anti-refusal),
트리거 악용(trigger abuse), 위험 코드(AST),
오염 추적(taint tracking), YARA 시그니처,
MCP 최소 권한, MCP 도구 오염
```

세 가지가 눈에 띈다.

**`trigger abuse`(트리거 악용).** `description`을 조작해 의도하지 않은 상황에 스킬이 불리게 만드는 공격이다. [1.5](../part1/05-triggering.md)에서 `description`이 트리거를 결정한다고 했는데, 그게 공격면이기도 하다. 과잉 트리거를 **일부러** 만들면 악성 스킬이 관계없는 작업에 끼어든다.

**`memory poisoning`(메모리 오염).** 메모리 스킬이 생태계에 여섯 개 넘게 있는 상황에서([5.3](../part5/03-rest.md)) 중요하다. 에이전트가 세션을 넘어 기억하면, 한 번 심은 거짓이 계속 남는다.

**`MCP tool poisoning`.** 스킬이 MCP 서버 설정을 건드려 도구를 오염시키는 경로다. 플러그인이 스킬, MCP, 훅을 한 묶음으로 배포하므로([1.4](../part1/04-boundaries.md)) 하나를 설치하면 셋이 들어온다.

### 검증, 서명, 게시 파이프라인

README가 더 큰 구조를 가리킨다.

> SkillSpector는 **NVIDIA Verified Skills 파이프라인**의 일부로, 게시 전에 에이전트 스킬을 스캔하고 평가하고 **서명한다.** 통과한 스킬은 NVIDIA 스킬 카탈로그에 게시된다.

| 단계 | 하는 일 |
|---|---|
| 스캔 | 71개 패턴 검사 (`SkillSpector`) |
| 평가 | — |
| **서명** | 무결성 보장 |
| 게시 | `NVIDIA/skills`(399개) |

**서명 단계가 있다.** 이것이 `cloudflare/agent-skills-discovery-rfc`(351)가 규격으로 제안한 무결성 검증과 같은 문제를 다른 방식으로 푼 것이다([6.6](06-cloudflare.md)).

| 접근 | 주체 | 무결성 |
|---|---|---|
| 설치 스킬 | OpenAI | 없음 |
| 인덱스 파일 | Google | 없음 |
| `.well-known` + 검증 절 | Cloudflare | 규격 제안(Draft) |
| 스캔 + 서명 + 카탈로그 | **NVIDIA** | **구현됨** |

규격은 아직 Draft인데 한 회사의 파이프라인은 돌아간다. **표준이 나오기 전에 관례가 자리 잡는** 상황이 또 나타난다.

### 도구로서의 완성도

```
NVIDIA/SkillSpector/
├── src/, tests/, scripts/
├── Dockerfile, Makefile, pyproject.toml, uv.lock
├── .pre-commit-config.yaml
├── .skillspector-baseline.example.yaml
├── CHANGELOG.md, SECURITY.md, THIRD_PARTY_NOTICES.md
├── docs/{DEVELOPMENT, ANALYSIS_RESOURCE_BOUNDS, SUPPRESSION, PI_EXTENSION, OPENCODE_EXTENSION}.md
├── extensions/, contrib/, skills/
├── model_registry.yaml, langgraph.json
└── .opencode/
```

**출력이 SARIF를 지원한다.** 정적 분석 도구의 표준 포맷이므로 기존 CI 파이프라인에 바로 붙는다. 터미널, JSON, 마크다운도 낸다.

**베이스라인으로 오탐을 억제한다.** `.skillspector-baseline.example.yaml`이 있고 `docs/SUPPRESSION.md`가 설명한다. 알려진 발견을 승인해 두면 재스캔에서 **새 문제만** 보인다. 보안 스캐너가 실무에서 쓰이려면 이 기능이 필수다 — 없으면 오탐에 묻혀 아무도 보지 않게 된다.

**`docs/ANALYSIS_RESOURCE_BOUNDS.md`가 있다.** "fail-closed 번들, 파서, 중첩 아티팩트, 장부, 발견 상한"을 다룬다. 악성 입력이 스캐너 자체를 공격하는 경우(압축 폭탄, 무한 중첩)를 막는 설계다. **스캐너가 공격 대상이 된다는 전제로 만들었다.**

**OSV.dev에 실시간 CVE를 조회한다.** 오프라인 폴백도 있다. 지식형 스킬의 수명 문제([4.2](../part4/02-three-types.md))를 외부 조회로 푼 사례다 — 취약점 목록을 저장소에 박아 두면 낡지만, 조회하면 안 낡는다.

### NVIDIA/skills — 통과한 것들의 카탈로그

| 항목 | 값 |
|---|---|
| 스타 | 3,512 |
| `SKILL.md` | 399 |
| 대상 | Physical AI, 로보틱스, 시뮬레이션, CUDA, RAG |

399개가 스캔, 서명을 거쳐 게시된 것들이다. **생태계에서 검증 절차를 명시한 유일한 대규모 카탈로그다.**

스타 3,512개로 `SkillSpector`(19,226)의 18%다. 스캐너가 카탈로그보다 5.5배 주목받았다. **"안전한 스킬 모음"보다 "안전한지 검사하는 도구"에 수요가 있다**는 뜻으로 읽힌다. 사용자는 남이 고른 것을 받기보다 자기가 고른 것을 검사하려 한다.

## alibaba/open-code-review — 스킬 4개로 4만 스타

| 항목 | 값 |
|---|---|
| 스타 | 43,474 |
| 생성 | 2026-05-18 |
| 푸시 | 2026-10-01 |
| 라이선스 | Apache-2.0 |
| 일평균 | 320 |

`SKILL.md`가 4개인데 실질적으로 2개다.

```
skills/open-code-review/SKILL.md
skills/open-code-review-delegate/SKILL.md
plugins/open-code-review/skills/open-code-review/SKILL.md          (플러그인 사본)
plugins/open-code-review/skills/open-code-review-delegate/SKILL.md (플러그인 사본)
```

같은 스킬을 `skills/`와 `plugins/` 양쪽에 둔다. 디렉터리만 복사하는 설치와 플러그인 설치를 둘 다 지원하는 구조다.

### delegate가 별도 스킬인 이유

`open-code-review`와 `open-code-review-delegate`로 나눴다. 리뷰를 **직접 하는 경로**와 **위임하는 경로**를 분리한 것으로 읽힌다.

[1.4](../part1/04-boundaries.md)에서 다룬 서브에이전트 판단이다. 코드 리뷰는 파일을 많이 읽어야 하고, 그 과정이 본 컨텍스트에 쌓이면 손해다. 그래서 위임 경로를 따로 둔다. 다만 모든 리뷰를 위임하면 결과를 이어서 쓰기 어렵다 — 그래서 두 경로를 다 제공한다.

**스킬 두 개로 4만 스타다.** 설명이 "알리바바 규모에서 실전 검증된, 안전하고 빠르고 효율적인 하이브리드 아키텍처"다. [8.2](../part8/02-code-review.md)에서 정밀 리뷰한다.

## alibaba/skill-up — 메타스킬

| 스타 | 설명 |
|---|---|
| 1,131 | 에이전트 스킬의 평가, 진화 도구 |

`microsoft/SkillOpt`(17,979)와 같은 문제를 푼다. 빅테크 세 곳이 각자 스킬 최적화 도구를 만들었다([6.5](05-microsoft.md)). [8.3](../part8/03-builders.md)에서 비교한다.

## AWS, Vercel, Timescale — 세 자리 스타 구간

| 저장소 | 스타 | 성격 |
|---|---|---|
| `timescale/pg-aiguide` | 1,854 | MCP 서버 + Postgres 스킬 |
| `vercel/vercel-plugin` | 296 | Vercel 생태계 플러그인 |
| `aws-samples/sample-well-architected-skills-and-steering` | 272 | AWS Well-Architected 가이드 |

세 저장소 모두 **자사 제품 사용법**이고 세 자리~네 자리 스타다. 다른 빅테크 공식 번들과 같은 구간이다.

`timescale/pg-aiguide`가 구조적으로 참고가 된다. MCP 서버와 스킬을 같이 배포한다. 수단(서버)과 잘 쓰는 법(스킬)을 함께 주는 패턴이고, `google/agents-cli`(6,043)와 같은 방향이다([6.4](04-google.md)).

`aws-samples/*`는 조직 이름이 `aws-samples`다. 공식 제품 조직이 아니라 샘플 저장소 조직이다. AWS가 스킬을 공식 제품으로 다루지 않고 있다는 신호로 읽힌다 — 수집 데이터에서 `aws` 조직의 스킬 저장소는 발견되지 않았다. `[확인 필요: AWS 공식 조직의 스킬 저장소 존재 여부]`

## 6부를 닫으며 — 빅테크 저장소의 공통 패턴

### 자사 제품 번들은 묻힌다

| 회사 | 자사 제품 번들 | 스타 | 작업 중심, 도구 | 스타 |
|---|---|---|---|---|
| Cloudflare | `cloudflare/skills` | 2,974 | `security-audit-skill` | 23,902 |
| Microsoft | `microsoft/skills` | 3,075 | `SkillOpt` | 17,979 |
| NVIDIA | `NVIDIA/skills` | 3,512 | `SkillSpector` | 19,226 |
| GitHub | `copilot-plugins` | 369 | `awesome-copilot` | 39,658 |
| Google | `google/skills` | 20,875 | — | — |

(수집 날짜: 2026-10-04)

네 회사에서 같은 방향이 나타난다. 자사 제품 사용법 카탈로그가 2,900~3,500 구간에 모이고, 작업을 푸는 저장소나 도구가 1만 7천~4만 구간에 있다. **5~107배 차이다.**

`google/skills`(20,875)가 예외처럼 보이지만, 155개 중 136개가 Cloud다. 제품 번들로서 가장 큰 사례이고 그래도 1위의 7%다.

### 평가 인프라는 스타수와 무관하다

| 저장소 | 스타 | 평가 |
|---|---|---|
| `dotnet/skills` | 5,543 | 기준선 비교 + 품질 게이트 + 검정력 하한 |
| `NVIDIA/SkillSpector` | 19,226 | 보안 스캔 + 베이스라인 억제 + SARIF |
| `anthropics/skills` | 179,497 | 평가 **도구** 제공, 자기 스킬 평가 없음 |
| `obra/superpowers` | 294,779 | 통합 테스트 + 토큰 분석, 기준선 비교 없음 |

**가장 엄격한 두 저장소가 스타 하위권이다.** [9.2](../part9/02-measuring-quality.md)에서 이 공백을 다룬다.

### 디스커버리, 무결성에 네 가지 접근이 경쟁한다

표준이 없고 각자 구현했다. 설치 스킬(OpenAI), 인덱스 파일(Google), `.well-known` 규격 제안(Cloudflare, Draft), 스캔, 서명, 카탈로그(NVIDIA, 구현).

**구현된 것 중 무결성을 보장하는 것은 NVIDIA 하나다.** 그리고 그 파이프라인은 NVIDIA 카탈로그에만 적용된다. 생태계 전체에는 26.1%와 5.2%라는 숫자가 그대로 남아 있다.

---

여기까지가 6부다. 다음은 개인과 커뮤니티 저장소로 넘어간다: [7.1 obra/superpowers](../part7/01-superpowers.md)
