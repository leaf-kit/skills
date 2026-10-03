# 부록 D. 참고 자료

본문에서 인용한 1차 자료다. **모두 직접 확인했고 확인 날짜를 적는다.**

## 규격

| 자료 | 주소 | 확인일 |
|---|---|---|
| Agent Skills 규격 | <https://agentskills.io/specification> | 2026-10-04 |
| 규격 저장소 | `agentskills/agentskills` | 2026-10-04 |
| 검증 라이브러리 | `agentskills/agentskills`의 `skills-ref/` | 2026-10-04 |

`anthropics/skills`의 `spec/agent-skills-spec.md`는 87바이트이고 위 사이트로 리다이렉트한다. **규격이 한 회사 저장소에서 중립 저장소로 나갔다.** → [6.1](../part6/01-anthropic-skills.md)

본문에서 인용한 규격 내용이다.

| 항목 | 값 |
|---|---|
| `name` | 1–64자, 소문자, 숫자, 하이픈, 연속 하이픈 불가, **부모 디렉터리 이름과 일치** |
| `description` | 1–1024자 |
| `compatibility` | 1–500자 |
| `allowed-tools` | **실험적** |
| 점진적 공개 | 메타데이터 ~100토큰 / 본문 <5,000토큰 권장 / 자원 제한 없음 |
| 본문 권장 상한 | **500줄** |
| 파일 참조 | 스킬 루트 기준 상대 경로, **깊이 1 유지** |

## 글쓰기 기준의 근거

[10.1](../part10/01-case-study.md)의 케이스 스터디가 쓴 외부 근거다.

| 자료 | 주소 | 확인일 |
|---|---|---|
| George Orwell, "Politics and the English Language" (1946) | <https://www.orwellfoundation.com/the-orwell-foundation/orwell/essays-and-other-works/politics-and-the-english-language/> | 2026-10-04 |
| Simon Willison, "Slop" (2024-05-08) | <https://simonwillison.net/2024/May/8/slop/> | 2026-10-04 |

오웰의 여섯 규칙 중 본문에서 쓴 것은 셋이다.

> i. Never use a metaphor, simile or other figure of speech which you are used to seeing in print.
>
> iii. If it is possible to cut a word out, always cut it out.
>
> vi. Break any of these rules sooner than say anything outright barbarous.

Willison의 정의에서 쓴 것은 책임 기준이다.

> 사람의 검토 없이 인공적으로 생성된 내용을 남에게 공유하는 것은 무례하다.

**"내 이름을 달고 말할 수 있는가" 테스트가 여기서 나왔다.** 모든 AI 생성물이 슬롭은 아니고, 사람이 읽어보고 자기 이름을 걸지 않은 채 남에게 떠넘긴 것이 슬롭이다.

같은 기준을 다른 저장소도 쓴다. `blader/humanizer`가 위키백과 "Signs of AI writing"에 기반했다고 밝힌다. → [7.3](../part7/03-single-purpose.md)

## 보안 통계

| 자료 | 주소 | 확인일 |
|---|---|---|
| `NVIDIA/SkillSpector` README | `NVIDIA/SkillSpector` | 2026-10-04 |

본문 여러 장이 의존하는 숫자다.

> 연구 데이터셋에서 분석한 31,132개 스킬 부분집합에서 **26.1%의 스킬이 취약점을 포함**하고 **5.2%가 악의적 의도로 보인다.**

탐지 범주 17개와 패턴 71개의 목록도 같은 README에 있다. → [9.3](../part9/03-supply-chain.md)

관련 문서들이다.

| 문서 | 내용 |
|---|---|
| `docs/ANALYSIS_RESOURCE_BOUNDS.md` | fail-closed 상한 — 스캐너가 공격 대상이 된다는 전제 |
| `docs/SUPPRESSION.md` | 베이스라인 기반 오탐 억제 |
| NVIDIA Verified Skills | <https://docs.nvidia.com/skills/> |

## 평가 설계

생태계에서 가장 참고할 만한 세 자료다.

| 자료 | 위치 | 왜 |
|---|---|---|
| `eng/eval-quality/README.md` | `dotnet/skills` | **평가의 함정 목록 + 통계적 검정력** |
| `evals/README.md` | `addyosmani/agent-skills` | **카탈로그 라우팅 평가 + 3단 비용 계층** |
| `benchmarks/` | `DietrichGebert/ponytail` | **기준선 + 조악한 대조군 + 다중 모델** |

### dotnet/skills

인용한 부분이다.

> `check_eval_quality.py`는 평가 결과를 오염시킬 수 있는 구조적 결함을 차단한다. 대부분은 평가가 자기 기준선에게 알 수 없이 패배했거나, 모든 시행에서 이겼는데도 실패한 뒤에야 발견된 것들이다.

> 서로 다른 자극 하나가 게이트 투표 하나를 준다. 반복 실행은 그 자극의 신뢰도를 재는 것이고 독립 과제 표본을 늘리지 않는다. 자극이 5개 미만이면 부호 검정이 어떤 효과 크기에서도 p ≤ 0.05에 도달할 수 없으므로, 어댑터는 이를 검정력 부족으로 보고한다 — 합격도 회귀도 아니다.

→ [6.5](../part6/05-microsoft.md), [9.2](../part9/02-measuring-quality.md)

### addyosmani/agent-skills

선행 연구를 밝힌 부분이다.

> `SKILL.md` 스킬을 평가하는 단일한 커뮤니티 표준은 없지만 두 접근이 앞선다. Anthropic의 skill-creator v2는 스킬별 `evals.json`을 정의한다. Superpowers(obra)는 bash + `claude -p` + 프롬프트 픽스처로 테스트한다. 둘 다 제공하지 않는 것은 다중 스킬 **카탈로그**에 대한 결정적이고 CI에서 안전한 검사다.

Tier 2의 한계도 직접 적는다.

> Tier 2는 라우팅의 어휘적 근사다. 의미를 판단할 수 없다. 하지만 실제 트리거 버그를 지배하는 두 실패 모드를 잡는다. Tier-2 실패는 보통 설명을 고치라는 뜻이고, 평가를 고치라는 뜻이 아니다.

→ [7.2](../part7/02-addyosmani.md)

## 디스커버리 규격 제안

| 자료 | 위치 | 상태 |
|---|---|---|
| Agent Skills Discovery via Well-Known URIs | `cloudflare/agent-skills-discovery-rfc` | **Draft v0.2.0** |

공개 2026-01-17, 갱신 2026-03-12. RFC 8615 기반이다.

문제 정의 부분이다.

> 오늘날 스킬을 발견하려면 깃허브 저장소 검색, 벤더 문서 읽기, 소셜 미디어 링크 따라가기, 최종 사용자의 수동 설정이 필요하다. **"example.com은 어떤 스킬을 공개하는가"에 답하는 표준 방법이 없다.**

17개 절 중 둘이 무결성을 다룬다 — `Integrity and Verification`, `Security Considerations`. **무결성 검증을 규격에 넣은 유일한 제안이다.** → [6.6](../part6/06-cloudflare.md)

## 위협 모델 문서화 사례

| 자료 | 위치 |
|---|---|
| `ASSURANCE_CASE.md` | `alibaba/open-code-review` |

스킬 저장소에서 위협 모델을 문서화한 사례를 이 저장소 외에 보지 못했다.

인용한 부분이다.

| 행위자 | 신뢰 수준 |
|---|---|
| 로컬 사용자 | 신뢰 |
| LLM 제공자 API | 준신뢰 — 응답을 쓰기 전에 검증 |
| **git 저장소** | **준신뢰 — 디프에 적대적 내용이 있을 수 있다** |
| 네트워크 | 비신뢰 |
| 웹 브라우저(뷰어) | 비신뢰 — DNS 리바인딩 |

**코드 리뷰는 신뢰할 수 없는 입력을 받아 판단을 내리는 작업이므로 프롬프트 인젝션에 가장 노출된다.** → [8.2](../part8/02-code-review.md)

## description 설계 사례

| 자료 | 위치 | 왜 |
|---|---|---|
| `index.json` | `google/skills` | **제외 조건 + 형제 스킬 교차 참조** |

94KB 기계 생성 파일이다. 항목마다 `name`, `description`, `entrypoint`(raw URL)를 담는다.

인용한 `description` 전문이다.

> Deploy open models or custom weights from Model Garden to Agent Platform endpoints... **Use when** asked to actively deploy a model, list the Model Garden CATALOG... **Don't use for** pure listing/discovery questions of the form "is X deployed?"... — for those use `agent-platform-endpoint-management`. **Don't use for** running model evaluations (use `agent-platform-eval-flywheel` skill).

**제외 조건마다 어느 스킬로 가야 하는지를 적었다.** 155개 규모에서 트리거 충돌을 관리하는 방법이다. → [6.4](../part6/04-google.md)

## 참조 구현

| 자료 | 위치 | 볼 것 |
|---|---|---|
| 최소 스킬 템플릿 | `anthropics/skills`의 `template/SKILL.md` | 5줄 |
| 실행형 참조 | `anthropics/skills`의 `skills/pdf/` | 스크립트 8개 + 분기 판단 |
| 메타 참조 | `anthropics/skills`의 `skills/skill-creator/` | 평가 도구 |
| 점진적 공개 극단 | `skills/canvas-design/` (465배) vs `skills/doc-coauthoring/` (1배) | 양 극단 |

## 이 책의 데이터

| 자료 | 위치 |
|---|---|
| 수집 스크립트 | [`data/collect.sh`](../data/collect.sh) |
| 판정 스크립트 | [`data/classify.sh`](../data/classify.sh) |
| 수집 원본 | `data/snapshots/2026-10/stars.tsv` (458개) |
| 판정 결과 | `data/snapshots/2026-10/classified.tsv` (상위 150개) |
| 재현 방법 | [부록 A](a-data.md) |

## 인용 원칙

이 책이 지킨 규칙이다.

| 규칙 | 이유 |
|---|---|
| 모든 자료에 확인 날짜를 붙인다 | 저장소 내용이 바뀐다 |
| 원문을 읽고 인용한다 | 기억으로 쓰면 틀린다 |
| 번역 인용은 원문 위치를 밝힌다 | 검증 가능해야 한다 |
| 확인하지 못한 것은 `[확인 필요]`로 남긴다 | 추측으로 채우지 않는다 |

**세 번째가 이 책에서 특히 중요하다.** 영어 README를 한국어로 옮겨 인용한 곳이 여럿이다. 번역이 의미를 바꿀 수 있으므로 어느 저장소의 어느 파일인지를 함께 적었다.

네 번째의 결과로 본문에 `[확인 필요]` 항목이 남아 있다. **미완의 표시이고, 다음 갱신에서 줄여야 할 부채다**([9.6](../part9/06-update-policy.md)).

---

여기까지가 부록이다. 처음으로: [README](../README.md)
