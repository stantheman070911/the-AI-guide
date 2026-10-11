[Contents](../../README.md#contents) › [Part 2: Ship](README.md) · **English** | [繁體中文](../../zh-TW/part-2-ship/03-securing-ai-features-and-agents.md)

# Securing AI Features and Coding Agents

Two attack surfaces: the LLM features you ship to users, and the coding agents you run on your own machine and repositories. Both fail the same way. The references are the [OWASP Top 10 for LLM Applications 2025](https://genai.owasp.org/llm-top-10/) and the [OWASP Top 10 for Agentic Applications](https://genai.owasp.org/resource/owasp-top-10-for-agentic-applications-for-2026/) (December 2025).

> Last verified: 2026-10-11.

## The core problem: prompt injection

A model reads instructions and data in the same channel. Text inside a web page, email, PDF, issue, or tool result can redirect it. No filter reliably stops this; OWASP describes foolproof prevention as unclear given how models work ([LLM01:2025](https://genai.owasp.org/llmrisk/llm01-prompt-injection/)), and guardrail models can themselves be injected ([cheat sheet](https://cheatsheetseries.owasp.org/cheatsheets/LLM_Prompt_Injection_Prevention_Cheat_Sheet.html)).

So design for the case where injection succeeds. The question is not "can the model be tricked?" but "what can it do once it is?"

## The lethal trifecta

Simon Willison's rule ([post](https://simonwillison.net/2025/Jun/16/the-lethal-trifecta/)): an agent is exploitable when one session combines

1. access to private data,
2. exposure to untrusted content, and
3. a way to communicate externally.

Remove any one leg and the data-theft path closes. The external channel is often less obvious than a "send email" tool: a rendered Markdown image whose URL carries data, a link preview, a web-fetch tool, a pull request comment, or a commit to a public repository.

A documented demonstration: in May 2025, a prompt injection in a public GitHub issue caused an agent using the GitHub MCP server to copy data from the owner's private repositories into a public pull request ([Invariant Labs](https://invariantlabs.ai/blog/mcp-github-vulnerability)). The server had no bug. The combination was the flaw.

## LLM features you ship

### 1. Treat model output as untrusted input

Model output goes through the same escaping and validation as user input (OWASP LLM05).

* Render as text, or sanitize before rendering HTML or Markdown. Block external images in rendered output, or restrict `img-src` in your CSP, to close the image exfiltration channel.
* Request structured output and validate it against a schema before acting on it.
* Never pass model output to `eval`, a shell, or string-built SQL. See the [playbook's injection items](02-security-remediation-playbook.md#a05-injection).

### 2. Give tools the least privilege that works

Excessive agency (LLM06) turns a wrong answer into a wrong action.

* Tools act with the end user's permissions, never a service role. A support bot that can query every customer's orders will, eventually.
* Prefer read-only tools. Scope write tools narrowly: "refund this order up to its value", not "run SQL".
* Require explicit user confirmation for irreversible or external actions: sending messages, payments, deletions, publishing.

### 3. Enforce access control before retrieval

Retrieved documents are untrusted content, and a vector index ignores your permissions (LLM08).

* Filter by tenant and user permission in the query that selects candidate chunks, not after the model has seen them.
* Keep one user's uploads out of another user's context unless sharing is intended.
* Store each chunk's source. When a poisoned document is found, you need to know what it reached.
* Review what agents write to long-term memory; a memory written from untrusted content is a stored injection.

### 4. Assume the system prompt is public

Users can extract it (LLM07). Keep secrets, API keys, and authorization rules out of prompts. Enforce permissions in code.

### 5. Bound consumption

Set maximum output tokens, request timeouts, agent step limits, per-user quotas, and provider-level monthly caps (LLM10). The [playbook's spend-control item](02-security-remediation-playbook.md#19-missing-rate-limits-and-spend-controls---high) covers platform limits.

### 6. Test injection like any other bug

Add injection cases to your evaluation suite: instructions hidden in documents, tool results, and user profiles, plus attempts to exfiltrate through each output channel. [promptfoo](https://github.com/promptfoo/promptfoo) is an open-source tool for this kind of red-team testing; OpenAI acquired it in March 2026 and said it would stay open source. Re-run the suite when you change models or prompts.

## Coding agents you run

### 7. Sandbox the agent, not just the code

A coding agent runs shell commands with your user account, your SSH keys, and your cloud credentials.

* Turn on the agent's OS-level sandbox and keep network access to an allowlist. Know its boundary: Claude Code's sandbox covers shell commands, while its file tools, MCP servers, and hooks run outside it ([docs](https://code.claude.com/docs/en/sandboxing)).
* Run unattended or "auto-approve" sessions in a dev container, VM, or cloud environment, never on the machine that holds your production credentials.
* Treat opening a repository as running its code. Project files such as `.claude/settings.json`, `.mcp.json`, and hooks can start servers, run commands, or redirect API traffic. Two Claude Code flaws did this before the trust prompt ([CVE-2025-59536](https://nvd.nist.gov/vuln/detail/CVE-2025-59536), [CVE-2026-21852](https://nvd.nist.gov/vuln/detail/CVE-2026-21852)). Keep agents updated, and open unfamiliar repositories in a container or VM.
* Grant broad permission modes per task, not permanently.

### 8. Keep production credentials away from agents

Anything an agent can read, it can leak: into logs, pull requests, or the prompts sent to a model provider.

* Give agents scoped, short-lived tokens for development resources. No production database URLs, no `service_role` or `sb_secret_` keys, no root cloud credentials.
* Deny reads of `.env` files and credential directories in the permission rules and in the sandbox (`sandbox.filesystem.denyRead` or `sandbox.credentials`). Permission rules alone do not stop a script the agent runs from opening the file. Keep production secrets out of local `.env` files.

### 9. MCP servers and skills are code you install

The MCP specification states that tools "represent arbitrary code execution" and that tool descriptions and annotations should be treated as untrusted unless they come from a trusted server ([spec](https://modelcontextprotocol.io/specification/latest)). Known attacks:

* **Tool poisoning:** hidden instructions in a tool description that the model reads and the user never sees.
* **Rug pulls:** a server changes a tool's description after you approved it ([Invariant Labs](https://invariantlabs.ai/blog/mcp-security-notification-tool-poisoning-attacks)).
* **Cross-server flows:** one server's output steering calls to another, which can assemble the lethal trifecta from individually harmless servers.

Install servers and skills from publishers you can identify, pin versions, read tool descriptions and any bundled scripts before enabling them, and give each server only the credentials its job needs. The NSA's May 2026 guidance on MCP covers the same ground for larger deployments ([NSA](https://www.nsa.gov/Press-Room/Press-Releases-Statements/Press-Release-View/Article/4496698/nsa-releases-security-design-considerations-for-ai-driven-automation-leveraging/)). [Appendix D](../appendix/04-evaluating-tools-and-skills.md) has a vetting checklist.

### 10. Separate untrusted input from write access

Issues, pull request comments, web pages, and dependency READMEs are untrusted content. An agent that processes them should not, in the same session, hold write access to private repositories, secrets, or deployment.

* Run triage agents read-only, or limit them to one public repository per session.
* Do not let CI agents triggered by external contributors see secrets.

### 11. Review what agents produce

Agents add dependencies, change auth code, and edit CI workflows as readily as they fix typos.

* Agents push to branches; humans merge. Protect the default branch.
* Require human review for changes to workflows, auth, database policies, migrations, and dependency manifests.
* Run the security checks from the [playbook](02-security-remediation-playbook.md) in CI, so review does not depend on attention alone.

---

[← Security Remediation Playbook](02-security-remediation-playbook.md) · [Part 2: Ship](README.md) · [Contents](../../README.md#contents) · [How to Not Look AI-Generated →](../part-3-craft/01-how-to-not-look-ai-generated.md)
