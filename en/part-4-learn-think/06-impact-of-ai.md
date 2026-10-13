[Contents](../../README.md#contents) › [Part 4: Learn and Think](README.md) · **English** | [繁體中文](../../zh-TW/part-4-learn-think/06-impact-of-ai.md)

# The Impact of AI

What AI changes for work, new hires, startups, society, academic integrity, and data security.

> Last verified: 2026-10-13.

> **Original language:** Traditional Chinese. This English version is a translation. If the two versions disagree, the [Chinese original](../../zh-TW/part-4-learn-think/06-impact-of-ai.md) is authoritative.

## 1. Look at work task by task

"Will AI replace us?" is too big a question. A job includes understanding context, coordinating with people, making decisions, doing repetitive tasks, and taking responsibility. AI can take over some of those tasks without the whole job disappearing.

What AI changes directly today is the individual tasks within a job. Much workplace context is hard to write down and still depends on human judgment and communication. When a process is badly designed, AI can even add checking, rework, and management overhead.

## 2. Team cases: how AI changed different departments

Anthropic has published how ten of its internal teams use Claude Code ([Anthropic](https://www-cdn.anthropic.com/58284b19e702b49db9302d5b6f135ad8871e7658.pdf)). The figures below are self-reported by the vendor and have not been independently verified.

| Team or area | Experience |
| --- | --- |
| Security | Infrastructure problems that took 10 to 15 minutes resolve about three times as fast |
| Inference | Research time cut by about 80% |
| Growth marketing | Ad copy that took about 2 hours now takes 15 minutes |
| Product design | Work that took a week of coordination became two 30-minute calls |
| Legal | With no engineering background, built a speech-assistance app for a family member with speaking difficulties in about an hour |
| Data science | A member with almost no TypeScript built an analytics app of about 5,000 lines |
| Growth marketing | Built an ad pipeline from two specialized sub-agents; creative output rose about tenfold |
| Finance | Wrote the rules in plain-text files and had AI help carry out the process |

The shared direction in these cases is turning individual know-how into explicit, reusable documents. Some teams tell the AI about themselves first, for example "I'm a designer and not much of a programmer; explain clearly and change one small thing at a time." Others write the AI's common mistakes into rules to improve consistency over time.

In December 2025 Anthropic also published an internal study surveying 132 engineers and researchers. Respondents estimated they used Claude in about 59% of their work (about 28% a year earlier) and that it raised their output by about 50% (about 20% a year earlier). About 27% of the work done with Claude would not have been done without AI, such as small side tools and exploratory projects ([Anthropic](https://www.anthropic.com/research/how-ai-is-transforming-work-at-anthropic)).

## 3. Productivity gains still need checking

The same cases have limits. The reinforcement learning engineering team said AI gets it right on the first try about a third of the time; it sometimes puts comments in odd places, and its code organization is not always sound.

So the speed of one generation cannot be converted straight into headcount. Count the cost of review, testing, fixes, integration, and retries. None of the ten teams took people out of the process; what they discussed was how to write better rules, how to divide oversight, and where to apply judgment to the output.

In the same internal study, more than half of respondents said they could fully hand off only 0–20% of their work to AI.

## 4. Collaboration changes, and so does the path for new hires

AI lets people try first on work that used to require finding someone who knew: understanding code, handling simple problems, finding documentation, building prototypes, or working out possible solutions before asking a colleague on Slack. Sometimes what gets replaced is the step of having to ask another person first.

In Anthropic's internal study, one engineer said 80–90% of their questions now go to Claude first. Senior engineers observed that junior colleagues ask fewer questions and learn faster, but that the traditional ways of mentoring and collaborating are changing.

The tasks easiest to hand to AI are the ones new hires used to build their skills on: reading a codebase, writing unit tests, simple refactors, looking up documentation. New hires get up to speed faster, but may miss the chance to practice judgment through basic work.

The value of professional work will concentrate further in defining problems, understanding situations, setting standards, weighing options, and being accountable for results.

Early employment data already shows a signal. Erik Brynjolfsson and colleagues at the Stanford Digital Economy Lab track ADP payroll data in *Canaries in the Coal Mine?*. For 22–25-year-olds in highly AI-exposed occupations, the employment gap relative to peers in less-exposed occupations widened from about 13% in the first version (August 2025) to about 19% in the August 2026 update ([Stanford Digital Economy Lab](https://digitaleconomy.stanford.edu/news/canariesaug26/)). The decline comes mainly from reduced hiring and is concentrated in jobs heavy in codified knowledge. Experienced workers in the same occupations, whose judgment rests on tacit knowledge, show no similar decline.

These data show correlation only. Students and new hires can deliberately build the abilities that cannot be written down: real projects, feedback from real people, and actual collaboration.

## 5. The average loses value; expertise gains leverage

Naval Ravikant argues that AI lets an individual do work that once took a whole team, widening what one person can do ([Naval](https://nav.al/ai)).

How much it amplifies depends on where you start. In the cases in [§2](#2-team-cases-how-ai-changed-different-departments), a lawyer with no programming background built an app in about an hour, and the marketing team's creative output rose about tenfold; senior engineers solved infrastructure problems about three times as fast. Experts still have value, but the gap between them and everyone else has narrowed.

In Naval's words, "there is no demand for average": once acceptable work is abundant, mediocre products and easily copied services lose value, and excellent products and specialized solutions matter more.

He repeats his old advice: "Become the best in the world at what you do." Deep expertise plus AI can let an individual outperform much larger teams.

AI also lowers the cost of starting a business. Naval stresses agency: people who find opportunities, make decisions, and own the results find it easier to turn ideas into businesses.

## 6. The one-human business

> **Expertise and experience → Content and distribution → Product or service → Revenue and feedback**

* **Expertise:** knowing or discovering something that can help others.
* **Distribution:** publishing useful work where the target audience can find it.
* **Offer:** packaging the solution as a product or service.
* **Iteration:** listening to users, improving the solution, refining the offer.

"Creator" here is broad: someone who makes useful things, not necessarily an influencer. AI can handle part of the research, production, administration, and technical execution; the person is responsible for running the whole. Content is the way to reach an audience, and published work and thinking are the evidence of your ability.

## 7. How startup teams actually use AI

Startups have limited resources. AI's value is in lowering the cost of experiments and shortening some steps of execution, so a small team sees testable results sooner. There are four kinds of use:

### Marketing: faster content and marketing experiments

AI can help with draft copy, email campaigns, SEO content, and ad assets, shortening the path from idea to first draft. Whether it works still depends on real conversions and audience response.

### Product: working prototypes in place of abstract discussion

Give AI a design and have it help build a working prototype, then discuss requirements and problems around it. The prototype is for communication and validation; the real product still has to be built separately.

### Operations: small processes standard software does not fit

When no SaaS product fits an internal process, AI-assisted development lowers the cost of building a small tool yourself. Whether it is worth building still depends on maintenance cost, data security, permissions, and stability.

### Decisions: clarify risks before irreversible choices

AI can help list likely consequences, objections, and unconfirmed assumptions; it is especially useful for a pre-mortem before a major decision. The final decision is still made by the person responsible.

Across all four, the shared practice is keeping a record of every experiment: what was tested, on what basis, what happened, and what to change next time. That is how one-off output accumulates into organizational knowledge.

When selling AI products to enterprise customers, security review, permissions, and data-handling requirements are often the main barrier to adoption.

## 8. Academic integrity: follow the specific rules first

AI can be a learning tool, and it can also go beyond the help a course allows. Student guidelines at schools such as Stanford, Harvard, and Oxford suggest these conservative working principles:

* If the teacher or course has not explicitly allowed a use, do not assume AI may write the work for you.
* In assignments, tests, or exams that forbid outside help, do not let AI substantially do the assessed part in your place.
* Disclose AI use as the course requires; when unsure, ask or explain.
* When disclosing, say at which stages AI was used and what it did.
* Whether or not you used AI, the person submitting is responsible for the accuracy, quality, and citations of the content.

Local rules are moving the same way. Taipei City's guidelines for students' use of generative AI in schools below university level require that AI-generated content be marked in the text, and that students judge and verify its accuracy themselves and avoid over-reliance ([Taipei City Department of Education](https://www.lssh.tp.edu.tw/wp-content/uploads/doc/ls801/%E8%87%BA%E5%8C%97%E5%B8%82%E9%AB%98%E7%B4%9A%E4%B8%AD%E7%AD%89%E4%BB%A5%E4%B8%8B%E5%AD%B8%E6%A0%A1%E7%94%9F%E6%88%90%E5%BC%8F%20AI%20%E5%B7%A5%E5%85%B7%E8%BC%94%E5%8A%A9%E5%AD%B8%E7%94%9F%E5%AD%B8%E7%BF%92%E6%8C%87%E5%BC%95.pdf), in Chinese). A disclosure can be specific, for example:

> This report used ChatGPT to help summarize the literature and check grammar. All arguments, citations, and conclusions were written and verified by me.

## 9. Data security and responsibility

High-risk data includes names, addresses, ID numbers, medical records, financial information, confidential work documents, and unpublished research. Before handling it, ask: what classification is this data? Is this tool approved to touch it?

1. Do not paste confidential, personal, or restricted data into public or unapproved AI services.
2. Where your school or company has approved services, use them first, and check the applicable contract, data-use terms, and settings. An enterprise plan does not mean every risk is gone.
3. Provide only the data the task needs, and grant no more access than necessary.
4. Agents that need access to sensitive systems should use connections with access control, not open access to the whole machine or every account.
5. If data is sent to the wrong place or accessed without authorization, report and handle it at once under your organization's rules. Do not cover it up.

**Who is ultimately responsible?** Even when AI organized the data and drafted the content, the person who submits, publishes, or acts on the result must confirm that it is appropriate and lawful.

## 10. Society: risk, trust, and the long view

At the scale of society, at least four questions still have no settled answer:

* **Education:** when AI can do the homework, what should schools teach and test? Stanford HAI's *AI Index 2026* reports that about four in five US high school and university students use AI for schoolwork; about half of middle and high schools have an AI policy, and only 6% of teachers say those policies are clear ([Stanford HAI](https://hai.stanford.edu/ai-index/2026-ai-index-report/education)).
* **Work:** entry-level jobs are shrinking, and entry-level jobs are where most people build experience and judgment (see [§4](#4-collaboration-changes-and-so-does-the-path-for-new-hires)). Where will the next generation of experts come from?
* **Trust:** when text, images, and video can all be generated at scale, what deserves belief? An AP-NORC poll released in October 2026 found that 64% of US adults think AI is developing too fast ([AP](https://www.ksat.com/news/politics/2026/10/08/most-americans-think-artificial-intelligence-is-developing-too-fast-a-new-ap-norc-poll-finds/)).
* **Power and safety:** who controls the compute, the data, and the permissions agents can use?

Naval's view is that people misusing AI is more worrying than AI developing harmful intent of its own. Over the long run, AI and robotics may lower costs and increase abundance, freeing people from repetitive work; automating the physical world is still hard.

## 11. Start today

A set of practices you can upgrade step by step:

1. **Pick one real need.** Confirm the problem is worth solving; do not invent work in order to use AI.
2. **Get good at one tool.** Start with the tasks you do most and whose risk you can control.
3. **Organize your own material.** Build maintainable Markdown documents, project notes, decision records, and templates.
4. **Hand off clear tasks.** State the outcome, context, constraints, format, and completion criteria.
5. **Check the output.** Verify sources, run tests, and when needed ask another model for objections.
6. **Write the steps that work into an SOP or skill.** Record why things failed and what made them succeed.
7. **Automate once it is stable.** Increase an agent's permissions step by step, according to risk.

Do not be quick to assume AI cannot do something. Ask whether it can, what material it needs, and what its limits are, then run a small experiment to confirm it can deliver reliably, correctly, and safely.

---

[← Living with AI](05-living-with-ai.md) · [Part 4: Learn and Think](README.md) · [Contents](../../README.md#contents) · [Appendix A: Core Writing Principles →](../appendix/01-writing-principles.md)
