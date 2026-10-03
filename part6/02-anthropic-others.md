# 6.2 Anthropic — 그 외 저장소

`anthropics/skills`(179,497) 외에 Anthropic이 공개한 스킬 저장소가 넷 있다. 스타수 차이가 크고, 그 차이가 무엇을 뜻하는지가 이 장의 주제다.

| 스타 | 저장소 | 생성 | 푸시 | 라이선스 | SKILL.md |
|---|---|---|---|---|---|
| 37,338 | `claude-plugins-official` | 2025-11-20 | 2026-10-02 | Apache-2.0 | 33 |
| 7,542 | `defending-code-reference-harness` | 2026-05-22 | 2026-08-06 | NOASSERTION | 9 |
| 1,026 | `launch-your-agent` | 2026-06-16 | 2026-09-23 | Apache-2.0 | 2 |
| 544 | `k12-teacher-skills` | 2026-07-10 | 2026-09-01 | Apache-2.0 | 4 |

(수집 날짜: 2026-10-04. 확인 수준: 정밀 리뷰)

**라이선스가 `anthropics/skills`와 다르다.** 본 저장소는 `Proprietary`인데 이 넷 중 셋이 Apache-2.0이다. 가져다 쓰거나 포크할 때 중요한 차이이고, 어느 쪽이 기본인지 헷갈리기 쉽다.

## claude-plugins-official — 그릇과 내용

```
claude-plugins-official/
├── plugins/                 (공식 관리)
│   ├── claude-code-setup/skills/claude-automation-recommender/
│   ├── claude-md-management/skills/claude-md-improver/
│   ├── claude-security/skills/claude-security/
│   ├── cwc-makers/skills/{cardputer-buddy, m5-onboard}/
│   └── example-plugin/skills/example-command/
└── external_plugins/        (외부 기여)
    ├── discord/skills/{access, configure}/
    ├── imessage/skills/{access, configure}/
    └── telegram/skills/{access, configure}/
```

플러그인 저장소인데 `SKILL.md`를 33개 담고 있다. [1.4](../part1/04-boundaries.md)에서 정리한 관계가 구조로 나타난다. **플러그인은 그릇이고 스킬이 내용이다.**

### 두 가지 구조적 관찰

**`plugins/`와 `external_plugins/`를 나눴다.** 공식이 관리하는 것과 외부 기여를 디렉터리로 구분한다. 큐레이션 저장소에서 가장 중요한 정보가 "무엇을 검증했는가"인데([4.3](../part4/03-scale.md)), 이 저장소는 그 경계를 디렉터리 이름으로 표시한다. 수집 데이터의 큐레이션 저장소 다수가 이 구분을 하지 않는다.

**메신저 플러그인이 `access`와 `configure` 두 스킬로 쪼개져 있다.** Discord, iMessage, Telegram이 모두 같은 패턴이다. 설정하는 일과 접근하는 일을 분리했다. 트리거 조건이 다르기 때문이다 — 처음 붙일 때와 쓸 때는 다른 상황이고, 하나로 합치면 `description`이 두 범위를 다 잡아야 한다([2.6](../part2/06-promotion.md)의 쪼갤 시점).

### 스타수 해석의 어려움

37,338개가 33개 스킬 중 어디에 붙었는지 알 수 없다. 플러그인 디렉터리의 스타는 "여기 공식 플러그인이 모여 있다"는 사실에 붙는다.

비교해 보면 선명하다. `claude-plugins-official`(33개 스킬, 37,338)과 `blader/humanizer`(1개 스킬, 53,726)다. 스킬 한 개짜리 개인 저장소가 공식 플러그인 디렉터리보다 1.4배 주목받았다.

## defending-code-reference-harness — 공식 보안 스킬

```
.claude/skills/
├── threat-model/     위협 모델링
├── vuln-scan/        취약점 스캔
├── triage/           트리아지
├── patch/            패치
├── verify/           검증
├── dnr-hunt/         탐지, 대응 — 헌팅
├── dnr-respond/      탐지, 대응 — 대응
├── quickstart/
└── customize/
```

스킬 9개가 **보안 작업의 파이프라인 순서로 배치돼 있다.** 위협 모델링 → 스캔 → 트리아지 → 패치 → 검증이 한 흐름이다.

### 설계에서 읽히는 것

**단계마다 스킬을 쪼갰다.** 보안 감사를 하나의 스킬로 만들면 본문이 거대해지고 트리거 범위가 흐려진다. 단계별로 나누면 각 스킬의 `description`이 좁고 명확해진다.

**`verify`가 별도 스킬이다.** 패치하고 끝나지 않고 검증 단계가 독립 스킬로 있다. `anthropics/skills`의 `pdf`에서 `create_validation_image.py`가 번들에 있는 것과 같은 설계 철학이다 — **실행 뒤에 확인이 온다.**

**`customize`가 있다.** 조직마다 보안 기준이 다르므로 기본 스킬을 자기 기준으로 조정하는 경로를 스킬로 제공한다. 지시문을 고치라고 하는 대신 고치는 절차를 스킬로 만든 것이다.

### 두 가지 경고 신호

**마지막 푸시가 2026-08-06이다.** 수집 시점 기준 약 두 달 전이다. 다른 Anthropic 저장소들이 9월~10월에 갱신된 것과 대조된다.

보안 스킬에서 이 신호는 무게가 다르다. 취약점 패턴과 공격 기법은 계속 바뀐다. 이 저장소는 지식형 성분이 크고, **지식형은 수명이 가장 짧다**([4.2](../part4/02-three-types.md)). 두 달 공백이 치명적이라고 단정할 수는 없지만, 보안 영역에서는 확인하고 쓸 일이다.

**라이선스가 `NOASSERTION`이다.** 깃허브가 라이선스를 식별하지 못했다는 뜻이다. 파일이 있어도 표준 형식이 아니거나, 커스텀 조항이 섞인 경우에 이렇게 나온다. 다른 세 저장소가 명확히 Apache-2.0인데 이것만 다르다.

보안 스킬을 조직에 들이는 상황에서 라이선스가 불명확한 것은 실무적 장애다. 쓰기 전에 원문을 확인해야 한다. `[확인 필요: 라이선스 원문 조항]`

## launch-your-agent — 스킬 2개로 끝낸 저장소

| 스킬 | 역할 |
|---|---|
| `launch-your-agent` | 아이디어에서 배포된 서비스까지 |
| `wrap-up` | 마무리 |

스킬이 둘뿐이다. 설명이 "창업자를 아이디어에서 라이브 서비스까지 데려가는 Claude Code 스킬"이다.

**방법론형의 작은 예시로 볼 가치가 있다.** 범위가 넓은 작업(창업)을 스킬 두 개로 담았다. 할 일을 나열하는 대신 순서와 판단 기준만 담았을 가능성이 높다 — 그렇지 않으면 스킬 2개로 안 된다.

`wrap-up`이 별도 스킬인 점이 흥미롭다. 마무리를 분리한 것은 **작업이 끝나는 시점의 트리거가 다르다**는 판단이다. 시작할 때와 끝낼 때는 다른 상황이다.

스타 1,026개다. `defending-code-reference-harness`의 14%, `claude-plugins-official`의 3%다.

## k12-teacher-skills — 비개발 영역

| 스킬 | 역할 |
|---|---|
| `k12-lesson-plan-creation` | 수업 계획 작성 |
| `k12-lesson-prep` | 수업 준비 |
| `k12-lesson-differentiation` | 수준별 수업 설계 |
| `k12-check-for-understanding` | 이해도 확인 |

설명에 "K-12 교사와 **공동 개발**한 스킬 및 평가 루브릭"이라고 적혀 있다.

### 두 가지가 눈에 띈다

**평가 루브릭을 포함한다고 명시했다.** 생태계에 평가를 포함한 저장소가 드문 상황에서([5.4](../part5/04-patterns.md)) 이 점이 중요하다. 그리고 교육 영역은 출력이 주관적이라 평가가 어려운 영역인데, 루브릭이라는 형태로 접근했다. 주관적 영역에서 어서션을 억지로 붙이는 대신 루브릭을 쓰는 것은 타당한 선택이다([3.7](../part3/07-evals.md)).

**도메인 전문가와 공동 개발했다.** 스킬의 품질은 작성자가 그 도메인을 아는지에 달려 있다. 수업 계획을 짜 본 적 없는 사람이 쓴 수업 계획 스킬은 그럴듯한 일반론이 된다([3.1](../part3/01-capture-intent.md)).

스타 544개다. 저장소 넷 중 가장 적다.

## 이 네 저장소가 말하는 것

### 스타수는 도메인 크기를 따라간다

| 저장소 | 도메인 | 스타 |
|---|---|---|
| `claude-plugins-official` | 전체 (플러그인 디렉터리) | 37,338 |
| `defending-code-reference-harness` | 보안 | 7,542 |
| `launch-your-agent` | 창업 | 1,026 |
| `k12-teacher-skills` | K-12 교육 | 544 |

**품질 순서가 아니라 대상 인구 순서다.** 깃허브 사용자 중 K-12 교사의 비율이 개발자 비율보다 낮다. 스킬이 잘 만들어졌는지와 무관하게 스타수가 결정된다.

이것이 스타수를 점수로 쓰지 않는 또 하나의 이유다([0.2](../part0/02-why-stars.md)). `k12-teacher-skills`는 평가 루브릭을 포함하고 도메인 전문가와 공동 개발했다 — 수집 데이터의 많은 고스타 저장소보다 설계 근거가 분명하다. 스타는 544개다.

### 공식 저장소도 유지가 갈린다

| 저장소 | 마지막 푸시 |
|---|---|
| `claude-plugins-official` | 2026-10-02 |
| `launch-your-agent` | 2026-09-23 |
| `k12-teacher-skills` | 2026-09-01 |
| `defending-code-reference-harness` | 2026-08-06 |

"공식 저장소니까 유지된다"는 가정이 성립하지 않는다. 그리고 가장 오래된 것이 **보안 저장소**다. 유지 상태의 중요도가 도메인마다 다른데, 스타수와 푸시 날짜는 그 중요도를 반영하지 않는다.

### 비개발 영역으로 확장되고 있다

교육(K-12), 창업, 보안 운영이 들어왔다. 코딩 도구에서 시작한 규격이 코딩 밖으로 나가고 있다는 신호다.

수집 데이터에서 같은 방향의 증거를 더 찾을 수 있다. `career-ops-hq/career-ops`(73,378, 구직), `phuryn/pm-skills`(26,743, 제품 관리), `HKUSTDial/Supervisor-Skills`(7,864, 박사 지도), `bitwize-music-studio/claude-ai-music-skills`(528, 음악 제작)가 있다. [8.8](../part8/08-product.md)에서 다룬다.

---

다음 장: [6.3 OpenAI — openai/skills](03-openai.md)
