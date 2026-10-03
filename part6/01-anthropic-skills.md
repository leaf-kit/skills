# 6.1 Anthropic — anthropics/skills

| 항목 | 값 |
|---|---|
| 스타 | 179,497 |
| 생성 | 2025-09-22 |
| 마지막 푸시 | 2026-09-29 |
| `SKILL.md` | 20개 |
| 유형 | 혼합 (실행형 + 지식형 + 방법론형) |
| 규모 | 번들 |
| 확인 수준 | **정밀 리뷰** |

(수집 날짜: 2026-10-04)

생태계의 기준점이다. 이 저장소의 생성일(2025-09-22) 직후 달에 신규 저장소가 3개에서 31개로 뛰었다([5.4](../part5/04-patterns.md)). 규격을 정의하고 참조 구현을 제공한 저장소이므로, 다른 모든 저장소를 읽을 때의 기준선이 된다.

## 구조

```
anthropics/skills/
├── README.md
├── THIRD_PARTY_NOTICES.md
├── .claude-plugin/
├── spec/
│   └── agent-skills-spec.md   (87바이트)
├── template/
│   └── SKILL.md               (5줄)
└── skills/                    (20개)
```

### 규격은 여기 없다

`spec/agent-skills-spec.md`가 87바이트다. 내용이 이게 전부다.

```markdown
# Agent Skills Spec

The spec is now located at <https://agentskills.io/specification>
```

규격이 **별도 사이트로 분리됐다.** 이 사실이 중요하다. 규격이 한 회사의 저장소 안에 있으면 그 회사의 것이고, 밖으로 나가면 공통 규격이 된다. `agentskills/agentskills`(25,877)가 그 규격과 검증 도구를 담당한다.

같은 방향의 증거가 수집 데이터에 더 있다. `openai/skills`, `google/skills`, `microsoft/skills`, `dotnet/skills`, `android/skills`, `cloudflare/skills`가 모두 같은 형식을 쓴다. **한 회사가 만든 규격이 업계 공통이 됐다.**

### 템플릿이 다섯 줄이다

```markdown
---
name: template-skill
description: Replace with description of the skill and when Claude should use it.
---

# Insert instructions below
```

최소 스킬의 모양이다. 진입 비용이 거의 0이라는 사실을 템플릿이 직접 보여 준다. 규격 공개 2주 안에 생태계가 움직인 이유가 여기 있다.

## 스킬 20개

| 분류 | 스킬 |
|---|---|
| 문서 생성 | `docx`, `xlsx`, `pptx`, `pdf` |
| 디자인, 시각화 | `canvas-design`, `frontend-design`, `theme-factory`, `algorithmic-art`, `web-artifacts-builder` |
| 개발 지원 | `mcp-builder`, `webapp-testing`, `claude-api` |
| 메타 | `skill-creator` |
| 글쓰기, 커뮤니케이션 | `doc-coauthoring`, `internal-comms`, `brand-guidelines`, `discernment-nudge` |
| 특수 영역 | `academy-guide`, `slack-gif-creator` |

**세 유형이 섞여 있다.** 문서 생성은 실행형, `claude-api`와 `brand-guidelines`는 지식형, `skill-creator`는 방법론형이다. 참조 구현으로서 각 유형의 예를 다 제공하는 구성으로 읽힌다.

## 측정 결과

20개를 측정했다. 번들 크기와 본문 크기의 비율이다.

| 스킬 | SKILL.md | 번들 총합 | 배수 | 파일 수 |
|---|---|---|---|---|
| `canvas-design` | 11,939 | 5,554,003 | 465.2× | 83 |
| `claude-api` | 101,724 | 1,857,674 | 18.3× | 81 |
| `pptx` | 20,796 | 1,139,175 | 54.8× | 56 |
| `docx` | 6,911 | 1,128,695 | 163.3× | 61 |
| `xlsx` | 8,598 | 1,102,893 | 128.3× | 53 |
| `skill-creator` | 33,168 | 224,992 | 6.8× | 18 |
| `theme-factory` | 3,124 | 144,094 | 46.1× | 13 |
| `mcp-builder` | 9,092 | 121,756 | 13.4× | 10 |
| `pdf` | 8,072 | 58,692 | 7.3× | 12 |
| `algorithmic-art` | 19,769 | 59,784 | 3.0× | 4 |
| `slack-gif-creator` | 7,841 | 43,697 | 5.6× | 7 |
| `web-artifacts-builder` | 3,087 | 45,840 | 14.8× | 5 |
| `webapp-testing` | 3,913 | 22,394 | 5.7× | 6 |
| `internal-comms` | 1,511 | 22,393 | 14.8× | 6 |
| `discernment-nudge` | 10,592 | 21,937 | 2.1× | 2 |
| `frontend-design` | 9,390 | 19,564 | 2.1× | 2 |
| `academy-guide` | 7,755 | 19,100 | 2.5× | 2 |
| `brand-guidelines` | 2,235 | 13,580 | 6.1× | 2 |
| `doc-coauthoring` | 15,815 | 15,815 | **1.0×** | 1 |

(측정: 기본 브랜치, 2026-10-04)

**배수가 1.0배부터 465배까지 분포한다.** 점진적 공개를 극단적으로 쓴 것(`canvas-design`)과 전혀 쓰지 않은 것(`doc-coauthoring`)이 같은 저장소에 있다.

이것이 참조 구현으로서 의미가 있다. "나누는 것이 규칙"이 아니라 "비용 구조를 이해하라"는 원리를 보여 준다([1.3](../part1/03-progressive-disclosure.md)). 나눌 것이 없으면 안 나눈다.

## 500줄 권고를 공식 스킬이 어긴다

| 스킬 | 줄 수 | 바이트 | 줄당 평균 |
|---|---|---|---|
| `internal-comms` | 32 | 1,511 | 47 |
| `theme-factory` | 59 | 3,124 | 53 |
| `brand-guidelines` | 73 | 2,235 | 31 |
| `docx` | 91 | 6,911 | 76 |
| `webapp-testing` | 95 | 3,913 | 41 |
| `xlsx` | 99 | 8,598 | 87 |
| `mcp-builder` | 236 | 9,092 | 39 |
| `pdf` | 314 | 8,072 | 26 |
| `skill-creator` | 485 | 33,168 | 68 |
| `claude-api` | **603** | 101,724 | **169** |

(측정: 2026-10-04)

`claude-api`가 603줄로 권고를 넘긴다. 그리고 줄당 169바이트로 다른 스킬의 2~5배다.

**이게 결함인지 판단하려면 유형을 봐야 한다.** `claude-api`는 지식형이다. 모델 ID, 가격, 파라미터처럼 기억으로 답하면 틀리는 사실을 담는다. 지식형은 사실을 생략할 수 없고, 그래서 길어진다.

더 흥미로운 것은 **줄 수와 토큰이 어긋난다**는 사실이다. `claude-api`는 603줄에 101KB이고 `skill-creator`는 485줄에 33KB다. 줄 수 차이는 1.2배인데 크기 차이는 3배다. 권고가 "500줄"과 "5,000 토큰 이하"를 같이 적어 둔 이유다. 세기 쉬운 쪽(줄)이 관례가 됐지만 실제로 중요한 건 토큰이다.

## pdf — 실행형 참조 구현

가장 교과서적인 구조다.

```
skills/pdf/
├── SKILL.md       (314줄 — 분기 판단)
├── forms.md       (양식 채우기)
├── reference.md   (상세 기술 참조)
├── LICENSE.txt
└── scripts/       (8개)
    ├── check_bounding_boxes.py
    ├── check_fillable_fields.py
    ├── convert_pdf_to_images.py
    ├── create_validation_image.py
    ├── extract_form_field_info.py
    ├── extract_form_structure.py
    ├── fill_fillable_fields.py
    └── fill_pdf_form_with_annotations.py
```

세 가지 설계가 보인다.

**분기는 본문, 실행은 스크립트.** 본문이 "채울 수 있는 필드가 있으면 A, 없으면 B"를 판단하고, 각 경로를 스크립트가 수행한다.

**이름이 동작을 말한다.** `check_`, `convert_`, `extract_`, `fill_`, `create_` 접두어를 쓴다. 스크립트를 읽지 않고 쓸 수 있다.

**검증 단계가 번들에 있다.** `create_validation_image.py`는 결과를 사람이 확인할 수 있게 만든다. 실행만 하고 끝나지 않는다.

`description`도 참고가 된다.

> Use this skill whenever the user wants to do anything with PDF files. This includes reading or extracting text/tables from PDFs, combining or merging multiple PDFs into one, splitting PDFs apart, rotating pages, adding watermarks, creating new PDFs, filling PDF forms, encrypting/decrypting PDFs, extracting images, and OCR on scanned PDFs to make them searchable. If the user mentions a .pdf file or asks to produce one, use this skill.

작업 열 가지를 나열하고 양쪽 끝에 지시를 박았다. 과소 트리거를 막는 설계다([1.5](../part1/05-triggering.md)).

## skill-creator — 메타 참조 구현

```
skills/skill-creator/
├── SKILL.md        (485줄)
├── references/     (JSON 스키마)
├── agents/         (채점자, 비교자, 분석자 지시문)
├── scripts/        (평가 실행, 집계, description 최적화, 패키징)
└── eval-viewer/    (결과 리뷰 HTML 생성)
```

번들 18개 파일 중 **대부분이 평가 도구**다. 스킬 만드는 법을 가르치는 스킬에서 비중이 가장 큰 부분이 "만든 것이 작동하는지 재는 법"이다.

`agents/` 디렉터리가 특징이다. 채점을 별도 에이전트에게 맡긴다. 만든 사람이 채점하면 관대해지기 때문이다. 그리고 채점자에게 어서션 자체를 비판하라고 지시한다 — 통과했는데 변별력 없는 항목, 아무 어서션도 검사하지 않는 중요한 결과를 찾아 보고하게 한다.

`description` 최적화 루프도 들어 있다. 질의 집합을 훈련 60% / 검증 40%로 나누고, **검증 점수로** 최종안을 고른다. 훈련 점수로 고르면 그 질의 집합에만 맞는 설명이 나온다는 문제를 구조로 막았다([3.2](../part3/02-description.md)).

## 라이선스 처리

공식 스킬들은 프런트매터에 `license`를 쓴다.

```yaml
license: Proprietary. LICENSE.txt has complete terms
```

짧게 적고 자세한 내용은 번들 파일로 넘긴다. 최상위에 `THIRD_PARTY_NOTICES.md`가 따로 있다.

**눈여겨볼 점은 라이선스가 `Proprietary`라는 것이다.** 생태계 상위권 저장소들이 MIT인 것과 대조된다 — `obra/superpowers`, `DietrichGebert/ponytail`, `addyosmani/agent-skills`, `blader/humanizer`가 모두 MIT다.

가져다 쓰거나 포크할 때 이 차이가 중요하다. [9.4](../part9/04-licensing.md)에서 다룬다.

## 평가

### 강점

**규격의 참조 구현으로서 완결적이다.** 세 유형(실행형, 지식형, 방법론형)의 예를 다 제공하고, 점진적 공개의 양 극단을 다 보여 준다. 스킬을 처음 만들 때 읽을 가치가 가장 높은 저장소다.

**스크립트 설계가 모범적이다.** `pdf` 스킬의 8개 스크립트는 이름, 분리, 검증 세 가지를 다 지킨다.

**메타 도구를 포함한다.** `skill-creator`가 평가 인프라까지 제공한다. 생태계에 평가를 포함한 저장소가 드문 상황에서([5.4](../part5/04-patterns.md)) 이게 큰 기여다.

### 한계

**평가 결과가 없다.** `skill-creator`가 평가하는 **방법**을 제공하지만, 저장소의 스킬 20개 자체에 대한 평가 결과나 테스트 케이스는 없다. 평가 도구를 만든 저장소가 자기 스킬을 평가하지 않은 상태다.

비교 대상이 있다. `dotnet/skills`는 CI에 평가 워크플로를 넣고 어서션의 변별력까지 검사한다([6.5](05-microsoft.md)). 스타는 `anthropics/skills`의 3%다.

**프로프라이어터리 라이선스.** 참조 구현인데 포크, 재배포에 제약이 있다. 생태계가 MIT로 수렴하는 가운데 기준점만 다르다.

**`claude-api`의 유지 부담.** 지식형이고 603줄 101KB다. 모델과 가격이 바뀌면 바로 낡는다. 수명이 가장 짧은 유형이므로 갱신 주기를 따로 봐야 한다([4.2](../part4/02-three-types.md)).

### 누가 읽어야 하나

| 목적 | 볼 것 |
|---|---|
| 스킬 구조를 배운다 | `template/`, `skills/pdf/` |
| 실행형 설계 | `skills/pdf/scripts/` |
| 평가 설계 | `skills/skill-creator/` |
| 지식형의 한계 | `skills/claude-api/` (603줄이 왜 필요한가) |
| 점진적 공개 | `canvas-design`(465배)과 `doc-coauthoring`(1배) 비교 |

---

다음 장: [6.2 Anthropic — 그 외 저장소](02-anthropic-others.md)
