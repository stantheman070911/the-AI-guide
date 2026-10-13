[Contents](../../README.md#contents) › [Part 4: Learn and Think](README.md) · **English** | [繁體中文](../../zh-TW/part-4-learn-think/02-learning-with-ai.md)

# Learning with AI

Active production at the center, and research evidence for turning AI into a learning coach.

> Last verified: 2026-10-13.

> **Original language:** Traditional Chinese. This English version is a translation. If the two versions disagree, the [Chinese original](../../zh-TW/part-4-learn-think/02-learning-with-ai.md) is authoritative.

## 1. The core principle: active production

Use AI to strengthen your own thinking, practice, recall, and output. You still have to do those things yourself.

| Passive consumption | Active production |
| --- | --- |
| Reading or rereading material | Recalling content from memory |
| Watching videos | Explaining a concept in your own words |
| Reading an AI-generated explanation | Answering questions without help |
| Collecting notes | Solving problems and applying knowledge |

Passive consumption creates the feeling of having understood. Active production tests whether you can retrieve and use the information. The core loop:

> **Attempt → get targeted feedback → fix mistakes → redo it alone → test from memory → review after a gap**

Roediger and Karpicke's 2006 experiment in Psychological Science ([APS](https://www.psychologicalscience.org/observer/test-enhanced-learning)):

| Method | Recall after 5 minutes | Recall after 1 week |
| --- | --- | --- |
| Reread the material four times | 83% | 40% |
| Read once, tested three times | 71% | 61% |

The rereading group remembered more after five minutes and was overtaken by the testing group a week later. Reading a polished AI explanation works about as well as rereading.

## 2. The evidence: how you use it decides what you learn

Research on learning with AI from the past two years points the same way: AI can speed learning up or weaken it, depending on how it is used and designed.

| Study | Design | Main findings |
| --- | --- | --- |
| Turkish high school math ([Bastani et al., PNAS 2025](https://papers.ssrn.com/abstract=4895486)) | Nearly 1,000 high school students; GPT Base, which gave answers, against GPT Tutor, which gave hints only and was designed with teachers | In practice, Base beat the control group by 48% and Tutor by 127%; on the exam without AI, Base scored 17% worse and Tutor matched the control |
| Anthropic coding-skills experiment ([January 2026](https://www.anthropic.com/news/AI-assistance-coding-skills)) | 52 engineers (mostly junior) learning Trio, an unfamiliar Python library, randomly assigned | The AI group averaged 50% on the quiz, the hand-coding group 67%; the AI group was not meaningfully faster; the largest gap was on debugging questions |
| Harvard physics AI tutor ([Kestin et al., Scientific Reports 2025](https://www.nature.com/articles/s41598-025-97652-6)) | 194 students; a carefully designed AI tutor at home against in-class active learning | Learning gains more than double the classroom's; median time 49 minutes |
| World Bank after-school program in Nigeria ([2024](https://blogs.worldbank.org/en/education/From-chalkboards-to-chatbots-Transforming-learning-in-Nigeria)) | Six weeks of English with GPT-4, supported by teachers, randomized evaluation | About 0.3 standard deviations, which the team equates to roughly two years of typical learning |
| MIT Media Lab, "Your Brain on ChatGPT" ([2025, preprint](https://arxiv.org/abs/2506.08872)) | 54 university students writing essays in three groups: LLM, search engine, no tools | After the first essay, more than 80% of the LLM group could not accurately quote a sentence they had just written; the weakest brain connectivity |

Anthropic's experiment also compared ways of using AI. People who handed the code over entirely, relied on AI more and more, or let AI debug for them averaged below 40% on the quiz. People who asked only conceptual questions and fixed errors themselves, asked for code together with explanations, or generated code and then asked "why" averaged 65% or more. The conceptual-questions group was also the second fastest.

Two ways to use it:

| Situation | Crutch | Coach |
| --- | --- | --- |
| **When stuck** | Ask for the answer | Ask for the smallest hint |
| **After getting a solution** | Stop once it makes sense | Close the AI and redo it from scratch |
| **Homework** | Let it write | Write it yourself and let it find errors |
| **Checking whether you learned it** | "I feel like I get it" | Test yourself without AI |
| **Result** | Smooth practice, empty skill | Slower, but you learn it |

**About the evidence:** these studies differ in sample, subject, and setting. The MIT study is a small preprint, and Anthropic's experiment measured understanding right after the task. They do not prove that "AI makes people dumber", but they point the same way: what you did not do yourself rarely sticks. A well-designed AI tutor guides step by step, withholds the answer, and asks you to redo the work. The roles and prompts below follow that design.

## 3. Define the learning outcome before you start

A vague topic cannot be planned. A concrete deadline, use, and form of assessment let the plan fit what you need.

**Example:** "In three weeks I have a timed Python coding interview. I know basic Python, and it will be live coding." That is far easier to plan for than "I want to learn coding."

## 4. Ten roles for AI in learning

Give the AI a clear role aimed at your current learning problem and it works much better. The ten roles below come from notes on the video How to Use AI to Learn Anything Faster.

| # | Role | When to use it | The AI's job | Your job |
| --- | --- | --- | --- | --- |
| 1 | **Interviewer** | You do not know where to start | Ask about goals, prior knowledge, constraints, and gaps | Give specific answers |
| 2 | **Mapmaker** | The topic is broad and shapeless | Build a syllabus with prerequisites and priorities | Follow the route and adjust |
| 3 | **Explainer** | Stuck on one concept | Clear only that obstacle | Redo it once without help |
| 4 | **Socratic Questioner** | You think you understand | Expose hidden gaps with questions | Reason your way to the answer |
| 5 | **Examiner** | You want to measure understanding | Raise difficulty step by step and assess answers | Answer without hints |
| 6 | **Checker** | You have finished a piece of work | Check the process, reasoning, and output for errors | Make the corrections yourself |
| 7 | **Listener** | You want to explain the topic back | Compare your explanation with the source | Speak, write, or draw from memory |
| 8 | **Diagnostician** | You keep making similar mistakes | Find the misconception that recurs across examples | Repair the underlying concept |
| 9 | **Sparring Partner** | Preparing a real-world skill | Simulate interviews, negotiations, sales calls | Practice real responses under constraints |
| 10 | **Clerk** | Notes and records are a mess | Organize notes and make review material | Check accuracy and review actively |

### Interviewer: diagnose before teaching

Before asking AI to teach, have it ask you questions. That separates the broad topic from the performance you actually need.

```text
Before teaching me [subject], interview me one question at a time about my objective, deadline, current knowledge, constraints, and how I will be tested. Identify what I already know and what I need to learn. Do not begin teaching until the assessment is complete.
```

### Mapmaker: build a roadmap

Break a broad topic into smaller concepts, dependencies, common sticking points, and exercises.

```text
Based on my goal and current level, map [subject] into a practical learning sequence. Include prerequisites, the most important subtopics, likely stumbling blocks, and a concrete exercise for each stage. Prioritize only what is necessary for my goal.
```

### Explainer: targeted help

After getting help on the hard step, go back to the start and redo the whole task on your own.

```text
I am trying to [task]. I got stuck at [specific step]. Explain only that part at my current level. Give a hint before a full solution. Afterward, remind me to repeat the whole task without your help.
```

### Socratic Questioner: find the gaps yourself

Use questions to expose assumptions and holes in understanding, so you find the answer yourself.

```text
Act as a Socratic tutor for [topic]. Ask one probing question at a time. Do not immediately reveal the answer. Use follow-up questions to help me find weaknesses in my reasoning.
```

### Examiner: measure what you can actually do

Raise the difficulty step by step until you reach a question you cannot answer.

```text
Quiz me on [topic], one question at a time. Start easy and gradually increase difficulty. Do not reveal the answer before I respond. Identify the highest level I can handle consistently and summarize the gaps I need to address.
```

### Checker: check the reasoning, not only the result

Check the intermediate steps and reasoning. The point is to understand why the work is right or wrong, and whether there is a more efficient approach.

```text
Here is my work: [paste work]. Check my reasoning and intermediate steps. Identify mistakes, omissions, and any simpler approach. Do not rewrite the entire solution; explain what I should improve and let me fix it.
```

### Listener: teach it back

Show understanding in several forms: speaking, writing, drawing. AI can compare these attempts with the source material.

```text
I will explain [topic] in my own words. Compare my explanation against [source material]. Tell me which points are correct, incomplete, or inaccurate. Do not treat confident wording as proof of understanding.
```

### Diagnostician: find the recurring root cause

When the same mistake keeps coming back, look at several examples together. Errors on different topics may come from the same missing foundation.

```text
Here are several mistakes from my recent practice: [paste mistakes and corrections]. Look for a recurring misconception or reasoning error. Distinguish clear patterns from guesses, then suggest the smallest exercise that would test and repair the underlying gap.
```

**A practical limit:** AI can analyze only the conversations and error logs you provide or that are available in the current context. Do not assume it can automatically and reliably review all your past conversations.

### Sparring Partner: rehearse real situations

Simulate the tasks you will actually face, including the difficulty, time limits, and tough feedback.

```text
Role-play a demanding [interviewer/client/negotiator]. My objective is [outcome]. Ask one realistic question at a time, challenge vague answers, and require concrete examples. Evaluate each response against the expectations of the real situation.
```

### Clerk: organize, but do not outsource the thinking

Use AI to organize notes, pull out mistakes, and make flashcards; keep the thinking for yourself.

```text
Turn these rough notes into a clean hierarchical outline. Preserve my meaning. Do not add unsupported facts. Separate key ideas, examples, uncertainties, and action items. Then create flashcards from the concepts I got wrong.
```

## 5. Learn from projects and avoid tutorial hell

Endless passive learning is **tutorial hell**. A real project gives you a reason to learn and a way to test advice. Follow something like an apprenticeship:

1. Pick a meaningful goal.
2. Start before you know every step.
3. Notice which knowledge gaps block progress.
4. Get targeted guidance from books, mentors, videos, or AI.
5. Apply what you learned right away.
6. Evaluate the result, then repeat.

Learning AI itself works the same way: use the leading models, build real projects, automate workflows, use AI as a tutor, and watch output quality and time saved.

## 6. When not to use AI

AI can remove the struggle that makes practice valuable. Deliberately skip AI when you are:

* Attempting a problem for the first time.
* Retrieving something from memory.
* Proving you can do a task on your own.
* Testing whether you understand the order of the reasoning.

Use AI afterwards for feedback, diagnosis, or a targeted explanation.

The learning scientist Robert Bjork calls effortful practices that are remembered longer, such as self-testing, spaced review, and interleaving, **desirable difficulties**. AI makes it easy to remove all of them.

In Anthropic's December 2025 internal study (132 engineers and researchers surveyed), engineers described a **paradox of supervision**: using AI well requires being able to supervise it, and the skills supervision needs are the ones most likely to wither with heavy reliance on AI ([Anthropic](https://www.anthropic.com/research/how-ai-is-transforming-work-at-anthropic)). Some engineers deliberately practice without AI to keep their skills.

## 7. Common traps and fixes

| Avoid | Do instead |
| --- | --- |
| Stopping once you have the explanation | Do one independent recall or application task |
| Letting AI solve the whole problem | Ask only for the smallest hint you need, then continue |
| Starting from a vague topic | Set a concrete outcome and deadline |
| Taking notes endlessly | Produce answers, explanations, and work |
| Staying on easy questions | Raise the difficulty and find your limit |
| Treating each mistake separately | Look for the shared underlying misconception |
| Trusting AI's judgment without question | Check important claims against the source or a reliable reference |
| Building an elaborate review system before learning | Finish one real task first, then organize the results |

## 8. Master Learning Coach prompt

Copy it into a new AI conversation and fill in the brackets:

```text
Act as my AI learning coach.

Your objective is to develop my independent ability to understand, remember, explain, and apply the subject—not simply give me answers.

Subject: [SUBJECT]
My measurable goal: [OUTCOME]
Deadline: [DATE]
Current knowledge: [WHAT I ALREADY KNOW]
How I will apply/test it: [REAL TASK OR ASSESSMENT]

Use these roles as needed:

1. INTERVIEWER — Ask one question at a time to assess my starting level, goals, constraints, and knowledge gaps.
2. MAPMAKER — Build a focused roadmap with prerequisites and practice tasks.
3. SOCRATIC QUESTIONER — Ask questions that reveal weak reasoning without immediately showing the answer.
4. EXPLAINER — When I get stuck, provide the smallest useful hint or explanation rather than completing the entire task.
5. EXAMINER — Test me with progressively harder questions, one at a time.
6. CHECKER — Review my reasoning and deliverables; let me make corrections.
7. LISTENER — Compare explanations in my own words against source material.
8. DIAGNOSTICIAN — Identify repeated mistakes from the evidence I provide.
9. SPARRING PARTNER — Simulate realistic scenarios and challenge my responses.
10. CLERK — Organize notes, mistake logs, and flashcards without adding unsupported material.

Rules:

- Prioritize active recall and practical application.
- Don't equate my feeling of understanding with demonstrated competence.
- Let me attempt tasks before providing solutions.
- After helping, ask me to repeat the original task without assistance.
- Keep challenges slightly beyond my demonstrated level.
- Distinguish verified facts from uncertain conclusions.
- Keep a running list of mistakes and revisit weak areas.
- Ask one question at a time during assessment and practice.

Start by interviewing me about my goal and current level.
```

ChatGPT's Study Mode, Gemini's Guided Learning, and Claude's learning mode also guide rather than hand over answers. They do not know your goal, deadline, or how you will be tested, so fill in the first lines of this prompt and paste it in for better results.

## 9. Spaced repetition: a review schedule

These intervals are a **starting template**; adjust them to how well you actually recall.

| When | Action | Check |
| --- | --- | --- |
| **Day 0** | Learn and recall immediately | Can you explain or do it without notes? |
| **Day 1** | Recall first, then reread | Which details can you write out on your own? |
| **Day 3** | Test weak spots | Can you fix earlier mistakes? |
| **Day 7** | Apply to a new problem | Can you transfer the concept to a new example? |
| **Day 14** | Retention test | Can you still explain the core principle? |
| **Day 30** | Long-term review | What is stable? What still needs practice? |

**Rule:** if recall is easy and correct, lengthen the interval; if it fails, go back to the prerequisite concepts and review sooner.

A prompt for making flashcards:

```text
Create 5–10 short, answerable flashcards from my error log. Prefer questions that require me to recall or apply an idea, not recognize a definition. Show the question and answer separately. Do not invent missing source facts.
```

## 10. The measure

> **AI-assisted learning succeeds when you can reliably do the thing without AI.**

---

[← AI Fundamentals](01-ai-fundamentals.md) · [Part 4: Learn and Think](README.md) · [Contents](../../README.md#contents) · [Thinking with AI →](03-thinking-with-ai.md)
