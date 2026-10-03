# 8.1 보안

보안은 스킬 생태계에서 가장 흥미로운 도메인이다. 세 종류가 다 있다. 방어 스킬, 공격 스킬, 그리고 **스킬 자체를 검사하는 스킬**이다.

| 스타 | 저장소 | SKILL.md | 성격 | 라이선스 | 푸시 |
|---|---|---|---|---|---|
| 23,902 | `cloudflare/security-audit-skill` | 1 | 방어 — 감사 | MIT | 2026-09-14 |
| 19,226 | `NVIDIA/SkillSpector` | — | **스킬 검사** | Apache-2.0 | 2026-10-02 |
| 7,542 | `anthropics/defending-code-reference-harness` | 9 | 방어 — 파이프라인 | NOASSERTION | 2026-08-06 |
| 7,351 | `trailofbits/skills` | 85 | 방어 — 감사, 연구 | **CC-BY-SA-4.0** | 2026-10-02 |
| 7,219 | `SnailSploit/Claude-Red` | 79 | **공격** | MIT | 2026-09-19 |
| 4,760 | `elementalsouls/Claude-BugHunter` | 83 | 공격 — 버그바운티 | MIT | 2026-10-03 |
| 3,385 | `ljagiello/ctf-skills` | 11 | CTF | MIT | 2026-09-13 |

(수집 날짜: 2026-10-04. 확인 수준: `cloudflare/security-audit-skill`, `NVIDIA/SkillSpector`는 [6.6](../part6/06-cloudflare.md), [6.8](../part6/08-others.md)에서 정밀 리뷰, 나머지 요약 리뷰)

## 방어 — 세 가지 설계

같은 문제(코드베이스의 취약점 찾기)에 세 가지 구조가 나왔다.

| 저장소 | 구조 | 스킬 수 | 스타 |
|---|---|---|---|
| `cloudflare/security-audit-skill` | 스킬 1개 + 참조 14개 | 1 | 23,902 |
| `anthropics/defending-code-reference-harness` | 단계별 스킬 | 9 | 7,542 |
| `trailofbits/skills` | 플러그인별 스킬 | 85 | 7,351 |

### 스킬 수가 적을수록 스타가 많다

1개 → 23,902. 9개 → 7,542. 85개 → 7,351.

[5.4](../part5/04-patterns.md)의 "개수가 주목과 반비례하는 구간"이 한 도메인 안에서 다시 확인된다. 이유는 설명의 선명도다. "코드베이스를 다단계 보안 감사한다"는 한 문장이고, 스킬 85개는 저장소를 열어야 무엇이 있는지 안다.

**다만 커버리지는 반대 방향이다.** 85개가 1개보다 훨씬 넓은 영역을 덮는다.

## trailofbits/skills — 전문 회사의 85개

| 항목 | 값 |
|---|---|
| 스타 | 7,351 |
| 생성 | 2026-01-14 |
| 푸시 | 2026-10-02 |
| 라이선스 | **CC-BY-SA-4.0** |
| `SKILL.md` | 85 |

Trail of Bits는 보안 감사 전문 회사다. **누가 만들었는지가 스타수보다 많은 것을 말하는 사례다.**

### 플러그인 단위로 묶었다

```
plugins/
├── agentic-actions-auditor/skills/agentic-actions-auditor/
├── audit-context-building/skills/audit-context-building/
└── building-secure-contracts/skills/
    ├── algorand-vulnerability-scanner/
    ├── cairo-vulnerability-scanner/
    ├── audit-prep-assistant/
    └── code-maturity-assessor/
```

`microsoft/skills`가 Azure 영역별로 플러그인을 나눈 것과 같은 구조다([6.5](../part6/05-microsoft.md)). 플러그인이 배포 단위이므로 설치 단위와 디렉터리를 일치시켰다.

### 두 가지가 눈에 띈다

**`agentic-actions-auditor`가 있다.** 에이전트의 행동을 감사하는 스킬이다. 보안 회사가 **에이전트 자체를 감사 대상으로 본다**는 신호다. `NVIDIA/SkillSpector`가 스킬을 검사하는 것과 같은 방향이고, 생태계가 자기를 위협 모델에 넣기 시작했다.

**블록체인 특화가 많다.** Algorand, Cairo(Starknet) 취약점 스캐너가 있다. Trail of Bits의 주력 영역이 반영된 것이고, **도메인 전문성이 스킬로 내려온 사례**다.

### 라이선스가 다르다

CC-BY-SA-4.0이다. 수집 데이터에서 드문 라이선스다.

| 라이선스 | 저장소 |
|---|---|
| MIT | `superpowers`, `ponytail`, `humanizer`, `Claude-Red`, `Claude-BugHunter`, `ctf-skills`, `security-audit-skill` |
| Apache-2.0 | `SkillSpector`, `open-code-review`, `claude-plugins-official` |
| **CC-BY-SA-4.0** | `trailofbits/skills` |
| Proprietary | `anthropics/skills` |
| NOASSERTION | `defending-code-reference-harness` |

CC-BY-SA는 **동일조건변경허락**(share-alike)이다. 이 스킬을 고쳐서 배포하면 같은 라이선스로 배포해야 한다. MIT와 섞어 쓸 때 제약이 생긴다.

스킬이 코드가 아니라 문서라서 문서 라이선스를 쓴 것으로 보인다. 타당한 선택이지만, **번들에 섞어 넣을 때 주의가 필요하다.** 스킬 여러 개를 모아 자기 번들로 만드는 큐레이션 저장소가 많은 생태계에서([7.4](../part7/04-awesome-lists.md)) 이 조건은 실무적 의미가 있다. [9.4](../part9/04-licensing.md)에서 다룬다.

## 공격 — Claude-Red와 Claude-BugHunter

### Claude-Red

| 항목 | 값 |
|---|---|
| 스타 | 7,219 |
| `SKILL.md` | 79 |
| 라이선스 | MIT |

설명이 명확하다.

> claude-red는 Claude 스킬 시스템을 위한 공격 보안 스킬 큐레이션 라이브러리다. 각 스킬은 특정 공격 표면에 대한 전문가 수준 방법론으로 Claude를 준비시키는 구조화된 `SKILL.md` 파일이다 — SQLi부터 셸코드, EDR 회피부터 익스플로잇 개발까지.

구조가 공격 표면별이다.

```
Skills/
├── active-directory/{offensive-active-directory, offensive-netexec}/
├── ai/offensive-ai-security/
├── api/{offensive-api-abuse, offensive-api-security}/
└── auth/offensive-jwt/
```

`cloudflare/security-audit-skill`이 참조 **파일**을 공격 분류별로 나눈 것과 같은 축인데, 이쪽은 **스킬**로 나눴다([6.6](../part6/06-cloudflare.md)).

`ai/offensive-ai-security`가 있다. AI 시스템 자체를 공격하는 방법론이다. `trailofbits/skills`의 `agentic-actions-auditor`와 공수가 맞는 쌍이다.

### Claude-BugHunter

| 항목 | 값 |
|---|---|
| 스타 | 4,760 |
| `SKILL.md` | 83 |
| 라이선스 | MIT |
| 푸시 | 2026-10-03 |

설명에 숫자가 많다.

> 버그 헌팅과 외부 레드팀 작업을 위한 Claude Code 스킬 번들 — 스킬 82개, 슬래시 명령 15개, **24개 핵심 취약점 분류에 걸쳐 선별한 공개 보고서 패턴 681개**, 엔터프라이즈 아이덴티티 + 인프라 공격 매트릭스.

**"공개 보고서 패턴 681개"가 설계의 핵심이다.** 실제로 공개된 버그바운티 보고서에서 패턴을 추출했다는 뜻이다.

이것이 [3.1](../part3/01-capture-intent.md)에서 말한 "가장 좋은 재료는 이미 한 작업의 기록"의 적용이다. 추상적인 취약점 분류가 아니라 **실제로 보상받은 보고서**에서 뽑았다.

`bugcrowd-reporting` 스킬이 있는 점도 실무적이다. 취약점을 찾는 것과 보고서를 쓰는 것은 다른 작업이고, 버그바운티에서는 보고서 품질이 보상을 결정한다. 그 단계를 스킬로 뒀다.

### 공격 스킬을 어떻게 볼 것인가

이 책의 입장을 적어 둔다.

공격 보안 스킬은 **인가된 테스트, 버그바운티, CTF, 보안 연구**의 도구다. 세 저장소 다 그 맥락을 설명에 명시한다 — "외부 레드팀 작업", "CTF 문제 풀이", "보안 연구". 방어를 설계하려면 공격을 알아야 하고, 그래서 공수 양쪽이 같은 생태계에 있는 것이 정상이다.

다만 리뷰할 때 확인할 것이 있다. **인가 맥락이 스킬 안에 적혀 있는가.** `description`이나 본문이 "인가된 범위에서만 쓴다"를 명시하는지, 범위 확인 단계를 절차에 두는지다. `[확인 필요: 세 저장소의 SKILL.md가 인가 범위 확인 단계를 포함하는지]`

## ctf-skills — 가장 평가하기 쉬운 보안 스킬

| 항목 | 값 |
|---|---|
| 스타 | 3,385 |
| `SKILL.md` | 11 |
| 라이선스 | MIT |

```
ctf-ai-ml/  ctf-crypto/  ctf-forensics/
ctf-malware/  ctf-misc/  ctf-osint/
(그 외 웹 공격, 바이너리 pwn, 리버싱 등)
```

CTF 분야별로 나눴다. 11개로 이 도메인에서 가장 적다.

**이 저장소가 평가 측면에서 특별하다.** CTF는 정답이 있다. 플래그를 찾으면 성공이고 못 찾으면 실패다.

[3.7](../part3/07-evals.md)에서 "테스트가 쉬운 스킬"과 "어려운 스킬"을 가른 표를 떠올리면, CTF는 가장 쉬운 쪽이다. 기준선 비교도 명확하다 — 스킬 있는 에이전트와 없는 에이전트에게 같은 문제를 주고 풀었는지 세면 된다.

**생태계에서 객관적 평가가 가장 쉬운 도메인인데, 그 평가가 있는지는 확인되지 않았다.** `[확인 필요: ctf-skills의 평가, 벤치마크 존재 여부]`

보안 도메인 전체로 넓혀도 같다. 취약점 탐지는 정답이 있는 작업이다(알려진 취약점이 심긴 코드베이스를 주면 된다). 그런데 수집한 보안 저장소 중 기준선 비교를 확인한 것이 없다.

## 가장 중요한 저장소는 방어도 공격도 아니다

`NVIDIA/SkillSpector`(19,226)다. **스킬을 검사한다.**

[6.8](../part6/08-others.md)에서 정밀 리뷰했다. 핵심 숫자를 다시 적는다.

> 연구 데이터셋에서 분석한 31,132개 스킬 부분집합에서 **26.1%의 스킬이 취약점을 포함**하고 **5.2%가 악의적 의도로 보인다.**

이 장에 실린 보안 저장소들이 `SKILL.md`를 합쳐 **268개** 담고 있다. 통계를 그대로 적용하면 그중 70개에 취약점이 있고 14개가 악성일 수 있다.

물론 이 통계를 특정 저장소에 적용할 수는 없다. 전체 분포이고, Trail of Bits 같은 전문 회사의 저장소가 평균과 같다고 볼 근거가 없다. **다만 보안 스킬을 설치하는 것이 보안 위험이라는 역설은 성립한다.**

### 탐지 패턴 중 보안 스킬에 걸리는 것들

`SkillSpector`의 17개 범주 중에 보안 스킬이 걸리기 쉬운 것들이 있다.

| 범주 | 보안 스킬에서 왜 문제인가 |
|---|---|
| 과도한 행위 권한 | 공격 스킬은 본래 강한 권한을 요구한다 |
| 위험 코드 (AST) | 익스플로잇 코드가 번들에 있을 수 있다 |
| 거부 우회 | 공격 방법론은 안전장치를 우회하는 모양이 된다 |
| 트리거 악용 | 공격 스킬이 의도치 않은 상황에 불리면 위험하다 |

**공격 스킬은 구조적으로 악성 스킬과 닮는다.** 정당한 공격 스킬과 악성 스킬을 기계가 구별하기 어렵다는 뜻이고, 반대로 악성 스킬이 "공격 보안 스킬"로 위장하기 쉽다는 뜻이다.

이 도메인에서 **출처와 라이선스 확인이 특히 중요하다.** `trailofbits/skills`는 회사 조직 계정이고, `cloudflare/security-audit-skill`도 그렇다. 개인 계정의 공격 스킬 번들은 같은 수준의 확인이 안 된다.

## 도메인 요약

### 강점

**공수 양쪽이 다 있다.** 방어(감사, 파이프라인), 공격(레드팀, 버그바운티, CTF), 메타(스킬 검사)가 전부 존재한다.

**실무 데이터에 기반한 설계가 있다.** `Claude-BugHunter`의 공개 보고서 패턴 681개가 그 예다.

**유지 상태가 좋다.** 일곱 저장소 중 다섯이 2026-09 이후 푸시다.

**전문 조직이 참여한다.** Trail of Bits, Cloudflare, NVIDIA, Anthropic이 각각 저장소를 낸다.

### 한계

**평가가 없다.** 객관적 평가가 가장 쉬운 도메인인데(정답이 있다) 기준선 비교를 확인한 저장소가 없다. `cloudflare/security-audit-skill`이 출력 스키마와 커버리지 장부를 검증하지만, 그건 형식 검증이고 기여 측정이 아니다.

**유지가 가장 중요한데 가장 오래된 것이 방어 스킬이다.** `anthropics/defending-code-reference-harness`가 2026-08-06으로 두 달 전이다. 공격 기법은 계속 바뀌고, 지식형 성분이 큰 저장소는 수명이 짧다([4.2](../part4/02-three-types.md)).

**공격 스킬과 악성 스킬의 경계가 기계로 구별되지 않는다.** 출처 확인이 유일한 방어선이고, 스킬 생태계에 출처 검증 표준이 없다([6.6](../part6/06-cloudflare.md)의 RFC가 Draft).

**라이선스가 섞여 있다.** MIT, Apache-2.0, CC-BY-SA-4.0, NOASSERTION이 다 있다. 보안 스킬을 조직에 들일 때 라이선스 검토가 필요하고, `NOASSERTION`은 원문을 읽어야 한다.

### 골라 쓰는 기준

| 상황 | 추천 |
|---|---|
| 코드베이스 전체 감사 | `cloudflare/security-audit-skill` (단일 스킬, 참조 분리) |
| 단계별로 제어하고 싶다 | `anthropics/defending-code-reference-harness` |
| 블록체인, 스마트 컨트랙트 | `trailofbits/skills` |
| 버그바운티 | `elementalsouls/Claude-BugHunter` |
| 특정 공격 표면 학습 | `SnailSploit/Claude-Red` |
| CTF | `ljagiello/ctf-skills` |
| **설치 전 검사** | `NVIDIA/SkillSpector` |

마지막 줄을 먼저 한다. 보안 스킬을 설치하기 전에 그 스킬을 검사하는 것이 순서상 맞다.

---

다음 장: [8.2 코드리뷰](02-code-review.md)
