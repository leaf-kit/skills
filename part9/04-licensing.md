# 9.4 라이선스와 출처

스킬은 코드인가 문서인가. 이 질문에 생태계가 합의하지 못했고, 그 결과가 라이선스 분포에 나타난다.

## 상위 60개의 라이선스 분포

`SKILL.md`를 보유한 상위 60개 저장소를 조회했다.

| 라이선스 | 저장소 수 | 비율 |
|---|---|---|
| MIT | 37 | 62% |
| Apache-2.0 | 12 | 20% |
| **NOASSERTION** | 5 | 8% |
| **없음(NONE)** | 4 | 7% |
| AGPL-3.0 | 2 | 3% |

(수집 날짜: 2026-10-04. 깃허브 API의 `license.spdx_id` 기준)

**MIT가 62%로 사실상 기본값이다.** 그런데 나머지 38%에 실무적으로 중요한 것들이 있다.

## 라이선스 파일이 없는 저장소 네 개

가장 중요한 발견이다.

| 스타 | 저장소 | 성격 |
|---|---|---|
| 179,497 | `anthropics/skills` | **규격 참조 구현** |
| 149,104 | `anthropics/claude-code` | 도구 |
| 76,418 | `ComposioHQ/awesome-claude-skills` | **큐레이션 864개** |
| 27,856 | `openai/skills` | Codex 카탈로그 |

(수집 날짜: 2026-10-04)

**저장소 루트에 `LICENSE` 파일이 없다.** 기본값은 모든 권리 유보다 — 명시적 허락이 없으면 복제, 수정, 재배포 권리가 없다.

### anthropics/skills — 스킬별로 라이선스를 둔다

전체를 보면 다르다. 저장소 루트에는 없지만 **스킬 디렉터리마다 `LICENSE.txt`가 있다.**

```
skills/academy-guide/LICENSE.txt
skills/algorithmic-art/LICENSE.txt
skills/brand-guidelines/LICENSE.txt
skills/canvas-design/LICENSE.txt
skills/claude-api/LICENSE.txt
skills/discernment-nudge/LICENSE.txt
... (총 18개)
```

프런트매터가 그 파일을 가리킨다.

```yaml
license: Proprietary. LICENSE.txt has complete terms
```

**라이선스 단위가 저장소가 아니라 스킬이다.** 설계로서 타당하다 — 스킬은 개별로 복사해 쓰는 단위이므로 라이선스도 그 단위에 붙는 것이 맞다.

다만 두 가지가 걸린다.

**첫째, `LICENSE.txt`가 18개인데 스킬은 20개다.** 두 스킬에 라이선스 파일이 없다. `[확인 필요: 어느 두 스킬인지, 의도된 것인지]`

**둘째, 깃허브가 식별하지 못한다.** 저장소 페이지에 라이선스가 표시되지 않고, API도 `NONE`을 반환한다. 자동 라이선스 검사 도구를 쓰는 조직에서는 "라이선스 없음"으로 잡힌다.

### 생태계가 MIT인데 기준점만 Proprietary다

| 저장소 | 라이선스 |
|---|---|
| `anthropics/skills` (참조 구현) | **Proprietary** |
| `obra/superpowers` (1위) | MIT |
| `DietrichGebert/ponytail` | MIT |
| `addyosmani/agent-skills` | MIT |
| `blader/humanizer` | MIT |

**참조 구현이 가장 제약이 크다.**

이게 포크에 영향을 준다. `obra/superpowers`가 MIT이고 실제로 중국어 확장판이 나왔다 — `jnMetaCode/superpowers-zh`(8,256)이고 원본보다 스킬이 6개 많다([7.5](../part7/05-regional.md)).

공식 스킬의 언어별 포크는 수집 데이터에서 보이지 않는다. 라이선스와 무관하지 않을 수 있다. `[확인 필요: anthropics/skills 라이선스가 포크, 번역을 허용하는 범위]`

### openai/skills — 라이선스가 아예 없다

저장소 전체에 `LICENSE` 파일이 0개다. 루트에 `.gitignore`, `README.md`, `contributing.md`, `skills/`만 있다.

그리고 이 저장소는 **폐기됐다**([6.3](../part6/03-openai.md)). 폐기된 데다 라이선스가 없는 저장소가 스타 27,856으로 톱 30에 있다.

## ComposioHQ/awesome-claude-skills — 864개와 13개

큐레이션 저장소의 라이선스 문제를 보여 주는 사례다.

| 항목 | 값 |
|---|---|
| 스타 | 76,418 |
| `SKILL.md` | **864** |
| 저장소 루트 `LICENSE` | **없음** |
| 저장소 전체의 `LICENSE` 파일 | **13** |

### 복사된 스킬은 라이선스를 가져왔다

확인해 봤다. 이 저장소의 `brand-guidelines/` 디렉터리에 `SKILL.md`와 `LICENSE.txt`가 있다.

```
brand-guidelines/
├── LICENSE.txt
└── SKILL.md
```

그리고 `SKILL.md`의 해시가 `anthropics/skills/skills/brand-guidelines/SKILL.md`와 **일치한다.**

```
anthropics/skills  md5: 207ce9f9ea28f742ff2c9deaca08bd6e
Composio           md5: 207ce9f9ea28f742ff2c9deaca08bd6e
```

**바이트 단위로 같은 복사본이고, `LICENSE.txt`를 함께 가져왔다.**

이게 올바른 재배포 방식이다. 원저작물을 복사할 때 라이선스 파일을 같이 옮긴다. 큐레이션 저장소에서 이 정도를 지킨 사례를 다른 데서 확인하지 못했다.

(원 라이선스가 재배포를 허용하는지는 별개 문제다. `Proprietary`이므로 원문을 읽어야 한다.)

### 그런데 864개에 13개다

`LICENSE` 파일이 13개이고 `SKILL.md`가 864개다. **851개 스킬에 라이선스 파일이 없다.**

그리고 저장소 루트에도 없다. 결과적으로 이렇게 된다.

| 대상 | 라이선스 상태 |
|---|---|
| 복사된 공식 스킬 13개 | 원 라이선스 동반 |
| 나머지 851개 | **불명** |
| 수집, 정리 작업 자체 | **불명** |

마지막 줄이 큐레이션 저장소의 고유 문제다. 모으고 분류하고 설명을 붙인 작업에도 권리가 있는데, 루트에 라이선스가 없으면 그 작업물을 쓸 권리가 없다.

**이 저장소를 가져다 쓰려면 851개의 출처를 각각 추적해야 한다.** 현실적으로 불가능하다.

## NOASSERTION — 식별 실패

| 스타 | 저장소 | 도메인 |
|---|---|---|
| 157,770 | `langgenius/dify` | 플랫폼 (선별 제외) |
| 82,962 | `lobehub/lobehub` | 제품 (선별 제외) |
| 69,766 | `code-yeongyu/oh-my-openagent` | 에이전트 제어 |
| 25,201 | `mksglu/context-mode` | 컨텍스트 최적화 |
| 7,871 | `HKUSTDial/Supervisor-Skills` | 연구 |
| 7,542 | `anthropics/defending-code-reference-harness` | **보안** |
| 7,151 | `deanpeters/Product-Manager-Skills` | 제품 관리 |

(수집 날짜: 2026-10-04)

`NOASSERTION`은 라이선스 파일이 있지만 깃허브가 표준 형식으로 식별하지 못했다는 뜻이다. 커스텀 조항이 섞였거나 수정된 표준 라이선스일 수 있다.

**원문을 읽어야 한다.** 그리고 자동 검사 도구가 통과시키지 않는다.

도메인에 따라 무게가 다르다.

| 저장소 | 왜 중요한가 |
|---|---|
| `anthropics/defending-code-reference-harness` | **보안 스킬**을 조직에 들일 때 법무 검토가 필요하다 |
| `mksglu/context-mode` | 대화 내용을 다루는 도구다 |
| `HKUSTDial/Supervisor-Skills` | 연구 성과물의 권리가 걸린다 |

## AGPL-3.0 — 가장 강한 카피레프트

| 스타 | 저장소 |
|---|---|
| 52,344 | `CherryHQ/cherry-studio` (선별 제외 — 제품) |
| 27,212 | `op7418/guizang-ppt-skill` |

`op7418/guizang-ppt-skill`은 `SKILL.md` 1개짜리 스킬 저장소다([8.7](../part8/07-design.md)).

### 스킬에서 AGPL이 뜻하는 것

AGPL은 **파생 저작물을 같은 라이선스로 공개**해야 하고, 네트워크를 통해 서비스로 제공하는 경우에도 소스 공개 의무가 생긴다.

실무적 결과가 셋이다.

| 상황 | 영향 |
|---|---|
| MIT 번들에 섞는다 | **라이선스 충돌** |
| 고쳐서 사내 배포 | 공개 의무 해석이 필요 |
| 패턴을 가져와 새 스킬 | AGPL이 따라온다 |

첫 번째가 이 생태계에서 실제로 문제가 된다. 스킬 수백 개를 모아 번들로 만드는 저장소가 많다([7.4](../part7/04-awesome-lists.md)). `sickn33/agentic-awesome-skills`가 8,212개를 모았다. 그 안에 AGPL 스킬이 섞여 있는지 확인된 바 없다.

## CC 계열 — 문서로 본 선택

상위 60개 조회에서는 CC 라이선스가 잡히지 않았지만, 리뷰 대상에 둘 있다.

| 라이선스 | 저장소 | 성격 |
|---|---|---|
| CC-BY-SA-4.0 | `trailofbits/skills`(7,351) | **동일조건변경허락** |
| CC-BY-4.0 | `rebelytics/one-skill-to-rule-them-all`(3,127) | 출처 표기만 |

**스킬을 코드가 아니라 문서로 보고 문서 라이선스를 쓴 사례다.** 타당한 관점이다 — `SKILL.md`는 마크다운이고 산문이다.

문제는 섞일 때다.

| 조합 | 결과 |
|---|---|
| MIT + MIT | 문제없다 |
| MIT + CC-BY-SA | **번들 전체가 share-alike에 걸린다** |
| MIT + AGPL | 충돌 |
| MIT + Proprietary | 재배포 불가 가능성 |

**스킬 생태계는 섞는 것이 기본 사용법이다.** 번들을 만들고, 필요한 스킬만 복사하고, 포크해서 고친다. 그 환경에서 라이선스가 MIT / Apache / CC-BY / CC-BY-SA / AGPL / Proprietary / NOASSERTION / 없음으로 흩어져 있다.

## 번들 자산의 라이선스는 별개다

[3.6](../part3/06-assets.md)에서 다룬 문제다.

`assets/`에 넣는 파일은 대개 만든 사람의 것이 아니다. 폰트, 아이콘, 템플릿, 데이터셋이다.

**스킬 자체의 라이선스와 번들 자산의 라이선스는 다르다.** MIT 스킬에 재배포 금지 폰트가 들어 있으면 그 스킬은 MIT로 쓸 수 없다.

규모를 보면 이 문제가 작지 않다.

| 스킬 | 번들 총합 | 파일 수 |
|---|---|---|
| `canvas-design` | 5,554,003 B | 83 |
| `claude-api` | 1,857,674 B | 81 |
| `pptx` | 1,139,175 B | 56 |
| `docx` | 1,128,695 B | 61 |

(측정: `anthropics/skills`, 2026-10-04)

**5.5MB 번들의 자산 출처를 설치자가 확인할 수 없다.** `anthropics/skills`가 루트에 `THIRD_PARTY_NOTICES.md`를 둔 것이 이 문제에 대한 대응이다.

## 원저작물 권리 — 변환형 스킬의 문제

[8.8](../part8/08-product.md)에서 다룬 사례다.

| 저장소 | 상황 |
|---|---|
| `virgiliojr94/book-to-skill`(33,440) | 기술서 PDF를 스킬로 바꾸는 **도구** |
| `wondelai/skills`(2,322) | "베스트셀러 책에서 가져온" 프레임워크 50개, **MIT** |

### 무엇이 저작권 대상인가

| 대상 | 저작권 |
|---|---|
| 책의 아이디어, 프레임워크 | 대상이 아니다 (표현이 아니라 발상) |
| 책의 문장, 구조, 도표 | **대상이다** |
| 프레임워크 이름 | 상표일 수 있다 |

**스킬이 어느 쪽인지는 내용을 봐야 안다.** 프레임워크를 자기 말로 설명했으면 문제가 적고, 책의 설명을 옮겼으면 문제가 된다.

MIT로 배포하는 것이 더 복잡하다. MIT는 "자유롭게 쓸 수 있다"는 허락인데, **원저작물의 권리는 배포자가 허락할 수 있는 범위를 넘는다.**

`book-to-skill`은 도구이므로 MIT가 타당하다. 그 도구로 만든 결과물의 권리는 도구가 보장하지 않는다. `[확인 필요: book-to-skill이 저작권 경고를 포함하는지]`

## 쓰는 쪽의 점검표

| 순서 | 확인 | 방법 |
|---|---|---|
| 1 | 저장소 루트 `LICENSE` | 없으면 **모든 권리 유보** |
| 2 | 스킬 디렉터리의 `LICENSE.txt` | 루트에 없어도 여기 있을 수 있다 |
| 3 | 프런트매터 `license` 필드 | 짧은 표시 + 파일 참조 |
| 4 | `NOASSERTION`인가 | 원문을 읽어야 한다 |
| 5 | AGPL, CC-BY-SA인가 | 번들에 섞을 수 없다 |
| 6 | `assets/`의 자산 출처 | `THIRD_PARTY_NOTICES` 확인 |
| 7 | 변환된 원저작물인가 | 책, 강의 기반이면 별도 검토 |

**1번과 2번을 둘 다 봐야 한다.** `anthropics/skills`가 루트에 없고 스킬별로 있다. 1번만 보면 "라이선스 없음"으로 판단하고, 실제로는 Proprietary다.

## 만드는 쪽의 점검표

| 항목 | 왜 |
|---|---|
| 루트에 `LICENSE`를 둔다 | 깃허브가 식별하고 자동 검사가 통과한다 |
| 표준 라이선스를 수정 없이 쓴다 | 수정하면 `NOASSERTION`이 된다 |
| 프런트매터 `license`를 쓴다 | 스킬 단위로 복사될 때 따라간다 |
| 번들 자산의 출처를 적는다 | `THIRD_PARTY_NOTICES.md` |
| 복사한 스킬의 `LICENSE`를 같이 옮긴다 | `ComposioHQ`가 한 것 |
| 변환형이면 원저작물 경고를 넣는다 | 사용자에게 책임이 전가된다 |

**세 번째가 이 생태계에 특유하다.** 스킬은 디렉터리 단위로 복사된다. 루트 `LICENSE`만 두면 복사할 때 떨어진다. 프런트매터 `license` 필드와 스킬별 `LICENSE.txt`가 같이 따라간다.

`anthropics/skills`의 방식이 이 점에서 옳다. 깃허브 식별이 안 되는 대가로 **복사 단위에 라이선스가 붙는다.**

가장 좋은 것은 둘 다 두는 것이다. 루트에 `LICENSE`, 스킬마다 `LICENSE.txt`와 프런트매터 `license`.

## 생태계의 미해결 문제

**스킬은 코드인가 문서인가.** 이 질문에 답이 없어서 라이선스가 흩어진다. 코드로 보면 MIT, Apache, AGPL이고, 문서로 보면 CC 계열이다.

**섞는 것이 기본 사용법인데 섞을 수 없는 조합이 있다.** 수천 개를 모은 번들에 AGPL이나 CC-BY-SA가 섞여 있으면 번들 전체가 영향을 받는다. 확인하는 도구가 없다.

**큐레이션 작업 자체의 라이선스가 비어 있다.** 864개를 모은 저장소에 루트 라이선스가 없다.

`NVIDIA/SkillSpector`가 보안을 스캔한다([9.3](03-supply-chain.md)). **라이선스를 스캔하는 도구는 수집 데이터에서 보이지 않는다.** npm 생태계의 `license-checker`에 해당하는 것이 스킬 생태계에 없다.

이것이 비어 있는 자리이고, 만들 수 있는 것이다. `SKILL.md`의 프런트매터에서 `license`를 읽고, 디렉터리의 `LICENSE` 파일을 찾고, 번들 전체의 호환성을 확인하는 도구는 기술적으로 어렵지 않다.

---

다음 장: [9.5 중복과 포화](05-saturation.md)
