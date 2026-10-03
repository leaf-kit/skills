# 6.4 Google — skills, agents-cli

| 저장소 | 스타 | 생성 | 푸시 | SKILL.md |
|---|---|---|---|---|
| `google/skills` | 20,875 | 2026-03-31 | 2026-10-02 | 155 |
| `google/agents-cli` | 6,043 | 2026-04-08 | 2026-09-30 | 15 |
| `android/skills` | 7,644 | — | — | 25 |
| `googleworkspace/cli` | 31,234 | — | — | 95 |
| `google/rust-skills` | 53 | — | — | — |

(수집 날짜: 2026-10-04. 확인 수준: `google/skills` 정밀 리뷰, 나머지 요약 리뷰)

Google은 조직이 여러 개로 흩어져 있다. `google`, `googleworkspace`, `android`가 각각 스킬 저장소를 갖는다. `googleworkspace/cli`는 선별에서 제외했다 — CLI 제품이고 스킬이 부속이다([5.2](../part5/02-top50.md)).

## google/skills — 제품 중심 구성

155개의 도메인 분포다.

| 도메인 | 개수 |
|---|---|
| `cloud` | 136 |
| `ads` | 14 |
| `analytics` | 2 |
| `developers` | 2 |
| `identity` | 1 |

**88%가 Google Cloud다.** `openai/skills`가 작업 중심이었던 것과 정반대다([6.3](03-openai.md)). 이쪽은 자사 제품 사용법의 집합이다.

구조는 둘로 나뉜다.

```
google/skills/
├── index.json                              (기계 생성 인덱스, 94KB)
├── skills/{ads, analytics, cloud, ...}/     (제품별)
├── plugins/cloud/google-cloud-developer/    (플러그인으로 묶은 것)
├── .agents/  .claude-plugin/                (하네스별 진입점)
└── .gitmodules                              (서브모듈)
```

유형은 **지식형**이다. Google Ads API나 Vertex AI의 사용법은 에이전트가 기억으로 답하면 틀린다. 그래서 수명이 짧고 갱신이 중요한 저장소다([4.2](../part4/02-three-types.md)). 마지막 푸시가 2026-10-02로 수집 시점 이틀 전이다 — 지식형으로서 필요한 상태를 유지하고 있다.

## index.json — 디스커버리를 푼 방식

가장 중요한 발견이다. 94KB 기계 생성 파일이고, 첫 줄이 이렇다.

```json
{"generator":"This file is generated. Do not edit it by hand.","skills":[...]}
```

항목 하나의 모양이다.

```json
{
  "name": "agent-platform-deploy",
  "description": "...",
  "entrypoint": "https://raw.githubusercontent.com/google/skills/main/skills/cloud/agent-platform-deploy/SKILL.md"
}
```

**`entrypoint`가 원격 URL이다.** 저장소를 복제하지 않고도 스킬 하나를 직접 가져올 수 있다.

이것이 [1.4](../part1/04-boundaries.md)에서 지적한 구조적 공백 — 설치하지 않은 스킬은 존재 자체가 안 보인다 — 에 대한 세 번째 답이다. 생태계에 세 가지 접근이 있다.

| 접근 | 주체 | 방식 |
|---|---|---|
| 설치 스킬 | OpenAI | `$skill-installer`를 기본 제공 |
| 인덱스 파일 | Google | `index.json`에 전체 목록과 URL |
| 프로토콜 | Cloudflare | `.well-known` 기반 발견 RFC(351) |

Google 방식이 가장 단순하다. 파일 하나를 읽으면 155개의 이름, 설명, 주소를 안다. 표준이 아니라 저장소 관례이고, 그래서 다른 저장소에서는 안 통한다.

## description 설계 — 데이터셋 최고 수준

`index.json`에 담긴 `description`들이 이 책 3부에서 처방한 내용을 거의 그대로 구현했다. 하나를 전문으로 인용한다.

> Deploy open models or custom weights from Model Garden to Agent Platform endpoints, check the status of an in-progress deployment operation, or clean up resources by undeploying models and deleting endpoints. **Use when** asked to actively deploy a model, list the Model Garden CATALOG of available models, check if a specific model is deployable (`gcloud ai model-garden models list-deployment-config`), query deployment cost, troubleshoot deployment errors (like quota limits), or undeploy/clean up endpoints. Also use when copying and deploying a 1P Tuned Model. **Don't use for** pure listing/discovery questions of the form "is X deployed?", "list my endpoints", or "which regions have models running?" — for those use `agent-platform-endpoint-management`. **Don't use for** running model evaluations (use `agent-platform-eval-flywheel` skill).

네 가지가 들어 있다.

**1. 무엇을 하는가** — 첫 문장.

**2. 언제 쓰는가** — `Use when`으로 시작하고 상황을 여섯 가지 나열한다. 실제 명령어(`gcloud ai model-garden models list-deployment-config`)까지 넣었다. 사용자가 그 명령어를 언급하면 걸린다.

**3. 쓰지 않을 조건** — `Don't use for`가 두 번 나온다. [3.2](../part3/02-description.md)에서 "가장 많이 빠뜨리는 항목"이라고 적은 것이다.

**4. 형제 스킬로 넘기기** — 제외 조건마다 **어느 스킬로 가야 하는지**를 적었다. `agent-platform-endpoint-management`, `agent-platform-eval-flywheel`을 이름으로 가리킨다.

네 번째가 특히 중요하다. 스킬 155개가 한 저장소에 있으면 서로 트리거 경쟁을 한다([1.5](../part1/05-triggering.md)). 제외 조건만 적으면 "이건 내 일이 아니다"에서 끝나고, 대안을 적으면 **경계가 그려진다.** 155개 규모에서 이게 없으면 어느 스킬이 불릴지 예측할 수 없다.

또 하나 눈여겨볼 점이 있다. 다른 스킬의 `description`에서 가져온 예다.

> NOTE: Reliability, Cost, Safety, and Security alerts use generic OTel metrics and work across runtimes (such as Cloud Run, Vertex AI). Quality alerts rely on Vertex AI Online Monitors and are **strictly bound to Vertex AI deployments**.

`description`에 **적용 범위의 제약**을 적었다. 어떤 기능은 런타임을 가리지 않고, 어떤 기능은 Vertex AI에서만 된다. 이 정보가 본문에만 있으면 트리거된 뒤에야 알게 되고, 그때는 이미 잘못 불린 것이다.

## google/agents-cli — 도구와 스킬을 같이 배포

설명이 이렇다.

> 어떤 코딩 어시스턴트든 Google Cloud에서 AI 에이전트를 만들고, **평가하고**, 배포하는 전문가로 만드는 CLI와 스킬.

CLI와 스킬을 같이 낸다. [1.4](../part1/04-boundaries.md)에서 다룬 패턴이다 — 도구가 수단을 주고 스킬이 잘 쓰는 법을 준다. `timescale/pg-aiguide`(1,854)가 MCP 서버와 스킬을 같이 배포하는 것과 같은 구조다.

"평가하고"가 설명에 들어간 점이 눈에 띈다. 에이전트를 평가하는 일을 스킬 범위에 포함했다.

## android/skills — 도메인 중심

25개가 플랫폼 영역별로 배치됐다.

```
build-system/agp/agp-9-upgrade/
camera/camerax/
device-ai/{appfunctions, ml-kit-genai-prompt-api}/
devtools/android-cli/
identity/{restore-credentials, verified-email}/
jetpack-compose/{adaptive, theming/styles, migration/migrate-xml-views-to-jetpack-compose}/
```

`google/skills`가 제품(Cloud, Ads)으로 나눈 것과 달리 **작업 영역**(빌드, 카메라, 인증, UI)으로 나눴다. 같은 회사 안에서도 구성 축이 다르다.

`agp-9-upgrade`와 `migrate-xml-views-to-jetpack-compose`가 흥미롭다. **마이그레이션 스킬**이다. 버전 업그레이드와 구식 API 전환은 절차가 길고 매번 같아서 스킬에 적합하다. 그리고 수명이 명확하다 — AGP 9 업그레이드는 그 전환기가 끝나면 쓸 데가 없어진다. 스킬에 유효기간이 있는 경우다.

## Google 저장소들의 공통 특징

### 지식형이고, 갱신되고 있다

세 저장소 모두 자사 제품, 플랫폼 지식이다. 지식형은 수명이 짧아서 갱신이 생명이다.

| 저장소 | 마지막 푸시 |
|---|---|
| `google/skills` | 2026-10-02 |
| `google/agents-cli` | 2026-09-30 |

(수집 날짜: 2026-10-04)

이틀, 나흘 전이다. 지식형 저장소로서 필요한 상태를 유지한다. `anthropics/defending-code-reference-harness`(2026-08-06)와 비교하면 차이가 있다([6.2](02-anthropic-others.md)).

### 조직이 흩어져 있다

`google`, `googleworkspace`, `android`가 각각 저장소를 갖는다. 그리고 구성 축도 서로 다르다(제품 중심 / CLI 부속 / 작업 영역 중심).

쓰는 쪽에서는 불편하다. "Google 관련 스킬"을 찾으려면 세 곳을 봐야 하고, `index.json`은 `google/skills`에만 있다.

### 평가가 없다

155개 스킬에 대한 평가나 테스트 케이스가 없다. `agents-cli`의 설명에 "에이전트를 평가하는" 기능이 있지만, 그건 사용자의 에이전트를 평가하는 것이고 스킬 자체의 평가가 아니다.

지식형에서 필요한 평가는 **사실 정확성**이다. 참조한 API 스펙이 현재와 맞는지 자동으로 확인할 수 있다. 155개를 손으로 검증할 수는 없으므로 이쪽은 자동화 여지가 큰 영역이다.

## 평가

### 강점

**`description` 설계가 생태계 최고 수준이다.** 제외 조건과 형제 스킬 교차 참조를 체계적으로 넣었다. 155개 규모에서 트리거 충돌을 관리하는 유일한 방법이고, 이걸 실제로 한 저장소다. 스킬을 만드는 사람이 `description` 쓰는 법을 배우려면 `index.json`을 읽는 것이 가장 빠르다.

**`index.json`으로 디스커버리를 해결했다.** 기계 생성이고 원격 진입점을 포함한다. 저장소를 복제하지 않고 스킬 하나를 가져올 수 있다.

**갱신된다.** 지식형으로서 가장 중요한 조건을 만족한다.

### 한계

**스타수가 낮다.** 20,875로 1위의 7%다([5.4](../part5/04-patterns.md)). `description` 설계는 최고 수준인데 주목은 그에 못 미친다. 제품 사용법 카탈로그가 드라마를 만들지 못하기 때문으로 보인다.

**자사 제품에 갇혀 있다.** Google Cloud를 쓰지 않으면 155개 중 136개가 쓸 데가 없다. `openai/skills`의 작업 중심 구성과 대조된다.

**조직이 흩어져 있고 축이 다르다.** 세 저장소를 따로 찾아야 하고, 구성 원리도 서로 다르다.

**평가가 없다.** 지식형이므로 사실 정확성 검증이 가장 필요한 유형인데 없다.

### 누가 읽어야 하나

| 목적 | 볼 것 |
|---|---|
| `description` 쓰는 법을 배운다 | **`index.json`** |
| 대규모 번들의 트리거 관리 | `index.json`의 교차 참조 패턴 |
| 디스커버리 해결 방식 | `index.json` 구조 |
| Google Cloud 작업 | `skills/cloud/` |
| 안드로이드 마이그레이션 | `android/skills` |

---

다음 장: [6.5 Microsoft — skills, SkillOpt, skill-recorder, azure-skills](05-microsoft.md)
