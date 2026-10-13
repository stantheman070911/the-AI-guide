[Contents](../../README.md#contents) › [Part 4: Learn and Think](README.md) · **English** | [繁體中文](../../zh-TW/part-4-learn-think/01-ai-fundamentals.md)

# AI Fundamentals

Decide what to do first; then understand models, context, tools, and agents. This chapter is the shared foundation for the rest of Part 4, written for readers starting to use AI seriously.

> Last verified: 2026-10-13.

> **Original language:** Traditional Chinese. This English version is a translation. If the two versions disagree, the [Chinese original](../../zh-TW/part-4-learn-think/01-ai-fundamentals.md) is authoritative.

## 1. Decide what to do before deciding whether to use AI

AI is worth something when it makes **work worth doing** easier to finish.

> **There is nothing so useless as doing efficiently that which should not be done at all.**
>
> — Peter Drucker ([Harvard Business Review, 1963](https://hbr.org/1963/05/managing-for-business-effectiveness))

A common mistake is to see what AI can do and then look for a use for it. The time goes into products nobody needs, processes nobody asked for, or automation that only looks clever. The joke that "a lot of vibe coders have built a budgeting app" is about exactly this kind of interchangeable practice project. Ask first: who has what problem? What result do they need? Can AI improve that result at a reasonable cost?

Part 4 can be read as one relationship:

> **Outcome × Context → more precise output**

* **Outcome:** what exactly to deliver, for whom, and what counts as done.
* **Context:** the background of the task, existing material, constraints, past decisions, and quality standards.
* **Verification and judgment:** whether the result serves its purpose is still a person's responsibility.

Before using AI, decide whether the task needs reasoning and generation. Fixed-rule administrative work that needs no judgment is better served by a spreadsheet, a template, or conventional automation. Adding AI to a broken process only makes the errors happen faster.

## 2. Where AI fits: a motorcycle for the mind

Naval Ravikant calls AI "a motorcycle for the mind", one that still needs someone to ride it ([Naval](https://nav.al/ai)). Once execution gets cheap, human judgment is worth more (see [Thinking with AI §1](03-thinking-with-ai.md#1-when-execution-is-abundant-judgment-is-the-advantage)).

AI is good at automation, coding, and information processing. It is still limited in independent reasoning, understanding of the physical world, and agency (the ability to act on its own initiative), so it needs human oversight and judgment.

People take roughly three stances toward AI (from notes on the video The Digital Renaissance):

| Type | Behavior | Main weakness |
| --- | --- | --- |
| **Purist** | Rejects AI and technological progress | Misses opportunities |
| **Automaton / Cyborg** | Outsources thinking and decisions to technology | Loses independent judgment |
| **Digital Renaissance Person** | Uses AI selectively while building their own judgment and skills | The recommended stance |

Let AI assist and execute; keep direction, quality, and decisions for yourself. The core model:

> **Human judgment + multidisciplinary skills + AI leverage = the ability to produce valuable work independently**

## 3. Learn the concepts before choosing tools

AI tools change fast: names, interfaces, prices, and features all move. How a model uses context and calls tools, and how a person sets goals and checks results, last much longer. Once you understand the structure, you do not have to start over every time you switch tools.

For a sense of the pace: between 22 September and 7 October 2026, Anthropic released three models, [Claude Opus 5.5](https://www.anthropic.com/news/claude-opus-5-5), [Sonnet 5.5](https://www.anthropic.com/claude-sonnet-5-5), and [Haiku 5.5](https://www.anthropic.com/claude-haiku-5-5).

Capability gains come from larger models, and also from compute spent at inference time, post-training, and the way agent systems use external tools. Researchers still disagree about how fast progress is.

Capability is rising quickly. The research group **METR** tracks it by asking how long a task, measured in expert human time, an AI agent can complete on its own with 50% success. Over the long run that length has doubled roughly every seven months, possibly faster since 2024 ([METR](https://metr.org/blog/2025-03-19-measuring-ai-ability-to-complete-long-tasks/)). METR estimates that publicly available frontier models in February and March 2026 could handle tasks that take a person about 12 hours at 50% success, with a confidence interval of 5 to 61 hours ([METR](https://metr.org/blog/2026-05-19-frontier-risk-report/)).

The higher the success rate you require, the shorter the task: at 80% success, the task length is several times shorter. METR also notes that its current task suite cannot reliably measure beyond 16 hours, and that the tasks are mostly automatically scored software tasks. A 50% horizon of X hours does not mean every task under X hours can be safely handed off ([METR](https://metr.org/notes/2026-01-22-time-horizon-limitations/)).

## 4. Basic terms

| Term | What it means in practice |
| --- | --- |
| **LLM (large language model)** | The core model that processes input and generates a response; in many workflows it does the understanding and reasoning. |
| **Token** | The basic unit a model counts when it processes text and other content. |
| **Prompt** | The question, request, or instruction a user gives. |
| **Context** | The relevant information the model can see during a task, including instructions, conversation history, and documents. |
| **Context window** | The most context a model can hold at once. |
| **Tool** | An external capability the model can use, such as reading and writing files, running commands, or querying data. |
| **API** | The interface and rules software systems use to exchange requests and results. |
| **API key** | A credential that identifies and authorizes you to a service. Treat it as a password; never paste it into a public repo, a screenshot, or a chat. |
| **CLI** | Command-line interface; a way to operate a program with text commands. |
| **Connector / Plugin** | A way to bring an external service into an AI workspace, usually without building the integration yourself. |
| **MCP** | Model Context Protocol; a common protocol for connecting AI systems to tools and data sources. |
| **Agent** | A system that, given a goal, repeatedly plans, acts, checks results, and adjusts. |
| **Skill / Agent Skill** | Saved, reusable rules, steps, and output formats. |

Products mentioned in Part 4 include Claude, ChatGPT, Claude Code, Codex, OpenClaw, Hermes, Obsidian, and GitHub.

## 5. From a model to a product that gets work done

AI products can be understood in four layers:

1. **Compute:** the data centers, chips, and computing resources that run models.
2. **Model:** generates content from input and supports capabilities such as reasoning.
3. **Harness:** the components that let a model use documents, memory, instructions, and external tools.
4. **Agent:** organizes multi-step actions within set goals and permissions, and keeps checking progress.

Mapped to real products: Claude Code, Codex, and OpenClaw are agents; Projects, Skills, and MCP are harness; Claude, GPT, and Gemini are models; GPUs, data centers, and chip manufacturing (TSMC, for example) are compute.

A basic conversation works like this:

> existing context + new prompt → model response

The same prompt with different context can produce a completely different response. Tell a model "I got 42 on my math midterm", and one set up as a strict teacher will answer very differently from one set up as a kind teacher.

Add tools and a loop that can run repeatedly, and the system can also search, update documents, run tests, or schedule follow-up actions. That calls for clearer permissions and verification.

## 6. What tools, MCP, and skills each do

The three do different jobs:

* **Tools** answer "what can the system do": whether it can access documents, run programs, or call services.
* **MCP** answers "how do tools and data sources get connected": a common way to plug them in.
* **Skills** answer "what rules to follow when the same kind of work keeps coming back": the approach, steps, checks, and format, written down once and applied each time.

Say you turn a batch of documents into the same format every week. You should not have to explain the requirements to the model each time. Write the steps as an SOP or a skill, and every output follows the same standard. This suits fixed-format replies, recurring reports, and high-volume repetitive processing; open-ended creative questions may not need such a strict process.

These pieces are also moving toward open standards. In December 2025, Anthropic donated MCP to the Agentic AI Foundation under the Linux Foundation ([Anthropic](https://www.anthropic.com/news/donating-the-model-context-protocol-and-establishing-of-the-agentic-ai-foundation)); the same month, Agent Skills became an open standard ([agentskills.io](https://agentskills.io)), now supported by OpenAI, Microsoft, GitHub, Cursor, and others. A skill you write is not tied to one vendor. The smallest skill can be a single `SKILL.md` in a folder:

```markdown
<!-- weekly-report/SKILL.md -->
---
name: weekly-report
description: Turn this week's notes into a weekly report
---

1. Read this week's files in notes/
2. Organize them in the format of template.md
3. List the items that are not finished yet
```

Third-party skills and MCP servers are code you install; vet them first ([Appendix D](../appendix/04-evaluating-tools-and-skills.md#vetting-checklist)).

## 7. Context is the foundation of output quality

### Give the prompt the whole task

What the model sees directly shapes the answer. "Write me a project plan" gets a very different result from a request that gives the target customers, product conditions, existing material, deadline, delivery format, and review criteria.

An effective handoff answers at least four questions:

1. **What to do:** the goal, scope, and deliverable.
2. **What to base it on:** sources, background, and constraints.
3. **How good it must be:** quality standard, format, and completion conditions.
4. **How to know it is right:** a check, test, or human review you can actually run.

A SoW (Statement of Work) or PRD (Product Requirements Document) exists to turn the expectations in your head into a specification another person, or an AI, can understand.

Before spending on an expensive model or a long process, you can use a cheaper model to tidy the prompt and clarify the requirements and data structure, so the context stays relevant, clear, and free of contradictions.

From mid-2025 the industry started using the term **context engineering** (Shopify CEO Tobi Lütke and Andrej Karpathy both promoted it publicly), with the emphasis on getting the right information in front of the model at the right time. For the practice with coding agents, see [Working with Coding Agents](../part-1-build/03-working-with-coding-agents.md#context-engineering).

### Context windows and the limits of long conversations

The context window is how much information a model can process at once. Once conversation, attachments, and system instructions pile up, the tool has to decide what to do with the overflow. Some agent tools use **compaction**: summarize what came before and carry the summary forward.

A summary keeps the work going, but it is lossy. Details can drop out, and repeated compaction can slowly pull the system away from the original requirements.

Even within capacity, where information sits affects how well it is used. The 2023 "Lost in the Middle" study found that models do not use information in the middle of a long context as reliably as information elsewhere ([Liu et al.](https://arxiv.org/abs/2307.03172)).

So for long tasks:

* Put the purpose, key constraints, and completion criteria where they are easy to find.
* Do not bury important rules in a long conversation or an unrelated attachment.
* Regularly write down current conclusions, decisions, and open questions; start a new conversation when needed.
* Put anything that needs to last into a document, not only the chat history.

### Memory, projects, and persistent context

Memory and project features let a fixed background be reused across related tasks: personal preferences, team conventions, project scope, shared documents. That saves repeated explanation. But more memory can also mean more weight: irrelevant old material interferes with new tasks, and the model may lean too far toward past preferences.

Sort what you keep into three kinds:

* **Long-term facts and rules:** fairly stable, worth keeping.
* **Project material:** valid only for a particular goal, client, or product.
* **Single-task context:** no need to keep once the task is done.

Memory, projects, files, skills, data connected through MCP, and tool results are all context. Agents like OpenClaw and Hermes update their own context as they work. Anyone can buy the model; your material, history, and standards are yours alone. The Second Brain in [Creating with AI](04-creating-with-ai.md#1-build-your-own-second-brain) is built for that.

---

[← Writing with AI](../part-3-craft/03-writing-with-ai.md) · [Part 4: Learn and Think](README.md) · [Contents](../../README.md#contents) · [Learning with AI →](02-learning-with-ai.md)
