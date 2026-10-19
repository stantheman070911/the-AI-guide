[Contents](../../README.md#contents) › [Appendix](README.md) · **English** | [繁體中文](../../zh-TW/appendix/08-spec-implementation-prompt.md)

# Appendix H: Spec Implementation Prompt

A prompt for building from a product specification. The agent reads the spec, then implements it, and flags the gaps that need a decision from you.

## How to use it

1. Attach the specification or place it in the repository. The [BRIEF template](../part-1-build/02-holy-trinity-plus-one/BRIEF.md) is one format that works; testable acceptance criteria give the agent a clear stopping point.
2. On an existing codebase, run [Appendix G](07-codebase-onboarding-prompt.md) first so the agent knows the code it will change.
3. Paste the block below as the task.
4. Answer the ambiguities it flags. Check the decisions it made on its own against the spec before you accept the work; [Appendix F](06-pr-review-prompt.md) can review the result.

## The prompt

```markdown
Please carefully review the attached product specification to understand the requirements, goals, and intended user experience. Once you have a clear understanding, begin implementation, following the spec closely and making reasonable decisions where details are not explicitly defined.

Prioritize clean, maintainable code, a polished user experience, and functional completeness. Work through the implementation systematically, and flag any critical ambiguities or blockers that require clarification.
```

---

[← Appendix G: Codebase Onboarding Prompt](07-codebase-onboarding-prompt.md) · [Appendix](README.md) · [Contents](../../README.md#contents)
