# 6.3 OpenAI — openai/skills

| 항목 | 값 |
|---|---|
| 스타 | 27,856 |
| 생성 | 2025-11-25 |
| 마지막 푸시 | 2026-09-08 |
| `SKILL.md` | 44개 (`.curated` 39 + `.system` 5) |
| 상태 | **폐기(deprecated)** |
| 확인 수준 | **정밀 리뷰** |

(수집 날짜: 2026-10-04)

## 이 저장소는 폐기됐다

`README.md` 첫 줄이 이렇다.

> **This repository is deprecated.** For current Codex skill and plugin examples, use the [OpenAI Plugins repository](https://github.com/openai/plugins).

후속 저장소를 확인했다.

| 저장소 | 스타 | 생성 | 푸시 | SKILL.md |
|---|---|---|---|---|
| `openai/skills` (폐기) | **27,856** | 2025-11-25 | 2026-09-08 | 44 |
| `openai/plugins` (현행) | **7,276** | 2026-03-04 | 2026-09-28 | 536 |

(수집 날짜: 2026-10-04)

**폐기된 저장소가 현행 저장소보다 스타가 3.8배 많다.** 스킬은 44개에서 536개로 12배 늘었는데 주목은 4분의 1로 줄었다.

이것이 이 책에서 스타수를 점수로 쓰지 않는 이유의 가장 선명한 사례다([0.2](../part0/02-why-stars.md)). 스타는 **누적**되고 폐기와 함께 사라지지 않는다. 스타수만 보고 고르면 폐기된 저장소를 고른다. 그리고 폐기 표시는 `README` 안에 있어서, 저장소 카드나 검색 결과에서는 안 보인다.

[5.2](../part5/02-top50.md)의 톱 30 표에서 `openai/skills`가 20위에 있다. 순위를 매길 때는 수집 데이터만 보고 정렬했고, 폐기 사실은 저장소를 실제로 열어 보고서야 알았다. **정밀 리뷰와 요약 리뷰를 구분하는 이유가 이것이다**([0.3](../part0/03-how-to-read.md)).

## 3단 티어 구조

폐기됐어도 설계는 볼 가치가 있다. 스킬을 세 등급으로 나눈다.

| 티어 | 개수 | 설치 방식 |
|---|---|---|
| `.system/` | 5 | **Codex에 자동 설치** |
| `.curated/` | 39 | `$skill-installer <이름>`으로 설치 |
| `.experimental/` | — | 폴더를 지정해 설치 |

이 구조가 푸는 문제가 있다. 큐레이션 저장소의 핵심 정보는 "무엇을 검증했는가"인데([4.3](../part4/03-scale.md)), 대부분의 저장소가 이 구분을 하지 않고 다 섞어 둔다. OpenAI는 **디렉터리 이름으로 신뢰 등급을 표시했다.**

`anthropics/claude-plugins-official`이 `plugins/`와 `external_plugins/`로 나눈 것과 같은 방향이다([6.2](02-anthropic-others.md)). 다만 OpenAI 쪽이 한 단계 더 나아갔다 — 자동 설치되는 등급을 따로 뒀다.

### .system — 자동 설치되는 다섯 개

| 스킬 | 역할 |
|---|---|
| `skill-creator` | 스킬을 만든다 |
| `skill-installer` | 스킬을 설치한다 |
| `plugin-creator` | 플러그인을 만든다 |
| `openai-docs` | OpenAI 문서 조회 |
| `imagegen` | 이미지 생성 |

**다섯 개 중 셋이 메타스킬이다.** 스킬을 만들고, 설치하고, 플러그인으로 묶는 일이다. 기본 제공 스킬의 절반 이상이 스킬 자체를 다룬다.

`skill-installer`가 기본 제공된다는 점이 구조적으로 중요하다. [1.4](../part1/04-boundaries.md)에서 지적한 디스커버리 공백 — 설치하지 않은 스킬은 존재 자체가 안 보인다는 문제 — 를 설치 스킬로 푼다. `cloudflare/agent-skills-discovery-rfc`(351)가 `.well-known` 방식으로 풀려는 것과 다른 접근이다.

그리고 Anthropic도 `skill-creator`를 제공한다([6.1](01-anthropic-skills.md)). **양쪽이 같은 이름의 메타스킬을 각자 만들었다.** 스킬을 만드는 일이 보편적인 반복 작업이 됐다는 증거다.

## 카탈로그의 성격 — 작업 중심

`.curated/` 39개를 보면 Google, Microsoft와 성격이 다르다.

| 묶음 | 스킬 |
|---|---|
| Figma (7) | `figma`, `figma-use`, `figma-generate-design`, `figma-generate-library`, `figma-create-new-file`, `figma-create-design-system-rules`, `figma-code-connect-components`, `figma-implement-design` |
| Notion (4) | `notion-knowledge-capture`, `notion-meeting-intelligence`, `notion-research-documentation`, `notion-spec-to-implementation` |
| 배포 (5) | `vercel-deploy`, `netlify-deploy`, `cloudflare-deploy`, `render-deploy` |
| 보안 (3) | `security-best-practices`, `security-threat-model`, `security-ownership-map` |
| 깃허브 (2) | `gh-address-comments`, `gh-fix-ci` |
| 브라우저 (3) | `playwright`, `playwright-interactive`, `screenshot` |
| 플랫폼 (3) | `aspnet-core`, `winui-app`, `jupyter-notebook` |
| 기타 | `linear`, `sentry`, `speech`, `transcribe`, `pdf`, `cli-creator`, `define-goal`, `chatgpt-apps`, `openai-docs`, `migrate-to-codex`, `yeet`, `hatch-pet` |

### 경쟁사 제품이 들어 있다

`cloudflare-deploy`, `vercel-deploy`, `netlify-deploy`, `render-deploy`, `aspnet-core`, `winui-app`이 있다. Cloudflare는 자기 공식 스킬 저장소를 갖고 있고([6.6](06-cloudflare.md)), `aspnet-core`와 `winui-app`은 Microsoft 플랫폼이다.

**OpenAI의 카탈로그는 제품 중심이 아니라 작업 중심이다.** "우리 제품을 쓰는 법"이 아니라 "개발자가 하는 일"로 구성했다.

비교하면 차이가 분명하다.

| 저장소 | 구성 축 | 예 |
|---|---|---|
| `openai/skills` | 작업 | Figma, Notion, 배포, 깃허브 |
| `google/skills` | 자사 제품 | Google Ads API, Google Cloud |
| `microsoft/skills` | 자사 플랫폼 | Azure 전반 |
| `cloudflare/skills` | 자사 제품 | Durable Objects, Workers |

OpenAI만 축이 다르다. Codex가 범용 코딩 도구라서 그렇다고 볼 수 있지만, 다른 설명도 가능하다. **자사 제품으로 채울 수 있는 스킬이 적다.** Google은 Ads API와 Cloud가 있고 Microsoft는 Azure가 있는데, OpenAI는 API 하나다. 그래서 작업 축으로 갈 수밖에 없었을 수 있다.

### Figma에 7개를 썼다

한 도구에 스킬 7개가 붙었다. 디자인 생성, 라이브러리 생성, 디자인 시스템 규칙, 코드 커넥트, 구현까지 나눴다.

[2.6](../part2/06-promotion.md)에서 다룬 쪼갤 시점 판단의 실제 적용이다. "Figma를 다룬다"를 한 스킬로 만들면 `description`이 범위를 못 잡는다. 디자인을 만드는 일과 디자인을 코드로 옮기는 일은 다른 트리거다.

### migrate-to-codex

다른 도구에서 Codex로 옮겨 오는 스킬이다. 스킬을 **마케팅 수단으로 쓴 사례**로 읽을 수 있다. 규격이 공통이라 다른 도구의 설정을 읽어 변환하는 일이 가능하다.

## 평가

### 강점

**신뢰 등급을 구조로 표시했다.** `.system` / `.curated` / `.experimental` 3단은 수집 데이터의 다른 큐레이션 저장소들이 하지 않는 일이다. 쓰는 쪽이 무엇을 믿어야 하는지 디렉터리 이름으로 안다.

**메타스킬을 기본 제공한다.** `skill-installer`가 자동 설치되면 디스커버리 문제가 완화된다. 스킬을 찾고 설치하는 일을 스킬로 푼 것이다.

**작업 중심 구성.** 자사 제품에 갇히지 않았다. 개발자가 실제로 쓰는 도구(Figma, Notion, Linear, Sentry)를 다룬다.

### 한계

**폐기됐다.** 가장 큰 문제이고, 스타수로는 보이지 않는다. 후속 저장소 `openai/plugins`(7,276)가 현행이다.

**폐기 표시가 발견되기 어렵다.** `README` 최상단 인용 블록에 있다. 저장소 설명(`description`)은 여전히 "Skills Catalog for Codex"이고 폐기 언급이 없다. 깃허브 검색 결과나 토픽 목록에서는 폐기 사실이 전혀 안 보인다. **저장소를 아카이브 처리하지 않았기 때문**이기도 하다 — 아카이브하면 깃허브가 배너를 띄운다.

**평가가 없다.** `skill-creator`를 기본 제공하면서 자기 카탈로그 39개에 대한 평가는 없다. `anthropics/skills`와 같은 상태다([6.1](01-anthropic-skills.md)).

### 실무 판단

| 목적 | 판단 |
|---|---|
| Codex용 스킬을 쓰려 한다 | `openai/plugins`로 간다 |
| 티어 구조를 참고하려 한다 | 이 저장소를 본다 |
| 작업 중심 카탈로그 설계 | 이 저장소를 본다 |
| Figma, Notion 연동 스킬 | `openai/plugins`에서 현행 버전 확인 |

## 이 저장소가 남긴 교훈

폐기된 저장소가 스타 3.8배로 앞서는 상황은 생태계의 구조적 결함을 드러낸다.

**스타는 누적되고 상태는 누적되지 않는다.** 저장소가 폐기되거나 관리가 끊기거나 후속으로 대체돼도 스타수는 그대로 남는다. 그래서 스타수가 높은 저장소 목록은 "한때 주목받은 것들의 목록"이고, "지금 쓸 만한 것들의 목록"이 아니다.

이 책이 마지막 푸시 날짜를 모든 리뷰에 적는 이유이고([0.2](../part0/02-why-stars.md)), 저장소를 실제로 열어 보지 않은 리뷰를 요약 리뷰로 따로 묶는 이유다. **폐기 사실은 메타데이터에 없다. 읽어야 안다.**

갱신 규칙에 이 항목을 넣는다 — 재수집할 때 상위 저장소의 `README` 첫 단락을 확인한다([9.6](../part9/06-update-policy.md)).

---

다음 장: [6.4 Google — skills, agents-cli](04-google.md)
