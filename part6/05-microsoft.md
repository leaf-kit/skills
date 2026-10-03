# 6.5 Microsoft — skills, dotnet/skills, SkillOpt, skill-recorder

| 저장소 | 스타 | 생성 | 푸시 | SKILL.md |
|---|---|---|---|---|
| `microsoft/SkillOpt` | 17,979 | 2026-05-08 | 2026-09-30 | 5 |
| `dotnet/skills` | 5,543 | 2026-02-03 | 2026-10-03 | 108 |
| `microsoft/skill-recorder` | 4,185 | — | — | — |
| `microsoft/skills` | 3,075 | — | — | 205 |
| `microsoft/azure-skills` | 1,532 | — | — | — |

(수집 날짜: 2026-10-04. 확인 수준: `dotnet/skills` 정밀 리뷰, 나머지 요약 리뷰)

Microsoft는 이 생태계에서 가장 흥미로운 사례다. 스타수로는 전부 하위권인데, **엔지니어링 수준은 데이터셋 최고다.**

## dotnet/skills — 이 책에서 가장 중요한 저장소

스타 5,543개로 1위 `obra/superpowers`(294,779)의 **1.9%다.** 톱 30에 들지 못했다.

그런데 이 저장소에는 생태계의 다른 어디에도 없는 것이 있다.

### CI에 들어간 평가 인프라

```
eng/skill-validator/src/
├── Check/
│   ├── AgentProfiler.cs
│   ├── ExternalDependencyChecker.cs
│   ├── ReferenceScanner.cs
│   ├── SkillProfiler.cs
│   └── PluginProfiler.cs
└── Evaluate/
    ├── AgentRunner.cs
    ├── AssertionEvaluator.cs
    ├── BaselineStore.cs        ← 기준선 저장
    ├── Comparator.cs           ← 비교
    └── ConsolidateCommand.cs

eng/eval-quality/
├── check_eval_quality.py
├── selftest_eval_quality.py
└── underpowered-allowlist.txt

.github/workflows/
├── eval-quality.yml
├── evaluation.yml
├── evaluation-run.yml
└── evaluation-workflow-tests.yml
```

`BaselineStore`와 `Comparator`가 있다. [3.7](../part3/07-evals.md)에서 "기준선 없는 평가는 평가가 아니다"라고 쓴 것이 코드로 구현돼 있다. 평가 관련 경로가 178개다.

### 평가 품질 게이트 — 평가를 평가한다

`eng/eval-quality/README.md`의 첫 단락이다.

> `check_eval_quality.py`는 평가 결과를 오염시킬 수 있는 구조적 결함을 차단한다. 대부분은 **평가가 자기 기준선에게 알 수 없이 패배했거나, 모든 시행에서 이겼는데도 실패한 뒤에야** 발견된 것들이다.

이 두 증상이 평가 설계 실패의 교과서적 사례다.

- **자기 기준선에게 패배** — 스킬이 결과를 나쁘게 만든다. [3.7](../part3/07-evals.md)의 변별력 표에서 "기준선만 통과 → 스킬이 해를 끼침"에 해당한다.
- **모든 시행에서 이겼는데 실패** — 어서션이 틀렸거나 측정이 깨졌다.

**이 저장소는 그 경험을 코드로 굳혔다.** 같은 함정에 다시 빠지지 않게 CI가 막는다.

막는 결함의 예다.

| 검사 | 막는 상황 |
|---|---|
| 참조된 픽스처가 디스크에 없음 | 설정 단계에서 실패하는데 **스킬 실패로 읽힌다** |
| 픽스처가 git으로 복원되지 않음 | 로컬에는 있고 CI 러너에는 없다 |
| 빈 픽스처 디렉터리 | git이 빈 디렉터리를 보존하지 않는다 |

첫 번째가 특히 교활하다. 입력 파일이 없어서 실패한 것을 "스킬이 못했다"로 기록하면, 평가 결과 전체가 거짓이 된다. 이 결함은 수동 채점으로는 거의 발견되지 않는다.

### 통계적 검정력을 따진다

`underpowered-allowlist.txt`의 머리 주석이다.

> `check_eval_quality.py`가 강제하는 **서로 다른 자극(stimulus) 5개 하한선** 아래인 평가들.
>
> 서로 다른 자극 하나가 게이트 투표 하나를 준다. **반복 실행은 그 자극의 신뢰도를 재는 것이고 독립 과제 표본을 늘리지 않는다.** 자극이 5개 미만이면 부호 검정이 어떤 효과 크기에서도 p ≤ 0.05에 도달할 수 없으므로, 어댑터는 이를 **검정력 부족**으로 보고한다 — 합격도 회귀도 아니다.

세 가지가 들어 있다.

**1. 반복 실행과 독립 표본을 구분한다.** 같은 테스트를 세 번 돌리면 재현성을 알게 되지만 테스트가 세 개가 되는 것은 아니다. 이 책 [3.7](../part3/07-evals.md)에서 "같은 케이스를 여러 번 돌려 분산을 본다"고 했는데, 그것이 **표본 수를 늘리지 않는다**는 점까지 명시한 것이다.

**2. 검정력 하한을 숫자로 정했다.** 자극 5개 미만이면 통계적으로 유의한 결론이 불가능하다. 그래서 그 평가를 "통과"로도 "실패"로도 기록하지 않고 **검정력 부족**으로 따로 분류한다.

이 책의 측정 사례는 테스트 케이스가 3개였다([10.2](../part10/02-validation.md)). 이 기준으로는 검정력 부족이다. 통과율 100% 대 71%라는 결과를 "유의하다"고 쓸 수 없다. 그 사실을 적어 두는 것이 정직한 처리다.

**3. 면제 목록을 축소 전용 장부로 운영한다.**

> 이 파일은 **부채 장부**이고 기계적으로 **축소 전용**이다. 게이트는 낡았거나 중복이거나 더 이상 필요 없는 항목에 오류를 내므로, 면제가 다른 평가에 조용히 재사용될 수 없다.

기준을 당장 다 만족시킬 수 없을 때 쓰는 현실적인 방법이다. 예외를 허용하되 목록으로 관리하고, 목록은 줄어들기만 한다.

### 메타스킬을 직접 만들었다

```
.agents/skills/
├── create-skill/
├── create-skill-test/
├── improve-skill-quality/
├── create-custom-agent/
└── authoring-github-workflows/
```

**`create-skill-test`가 별도 스킬이다.** 스킬을 만드는 일과 그 스킬의 테스트를 만드는 일을 분리했다. 생태계에서 평가를 포함한 저장소가 드문 상황에서([5.4](../part5/04-patterns.md)) 테스트 작성 자체를 스킬로 만든 것은 드문 선택이다.

`improve-skill-quality/references/eval-triage.md`도 있다. 평가 결과를 트리아지하는 참조 문서다.

### 검증기 테스트 픽스처

```
eng/skill-validator/tests/fixtures/
├── no-eval-skill/SKILL.md
└── sample-skill/SKILL.md
```

`no-eval-skill`이라는 이름의 픽스처가 있다. **평가가 없는 스킬**을 테스트 케이스로 둔 것이다. 검증기가 그 상황을 감지하는지 확인하기 위한 것으로 읽힌다.

평가 없는 스킬을 결함으로 취급한다는 뜻이다. 생태계 대부분이 평가 없이 배포되는 상황과 대조된다.

## microsoft/skills — Azure 전용, 205개

205개가 `.github/plugins/azure-*` 아래에 플러그인 단위로 묶여 있다.

```
.github/plugins/
├── azure-cost/skills/{cost-analysis, cost-estimation, cost-governance, cost-optimization}/
├── azure-kusto-graph-skills/skills/{azure-kusto-graph, azure-kusto-irql, ...}/
├── azure-local-skills/skills/{azure-local, azure-local-multi-rack}/
└── azure-sdk-dotnet/skills/{azure-ai-agents-persistent-dotnet, ...}/
```

`google/skills`가 제품 디렉터리(`skills/cloud/`)로 나눈 것과 달리 **플러그인 단위**로 묶었다. 플러그인이 배포 단위이므로([1.4](../part1/04-boundaries.md)) 설치 단위와 디렉터리 구조를 일치시킨 설계다.

스타 3,075개로, 205개 스킬에 붙은 주목이 스킬 1개짜리 `blader/humanizer`(53,726)의 6%다.

## microsoft/SkillOpt — 스킬을 최적화한다

| 스타 | 생성 | 푸시 | SKILL.md |
|---|---|---|---|
| 17,979 | 2026-05-08 | 2026-09-30 | 5 |

설명이 "재사용 가능한 자연어 스킬을 훈련하는 **텍스트 공간** 최적화기"다.

모델 가중치를 건드리지 않고 지시문 텍스트를 개선한다는 뜻이다. [4.4](../part4/04-meta-skills.md)에서 분류한 메타스킬 중 "최적화" 갈래다.

같은 문제를 다루는 저장소가 셋 있다.

| 저장소 | 스타 | 주체 |
|---|---|---|
| `microsoft/SkillOpt` | 17,979 | Microsoft |
| `alibaba/skill-up` | 1,131 | Alibaba |
| `anthropics/skills`의 `skill-creator` | — | Anthropic (번들 내) |

**빅테크 세 곳이 같은 문제를 각자 풀었다.** 스킬을 자동으로 개선하는 일이 공통 과제가 됐다는 신호다.

Microsoft 저장소 중 스타가 가장 많다. Azure 지식(205개 스킬, 3,075)보다 메타 도구 하나(17,979)가 6배 주목받았다. [5.4](../part5/04-patterns.md)의 "개수가 주목과 반비례하는 구간"과 일치한다.

## microsoft/skill-recorder — 녹화로 스킬을 만든다

| 스타 | 설명 |
|---|---|
| 4,185 | 화면 작업 세션을 녹화해 스킬로 만드는 데스크톱 앱 |

변환형 메타스킬 중에서 **입력이 다르다.** 다른 변환 도구들은 문서를 입력으로 받는다.

| 저장소 | 입력 | 결과물의 유형 |
|---|---|---|
| `virgiliojr94/book-to-skill`(33,430) | 기술서 PDF | 지식형 |
| `yusufkaraaslan/Skill_Seekers`(15,097) | 문서 사이트, 저장소 | 지식형 |
| `microsoft/skill-recorder`(4,185) | **작업 녹화** | 실행형 |

문서에서 뽑으면 "적혀 있는 것"이 들어가고, 작업에서 뽑으면 "실제로 하는 것"이 들어간다. [3.1](../part3/01-capture-intent.md)에서 "가장 좋은 재료는 이미 한 작업의 기록"이라고 쓴 것과 같은 방향이다.

## 평가

### 강점

**평가 인프라가 생태계 최고다.** `dotnet/skills`는 기준선 저장, 비교, 평가 품질 게이트, 통계적 검정력 하한, 부채 장부를 다 갖췄다. 다른 어느 저장소에도 이 수준이 없다.

**실패 경험을 코드로 굳혔다.** "평가가 자기 기준선에게 패배"했던 경험이 CI 검사로 남아 있다. 문서로 적어 두는 것과 기계가 막는 것은 다르다.

**메타 도구를 여러 각도로 만들었다.** 최적화(`SkillOpt`), 녹화(`skill-recorder`), 검증기(`skill-validator`), 테스트 작성 스킬(`create-skill-test`)이 각각 다른 문제를 푼다.

### 한계

**스타수가 전부 하위권이다.** 가장 많은 `SkillOpt`가 17,979로 1위의 6%다. `dotnet/skills`는 1.9%다.

**Azure, .NET에 묶여 있다.** `microsoft/skills` 205개가 전부 Azure다. Azure를 안 쓰면 쓸 데가 없다.

**평가 인프라가 저장소 안에만 있다.** `skill-validator`는 C#으로 쓰인 `dotnet/skills` 전용 도구다. 다른 저장소가 가져다 쓰기 어렵다. `check_eval_quality.py`는 파이썬이고 원리가 일반적이지만, 이 저장소의 디렉터리 관례에 묶여 있다.

**생태계가 이걸 모른다.** 가장 중요한 문제다.

## 이 장이 말하는 것

**스타수와 엔지니어링 수준은 상관이 없다.**

| 저장소 | 스타 | 평가 인프라 |
|---|---|---|
| `obra/superpowers` | 294,779 | 통합 테스트 + 토큰 분석. **기준선 비교는 확인되지 않음** |
| `anthropics/skills` | 179,497 | 평가 **도구**는 제공, 자기 스킬 평가는 없음 |
| `dotnet/skills` | **5,543** | 기준선 비교 + 품질 게이트 + 검정력 하한 |

`dotnet/skills`가 1위의 1.9%다. 이 저장소를 쓸 사람은 .NET 개발자뿐이고, 그게 스타수를 정한다. 스킬을 어떻게 평가해야 하는지 배우려는 사람에게는 **데이터셋에서 가장 가치 있는 저장소**인데, 스타수로 줄 세우면 보이지 않는다.

이것이 [0.2](../part0/02-why-stars.md)에서 스타수를 "순서를 정하는 데만 쓰고 점수로 쓰지 않는다"고 못 박은 이유다. 그리고 [9.2 스킬 품질을 재는 방법](../part9/02-measuring-quality.md)에서 이 저장소를 중심 사례로 다룬다.

### 누가 읽어야 하나

| 목적 | 볼 것 |
|---|---|
| **평가 설계를 배운다** | `eng/eval-quality/README.md` — 생태계 최고 자료 |
| 평가의 함정 | `check_eval_quality.py`가 막는 결함 목록 |
| 통계적 엄격성 | `underpowered-allowlist.txt` 주석 |
| 기준선 비교 구현 | `eng/skill-validator/src/Evaluate/` |
| 스킬 최적화 | `microsoft/SkillOpt` |
| 작업 녹화로 스킬 만들기 | `microsoft/skill-recorder` |

---

다음 장: [6.6 Cloudflare — security-audit-skill 외](06-cloudflare.md)
