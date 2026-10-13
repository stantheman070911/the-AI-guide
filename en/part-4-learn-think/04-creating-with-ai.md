[Contents](../../README.md#contents) › [Part 4: Learn and Think](README.md) · **English** | [繁體中文](../../zh-TW/part-4-learn-think/04-creating-with-ai.md)

# Creating with AI

A Second Brain, agent workflows, permissions and safety, and what to build. Coding details are in [Part 1](../part-1-build/README.md), and coding-agent security in [Securing AI Features and Coding Agents](../part-2-ship/03-securing-ai-features-and-agents.md); this chapter is for anyone who makes things with AI.

> Last verified: 2026-10-13.

> **Original language:** Traditional Chinese. This English version is a translation. If the two versions disagree, the [Chinese original](../../zh-TW/part-4-learn-think/04-creating-with-ai.md) is authoritative.

## 1. Build your own Second Brain

### Why own your context

Anyone can use a general-purpose model. The documents, history, decisions, work habits, and quality standards you accumulate are yours. Organize them into a personal knowledge base you maintain over time, and you have a **Second Brain**.

A Second Brain can be just a folder plus the habit of keeping it in order. It holds notes, templates, SOPs, decision records, research, and project descriptions, in a form both you and different AI tools can read.

### Why plain text and Markdown

Plain text is simple, durable, easy to search, and does not depend on any one program. Markdown expresses headings, lists, links, and tables with a few symbols, which makes it a good base format for documents. Over time:

* Different tools can read it, so you are less locked into one platform.
* It can be version-controlled, keeping a record of changes.
* A new tool or a new colleague can use the existing material without building context from zero.
* Fix one document, and later work based on it is more likely to improve too.

### Keeping the knowledge base usable

The reliable principle is **structure over quantity**: one topic per file, clear titles, related documents linked to each other, and regular deletion of duplicate, outdated, or contradictory content.

A simple example structure (adjust as needed):

```text
Second-Brain/
├── Projects/    # active projects and requirements
├── Knowledge/   # notes, research, and reference material
├── Processes/   # SOPs, skills, recurring workflows
├── Decisions/   # important decisions and their reasons
└── Templates/   # reusable document formats
```

You can use a plain-text editor such as [Obsidian](https://obsidian.md), or just the file system. If you have programming experience, Claude Code or Codex can help you build, organize, and maintain it.

You do not need a complex system at the start. It is enough that documents can be updated, found, and reused after every task. This material may outlast any AI tool that is popular today.

References: [LLM Wiki](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f) (Andrej Karpathy; a direction for organizing personal knowledge), [Vault for Founders](https://github.com/cwlin0131/Vault-for-Founders) (an example knowledge-base structure).

## 2. Agents: from answering questions to doing work

A traditional conversation is mostly one answer at a time. An agent keeps working on a task toward a goal:

> **Plan → act → check → adjust → finish**

It may break the problem down, operate tools, check whether the result meets the goal, and change course when something goes wrong. OpenClaw and Hermes are products of this kind, though they differ in autonomy, memory, and permission management.

Agents suit large-scale document organization, repetitive format conversion, batch checking, and work that needs multi-step exploration. They also let people without a programming background build small personal tools, or start finding a way into a problem they did not know how to approach.

## 3. Permission is a spectrum

Agents can be given different levels of authority:

| Level | How it acts | Example |
| --- | --- | --- |
| **Suggests** | AI suggests; a person decides and acts | Drafts an email; the user reviews and sends it |
| **Prepares, then waits for approval** | AI prepares; key actions wait for approval | Gets documents ready to send; the owner approves |
| **Acts, then reports** | AI acts within pre-approved limits and reports afterwards | Updates a routine spreadsheet and reports changes on a schedule |
| **Highly autonomous** | AI takes external actions within set permissions | Sends messages externally without case-by-case review |

To decide the level, think of it as onboarding a new colleague: what data can they handle, what mistakes might they make, can those mistakes be undone, and which decisions need someone's approval?

Permission is also a security question. An agent that can read messages, change files, call external services, or act in your name does damage in proportion to its permissions if it is misled, compromised, or misunderstands an instruction. Match the scope of permission to the sensitivity of the data, whether the action can be reversed, and how closely you can supervise.

[OpenClaw](https://github.com/openclaw/openclaw), an open-source personal assistant that went viral in early 2026, is a concrete case. It connects to messaging platforms such as WhatsApp, Slack, and Telegram, reads messages, works with files, sends messages in the user's name, and has its own skill marketplace, ClawHub. In February 2026, the security firm Koi Security audited the 2,857 skills on ClawHub and found 341 of them malicious (about 12%), stealing credentials, API keys, and crypto wallets ([The Hacker News](https://thehackernews.com/2026/02/researchers-find-341-malicious-clawhub.html)).

Three basic rules: give only the minimum permission the task needs; check the source before installing a skill or plugin; route sensitive data through connections with access control, and do not hand the whole machine to an agent. For coding agents, see [Securing AI Features and Coding Agents](../part-2-ship/03-securing-ai-features-and-agents.md#coding-agents-you-run).

## 4. Make verification part of the work

When you hand off a task, say what to do and also how to prove it is done. For code, arrange tests; for document work, check counts, format, and sources; for research, require traceable citations.

Practical techniques:

1. **Try once before deciding whether to break it down.** For low-risk tasks that can be retried, let the system try first; guide it step by step only if it fails.
2. **Keep a state you can return to.** Save often, so you can roll back to a clean version when something breaks.
3. **Ask for simplicity.** When AI overcomplicates a solution, ask it to explain why and propose something simpler.
4. **Provide concrete visuals.** For interfaces and dashboards, a screenshot or mockup is often clearer than a long description.
5. **Give it checks it can run.** Run tests, compare output, check conditions; do not accept "done" as a text reply.
6. **Match oversight to risk.** Reversible peripheral work can get more autonomy; core logic and irreversible actions get closer review.

Some teams save their state, let the system run for a while, then accept the result or start over ([Anthropic](https://www-cdn.anthropic.com/58284b19e702b49db9302d5b6f135ad8871e7658.pdf)); whether that suits you depends on the task. For the full loop when writing code, see [Working with Coding Agents](../part-1-build/03-working-with-coding-agents.md#the-loop).

## 5. Pick a tool that fits the work

You do not need every tool at once. Pick the kind of work you do most, do it well, then add new capabilities.

Claude Code and Codex suit folders, code projects, and multi-step tasks; personal-assistant agents such as OpenClaw and Hermes suit messaging integration and scheduling. Where each tool fits, and its trust tier, is in [Appendix D](../appendix/04-evaluating-tools-and-skills.md#by-use-case). Features, plans, and prices change quickly; check the official information before adopting one.

## 6. Coding and non-coding work

For people who code, AI is an accelerator: it helps them understand code, debug, write tests, and change existing features. That is an **augmented workflow**.

For people who do not code, the change may be bigger: small tools, data conversions, or simple prototypes they could not have built alone are now within reach with AI's help. Reliability, maintenance, security, and deployment still need checking.

Anthropic's product design team calls these the "augmented workflow" and the "holy crap, I'm a developer workflow", and sees the biggest difference in the second group ([Anthropic](https://www-cdn.anthropic.com/58284b19e702b49db9302d5b6f135ad8871e7658.pdf)). Andrej Karpathy coined "vibe coding" in February 2025 ([Karpathy](https://x.com/karpathy/status/1886192184808149383)), and in November that year Collins named it Word of the Year ([Collins](https://blog.collinsdictionary.com/language-lovers/collins-word-of-the-year-2025-ai-meets-authenticity-as-society-shifts/)).

Everyday tasks to try:

* Pull key facts from a batch of documents into a table.
* Turn messy data into a consistent format, or translate it.
* Apply the same well-defined operation to many files.
* Build a small private tool that no existing product covers.
* Produce routine slides or work summaries with a fixed process.
* When researching or solving a problem, let AI propose an approach first, then refine it against the data and results.

**GitHub** hosts code and project files; think of it as a cloud drive for code. It keeps version history and supports collaboration, which makes it an important way to save and restore AI-assisted work.

References: [Appendix A: Core Writing Principles](../appendix/01-writing-principles.md) and [Appendix C: Skills and Tools I Use](../appendix/03-skills-and-tools.md) (prompts and notes), [Loot Drop](https://www.loot-drop.io/) (product case studies of failed startups).

## 7. From one-off prompts to maintainable workflows

A more mature approach than handing AI one job is to leave behind a work specification that can be run again:

1. Define the input data and the expected output.
2. Fix the necessary rules, templates, and judgment criteria.
3. Specify which steps AI may carry out on its own.
4. Add a verification step that can actually be run.
5. Keep the outputs, change history, and lessons from errors.
6. Once the process is stable, consider scheduling or automating it.

For software projects, the full version is the [Holy Trinity + 1](../part-1-build/02-holy-trinity-plus-one/README.md) templates.

## 8. Three prompts for learning while building

### Build while learning

```text
I want to build [PROJECT], but I have limited experience.

Act as my mentor. Break it into the smallest practical steps. Tell me only what I need to understand for the next step. Explain important decisions, let me choose, and help me troubleshoot as I build.

If you do something I don't understand, explain what you did and why.

Do not complete the entire project without involving me.
```

### Identify automation opportunities

```text
Review this list of my recurring tasks:

[TASK LIST]

Classify each as:

1. Suitable for AI automation
2. Suitable for AI-assisted work with human review
3. Best kept human-led

Estimate implementation difficulty and practical benefit. Recommend one low-risk task to automate first. Provide a step-by-step setup and testing plan, including how to check for errors.
```

### Improve your first draft

```text
Critique this draft as a demanding editor and experienced end user:

[DRAFT]

Target audience: [AUDIENCE]
Intended outcome: [OUTCOME]

Identify unclear assumptions, weak logic, generic content, usability problems, and missing evidence. Rank the five most important improvements.

Then help me revise one issue at a time. Do not flatter the draft.
```

## 9. The easier software is to build, the more choosing what to build matters

AI makes building cheap, so features alone rarely form a moat. [Reverse Engineer Anything (REA)](https://github.com/morluto/rea) is an MCP server that lets AI coding agents use existing reverse-engineering tools such as Ghidra, Hopper, and IDA to analyze software and rebuild compatible behavior.

Demos of tools like this teach two lessons: do not treat a demo as a benchmark, and do not judge a tool by its GitHub stars. Start with the simplest method that finishes the task.

| Easy to copy | Harder to copy |
| --- | --- |
| A generic AI chat wrapper | Deep, well-integrated workflows in a specific domain |
| Common interface patterns | Proprietary data you have the legal right to use |
| A simple convenience feature | Reliable end-to-end completion of a task |
| A demo that goes viral once | Users who keep coming back |
| The feature by itself | Distribution, trust, support, and execution |

A better product question: which frustrating process can a few mature capabilities improve?

**Legal and safety note:** analyze only software and environments you have the right to inspect. Before installing a third-party MCP server, check the permissions and dependencies it asks for. Respect licenses, intellectual property, and confidentiality obligations. Rebuilding behavior does not give you the source code or a license; use it only for learning and original work.

---

[← Thinking with AI](03-thinking-with-ai.md) · [Part 4: Learn and Think](README.md) · [Contents](../../README.md#contents) · [Living with AI →](05-living-with-ai.md)
