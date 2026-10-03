# 1.2 SKILL.md 한 장의 구조

스킬 하나는 디렉터리 하나다. 그 안에 `SKILL.md`가 반드시 있고, 나머지는 선택이다.

```
skill-name/
├── SKILL.md          필수 — 메타데이터 + 지시문
├── scripts/          선택 — 실행 코드
├── references/       선택 — 필요할 때 읽는 문서
├── assets/           선택 — 템플릿, 이미지, 데이터 파일
└── ...               그 밖의 파일과 디렉터리
```

(출처: [agentskills.io/specification](https://agentskills.io/specification))

최소 스킬은 이게 전부다. 공식 저장소의 `template/SKILL.md`를 그대로 옮기면 이렇다.

```markdown
---
name: template-skill
description: Replace with description of the skill and when Claude should use it.
---

# Insert instructions below
```

다섯 줄이다. 필수 요소는 `name`과 `description` 두 개뿐이고, 본문은 아무 형식 제약이 없다.

## 프런트매터 — 필드 6개

YAML 머리말에 들어갈 수 있는 필드는 여섯 개다. 둘이 필수이고 넷이 선택이다.

| 필드 | 필수 | 제약 |
|---|---|---|
| `name` | ○ | 1–64자. 소문자, 숫자, 하이픈만. 하이픈으로 시작, 끝 불가. 연속 하이픈 불가. **부모 디렉터리 이름과 같아야 한다** |
| `description` | ○ | 1–1024자. 비어 있으면 안 된다 |
| `license` | | 라이선스 이름 또는 번들된 라이선스 파일 이름 |
| `compatibility` | | 1–500자. 환경 요구사항 |
| `metadata` | | 문자열 키-값 맵. 규격에 없는 속성을 담는 자리 |
| `allowed-tools` | | 공백으로 구분한 사전 승인 도구 목록. **실험적** |

### `name`

규칙이 빡빡한 이유는 디렉터리 이름과 일치해야 하기 때문이다. 파일시스템과 URL에서 모두 안전한 글자만 허용한다.

```yaml
name: pdf-processing     # 유효
name: PDF-Processing     # 대문자 불가
name: -pdf               # 하이픈으로 시작 불가
name: pdf--processing    # 연속 하이픈 불가
```

실무에서 가장 많이 걸리는 건 **디렉터리 이름과의 불일치**다. 스킬 이름을 바꾸면서 디렉터리를 그대로 두면 로딩되지 않는다. 이름을 바꿀 때는 둘을 같이 바꾼다.

### `description`

1,024자까지 쓸 수 있다. 짧게 쓰라는 제약이 아니라 길게 쓸 수 있다는 뜻이다. 이 필드가 스킬이 불릴지 말지를 결정하기 때문에 실제로 길게 쓰는 편이 유리하다.

규격이 직접 좋은 예와 나쁜 예를 제시한다.

```yaml
# 나쁜 예
description: Helps with PDFs.

# 좋은 예
description: Extracts text and tables from PDF files, fills PDF forms, and
  merges multiple PDFs. Use when working with PDF documents or when the user
  mentions PDFs, forms, or document extraction.
```

차이는 두 가지다. **무엇을 하는지**와 **언제 쓰는지**가 둘 다 들어 있고, 검색에 걸릴 키워드가 들어 있다.

실제 공식 `pdf` 스킬의 `description`은 더 길다.

> Use this skill whenever the user wants to do anything with PDF files. This includes reading or extracting text/tables from PDFs, combining or merging multiple PDFs into one, splitting PDFs apart, rotating pages, adding watermarks, creating new PDFs, filling PDF forms, encrypting/decrypting PDFs, extracting images, and OCR on scanned PDFs to make them searchable. If the user mentions a .pdf file or asks to produce one, use this skill.

작업을 열 가지 가까이 나열하고, 마지막에 "`.pdf` 파일을 언급하거나 만들어 달라고 하면 이 스킬을 쓰라"는 조건을 못 박았다. `description` 설계는 [3.2](../part3/02-description.md)에서 한 장을 들여 다룬다.

### `license`

공식 저장소의 스킬들은 대부분 이 필드를 쓴다.

```yaml
license: Proprietary. LICENSE.txt has complete terms
```

짧게 쓰고 자세한 내용은 번들된 파일로 넘기는 방식이다. 남의 스킬을 가져다 쓸 때 가장 자주 빠뜨리는 확인 항목이라서 [9.4 라이선스와 출처](../part9/04-licensing.md)에서 따로 다룬다.

### `compatibility`

환경 요구사항을 적는 자리다.

```yaml
compatibility: Requires git, docker, jq, and access to the internet
compatibility: Requires Python 3.14+ and uv
compatibility: Designed for Claude Code (or similar products)
```

규격은 "대부분의 스킬은 이 필드가 필요 없다"고 적어 두었다. 스크립트를 번들하고 외부 패키지를 쓰는 스킬이라면 넣는 쪽이 낫다. 설치한 사람이 왜 안 되는지 알 수 있다.

### `allowed-tools`

사전 승인할 도구를 적는다.

```yaml
allowed-tools: Bash(git:*) Bash(jq:*) Read
```

**실험적 필드다.** 구현체마다 지원 여부가 다르다고 규격이 명시한다. 이 필드에 의존하는 스킬은 다른 도구에서 다르게 동작할 수 있다.

## 본문 — 형식 제약이 없다

프런트매터 아래 본문에는 규격상 제약이 없다. 권장 사항만 있다.

- 단계별 지시
- 입력과 출력의 예시
- 자주 걸리는 예외 상황

그리고 한 줄이 중요하다. 규격이 이렇게 적어 두었다.

> 스킬을 활성화하기로 결정하면 에이전트가 이 파일 전체를 읽는다. `SKILL.md`가 길어지면 참조 파일로 나누는 것을 고려하라.

**본문은 전부 읽힌다.** 조건부가 아니다. 그래서 본문에 안 쓰는 내용이 많으면 그 스킬이 트리거될 때마다 비용이 발생한다. 권장 상한은 **500줄**이고, 토큰으로는 5,000 토큰 이하다.

## 선택 디렉터리 세 개

### `scripts/` — 실행 코드

말로 설명하면 매번 다르게 실행되는 절차를 코드로 내린다. 공식 `pdf` 스킬이 이 패턴의 교과서다.

```
skills/pdf/
├── SKILL.md
├── forms.md
├── reference.md
├── LICENSE.txt
└── scripts/
    ├── check_bounding_boxes.py
    ├── check_fillable_fields.py
    ├── convert_pdf_to_images.py
    ├── create_validation_image.py
    ├── extract_form_field_info.py
    ├── extract_form_structure.py
    ├── fill_fillable_fields.py
    └── fill_pdf_form_with_annotations.py
```

규격이 스크립트에 요구하는 것은 세 가지다. 자체 완결적이거나 의존성을 명시할 것, 쓸모 있는 오류 메시지를 낼 것, 예외 상황을 무너지지 않고 처리할 것.

### `references/` — 필요할 때 읽는 문서

본문에서 분리한 상세 문서가 들어간다. 규격이 예로 드는 이름은 `REFERENCE.md`, `FORMS.md`, 도메인별 파일(`finance.md`, `legal.md`)이다.

핵심은 **파일을 작게 유지하는 것**이다. 필요할 때 읽어 들이는 구조이므로, 파일이 크면 조금 필요한 경우에도 전부 들어온다.

규격의 디렉터리 관례와 실제 스킬이 어긋나는 지점이 하나 있다. 공식 `pdf` 스킬은 `forms.md`와 `reference.md`를 `references/` 안이 아니라 스킬 루트에 둔다. 규격은 관례를 "권장"이라고만 적었고 강제하지 않는다. 남의 스킬을 읽을 때 `references/`가 없다고 참조 파일이 없다고 판단하면 안 된다.

### `assets/` — 출력물에 쓰는 자원

문서 템플릿, 설정 템플릿, 이미지, 조회 테이블 같은 정적 파일이다. 에이전트가 읽어서 이해하는 대상이 아니라 **출력물에 넣는 재료**라는 점이 `references/`와 다르다.

## 파일 참조 규칙

본문에서 다른 파일을 가리킬 때는 스킬 루트 기준 상대 경로를 쓴다.

```markdown
See [the reference guide](references/REFERENCE.md) for details.

Run the extraction script:
scripts/extract.py
```

규격이 한 가지를 더 요구한다. **참조는 한 단계 깊이로 유지하고, 깊게 이어지는 참조 사슬을 피하라.** `SKILL.md` → `references/a.md` → `references/b.md` → `references/c.md`처럼 연결하면, 에이전트가 끝까지 따라가다 중간에서 멈추거나 전부 읽어 비용을 쓴다.

## 검증

규격 준수를 기계로 확인할 수 있다.

```bash
skills-ref validate ./my-skill
```

`agentskills/agentskills` 저장소의 `skills-ref` 라이브러리가 제공한다. 프런트매터가 유효한지, 이름 규칙을 지키는지 검사한다. 이 저장소는 스타 25,877개인데 `SKILL.md`를 한 개도 담고 있지 않다 — 스킬 저장소 선별에서 기계 판정이 왜 실패하는지 보여주는 사례이고, [5.1](../part5/01-collection.md)에서 다뤘다.

---

다음 장: [1.3 점진적 공개](03-progressive-disclosure.md)
