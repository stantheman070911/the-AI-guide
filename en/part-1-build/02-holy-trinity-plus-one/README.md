[Contents](../../../README.md#contents) › [Part 1: Build](../README.md) · **English** | [繁體中文](../../../zh-TW/part-1-build/02-holy-trinity-plus-one/README.md)

# The Holy Trinity + 1

A reusable documentation system for AI-assisted coding projects: three documents that
answer *what*, *how*, and *now* — the "holy trinity" — plus the constitution that
governs them. A fifth, optional document (the runbook) carries operational procedure
once a project has a real deployment.

Copy the templates in this folder into a new project's `docs/` folder, fill in the
placeholders, and delete what doesn't apply.

## The five documents

| Document | Question it answers | Authority |
| --- | --- | --- |
| [`CONSTITUTION.md`](CONSTITUTION.md) | How must this project be built? | Permanent rules |
| [`BRIEF.md`](BRIEF.md) | What are we building and why? | Product truth |
| [`PLAN.md`](PLAN.md) | How are we going to build it? | Execution truth |
| [`LOG.md`](LOG.md) | What is actually happening now? | Operational memory |
| [`RUNBOOK.md`](RUNBOOK.md) | How do we release, activate, and recover it? | Operational procedure |
| Code + tests + Git | What actually exists? | **Machine truth** |

That last row is the one rule everything else defers to. The documents *control* the
work — they tell an agent what to build next and what "done" means — but they must
never be allowed to override what the repository, the tests, and Git history actually
demonstrate. When a document and the code disagree, the code is right.

## Why separate documents and not one giant instruction file

A single sprawling `AGENTS.md`-style file becomes counterproductive at scale: it
consumes context, goes stale, and makes everything look equally important. Splitting
by *question* rather than by *topic* keeps each document short, keeps it obviously
current or obviously stale, and lets a session load only the one it needs.

The split also creates a control property large instruction files don't have:
**a bug can't be "fixed" by quietly rewriting the requirement.** BRIEF.md defines what
must be true; PLAN.md defines how; LOG.md records whether it actually is. As long as
those stay separate, a coding agent can't paper over a failing acceptance test by
loosening the acceptance criteria in the same breath — the two facts live in different
files with different owners. [CONSTITUTION.md Law II](CONSTITUTION.md#law-ii--document-authority-is-asymmetric)
sets who may change each one.

### Make each document sharp, not vague

- **BRIEF.md** is only useful if its must-haves are testable. "Users can log in" gives
  an agent nothing to check against. "An invalid credential returns an error without
  revealing whether the account exists" does. Convert every must-have into acceptance
  criteria before implementation starts — and write down what's explicitly **out of
  scope**, because models embellish, and the brief is the only place that says no.
- **PLAN.md** is not just an architecture description — it's the executable work
  queue. A task without a stopping condition ("done when these acceptance criteria
  pass") invites an agent to keep "improving" it indefinitely. Plan the architecture
  broadly; plan only the next few tasks precisely, and re-plan the next slice once the
  current one lands rather than trying to predict the whole project up front.
- **LOG.md** is what makes a fresh agent session productive after 30 seconds of
  reading, instead of re-deriving state from scratch. Keep it operational: current-state
  sections are rewritten in place, session entries are appended. Don't narrate the journey. Git
  already has the detailed history — LOG.md carries the *semantic* summary that Git
  can't: what's actually verified, what's blocking, what's next.

## Verification

The natural workflow is *intent → implementation → memory*. That's missing a step. It
needs to be *intent → implementation → verification → memory* — otherwise "the agent
says it's done" is the only signal anyone has, and that signal is exactly the one that
fails silently.

Verification lives in tests, CI, and PLAN.md's verification matrix; LOG.md records the
results. A working session loop:

1. Read CONSTITUTION.md, BRIEF.md, PLAN.md, LOG.md, and recent Git state.
2. Confirm the app currently works before changing it.
3. Pick one bounded item from PLAN.md's work queue.
4. Implement it.
5. Run the deterministic gate: build, lint, types, tests.
6. Compare the result against BRIEF.md's acceptance criteria directly — not against a
   vague sense of "should work now."
7. Review the diff for anything unintended.
8. Commit.
9. Remove the finished item from PLAN.md's work queue and append the result to LOG.md.
10. Only start the next item if the tree is clean.

## The completion trap, and how to close it

The agent that builds a feature is not a reliable judge of whether the feature is
finished — it's the same model that just convinced itself the current implementation
was the right one. Don't ask "have we finished everything?" Ask instead:

> Assume the implementation is incomplete. Compare each acceptance criterion in
> BRIEF.md against the repository and provide evidence that it's satisfied. Any
> criterion without evidence is incomplete.

Run that as a separate pass after each milestone, before declaring it done. Gaps become
new PLAN.md items; repeat until none turn up.

## Using this folder

1. Copy `CONSTITUTION.md`, `BRIEF.md`, `PLAN.md`, `LOG.md`, and — once there's a real
   deployment — `RUNBOOK.md` into the new project's `docs/`.
2. Fill in Law IV/V of `CONSTITUTION.md` with this project's actual non-negotiables,
   then treat the rest of the constitution as done — it's the same governance
   structure for every project.
3. Write `BRIEF.md` first, with testable acceptance criteria and an explicit
   out-of-scope list.
4. Let `PLAN.md`'s work queue grow one bounded slice at a time, not all at once.
5. Keep `LOG.md` current every session.
6. Point the project's `AGENTS.md` or `CLAUDE.md` at these files, so every session
   reads them first ([Working with Coding Agents](../03-working-with-coding-agents.md#context-engineering)).

---

[← Stack Decision](../01-stack-decision.md) · [Part 1: Build](../README.md) · [Contents](../../../README.md#contents) · [Working with Coding Agents →](../03-working-with-coding-agents.md)
