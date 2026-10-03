# 5.3 31위 이하 요약 리뷰

[5.2](02-top50.md)에서 다루지 않은 저장소들이다. **요약 리뷰**이고, 저장소 설명과 메타데이터에 기반한다. 정밀 리뷰와 구분해 읽는다([0.3](../part0/03-how-to-read.md)).

여기서 발견한 저장소 중 일부는 6, 7, 8부에서 정밀 리뷰로 올라간다. 중요도가 스타수 순서와 일치하지 않기 때문이다.

## 보안 — 가장 중요한 발견이 이 구간에 있다

| 스타 | 저장소 | SKILL.md | 성격 |
|---|---|---|---|
| 19,218 | `NVIDIA/SkillSpector` | 27 | **에이전트 스킬 취약점 스캐너** |
| 7,541 | `anthropics/defending-code-reference-harness` | 9 | 위협 모델링, 스캔, 트리아지, 패치 |
| 7,350 | `trailofbits/skills` | 85 | 보안 리뷰용 스킬 묶음 |
| 7,217 | `SnailSploit/Claude-Red` | — | 공격 보안 스킬 라이브러리 |
| 4,760 | `elementalsouls/Claude-BugHunter` | — | 버그 헌팅, 레드팀 82개 스킬 |
| 3,385 | `ljagiello/ctf-skills` | — | CTF 문제 풀이 스킬 |

(수집 날짜: 2026-10-04)

`NVIDIA/SkillSpector`(19,218)는 이 구간에서 가장 중요한 저장소다. 설명이 "AI 에이전트 스킬을 위한 보안 스캐너. 취약점을 탐지한다"다.

**스킬을 스캔하는 도구가 빅테크에서 나왔다는 사실**이 생태계의 성숙도를 말한다. 스킬은 에이전트가 읽고 그대로 따르는 지시문이고, 설치 비용이 거의 0이다. 그 조합이 위험하다는 인식이 도구로 나타났다. [9.3 공급망 위험](../part9/03-supply-chain.md)에서 정밀 리뷰한다.

`trailofbits/skills`(7,350)도 주목할 만하다. Trail of Bits는 보안 감사 전문 회사다. 스타수는 상위 30위에 못 들지만, **누가 만들었는지**가 스타수보다 더 많은 것을 말하는 사례다. [8.1](../part8/01-security.md)에서 다룬다.

## 메모리, 컨텍스트 — 포화의 전형

| 스타 | 저장소 | SKILL.md | 설명 요지 |
|---|---|---|---|
| 31,332 | `topoteretes/cognee` | 18 | AI 메모리 플랫폼 |
| 25,190 | `mksglu/context-mode` | 11 | 컨텍스트 창 최적화 |
| 14,491 | `NevaMind-AI/memU` | 1 | 에이전트 간 개인 메모리 |
| 13,330 | `EverMind-AI/EverOS` | 5 | 모든 AI 에이전트용 이식 가능 메모리 계층 |
| 11,685 | `MemTensor/MemOS` | 7 | 자기진화 메모리 OS |
| 27,266 | `OthmanAdi/planning-with-files` | 18 | 파일 기반 영속 계획 |

(수집 날짜: 2026-10-04)

여섯 저장소가 같은 문제를 푼다. **에이전트가 세션을 넘어 기억하지 못한다**는 문제다. 이름까지 닮았다 — `memU`, `MemOS`, `EverOS`, `claude-mem`(95,383, 6위).

이 구간이 [9.5 중복과 포화](../part9/05-saturation.md)의 주요 증거다. 같은 문제를 푸는 저장소가 여섯 개 넘게 있고, 각각 1만~9만 스타를 받는다. 사용자가 여섯 개를 비교해서 고르지 않는다. 먼저 눈에 띈 것을 쓴다.

## 빅테크 — 스타수와 중요도가 어긋나는 구간

| 스타 | 저장소 | SKILL.md |
|---|---|---|
| 20,875 | `google/skills` | 155 |
| 19,218 | `NVIDIA/SkillSpector` | 27 |
| 7,644 | `android/skills` | 25 |
| 7,541 | `anthropics/defending-code-reference-harness` | 9 |
| 5,543 | `dotnet/skills` | 108 |
| 3,075 | `microsoft/skills` | — |
| 2,974 | `cloudflare/skills` | — |
| 1,532 | `microsoft/azure-skills` | — |
| 1,131 | `alibaba/skill-up` | — |
| 369 | `github/copilot-plugins` | — |
| 351 | `cloudflare/agent-skills-discovery-rfc` | — |
| 295 | `vercel/vercel-plugin` | — |

(수집 날짜: 2026-10-04)

`microsoft/skills`(3,075)와 `cloudflare/skills`(2,974)는 공식 저장소인데 스타가 세 자리에서 네 자리다. 같은 회사의 단일 스킬 저장소인 `cloudflare/security-audit-skill`은 23,894다. **공식 번들보다 단일 목적 스킬이 8배 많은 주목을 받았다.**

이 어긋남이 6부의 핵심 질문이 된다([6.6](../part6/06-cloudflare.md)).

## 중국어권 — 규모가 큰 구간

| 스타 | 저장소 | SKILL.md | 성격 |
|---|---|---|---|
| 69,766 | `code-yeongyu/oh-my-openagent` | 59 | 키워드 기반 에이전트 제어 |
| 26,312 | `JimLiu/baoyu-skills` | 22 | 개인 스킬 묶음 |
| 21,127 | `KKKKhazix/khazix-skills` | 6 | AI 스킬 모음 |
| 17,053 | `tradecatlabs/vibe-coding-cn` | 24 | Vibe Coding 교재 |
| 16,929 | `wanshuiyin/Auto-claude-code-research-in-sleep` | 189 | 마크다운 전용 자동 연구 |
| 12,719 | `ConardLi/garden-skills` | 5 | 개인 스킬 모음 |
| 8,256 | `jnMetaCode/superpowers-zh` | 21 | **`superpowers`의 중국어 확장판** |
| 7,864 | `HKUSTDial/Supervisor-Skills` | 12 | 박사 지도 경험을 스킬로 |
| 7,505 | `anbeime/skill` | 84 | 스킬 상점 |

(수집 날짜: 2026-10-04)

`jnMetaCode/superpowers-zh`(8,256)가 특히 흥미롭다. 1위 저장소 `obra/superpowers`의 중국어 확장판이다. **스킬이 번역, 현지화되는 단계에 들어섰다.** 소프트웨어가 아니라 마크다운이므로 포크하고 번역하는 비용이 낮다. [7.5](../part7/05-regional.md)에서 다룬다.

## 도구, 빌더

| 스타 | 저장소 | SKILL.md | 성격 |
|---|---|---|---|
| 16,752 | `composio-community/awesome-codex-skills` | 880 | Codex 스킬 큐레이션 |
| 15,097 | `yusufkaraaslan/Skill_Seekers` | 26 | 문서, 저장소, PDF를 스킬로 변환 |
| 14,009 | `nidhinjs/prompt-master` | 1 | 프롬프트를 작성하는 스킬 |
| 9,127 | `EvoMap/evolver` | 1 | 자기진화 엔진 |
| 7,532 | `refly-ai/refly` | 1 | 오픈소스 에이전트 스킬 빌더 |
| 7,491 | `tigerless-labs/autoharness` | 1 | 자기학습 스킬 계층 |

(수집 날짜: 2026-10-04)

`nidhinjs/prompt-master`(14,009)가 재귀적이다. **프롬프트를 쓰는 스킬**이다. 2부와 3부의 내용을 스킬로 만든 것에 해당한다.

## 문서, 디자인, 제작

| 스타 | 저장소 | SKILL.md | 성격 |
|---|---|---|---|
| 35,581 | `JCodesMore/ai-website-cloner-template` | 1 | 웹사이트 복제 |
| 33,884 | `freestylefly/awesome-gpt-image-2` | 1 | 이미지 프롬프트 사례집 |
| 19,591 | `teng-lin/notebooklm-py` | 1 | NotebookLM 비공식 API + 스킬 |
| 9,809 | `Agents365-ai/drawio-skill` | 1 | 자연어를 draw.io 다이어그램으로 |
| 9,352 | `ibelick/ui-skills` | 7 | 디자인 엔지니어용 스킬 |
| 8,992 | `nexu-io/html-anything` | 81 | 에이전틱 HTML 편집기 |
| 7,986 | `ChenLiu-1996/figures4papers` | 1 | 논문용 고품질 그림 |
| 13,220 | `latent-spaces/brag` | 2 | 만든 것을 공유 가능한 글로 |

(수집 날짜: 2026-10-04)

`SKILL.md` 1개짜리가 많다. 단일 목적 스킬이 이 구간의 주류다.

## 유지가 끊긴 고스타 저장소

요약 리뷰에서 기록해 둘 항목이다.

| 스타 | 저장소 | 마지막 푸시 | 성격 |
|---|---|---|---|
| 15,253 | `travisvn/awesome-claude-skills` | 2026-04-28 | 큐레이션 |
| 13,217 | `Orchestra-Research/AI-Research-SKILLs` | 2026-06-16 | 연구 스킬 98개 |
| 12,719 | `ConardLi/garden-skills` | 2026-07-12 | 개인 모음 |
| 6,257 | `heilcheng/awesome-agent-skills` | 2026-04-05 | 큐레이션 |

(수집 날짜: 2026-10-04)

`Orchestra-Research/AI-Research-SKILLs`는 지식형 저장소이고 `SKILL.md`가 98개다. 지식형은 수명이 짧다([4.2](../part4/02-three-types.md)). 2026년 6월 이후 갱신이 없다면 그 안의 사실들이 낡았을 가능성이 있다. 스타 1만 3천이 그 사실을 가린다.

## 이 구간에서 정밀 리뷰로 올리는 저장소

스타수 순위로는 31위 아래지만 중요도가 높아 뒤에서 자세히 다룬다.

| 저장소 | 올리는 이유 | 어디서 |
|---|---|---|
| `NVIDIA/SkillSpector` | 스킬 보안 스캐너. 생태계 성숙도의 지표 | [9.3](../part9/03-supply-chain.md) |
| `trailofbits/skills` | 보안 전문 회사가 만든 스킬 | [8.1](../part8/01-security.md) |
| `anthropics/defending-code-reference-harness` | 공식 보안 스킬 | [6.2](../part6/02-anthropic-others.md) |
| `jnMetaCode/superpowers-zh` | 스킬 현지화 사례 | [7.5](../part7/05-regional.md) |
| `android/skills`, `dotnet/skills` | 플랫폼 공식 저장소 | [6.5](../part6/05-microsoft.md), [6.8](../part6/08-others.md) |
| `cloudflare/agent-skills-discovery-rfc` | 디스커버리 공백 | [6.6](../part6/06-cloudflare.md) |
| `alibaba/skill-up`, `microsoft/SkillOpt` | 메타스킬 | [8.3](../part8/03-builders.md) |

**스타수로 줄 세우면 이 저장소들이 뒤로 밀린다.** 이것이 스타수를 순서 정하는 데만 쓰고 점수로 쓰지 않는 이유다([0.2](../part0/02-why-stars.md)).

---

다음 장: [5.4 순위에서 읽히는 패턴](04-patterns.md)
