[Contents](../../README.md#contents) › [Part 2: Ship](README.md) · **English** | [繁體中文](../../zh-TW/part-2-ship/02-security-remediation-playbook.md)

# Security Remediation Playbook

Detailed, actionable guidance for the highest-risk items in the [Production Readiness Checklist](01-production-readiness-checklist.md). Each entry lists the risk, the fix approach, and a verification checklist.

Severity legend: 🚨 Critical (fix before shipping) · 🔴 High (fix soon after) · 🟠 Medium (schedule it). These map onto the checklist's P0/P1/P2 scale — 🚨 and 🔴 items here are P0.

## Authentication & Authorization

### 1. Client-Side Authentication — 🚨 Critical

If the login check runs in browser JavaScript, any user can read the source and bypass it. Authentication logic belongs on the server; the client should receive only a session token after the server verifies credentials.

**Fix:**

* Audit the codebase for auth/authorization logic running client-side (password comparisons, role checks, token validation)
* Move all credential validation and role decisions to server-side endpoints
* Client submits credentials only, and receives a verified session token (JWT or secure cookie) in return

**Checklist:**

* \[ \] No password comparisons in frontend JS
* \[ \] No role/permission checks in browser code
* \[ \] Auth logic moved to server/backend

### 2. Missing Authorization Checks (IDOR) — 🚨 Critical

Being logged in doesn't mean access to everything. Every endpoint that returns data must verify the requester owns or is permitted to access that specific resource.

**Fix:**

* Audit every endpoint accepting an identifier (`userId`, `documentId`, `orderId`, etc.) for a server-side ownership/role check
* Never assume authentication implies authorization
* Reject unauthorized access with `403`; scope all ID-based queries to the authenticated user

**Checklist:**

* \[ \] Every resource endpoint checks ownership
* \[ \] IDs are not guessable/sequential without access control
* \[ \] Server validates the user–resource relationship on every request

### 3. Broken Access Controls — 🚨 Critical

Authenticated users should only be able to modify or delete resources they own. Without this, any logged-in attacker can corrupt another user's data.

**Fix:**

* Audit all write/update/delete routes (`POST`/`PUT`/`PATCH`/`DELETE`) for explicit server-side ownership checks
* Enforce `resource.ownerId === user.id`, plus role-based checks for admin actions
* Reject unauthorized operations with `403`

**Checklist:**

* \[ \] Delete/edit operations validate ownership server-side
* \[ \] Admin-only routes are protected by role checks
* \[ \] No resource can be modified by an unauthorized user

### 4. Weak Session Handling — 🔴 High

Sessions must be cryptographically secure, expire properly, and be invalidated on logout.

**Fix:**

* Verify session tokens use a cryptographically secure random source with sufficient entropy
* Configure idle and absolute expiration; destroy sessions server-side on logout
* Enforce HTTPS-only transmission with `Secure`/`HttpOnly`/`SameSite` cookies; regenerate session IDs after login or privilege changes

**Checklist:**

* \[ \] Sessions use cryptographically random tokens
* \[ \] Session expiry is configured
* \[ \] Logout invalidates the session server-side
* \[ \] Tokens transmitted only over HTTPS

### 5. Authentication Bypass Paths — 🚨 Critical

Routes that skip authentication entirely — often created by accident — let anyone reach protected functionality without logging in.

**Fix:**

* Build a full route inventory and flag routes that should require auth but don't
* Test for bypass vectors: path manipulation, encoded variants, case-sensitivity gaps, middleware misconfiguration
* Apply consistent auth middleware to every protected route; normalize paths before authorization checks

**Checklist:**

* \[ \] Every protected route has auth middleware applied
* \[ \] No accidental public routes to private resources
* \[ \] Auth middleware cannot be bypassed via URL tricks

## Secrets & Keys

### 6. Hard-Coded Credentials — 🚨 Critical

Passwords, database connection strings, and secrets embedded in source code get committed to git and leaked permanently.

**Fix:**

* Scan source, config files, and committed files for credentials, API keys, and high-entropy tokens
* Migrate all secrets to environment variables; rotate anything already exposed
* Add sensitive files to `.gitignore` and generate a `.env.example` with placeholder values

**Checklist:**

* \[ \] No passwords in source code
* \[ \] No connection strings with credentials in code
* \[ \] All secrets loaded from environment variables
* \[ \] `.env` is in `.gitignore`

### 7. Exposed API Keys in Client-Side Code — 🚨 Critical

Any key shipped in the frontend bundle is public — anyone can open DevTools and take it.

**Fix:**

* Scan frontend code for embedded third-party keys (OpenAI, AWS, Stripe, SendGrid, Firebase, etc.)
* Move the secret server-side and add a backend proxy endpoint that calls the external API and returns only what the client needs
* Apply auth/rate limiting on the proxy and filter sensitive fields from the response

**Checklist:**

* \[ \] No API keys in frontend JS or React code
* \[ \] External API calls proxied through backend
* \[ \] Keys only in server-side environment variables

## Injection Vulnerabilities

### 8. SQL Injection (SQLi) — 🚨 Critical

Concatenating user input into SQL queries lets attackers read, modify, or delete the entire database.

**Fix:**

* Audit every query for string concatenation or interpolation of user input
* Replace with parameterized queries/prepared statements, or the ORM's safe query builder
* Apply input validation and least-privilege database accounts

**Checklist:**

* \[ \] All queries use parameterized statements or ORM-safe methods
* \[ \] No string concatenation with user input in SQL
* \[ \] Database user has minimal required permissions

### 9. Cross-Site Scripting (XSS) — 🔴 High

Rendering unescaped user input in HTML lets attackers inject scripts that steal cookies, hijack sessions, or deface the app.

**Fix:**

* Scan for `dangerouslySetInnerHTML`, direct `innerHTML` assignment, `document.write`, or string-built HTML using user input
* Replace with safe rendering (JSX binding, `textContent`) or sanitize with a trusted library (e.g., DOMPurify) when raw HTML is unavoidable
* Add a production Content Security Policy, minimizing `unsafe-inline`/`unsafe-eval`

**Checklist:**

* \[ \] No `dangerouslySetInnerHTML` with unsanitized input
* \[ \] No `innerHTML` with user data
* \[ \] Server-rendered content is escaped
* \[ \] CSP headers configured

### 10. Command Injection — 🚨 Critical

Passing user input to shell commands lets attackers run arbitrary code on the server.

**Fix:**

* Scan for `exec`, `system`, `spawn`, `subprocess`, `os.system`, `popen` calls and trace whether user input reaches them
* Where shell execution is necessary, use array-based arguments (not interpolated strings) and disable shell interpretation
* Where it isn't necessary, replace with a native/library alternative that avoids the shell entirely

**Checklist:**

* \[ \] No user input passed to shell/exec functions
* \[ \] Child processes use argument arrays, not string interpolation
* \[ \] Shell calls replaced with native library alternatives where possible

## Data Storage & Handling

### 11. Insecure Client-Side Storage — 🔴 High

`localStorage` and `sessionStorage` are readable by any JavaScript on the page, including injected scripts — sensitive tokens don't belong there.

**Fix:**

* Scan for `localStorage`/`sessionStorage` usage and classify what's stored (JWTs, session IDs, PII)
* Move auth/session handling to `httpOnly`, `Secure`, `SameSite` cookies set by the server
* Add CSRF protection to match the cookie-based auth flow

**Checklist:**

* \[ \] JWT tokens not stored in `localStorage`
* \[ \] Sensitive data not in `sessionStorage`
* \[ \] Auth tokens use `httpOnly`, `Secure` cookies

### 12. Weak Password Storage — 🚨 Critical

Plain-text passwords or MD5/SHA-1 hashes are trivially cracked. Use bcrypt, Argon2, or scrypt.

**Fix:**

* Audit the registration/login flow for the hashing method in use
* Replace with bcrypt (cost ≥ 12\) or Argon2id, using the library's built-in salting and constant-time comparison
* Add a transparent migration: re-hash with the new algorithm on next successful login for legacy users

**Checklist:**

* \[ \] Passwords hashed with bcrypt (≥12 rounds) or Argon2
* \[ \] No plain text passwords in database
* \[ \] No MD5/SHA-1 password hashing

### 13. Sensitive Data in URLs and Logs — 🟠 Medium

Tokens or passwords in URLs end up in browser history and server/CDN logs; credentials in log statements persist for months.

**Fix:**

* Check for auth tokens, API keys, or PII passed via query strings or URL paths
* Move sensitive data to POST bodies or headers instead of URLs
* Sanitize logs: avoid dumping full request/response objects, redact credential fields, and keep debug logging out of production

**Checklist:**

* \[ \] No tokens or passwords in URL query strings
* \[ \] Log statements sanitize sensitive fields
* \[ \] Error messages don't expose stack traces or internal data to users

## Security Headers & Protections

### 14. Missing Security Headers — 🟠 Medium

HSTS, CSP, X-Frame-Options, and a few others take under an hour to add and close a meaningful number of attack vectors. Most vibe-coded apps ship without any of them.

**Fix:**

* Add HSTS, CSP, X-Frame-Options, X-Content-Type-Options, Referrer-Policy, and Permissions-Policy globally via middleware
* Write a strict, app-specific CSP (`default-src 'self'`, explicit `script-src`/`style-src`/`img-src`/`connect-src`/`font-src`, no `unsafe-inline`/`unsafe-eval` unless unavoidable)
* Enforce (not report-only) once verified not to break functionality

**Checklist:**

* \[ \] HSTS header configured
* \[ \] CSP header configured
* \[ \] X-Frame-Options set
* \[ \] X-Content-Type-Options set
* \[ \] Referrer-Policy set

### 15. No CSRF Protection — 🔴 High

Without CSRF protection, a malicious website can trigger authenticated requests to the app on a logged-in user's behalf.

**Fix:**

* Add a framework-appropriate CSRF library (`csurf`, Django's `CsrfViewMiddleware`, Flask-WTF, Spring Security CSRF) to all `POST`/`PUT`/`PATCH`/`DELETE` routes
* Inject tokens into server-rendered forms; send via header for AJAX/fetch requests
* Set `SameSite=Strict`/`Lax` and `Secure` on session cookies; reject requests with missing/invalid tokens (`403`)

**Checklist:**

* \[ \] CSRF tokens on all state-changing forms
* \[ \] CSRF tokens validated server-side
* \[ \] `SameSite=Strict` or `Lax` on session cookies

### 16. Missing Rate Limiting — 🔴 High

Without rate limiting, attackers can brute-force passwords, enumerate users, or abuse the API indefinitely.

**Fix:**

* Add a rate-limiting library backed by a shared store (e.g., Redis) so limits hold across instances
* Tighten limits on auth (\~5/15 min), password reset (\~3–5/hour), and registration endpoints; apply a baseline limit to public APIs
* Return `429` with a `Retry-After` header; key limits by IP and, where relevant, by account

**Checklist:**

* \[ \] Login endpoint rate limited
* \[ \] Password reset rate limited
* \[ \] Public API endpoints rate limited
* \[ \] Proper 429 responses returned

## Dependencies & Supply Chain

### 17. Hallucinated Packages — 🔴 High

AI models sometimes suggest package names that don't exist. Attackers register those names with malicious code, and the install picks it up.

**Fix:**

* Verify every dependency in the manifest exists on the official registry under the exact expected name
* Check maintainer legitimacy, release activity, and download counts for anything unfamiliar
* Flag typosquatting risks and low-usage packages for manual review before they ship

**Checklist:**

* \[ \] All packages verified on official registries
* \[ \] Package names double-checked for typosquatting
* \[ \] No AI-suggested packages installed without verification

### 18. Outdated Libraries with Known CVEs — 🔴 High

Outdated dependencies are the most common entry point for real-world attacks.

**Fix:**

* Run the stack's audit tool (`npm audit`, `pip-audit`, `cargo audit`, `govulncheck`) and triage by severity
* Upgrade critical/high findings first; note breaking changes that need migration
* Turn on automated dependency alerts (Dependabot or Renovate) so this doesn't silently drift again

**Checklist:**

* \[ \] `npm audit` / `pip-audit` run with no critical/high CVEs
* \[ \] Automated dependency update alerts configured
* \[ \] Lock files committed and up to date

### 19. Insecure Deserialization — 🔴 High

Deserializing untrusted data (especially Python pickle, Java serialization) can execute arbitrary code.

**Fix:**

* Scan for `pickle.loads`, `marshal.loads`, Java `ObjectInputStream.readObject`, PHP `unserialize()`, and unsafe YAML loaders on untrusted input
* Replace with safe formats (strict JSON) and `yaml.safe_load()`; avoid object instantiation during parsing
* Validate incoming data against a schema (JSON Schema, Pydantic, Zod, Joi) before it's processed

**Checklist:**

* \[ \] No `pickle.loads()` with user data
* \[ \] YAML uses `safe_load()` not `load()`
* \[ \] No untrusted data passed to deserializers
* \[ \] User-supplied data validated against a schema before processing

## Advanced Hardening (Mature-Stage Layer)

A further layer of controls, worth adding once the base playbook above is covered and the product has matured past early-stage risk:

* String comparisons for secrets use constant-time checks, not regular equality
* GraphQL APIs have query depth and complexity limits
* Outbound webhooks are protected against SSRF, so they can't be tricked into hitting the internal network
* The lockfile (`package-lock.json`/`pnpm-lock.yaml`/`yarn.lock`) is checked in, so a compromised package can't sneak into a build
* The admin dashboard is IP allow-listed, not open to the whole internet
* DNS has CAA records, so only the chosen CA can issue certificates for the domain
* The domain registrar account has its own separate MFA from everything else
* Canary tokens are planted in the app to give immediate signal when someone's poking around where they shouldn't
* Session tokens are bound to a device fingerprint, not just the token itself
* The CI/CD pipeline scans for secrets before every commit gets merged

## Additional Vulnerability Classes to Audit

Also audit for the following. Classes already covered in detail above link to their entry.

* Cross-site scripting — see [item 9](#9-cross-site-scripting-xss---high)
* Cross-site request forgery — see [item 15](#15-no-csrf-protection---high)
* Insecure file uploads
* Path traversal vulnerabilities
* Server-side request forgery
* Broken password reset flows
* Weak session management — see [item 4](#4-weak-session-handling---high)
* Vulnerable JWT secrets
* Overly permissive CORS
* Missing rate limits — see [item 16](#16-missing-rate-limiting---high)
* Exposed test or staging environments
* Default credentials left unchanged
* Webhook endpoints without signature verification
* Payment or subscription checks done only on the front end
* IDOR and role escalation — see [items 2–3](#2-missing-authorization-checks-idor---critical)
* API endpoints trusting user-controlled input
* Logs containing sensitive information — see [item 13](#13-sensitive-data-in-urls-and-logs---medium)
* Exposed source maps

---

[← Production Readiness Checklist](01-production-readiness-checklist.md) · [Part 2: Ship](README.md) · [Contents](../../README.md#contents) · [How to Not Look AI-Generated →](../part-3-craft/01-how-to-not-look-ai-generated.md)
