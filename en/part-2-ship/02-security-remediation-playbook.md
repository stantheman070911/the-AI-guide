[Contents](../../README.md#contents) › [Part 2: Ship](README.md) · **English** | [繁體中文](../../zh-TW/part-2-ship/02-security-remediation-playbook.md)

# Security Remediation Playbook

Fixes for the highest-risk items in the [Production Readiness Checklist](01-production-readiness-checklist.md), grouped by the [OWASP Top 10:2025](https://top10.owasp.org/2025/0x00_2025-Introduction/). Each entry says how to find the problem, fix it, and prove the fix works. Risks specific to LLM features and coding agents are in [Securing AI Features and Coding Agents](03-securing-ai-features-and-agents.md).

Severity: 🚨 Critical (fix before shipping) · 🔴 High (fix before shipping if the app has the affected feature) · 🟠 Medium (schedule it). 🚨 and 🔴 items are P0 on the checklist's scale.

Test only systems you own or are authorized to test.

> Last verified: 2026-10-11.

## Why this matters more with AI-written code

In Veracode's 2025 vendor research, testing more than 100 models on 80 security-sensitive tasks, 45% of generated code samples contained an OWASP Top 10 class of vulnerability, and larger models did no better ([press release](https://www.veracode.com/press-release/ai-generated-code-poses-major-security-risks-in-nearly-half-of-all-development-tasks-veracode-research-reveals/)). The agent will write the happy path. Access control, input handling, and failure behavior are where you review.

## A01 Broken access control

### 1. Client-side authentication — 🚨 Critical

A login check in browser JavaScript can be read and skipped.

* **Detect:** Search frontend code for password comparisons, role checks, and token validation.
* **Fix:** Verify credentials and decide roles on the server. The client receives only a session cookie or token.
* **Verify:** Call every protected API directly, without the UI, as an anonymous user. Each call fails.

### 2. Missing object-level authorization (IDOR) — 🚨 Critical

Logged in does not mean allowed. Any endpoint that takes an ID must check that the caller may access that object.

* **Detect:** List every route that accepts `userId`, `orderId`, `documentId`, or similar. Look for queries that filter by the ID alone.
* **Fix:** Scope every query to the authenticated user or tenant (`WHERE id = $1 AND owner_id = $2`). Return `404` or `403` otherwise.
* **Verify:** With two test accounts, request account B's objects while logged in as A. Every request fails, for reads and writes.

### 3. Missing function-level authorization — 🚨 Critical

Admin and write operations reachable by ordinary users.

* **Detect:** List all `POST`/`PUT`/`PATCH`/`DELETE` routes and admin pages. Note which check the role on the server.
* **Fix:** Enforce role and ownership checks in server code for each operation. A hidden button is not a permission check.
* **Verify:** Replay admin requests with a regular user's session. All return `403`.

### 4. Tenant isolation and database policies — 🚨 Critical

The most common serious flaw in AI-built apps. Supabase and Firebase expose the database to the browser by design; the key in the client is public, and only row-level policies stand between it and your data. In CVE-2025-48757, a researcher's scan of 1,645 apps from Lovable's showcase found 170 with tables readable or writable by anyone ([NVD](https://nvd.nist.gov/vuln/detail/CVE-2025-48757)). Lovable disputes the CVE, holding that each app's owner is responsible for its data.

* **Detect:** Run the Supabase Security Advisor (`supabase db advisors`, or the dashboard). Treat every security lint at level ERROR (among them `rls_disabled_in_public`, `security_definer_view`, `rls_references_user_metadata`, `auth_users_exposed`, `sensitive_columns_exposed`, `insecure_queue_exposed_in_api`) and `permissive_rls_policy` (`USING (true)`) as release blockers ([lint list](https://supabase.com/docs/guides/observability/advisors)). For Firebase, review Security Rules for `allow read, write: if true`.
* **Fix:** Enable RLS on every exposed table. Write policies against `auth.uid()` or a tenant ID from a trusted source, never from user-editable metadata. Keep the secret key (`sb_secret_…`, or the legacy `service_role` key) on the server only. Supabase is deprecating the legacy `anon` and `service_role` keys by the end of 2026; new projects use publishable and secret keys.
* **Verify:** Using only the public URL and the publishable (or legacy anon) key, try to read and write each table with no session, then with account A against account B's rows. Add these as automated tests so a later migration cannot silently reopen them.

### 5. Authentication bypass paths — 🚨 Critical

Routes that skip authentication, or a single check that can be skipped. In CVE-2025-29927, a crafted `x-middleware-subrequest` header bypassed Next.js middleware entirely on self-hosted apps; apps that enforced auth only in middleware were exposed ([OSV](https://osv.dev/vulnerability/CVE-2025-29927)).

* **Detect:** Build a route inventory and mark which routes require auth. Test path variants: trailing slashes, encoding, case.
* **Fix:** Check authorization next to the data access (route handler, server action, or database policy), not only in middleware. Keep the framework patched.
* **Verify:** Request every protected route without a session, including API routes and server actions. All fail.

### 6. Server-side request forgery (SSRF) — 🔴 High

Any feature that fetches a URL the user controls: link previews, image imports, webhooks, and AI tools that browse. An attacker points it at `169.254.169.254` or an internal service. OWASP 2025 folds SSRF into broken access control.

* **Detect:** Search for server-side `fetch`, `axios`, `requests`, or `curl` calls that take user input.
* **Fix:** Allowlist destination hosts where possible. Otherwise resolve DNS, reject private, loopback, and link-local ranges, and re-check after every redirect. Run fetchers without credentials to internal systems.
* **Verify:** Submit `http://127.0.0.1`, `http://169.254.169.254/`, a hostname that resolves to a private IP, and a URL that redirects to one. All are refused.

## A02 Security misconfiguration

### 7. Security headers — 🟠 Medium

* **Fix:** Set globally: `Content-Security-Policy` (start with `default-src 'self'`, avoid `unsafe-inline` and `unsafe-eval`), `frame-ancestors` in the CSP to control framing (keep `X-Frame-Options` only for old browsers), `Strict-Transport-Security`, `X-Content-Type-Options: nosniff`, `Referrer-Policy`, and `Permissions-Policy`. Do not add `X-XSS-Protection`; it is obsolete. Ship the CSP as `Content-Security-Policy-Report-Only` first, then enforce.
* **Verify:** Inspect production response headers (`curl -I`), not local dev.

### 8. Exposed environments and cloud misconfiguration — 🔴 High

Preview and staging deployments with production data, public storage buckets, debug endpoints, default credentials, exposed source maps, and CORS set to `*` on authenticated APIs.

* **Detect:** List every deployment URL and storage bucket. Check bucket and storage policies. Search for `Access-Control-Allow-Origin: *` together with credentials.
* **Fix:** Protect previews (platform deployment protection or auth), give them separate credentials and data, make buckets private by default, and allowlist CORS origins.
* **Verify:** From a logged-out browser, open preview URLs, bucket object URLs, and `/.map` files. None expose private data.

## A03 Software supply chain failures

### 9. Hallucinated and malicious packages — 🔴 High

Models invent package names, and attackers register them ("slopsquatting"). Across 576,000 generated samples from 16 models, hallucinated packages averaged at least 5.2% for commercial models and 21.7% for open-source ones, with 205,474 unique invented names ([USENIX Security 2025](https://www.usenix.org/conference/usenixsecurity25/presentation/spracklen)).

* **Detect:** Review every new dependency in a diff. Check that it exists under that exact name, its age, maintainers, and download history.
* **Fix:** Add dependencies yourself, not through the agent's unreviewed install commands. Use a release-age cooldown so brand-new versions are not installed automatically (`min-release-age` in npm, in days; `minimumReleaseAge` in pnpm; `npmMinimalAgeGate` in Yarn).
* **Verify:** CI fails when the lockfile changes without a matching manifest change, and installs use `npm ci` or the equivalent frozen-lockfile mode.

### 10. Vulnerable dependencies — 🔴 High

* **Detect:** Run the ecosystem's audit (`npm audit`, `pip-audit`, `cargo audit`, `govulncheck`) in CI.
* **Fix:** Patch critical and high findings first. Enable Dependabot or Renovate, with a cooldown, so updates arrive as reviewable pull requests.
* **Verify:** The audit step runs on every pull request and blocks on critical findings.

### 11. CI/CD and publishing credentials — 🔴 High

Two 2025 incidents show the pattern. In the tj-actions/changed-files compromise (CVE-2025-30066), attackers moved existing version tags to a malicious commit; workflows pinned to a commit SHA were unaffected ([NVD](https://nvd.nist.gov/vuln/detail/CVE-2025-30066)). The Shai-Hulud worm stole npm and cloud tokens from developer machines and used them to publish infected versions of more than 500 packages ([CISA](https://www.cisa.gov/news-events/alerts/2025/09/23/widespread-supply-chain-compromise-impacting-npm-ecosystem)).

* **Fix:** Pin third-party actions to a full commit SHA, which GitHub calls "the only way to use an action as an immutable release" ([GitHub](https://docs.github.com/en/actions/reference/security/secure-use)). Set `GITHUB_TOKEN` to read-only by default and grant more per job. Avoid `pull_request_target` with untrusted code. Use OIDC instead of long-lived cloud keys. Publish packages through trusted publishing, not personal tokens. Turn on secret scanning with push protection.
* **Verify:** A script or linter flags any `uses:` line not pinned to a SHA. Workflow files declare `permissions:` explicitly.

## Secrets and keys

### 12. Hard-coded and leaked credentials — 🚨 Critical

* **Detect:** Scan the full Git history, not just the current tree, with `gitleaks` or `trufflehog`. Check build logs and CI output.
* **Fix:** Rotate anything found; deleting the commit does not revoke the key. Move secrets to environment variables or a secret manager, commit a `.env.example`, and add `.env*` to `.gitignore`.
* **Verify:** The scanner runs in CI and as a pre-commit hook, and passes on the full history.

### 13. Secret keys in client code — 🚨 Critical

Anything in the browser bundle is public. Know which keys are designed to be public (Supabase publishable key `sb_publishable_…` or legacy `anon` key, Stripe publishable key `pk_…`) and which are not (Supabase secret key `sb_secret_…` or legacy `service_role` key, Stripe `sk_…` and restricted `rk_…` keys, webhook secrets `whsec_…`, any LLM provider key).

* **Detect:** Search the built bundle, not only the source, for full secret prefixes: `sb_secret_`, `sk_live_`, `sk_test_`, `rk_live_`, `rk_test_`, `whsec_`, and the pattern `\bsk-[A-Za-z0-9_-]{20,}` for OpenAI- and Anthropic-style keys. A bare `sk-` also matches ordinary code such as `mask-`. Legacy Supabase keys are JWTs: decode each `eyJ…` string and fail if its `role` claim is `service_role`. Check which environment variables carry a public prefix (`NEXT_PUBLIC_`, `VITE_`).
* **Fix:** Call third-party APIs from a server route that holds the key, authenticates the user, rate-limits, and returns only what the client needs.
* **Verify:** Re-run both checks on the production build output: no secret prefix appears, and no decoded JWT has `role: service_role`.

## A04 Cryptographic failures

### 14. Password storage and policy — 🚨 Critical

Prefer a managed auth provider. If you store passwords yourself:

* **Fix:** Hash with Argon2id (minimum 19 MiB memory, 2 iterations, parallelism 1). Use scrypt if Argon2id is unavailable. bcrypt is for legacy systems only: work factor 10 or more, and it ignores input beyond 72 bytes ([OWASP](https://cheatsheetseries.owasp.org/cheatsheets/Password_Storage_Cheat_Sheet.html)). Re-hash legacy hashes on next login.
* **Policy:** NIST SP 800-63B-4 requires at least 15 characters for password-only login (8 with MFA), screening against breached and common passwords, and forbids composition rules and forced periodic rotation ([NIST](https://pages.nist.gov/800-63-4/sp800-63b.html)).
* **Verify:** Every stored password hash is Argon2id, scrypt, bcrypt, or PBKDF2. None is plaintext or a fast hash (MD5, SHA-1, SHA-256), salted or not.

### 15. Sensitive data in URLs, logs, and errors — 🟠 Medium

Tokens in query strings end up in browser history and CDN logs. Full request dumps put credentials in logs for months.

* **Fix:** Send tokens in headers or POST bodies. Redact credential and personal-data fields in logs. Return generic error messages to users.
* **Verify:** Search a day of production logs for `password`, `token`, `authorization`, and key prefixes.

## A05 Injection

### 16. SQL injection — 🚨 Critical

* **Detect:** Search for string-built SQL and ORM escape hatches (`$queryRawUnsafe`, `sequelize.literal`, raw `execute` with template strings), including SQL inside database functions.
* **Fix:** Use parameterized queries or the ORM's safe builder. Run the app's database user with least privilege.
* **Verify:** Unit-test each dynamic query with `' OR 1=1 --` and quote characters. `sqlmap` can confirm against a staging copy.

### 17. Cross-site scripting (XSS) — 🔴 High

Includes model output rendered as HTML or Markdown.

* **Detect:** Search for `dangerouslySetInnerHTML`, `innerHTML`, `v-html`, `document.write`, and Markdown renderers with raw HTML enabled.
* **Fix:** Render text through the framework's escaping. When HTML is unavoidable, sanitize with DOMPurify. Enforce a CSP (item 7).
* **Verify:** Store `<img src=x onerror=alert(1)>` in every user-editable field and in a prompt that the model will echo. Nothing executes.

### 18. Command injection — 🚨 Critical

* **Detect:** Search for `exec`, `system`, `spawn` with `shell: true`, `subprocess` with `shell=True`, and `os.system`, and trace whether user or model input reaches them.
* **Fix:** Use a library instead of a shell. If you must spawn a process, pass an argument array with the shell disabled.
* **Verify:** Feed `; id` and `$(id)` through each path. Nothing executes.

## A06 Insecure design

### 19. Missing rate limits and spend controls — 🔴 High

Brute force, scraping, and AI endpoints that turn a small bill into a large one.

* **Fix:** Rate-limit by IP and account with a shared store (Redis, or the platform's built-in limiter): about 5 login attempts per 15 minutes, 3–5 password resets per hour, and per-user quotas on AI and other expensive endpoints. Return `429` with `Retry-After`. Then cap spending where the provider allows: Vercel's on-demand budget does not stop usage unless **Pause Production Deployments** is enabled, and checks run every few minutes ([Vercel](https://vercel.com/docs/spend-management)). Pausing stops production deployments only; AI Gateway and v0 usage billed to the team continue, so cap model spend separately. Supabase Pro has a spend cap on by default ([pricing](https://supabase.com/pricing)). Set monthly limits on every LLM provider key.
* **Verify:** Script 50 rapid login attempts and 50 AI requests from one account. Both get throttled. Confirm each provider's alert reaches a person.

### 20. Payments and webhooks trusted without verification — 🚨 Critical

* **Fix:** Grant paid access only from verified server-side events. Verify webhook signatures (for Stripe, with the endpoint's signing secret on the raw body), reject stale timestamps, and process each event ID once.
* **Verify:** Send a forged webhook with no or a wrong signature: rejected. Replay a valid one: no duplicate effect. Change the price or plan in a client request: ignored.

## A07 Authentication failures

### 21. Session handling — 🔴 High

* **Fix:** Use the framework's or provider's sessions. Cookies are `HttpOnly`, `Secure`, and `SameSite=Lax` or `Strict`. Rotate the session ID at login and privilege change, set idle and absolute expiry, and destroy sessions server-side at logout. Keep tokens out of `localStorage`. Chrome's Device Bound Session Credentials, available on Windows since Chrome 146, bind cookies to a hardware key and are worth supporting once your auth provider does ([Google](https://blog.google/security/protecting-cookies-with-device-bound-session-credentials/)).
* **Verify:** After logout, the old cookie is rejected by the API.

### 22. Cross-site request forgery (CSRF) — 🔴 High

Applies to cookie-authenticated, state-changing requests.

* **Fix:** Use the framework's built-in protection first. Otherwise use synchronizer tokens (stateful apps) or HMAC-signed double-submit cookies (stateless apps). For modern browsers, rejecting unsafe cross-site requests by `Sec-Fetch-Site`, with an `Origin` check as fallback, is also accepted. `SameSite` cookies are defense in depth, not a complete defense ([OWASP](https://cheatsheetseries.owasp.org/cheatsheets/Cross-Site_Request_Forgery_Prevention_Cheat_Sheet.html)). The npm package `csurf` is deprecated; do not add it.
* **Verify:** Submit each state-changing form from another origin. All are rejected.

### 23. Password reset and account recovery — 🔴 High

* **Fix:** Single-use, short-lived, random reset tokens; the same response whether or not the account exists; sessions invalidated after a reset; rate limits (item 19).
* **Verify:** A used or expired token fails. Reset responses for real and fake emails are identical.

## A08 Software or data integrity failures

### 24. Insecure deserialization — 🔴 High

* **Detect:** Search for `pickle.loads`, `marshal.loads`, `yaml.load`, Java `ObjectInputStream`, and PHP `unserialize()` on untrusted input.
* **Fix:** Use JSON and `yaml.safe_load()`. Validate input against a schema (Zod, Pydantic, JSON Schema) before use.
* **Verify:** Unit tests feed malformed and oversized payloads; they are rejected before business logic runs.

## A09 Security logging and alerting failures

### 25. Nothing alerts when something goes wrong — 🟠 Medium

* **Fix:** Log authentication events, permission denials, admin actions, and payment events with user and request IDs, without secrets. Alert a person on spikes in failed logins, `403`s, and spending.
* **Verify:** Trigger each alert once in staging and confirm someone receives it.

## A10 Mishandling of exceptional conditions

### 26. Failing open — 🔴 High

Code that grants access when a check throws: a `try/catch` that returns `true`, a missing role treated as admin, a timed-out policy service that is skipped.

* **Fix:** Default to deny. Treat errors in auth, payment, and policy checks as failures.
* **Verify:** Make the auth provider, database, or policy service unavailable in a test. Protected actions are refused.

## Advanced hardening

Worth adding once the items above are done:

* Constant-time comparison for secrets and signatures.
* Query depth and complexity limits on GraphQL APIs.
* IP allowlisting or SSO in front of admin dashboards.
* CAA DNS records so only your chosen certificate authority can issue certificates for the domain.
* Separate, hardware-key MFA on the domain registrar, DNS, and cloud root accounts.
* Canary tokens in places an intruder would look.

---

[← Production Readiness Checklist](01-production-readiness-checklist.md) · [Part 2: Ship](README.md) · [Contents](../../README.md#contents) · [Securing AI Features and Coding Agents →](03-securing-ai-features-and-agents.md)
