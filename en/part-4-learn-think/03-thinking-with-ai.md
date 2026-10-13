[Contents](../../README.md#contents) › [Part 4: Learn and Think](README.md) · **English** | [繁體中文](../../zh-TW/part-4-learn-think/03-thinking-with-ai.md)

# Thinking with AI

Judgment, the jagged edge of AI capability, root-cause analysis, and ways to verify AI output.

> Last verified: 2026-10-13.

> **Original language:** Traditional Chinese. This English version is a translation. If the two versions disagree, the [Chinese original](../../zh-TW/part-4-learn-think/03-thinking-with-ai.md) is authoritative.

## 1. When execution is abundant, judgment is the advantage

Naval Ravikant's view: AI coding agents and vibe coding lower the bar for *how* to build, so *what* to build matters more ([Naval](https://nav.al/ai)). The competitive advantage shifts to:

* **Taste:** recognizing quality.
* **Judgment:** choosing problems worth solving.
* **Creativity:** developing original ideas.
* **Expertise:** understanding a specialized field.
* **Distribution:** reaching customers and building a defensible business.

AI can generate a large number of possibilities. Which ideas are original, meaningful, and worth pursuing is still a human call.

## 2. Ray Dalio's five-step loop

In *Principles*, Ray Dalio breaks reaching a goal into five steps and sums up the attitude behind them as Pain + Reflection = Progress. The steps run in a loop:

> **Goal → problem → root cause → plan → execution → continuous improvement**

What each step involves, and how the work divides once AI is added:

| Step | What it involves | Where AI helps | Only you can |
| --- | --- | --- | --- |
| **1 Set clear goals** | Prioritize; you can have almost anything, but not everything at once | List options, compare trade-offs | Decide what matters most and what to give up |
| **2 Identify and face problems** | Catch them early; do not tolerate problems that block progress | Organize records, flag anomalies | Admit the problem exists |
| **3 Diagnose root causes** | Separate symptoms from causes; see your own and others' blind spots | Find patterns across repeated mistakes | Face your own blind spots and ego |
| **4 Design a solution** | Break out the steps, resources, and expected results from the root cause | Break down steps, estimate resources | Own the plan |
| **5 Push it through** | Track with metrics and adjust to the results | Track progress, send reminders | Discipline and execution |

## 3. Treat AI as an assistant in training

| Principle | In practice |
| --- | --- |
| **Know what good looks like** | Define the outcome, audience, constraints, and success criteria |
| **Maintain high standards** | Treat AI output as a draft; review and revise it |
| **Try replacing parts of your work with AI** | Find tasks suited to automation, and learn where human oversight is still needed |

AI is like a new employee: it needs examples, context, clear instructions, feedback, and quality checks.

## 4. AI's capabilities have a jagged edge

AI's capability frontier is jagged: it can be astonishing at very hard things and wrong about things that look simple. In July 2025, models from OpenAI and Google DeepMind reached gold-medal level at the International Mathematical Olympiad ([Google DeepMind](https://deepmind.google/discover/blog/advanced-version-of-gemini-with-deep-think-officially-achieves-gold-medal-standard-at-the-international-mathematical-olympiad/)). Yet according to Stanford HAI's *AI Index 2026*, the best model reads an analog clock correctly only 50.1% of the time ([Stanford HAI](https://hai.stanford.edu/ai-index/2026-ai-index-report)).

The term **jagged technological frontier** comes from a 2023 Harvard Business School and BCG experiment with 758 consultants. On tasks inside AI's abilities, consultants using AI completed 12.2% more tasks, worked 25.1% faster, and produced work of about 40% higher quality. On a task the researchers designed to sit outside AI's abilities, consultants using AI were about 19 percentage points less likely to get it right ([Dell'Acqua et al.](https://mitsloan.mit.edu/sites/default/files/2023-10/SSRN-id4573321.pdf)).

The edge moves as models update, so each time, first ask: is this task inside the frontier or outside it?

## 5. Two kinds of error: wrong answers and wrong actions

In a single exchange, a model can produce unfounded details in a perfectly confident tone. This is usually called **hallucination**.

Another tendency is **sycophancy**: the more memory it has and the more the user insists, the more readily the model agrees. In April 2025, OpenAI rolled back a GPT-4o update because it agreed with users too much ([OpenAI](https://openai.com/index/sycophancy-in-gpt-4o/)).

Agents add a different kind of error: one step rests on a false premise and the next ten follow it off course, or the system reports it is done when nothing usable exists. Common situations:

* The goal is unclear, so the system guesses the expected result.
* An early step goes wrong and later work carries the error forward.
* Intermediate data is compressed, lost, or mixed with irrelevant information.
* The output looks complete but fails a real check.
* When things drift, the system has no way to notice.

The fix is better original context, tighter permissions, and verification designed into the process (see [Creating with AI §4](04-creating-with-ai.md#4-make-verification-part-of-the-work)). For the "agent says it's done" problem in code, see [the completion trap](../part-1-build/02-holy-trinity-plus-one/README.md#the-completion-trap-and-how-to-close-it).

## 6. How it feels versus what it measures

"I feel like AI helped" can also be wrong. In a 2025 randomized controlled trial, METR had 16 experienced open-source developers complete 246 real tasks in projects they knew well, randomly deciding which tasks allowed AI. They expected to be 24% faster, estimated afterwards that they had been 20% faster, and were measured as 19% slower ([METR](https://metr.org/blog/2025-07-10-early-2025-ai-experienced-os-dev-study/)).

The sample was limited to experienced developers in large projects they knew, and the tools keep improving. METR's 2026 follow-up could not produce a reliable estimate: many developers did not want to work without AI, so they declined to take part or skipped some tasks ([METR](https://metr.org/blog/2026-02-24-uplift-update/); see also [Working with Coding Agents](../part-1-build/03-working-with-coding-agents.md#what-the-evidence-says)).

A CHI 2025 survey of 319 knowledge workers by Microsoft Research and Carnegie Mellon University found the same pattern: the more people trusted AI, the less critical thinking they did; the more they trusted their own ability, the more they did ([Lee et al.](https://www.microsoft.com/en-us/research/publication/the-impact-of-generative-ai-on-critical-thinking-self-reported-reductions-in-cognitive-effort-and-confidence-effects-from-a-survey-of-knowledge-workers/)).

## 7. Cross-examination: an AI council

For important answers, have model A reach a first conclusion, then give it to model B to find errors, gaps, or inconsistencies: an **AI model council**. Different models can make the same mistake, so still go back to the source to check.

Use a model from a different company where you can, because the training data and blind spots differ. With only one model, open a new conversation and check again in a clean context, so it does not defend its earlier answer.

For research tasks, require citations you can open and trace.

## 8. Make AI help you think one level deeper

These uses add a little friction to thinking, for the same reason as the desirable difficulties in [Learning with AI](02-learning-with-ai.md#6-when-not-to-use-ai):

* **Devil's advocate:** "Argue against my idea with the strongest case you can. Don't be polite." This offsets the model's tendency to agree.
* **Pre-mortem:** "Assume this plan has failed a year from now. What are the three most likely reasons?" The method comes from the psychologist Gary Klein.
* **Ask me first:** "Before giving advice, ask me five questions you need answered."
* **Tough editor:** ask it to critique a draft like a demanding editor and a real user, without flattery (see [Creating with AI §8](04-creating-with-ai.md#8-three-prompts-for-learning-while-building)).

## 9. Separate predictions from established facts

Talk about AI and work often mixes practical advice with strong predictions. One way to sort them:

| Claim | How to use it |
| --- | --- |
| AI lets one person do the work of a much larger team | Treat it as a task-dependent possibility; test the actual quality and limits |
| Technical skill with specific tools will be worth less | Treat it as a directional prediction; keep practicing the technical basics |
| Creators and audiences will replace institutions and employers | Treat independent publishing as one more option |
| Small teams with AI can produce more | Verify with projects, user feedback, and cost |
| AI output becomes valuable through repeated revision | Apply directly: define standards, check drafts, keep improving |

---

[← Learning with AI](02-learning-with-ai.md) · [Part 4: Learn and Think](README.md) · [Contents](../../README.md#contents) · [Creating with AI →](04-creating-with-ai.md)
