[Contents](../../README.md#contents) › [Part 2: Ship](README.md) · **English** | [繁體中文](../../zh-TW/part-2-ship/01-production-readiness-checklist.md)

# Website Production Readiness Checklist

A consolidated checklist for shipping a "vibecoded" website — one built quickly, often with heavy AI assistance — to production.

## 1. Domain, Branding & Basic Production Polish

* Connect a custom domain instead of only using `*.vercel.app`
* Add a favicon
* Replace default "Vite", "React", "Next.js" browser titles
* Give every important page a unique page title
* Add a real logo, and make it clickable back to the homepage
* Fix the copyright year
* Remove placeholder text and unused navigation items
* Replace generic stock imagery with real business/team photography where appropriate

## 2. Mobile & Responsive Design

* Make every page mobile-optimized; remove horizontal scrolling and fix overflow
* Add a proper mobile navigation menu
* Check tap targets, typography, and image containment at small screen sizes
* Check tables, cards, and forms on mobile
* Add a sticky mobile CTA where appropriate
* Test common widths: 320px, 375px, 390px, 430px, tablet, and desktop

A website is not production-ready if the desktop version works but the mobile version merely "shrinks."

## 3. Navigation & Broken Interactions

* Find and repair broken links, buttons, and footer links
* Make phone numbers clickable with `tel:` and email addresses with `mailto:`
* Check all navigation links, CTA destinations, external links, and anchor links
* Remove dead navigation items
* Confirm browser Back/Forward navigation works correctly

## 4. Error Handling & User Feedback

* Add a custom, useful 404 page — not merely decorative
* Add success and error messages after forms/actions, and visible loading states
* Prevent buttons from appearing unresponsive during requests
* Handle failed API requests, empty states, and expired/invalid URLs gracefully
* Remove raw framework/server errors from the user-facing UI

## 5. Forms & Lead Generation

* Add clear, obvious calls-to-action above the fold
* Add a thank-you page and confirmation/success state after form submission
* Add useful validation messages; avoid asking for unnecessary information
* Test all contact forms end-to-end and verify inquiries reach their destination
* Add a response-time promise where commercially appropriate (e.g. *"We typically respond within one business day"*)
* Track form submissions as conversions

## 6. SEO Fundamentals

* Unique `<title>` and meta description for every important page
* Add canonical tags, `robots.txt`, and `sitemap.xml`
* Ensure important pages are indexable; confirm `noindex` isn't accidentally enabled
* Add internal links and breadcrumbs where appropriate; use descriptive URLs
* Avoid duplicate pages/content
* Redirect HTTP → HTTPS and duplicate hostname versions consistently
* Configure proper 301 redirects when URLs change

## 7. HTML Structure & Semantic SEO

* One meaningful `<h1>` per important page — avoid competing `<h1>` headings
* Use a logical `h1 → h2 → h3` hierarchy
* Add a `lang` attribute to `<html>`
* Use semantic elements (`header`, `nav`, `main`, `section`, `article`, `footer`) instead of building everything from generic `<div>`s

The goal is a coherent document hierarchy, not simply satisfying an SEO checker.

## 8. Image SEO & Accessibility

* Add useful alt text to meaningful images; use empty alt text for decorative ones
* Avoid keyword-stuffed alt text
* Compress images, serve appropriately sized versions, and prefer modern formats
* Lazy-load below-the-fold images
* Set image width/height to reduce layout shift

## 9. Social Sharing

* Add Open Graph metadata: title, description, canonical/share URL, and a share image
* Add Twitter/X card metadata where relevant
* Test how links actually look when shared

You do not want "Vite \+ React", a localhost-style title, no image, and a random description appearing when someone shares your business.

## 10. Structured Data / Schema

* Add relevant Schema.org structured data (LocalBusiness, Organization, Breadcrumb, FAQ where applicable and consistent with visible content)
* Add contact/business information correctly and validate the structured data
* Keep schema consistent with what users can actually see

## 11. Local Business Websites

For plumbers, contractors, dentists, restaurants, agencies, clinics, etc.:

* Add business address, clickable phone number, hours, map, and directions
* Add LocalBusiness schema and service-area information
* Add real customer reviews, testimonials, and project/customer photography
* Add location/service pages where genuinely useful
* Keep NAP information (Name, Address, Phone) consistent everywhere it appears

## 12. Trust & Conversion

* Clear CTA and value proposition above the fold; explain who the product/service is for
* Add real customer reviews and testimonials with attribution, plus a case-study section
* Add roughly five useful FAQs and response-time expectations
* Add real team/company photography and contact information
* Add a privacy policy and terms where appropriate
* Add trust indicators only when genuine — avoid fabricated logos, reviews, or testimonials

## 13. Content Quality

* Remove AI placeholder copy, "Lorem ipsum," and generic claims like "We provide innovative solutions"
* Remove duplicated sections; check spelling and grammar; verify all factual claims
* Make CTAs specific and explain services/products clearly
* Make homepage messaging understandable within several seconds
* Ensure every page has a clear purpose

A common vibecoding failure is a technically functional website containing copy that says almost nothing.

## 14. Crawlability & Rendering

* Check what appears in View Source, and confirm crawlers can reach critical content
* Avoid unnecessarily making the entire site client-rendered
* Verify page metadata is server-rendered where appropriate
* Check pages with JavaScript disabled/degraded if SEO matters
* Check robots directives, and decide intentionally whether AI crawlers should be allowed or blocked

An empty-looking View Source is a warning sign, not automatically a bug. For an app or dashboard, heavy client rendering can be reasonable; for SEO landing pages, it deserves investigation.

## 15. Analytics & Measurement

* Install analytics (Google Analytics, PostHog, or another intentional stack) and verify it fires in production
* Track major CTA clicks, form submissions, and conversions (signup, purchase/subscription completion, etc.)
* Exclude internal/test traffic where useful
* Avoid collecting unnecessary personal information

## 16. Performance

* Compress images; remove enormous JS bundles and unused dependencies
* Code-split and lazy-load expensive components; avoid shipping server libraries to the client
* Audit third-party scripts and optimize fonts
* Avoid layout shifts; check Largest Contentful Paint, Interaction to Next Paint, and Cumulative Layout Shift
* Test on a slower mobile connection and lower-end hardware

Vibecoded sites frequently perform well on the developer's MacBook and poorly on an actual customer's phone.

## 17. Browser Console & Production Hygiene

* Production console should not be full of errors — fix failed network requests, framework warnings, and hydration errors
* Remove debug logging, development banners, and unused code/assets
* Disable debug mode and check production environment configuration
* Decide intentionally whether production source maps should be exposed
* Verify production builds rather than relying solely on local dev mode

## 18. Secrets & API Keys

**Critical, not optional polish.**

* Hide API keys; never put secret keys in frontend JavaScript
* Audit environment variables and distinguish public vs. private ones
* Check Git history (including old branches/tags) for accidentally committed secrets, and rotate anything exposed
* Restrict API keys where the provider supports it; use separate dev/production credentials
* Ensure `.env` files are not committed, and verify build logs don't expose secrets

One of the highest-risk vibecoding mistakes is asking an AI to integrate an API and then accidentally shipping the secret into the client bundle.

*See the [Security Remediation Playbook](02-security-remediation-playbook.md#secrets-and-keys) for detailed remediation steps on hard-coded credentials and exposed client-side keys.*

## 19. Authentication & Authorization

* Add authentication when private functionality exists; protect admin routes and APIs
* Verify authentication and check permissions server-side
* Implement authorization separately from authentication; prevent users from requesting another user's data
* Test unauthenticated requests and low-privilege users attempting admin actions manually

**Critical principle:** a button hidden from the user does not mean permission denied. The server/database must enforce authorization.

*See the [Security Remediation Playbook](02-security-remediation-playbook.md#a01-broken-access-control) for detailed remediation steps on client-side auth, IDOR, broken access controls, session handling, and auth bypass paths.*

## 20. Database Security

* Check database access rules; enable Row Level Security where applicable
* Test database policies and prevent direct unauthorized writes
* Parameterize database queries and apply least-privilege access
* Never expose service/admin database credentials to browsers
* Back up important data and verify destructive operations require appropriate authorization

For Supabase in particular, a very common vibecoding mistake is building the UI first, discovering permissions later, then leaving tables overly permissive so the app "works." See [playbook item 4](02-security-remediation-playbook.md#4-tenant-isolation-and-database-policies---critical).

## 21. Input & Application Security

* Sanitize and validate user input — on the server, not only the client
* Protect against XSS, SQL injection, and unsafe URL redirects
* Validate IDs and object ownership; reject unexpected input and limit payload sizes
* Avoid blindly rendering AI- or user-generated HTML; escape output appropriately

*See the [Security Remediation Playbook](02-security-remediation-playbook.md#a05-injection) for detailed remediation steps on SQL injection, XSS, and command injection.*

## 22. Abuse Prevention & Cost Protection

Particularly important for AI products.

* Add rate limiting, especially on authentication endpoints, expensive APIs, and AI generation endpoints
* Protect contact forms from spam and add reasonable request-size limits
* Add provider billing/spend alerts and spend caps where supported
* Add per-user usage quotas where appropriate to prevent unlimited expensive jobs

An AI endpoint without rate limiting can turn a $20/month infrastructure bill into a $2,000 surprise bill very quickly.

*See [Security Remediation Playbook, item 19](02-security-remediation-playbook.md#19-missing-rate-limits-and-spend-controls---high) for a detailed remediation plan.*

## 23. File Upload Security

* Require authentication where appropriate; restrict file types and verify MIME types
* Limit maximum file size and generate server-side filenames rather than trusting user filenames
* Prevent executable uploads where inappropriate; restrict storage permissions
* Prevent users from accessing private uploads belonging to others; avoid exposing private storage buckets accidentally
* Consider malware scanning for higher-risk systems

## 24. Web Security Configuration

* Enable HTTPS and redirect HTTP to HTTPS
* Add appropriate security headers: CSP, HSTS, `X-Content-Type-Options`, `Referrer-Policy`
* Control framing with CSP `frame-ancestors`
* Secure cookies with `HttpOnly`, `Secure`, and an appropriate `SameSite` policy
* Check CORS configuration; avoid `Access-Control-Allow-Origin: *` for sensitive APIs
* Add CSRF protection where the authentication architecture requires it

*See the Security Remediation Playbook for [security headers](02-security-remediation-playbook.md#7-security-headers---medium) and [CSRF](02-security-remediation-playbook.md#22-cross-site-request-forgery-csrf---high).*

## 25. Deployment & Production Configuration

* Check all production environment variables and staging vs. production configuration
* Disable debug mode and development-only endpoints
* Check production API URLs, OAuth redirect URLs, webhook URLs, and allowed origins
* Verify email is using the production domain, and that the payment system is in the correct mode
* Verify the database points to production, and that backups, monitoring, and error tracking are in place
* Test deployment from a clean build

## 26. Accessibility

* Meet WCAG 2.2 AA: text contrast, visible focus, keyboard access, labeled inputs, 24 × 24 px minimum targets
* Do a keyboard-only pass and a screen reader pass, not only an automated scan
* Check whether the European Accessibility Act applies to you

*See [How to Not Look AI-Generated, §23](../part-3-craft/01-how-to-not-look-ai-generated.md#23-treat-accessibility-as-a-design-constraint).*

## 27. AI Features

* Treat model output as untrusted: escape it, validate structured output, never execute it
* Give tools the end user's permissions; confirm irreversible actions with the user
* Filter retrieval by tenant and permission before the model sees anything
* Cap tokens, steps, and spend per user and per provider
* Test prompt injection through every input and output channel

*See [Securing AI Features and Coding Agents](03-securing-ai-features-and-agents.md).*

## The higher-level audit

The checklist above reduces to eight production gates:

| Gate | Question |
| ----- | ----- |
| 1\. Does it work? | Links, buttons, forms, routing, 404, errors |
| 2\. Does it work on mobile? | Responsive design, overflow, menus, tap targets |
| 3\. Can people find it? | SEO, metadata, sitemap, robots, schema |
| 4\. Does it convert? | CTAs, reviews, FAQs, case studies, forms |
| 5\. Does it look legitimate? | Domain, favicon, branding, real content/photos |
| 6\. Is it fast? | Images, JS bundles, rendering, Core Web Vitals |
| 7\. Can we measure it? | Analytics, conversions, error monitoring |
| 8\. Can it be attacked? | Secrets, auth, authorization, input, DB, uploads, abuse, AI features |

The last gate deserves the most weight in the AI/vibecoding era: bad metadata makes a site look amateur, but bad authorization can expose an entire customer database.

Treat the checklist across three severity levels:

* **P0 — Security / data / money:** exposed API keys, auth, permissions, database rules, uploads, rate limiting, payment configuration, production settings.
* **P1 — Functionality / conversion:** broken links, forms, buttons, mobile, errors, CTAs, 404s.
* **P2 — Discoverability / polish:** SEO, schema, favicon, OG images, titles, metadata, case studies, FAQs.

P0 items correspond to the 🚨 Critical / 🔴 High entries in the [Security Remediation Playbook](02-security-remediation-playbook.md).

---

[← Building with LLMs](../part-1-build/04-building-with-llms.md) · [Part 2: Ship](README.md) · [Contents](../../README.md#contents) · [Security Remediation Playbook →](02-security-remediation-playbook.md)
