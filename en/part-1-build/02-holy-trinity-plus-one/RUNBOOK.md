# [PROJECT_NAME] — Operations Runbook

_Role: the operational procedure for releasing, activating, and recovering the
deployed system · governed by [`CONSTITUTION.md`](CONSTITUTION.md)_

This document states the **procedure**, not the current status — for what's actually
been done, see [`LOG.md`](LOG.md).

## Secret handling

Applies to every step below.

- Generate each secret independently — never reuse one value across two purposes.
- A length check is not a strength check; use a real generator (e.g. `openssl rand
  -base64 32`).
- Use different values in each environment. A leaked local secret should cost
  nothing.
- Never place a secret in chat, a commit, shell history, or this document. Confirm
  presence by variable name only.

## Routine release

Every deployment that changes schema or application code.

1. Review the migration/change dry-run, then secure a rollback before applying
   anything.
   - A change that only **adds** (a table, a route, an index) may proceed against a
     rollback recorded in advance.
   - A change that **alters or destroys existing data** must not be applied without a
     real, restorable backup — a row count is not a copy of the rows.
2. Capture a baseline (advisor output, health check, whatever this stack provides)
   before applying anything.
3. Apply the change from an approved release context.
4. Regenerate any generated artifacts (types, schema snapshots) and require a clean
   diff.
5. Deploy, then compare the post-deploy baseline against the pre-deploy one — a new
   warning or error is fixed or explicitly accepted in LOG.md, not ignored.
6. Verify the core critical paths still work end to end (auth, the primary write
   path, whatever this product cannot ship broken).

## Backup

1. [Dump command(s) for schema, data, and any platform-owned data (auth, storage)
   the primary dump excludes.]
2. Validate before trusting: restore into a disposable environment, apply under a
   fail-fast flag, and compare row counts and a content hash against a fresh
   production read. Then break one table on purpose and confirm the check reports it.
3. Encrypt before the file leaves the machine. Decrypt-test every archive against its
   plaintext source before deleting the plaintext.
4. An upload is not a transfer — download the archive back and hash-compare before
   deleting any earlier copy.

## Initial production activation

One-time steps, in order, for the life of the project:

1. [Data/content migration into production, with a dry-run and a verification pass.]
2. [Any provider webhook/endpoint that must exist before its secret can be
   configured.]
3. [Configure deployment variables per the table below, under Secret handling.]
4. [Provision privileged accounts/allowlists, never through a form that creates a
   second, unintended access path.]
5. [Configure the auth/email/notification provider.]
6. Deploy with any dangerous feature flag **off**. Verify the core paths.
7. If a feature needs a live verification window (e.g. sending real email), open it
   deliberately, run the matrix, then **close it again** — state in LOG.md that it was
   closed and what (if anything) it left behind.
8. Enable monitoring and backups; observe any report-only security policy before
   enforcing it.

## Variables

| Variable | Source | Same value in every environment? |
| --- | --- | --- |
| [name] | [where it comes from] | [yes/no] |

## Configuration probes

Prove a secret is *configured* without ever printing it — an unauthenticated request
to a secret-gated endpoint should fail in a specific, known way.

| Probe | Configured (fail-closed) response | Misconfiguration signal |
| --- | --- | --- |
| [e.g. cron endpoint without auth header] | [e.g. 401] | [e.g. 500 = secret missing] |

## Troubleshooting

### [Common failure — e.g. "OTP/email doesn't arrive"]

[Where to actually look — which log, which layer — and the specific error strings
that mean what.]

## Recovery

- [What a stuck/stale job looks like, and how it self-recovers or gets manually
  requeued.]
- [What's a terminal state vs. retryable, and what must never be manually overridden.]

## Secret rotation

**A variable change does not reach a running deployment until redeploy.** State this
explicitly for every secret below, because forgetting it reads as a failed rotation
when the rotation simply never took effect.

- `[SECRET_NAME]`: [what breaks/invalidates when rotated, and what plan is needed
  before rotating it].

## Monitoring

- Alert on: [the failure modes that actually matter for this product].
- Verify backup **restore** procedures periodically — a backup that has never been
  restored is not recovery evidence.
