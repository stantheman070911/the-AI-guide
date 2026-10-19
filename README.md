**English** | [繁體中文](README.zh-TW.md)

# The AI Guide

Practical, opinionated notes for shipping real products with AI-assisted ("vibecoded") development — what stack to use, how to know a site is actually production-ready, how to close the security gaps AI coding tools tend to leave open, and how to make AI-assisted design and writing not look AI-generated. Part 4 covers using AI to learn, think, and work.

## Who this is for

* **Solo founders and small teams** who build with AI coding tools and want to ship something real.
* **Anyone reviewing or inheriting a vibecoded project** who needs a list of what to check.
* **Designers and writers** who use AI and want the result to still feel authored.
* **Students and anyone new to AI** who want to learn, think, and work with it.

Part 2 assumes some familiarity with web development. Parts 3 and 4 and the appendix do not.

## Contents

### [Part 1: Build](en/part-1-build/README.md)

1. [Stack Decision](en/part-1-build/01-stack-decision.md) — the smallest stack that safely ships a SaaS, with optional upgrades, specialized alternatives, and what to avoid.
2. [The Holy Trinity + 1](en/part-1-build/02-holy-trinity-plus-one/README.md) — reusable CONSTITUTION/BRIEF/PLAN/LOG (+ RUNBOOK) documentation templates for keeping an AI coding agent aligned across a project's lifetime.
3. [Working with Coding Agents](en/part-1-build/03-working-with-coding-agents.md) — what the evidence says, the working loop, context engineering, testing, review, and deployment.
4. [Building with LLMs](en/part-1-build/04-building-with-llms.md) — model choice by evaluation, structured output, retrieval, cost, observability, and local models.

### [Part 2: Ship](en/part-2-ship/README.md)

1. [Website Production Readiness Checklist](en/part-2-ship/01-production-readiness-checklist.md) — everything to check before a vibecoded site goes live: mobile, SEO, forms, performance, accessibility, and more.
2. [Security Remediation Playbook](en/part-2-ship/02-security-remediation-playbook.md) — fixes for the vulnerabilities AI-generated code most often introduces, organized by the OWASP Top 10:2025.
3. [Securing AI Features and Coding Agents](en/part-2-ship/03-securing-ai-features-and-agents.md) — prompt injection, the lethal trifecta, tool permissions, MCP servers, and running agents safely.

### [Part 3: Craft](en/part-3-craft/README.md)

1. [How to Not Look AI-Generated](en/part-3-craft/01-how-to-not-look-ai-generated.md) — a designer's guide to keeping authorship and a point of view in AI-assisted design work.
2. [Copywriting Guide](en/part-3-craft/02-copywriting-guide.md) — ten classic copywriting lessons, eight additions for the AI and social era, and a pre-publish checklist.
3. [Writing with AI](en/part-3-craft/03-writing-with-ai.md) — an editing workflow for AI-drafted prose and research without invented sources.

### [Part 4: Learn and Think](en/part-4-learn-think/README.md)

1. [AI Fundamentals](en/part-4-learn-think/01-ai-fundamentals.md) — outcome and context, models, tools, MCP, skills, and agents.
2. [Learning with AI](en/part-4-learn-think/02-learning-with-ai.md) — active production, the research evidence, ten roles for AI as a learning coach, and spaced repetition.
3. [Thinking with AI](en/part-4-learn-think/03-thinking-with-ai.md) — judgment, the jagged frontier, hallucination and sycophancy, and cross-checking AI output.
4. [Creating with AI](en/part-4-learn-think/04-creating-with-ai.md) — a Second Brain, agent permissions, verification, and choosing what to build.
5. [Living with AI](en/part-4-learn-think/05-living-with-ai.md) — four dimensions of life, a skill stack, one craft, focus and rest.
6. [The Impact of AI](en/part-4-learn-think/06-impact-of-ai.md) — work, new hires, startups, academic integrity, data security, and society.

### [Appendix](en/appendix/README.md)

* [A. Core Writing Principles](en/appendix/01-writing-principles.md) — the writing rules I give AI tools when asking them to write or edit prose.
* [B. CLAUDE.md Preset — Rules for Coding](en/appendix/02-claude-md-coding-rules.md) — a starting `CLAUDE.md` with one prime directive and twelve coding rules.
* [C. Skills and Tools I Use](en/appendix/03-skills-and-tools.md) — my running list of the skills and tools I use.
* [D. Evaluating Tools and Skills](en/appendix/04-evaluating-tools-and-skills.md) — trust tiers, a vetting checklist, and vetted choices by use case.
* [E. Codebase Audit Prompt](en/appendix/05-codebase-audit-prompt.md) — a review-only prompt that asks an agent for the smallest set of changes worth making.
* [F. PR Review Prompt](en/appendix/06-pr-review-prompt.md) — a review-only prompt that checks a pull request against the codebase it changes.
* [G. Codebase Onboarding Prompt](en/appendix/07-codebase-onboarding-prompt.md) — a prompt that has an agent study a codebase and report back before a feature session.
* [H. Spec Implementation Prompt](en/appendix/08-spec-implementation-prompt.md) — a prompt that has an agent build from a product specification and flag what it cannot decide.

## Suggested reading paths

| If you are… | Read |
| --- | --- |
| New to shipping with AI | Part 1 through Part 3, in order |
| New to AI | [AI Fundamentals](en/part-4-learn-think/01-ai-fundamentals.md), then [Learning with AI](en/part-4-learn-think/02-learning-with-ai.md) and [Thinking with AI](en/part-4-learn-think/03-thinking-with-ai.md) |
| Launching soon | [Checklist](en/part-2-ship/01-production-readiness-checklist.md) (P0 items first), then the [Security Playbook](en/part-2-ship/02-security-remediation-playbook.md) |
| Starting a project with an AI coding agent | [Working with Coding Agents](en/part-1-build/03-working-with-coding-agents.md), [The Holy Trinity + 1](en/part-1-build/02-holy-trinity-plus-one/README.md), then [Appendix B](en/appendix/02-claude-md-coding-rules.md) |
| Adding an AI feature to a product | [Building with LLMs](en/part-1-build/04-building-with-llms.md), then [Securing AI Features and Coding Agents](en/part-2-ship/03-securing-ai-features-and-agents.md) |
| A designer or writer | [How to Not Look AI-Generated](en/part-3-craft/01-how-to-not-look-ai-generated.md), the [Copywriting Guide](en/part-3-craft/02-copywriting-guide.md), [Writing with AI](en/part-3-craft/03-writing-with-ai.md), then [Appendix A](en/appendix/01-writing-principles.md) |

## Quick lookup

| Topic | Where |
| --- | --- |
| Which services to start with | [Stack Decision](en/part-1-build/01-stack-decision.md#1-default-stack) |
| Background jobs and queues | [Stack Decision §6](en/part-1-build/01-stack-decision.md#6-background-jobs) |
| Writing an AGENTS.md or CLAUDE.md | [Context engineering](en/part-1-build/03-working-with-coding-agents.md#context-engineering) · [Appendix B](en/appendix/02-claude-md-coding-rules.md) |
| Keeping an AI agent aligned with requirements | [The Holy Trinity + 1](en/part-1-build/02-holy-trinity-plus-one/README.md) |
| Writing testable acceptance criteria | [BRIEF template](en/part-1-build/02-holy-trinity-plus-one/BRIEF.md#acceptance-criteria) |
| Choosing a model | [Building with LLMs](en/part-1-build/04-building-with-llms.md#choose-models-with-your-own-evaluation-set) |
| Retrieval (RAG) | [Building with LLMs](en/part-1-build/04-building-with-llms.md#retrieval-rag) |
| What to fix first before launch (P0/P1/P2) | [Checklist: the higher-level audit](en/part-2-ship/01-production-readiness-checklist.md#the-higher-level-audit) |
| API keys and secrets | [Checklist §18](en/part-2-ship/01-production-readiness-checklist.md#18-secrets--api-keys) · [Playbook](en/part-2-ship/02-security-remediation-playbook.md#secrets-and-keys) |
| Authorization and database policies (RLS) | [Playbook](en/part-2-ship/02-security-remediation-playbook.md#a01-broken-access-control) |
| Rate limiting and spend caps | [Checklist §22](en/part-2-ship/01-production-readiness-checklist.md#22-abuse-prevention--cost-protection) · [Playbook #19](en/part-2-ship/02-security-remediation-playbook.md#19-missing-rate-limits-and-spend-controls---high) |
| Supply chain and CI/CD | [Playbook](en/part-2-ship/02-security-remediation-playbook.md#a03-software-supply-chain-failures) |
| Prompt injection | [Securing AI Features and Coding Agents](en/part-2-ship/03-securing-ai-features-and-agents.md#the-lethal-trifecta) |
| Auditing an existing codebase | [Appendix E](en/appendix/05-codebase-audit-prompt.md) |
| Reviewing a pull request with an agent | [Appendix F](en/appendix/06-pr-review-prompt.md) |
| Starting a feature session on an existing codebase | [Appendix G](en/appendix/07-codebase-onboarding-prompt.md) |
| Having an agent build from a spec | [Appendix H](en/appendix/08-spec-implementation-prompt.md) |
| Vetting a skill or MCP server | [Appendix D](en/appendix/04-evaluating-tools-and-skills.md#vetting-checklist) |
| Accessibility | [Design §23](en/part-3-craft/01-how-to-not-look-ai-generated.md#23-treat-accessibility-as-a-design-constraint) |
| Testing whether a design looks generic | [Three final tests](en/part-3-craft/01-how-to-not-look-ai-generated.md#three-final-tests) |
| Headlines, offers, and proof | [Copywriting Guide](en/part-3-craft/02-copywriting-guide.md) |
| Learning with AI without depending on it | [Learning with AI](en/part-4-learn-think/02-learning-with-ai.md) |
| Checking AI answers and agent work | [Thinking with AI §5](en/part-4-learn-think/03-thinking-with-ai.md#5-two-kinds-of-error-wrong-answers-and-wrong-actions) |
| A personal knowledge base (Second Brain) | [Creating with AI §1](en/part-4-learn-think/04-creating-with-ai.md#1-build-your-own-second-brain) |
| Academic integrity and disclosing AI use | [The Impact of AI §8](en/part-4-learn-think/06-impact-of-ai.md#8-academic-integrity-follow-the-specific-rules-first) |

## How this guide is organized

* English pages live in [`en/`](en/) and Chinese pages in [`zh-TW/`](zh-TW/), at the same paths. Every chapter links to its other-language version at the top.
* Chapters with product details carry a "Last verified" date. Principles come first; time-sensitive tables come after.
* Open questions are tracked in the [research backlog](RESEARCH_BACKLOG.md).

## Contributing

Issues and pull requests are welcome in English or Chinese.

* [Contributing guide](CONTRIBUTING.md) — how to propose changes, add a chapter, and keep translations in sync.
* [Style guide](STYLE_GUIDE.md) and [glossary](GLOSSARY.md) — writing and translation conventions.
* [Code of conduct](CODE_OF_CONDUCT.md) — how we treat each other here.

## License

Text © 2026 Stanley Lu, licensed under [CC BY 4.0](LICENSE). Code, code samples, the [Holy Trinity + 1](en/part-1-build/02-holy-trinity-plus-one/README.md) templates, and the [Appendix B](en/appendix/02-claude-md-coding-rules.md) preset are licensed under the [MIT License](LICENSE-CODE).
