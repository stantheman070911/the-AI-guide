[目錄](../../README.zh-TW.md#目錄) › [第四部：學習與思考](README.md) · [English](../../en/part-4-learn-think/01-ai-fundamentals.md) | **繁體中文**

# AI 基礎

先決定做什麼；再理解模型、context、tools 與 agent。本章是第四部其他各章的共同基礎，適合第一次認真使用 AI 的讀者。

> 最後查證：2026-10-13。

> **原文語言**：繁體中文。這是原文；[英文版](../../en/part-4-learn-think/01-ai-fundamentals.md)為翻譯。兩者不一致時，以本中文原文為準。

## 1. 先決定要做什麼，再決定要不要用 AI

AI 的價值，在於讓**值得做的事情**更容易完成。

> **There is nothing so useless as doing efficiently that which should not be done at all.**
>
> 沒有什麼比高效率地完成一件根本不該做的事，更加徒勞。
>
> ——Peter Drucker（[Harvard Business Review, 1963](https://hbr.org/1963/05/managing-for-business-effectiveness)）

常見的誤區，是先看到 AI 能做什麼，再替它找用途，結果把時間花在沒有需求的產品、不必要的流程，或只是看起來精巧的 automation 上。「很多 vibe coder 都做過記帳軟體」這句玩笑，說的就是同質化的練習作品。該先問的是：誰有什麼問題？需要什麼結果？AI 能否以合理的成本改善這個結果？

第四部可以用一個關係來理解：

> **Outcome × Context → 更精準的產出**

* **Outcome（預期結果）**：具體要交付什麼、給誰用、怎樣算完成。
* **Context（脈絡）**：任務背景、既有資料、限制條件、過去的決策，以及品質標準。
* **驗證與判斷**：結果是否符合目的，仍然由人負責。

用 AI 之前，先判斷任務是否需要推理與生成。規則固定、不需判斷的行政作業，用表格、模板或傳統 automation 更合適。把 AI 加進有缺陷的流程，只會讓錯誤發生得更快。

## 2. AI 的定位：a motorcycle for the mind

Naval Ravikant 把 AI 比作「心智的摩托車」，但仍要有人騎（[Naval](https://nav.al/ai)）：execution 變得便宜後，人的判斷就更有價值（見[用 AI 思考 §1](03-thinking-with-ai.md#1-當執行變得充裕判斷就是優勢)）。

AI 擅長 automation、coding 與資訊處理，但在獨立推理、對真實世界的理解與 agency（主動行事的能力）上仍有侷限，需要人的監督與判斷。

面對 AI，大致有三種姿態（整理自影片筆記 The Digital Renaissance）：

| 類型 | 行為 | 主要弱點 |
| --- | --- | --- |
| **Purist** | 拒絕 AI 與技術進步 | 錯失機會 |
| **Automaton / Cyborg** | 把思考與決策外包給技術 | 失去獨立判斷 |
| **Digital Renaissance Person** | 有選擇地使用 AI，同時培養自己的判斷與技能 | 建議採取的姿態 |

讓 AI 負責協助與執行；方向、品質與決策由自己負責。核心模型如下：

> **Human judgment + multidisciplinary skills + AI leverage = 獨立做出有價值作品的能力**

## 3. 先理解概念，再選工具

AI 工具更新很快，名稱、介面、定價與功能都會變。但模型如何使用 context、如何呼叫工具，以及人如何設定目標、檢查結果，這些基本問題更有延續性。掌握結構，才不必每換一次工具就從頭學起。

工具更新的速度，可以用一個例子感受：2026 年 9 月 22 日到 10 月 7 日之間，Anthropic 陸續推出 [Claude Opus 5.5](https://www.anthropic.com/news/claude-opus-5-5)、[Sonnet 5.5](https://www.anthropic.com/claude-sonnet-5-5) 與 [Haiku 5.5](https://www.anthropic.com/claude-haiku-5-5) 三個模型。

能力進步來自把模型做大，也來自推論階段投入的運算（inference-time compute）、後訓練（post-training），以及 agent 系統使用外部工具的方式。研究界對進展速度仍有分歧。

能力確實在快速增加。研究機構 **METR** 用「AI agent 能以 50% 成功率獨立完成、人類專家需要多久的任務」來追蹤進展：長期來看，這個任務長度大約每 7 個月翻倍一次，2024 年之後可能更快（[METR](https://metr.org/blog/2025-03-19-measuring-ai-ability-to-complete-long-tasks/)）。METR 估計，2026 年 2 至 3 月公開可用的前沿模型，在 50% 成功率下已能處理人類需時約 12 小時的任務，信賴區間是 5 到 61 小時（[METR](https://metr.org/blog/2026-05-19-frontier-risk-report/)）。

成功率要求越高，可交付的任務就越短：要求 80% 成功率時，任務長度會短好幾倍。METR 也指出，現行題庫對 16 小時以上的量測已不可靠，題目也以可自動評分的軟體任務為主；50% 成功率下能做 X 小時的任務，不代表 X 小時以內的任務都能放心交出去（[METR](https://metr.org/notes/2026-01-22-time-horizon-limitations/)）。

## 4. 基本名詞

| 名詞 | 實務上的意思 |
| --- | --- |
| **LLM（大型語言模型）** | 處理輸入、生成回應的核心模型；在許多工作流中承擔理解與推理。 |
| **Token** | 模型處理文字等內容時的基本計量單位。 |
| **Prompt** | 使用者提供的問題、要求或指令。 |
| **Context** | 模型在當次任務中可見的相關資訊，包括指令、歷史對話與文件。 |
| **Context window** | 模型一次處理所能容納的脈絡容量上限。 |
| **Tool** | 模型可用的外部能力，例如讀寫檔案、執行指令、查詢資料。 |
| **API** | 軟體系統之間交換要求與結果的介面與規則。 |
| **API Key** | 呼叫特定服務時用來識別與授權的憑證，等同密碼；不要貼進公開的 repo、截圖或對話。 |
| **CLI** | Command-line interface；以文字指令操作程式的介面。 |
| **Connector / Plugin** | 把外部服務接入 AI 工作環境的整合方式，通常可省去自行串接。 |
| **MCP** | Model Context Protocol；讓 AI 系統連接工具與資料來源的通用協定。 |
| **Agent** | 接受目標後，能反覆規劃、行動、檢查結果並調整的系統。 |
| **Skill / Agent Skill** | 預先保存、可重複使用的規則、操作步驟與輸出格式。 |

第四部提到的產品包括 Claude、ChatGPT、Claude Code、Codex、OpenClaw、Hermes、Obsidian 與 GitHub。

## 5. 從模型到能完成工作的產品

AI 產品可以用四層結構理解：

1. **算力（Compute）**：支撐模型運作的資料中心、晶片與運算資源。
2. **模型（Model）**：根據輸入產生內容，並支援推理等能力。
3. **Harness（執行環境）**：讓模型能使用文件、記憶、指令與外部工具的組件。
4. **Agent（代理系統）**：在設定的目標與權限內，組織多步驟行動並持續檢查進度。

對照實際產品：Claude Code、Codex、OpenClaw 屬於 agent；Projects、Skills、MCP 屬於 harness；Claude、GPT、Gemini 是模型；GPU、資料中心與晶片製造（例如台積電）屬於算力。

基本對話可以理解成：

> 已有的 context + 新的 prompt → 模型回應

同一句 prompt，換一份 context，回應就可能完全不同。例如「我這次段考數學 42 分」，被設定成嚴格老師的模型和被設定成溫柔老師的模型，回應會截然不同。

加入工具與可循環執行的機制後，系統還能搜尋資料、更新文件、執行測試或安排後續動作，也就需要更明確的授權與驗證。

## 6. Tool、MCP 與 Skill 各做什麼

三者的作用不同：

* **Tool** 解決「系統能做什麼」：能否存取文件、執行程式或呼叫服務。
* **MCP** 解決「如何把工具和資料來源接進來」：提供通用的連接方式。
* **Skill** 解決「同類工作一再出現時，照什麼規則完成」：把做法、步驟、檢查條件和格式寫下來，之後直接套用。

例如每週都要把一批文件整理成同一格式，不必每次重新向模型解釋要求。把步驟寫成 SOP 或 Skill，每次輸出就會遵循同一標準。這種方式特別適合固定格式回覆、週期性報告與大量重複處理；高度開放的創作問題則未必需要這麼嚴格的流程。

這些元件也在走向開放標準。Anthropic 在 2025 年 12 月把 MCP 捐給 Linux Foundation 旗下的 Agentic AI Foundation 中立管理（[Anthropic](https://www.anthropic.com/news/donating-the-model-context-protocol-and-establishing-of-the-agentic-ai-foundation)）；Agent Skills 同月成為開放標準（[agentskills.io](https://agentskills.io)），OpenAI、Microsoft、GitHub、Cursor 等工具都已支援。寫好的一份 Skill，不必被單一廠商綁住。一個最小的 Skill，可以只是資料夾裡的一份 `SKILL.md`：

```markdown
<!-- weekly-report/SKILL.md -->
---
name: weekly-report
description: 把本週筆記整理成週報
---

1. 讀 notes/ 裡本週的檔案
2. 照 template.md 的格式整理
3. 列出還沒完成的事項
```

第三方 skill 與 MCP server 都是你安裝的程式碼，安裝前先審查（[附錄 D](../appendix/04-evaluating-tools-and-skills.md#審查清單)）。

## 7. Context 是結果品質的基礎

### Prompt 要交代完整的任務

模型看到什麼，直接影響答案。只寫「幫我做企劃」，和提供目標客群、產品條件、既有資料、時間限制、交付格式與審核標準，得到的結果通常差很多。

有效的任務交付，至少回答四個問題：

1. **要做什麼**：目標、範圍與交付成果。
2. **根據什麼做**：資料來源、背景與限制。
3. **做到什麼程度**：品質標準、格式與完成條件。
4. **怎麼知道做對了**：可執行的檢查、測試或人工審閱方式。

SoW（Statement of Work）與 PRD（Product Requirements Document）的用處，就是把腦中的預期寫成別人或 AI 都能理解的規格。

在投入成本較高的模型或長流程之前，可以先用較便宜的模型整理 prompt，釐清需求與資料結構，讓 context 保持相關、清楚、少衝突。

2025 年年中起，業界開始改用 **context engineering（上下文工程）** 一詞（Shopify 執行長 Tobi Lütke 與 Andrej Karpathy 都曾公開提倡），重點放在讓模型在對的時間看到對的資訊。用程式代理時的具體做法，見[與程式代理協作](../part-1-build/03-working-with-coding-agents.md#上下文工程)。

### Context window 與長對話的侷限

Context window 是模型一次可處理的資訊容量。對話、附件與系統指令累積到一定程度，工具就必須決定如何處理超出的內容。有些 agent 工具會用 **compaction（脈絡壓縮）**：先把先前資訊摘要，再把摘要帶進後續處理。

摘要能延續工作，但它是有損的。細節可能被省略，反覆壓縮也可能讓系統逐漸偏離原本的要求。

即使沒有超出容量，資訊所在的位置也會影響取用效果。2023 年的「Lost in the Middle」研究指出：模型不一定能同樣可靠地使用長脈絡中段的資訊（[Liu et al.](https://arxiv.org/abs/2307.03172)）。

長任務因此可以這樣處理：

* 把目的、關鍵限制與完成標準放在容易辨識的位置。
* 不要把重要規則埋在冗長對話或無關附件裡。
* 定期整理目前的結論、決策與未解問題，必要時開新對話。
* 需要長期保存的資料寫進文件，不要只依賴聊天紀錄。

### 記憶、Project 與持續的脈絡

Memory 與 Project 類功能的用途，是讓固定背景在相關任務中重複使用，例如個人偏好、團隊規範、專案範圍或共同文件。這能減少反覆解釋；但記憶越多，負擔也可能越重：不相關的舊資料會干擾新任務，模型也可能過度迎合先前的偏好。

應把內容分成三種性質：

* **長期事實與規則**：相對穩定，值得持續保存。
* **專案資料**：只對特定目標、客戶或產品有效。
* **單次任務的上下文**：完成後不必永久保留。

記憶、Project、檔案、Skill、經 MCP 接進來的資料與工具回傳的結果，都是 context。OpenClaw、Hermes 這類 agent 會邊做邊更新自己的 context。模型人人都買得到，你的素材、歷史與標準只有你有；[用 AI 創造](04-creating-with-ai.md#1-建立自己的-second-brain)一章的 Second Brain 就是為此而建。

---

[← 用 AI 寫作](../part-3-craft/03-writing-with-ai.md) · [第四部：學習與思考](README.md) · [目錄](../../README.zh-TW.md#目錄) · [用 AI 學習 →](02-learning-with-ai.md)
