# 11.10 보안 스킬 — 분류를 가로지르는 묶음

보안은 [11.1](01-taxonomy.md)의 작업 대상 축으로 나누면 **두 군데로 흩어진다.**

| 범주 | 지키는 대상 |
|---|---|
| A3 보안 | **코드** — 내 코드의 취약점 |
| G3 스킬 보안 검사 | **에이전트** — 설치한 스킬이 나를 공격하는 것 |

MECE를 유지하려고 작업 대상을 우선했고, 그래서 보안이 쪼개졌다. 실무에서는 둘을 같이 봐야 하므로 이 장에서 묶는다.

**두 방향이 비대칭이다.** 코드 보안은 도구가 여럿인데, 스킬 보안은 생태계 전체에 사실상 두 저장소뿐이다.

---

## 왜 스킬 보안이 따로 필요한가

[9.3](../part9/03-supply-chain.md)의 숫자를 다시 적는다.

> 분석한 31,132개 스킬 중 **26.1%가 취약점을 포함**하고 **5.2%가 악의적 의도로 보인다.**

(출처: `NVIDIA/SkillSpector` README, 2026-10-04 확인)

세 조건이 겹친다.

| 조건 | 내용 |
|---|---|
| 스킬은 **실행되는 지시문**이다 | 에이전트가 읽고 그대로 따른다 |
| 설치 비용이 0이다 | 파일 복사. 레지스트리도 서명도 없다 |
| 검증이 불가능한 규모다 | 8,212개를 읽을 수 없다 |

**스킬은 설치하는 순간 내 권한으로 움직인다.** 파일을 읽고 쓰고 명령을 실행하고 네트워크에 접근한다.

---

## 전체 목록 — 검증 결과

주목할 보안 저장소를 한 표에 모았다. **직접 조회해서 확인한 값이다.**

| 스타 | 저장소 | SKILL.md | 라이선스 | 마지막 푸시 | 지키는 대상 |
|---|---|---|---|---|---|
| 23,894 | `cloudflare/security-audit-skill` | 1 | MIT | 2026-09-14 | 코드 |
| 19,240 | `NVIDIA/SkillSpector` | 27 | Apache-2.0 | 2026-10-02 | **스킬** |
| 7,541 | `anthropics/defending-code-reference-harness` | 9 | NOASSERTION | 2026-08-06 | 코드 |
| 7,352 | `trailofbits/skills` | 85 | **CC-BY-SA-4.0** | 2026-10-02 | 코드 |
| 7,217 | `SnailSploit/Claude-Red` | 79 | MIT | 2026-09-19 | 코드(공격) |
| 6,294 | `anthropics/claude-code-security-review` | **0** | MIT | **2026-02-11** | 코드 |
| 4,760 | `elementalsouls/Claude-BugHunter` | 83 | MIT | 2026-10-03 | 코드(공격) |
| 3,385 | `ljagiello/ctf-skills` | 11 | MIT | 2026-09-13 | 코드(CTF) |
| 286 | `tanviet12/vbsec` | 3 | MIT | 2026-09-28 | 코드 |
| 226 | `AgriciDaniel/claude-cybersecurity` | 1 | MIT | **2026-04-15** | 코드 |
| 36 | `efij/awesome-claude-code-security` | 0 | NOASSERTION | **2026-03-12** | 목록 |
| 13 | `RationalEyes/claude-skills-security-guide` | 9 | MIT | **2026-03-30** | **스킬** |

(수집 날짜: 2026-10-04. 확인 수준: 저장소 메타데이터와 파일 트리 직접 조회)

---

## 검증에서 드러난 것

### 1. 절반이 정지 상태다

| 저장소 | 마지막 푸시 | 경과 |
|---|---|---|
| `claude-code-security-review` | 2026-02-11 | **약 8개월** |
| `efij/awesome-claude-code-security` | 2026-03-12 | 약 7개월 (**생성일과 같은 날**) |
| `RationalEyes/claude-skills-security-guide` | 2026-03-30 | 약 6개월 |
| `AgriciDaniel/claude-cybersecurity` | 2026-04-15 | 약 6개월 |

**보안 영역에서 이 공백의 무게가 다르다.** 취약점 패턴과 공격 기법은 계속 바뀌고, 이 저장소들은 지식형 성분이 크다([4.2](../part4/02-three-types.md)).

`efij/awesome-claude-code-security`는 특히 분명하다. **생성일(2026-03-12)과 마지막 푸시가 같은 날이다.** 40KB짜리 목록을 올리고 한 번도 갱신하지 않았다. 목록은 갱신되지 않으면 폐기된 저장소를 추천한다([7.4](../part7/04-awesome-lists.md)).

### 2. 하나는 스킬이 아니다

`anthropics/claude-code-security-review`는 **`SKILL.md`가 0개다.**

```
action.yml          ← GitHub Action 정의
claudecode/         ← 파이썬 패키지
docs/  examples/  scripts/
```

**GitHub Action이지 스킬이 아니다.** PR이 열릴 때 자동으로 돌고 댓글을 남기는 CI 도구다.

이 구분이 실무적으로 중요하다. [1.4](../part1/04-boundaries.md)의 기준으로 보면 **이건 훅의 영역이다** — 판단 없이 항상 실행된다. 스킬은 트리거되지 않는 날에 통과한다.

**"머지 전 마지막 관문"이 필요하면 스킬이 아니라 이것이 맞다.** 다만 8개월 정지 상태를 감안하고 쓴다.

### 3. 가장 엄격한 저장소가 286스타다

`tanviet12/vbsec`에 **언어별 기대 출력 픽스처**가 있다.

```
scripts/check-fixtures.py
scripts/run-fixtures.sh
tests/expected/
├── python.json
├── go.json          go-hard.json
├── php.json         php-hard.json
└── dotnet.json
```

**스캐너 출력을 언어별 기대값과 대조하는 회귀 테스트다.** 이 묶음에서 유일하다.

[9.2](../part9/02-measuring-quality.md)의 다섯 축 중 B(기여)에 해당한다. 알려진 취약점이 심긴 코드를 주고 찾는지 세는 방식이고, 보안은 그게 가능한 도메인인데 **대부분의 저장소가 하지 않는다.**

`-hard` 변형을 따로 둔 점도 눈에 띈다. 쉬운 케이스와 어려운 케이스를 나눠서 재면 변별력이 생긴다([3.7](../part3/07-evals.md)).

**286스타다.** `trailofbits/skills`(7,352)의 4%다.

### 4. 공격 예시 스킬을 담은 저장소가 있다

`RationalEyes/claude-skills-security-guide`의 `SKILL.md` 9개 구성이다.

| 디렉터리 | 스킬 | 성격 |
|---|---|---|
| `skills/` | `security-monitor`, `hash-verifier`, `output-sanitizer` | **방어** |
| `examples/` | `env-exfil`, `self-replicating`, `poisoned-output`, `covert-formatter`, `multi-agent-propagation`, `sensitive-trigger` | **공격 예시** |

**위협 분류를 글이 아니라 실물 스킬로 담았다.** `docs/threat-taxonomy.md`(20KB)와 `technical-manual.md`(128KB)가 함께 있다.

공격 예시 여섯 개의 이름이 그대로 위협 목록이다.

| 예시 스킬 | 공격 방식 |
|---|---|
| `env-exfil` | 환경변수 유출 |
| `self-replicating` | 자기 복제 |
| `poisoned-output` | 출력 오염 |
| `covert-formatter` | 은닉된 포매터 |
| `multi-agent-propagation` | 에이전트 간 전파 |
| `sensitive-trigger` | 민감 트리거 |

`NVIDIA/SkillSpector`의 탐지 범주와 겹친다 — 데이터 유출, 메모리 오염, 트리거 악용이다([11.8](08-meta.md)의 G3).

**스캐너를 검증할 재료로 쓸 수 있다.** 탐지 도구가 이 여섯 개를 잡는지 돌려 보면 된다.

**다만 그 자체가 악성 패턴이다.** 저장소에 의도적으로 악성 스킬이 들어 있으므로, 복사해 쓰지 않도록 주의한다. 13스타라 노출이 적다는 점이 역설적으로 완화 요인이다.

### 5. 자기 저장소를 감사한 사례

`AgriciDaniel/claude-cybersecurity`가 `SECURITY-AUDIT-2026-04-15.md`를 커밋했다. `PRIVACY.md`, `SECURITY.md`, `CONTRIBUTING.md`도 있다.

**보안 스킬이 자기 자신을 감사한 보고서를 공개한 사례다.** 226스타 저장소에서 이 정도 문서를 갖춘 것은 드물다.

다만 **"8개 전문 에이전트"는 구조가 아니다.** `SKILL.md`는 1개이고, 에이전트별 파일은 `assets/agents-chart.svg`(그림)뿐이다. 여덟 개의 역할 분담이 본문 안에 서술돼 있는 구조로 읽힌다.

**설명의 숫자와 저장소 구조가 다를 수 있다는 사례다.** 설치 전에 파일 트리를 보는 것이 맞다.

---

## 언제 무엇을 쓰나

### 상황별 선택

| 상황 | 추천 | 이유 |
|---|---|---|
| **남이 만든 스킬을 설치하기 직전** | `NVIDIA/SkillSpector` | 스킬 자체를 검사하는 유일한 활성 도구 |
| 팀 작업, 머지 전 마지막 관문 | `claude-code-security-review` | GitHub Action이라 **누락이 없다**. 8개월 정지 감안 |
| 코드베이스 전체 감사 | `cloudflare/security-audit-skill` | 스킬 1개 + 참조 14개. 검증 스크립트에 테스트가 있다 |
| 단계별로 제어 | `anthropics/defending-code-reference-harness` | 위협 모델링 → 스캔 → 트리아지 → 패치 → 검증 |
| 블록체인, 스마트 컨트랙트 | `trailofbits/skills` | 보안 전문 회사. **CC-BY-SA 확인** |
| 보안을 잘 모르는데 배포 직전 | `tanviet12/vbsec` | 21종 + 공격 방식 + 고친 코드. **회귀 테스트 있음** |
| 변경분만 빠르게 | `AgriciDaniel/claude-cybersecurity` | 전체/변경분 모드 선택. 6개월 정지 감안 |
| 버그바운티 | `elementalsouls/Claude-BugHunter` | 공개 보고서 패턴 681개 |
| 특정 공격 표면 학습 | `SnailSploit/Claude-Red` | 공격 표면별 분할 |
| CTF | `ljagiello/ctf-skills` | 정답이 있는 영역 |
| 스킬 공격 유형 공부 | `RationalEyes/...-security-guide` | 위협 분류 + 실물 예시 |
| 지도부터 보고 싶다 | `efij/awesome-...-security` | **7개월 정지.** 목록으로만 쓴다 |

### 순서

**설치 전 검사가 가장 먼저다.** 보안 스킬을 설치하는 것 자체가 보안 위험이다.

```
1. SkillSpector 로 설치할 스킬을 스캔
2. 머지 전 관문은 훅이나 GitHub Action 으로 (스킬 아님)
3. 코드 감사 스킬은 그다음
```

악성 스킬의 품질을 측정하는 것은 의미가 없다([9.2](../part9/02-measuring-quality.md)).

---

## 이 범주의 구조적 문제

### 공격 스킬과 악성 스킬이 기계로 구별되지 않는다

| `SkillSpector` 탐지 범주 | 정당한 공격 스킬에서 |
|---|---|
| 과도한 행위 권한 | 공격 스킬은 본래 강한 권한을 요구한다 |
| 위험 코드 (AST) | 익스플로잇 코드가 번들에 있다 |
| 거부 우회 | 공격 방법론은 안전장치를 우회하는 모양이 된다 |
| 트리거 악용 | 공격 스킬이 의도치 않게 불리면 위험하다 |

**악성 스킬이 "공격 보안 스킬"로 위장하기 쉽다.** 이 장의 목록에 공격 스킬 묶음이 셋 있고 합쳐서 `SKILL.md` 170개가 넘는다.

**출처가 유일한 방어선이다.** 조직 계정(`cloudflare`, `anthropics`, `trailofbits`, `NVIDIA`)과 개인 계정의 무게가 다르다.

### 평가가 가장 쉬운데 거의 없다

보안은 객관적 평가가 가능하다. 알려진 취약점이 심긴 코드를 주고 찾는지 세면 된다.

| 저장소 | 평가 |
|---|---|
| `tanviet12/vbsec` | **언어별 기대 출력 픽스처** |
| `cloudflare/security-audit-skill` | 출력 스키마 + 커버리지 장부 검증 (형식 검증) |
| 나머지 | 확인되지 않음 |

**둘뿐이고, 기준선 비교를 하는 곳은 없다.**

`cloudflare`의 커버리지 장부가 흥미롭다. 감사의 실패 방식은 "틀린 것을 찾는 것"이 아니라 "**안 본 영역을 봤다고 하는 것**"이고, 장부를 검증하면 그걸 막는다.

### 라이선스가 제각각이다

| 라이선스 | 저장소 |
|---|---|
| MIT | 6개 |
| Apache-2.0 | `SkillSpector` |
| **CC-BY-SA-4.0** | `trailofbits/skills` — **동일조건변경허락** |
| **NOASSERTION** | `defending-code-reference-harness`, `efij/awesome-...` |

**`trailofbits`를 MIT 번들에 섞을 수 없다.** 고쳐서 배포하면 같은 라이선스로 배포해야 한다([9.4](../part9/04-licensing.md)).

**`NOASSERTION` 둘은 원문을 읽어야 한다.** 보안 스킬을 조직에 들이는 상황에서 라이선스 불명은 실무적 장애다.

### 스킬을 지키는 도구가 둘뿐이다

| 저장소 | 스타 | 상태 |
|---|---|---|
| `NVIDIA/SkillSpector` | 19,240 | 활성 |
| `RationalEyes/claude-skills-security-guide` | 13 | 6개월 정지 |

**생태계 전체에서 "스킬로부터 나를 지키는" 도구가 사실상 하나다.** 그리고 그 하나가 제시한 숫자가 26.1%와 5.2%다.

코드 보안 도구는 열 개 넘게 있는데 스킬 보안 도구는 하나다. **비대칭이 분명하고, 비어 있는 자리다**([9.5](../part9/05-saturation.md)).

---

## 요약 — 세 줄

**설치 전 스캔이 먼저다.** 스킬 네 개 중 하나에 취약점이 있고, 검사하는 도구는 사실상 하나다.

**머지 전 관문은 스킬이 아니다.** 누락이 사고인 검사는 훅이나 GitHub Action으로 간다.

**이 범주에서는 마지막 푸시 날짜를 스타수보다 먼저 본다.** 목록의 절반이 수개월 정지 상태이고, 공격 기법은 그 사이에 바뀐다.

---

여기까지가 11부다. 처음으로: [11.1 분류 체계](01-taxonomy.md)
