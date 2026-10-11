# [PROJECT_NAME] — Development Log

_Last updated: [YYYY-MM-DD]_
_Role: what is verified true right now · governed by [`CONSTITUTION.md`](CONSTITUTION.md)_

This document is what makes a brand-new agent session productive after 30 seconds of
reading. It is **append-only and operational** — not a diary. Replace a stale line
with the new true statement; do not narrate the journey that got there.

Bad entry (a diary):

> Worked on login today. Had some problems but eventually got it working.

Good entry (evidence):

> 2026-08-22 / Session 14
> Completed: P-010, P-011
> Verified: auth integration suite 14/14 passing
> Changed decision: switched token storage from plaintext to SHA-256 hashes; PLAN §2
> updated
> Known issue: P-014 callback intermittently fails locally
> Current blocker: [external dependency] unavailable
> Next: P-012
> Commit: [sha]

## Deployed state

[Which branch is deployed, where, and whether it currently matches `main`/trunk.
What the deployment does and does not yet carry — call out anything provisioned but
not yet exercised end to end.]

## Verification results

| Check | Verified result |
| --- | --- |
| [e.g. "Local gate"] | [what passed, when, against what] |

Only put a result here once it has actually been run. A row that says what *should*
pass is a plan, not a log.

## Configuration state

Identifiers and provisioning facts other documents reference. Read here, not copied
elsewhere.

| Value | Confirmed state |
| --- | --- |
| [service / credential / env var] | [what's confirmed, and how it was confirmed] |

## Step status

| Step (from BRIEF.md) | Status | Open condition |
| --- | --- | --- |
| [Step N] | [Complete / Partially complete / Not started] | [what's still open, or "None"] |

## Open items

Numbered, each with what's blocking it and who/what it's waiting on. State clearly
when an item is deferred rather than dropped — a hold must not quietly become an
acceptance.

1. **[Item title.]** [Current state and what's blocking it.]

## Deferred

Things intentionally not being done now, and the condition that reopens them.

- [Deferred thing] — waits on [condition]

## Immediate objective

The one or two things a session picking this up next should work on, and anything
that must NOT happen while they're open (e.g. "no discretionary refactor while a
production activation window is open").
