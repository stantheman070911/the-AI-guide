[目錄](../../README.zh-TW.md#目錄) › [第四部：學習與思考](README.md) · [English](../../en/part-4-learn-think/02-learning-with-ai.md) | **繁體中文**

# 用 AI 學習

以 active production 為核心，用研究證據把 AI 變成學習教練。

> 最後查證：2026-10-13。

> **原文語言**：繁體中文。這是原文；[英文版](../../en/part-4-learn-think/02-learning-with-ai.md)為翻譯。兩者不一致時，以本中文原文為準。

## 1. 核心原則：Active production

用 AI 提升自己思考、練習、回想與產出的能力，這些活動仍要自己做。

| Passive consumption（被動吸收） | Active production（主動產出） |
| --- | --- |
| 閱讀或重讀材料 | 憑記憶回想內容 |
| 看影片 | 用自己的話解釋概念 |
| 閱讀 AI 生成的解說 | 在沒有協助下回答問題 |
| 收集筆記 | 解題並應用知識 |

被動吸收會製造「好像懂了」的感覺；主動產出才檢驗你能否提取並使用資訊。核心流程如下：

> **Attempt → 取得針對性回饋 → 修正錯誤 → 獨立重做 → 憑記憶測試 → 隔段時間複習**

Roediger 與 Karpicke（2006）發表於 Psychological Science 的實驗（[APS](https://www.psychologicalscience.org/observer/test-enhanced-learning)）：

| 方法 | 5 分鐘後回想 | 1 週後回想 |
| --- | --- | --- |
| 重讀材料四次 | 83% | 40% |
| 讀一次、測驗三次 | 71% | 61% |

重讀組 5 分鐘後記得較多，一週後被測驗組超越。讀 AI 寫的漂亮解說，效果接近重讀。

## 2. 研究證據：用法決定學習效果

近兩年關於「用 AI 學習」的研究，結論相當一致：AI 可能加快學習，也可能削弱學習，取決於用法與設計。

| 研究 | 設計 | 主要發現 |
| --- | --- | --- |
| 土耳其高中數學（[Bastani et al., PNAS 2025](https://papers.ssrn.com/abstract=4895486)） | 近 1,000 名高中生；直接給答案的 GPT Base，對照只給提示、由老師參與設計的 GPT Tutor | 練習時 Base 組比對照組好 48%、Tutor 組好 127%；拿掉 AI 考試時，Base 組差 17%，Tutor 組與對照組相當 |
| Anthropic 程式技能實驗（[2026 年 1 月](https://www.anthropic.com/news/AI-assistance-coding-skills)） | 52 位（多為資淺）工程師學習陌生的 Python 函式庫 Trio，隨機分組 | 用 AI 組測驗平均 50%，自己動手組 67%；AI 組沒有明顯較快；差距最大在 debug 題 |
| Harvard 物理 AI 家教（[Kestin et al., Scientific Reports 2025](https://www.nature.com/articles/s41598-025-97652-6)） | 194 名學生；在家使用精心設計的 AI tutor，對照課堂 active learning | 學習進步幅度超過課堂的兩倍；中位數只花 49 分鐘 |
| World Bank 奈及利亞課後輔導（[2024](https://blogs.worldbank.org/en/education/From-chalkboards-to-chatbots-Transforming-learning-in-Nigeria)） | 6 週，老師陪同使用 GPT-4 學英文，隨機評估 | 約 0.3 個標準差，研究團隊換算約等於兩年的一般學習進度 |
| MIT Media Lab「Your Brain on ChatGPT」（[2025，預印本](https://arxiv.org/abs/2506.08872)） | 54 名大學生寫作文：用 LLM、用搜尋引擎、只靠自己三組 | 第一次寫完後，LLM 組超過八成無法準確引用自己剛寫的句子；腦部連結性最弱 |

Anthropic 的實驗也比較了用法：把程式整個交給 AI、逐漸完全依賴、讓 AI 代為 debug 的人，測驗平均低於 40%；只問概念並自己修錯、要程式碼也要解釋、先生成再追問「為什麼」的人，平均在 65% 以上，其中只問概念的一組速度也是第二快。

整理成兩種用法：

| 情境 | 拐杖 Crutch | 教練 Coach |
| --- | --- | --- |
| **卡住的時候** | 要答案 | 要最小的提示 |
| **拿到解法之後** | 看懂就停 | 關掉 AI，自己從頭重做一次 |
| **寫作業** | 讓它寫 | 自己寫，讓它挑錯 |
| **判斷學會沒** | 「我感覺懂了」 | 不靠 AI，考自己 |
| **結果** | 練習很順，實力是空的 | 慢一點，但學得會 |

**證據說明**：這些研究的樣本、學科與情境各不相同；MIT 研究是小樣本預印本，Anthropic 實驗量的是完成當下的理解。它們不足以證明「AI 會讓人變笨」，但方向一致：自己沒出力的部分，很難留下來。設計得好的 AI 家教會一步步引導、不直接給答案、要求重做；接下來的角色與 prompt 就是這種設計。

## 3. 先定義學習成果，再開始學

模糊的主題無法規劃。具體的期限、用途與評量方式，才能讓學習計畫切中需要。

**例子**：「三週後有一場限時 Python coding interview。我會基礎 Python，評量方式是 live coding。」這比「我想學 coding」好規劃得多。

## 4. AI 在學習中的十種角色

給 AI 一個明確角色，對準你當下的學習問題，效果會好很多。以下十種角色整理自影片筆記 How to Use AI to Learn Anything Faster。

| # | Role | 何時使用 | AI 的工作 | 你的工作 |
| --- | --- | --- | --- | --- |
| 1 | **Interviewer** | 不知從何開始 | 詢問目標、先備知識、限制與缺口 | 給具體回答 |
| 2 | **Mapmaker** | 主題廣泛、沒有輪廓 | 建立含先備條件與優先順序的課綱 | 依路線前進並調整 |
| 3 | **Explainer** | 卡在某個概念 | 只釐清那個障礙 | 不靠協助重做一次 |
| 4 | **Socratic Questioner** | 自以為懂了 | 用提問揭露隱藏的缺口 | 自己推理出答案 |
| 5 | **Examiner** | 想衡量理解程度 | 逐步加深難度並評估回答 | 不看提示作答 |
| 6 | **Checker** | 已完成作品 | 檢查過程、推理與產出的錯誤 | 自己修改 |
| 7 | **Listener** | 想把主題講回來 | 比對你的解釋與原始資料 | 口說、書寫或憑記憶畫圖 |
| 8 | **Diagnostician** | 一再犯類似錯誤 | 找出跨例子的反覆誤解 | 修補底層概念 |
| 9 | **Sparring Partner** | 準備實戰技能 | 模擬面試、談判、銷售電話等 | 在限制下練習真實回應 |
| 10 | **Clerk** | 筆記與紀錄雜亂 | 整理筆記、製作複習材料 | 核對正確性並主動複習 |

### Interviewer：先診斷，再學習

在要求 AI 上課之前，先讓它問你問題，把廣泛的主題和實際要達成的表現目標分開。

```text
Before teaching me [subject], interview me one question at a time about my objective, deadline, current knowledge, constraints, and how I will be tested. Identify what I already know and what I need to learn. Do not begin teaching until the assessment is complete.
```

### Mapmaker：建立路線圖

把廣泛主題拆成較小的概念、依賴關係、常見卡點與練習。

```text
Based on my goal and current level, map [subject] into a practical learning sequence. Include prerequisites, the most important subtopics, likely stumbling blocks, and a concrete exercise for each stage. Prioritize only what is necessary for my goal.
```

### Explainer：針對性協助

在困難步驟得到幫助後，回到起點，獨立重做整個任務。

```text
I am trying to [task]. I got stuck at [specific step]. Explain only that part at my current level. Give a hint before a full solution. Afterward, remind me to repeat the whole task without your help.
```

### Socratic Questioner：自己發現缺口

用提問揭露假設與理解上的漏洞，讓自己找出答案。

```text
Act as a Socratic tutor for [topic]. Ask one probing question at a time. Do not immediately reveal the answer. Use follow-up questions to help me find weaknesses in my reasoning.
```

### Examiner：衡量實際能力

逐步提高難度，直到碰到你不會的那一題。

```text
Quiz me on [topic], one question at a time. Start easy and gradually increase difficulty. Do not reveal the answer before I respond. Identify the highest level I can handle consistently and summarize the gaps I need to address.
```

### Checker：檢查推理，不只看結果

檢查中間步驟與推理。目的是理解作品「為什麼」對或錯，以及有沒有更有效率的做法。

```text
Here is my work: [paste work]. Check my reasoning and intermediate steps. Identify mistakes, omissions, and any simpler approach. Do not rewrite the entire solution; explain what I should improve and let me fix it.
```

### Listener：教回去

用多種形式證明理解：口說、書寫、視覺化。AI 可以把這些嘗試與原始資料比對。

```text
I will explain [topic] in my own words. Compare my explanation against [source material]. Tell me which points are correct, incomplete, or inaccurate. Do not treat confident wording as proof of understanding.
```

### Diagnostician：找出反覆出現的根因

錯誤一再出現時，把多個例子放在一起看。不同主題的錯誤，可能源自同一個缺漏的基礎概念。

```text
Here are several mistakes from my recent practice: [paste mistakes and corrections]. Look for a recurring misconception or reasoning error. Distinguish clear patterns from guesses, then suggest the smallest exercise that would test and repair the underlying gap.
```

**實際限制**：AI 能分析的，是你提供的、或目前 context 中可存取的對話與錯誤紀錄。不要假設它能自動、可靠地檢視所有過去的對話。

### Sparring Partner：演練真實情境

模擬實際會遇到的任務，包括難度、時間限制與嚴格回饋。

```text
Role-play a demanding [interviewer/client/negotiator]. My objective is [outcome]. Ask one realistic question at a time, challenge vague answers, and require concrete examples. Evaluate each response against the expectations of the real situation.
```

### Clerk：整理，但不外包思考

用 AI 整理筆記、擷取錯誤、製作 flashcards；思考的工作留給自己。

```text
Turn these rough notes into a clean hierarchical outline. Preserve my meaning. Do not add unsupported facts. Separate key ideas, examples, uncertainties, and action items. Then create flashcards from the concepts I got wrong.
```

## 5. 從專案中學，避開 tutorial hell

無止境的被動學習，就是 **tutorial hell**。一個真實的專案，給你學習的理由，也給你檢驗建議的方法。建議採取類似學徒制的順序：

1. 選一個有意義的目標。
2. 在還不清楚每一步之前，就開始做。
3. 注意哪些知識缺口卡住了進度。
4. 從書、mentor、影片或 AI 找針對性的指引。
5. 立刻應用所學。
6. 評估結果，然後重複。

學 AI 本身也一樣：實際使用領先的模型、做真實專案、把工作流自動化、把 AI 當 tutor，關注產出品質與節省的時間。

## 6. 何時不該用 AI

AI 可能拿走讓練習有價值的那份掙扎。以下情況，刻意不用 AI：

* 第一次嘗試解一個問題。
* 憑記憶提取內容。
* 證明自己能獨立完成任務。
* 測試自己是否理解推理的順序。

之後再用 AI 取得回饋、診斷或針對性的解說。

學習科學家 Robert Bjork 把自我測驗、間隔複習、交錯練習這類比較吃力、卻記得比較久的做法，稱為 **desirable difficulties（有益的困難）**。AI 很容易把這些困難全部拿走。

Anthropic 2025 年 12 月的內部研究（訪問 132 位工程師與研究員）中，工程師點出一個 **paradox of supervision（監督的悖論）**：要有效使用 AI，就得能監督它；而監督所需的技能，恰好是過度依賴 AI 時最可能退化的那些（[Anthropic](https://www.anthropic.com/research/how-ai-is-transforming-work-at-anthropic)）。因此有工程師刻意不用 AI 練習，保持手感。

## 7. 常見陷阱與修正

| 避免 | 改為 |
| --- | --- |
| 要了解說就停在那裡 | 做一次獨立回想或應用任務 |
| 讓 AI 解完整個問題 | 只要求最小的必要提示，然後繼續 |
| 從模糊的主題開始 | 設定具體成果與期限 |
| 無止境地做筆記 | 產出答案、解釋與成果 |
| 停留在簡單題 | 提高難度，找出自己的極限 |
| 把每個錯誤分開處理 | 尋找共同的底層誤解 |
| 不加質疑地相信 AI 的判斷 | 用原始資料或可靠來源核對重要說法 |
| 學習前先打造繁複的複習系統 | 先完成一個真實任務，再整理結果 |

## 8. Master Learning Coach Prompt

複製到新的 AI 對話，填入方括號內容：

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

ChatGPT 的 Study Mode、Gemini 的 Guided Learning 與 Claude 的 Learning 模式，也都採用引導、不直接給答案的做法。它們不知道你的目標、期限與考法，先填好這份 prompt 的前幾行再貼上，效果較好。

## 9. Spaced repetition：複習排程

以下間隔是**起始範本**，依實際回想表現調整。

| 時間 | 行動 | 成功檢查 |
| --- | --- | --- |
| **Day 0** | 學習並立即回想 | 不看筆記能解釋或做到嗎？ |
| **Day 1** | 先回想，再重讀 | 哪些細節能獨立寫出？ |
| **Day 3** | 測試弱點 | 能修正之前的錯誤嗎？ |
| **Day 7** | 套用到新問題 | 能把概念遷移到新例子嗎？ |
| **Day 14** | 保留測試 | 還能解釋核心原則嗎？ |
| **Day 30** | 長期複習 | 哪些已穩定？哪些還要練？ |

**規則**：回想輕鬆又正確，就拉長間隔；回想失敗，就回到先備概念，提早複習。

製作 flashcards 的 prompt：

```text
Create 5–10 short, answerable flashcards from my error log. Prefer questions that require me to recall or apply an idea, not recognize a definition. Show the question and answer separately. Do not invent missing source facts.
```

## 10. 衡量標準

> **衡量 AI 輔助學習成不成功，看的是你不靠 AI 能可靠地做到什麼。**

---

[← AI 基礎](01-ai-fundamentals.md) · [第四部：學習與思考](README.md) · [目錄](../../README.zh-TW.md#目錄) · [用 AI 思考 →](03-thinking-with-ai.md)
