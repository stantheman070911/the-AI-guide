[Contents](../../README.md#contents) › [Part 1: Build](README.md) · **English** | [繁體中文](../../zh-TW/part-1-build/01-stack-decision.md)

# Stack Decision

The smallest stack that can safely ship and scale a SaaS for a solo founder or small team, when to add more, and what to skip.

> **Recommendation.** Start with eight services: one coding agent, GitHub, Vercel, Supabase, Stripe, Resend, Cloudflare, and PostHog. Treat everything else as an upgrade you add when a measured need appears. The principles below are durable; the tables are time-sensitive.

> Last verified: 2026-10-11. Prices and plan limits change; check the linked pages before deciding.

## Principles

* Prefer one system of record. Postgres should own durable application data wherever practical.
* Do not add a specialist database until the general-purpose one fails a measured requirement.
* Keep synchronous request paths short. Move email, embeddings, file processing, reports, and long-running AI work to queues or workflows.
* Add infrastructure for load, reliability, or product requirements you have, not scale you expect.
* Optimize for reversibility. A boring, portable, Postgres-centered architecture usually beats an elegant proprietary one.
* Every vendor has a carrying cost: SDKs, secrets, webhooks, billing, outages, permissions, monitoring, and data synchronization.
* Prefer widely used, well-documented tools. Coding agents produce better code for frameworks and services that are well represented in public code and docs. (Judgment, not a measured result.)
* Set spending limits on day one, on every platform and model provider.

## 1. Default stack

| Layer | Default | Why | Watch for |
| --- | --- | --- | --- |
| Coding agent | Claude Code or Codex | Mature terminal agents with sandboxing, MCP, and project instruction files. Pick one and learn it well. | See [Working with Coding Agents](03-working-with-coding-agents.md). Gemini CLI stopped serving requests on 18 June 2026 ([Google](https://developers.googleblog.com/an-important-update-transitioning-gemini-cli-to-antigravity-cli/)). |
| Code and CI | GitHub | Source of truth for code, reviews, issues, and Actions. | Harden Actions: [playbook item 11](../part-2-ship/02-security-remediation-playbook.md#11-cicd-and-publishing-credentials---high). |
| Hosting | Vercel | Lowest operational burden for Next.js. | The on-demand budget does not stop usage unless **Pause Production Deployments** is on ([docs](https://vercel.com/docs/spend-management)). |
| Database, auth, storage | Supabase | Postgres, auth, storage, realtime, queues, cron, and pgvector in one platform. Free: 500 MB, 50,000 MAU, paused after a week idle. Pro from $25/month with a spend cap on by default ([pricing](https://supabase.com/pricing)). | Row-level security is your security boundary: [playbook item 4](../part-2-ship/02-security-remediation-playbook.md#4-tenant-isolation-and-database-policies---critical). |
| Payments | Stripe | Checkout, Billing, webhooks, customer portal. | Selling digital products across borders: see merchant of record below. |
| Email | Resend | Transactional email with a simple API. | Set up SPF, DKIM, and DMARC before launch. |
| DNS and edge | Cloudflare | DNS, CDN, WAF, and an optional registrar. | A separate registrar is a defensible account-separation choice. |
| Analytics and errors | PostHog | Analytics, session replay, feature flags, experiments, and error tracking; the first 100,000 exceptions a month are free ([pricing](https://posthog.com/docs/error-tracking/pricing)). | Exclude internal traffic; avoid recording personal data in replays. |

## 2. Optional upgrades

Add one when its trigger is real.

| Upgrade | Add it when | Notes |
| --- | --- | --- |
| Merchant of record: Stripe Managed Payments or Paddle | Registering for and filing VAT or sales tax in many countries costs more than the fee. | Managed Payments became generally available in April 2026, for digital products, at 3.5% per transaction on top of standard Stripe fees ([pricing](https://support.stripe.com/questions/managed-payments-pricing)). |
| Sentry | Debugging needs exceed PostHog: tracing, release health, deeper stack analysis. | PostHog explains user behavior; Sentry explains application failure. |
| Upstash Redis | Caching, rate limiting, or ephemeral state the database handles poorly. | Not because "every SaaS needs Redis". |
| Vercel Workflows | Multi-step jobs must survive crashes, retries, and waits of hours or days. | Built on the open-source Workflow SDK; usage-based pricing ([docs](https://vercel.com/docs/workflows)). |
| Clerk | You want prebuilt auth UI, organizations, and invitations without building them. | Free up to 50,000 monthly retained users; basic organizations included, advanced B2B features $100/month ([pricing](https://clerk.com/pricing)). |
| AI gateway: Vercel AI Gateway or OpenRouter | You use several model providers and need fallback, routing, or one bill. | Adds a network hop and one more party that sees your prompts. |
| AI code review: CodeRabbit or Greptile | Pull request volume outgrows careful human review. | Published comparisons disagree and are often vendor-run. Trial both on your own pull requests. |

## 3. Specialized alternatives

Better than the default for particular requirements, not in general.

| Alternative | Choose it when |
| --- | --- |
| Better Auth | You want auth inside your own database without a hosted provider, especially off Supabase. Its team has maintained Auth.js, now security fixes only, since September 2025 ([announcement](https://www.better-auth.com/blog/authjs-joins-better-auth)). |
| Neon | You want serverless Postgres with instant branching per pull request. Databricks acquired it in May 2025. |
| Convex | Your app is realtime-heavy and you prefer a reactive TypeScript backend over SQL. |
| Railway, Render, or Fly.io | You need long-running processes, WebSockets, containers, or background workers that do not fit serverless functions. |
| Cloudflare Workers and R2 | You want edge compute, or storage with heavy public egress. |
| Firebase | Mobile-first apps already tied to Google services. |
| Turso | SQLite at the edge, or one database per tenant. |
| Pinecone | Retrieval is a core workload and pgvector is the measured bottleneck. |
| Ollama | Data cannot leave the machine, or you need offline inference. See [Building with LLMs](04-building-with-llms.md). |
| MongoDB Atlas | Your data is document-shaped and the team already knows MongoDB. |

## 4. Experimental

Promising, young, or with benefits so far reported only by their makers.

* **Antigravity CLI** — Google's closed-source replacement for Gemini CLI, launched May 2026.
* **Traycer** — a planning layer that writes file-level plans for coding agents.
* **Headroom** — compresses tool output and context before it reaches the model.
* **OpenViking** — a context database for agents, from Volcengine.
* **AI app builders as production backends** (Lovable, Emergent, Dreamflow) — fine for prototypes. Audit database policies before real data arrives.

## 5. Not recommended or unverified

* **Gemini CLI** — retired; migrate.
* **9Router** — routes your code and credentials through dozens of third-party providers, including free tiers. The data and terms-of-service risk outweighs the token savings.
* **Shared PHP hosting** for this stack — the wrong runtime model for a Next.js and Postgres app.
* **Adding Pinecone, Clerk, Redis, or Sentry by default** — each solves a problem you may not have yet.

## 6. Background jobs

Async execution matters more than another database. Typical work: Stripe webhooks, email, embeddings, file conversion, scheduled cleanup, external syncs, and long-running AI tasks.

| Need | Use first |
| --- | --- |
| Simple scheduled task | Vercel Cron or Supabase Cron |
| Database-driven async work | Supabase Queues |
| Long-running or multi-step workflow | Vercel Workflows |
| Cache, rate limiting, ephemeral state | Upstash Redis |

> **Operating rule.** Add a vendor only when it removes a measured constraint, or creates a product advantage larger than its ongoing operational cost.

---

[Part 1: Build](README.md) · [Contents](../../README.md#contents) · [The Holy Trinity + 1 →](02-holy-trinity-plus-one/README.md)
