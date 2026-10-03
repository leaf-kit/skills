# 8.7 디자인, 다이어그램

스타 합계로는 생태계에서 가장 큰 도메인이다. 상위 네 저장소가 31만 스타를 넘는다.

| 스타 | 저장소 | SKILL.md | 라이선스 | 푸시 |
|---|---|---|---|---|
| 99,291 | `nexu-io/open-design` | 537 | Apache-2.0 | 2026-10-03 |
| 92,269 | `Leonxlnx/taste-skill` | 13 | MIT | 2026-09-26 |
| 76,618 | `tt-a1i/archify` | 2 | MIT | 2026-10-03 |
| 43,213 | `cathrynlavery/diagram-design` | 1 | MIT | 2026-10-01 |
| 27,212 | `op7418/guizang-ppt-skill` | 1 | **AGPL-3.0** | 2026-08-07 |
| 9,810 | `Agents365-ai/drawio-skill` | 1 | MIT | 2026-10-02 |
| 9,355 | `ibelick/ui-skills` | 7 | MIT | 2026-09-30 |

(수집 날짜: 2026-10-04. 확인 수준: 요약 리뷰)

여기에 공식 번들의 디자인 스킬이 있다. `anthropics/skills`의 `canvas-design`(번들 5.5MB, 465배), `frontend-design`, `theme-factory`, `algorithmic-art`, `web-artifacts-builder`다([6.1](../part6/01-anthropic-skills.md)).

## 이 도메인도 "슬롭"을 문제로 지목한다

설명에 적힌 문구들이다.

| 저장소 | 문구 |
|---|---|
| `Leonxlnx/taste-skill` | AI가 **지루하고 일반적인 슬롭**을 생성하는 것을 멈춘다 |
| `cathrynlavery/diagram-design` | 그림자 없음. **Mermaid 슬롭 없음** |

**"슬롭"이라는 말이 글쓰기 도메인 밖에서 쓰인다**([8.5](05-writing.md)).

문제 구조가 같다. AI가 만든 것이 틀리지는 않았는데 밋밋하다. 다이어그램이면 Mermaid 기본 스타일이고, 디자인이면 어디서 본 듯한 랜딩 페이지다.

### taste-skill — 취향을 스킬로

| 항목 | 값 |
|---|---|
| 스타 | 92,269 |
| `SKILL.md` | 13 |
| 설명 | AI에게 좋은 취향을 준다. AI가 지루하고 일반적인 슬롭을 생성하는 것을 멈춘다 |

스킬 구성이 디자인 방향별이다.

```
skills/brandkit/                   브랜드 키트
skills/brutalist-skill/            브루탈리즘
skills/minimalist-skill/           미니멀리즘
skills/image-to-code-skill/        이미지를 코드로
skills/imagegen-frontend-web/      웹 프런트엔드 이미지 생성
skills/imagegen-frontend-mobile/   모바일
skills/gpt-tasteskill/             GPT용
skills/output-skill/               출력
```

**`brutalist`와 `minimalist`가 별도 스킬이다.** 디자인 방향을 선택지로 제공한다.

이것이 "슬롭" 문제의 구조적 해법이다. 밋밋함은 **방향이 없을 때** 생긴다([2.3](../part2/03-length-myth.md)에서 다룬 "조건이 쌓이면 평균으로 수렴한다"와 같다). 조건을 여러 개 붙이면 평균으로 가고, 방향을 하나 고르면 평균에서 벗어난다.

`addyosmani/agent-skills`의 다섯 개 `-driven-development`와 같은 구조다([7.2](../part7/02-addyosmani.md)) — 선택지를 제공하고 사용자가 고른다. 트리거 경쟁 위험이 따라오는 것도 같다.

### diagram-design — 설명에 안티패턴을 적었다

| 항목 | 값 |
|---|---|
| 스타 | 43,213 |
| `SKILL.md` | **1** |
| 설명 | Claude Code, Codex, GitHub Copilot, Factory Droid, Pi용 **편집 품질** 다이어그램 디자인. 42가지 다이어그램 유형. 자체 완결 HTML + SVG. **그림자 없음. Mermaid 슬롭 없음.** |

**`description`에 하지 말 것을 적었다.** "그림자 없음", "Mermaid 슬롭 없음"이다.

이것이 영리한 설계다. 금지선이 트리거 단계에서 전달된다. 사용자가 "Mermaid 말고 제대로 된 다이어그램"을 원할 때 걸린다 — [1.5](../part1/05-triggering.md)에서 다룬 "사용자가 실제로 쓰는 말"에 불만 표현이 포함된다는 점을 활용했다. `DietrichGebert/ponytail`이 "over-engineering, bloat에 대한 불만"을 키워드로 넣은 것과 같다([7.3](../part7/03-single-purpose.md)).

**"42가지 다이어그램 유형"이 단일 `SKILL.md`에 들어 있다.** 점진적 공개를 쓰지 않은 구조로 보인다. `blader/humanizer`와 같은 선택이다([7.3](../part7/03-single-purpose.md)). 유형별로 참조 파일을 나누면 비용이 줄 여지가 있다 — 시퀀스 다이어그램을 그릴 때 42가지 전부를 읽을 필요가 없다.

`cloudflare/security-audit-skill`이 단일 스킬에 참조 파일 14개를 둔 것과 대조된다([6.6](../part6/06-cloudflare.md)).

### archify — "검증 가능한" 다이어그램

| 항목 | 값 |
|---|---|
| 스타 | 76,618 |
| 설명 | 아름답고 **검증 가능한** 아키텍처, 워크플로, 시퀀스, 데이터플로, 생애주기 다이어그램 |

"검증 가능한(verifiable)"이 설명에 있다. 다이어그램이 실제 구조와 맞는지 확인할 수 있다는 주장이다.

[2.1](../part2/01-criteria.md)의 검증 가능성 기준을 디자인 영역에 적용한 것이다. 다이어그램은 보통 주관적 산출물인데, **코드 구조와의 일치**는 객관적으로 확인된다.

## drawio-skill — 이 도메인에서 유일하게 테스트를 말한다

| 항목 | 값 |
|---|---|
| 스타 | 9,810 |
| `SKILL.md` | 1 |
| 라이선스 | MIT |

설명이 길고 구조가 분명하다.

> 자연어, 코드, Terraform/K8s, SQL, OpenAPI, AsyncAPI, Protobuf, GraphQL 소스를 편집 가능하고 **테스트된** draw.io 아키텍처 다이어그램으로 바꾼다: 증분 동기화, 다중 뷰 투영, **드리프트 디프**, **CI 아키텍처 테스트**, 화이트보드 디래스터화, 인터랙티브 HTML/PPTX/Mermaid 내보내기.

세 가지가 이 도메인에서 유일하다.

**`drift diff`(드리프트 디프).** 다이어그램과 실제 구조가 어긋났는지 비교한다. 아키텍처 문서가 낡는 문제를 기계로 잡는다.

**`CI architecture tests`.** 다이어그램을 CI에서 검사한다. 코드가 바뀌면 다이어그램이 틀려지는데, 그걸 빌드 실패로 만든다.

**입력이 선언적 소스다.** Terraform, K8s, SQL, OpenAPI, Protobuf, GraphQL이다. 자연어 설명이 아니라 **실제 시스템 정의**를 읽는다. 그래서 검증이 가능하다.

이것이 `archify`의 "검증 가능한"을 한 단계 더 간 것이다. 다이어그램 생성을 **빌드 산출물**로 취급한다.

스타는 9,810으로 `archify`(76,618)의 13%다. [7.6](../part7/06-why-individuals-win.md)에서 본 패턴이 또 나타난다 — 엄격한 쪽이 주목을 덜 받는다.

## op7418/guizang-ppt-skill — AGPL-3.0

| 항목 | 값 |
|---|---|
| 스타 | 27,212 |
| `SKILL.md` | 1 |
| 라이선스 | **AGPL-3.0** |
| 푸시 | 2026-08-07 |

**데이터셋에서 가장 강한 카피레프트다.**

지금까지 본 라이선스 분포에 넣어 보면 이렇다.

| 라이선스 | 성격 | 저장소 예 |
|---|---|---|
| MIT | 제약 거의 없음 | `superpowers`, `ponytail`, `humanizer`, `archify`, `diagram-design` |
| Apache-2.0 | 특허 조항 + 고지 | `SkillSpector`, `open-code-review`, `open-design` |
| CC-BY-4.0 | 출처 표기 | `one-skill-to-rule-them-all` |
| CC-BY-SA-4.0 | 출처 표기 + **동일조건변경허락** | `trailofbits/skills` |
| **AGPL-3.0** | **파생물 소스 공개 + 네트워크 사용 포함** | `guizang-ppt-skill` |
| Proprietary | 제약 있음 | `anthropics/skills` |

AGPL은 **파생 저작물을 같은 라이선스로 공개**해야 하고, 네트워크를 통해 서비스로 제공하는 경우에도 소스 공개 의무가 발생한다.

### 스킬에서 AGPL이 뜻하는 것

실무적 결과가 세 가지다.

**1. 큐레이션 저장소에 넣기 어렵다.** 스킬 수백 개를 모아 자기 번들로 만드는 저장소가 많은 생태계에서([7.4](../part7/04-awesome-lists.md)) AGPL 스킬을 MIT 번들에 섞으면 문제가 된다.

**2. 사내 포크에도 영향이 있을 수 있다.** 고쳐서 쓰는 것 자체는 되지만, 배포하거나 서비스로 제공하면 공개 의무가 걸린다. 스킬을 사내 플랫폼에 올려 팀이 쓰게 하는 경우 해석이 필요하다.

**3. 파생 스킬을 만들 때 같은 라이선스를 써야 한다.** 이 스킬의 패턴을 가져와 자기 스킬을 만들면 AGPL이 따라온다.

**스킬 라이선스가 코드 라이선스처럼 전파된다는 점을 생태계가 아직 다루지 않는다.** 스킬은 "문서인가 코드인가"가 애매하고, 라이선스 선택이 MIT / Apache / CC / AGPL로 흩어져 있다. [9.4](../part9/04-licensing.md)에서 다룬다.

푸시가 2026-08-07로 이 도메인에서 가장 오래됐다.

## nexu-io/open-design — 537개 스킬

| 항목 | 값 |
|---|---|
| 스타 | 99,291 |
| `SKILL.md` | 537 |
| 라이선스 | Apache-2.0 |

설명이 범위를 보여 준다.

> 최고의 DeepSeek 하네스 디자인 플러그인. 오픈소스 Claude Design 대안. 로컬 우선 데스크톱 앱. 당신의 코딩 에이전트가 디자인 엔진이 된다: 프로토타입, 랜딩 페이지, 대시보드, 슬라이드, 이미지, 영상 — **실제 파일**, HTML/PDF/PPTX/MP4 내보내기. Claude Code / Codex / Cursor / DeepSeek Harness / OpenCode 및 **20개 이상 CLI**를 BYOK로.

**마켓플레이스 규모다**(537개). 그리고 데스크톱 앱이 포함된다 — 스킬만 있는 저장소가 아니다.

[5.2](../part5/02-top50.md)에서 트랙 A에 넣었는데, 판정이 애매한 쪽이다. 데스크톱 앱을 빼도 스킬 537개가 남고, 스킬을 빼면 앱이 남는다. 설명의 비중이 스킬 쪽에 있어서 포함했다.

**"20개 이상 CLI"가 상위권 저장소의 공통 전략을 다시 확인한다**([7.6](../part7/06-why-individuals-win.md)). `superpowers` 16개, `ponytail` 20개, 이 저장소 20개 이상이다.

## 공식 번들과의 비교 — canvas-design

`anthropics/skills`의 `canvas-design`이 이 도메인의 대조군이다.

| 항목 | 값 |
|---|---|
| `SKILL.md` | 11,939 B |
| 번들 총합 | 5,554,003 B |
| 배수 | **465.2×** |
| 파일 수 | 83 |

**점진적 공개를 가장 극단적으로 쓴 스킬이다.** 본문이 전체의 0.2%다([1.3](../part1/03-progressive-disclosure.md)).

디자인 스킬에서 이 구조가 자연스러운 이유가 있다. 디자인은 **자산**이 많다. 폰트, 템플릿, 색상 정의, 예시 이미지가 `assets/`에 들어가고, 그건 에이전트가 읽을 대상이 아니라 출력물에 넣을 재료다([3.6](../part3/06-assets.md)).

그런데 이 도메인의 개인 저장소들은 반대 선택을 했다.

| 저장소 | SKILL.md | 구조 |
|---|---|---|
| `canvas-design` (공식) | 11,939 B | 번들 83개 파일, 465배 |
| `diagram-design` | 1개 | 42가지 유형을 한 파일에 |
| `archify` | 2개 | — |
| `drawio-skill` | 1개 | — |

**개인 저장소는 "자체 완결 HTML"을 내세운다.** `diagram-design`과 `archify`가 둘 다 `self-contained HTML`을 설명에 적는다.

자산을 번들하지 않고 HTML 안에 다 넣는 접근이다. 설치가 간단하고(파일 하나), 결과물이 독립적이다. 대가는 본문이 커지는 것이다.

**둘 다 타당한 선택이고, 어느 쪽이 비용이 적은지는 측정해야 안다.** 이 도메인에 측정이 없다.

## 도메인 요약

### 강점

**"슬롭" 문제를 정면으로 지목한다.** 밋밋함이 품질 문제라는 인식이 설명에 들어 있다. `taste-skill`의 방향 선택(브루탈리즘/미니멀리즘)은 그 구조적 해법이다.

**설명에 안티패턴을 적은 사례가 있다.** `diagram-design`의 "그림자 없음, Mermaid 슬롭 없음"은 금지선을 트리거 단계에서 전달한다.

**검증 가능성을 추구한 사례가 있다.** `drawio-skill`의 드리프트 디프와 CI 아키텍처 테스트는 이 도메인에서 유일하게 기계 검증을 구현했다. 입력을 선언적 소스(Terraform, OpenAPI)로 받아 검증을 가능하게 만든 설계다.

**유지가 잘 된다.** 일곱 저장소 중 여섯이 2026-09 이후 푸시다.

**다중 하네스 지원이 보편적이다.** `open-design` 20개 이상, `diagram-design` 5개다.

### 한계

**평가가 거의 없다.** `drawio-skill`을 빼면 측정이 확인되지 않는다. 디자인 품질은 주관적이지만, "다이어그램이 코드 구조와 맞는가"는 객관적이다. `archify`가 "검증 가능한"을 주장하면서 검증 결과를 내놓지 않는다.

**점진적 공개를 쓸지가 미해결이다.** 공식 스킬은 465배로 나누고, 개인 저장소는 자체 완결을 택한다. 비교 측정이 없다.

**AGPL 스킬이 있다.** `guizang-ppt-skill`이 AGPL-3.0이다. 큐레이션 번들이나 사내 배포에서 해석이 필요하고, 생태계가 이 문제를 다루지 않는다.

**엄격한 쪽이 주목을 덜 받는다.** `drawio-skill`(CI 테스트 포함)이 `archify`의 13%다.

### 골라 쓰는 기준

| 상황 | 추천 |
|---|---|
| 아키텍처 다이어그램을 CI로 검증한다 | `Agents365-ai/drawio-skill` |
| 아키텍처, 시퀀스, 데이터플로 다이어그램 | `tt-a1i/archify` |
| 편집 품질 다이어그램 42종 | `cathrynlavery/diagram-design` |
| 디자인 방향을 고르고 싶다 | `Leonxlnx/taste-skill` (브루탈리즘/미니멀리즘) |
| 프로토타입, 랜딩, 대시보드 전반 | `nexu-io/open-design` |
| 디자인 엔지니어용 | `ibelick/ui-skills` |
| HTML 슬라이드 | `op7418/guizang-ppt-skill` — **AGPL 확인** |
| 번들 자산이 필요한 작업 | `anthropics/skills`의 `canvas-design` |

AGPL 항목을 강조해 둔다. 이 도메인에서 유일하게 라이선스가 실무 결정을 바꿀 수 있는 저장소다.

---

다음 장: [8.8 제품, 업무](08-product.md)
