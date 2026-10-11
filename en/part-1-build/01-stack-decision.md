[Contents](../../README.md#contents) › [Part 1: Build](README.md) · **English** | [繁體中文](../../zh-TW/part-1-build/01-stack-decision.md)

# Stack Decision

A compact, opinionated default stack for a solo founder or small team, and when it is actually worth adding more.

> **Executive conclusion.** The current stack is already strong. The better optimization is consolidation: keep the systems that compound development velocity, remove overlapping services, and treat Redis, dedicated vector search, deep observability, and dedicated feedback tooling as optional layers rather than defaults.

## 1. Recommended core stack

This is the default stack worth shipping and scaling a serious SaaS on, before introducing additional infrastructure.

| Layer | Default | Why it earns a place |
| ----- | ----- | ----- |
| Development | **Claude / Codex** | Code generation, review, debugging, and implementation acceleration. |
| Version control | **GitHub** | Source of truth for code, pull requests, issues, and CI/CD integration. |
| Application / deployment | **Vercel** | Best default for a Next.js/TypeScript product; low operational burden. |
| Backend / database | **Supabase** | Postgres, storage, auth, realtime, queues/cron, and vector support in one platform. |
| Payments | **Stripe** | Billing, subscriptions, Checkout, webhooks, and customer portal. |
| Email | **Resend** | Transactional email with a simple developer experience. |
| DNS / edge | **Cloudflare** | DNS, CDN/security controls, edge services, and optional registrar. |
| Product analytics | **PostHog** | Analytics, replay, flags, experiments — enough observability for many early-stage products. |

## 2. What to remove from the default stack

**Pinecone → Supabase pgvector.** For a normal SaaS with RAG, semantic search, or embeddings, keeping vectors inside Postgres is simpler. It avoids dual writes, metadata synchronization, deletion synchronization, and another network dependency. Introduce Pinecone only when retrieval is a core workload and pgvector is demonstrably the bottleneck.

**Clerk → Supabase Auth**, unless B2B identity is a product feature. Supabase Auth is sufficient for standard user accounts, social login, magic links, and database-aware authorization. Clerk earns its place when polished organization management, invitations, role-based access, and tenant switching materially improve a B2B product.

**Sentry → optional alongside PostHog.** PostHog now covers enough analytics, replay, and error visibility to be a credible early-stage default. Add Sentry when the team needs deeper exception analysis, tracing, and production debugging. At that point the separation is useful: PostHog explains user behavior; Sentry explains application failure.

**Namecheap → optional.** Because Cloudflare already handles DNS, registrar consolidation is convenient. Keeping the registrar separate is also defensible as an account-separation/security choice — this is an operational preference, not a technical requirement.

## 3. Services that should be demand-driven

| Service | Add it when… | Default position |
| ----- | ----- | ----- |
| **Upstash / Redis** | Caching, rate limits, ephemeral state, or a workload that actually benefits from Redis. | Do not add because "every SaaS needs Redis." |
| **Pinecone** | Dedicated, high-volume retrieval or advanced vector-search requirements. | Add after measuring a pgvector limitation. |
| **Sentry** | Production debugging needs exceed PostHog's capabilities. | Add when issue diagnosis is costing meaningful engineering time. |
| **ProductBridge** | Feedback volume is high enough that consolidation, deduplication, and prioritization are painful. | Early on, PostHog surveys \+ support \+ a simple backlog are sufficient. |
| **Cloudflare R2** | Large public files, substantial media bandwidth, or object-storage economics justify it. | Use Supabase Storage first. |
| **Clerk** | Organizations, team invites, sophisticated B2B RBAC, or auth UX are strategically important. | Use Supabase Auth otherwise. |

## 4. Architecture doctrine

* Prefer one system of record. Postgres should own durable application data wherever practical.
* Do not introduce a specialist database until the general-purpose database fails a measured requirement.
* Keep synchronous request paths short. Move email, embeddings, file processing, reports, and long-running AI work into queues/workflows.
* Add infrastructure in response to load, reliability, or product requirements — not anticipated scale.
* Optimize for reversibility. A boring, portable Postgres-centered architecture is usually preferable to an elegant proprietary abstraction.
* Every vendor has a carrying cost: SDKs, secrets, webhooks, billing, outages, permissions, monitoring, and data synchronization.

## 5. Background jobs: the one capability to plan deliberately

Async execution is more important than another database. Typical workloads include Stripe webhook processing, emails, embedding generation, file conversion, scheduled cleanup, external syncs, and long-running AI tasks.

| Need | Use first |
| ----- | ----- |
| Simple scheduled task | **Vercel Cron** |
| Database-driven async work | **Supabase Queues / Cron** |
| Long-running application or AI workflow | **Vercel Workflows** |
| Cache / rate limiting / ephemeral state | **Upstash Redis** |

## 6. Final stack

**Core — ship with this**

* Claude / Codex
* GitHub
* Vercel
* Supabase
* Stripe
* Resend
* Cloudflare
* PostHog

**Optional — add only when the trigger is real**

* Clerk — B2B identity
* Sentry — deep observability
* Upstash — Redis workloads
* Pinecone — vector scale
* ProductBridge — feedback volume
* R2 — object-storage economics

> **Operating rule.** Start with the smallest stack that can safely ship the product. Add a vendor only when it removes a measured constraint or creates a product advantage larger than its ongoing operational cost.

---

[Part 1: Build](README.md) · [Contents](../../README.md#contents) · [The Holy Trinity + 1 →](02-holy-trinity-plus-one/README.md)
