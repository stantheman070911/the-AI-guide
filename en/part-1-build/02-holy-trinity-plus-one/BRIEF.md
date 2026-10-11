# [PROJECT_NAME] — Brief

_Last updated: [YYYY-MM-DD]_
_Role: what must be delivered, and the criteria for calling it done · governed by
[`CONSTITUTION.md`](CONSTITUTION.md)_

This is the most important human-authored document in the system. It answers: **what
does success look like?** It does not describe how the product is built — that is
[`PLAN.md`](PLAN.md) — and it does not describe current status — that is
[`LOG.md`](LOG.md).

A requirement stays in this document even after it ships, because the delivered
product has to go on satisfying it. Nothing here is crossed out on completion; status
lives only in LOG.md.

## 0. Problem, users, outcome

- **Problem:** [what is broken, missing, or costly today]
- **Users:** [who this is for — be specific, not "everyone"]
- **Desired outcome:** [what changes for the user once this ships]

## 1. Product requirements

### Step [N] — [Feature or milestone name]

The product must:

- [Requirement, stated as a testable behaviour, not an implementation]
- [Requirement]

#### Acceptance criteria

Weak requirements ("users can log in") are not precise enough for a coding agent to
verify against. Convert every must-have into observable criteria before implementation
starts:

- [REQ_ID].1 — [Given ... when ... then ...]
- [REQ_ID].2 — [Given ... when ... then ...]
- [REQ_ID].3 — [the negative/error case]

### Step [N+1] — [Next feature or milestone]

[Repeat the shape above. One step per coherent, independently shippable unit of
product behaviour.]

## 2. Should-haves

Wanted, not blocking. Do not let these silently become must-haves during
implementation — if one turns out to be load-bearing, move it up and say so.

- [Should-have]

## 3. Explicitly out of scope

Models embellish. Tell the agent what **not** to build — this list is as load-bearing
as the requirements above it.

- [Thing that looks adjacent to this project but is not part of it]
- [Feature a past version of this brief considered and rejected, with a one-line reason]

## 4. Constraints

Product-level constraints that bound the solution space (not implementation choices —
those belong in PLAN.md unless they are a genuine product requirement, e.g. "must run
offline", "must not use a specific vendor").

- [Constraint]

## 5. Edge cases

Cases the product must handle correctly that are easy to omit from a first pass.

- [Edge case] → [required behaviour]

## 6. Cross-cutting requirements

Requirements that apply across every surface in the product, not just one step.
Typical categories — delete any that don't apply, add ones that do:

### Design and consistency

- [e.g. "reuse the existing design system; no new tokens, colours, or interaction
  patterns without approval"]

### Accessibility and interaction

- [e.g. minimum touch-target size, keyboard navigability, contrast]

### Responsive behaviour

- [e.g. minimum supported viewport width; no horizontal scroll; no clipped content]

### Privacy and security

- [e.g. what must never reach the browser; what must be logged/audited; consent
  requirements; what "gated" content actually means at the server]

## 7. Editorial / review gates

Human review of content, copy, or presentation is **not** a completion gate for the
engineering step it touches unless this brief says otherwise. Track it as an open item
in LOG.md instead of blocking the step's status on it.
