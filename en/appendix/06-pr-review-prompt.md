[Contents](../../README.md#contents) › [Appendix](README.md) · **English** | [繁體中文](../../zh-TW/appendix/06-pr-review-prompt.md)

# Appendix F: PR Review Prompt

A review-only prompt for checking a pull request against the codebase it changes. The agent learns the repository first, then judges the change in that context.

## How to use it

1. Open the repository in your coding agent, with the pull request's branch checked out or its diff available.
2. Paste the block below as the task. Name the pull request at the top if the agent cannot see which one you mean.
3. Check each finding against the diff before acting on it. A finding is a claim to verify, not a confirmed fix.
4. The last line keeps the agent's understanding of the codebase for the rest of the session. Follow-up fixes can start from it. To audit a whole codebase instead of one change, use [Appendix E](05-codebase-audit-prompt.md).

## The prompt

```markdown
# Review PR

Thoroughly explore the repository to understand its architecture, core modules, data flows, dependencies, coding conventions, and implementation patterns.

Then review the PR in the context of the existing codebase, focusing on:

* Correctness: Logic errors, edge cases, and unintended behavior.
* Architecture: Consistency with existing patterns and design decisions.
* Code quality: Readability, maintainability, duplication, and unnecessary complexity.
* Reliability: Potential regressions, security issues, performance concerns, and missing tests.
* Integration: Compatibility with existing components, interfaces, and data flows.

Prioritize actionable findings by severity. For each issue, identify the affected file and lines, explain the impact, and recommend a specific fix. Avoid speculative concerns and unnecessary refactoring.

Do not modify any code.

Conclude with a concise summary of the PR, critical findings, testing gaps, and any risks that should be addressed before merging.

Use your understanding of the codebase as the foundation for subsequent development work in this session.
```

---

[← Appendix E: Codebase Audit Prompt](05-codebase-audit-prompt.md) · [Appendix](README.md) · [Contents](../../README.md#contents) · [Appendix G: Codebase Onboarding Prompt →](07-codebase-onboarding-prompt.md)
