[Contents](../../README.md#contents) › [Part 3: Craft](README.md) · **English** | [繁體中文](../../zh-TW/part-3-craft/03-writing-with-ai.md)

# Writing with AI

An editing workflow for prose drafted with AI help, so the result is short, specific, and sounds like a person meant it. The rules for the prose itself are in [Appendix A](../appendix/01-writing-principles.md); give them to the model.

## The workflow

1. **Decide the point yourself.** Write it in one or two sentences before prompting. A model can supply fluent sentences, not your position.
2. **Give the model material.** Notes, facts, the audience, the length, Appendix A, and a sample of your own writing. Without material it fills space with averages.
3. **Draft.**
4. **Cut.** Delete the opening that warms up, the summary of what was just said, the closing that restates, and every sentence the piece survives without.
5. **Make it specific.** Replace each general claim with a name, a number, an example, or a source. If you have none, the claim may not belong.
6. **Check every fact.** Numbers, quotes, names, dates, and links. Models invent citations that look real.
7. **Read it aloud.** Rewrite whatever you would not say.

## Patterns that mark AI prose

* **Structure:** every section ends in a summary; every list has three items; a heading and three bullets for every idea.
* **Phrasing:** "It's not just X, it's Y"; stacked hedges; the same few inflated words ("robust", "seamless", "landscape", "delve").
* **Content:** explaining the obvious, caveats nobody asked for, answers to objections nobody raised, examples that could fit any topic.

Swapping synonyms does not fix these. Delete the sentence, or replace it with a specific fact.

## Prompting for edits

"Make it better" invites rewriting. Ask for operations you can check:

```text
Edit the draft below to about 60% of its length.
Keep every fact, number, and claim; do not add new ones.
Delete repetition, warm-up sentences, and closing summaries first.
Then list the five weakest remaining sentences and say why.
```

Ask for changes as a list or diff with reasons, so you can accept them one by one.

## Research and analysis

* Use the model to find and summarize sources, then read the primary source before you cite it.
* Ask for URLs and open each one. Check that it exists and says what was claimed.
* Keep what a source says separate from what the model infers from it.
* For data analysis, have the model write code that runs on the real data. Do not trust arithmetic done in the response.

---

[← Copywriting Guide](02-copywriting-guide.md) · [Part 3: Craft](README.md) · [Contents](../../README.md#contents) · [AI Fundamentals →](../part-4-learn-think/01-ai-fundamentals.md)
