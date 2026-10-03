# 부록 B. 저장소 색인

판정 대상 150개의 전체 목록이다. `SKILL.md` 보유 여부로 나눴다.

**이 표는 기계 수집 결과이고 선별 판정이 아니다.** 트랙 A/B 선별과 제외 판정은 [5.1](../part5/01-collection.md)과 [5.2](../part5/02-top50.md)에 있다.

| 항목 | 값 |
|---|---|
| 수집 날짜 | 2026-10-04 |
| 전체 수집 | 458개 |
| 판정 대상 | 상위 150개 |
| `SKILL.md` 보유 | 126개 |
| 원본 | [`data/snapshots/2026-10/classified.tsv`](../data/) |

## 읽을 때 주의

**`SKILL.md` 개수는 선별에만 쓴다. 품질 지표가 아니다.** 최대값 8,212개와 최소값 1개의 차이는 저장소 성격의 차이이지 품질의 차이가 아니다([4.3](../part4/03-scale.md)).

**0개로 집계된 저장소에 스킬이 없다는 뜻이 아니다.** 세 가지 경우가 있다.

| 경우 | 사례 |
|---|---|
| 실제로 스킬이 없다 (큐레이션, 규격, 도구) | `agentskills/agentskills`(25,877) |
| 사람의 역량을 뜻하는 "skill"이 걸렸다 | `Snailclimb/JavaGuide`(159,013) |
| **파일명이 규격을 따르지 않는다** | `Graphify-Labs/graphify`(123,488) — 실제 12개 |

세 번째는 기계 판정으로 잡히지 않는다([8.9](../part8/09-code-understanding.md)).

---

## SKILL.md 보유 (126개)


| 스타 | 저장소 | SKILL.md | 설명 |
|---|---|---|---|
| 294,779 | `obra/superpowers` | 15 | An agentic skills framework & software development methodology that wo |
| 179,497 | `anthropics/skills` | 20 | Public repository for Agent Skills |
| 157,770 | `langgenius/dify` | 7 | Build Agentic workflows, RAG pipelines, with rich AI model and tool su |
| 152,808 | `DietrichGebert/ponytail` | 12 | Makes your AI agent think like the laziest senior dev in the room. The |
| 149,104 | `anthropics/claude-code` | 10 | Claude Code is an agentic coding tool that lives in your terminal, und |
| 100,746 | `addyosmani/agent-skills` | 25 | Production-grade engineering skills for AI coding agents. |
| 99,281 | `nexu-io/open-design` | 537 | 🎨 Best DeepSeek Harness Design Plugin. The open-source Claude Design a |
| 96,087 | `ruvnet/RuView` | 54 | π RuView turns commodity WiFi signals into real-time spatial intellige |
| 95,383 | `thedotmack/claude-mem` | 36 | Persistent Context Across Sessions for Every Agent –  Captures everyth |
| 92,250 | `Leonxlnx/taste-skill` | 13 | Taste-Skill - gives your AI good taste. stops the AI from generating b |
| 85,158 | `Egonex-AI/Understand-Anything` | 9 | Graphs that teach > graphs that impress. Turn any code into an interac |
| 82,962 | `lobehub/lobehub` | 52 | 🤯 LobeHub is your Chief Agent Operator, organizing your agents into 7× |
| 76,593 | `tt-a1i/archify` | 2 | Agent skill for beautiful, verifiable architecture, workflow, sequence |
| 76,418 | `ComposioHQ/awesome-claude-skills` | 864 | A curated list of awesome Claude Skills, resources, and tools for cust |
| 73,778 | `ruvnet/ruflo` | 375 | 🌊 The original agent harness. Deploy intelligent multi-player swarms, |
| 73,378 | `career-ops-hq/career-ops` | 8 | Open-source AI job search agent and job finder: scan job boards, score |
| 69,766 | `code-yeongyu/oh-my-openagent` | 59 | OmO: Just type "mass ulw" keyword with your prompt. Now you are the ma |
| 67,032 | `shanraisshan/claude-code-best-practice` | 9 | from vibe coding to agentic engineering - practice makes claude perfec |
| 53,726 | `blader/humanizer` | 1 | Agent skill that removes signs of AI-generated writing from text |
| 53,105 | `ayghri/i-have-adhd` | 2 | A skill to stop your coding agent from burying the answer. ADHD-friend |
| 52,344 | `CherryHQ/cherry-studio` | 35 | AI productivity studio with smart chat, autonomous agents, and 300+ as |
| 49,109 | `kepano/obsidian-skills` | 6 | Agent skills for Obsidian. Teach your agent to use Obsidian CLI and op |
| 47,467 | `K-Dense-AI/scientific-agent-skills` | 177 | Turn any AI agent into an AI Scientist. The #1 Agent Skills library fo |
| 47,222 | `zhayujie/CowAgent` | 3 | Open-source personal AI assistant & Agent Harness. Plans tasks, runs t |
| 47,214 | `sickn33/agentic-awesome-skills` | 8212 | AAS Core is the local, agent-first control plane for complete catalog  |
| 43,722 | `reactive-resume/reactive-resume` | 1 | A one-of-a-kind resume builder that keeps your privacy in mind. Comple |
| 43,468 | `alibaba/open-code-review` | 4 | Secure, fast, efficient, battle-tested at Alibaba's scale. Hybrid arch |
| 43,204 | `cathrynlavery/diagram-design` | 1 | Editorial diagram design for Claude Code, Codex, GitHub Copilot, Facto |
| 40,174 | `wshobson/agents` | 184 | Multi-harness agentic plugin marketplace for Claude Code, Codex, Curso |
| 39,658 | `github/awesome-copilot` | 444 | Community-contributed instructions, agents, skills, and configurations |
| 37,338 | `anthropics/claude-plugins-official` | 33 | Official, Anthropic-managed directory of high quality Claude Code Plug |
| 35,581 | `JCodesMore/ai-website-cloner-template` | 1 | Clone any website with one command using AI coding agents |
| 35,426 | `agentscope-ai/QwenPaw` | 48 | Your Personal AI Assistant; easy to install, deploy on your own machin |
| 33,884 | `freestylefly/awesome-gpt-image-2` | 1 | Prompt as Code \| GPT Image 2 / 2.5 提示词与案例库，530+ 个案例、20+ 套工业级模板与可复用 Ski |
| 33,430 | `virgiliojr94/book-to-skill` | 1 | Turn any technical book PDF into a Claude Code skill — ready to study, |
| 33,419 | `alibaba/nacos` | 1 | an easy-to-use dynamic service discovery, configuration and service ma |
| 33,292 | `iOfficeAI/AionUi` | 4 | Open-source 24/7 Cowork app for OpenClaw, Hermes, Claude Code, Codex, |
| 31,513 | `iOfficeAI/OfficeCLI` | 12 | OfficeCLI is the first and best Office suite  purpose-built for AI age |
| 31,332 | `topoteretes/cognee` | 18 | Cognee is the open-source AI memory platform for agents. Give your AI  |
| 31,234 | `googleworkspace/cli` | 95 | Google Workspace CLI — one command-line tool for Drive, Gmail, Calenda |
| 30,869 | `nanocoai/nanoclaw` | 63 | A lightweight alternative to OpenClaw that runs in containers for secu |
| 27,856 | `openai/skills` | 44 | Skills Catalog for Codex |
| 27,426 | `alirezarezvani/claude-skills` | 846 | 380 Claude Code skills & agent skills & plugins (30+ Agents, 70+ custo |
| 27,266 | `OthmanAdi/planning-with-files` | 18 | Persistent file-based planning for AI coding agents and long-running t |
| 27,212 | `op7418/guizang-ppt-skill` | 1 | AI-agent Skill for generating polished HTML slide decks: editorial mag |
| 26,743 | `phuryn/pm-skills` | 69 | PM Skills Marketplace: 100+ agentic skills, commands, and plugins — fr |
| 26,312 | `JimLiu/baoyu-skills` | 22 |  |
| 25,269 | `titanwings/distilly` | 1 | Distilly — Distill how they think into reusable Skills for any Agent o |
| 25,190 | `mksglu/context-mode` | 11 | Context window optimization for AI coding agents. Sandboxes tool outpu |
| 24,591 | `pascalorg/editor` | 4 | Open-source 3D architectural editor with a local CLI, MCP tools, and p |
| 23,894 | `cloudflare/security-audit-skill` | 1 | A coding-agent skill for multi-phase security audits with independentl |
| 21,127 | `KKKKhazix/khazix-skills` | 6 | 数字生命卡兹克开源的 AI Skills 合集 \| Agent Skills: leader（帮你定义目标）, neat-freak 洁癖, |
| 20,875 | `google/skills` | 155 | Agent Skills for Google products and technologies |
| 19,591 | `teng-lin/notebooklm-py` | 1 | Unofficial Python API and agentic skill for Google Gemini Notebook. Fu |
| 19,218 | `NVIDIA/SkillSpector` | 27 | Security scanner for AI agent skills. Detect vulnerabilities, maliciou |
| 17,979 | `microsoft/SkillOpt` | 5 | SkillOpt is a text-space optimizer that trains reusable natural-langua |
| 17,059 | `kubesphere/kubesphere` | 32 | The container platform tailored for Kubernetes multi-cloud, datacenter |
| 17,053 | `tradecatlabs/vibe-coding-cn` | 24 | Vibe Coding 从入门到精通教程｜AI 结对编程工作流｜Prompt、Skill、Workflow、上下文管理、codex实战指南 |
| 16,929 | `wanshuiyin/Auto-claude-code-research-in-sleep` | 189 | ARIS ⚔️ (Auto-Research-In-Sleep) — Lightweight Markdown-only skills fo |
| 16,798 | `citrolabs/ego-lite` | 2 | The fastest browser for AI agents to run browser automation, built for |
| 16,752 | `composio-community/awesome-codex-skills` | 880 | A curated list of practical Codex skills for automating workflows acro |
| 15,453 | `eigent-ai/eigent` | 6 | Eigent: The Open Source Cowork Desktop - Local and Free Alternative to |
| 15,334 | `AgriciDaniel/claude-obsidian` | 16 | Self-organizing AI second brain for Obsidian + Claude Code. Drop any s |
| 15,097 | `yusufkaraaslan/Skill_Seekers` | 26 | Convert documentation websites, GitHub repositories, and PDFs into Cla |
| 14,491 | `NevaMind-AI/memU` | 1 | Personal memory across agents |
| 14,009 | `nidhinjs/prompt-master` | 1 | A Claude skill that writes the accurate prompts for any AI tool. Zero  |
| 13,330 | `EverMind-AI/EverOS` | 5 | One portable memory layer for every AI agent: local-first, Markdown-na |
| 13,220 | `latent-spaces/brag` | 2 | You built it. Now brag. Turn the project you just created into a short |
| 13,217 | `Orchestra-Research/AI-Research-SKILLs` | 98 | Comprehensive open-source library of AI research and engineering skill |
| 12,719 | `ConardLi/garden-skills` | 5 | ConardLi's open-source Skills collection, featuring web design, knowle |
| 12,664 | `Untrivial-ai/agent-orchestrator` | 7 | Run and supervise teams of coding agents from planning to merge. Any h |
| 12,579 | `krillinai/OpenCreator` | 15 | Formerly KrillinAI. Open-source AI workspace for creators, powered by  |
| 11,716 | `Jeffallan/claude-skills` | 67 | 67 Specialized Skills for Full-Stack Developers. Transform Claude Code |
| 11,685 | `MemTensor/MemOS` | 7 | Self-evolving memory OS for LLM & AI Agents: ultra-persistent memory, |
| 11,088 | `aden-hive/hive` | 24 | Multi-Agent Harness for Production AI |
| 10,716 | `mcp-use/mcp-use` | 6 | The fullstack MCP framework to develop MCP Apps for ChatGPT / Claude & |
| 9,809 | `Agents365-ai/drawio-skill` | 1 | Agent skill that turns natural language, code, Terraform/K8s, SQL, Ope |
| 9,689 | `AgriciDaniel/claude-ads` | 34 | Claude-first paid-media operations skill for Claude Code across 12 ad  |
| 9,352 | `ibelick/ui-skills` | 7 | Skills for Design Engineers |
| 9,127 | `EvoMap/evolver` | 1 | The GEP-powered self-evolving engine for AI agents. Auditable evolutio |
| 9,120 | `backnotprop/plannotator` | 18 | Annotate and review coding agent plans and code diffs visually, share  |
| 8,992 | `nexu-io/html-anything` | 81 | ✨ The agentic HTML editor — your local AI agent writes the HTML, you s |
| 8,913 | `pacifio/atlas` | 5 | Source control for agents. Use multiple coding agents, track their cha |
| 8,482 | `genspark-ai/genoffice` | 1 | Free, open-source AI Office suite: Docs, Sheets, Slides, PDF, Markdown |
| 8,256 | `jnMetaCode/superpowers-zh` | 21 | 🦸 AI 编程超能力 · 中文增强版 — superpowers（250k+ ⭐）完整汉化 + 4 个中国原创 skills，让 Claud |
| 8,072 | `YaoApp/yao` | 13 | ✨ All your agents and workspaces in one place, on every device you own |
| 7,986 | `ChenLiu-1996/figures4papers` | 1 | My Python scripts to make high-quality figures for publications in top |
| 7,864 | `HKUSTDial/Supervisor-Skills` | 12 | 将博导十年科研经验炼化为可直接调用的 AI 技能。从 Idea 构思到论文投稿，你的 AI 科研副导师。 |
| 7,644 | `android/skills` | 25 |  |
| 7,541 | `anthropics/defending-code-reference-harness` | 9 | Skills for threat modeling, scanning, triage, patching, plus an autono |
| 7,532 | `refly-ai/refly` | 1 | The first open-source agent skills builder. Define skills by vibe work |
| 7,511 | `Gentleman-Programming/gentle-ai` | 26 | Gentle-AI configures the AI coding agents you already use: Claude Code |
| 7,505 | `anbeime/skill` | 84 | 收录最全、更新最快的技能Skills商店：精选原创技能包（涵盖文档处理、内容创作、编程开发、机器学习、自动化工作流），全部打包好可直接安装使 |
| 7,491 | `tigerless-labs/autoharness` | 1 | Autoharness — a self-learning skill layer for Claude Code — distills s |
| 7,350 | `trailofbits/skills` | 85 | Trail of Bits Claude Code skills for security research, vulnerability  |
| 7,254 | `WenyuChiou/awesome-agentic-ai-zh` | 1 | A trilingual (繁中 / English / 简中) learning roadmap for agentic AI: from |
| 7,233 | `zenstory-ai/oh-story-claudecode` | 13 | Claude Code / Codex / OpenCode agent skills for writing Chinese web no |
| 7,217 | `SnailSploit/Claude-Red` | 79 | claude-red is a curated library of offensive security skills designed  |
| 7,151 | `deanpeters/Product-Manager-Skills` | 77 | Product Management skills framework built on battle-tested methods for |
| 7,133 | `ParthJadhav/app-store-screenshots` | 1 | end to end app store screenshot creation using AI |
| 7,102 | `tw93/Waza` | 16 | 🥷 Engineering habits you already know, turned into skills Claude can r |
| 7,082 | `TokenRhythm/opensquilla` | 11 | OpenSquilla — Token-Efficient AI Agent with same budget, higher intell |
| 7,040 | `htdt/godogen` | 1 | Autonomous game development for Godot, Bevy, and Babylon.js with Claud |
| 7,026 | `tech-leads-club/agent-skills` | 92 | The secure, validated skill registry for professional AI coding agents |
| 6,644 | `SawyerHood/dev-browser` | 1 | A Claude Skill to give your agent the ability to use a web browser |
| 6,597 | `Devin-AXIS/iPolloWork` | 92 | Enterprise-grade, local-first Agent Workbench for people and agent tea |
| 6,465 | `htmlstreamofficial/preline` | 2 | Preline UI is an open-source set of prebuilt UI components based on th |
| 6,357 | `ThinkInAIXYZ/deepchat` | 25 | 🐬DeepChat - A smart assistant that connects powerful AI to your person |
| 6,339 | `internet-court/internet-court-skill` | 94 | The trust layer for agent-to-agent commerce — natural-language mandate |
| 6,333 | `anysearch-ai/anysearch-skill` | 1 | Unified real-time search engine skill for AI agents. Supports general  |
| 6,330 | `kucherenko/jscpd` | 5 | Copy/paste detector for source code. 220+ languages, Rust engine, SARI |
| 6,315 | `ningzimu/codex-ppt-skill` | 1 | GPT-Image-2 PPT Generator Skill for Creating Image-Based PowerPoint Pr |
| 6,307 | `Sylinko/Everywhere` | 1 | On-screen aware AI assistant for your desktop. Uses current app contex |
| 6,258 | `gosom/google-maps-scraper` | 1 | scrape data  from Google Maps. Extracts data such as the name, address |
| 6,176 | `Q00/ouroboros` | 24 | Agent OS: the agent gets smarter on its own. We just hold the line: In |
| 6,162 | `jihe520/MathModelAgent` | 11 | 🤖📐专为数学建模设计的 Agent & skills ,自动完成数学建模，生成一份完整的可以直接提交的论文。 An Agent Design |
| 6,087 | `browser-act/skills` | 103 | Browser automation CLI built for AI agents. Break through anti-bot wal |
| 6,043 | `google/agents-cli` | 15 | The CLI and skills that turn any coding assistant into an expert at cr |
| 5,937 | `antfu/skills` | 11 | Anthony Fu's curated collection of agent skills. |
| 5,903 | `larashero3-dotcom/lieflat-charts` | 1 | Data visualization Skill for AI Agents, turning data into polished, in |
| 5,835 | `epoko77-ai/im-not-ai` | 7 | AI가 쓴 한글을 사람 글처럼 윤문하는 Claude 스킬 — Korean AI-text humanizer: detects an |
| 5,738 | `OpenSenseNova/SenseNova-Skills` | 83 | Modular SenseNova skills for building AI-powered office assistants and |
| 5,629 | `wuyoscar/GPT-Image2-Skill` | 2 | GPT Image 2/2.5 prompt gallery, image prompt library, agentic skill, a |
| 5,623 | `GargantuaX/gemini-watermark-remover` | 1 | A high-performance, 100% client-side tool for removing Gemini AI image |
| 5,543 | `dotnet/skills` | 108 | Repository for skills to assist AI coding agents with .NET and C# |
| 5,445 | `maziyarpanahi/openmed` | 74 | Local-first healthcare AI: clinical NER & HIPAA PII de-identification  |


### 판정에서 제외 (SKILL.md 0개)

| 스타 | 저장소 | 설명 |
|---|---|---|
| 159,013 | `Snailclimb/JavaGuide` | Java 面试 & 后端通用面试指南，覆盖计算机基础、数据库、分布式、高并发、系统设计与 AI 应用开发 |
| 139,757 | `farion1231/cc-switch` | A cross-platform desktop All-in-One assistant for Claude Code, Codex, |
| 123,467 | `Graphify-Labs/graphify` | Turn any codebase, with its docs, SQL schemas, configs, and PDFs, into |
| 55,001 | `hesreallyhim/awesome-claude-code` | A hand-picked collection of the finest of resources for the most aweso |
| 52,922 | `VoltAgent/awesome-openclaw-skills` | The awesome collection of OpenClaw skills. 5,400+ skills filtered and  |
| 48,070 | `jeecgboot/JeecgBoot` | 【低代码v2.0，一句话即可生成整个系统】企业级AI低代码平台，一键生成前后端代码甚至整个系统。 AI Skills 一句话画流程、设计表单 |
| 35,154 | `VoltAgent/awesome-agent-skills` | A curated collection of 1000+ agent skills from official dev teams and |
| 28,852 | `Ebazhanov/linkedin-skill-assessments-quizzes` | Full reference of LinkedIn answers 2024 for skill assessments (aws-lam |
| 25,877 | `agentskills/agentskills` | Specification and documentation for Agent Skills |
| 25,057 | `flipped-aurora/gin-vue-admin` | 🚀Vite+Vue3+Gin拥有AI辅助的基础开发平台，企业级业务AI+开发解决方案，内置mcp辅助服务，内置skills管理，支持TS和J |
| 16,059 | `alibaba/zvec` | A lightweight, lightning-fast, in-process vector database |
| 15,253 | `travisvn/awesome-claude-skills` | A curated list of awesome Claude Skills, resources, and tools for cust |
| 11,871 | `trimstray/test-your-sysadmin-skills` | A collection of Linux Sysadmin Test Questions and Answers. Test your k |
| 10,831 | `x-hw/amazing-qr` | 💮 amazing QRCode generator (supporting animated gif) - amazing 二维码生成器（ |
| 9,820 | `hoochanlon/hamuleite` | 🌊深度整合全球顶尖学术、金融与教育资源：学术板块汇聚 JSTOR、Taylor & Francis、剑桥大学出版社等权威平台的论文，并接入  |
| 9,542 | `olistic/warriorjs` | 🏰 An exciting game of programming and Artificial Intelligence |
| 8,192 | `xixu-me/xget` | Ultra-high-performance, secure, all-in-one acceleration engine for dev |
| 7,838 | `cassidoo/getting-a-gig` | Guide for getting a gig as a tech student. |
| 6,735 | `sourcerer-io/sourcerer-app` | 🦄 Sourcerer app makes a visual profile from your GitHub and git reposi |
| 6,614 | `MycroftAI/mycroft-core` | Mycroft Core, the Mycroft Artificial Intelligence platform.  |
| 6,467 | `eastlakeside/interpy-zh` | 📘《Python进阶》（Intermediate Python - Chinese Version） |
| 6,257 | `heilcheng/awesome-agent-skills` | Tutorials, Guides and Agent Skills Directories |
| 6,206 | `ikaijua/Awesome-AITools` | Collection of AI-related utilities. Welcome to submit pull requests /收 |
| 5,788 | `0xNyk/awesome-hermes-agent` | Independent directory of useful skills, plugins, memory providers, too |

---

## 이 표에 없는 저장소

판정 범위는 상위 150개다. 그 아래는 기계 판정을 하지 않았다. 150은 비용과 의미가 갈리는 선에서 고른 숫자이고, 더 내려갈 이유가 생기면 내린다([5.1](../part5/01-collection.md)).

본문에서 리뷰했지만 이 표에 없는 저장소가 있다. 스타수가 150위 아래이거나 기준점 조회로만 들어온 경우다.

| 저장소 | 스타 | 리뷰 위치 |
|---|---|---|
| `cloudflare/skills` | 2,974 | [6.6](../part6/06-cloudflare.md) |
| `microsoft/skills` | 3,075 | [6.5](../part6/05-microsoft.md) |
| `NVIDIA/skills` | 3,512 | [6.8](../part6/08-others.md) |
| `microsoft/skill-recorder` | 4,185 | [8.3](../part8/03-builders.md) |
| `dotnet/skills` | 5,543 | [6.5](../part6/05-microsoft.md) |
| `google/agents-cli` | 6,043 | [6.4](../part6/04-google.md) |
| `openai/plugins` | 7,276 | [6.3](../part6/03-openai.md) |
| `trailofbits/skills` | 7,351 | [8.1](../part8/01-security.md) |
| `anthropics/defending-code-reference-harness` | 7,542 | [6.2](../part6/02-anthropic-others.md) |
| `android/skills` | 7,644 | [6.4](../part6/04-google.md) |
| `timescale/pg-aiguide` | 1,854 | [6.8](../part6/08-others.md) |
| `alibaba/skill-up` | 1,131 | [8.3](../part8/03-builders.md) |
| `anthropics/launch-your-agent` | 1,026 | [6.2](../part6/02-anthropic-others.md) |
| `anthropics/k12-teacher-skills` | 544 | [6.2](../part6/02-anthropic-others.md) |
| `github/copilot-plugins` | 369 | [6.7](../part6/07-github.md) |
| `cloudflare/agent-skills-discovery-rfc` | 351 | [6.6](../part6/06-cloudflare.md) |
| `vercel/vercel-plugin` | 296 | [6.8](../part6/08-others.md) |
| `aws-samples/sample-well-architected-skills-and-steering` | 272 | [6.8](../part6/08-others.md) |
| `taneltaluri/evolve-skill` | 2 | [8.3](../part8/03-builders.md) |

(수집 날짜: 2026-10-04)

**스타수가 낮은 것이 중요도가 낮다는 뜻이 아니다.** `dotnet/skills`(5,543)는 평가 인프라가 생태계 최고 수준이고, `cloudflare/agent-skills-discovery-rfc`(351)는 디스커버리 공백을 규격으로 다룬 유일한 제안이다([9.1](../part9/01-star-traps.md)).

---

다음: [부록 C 용어집](c-glossary.md)
