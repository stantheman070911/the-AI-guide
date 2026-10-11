[Contents](../../README.md#contents) › [Part 1: Build](README.md) · **English** | [繁體中文](../../zh-TW/part-1-build/03-working-with-coding-agents.md)

# Working with Coding Agents

How to get reliable work out of an AI coding agent, session by session. [The Holy Trinity + 1](02-holy-trinity-plus-one/README.md) covers the documents that persist across sessions; this chapter covers what happens inside one.

> Last verified: 2026-10-11.

## What the evidence says

* **Feeling fast is not being fast.** In METR's 2025 randomized trial, 16 experienced developers working in their own repositories took 19% longer with early-2025 AI tools, while believing they had been 20% faster ([METR](https://metr.org/blog/2025-07-10-early-2025-ai-experienced-os-dev-study/)). METR's February 2026 follow-up suggests later tools do speed developers up, but its confidence intervals include no effect and METR calls the data "very weak evidence" of how much ([update](https://metr.org/blog/2026-02-24-uplift-update/)). Measure on your own work before trusting the impression.
* **AI amplifies the team you already have.** The 2025 DORA report found about 90% of developers using AI, and that it magnifies existing strengths and dysfunctions rather than fixing delivery on its own ([Google](https://blog.google/innovation-and-ai/technology/developers-tools/dora-report-2025/)). Tests, small changes, and review matter more with agents, not less.
* **The code needs security review.** See the [Security Remediation Playbook](../part-2-ship/02-security-remediation-playbook.md#why-this-matters-more-with-ai-written-code).

## The loop

1. **Explore.** Have the agent read the relevant code and explain how it works before changing anything. Wrong understanding is cheaper to fix than wrong code.
2. **Plan.** Ask for a plan: files to touch, approach, risks, how it will be verified. Correct the plan, not the diff.
3. **Implement one slice.** A change you can review in one sitting.
4. **Verify.** The agent runs tests, type checks, lint, and the app, and shows the output. "It should work now" is not evidence.
5. **Review and commit.** Read the diff yourself. Commit. Start the next task in a fresh or compacted session.

Give the agent a way to check its own work: a test suite, a type checker, a script that reproduces the bug, a browser it can open. Without a check it can run, "looks done" is the only signal the agent has, and you become the verification loop ([Claude Code docs](https://code.claude.com/docs/en/best-practices)).

## Context engineering

The model only knows what is in its context window, and quality degrades as the window fills. Anthropic calls this "context rot" and treats context as a finite budget ([Anthropic](https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents)).

* **Project instruction file.** Use [AGENTS.md](https://agents.md), the cross-tool format now stewarded by the Linux Foundation's Agentic AI Foundation, or your tool's equivalent (`CLAUDE.md`). Include build and test commands, conventions, and the mistakes the agent keeps making. Keep it short; it loads into every session. [Appendix B](../appendix/02-claude-md-coding-rules.md) is a starting point.
* **Load just in time.** Point to files and paths instead of pasting them. Let the agent search.
* **One task per session.** Clear or compact the context between tasks. A long session full of abandoned approaches misleads the model.
* **Keep state outside the window.** Progress, decisions, and next steps go in a file (`LOG.md`, or a scratch `NOTES.md`) that a fresh session can read.
* **Delegate exploration.** Sub-agents can search a codebase or the web and return a short summary, keeping the main context clean.
* **Package repeated workflows as skills.** An [Agent Skill](https://agentskills.io) is a folder with a `SKILL.md` file and optional scripts. Agents read only its name and description until a task needs it, so many skills cost little context. The format is supported across most major coding agents. Vet third-party skills first ([Appendix D](../appendix/04-evaluating-tools-and-skills.md)).
* **Connect MCP servers only when needed.** Each one adds tool definitions to the context and widens the attack surface.

## Writing the task

A good task states the goal, the constraints, and how to know it is done:

```text
Add rate limiting to POST /api/generate.
Limit: 20 requests per user per hour, using the existing Upstash client in lib/redis.ts.
Return 429 with Retry-After. Do not change the response format for successful requests.
Done when: a new test in tests/api/generate.test.ts sends 21 requests and the last one gets 429,
and the existing test suite passes.
```

Point to an existing file as the pattern to follow. Say what not to change. When requirements are ambiguous, ask the agent to list its questions before writing code.

## Testing

* For core logic, write or approve the tests first. A failing test is a target the agent cannot argue with.
* Never accept a change that weakens, skips, or deletes a failing test to get green.
* The session that wrote the code is a poor judge of whether it is finished. Review in a fresh session, or run the completion audit from [The Holy Trinity + 1](02-holy-trinity-plus-one/README.md#the-completion-trap-and-how-to-close-it).
* Check UI changes in a real browser at real widths.

## Debugging

* Give the agent the exact error, logs, and steps to reproduce.
* Have it reproduce the bug first, then rank hypotheses and test them one at a time.
* If it proposes the same fix twice, stop. Clear the context, restate what is known, and start again.

## Refactoring

Refactor only with tests passing before and after. Keep refactoring commits separate from behavior changes, so a reviewer can tell which is which.

## Review

Read agent diffs as you would a capable new hire's pull request. Spend attention where mistakes are expensive: authorization, data access, new dependencies, migrations, error handling, and CI configuration. AI review tools are a useful second pass, not a substitute.

## Permissions and safety

Agents run commands with your credentials. Sandboxing, secret handling, MCP vetting, and untrusted input are covered in [Securing AI Features and Coding Agents](../part-2-ship/03-securing-ai-features-and-agents.md#coding-agents-you-run).

## Deployment

Agents open pull requests; CI runs tests and security checks; preview deployments get a human look; humans approve production. Migrations and infrastructure changes get explicit review and a rollback plan ([RUNBOOK template](02-holy-trinity-plus-one/RUNBOOK.md)).

## Vibe mode and engineering mode

Loose, fast iteration is fine for a local prototype with no users and no real data. Once real users, data, payments, or credentials are involved, switch to engineering mode: acceptance criteria, tests, security review, full diff review. The switch is one-way for that surface ([Constitution, Law V](02-holy-trinity-plus-one/CONSTITUTION.md#law-v--two-risk-modes)).

---

[← The Holy Trinity + 1](02-holy-trinity-plus-one/README.md) · [Part 1: Build](README.md) · [Contents](../../README.md#contents) · [Building with LLMs →](04-building-with-llms.md)
