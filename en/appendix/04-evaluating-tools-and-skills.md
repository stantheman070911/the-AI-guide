[Contents](../../README.md#contents) › [Appendix](README.md) · **English** | [繁體中文](../../zh-TW/appendix/04-evaluating-tools-and-skills.md)

# Appendix D: Evaluating Tools and Skills

How to decide whether a tool, agent skill, or MCP server is worth installing, and which ones passed for common jobs. Popularity, sponsorship, and launch videos are not evidence of quality.

> Last verified: 2026-10-11.

## Trust tiers

| Tier | What it means | Default stance |
| --- | --- | --- |
| Official | Published by the vendor of the platform it integrates with. | Use after reading what it does. |
| Community | Public source, identifiable and active maintainers. | Review the code and pin a version before installing. |
| Experimental | Young, few maintainers, or benefits reported only by its makers. | Try in a sandbox on a throwaway project. |
| Unverified | Unknown publisher, no source, or claims you cannot check. | Do not install. |

## Vetting checklist

Before installing a skill, MCP server, or agent plugin:

1. **Publisher.** Can you identify the maintainer and read the source?
2. **Maintenance.** Recent releases, answered issues, more than one contributor.
3. **What it runs.** Read `SKILL.md`, bundled scripts, install hooks, and every MCP tool description. Instructions for the model are code for this purpose.
4. **What it can reach.** Filesystem paths, network hosts, and credentials. Grant the minimum.
5. **Pinning.** Pin a version or commit. A tool whose description changes after you approved it is a known attack ([Securing AI Features and Coding Agents](../part-2-ship/03-securing-ai-features-and-agents.md#9-mcp-servers-and-skills-are-code-you-install)).
6. **Combination.** Does it complete the lethal trifecta together with tools you already run?
7. **Evidence.** Speed and token-saving figures from the makers are hypotheses. Measure on your own work.
8. **Exit.** Can you remove it without breaking the project?

## By use case

### Coding agents

Pick one and learn it. Claude Code and Codex are the default terminal agents ([Stack Decision](../part-1-build/01-stack-decision.md#1-default-stack)). Cursor and GitHub Copilot suit editor-centered work; JetBrains Junie suits IntelliJ users; [OpenHands](https://github.com/OpenHands/OpenHands) is the open-source option for self-hosted agents. Gemini CLI no longer serves free and personal Google AI plans as of June 2026; Google's replacement for those plans, Antigravity CLI, is experimental.

### Planning

The [Holy Trinity documents](../part-1-build/02-holy-trinity-plus-one/README.md) need no tool. Traycer, a dedicated planning layer for agents, is experimental.

### Code review

CodeRabbit and Greptile are the most widely compared AI reviewers. Published comparisons are mostly vendor-run and disagree, so trial both on two weeks of your own pull requests and count the comments you acted on. Keep humans as the approvers.

### Testing and evaluation

* [Playwright](https://playwright.dev) for end-to-end tests. Microsoft's official [Playwright MCP server](https://github.com/microsoft/playwright-mcp) lets an agent drive a browser through accessibility snapshots, so it can check its own UI work.
* [promptfoo](https://github.com/promptfoo/promptfoo) for LLM evaluations and red-team tests.

### Security

| Job | Tools |
| --- | --- |
| Secrets in code and history | `gitleaks`, `trufflehog`, GitHub secret scanning with push protection |
| Static analysis | Semgrep, GitHub code scanning |
| Dependencies | `npm audit`, `pip-audit`, Dependabot or Renovate |
| Database policies | Supabase Security Advisor |
| Authorized dynamic testing | ZAP; `nmap` and `sqlmap` against your own staging systems only |

### Databases

Choose the database with the [Stack Decision](../part-1-build/01-stack-decision.md). If you connect an agent to Supabase through its official MCP server, scope it to one project, use read-only mode, and point it at a development project; read-only mode still lets readable rows enter the model's context, and prompt injection remains the main risk ([Supabase](https://supabase.com/docs/guides/ai-tools/mcp)).

### Browsing and web data for agents

Playwright MCP for local browsing. Hosted browsers (Browserbase) and search APIs (Exa, SerpAPI) when an agent needs web access at volume. Everything fetched is untrusted content.

### Design

Impeccable is a community skill that adds design critique and polish commands for frontend work. Mobbin is a paid library of real app screens; useful for interaction patterns, but it is the same visual feed everyone else uses ([How to Not Look AI-Generated, §13](../part-3-craft/01-how-to-not-look-ai-generated.md#13-build-references-from-outside-the-same-visual-feedback-loop)).

### LLM app builders

Dify is an open-source visual builder for LLM workflows, good for internal tools and prototypes. For product features, prefer code you own and can test.

### Persona packs

Collections of agent "personas", such as The Agency, add role descriptions rather than capability. Prefer skills that encode a procedure and a way to check the result.

---

[← Appendix C: Skills and Tools I Use](03-skills-and-tools.md) · [Appendix](README.md) · [Contents](../../README.md#contents)
