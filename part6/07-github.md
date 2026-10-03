# 6.7 GitHub — awesome-copilot, copilot-plugins

| 저장소 | 스타 | 생성 | 푸시 | 라이선스 | SKILL.md |
|---|---|---|---|---|---|
| `github/awesome-copilot` | 39,658 | 2025-06-11 | 2026-10-01 | MIT | 444 |
| `github/copilot-plugins` | 369 | 2026-01-21 | 2026-08-31 | — | — |

(수집 날짜: 2026-10-04. 확인 수준: 정밀 리뷰)

GitHub의 두 저장소는 스타 차이가 107배다. 그 차이가 이 장의 주제다.

## awesome-copilot — 커뮤니티 기여를 공식 저장소로 받았다

생성일이 **2025-06-11**이다. `anthropics/skills`(2025-09-22)보다 석 달 빠르다. 스킬 규격이 공개되기 전에 만들어진 저장소이고, 규격이 나온 뒤 `skills/` 디렉터리를 추가한 것으로 보인다.

`SKILL.md`가 444개다. 마켓플레이스 규모다([4.3](../part4/03-scale.md)).

### 구조 — 확장 수단을 전부 받는다

```
github/awesome-copilot/
├── skills/          스킬
├── agents/          에이전트
├── instructions/    지침
├── hooks/           훅
├── plugins/         플러그인
├── extensions/      확장
├── workflows/       워크플로
├── cookbook/        레시피
├── docs/, website/  문서, 사이트
├── eng/             엔지니어링
├── .schemas/        스키마
├── mcp.json         MCP 설정
├── AGENTS.md
└── CONTRIBUTING.md, CODEOWNERS, SECURITY.md
```

[1.4](../part1/04-boundaries.md)에서 구분한 다섯 수단(스킬, 서브에이전트, MCP, 플러그인, 훅)이 **전부 별도 디렉터리로 있다.** 스킬만 모은 저장소가 아니라 확장 수단 전체의 카탈로그다.

### 큐레이션 저장소로서 갖춘 것

마켓플레이스의 핵심 정보는 "무엇을 검증했는가"다([4.3](../part4/03-scale.md)). 이 저장소는 그 장치를 여러 개 갖췄다.

| 파일/디렉터리 | 역할 |
|---|---|
| `CONTRIBUTING.md` | 기여 규칙 |
| `CODEOWNERS` | 영역별 책임자 |
| `SECURITY.md` | 보안 보고 경로 |
| `.schemas/` | 기여물의 형식 검증 |
| `.codespellrc` | 오타 검사 |
| `eng/` | 엔지니어링 도구 |
| `.all-contributorsrc` | 기여자 기록 |

**`.schemas/`가 있다는 점이 중요하다.** 444개를 사람이 다 읽을 수 없으므로, 기계가 형식을 검증한다. 수집 데이터의 다른 마켓플레이스 저장소 대부분이 이 장치를 갖추지 않았다.

`CODEOWNERS`도 큐레이션에서 의미가 있다. 영역마다 책임자가 지정되면 기여물이 아무도 보지 않은 채로 들어오지 않는다. **큐레이션 저장소에서 가장 흔한 실패는 "모았지만 아무도 읽지 않았다"는 것**인데, 이 구조가 그걸 완화한다.

### 형식 검증과 품질 검증은 다르다

다만 `.schemas/`가 하는 일은 **형식** 검증이다. 프런트매터가 유효한지, 필수 필드가 있는지를 본다. 그 스킬이 작동하는지는 검사하지 않는다.

`dotnet/skills`와 비교하면 차이가 분명하다([6.5](05-microsoft.md)).

| 저장소 | 형식 검증 | 기능 검증 | 평가 품질 검증 |
|---|---|---|---|
| `github/awesome-copilot` | ○ (`.schemas/`) | ✕ | ✕ |
| `dotnet/skills` | ○ (`skill-validator`) | ○ (`BaselineStore`, `Comparator`) | ○ (`check_eval_quality.py`) |

`awesome-copilot`이 444개, `dotnet/skills`가 108개다. **규모가 클수록 기능 검증이 어렵고, 그래서 형식 검증에서 멈춘다.** 마켓플레이스의 구조적 한계다.

### 갱신되고 있다

마지막 푸시가 2026-10-01로 수집 시점 사흘 전이다. 1년 4개월 된 저장소가 활발하게 유지된다.

이것이 큐레이션 저장소에서 드문 상태다. 같은 범주의 다른 저장소들을 보면 그렇다.

| 저장소 | 스타 | 마지막 푸시 |
|---|---|---|
| `github/awesome-copilot` | 39,658 | 2026-10-01 |
| `travisvn/awesome-claude-skills` | 15,253 | 2026-04-28 |
| `Orchestra-Research/AI-Research-SKILLs` | 13,217 | 2026-06-16 |
| `heilcheng/awesome-agent-skills` | 6,257 | 2026-04-05 |

(수집 날짜: 2026-10-04)

**조직 저장소가 개인 큐레이션보다 오래 유지된다.** 개인 목록은 작성자가 흥미를 잃으면 멈추고, 조직 저장소는 담당자가 바뀌어도 이어진다. [7.4](../part7/04-awesome-lists.md)에서 다룬다.

## copilot-plugins — 369스타의 공식 저장소

설명이 "공식 GitHub Copilot 플러그인 컬렉션 — MCP 서버, 스킬, 훅, 기타 확장 도구"다.

`awesome-copilot`과 범위가 겹친다. 양쪽 다 스킬, 훅, MCP를 담는다. 차이는 하나로 보인다.

| | `awesome-copilot` | `copilot-plugins` |
|---|---|---|
| 성격 | **커뮤니티 기여** | **공식 제공** |
| 스타 | 39,658 | 369 |
| 마지막 푸시 | 2026-10-01 | 2026-08-31 |

**커뮤니티 저장소가 공식 저장소의 107배 주목받았다.**

같은 패턴이 다른 회사에서도 나타난다.

| 회사 | 커뮤니티, 작업 중심 | 스타 | 자사 공식 번들 | 스타 | 배수 |
|---|---|---|---|---|---|
| GitHub | `awesome-copilot` | 39,658 | `copilot-plugins` | 369 | 107× |
| Cloudflare | `security-audit-skill` | 23,902 | `cloudflare/skills` | 2,974 | 8× |
| Microsoft | `SkillOpt` | 17,979 | `microsoft/skills` | 3,075 | 5.8× |

(수집 날짜: 2026-10-04)

세 회사에서 같은 방향이 관측된다. **자사 제품 사용법을 모은 공식 번들이 가장 적게 주목받는다.** 이유는 [7.6](../part7/06-why-individuals-win.md)에서 다룬다.

`copilot-plugins`는 마지막 푸시도 2026-08-31로 한 달 넘게 지났다. 공식 저장소가 커뮤니티 저장소보다 덜 갱신되는 상태다.

## awesome-copilot이 Copilot 전용이 아니다

눈여겨볼 점이 하나 더 있다. 이 저장소는 GitHub Copilot용인데 **스킬 규격은 공통**이다([6.1](01-anthropic-skills.md)).

`AGENTS.md`가 루트에 있다. `AGENTS.md`는 특정 벤더에 묶이지 않은 지침 파일 관례다. `.github/` 아래가 아니라 루트에 둔 것은 다른 도구도 읽을 수 있게 한 배치로 읽힌다.

수집 데이터에서 같은 방향의 증거가 있다. `ciembor/agent-rules-books`(2,900)의 설명이 "AI 코딩 에이전트용 AGENTS.md 규칙/스킬: Codex, Cursor, Claude"다. 한 저장소가 여러 도구를 대상으로 한다.

**스킬 저장소를 도구별로 분류하는 축이 무의미해지고 있다**는 [4.1](../part4/01-taxonomy.md)의 관찰과 일치한다.

## 평가

### 강점

**큐레이션 장치를 제대로 갖췄다.** `CONTRIBUTING.md`, `CODEOWNERS`, `.schemas/`, `SECURITY.md`가 다 있다. 444개 규모에서 최소한의 품질 하한을 기계로 유지한다.

**확장 수단 전체를 다룬다.** 스킬만이 아니라 에이전트, 훅, MCP, 플러그인, 워크플로를 한 저장소에서 본다. 어느 수단을 써야 하는지 비교하려는 사람에게 유용하다.

**유지된다.** 큐레이션 저장소에서 가장 중요한 조건이고, 개인 목록들이 못 지키는 조건이다.

**규격 공개보다 먼저 있었다.** 2025-06-11 생성이고, 규격이 나온 뒤 흡수했다. 생태계 변화에 저장소 구조를 맞춰 온 기록이다.

### 한계

**형식 검증에서 멈춘다.** `.schemas/`는 프런트매터가 유효한지를 보고, 스킬이 작동하는지는 보지 않는다. 444개 규모에서 기능 검증은 현실적으로 어렵다 — 마켓플레이스의 구조적 한계이고 이 저장소의 결함이라기보다 규모의 결과다.

**스타수가 444개 중 무엇에 붙었는지 알 수 없다.** 마켓플레이스 스타수의 공통 문제다([4.3](../part4/03-scale.md)).

**공식 저장소와 범위가 겹친다.** `copilot-plugins`와 무엇이 다른지가 저장소 설명만으로는 분명하지 않다. 쓰는 쪽에서 어디를 봐야 하는지 헷갈린다.

### 누가 읽어야 하나

| 목적 | 볼 것 |
|---|---|
| 큐레이션 저장소를 운영한다 | `CONTRIBUTING.md`, `CODEOWNERS`, `.schemas/` |
| 확장 수단을 비교한다 | `skills/`, `agents/`, `hooks/`, `plugins/` 디렉터리 구성 |
| Copilot용 스킬을 찾는다 | `skills/` (444개) |
| 도구 중립적 지침 | 루트의 `AGENTS.md` |

---

다음 장: [6.8 Alibaba, NVIDIA, AWS, Vercel](08-others.md)
