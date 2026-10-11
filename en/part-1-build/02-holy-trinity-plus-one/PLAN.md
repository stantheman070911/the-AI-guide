# [PROJECT_NAME] — Implementation Plan

_Last updated: [YYYY-MM-DD]_
_Role: how the approved brief is built and verified · governed by
[`CONSTITUTION.md`](CONSTITUTION.md)_

This is the **executable work queue**, not just an architecture description. Plan the
architecture broadly; plan the next few tasks precisely. Do not try to predict every
implementation detail months ahead — re-plan the next slice once the current one lands.

## 1. Architecture

| Concern | Selected implementation |
| --- | --- |
| Application framework | [choice] |
| Hosting | [choice] |
| Database / auth | [choice] |
| Third-party services | [choice] |
| Design system | [choice] |
| Linting / type checking | [choice] |
| CI | [choice] |

Project identifiers, credentials, and provisioning status are configuration facts —
they live in [`LOG.md`](LOG.md) → Configuration state, not here.

### Ownership boundaries

Which directory or module owns what, so a change lands in one predictable place.

| Location | Owns |
| --- | --- |
| [path] | [what it owns] |

## 2. Engineering constraints

Rules that bind implementation. State the rule and just enough reason that nobody
undoes it by accident. Group by concern — module boundaries, security, a particular
subsystem's invariants — whatever categories this project actually needs.

### [Category, e.g. "Module boundaries"]

- **[Rule.]** [One-line reason.]

### Security

- [Rule about what must never be client-reachable, what needs a grant vs. a policy,
  how secrets are pseudonymised, etc.]

## 3. Implementation method, by step

One subsection per BRIEF.md step that needs more than the architecture table to
implement correctly — flows, data model decisions, sequencing within the step. Skip a
step here if the architecture section above already says everything needed; restating
it is history, not plan.

### Step [N] — [name]

[Flow / data model / sequencing specific to this step.]

## 4. Work queue

The plan's second level: bounded, independently verifiable tasks. A task without a
verification step and a stopping condition invites an agent to "keep improving" it
indefinitely.

```
[P-ID] — [Task title]

Requirement:      BRIEF [REQ_ID]
Status:           [not started | in progress | blocked | done — done items LEAVE this
                   list; status lives in LOG.md, not here]
Depends on:       [P-ID or none]
Files likely affected: [path/*]
Implementation:   [one or two lines — what changes]
Verification:     [the specific test(s) or check(s) that prove it]
Done when:        [the exact acceptance criteria from BRIEF.md that must pass]
```

Keep this list to the next few bounded slices, not the whole project. A completed
task is removed from this queue, not crossed out and kept.

## 5. Verification matrix

| Area | Required verification |
| --- | --- |
| [Step / area] | [what must be checked, and how] |

Every completed slice must pass, before it may be called complete:

```bash
[the project's actual gate command — install, typecheck, lint, test, build]
```

### Rules about what counts as evidence

Add a rule here only after a check has actually passed while testing nothing — that is
what earns a permanent rule. Starter set, keep what applies:

- A route is not verified until it has been requested over HTTP; a green build proves
  generation, not reachability.
- Read a command's exit status, not the tail of its output.
- A width/viewport claim is measured in a real narrow-viewport tool, never a resized
  desktop browser window.
- A verifier that has never been observed to fail is not evidence — break the
  condition once and confirm the check catches it.
- An empty or trivial response can pass a check vacuously — assert size/shape, not
  just absence.

## 6. Remaining sequence

The approved order of what's left. Sequencing only — whether an item has actually
happened, and what currently blocks it, belongs in LOG.md.

1. [Next priority]
2. [Then this]

An item leaves this list when it lands. This is a priority order, not a schedule.

## 7. Brief → implementation traceability

So every requirement's coverage can be checked without re-reading the brief.

| Brief requirement | Implementation | Verification |
| --- | --- | --- |
| [REQ_ID] | [§ in this file] | [row in the matrix above] |
