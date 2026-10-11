# [PROJECT_NAME] — Constitution

_Last updated: [YYYY-MM-DD]_
_Role: the permanent rules every other document and every agent session must obey_

This is the only document a coding agent may not edit on its own. Changes here are
human-approved, deliberate, and rare. Keep this file **short — 50 to 150 lines.** A
constitution nobody can hold in their head stops being read; a map beats an encyclopedia.

## Law I — What each document owns

| Document | Question it answers | Owns | Must not contain |
| --- | --- | --- | --- |
| **BRIEF.md** | What are we building, and why? | Requirements, user-visible behaviour, acceptance criteria, scope decisions | Implementation detail, status, history |
| **PLAN.md** | How are we building it? | Architecture, constraints, the sequence of remaining work, verification rules | A record of what already happened |
| **LOG.md** | What is actually true right now? | Status, verification results, blockers, decisions, the immediate objective | Requirements; instructions for how future work should be built |
| **RUNBOOK.md** | How do we release, activate, and recover? | Operational procedure | Present status — point at LOG.md instead |
| Code + tests + Git | What actually exists? | Machine truth | — |

The four documents **control** the work. They may never override what the repository,
the test suite, and Git history actually demonstrate. When a document and the code
disagree, the code is right and the document is wrong until proven otherwise.

**Routing a change:**

| Kind of change | Action |
| --- | --- |
| Product scope or acceptance criteria | Update BRIEF.md; update PLAN.md only if implementation must change; note the consequence in LOG.md |
| Architecture, implementation, sequencing | Update PLAN.md; update LOG.md if current state changed; leave BRIEF.md untouched unless product behaviour changed |
| Operational procedure | Update RUNBOOK.md |
| Status, blocker, completion, priority | Update LOG.md only |
| Resolved incident with no lasting constraint | Record it outside the four documents, or delete it |

**One fact, one home.** A document may reference a fact another document owns, but must
never keep its own copy. When two documents disagree, the owning document wins and the
other is corrected.

## Law II — Document authority is asymmetric

Do not let an agent freely edit all four documents — that is how an agent quietly
"solves" a hard requirement by rewriting the requirement instead of the code.

| Document | Who may change it |
| --- | --- |
| CONSTITUTION.md | Human only. An agent may propose a change; it may never apply one unasked. |
| BRIEF.md | Human-approved. An agent may propose an amendment when implementation exposes a genuine product ambiguity, but does not merge it unasked. |
| PLAN.md | Human and agent, collaboratively — this is the normal working document during implementation. |
| LOG.md | Mostly agent-maintained, append-only. Correct a factual error if one is found; do not rewrite history. |

## Law III — Retention

A document holds only what is still useful. Every line must answer one of: what must
the product do; how must it be built or verified; what is true right now; what
operational step is next. A sentence that answers none of these belongs in Git history,
an issue tracker, or nowhere.

When state changes, the new statement **replaces** the old one — LOG.md does not
accumulate a diary of superseded status. A lesson learned from a defect may become a
permanent rule if violating it would recreate the defect; keep the rule and the minimum
reason, not the incident narrative.

## Law IV — Engineering rules

Non-negotiable, regardless of what any single session decides in the moment:

- Never mark a task complete solely because an agent says it is complete. Completion
  requires the acceptance criteria in BRIEF.md to be independently verified.
- Every must-have requirement has an observable acceptance criterion before work on it
  starts.
- Never weaken, skip, or remove a failing test to make the suite green. Fix the cause.
- No new dependency without a one-line reason in PLAN.md for why it is required.
- Secrets never enter source code, chat, or committed files.
- Security- or privacy-sensitive changes get explicit human review before merge.
- Work lands in small, independently verifiable increments — not one large
  unreviewable change.
- [ADD_PROJECT_SPECIFIC_RULE — e.g. a design-system adherence rule, a data-retention
  rule, a rule born from a defect this project actually hit]

## Law V — Two risk modes

The same agent, a different risk budget, chosen explicitly and stated in LOG.md:

| Mode | When | What changes |
| --- | --- | --- |
| **Vibe mode** | Local prototype, no real users, no real data, nothing to lose | Wide latitude, fast iteration, light process |
| **Engineering mode** | Real users, real data, payments, credentials, or a production deployment | Acceptance criteria, tests, security review, full diff review, and controlled deployment become mandatory |

Moving from vibe to engineering mode is a one-way door for a given surface — do not
quietly relax back to vibe-mode latitude on code real users depend on.

## Law VI — Amendments

An amendment exists only to reconcile or explicitly change an existing rule. Once
accepted, fold it into the relevant Law above and delete the amendment — a satisfied
amendment must never become a second, permanent, duplicate document.

_Active amendments (delete this line if none):_

- [DATE] — [AMENDMENT TEXT]
