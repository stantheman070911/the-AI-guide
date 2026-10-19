[Contents](../../README.md#contents) › [Appendix](README.md) · **English** | [繁體中文](../../zh-TW/appendix/05-codebase-audit-prompt.md)

# Appendix E: Codebase Audit Prompt

A review-only prompt for auditing a finished codebase. It asks an AI coding agent for the smallest set of changes that would meaningfully improve the project, not the longest list of findings.

## How to use it

1. Open the project in your coding agent and paste the block below as the task.
2. The agent should not change anything. If your tool has a read-only or plan mode, use it.
3. Check each finding against the code before acting on it. A finding is a claim to verify, not a confirmed fix.
4. Apply the recommended priorities one at a time. [Appendix B](02-claude-md-coding-rules.md) covers how to make each change.

## The prompt

```markdown
# Codebase Audit & Review

This is a fully implemented project. Audit the existing codebase and identify only improvements that are genuinely worth making.

Guiding principle:
"There is nothing so useless as doing efficiently that which should not be done at all."

## 1. Approach

* Understand before evaluating. Explore the project architecture, key modules, data flows, dependencies, conventions, and constraints before concluding.
* Focus on what matters. Assess security, correctness, reliability, performance, and maintainability. Consider other areas only when they have meaningful impact.
* Verify before reporting. Trace relevant code paths and examine existing safeguards before identifying an issue. Distinguish confirmed problems from potential risks.
* Review only. Do not modify code, configuration, dependencies, or project files.

## 2. Review Standards

* Value over volume. Report an issue only when fixing it provides a clear, practical benefit. Do not manufacture findings to fill categories.
* Evidence over speculation. Ground each finding in the actual implementation. Include file paths and line numbers. State any uncertainty or verification limits explicitly.
* Simplicity over complexity. Prefer removing, consolidating, or simplifying code over introducing new mechanisms. Recommend dependencies, abstractions, or architectural layers only when their benefits clearly justify their costs.
* Impact over convention. Ignore cosmetic issues, subjective style preferences, generic best practices, and hypothetical risks without a credible failure scenario.
* Remove unnecessary work. Identify dead code, redundant logic, unnecessary complexity, and over-engineering when removing them would meaningfully improve the project.
* Respect existing decisions. Account for the project's actual requirements, scale, architecture, and conventions. Do not recommend changes merely to follow a different design philosophy.
* Avoid duplicate findings. Consolidate issues that share the same root cause or can be resolved by the same change.

## 3. Output

### Architecture Overview

Briefly summarize the architecture, key modules, major data flows, important patterns, dependencies, and relevant constraints. Include only the context needed to understand the findings.

### Findings

Group findings by severity:

* Critical: Immediate security, data integrity, or system availability risk.
* High: Significant correctness, security, reliability, or performance issue with a credible real-world impact.
* Medium: Meaningful weakness or unnecessary complexity that warrants correction but is not urgent.
* Low: Small, demonstrable improvement worth making when convenient.

For each finding, provide:

* Location: File path and line number(s).
* Problem: What is wrong and why.
* Impact: The concrete consequence, including the conditions under which it occurs.
* Minimal fix: The simplest effective correction.
* Effort: Small (S), Medium (M), or Large (L).

Order findings by severity and practical impact. Omit empty categories.

### Recommended Priorities

Identify up to 5 improvements worth addressing first, ranked by impact, urgency, effort, and risk reduction.

Briefly explain why each deserves priority. If fewer than 5 improvements are justified, list fewer.

## 4. Final Constraints

* Do not make any changes.
* Do not treat unverified assumptions as confirmed findings.
* Do not recommend broad refactoring when a targeted correction is sufficient.
* Do not introduce complexity without a demonstrable net benefit.
* Do not confuse the number of findings with audit quality.

The objective is not to find as many problems as possible. It is to identify the smallest set of changes that would meaningfully improve the codebase.
```

---

[← Appendix D: Evaluating Tools and Skills](04-evaluating-tools-and-skills.md) · [Appendix](README.md) · [Contents](../../README.md#contents) · [Appendix F: PR Review Prompt →](06-pr-review-prompt.md)
