# 6.6 Cloudflare — security-audit-skill 외

| 저장소 | 스타 | 생성 | 푸시 | 라이선스 | SKILL.md |
|---|---|---|---|---|---|
| `cloudflare/security-audit-skill` | 23,902 | 2026-06-18 | 2026-09-14 | MIT | 1 |
| `cloudflare/skills` | 2,974 | — | — | — | 16 |
| `cloudflare/agent-skills-discovery-rfc` | 351 | — | — | — | 0 |

(수집 날짜: 2026-10-04. 확인 수준: 정밀 리뷰)

Cloudflare는 빅테크 중 유일하게 **단일 목적 스킬로 성공했다.** 그리고 생태계의 구조적 공백에 규격 제안을 냈다.

## security-audit-skill — 공식 번들을 8배 앞선 단일 스킬

같은 회사의 두 저장소를 비교하면 이 장의 주제가 바로 나온다.

| 저장소 | 스킬 수 | 스타 |
|---|---|---|
| `cloudflare/security-audit-skill` | **1** | 23,902 |
| `cloudflare/skills` | 16 | 2,974 |

**스킬 한 개짜리가 공식 번들의 8배다.**

`cloudflare/skills`는 자사 제품 사용법이다 — `durable-objects`, `agents-sdk`, `nextjs-on-cloudflare`, `cloudflare-email-service`, `k2`, `basin` 등 16개다. Google, Microsoft의 공식 저장소와 같은 성격이고 같은 스타 구간(세 자리~네 자리)에 있다.

`security-audit-skill`은 다르다. 제품 사용법이 아니고 **작업을 푼다.** 코드베이스를 보안 감사하는 일이다. Cloudflare를 쓰지 않는 사람도 쓴다.

96일에 2만 4천 스타, 일평균 225개다. 같은 기간 `anthropics/claude-code`의 일평균(254)에 근접한다([0.2](../part0/02-why-stars.md)).

### 구조 — 단일 스킬인데 번들이 두껍다

```
skills/security-audit/
├── SKILL.md
├── RECONNAISSANCE.md
├── ATTACK-CLASSES.md
├── HUNTING.md
├── VALIDATION-AND-REPORTING.md
├── WEB-PROTOCOL-AND-AUTH.md
├── CLIENT-SIDE.md
├── MEMORY-SAFETY-AND-BINARY.md
├── PROTOCOLS-RPC-AND-MESSAGING.md
├── DATA-ISOLATION-AND-LIFECYCLE.md
├── CLOUD-AND-DEPLOYMENT.md
├── DESKTOP-MOBILE-AND-LOCAL-IPC.md
├── RESOURCE-EXHAUSTION-AND-AVAILABILITY.md
├── SUPPLY-CHAIN-AND-RELEASE.md
├── AI-AND-LLM.md
├── report-schema.json
├── validate-coverage-ledger.cjs
├── validate-coverage-ledger.test.cjs
├── validate-findings.cjs
└── validate-findings.test.cjs
```

`SKILL.md`는 하나인데 참조 파일이 14개다. **점진적 공개를 제대로 쓴 단일 스킬**이다.

`blader/humanizer`(53,726)와 대조하면 차이가 선명하다. 그쪽은 `SKILL.md` 한 파일에 397줄 32KB를 다 넣었다. 트리거될 때마다 32KB가 전부 읽힌다([5.2](../part5/02-top50.md)). 이쪽은 공격 분류별로 쪼개서, 웹 취약점을 보는 감사에서 메모리 안전성 문서를 읽지 않는다.

### 공격 분류로 쪼갠 설계

참조 파일 이름이 **공격 표면**이다. 웹/프로토콜, 인증, 클라이언트 사이드, 메모리 안전성, 바이너리, RPC, 메시징, 데이터 격리, 생애주기, 클라우드, 배포, 데스크톱, 모바일, IPC, 자원 소진, 가용성, 공급망, 릴리스, AI, LLM.

[3.4](../part3/04-references.md)에서 다룬 도메인별 분리의 실제 적용이다. 감사 대상이 웹 앱이면 웹 문서를, 바이너리면 메모리 문서를 읽는다. 예시가 범위를 좁히는 문제도 같이 해결된다 — 본문에 웹 예시만 있으면 바이너리 감사가 약해진다([2.5](../part2/05-examples.md)).

### 절차가 파일 순서에 있다

`RECONNAISSANCE` → `ATTACK-CLASSES` → `HUNTING` → `VALIDATION-AND-REPORTING`이 감사 파이프라인이다. 정찰, 공격 분류 파악, 헌팅, 검증, 보고 순이다.

`anthropics/defending-code-reference-harness`가 같은 흐름을 스킬 9개로 나눈 것과 대조된다([6.2](02-anthropic-others.md)). 한쪽은 스킬 9개, 한쪽은 스킬 1개 + 참조 파일 14개다.

| | `defending-code-reference-harness` | `security-audit-skill` |
|---|---|---|
| 구조 | 스킬 9개 | 스킬 1개 + 참조 14개 |
| 트리거 | 단계마다 별도 | 한 번 |
| 장점 | 각 단계를 따로 부를 수 있다 | 트리거 충돌이 없다 |
| 단점 | 9개가 서로 경쟁한다 | 전체 감사만 가능 |
| 스타 | 7,542 | 23,902 |

같은 문제에 대한 두 설계가 실제로 존재하고, 단일 스킬 쪽이 3배 주목받았다. 설계의 우열이 아니라 **설명의 선명도 차이**로 보인다. "코드베이스를 다단계 보안 감사한다"는 한 문장이고, 스킬 9개는 저장소를 열어야 무엇이 있는지 안다.

### 검증 스크립트를 번들했다

```
report-schema.json
validate-coverage-ledger.cjs      + .test.cjs
validate-findings.cjs             + .test.cjs
```

`.test.cjs`가 있다. **검증 스크립트 자체의 테스트**다. 생태계에서 드문 수준이다.

`report-schema.json`은 출력 형식을 기계가 검증할 수 있게 만든 것이고([2.4](../part2/04-output-format.md)), `validate-findings.cjs`가 발견 항목이 스키마를 만족하는지 검사한다. `validate-coverage-ledger.cjs`는 커버리지 장부를 검사한다 — 감사에서 어느 공격 분류를 봤는지 추적하는 장치로 읽힌다.

**이것이 보안 감사 스킬에서 중요한 이유**가 있다. 감사의 실패 방식은 "틀린 것을 찾는 것"이 아니라 "안 본 영역을 봤다고 하는 것"이다. 커버리지 장부를 검증하면 그걸 막는다.

다만 평가(기준선 비교)는 없다. 출력 형식과 커버리지를 검증하는 것은 **스킬이 제 형식을 지켰는지**를 재는 것이고, 스킬이 없을 때보다 나은지를 재는 것이 아니다([3.7](../part3/07-evals.md)).

## agent-skills-discovery-rfc — 351스타의 규격 제안

| 항목 | 값 |
|---|---|
| 스타 | 351 |
| 상태 | Draft, v0.2.0 |
| 공개 | 2026-01-17 |
| 갱신 | 2026-03-12 |

스타 351개다. 이 책이 다루는 저장소 중 가장 적다. 그런데 생태계의 구조적 공백을 정면으로 다룬다.

### 문제 정의

RFC가 적은 문제다.

> 오늘날 스킬을 발견하려면 이것이 필요하다.
> - 깃허브 저장소 검색
> - 벤더 문서 읽기
> - 소셜 미디어에 공유된 링크 따라가기
> - 최종 사용자의 수동 설정
>
> "**example.com은 어떤 스킬을 공개하는가**"에 답하는 표준 방법이 없다.

이 책의 작업이 그 증거다. 458개 저장소를 모으려고 토픽 6개를 검색하고 기준점 21개를 직접 지정했다. 그리고 상위 150개의 파일 트리를 조회해서 스킬 저장소인지 판정했다([5.1](../part5/01-collection.md)). **표준 디스커버리가 있으면 이 작업이 필요 없다.**

### 해결 방식

`agent-skills`를 `.well-known` URI 접미사로 등록한다. RFC 8615 기반이다.

```
https://example.com/.well-known/agent-skills/
```

**조직이 자기 도메인에 스킬을 게시한다.** 깃허브가 아니라 도메인이 출처가 된다.

### 목차에서 읽히는 완성도

17개 절이 있다. 그중 셋이 중요하다.

| 절 | 왜 중요한가 |
|---|---|
| Progressive Disclosure | 규격의 핵심 원리를 디스커버리 계층에도 적용 |
| **Integrity and Verification** | 가져온 스킬이 조작되지 않았는지 확인 |
| **Security Considerations** | 스킬이 공격면이라는 인식 |

Integrity 절이 있다는 사실이 이 제안을 다른 디스커버리 접근과 가른다.

| 접근 | 주체 | 무결성 검증 |
|---|---|---|
| 설치 스킬(`skill-installer`) | OpenAI | 없음 |
| 인덱스 파일(`index.json`) | Google | 없음 |
| `.well-known` + 서명 | Cloudflare | **있음** |

Google의 `index.json`은 `entrypoint`로 raw 깃허브 URL을 준다([6.4](04-google.md)). 그 URL의 내용이 바뀌어도 알 수 없다. 스킬은 에이전트가 읽고 그대로 따르는 지시문이므로, 내용이 바뀌면 동작이 바뀐다. [9.3 공급망 위험](../part9/03-supply-chain.md)에서 다룬다.

### 왜 351스타인가

RFC는 스타가 붙는 물건이 아니다. 쓸 수 있는 스킬이 들어 있지 않고, 설치할 것도 없다. 읽고 구현하는 문서다.

**그래서 스타수로는 이 저장소의 중요도를 재지 못한다.** 생태계에 규격 제안이 몇 개 있는지, 그 제안이 채택되는지는 스타수와 무관하게 결정된다.

[5.3](../part5/03-rest.md)에서 이 저장소를 "정밀 리뷰로 올리는" 목록에 넣은 이유다.

## 평가

### 강점

**단일 목적 스킬의 모범이다.** `security-audit-skill`은 스킬 1개에 참조 파일 14개로 점진적 공개를 제대로 썼다. 공격 분류별 분리는 도메인 분리의 교과서적 적용이다.

**검증 스크립트에 테스트가 있다.** 생태계에서 드물다. 커버리지 장부 검증은 감사 스킬의 핵심 실패 모드를 막는다.

**MIT 라이선스다.** `anthropics/skills`의 `Proprietary`와 대조된다([9.4](../part9/04-licensing.md)).

**디스커버리 공백에 규격을 냈다.** 무결성 검증과 보안 고려사항을 포함한 유일한 접근이다.

### 한계

**평가(기준선 비교)가 없다.** 형식과 커버리지는 검증하지만 스킬의 기여를 측정하지 않는다.

**공식 번들이 묻혔다.** `cloudflare/skills`(16개, 2,974)는 자사 제품 사용법으로 구성돼 있고 주목을 못 받는다. 다른 빅테크 공식 저장소와 같은 처지다.

**RFC가 Draft에 머물러 있다.** v0.2.0이고 마지막 갱신이 2026-03-12다. 채택 여부가 불확실하다. 그리고 경쟁 접근(OpenAI의 설치 스킬, Google의 인덱스 파일)이 이미 각자 돌아가고 있다 — **표준이 나오기 전에 관례가 자리 잡는 전형적인 상황**이다.

### 누가 읽어야 하나

| 목적 | 볼 것 |
|---|---|
| 단일 스킬에서 참조 파일 설계 | `skills/security-audit/`의 14개 파일 구성 |
| 출력 형식 검증 | `report-schema.json`, `validate-findings.cjs` |
| 감사 커버리지 추적 | `validate-coverage-ledger.cjs` |
| 디스커버리 문제의 정의 | RFC의 Problem 절 |
| 스킬 공급망 위험 | RFC의 Integrity and Verification 절 |

---

다음 장: [6.7 GitHub — awesome-copilot, copilot-plugins](07-github.md)
