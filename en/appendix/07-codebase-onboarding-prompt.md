[Contents](../../README.md#contents) › [Appendix](README.md) · **English** | [繁體中文](../../zh-TW/appendix/07-codebase-onboarding-prompt.md)

# Appendix G: Codebase Onboarding Prompt

A prompt for the start of a feature session. The agent studies the codebase and reports what it found before it writes any code.

## How to use it

1. Open the project in your coding agent at the start of a session where you plan to add features.
2. Paste the block below as the first task. If your tool has a read-only or plan mode, use it.
3. Read the overview. Correct anything the agent got wrong before you ask for the first feature; its mistakes here carry into every change that follows.
4. Then describe the first feature. To review one change instead, use [Appendix F](06-pr-review-prompt.md); to audit the whole codebase, use [Appendix E](05-codebase-audit-prompt.md).

## The prompt

```markdown
Please thoroughly explore and analyze this codebase to develop a comprehensive understanding of its architecture, structure, and implementation patterns.

We will be adding new features throughout this session, so take the time to understand the existing functionality, key components, data flows, dependencies, and design decisions.

Pay particular attention to the project's coding conventions, architectural patterns, and how different parts of the system interact.

Do not make any code changes yet. Your goal is to build a solid understanding of the codebase so that future features can be implemented cleanly, consistently, and without introducing unnecessary complexity or regressions.

Once your analysis is complete, provide a concise overview of the architecture, important modules, existing patterns, and any technical constraints or potential risks we should keep in mind.

Use this understanding as the foundation for all subsequent development work in this session.
```

---

[← Appendix F: PR Review Prompt](06-pr-review-prompt.md) · [Appendix](README.md) · [Contents](../../README.md#contents)
