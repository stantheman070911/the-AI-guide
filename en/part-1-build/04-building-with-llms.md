[Contents](../../README.md#contents) › [Part 1: Build](README.md) · **English** | [繁體中文](../../zh-TW/part-1-build/04-building-with-llms.md)

# Building with LLMs

Decisions for shipping LLM features: which model, how to call it, how to ground it in your data, what it costs, and how to know it works. Security for these features is in [Securing AI Features and Coding Agents](../part-2-ship/03-securing-ai-features-and-agents.md).

> Last verified: 2026-10-11. Model names and prices change monthly, so this chapter names none.

## Start simpler than you think

Anthropic's guidance on agents: start with "the simplest solution possible, and only increasing complexity when needed" ([Anthropic](https://www.anthropic.com/engineering/building-effective-agents)). In practice:

1. **One model call** with good instructions, examples, and retrieved context. Most features stop here.
2. **A fixed workflow** of several calls, when the steps are known in advance (extract, then classify, then draft).
3. **An agent loop**, where the model picks its next tool call, only when the steps cannot be decided in advance. Agents cost more, run slower, and compound errors.

## Choose models with your own evaluation set

Public leaderboards measure someone else's tasks.

* Collect 20 to 100 real inputs with expected outputs or grading criteria. Include hard and adversarial cases.
* Establish quality with a capable model, then try smaller and cheaper ones on the same set. Ship the cheapest one that passes.
* Re-run the set whenever you change a model, prompt, or retrieval setting. [promptfoo](https://github.com/promptfoo/promptfoo) is an open-source runner for this.
* Keep the model ID in configuration, not scattered through the code. You will change it.

## Calling the API

* **Structured output.** Use the provider's schema-constrained output or tool calling for anything your code parses, then validate with Zod or Pydantic anyway.
* **Streaming** for anything a user waits on.
* **Timeouts and retries** with backoff for rate limits and server errors. Set a maximum output length on every call.
* **Keys stay on the server.** See [playbook item 13](../part-2-ship/02-security-remediation-playbook.md#13-secret-keys-in-client-code---critical).
* **Prompts live in version control** next to the code, and change only with an evaluation run.

## Retrieval (RAG)

1. **Check whether you need it.** If the source material fits in the context window and the cost is acceptable with prompt caching, sending it whole is simpler and often better. (Judgment; test both on your evaluation set.)
2. **Start in Postgres.** pgvector in Supabase or Neon keeps vectors next to the data and its permissions. See [Stack Decision](01-stack-decision.md#3-specialized-alternatives) for when a dedicated vector database is worth it.
3. **Use hybrid search.** Embeddings miss exact strings such as error codes, SKUs, and names; full-text search catches them. Merge the two result lists.
4. **Add context to chunks, then rerank.** In Anthropic's tests, prepending a short chunk-specific context cut top-20 retrieval failures by 35%; adding BM25 brought the reduction to 49%; adding a reranker, to 67% ([Anthropic](https://www.anthropic.com/engineering/contextual-retrieval)).
5. **Filter by permission in the retrieval query.** Not after. See [AI security item 3](../part-2-ship/03-securing-ai-features-and-agents.md#3-enforce-access-control-before-retrieval).
6. **Evaluate retrieval separately.** Check whether the right chunk appears in the top results before judging the generated answer.

## Cost

* **Prompt caching** for repeated prefixes: system prompts, tool definitions, long documents.
* **Batch APIs** for work that can wait: Anthropic and OpenAI both price batch requests at half the normal rate ([Anthropic](https://platform.claude.com/docs/en/build-with-claude/batch-processing)).
* **Route by difficulty.** Send easy, high-volume tasks to a small model.
* **Measure per feature.** Log tokens and cost per request, tagged by feature and user, so you know what is expensive before the invoice does.
* **Cap it.** Per-user quotas and provider monthly limits ([playbook item 19](../part-2-ship/02-security-remediation-playbook.md#19-missing-rate-limits-and-spend-controls---high)).

## Observability

Log, for each call: prompt version, model, input and output tokens, latency, cost, and any user feedback. Review a sample of real transcripts every week; they show failures that metrics miss. Redact personal data before it reaches the logs.

[PostHog AI observability](https://posthog.com/ai-observability) fits if you already use PostHog. [Langfuse](https://github.com/langfuse/langfuse) is an open-source alternative with tracing, evaluations, and prompt management.

## Local models

Worth it when data cannot leave the machine, when you need offline use, or for predictable cost at high volume. [Ollama](https://ollama.com) is the easiest way to run open-weight models locally. Expect lower quality than frontier hosted models on complex reasoning, and memory to limit model size.

## Agents in production

* Design a small set of clearly scoped tools with helpful error messages and compact outputs. Overlapping tools confuse the model ([Anthropic](https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents)).
* Cap steps, time, and spend per run.
* Use durable execution for long tasks, so a crash or deploy does not lose progress. See [background jobs](01-stack-decision.md#6-background-jobs).
* Require human approval before irreversible actions.

---

[← Working with Coding Agents](03-working-with-coding-agents.md) · [Part 1: Build](README.md) · [Contents](../../README.md#contents) · [Production Readiness Checklist →](../part-2-ship/01-production-readiness-checklist.md)
