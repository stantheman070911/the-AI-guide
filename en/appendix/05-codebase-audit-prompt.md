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

## Objective

This is an existing, fully implemented project. Audit the codebase to identify only improvements that would materially improve its security, correctness, reliability, performance, or maintainability.

The goal is not to maximize findings, enforce idealized architecture, or generate unnecessary work. It is to identify the smallest set of changes that provides meaningful, demonstrable value.

Guiding principle:
"There is nothing so useless as doing efficiently that which should not be done at all."

## 1. Audit Approach

### Understand Before Evaluating

Establish sufficient context before drawing conclusions.

* Examine the architecture, key modules, entry points, dependencies, configuration, and major data flows.
* Identify the project's intended behavior, operating environment, scale, and relevant constraints.
* Understand existing conventions, safeguards, tests, and architectural decisions.
* Trace important interactions across modules rather than judging isolated code fragments.
* Do not assume an unfamiliar pattern is incorrect or unnecessary.

### Investigate by Risk and Impact

Prioritize areas where defects or complexity would have meaningful consequences.

Consider:

* Security: Authentication, authorization, input handling, sensitive data, trust boundaries, and credible attack paths.
* Correctness: Business logic, state transitions, edge cases, data integrity, and error handling.
* Reliability: Failure recovery, resource management, concurrency, transactional consistency, and operational resilience.
* Performance: Demonstrable bottlenecks, inefficient operations, unnecessary resource consumption, and scalability constraints.
* Maintainability: Unnecessary complexity, duplication, dead code, fragile coupling, and avoidable maintenance costs.

Focus investigation according to the project's actual architecture and risk profile. Do not force equal coverage or generate findings for every category.

### Verify Before Reporting

For each potential issue:

1. Identify the exact implementation responsible.
2. Trace the relevant execution path and affected callers or consumers.
3. Check whether existing validation, safeguards, constraints, or tests already address the concern.
4. Establish the conditions required for the issue to occur.
5. Assess the realistic impact and likelihood within the project's intended use.
6. Determine whether a correction would provide a meaningful benefit relative to its cost and complexity.

Distinguish between:

* Confirmed: The implementation provides sufficient evidence that the problem exists.
* Credible but unverified: A realistic risk exists, but a specific assumption or runtime condition remains unverified.
* Speculative: The concern lacks sufficient evidence or a credible failure scenario.

Report confirmed issues and material, credible risks only. Clearly identify any unresolved assumptions. Omit speculative concerns.

Do not equate missing tests, theoretical edge cases, or possible future requirements with confirmed defects.

### Read-Only Execution

This is strictly an audit.

* Do not modify source code, configuration, dependencies, tests, or project files.
* Do not install packages, apply fixes, generate files, or execute commands that would alter project or external state.
* Use read-only inspection and safe validation methods.
* If verification requires a prohibited action, document the limitation rather than performing it.

## 2. Review Standards

### Value Over Volume

Every finding must justify the work required to resolve it.

Do not manufacture issues to populate categories or meet an implied finding count. An audit with no actionable findings is a valid outcome.

### Evidence Over Speculation

Ground conclusions in the actual implementation.

Provide precise file paths and line references. Explain relevant execution paths, existing safeguards, and failure conditions.

Never present an assumption, inferred behavior, or unexecuted test as verified fact.

### Simplicity Over Complexity

Prefer the smallest effective correction.

Favor removing, consolidating, or simplifying existing code when appropriate. Recommend new abstractions, dependencies, infrastructure, or architectural layers only when their benefits clearly outweigh their costs.

Do not recommend replacing a working design merely because another approach is more fashionable or theoretically extensible.

### Impact Over Convention

Ignore:

* Cosmetic issues and subjective style preferences.
* Generic best-practice recommendations without project-specific justification.
* Theoretical vulnerabilities without a credible attack or failure path.
* Premature optimization without meaningful performance implications.
* Missing abstractions without demonstrated duplication or fragility.
* Missing tests without an associated material risk.
* Speculative requirements or hypothetical future scale.

### Remove Unnecessary Work

Actively identify dead code, redundant operations, duplicate logic, unnecessary dependencies, and over-engineering when their removal would meaningfully reduce complexity, risk, or maintenance effort.

Do not recommend cleanup whose cost exceeds its practical benefit.

### Respect Existing Decisions

Evaluate the project against its actual requirements, constraints, conventions, and expected operating conditions.

Do not impose a different architectural philosophy without demonstrating why the existing approach causes a meaningful problem.

### Consolidate Root Causes

Avoid duplicate or overlapping findings.

When several symptoms arise from the same root cause, report one finding that captures the underlying problem and its significant consequences.

## 3. Reporting Threshold

Before including a finding, answer these questions:

1. Evidence: What specific code demonstrates the problem?
2. Scenario: Under what realistic conditions does it matter?
3. Impact: What concrete failure, risk, waste, or maintenance burden results?
4. Existing protection: Is the concern already prevented or mitigated elsewhere?
5. Remedy: What is the simplest effective correction?
6. Value: Is the expected benefit worth the implementation and maintenance cost?

If these questions cannot be answered sufficiently, investigate further or omit the finding.

Do not lower the reporting threshold simply because few issues were found.

## 4. Output Format

### Architecture Overview

Briefly describe:

* Overall architecture and key modules.
* Major execution paths and data flows.
* Significant dependencies and design patterns.
* Relevant constraints and existing safeguards.

Include only the context necessary to understand the audit findings.

### Findings

Group findings by severity.

* Critical: Immediate or readily exploitable risk to security, data integrity, or system availability.
* High: Significant correctness, security, reliability, or performance problem with credible real-world impact.
* Medium: Meaningful weakness, operational risk, or unnecessary complexity that warrants correction but is not urgent.
* Low: Small, demonstrably beneficial improvement worth addressing when convenient.

For each finding, provide:

* Title: Concise description of the underlying issue.
* Severity: Critical / High / Medium / Low.
* Location: Exact file path and line number(s), including related locations when necessary.
* Evidence: Relevant implementation details and execution path supporting the conclusion.
* Problem: What is wrong and why existing behavior is insufficient.
* Impact: Concrete consequences and the conditions under which they occur.
* Verification: Confirmed or Credible but Unverified, including any assumptions or limitations.
* Minimal Fix: The simplest correction that addresses the root cause.
* Effort: Small (S), Medium (M), or Large (L).

Order findings by severity and practical impact. Consider likelihood and scope of impact when ranking issues within a severity level.

Omit empty severity categories.

Do not invent file paths, line numbers, execution behavior, test results, or supporting evidence.

### Recommended Priorities

Identify up to five improvements worth implementing first.

Rank them according to:

1. Expected impact and risk reduction.
2. Severity and urgency.
3. Confidence in the finding.
4. Implementation effort and complexity.
5. Potential regression risk.

Briefly explain why each improvement deserves priority and reference its corresponding finding.

Do not automatically prioritize a large architectural change over a smaller fix that delivers comparable benefits.

If fewer than five improvements are justified, recommend fewer.

### Coverage and Limitations

Briefly identify:

* Major areas inspected.
* Important areas not examined sufficiently.
* Verification limitations that materially affect confidence in the conclusions.

Do not imply exhaustive coverage if the audit was selective or constrained.

If no findings meet the reporting threshold, state that explicitly without inventing recommendations.

## 5. Final Constraints

* Do not make any changes.
* Do not report assumptions as confirmed defects.
* Do not confuse unfamiliar code with incorrect code.
* Do not recommend broad refactoring when a targeted fix is sufficient.
* Do not introduce complexity without demonstrable net benefit.
* Do not reward hypothetical future-proofing over present requirements.
* Do not repeat findings that share the same root cause.
* Do not confuse audit length or finding count with audit quality.
* Do not recommend work whose expected benefit does not justify its cost.

Final objective: Produce an evidence-based, prioritized assessment that identifies only the changes genuinely worth making. Every recommendation should be defensible, proportionate, and actionable. A clean audit is preferable to a list of manufactured problems.
```

---

[← Appendix D: Evaluating Tools and Skills](04-evaluating-tools-and-skills.md) · [Appendix](README.md) · [Contents](../../README.md#contents) · [Appendix F: PR Review Prompt →](06-pr-review-prompt.md)
