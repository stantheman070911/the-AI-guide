[目錄](../../README.zh-TW.md#目錄) › [第四部：學習與思考](README.md) · [English](../../en/part-4-learn-think/03-thinking-with-ai.md) | **繁體中文**

# 用 AI 思考

判斷、鋸齒狀的能力邊界、根因分析，以及驗證 AI 產出的方法。

> 最後查證：2026-10-13。

> **原文語言**：繁體中文。這是原文；[英文版](../../en/part-4-learn-think/03-thinking-with-ai.md)為翻譯。兩者不一致時，以本中文原文為準。

## 1. 當執行變得充裕，判斷就是優勢

Naval Ravikant 的觀點是：AI coding agent 與 vibe coding 讓「怎麼做」的門檻下降，「做什麼」因此更重要（[Naval](https://nav.al/ai)）。競爭優勢轉向：

* **Taste**：辨識品質。
* **Judgment**：選擇值得解決的問題。
* **Creativity**：發展原創的想法。
* **Expertise**：理解專門領域。
* **Distribution**：接觸客戶，建立可防守的事業。

AI 能生成大量可能性；哪些想法原創、有意義、值得追求，仍要人來判斷。

## 2. Ray Dalio 的五步循環

Ray Dalio 在《Principles》中把達成目標分成五步，並以 Pain + Reflection = Progress（痛苦加反思，等於進步）概括背後的態度。五步依序循環：

> **目標 → 問題 → 根因 → 計畫 → 執行 → 持續優化**

各步驟的要點，以及加入 AI 之後的分工：

| 步驟 | 要點 | AI 幫得上 | 只有你能做 |
| --- | --- | --- | --- |
| **1 設定清晰的目標** | 排定優先順序；幾乎什麼都能得到，但無法同時得到全部 | 列出選項、比較取捨 | 決定什麼最重要、放棄什麼 |
| **2 找出並正視問題** | 及早發現，不容忍阻礙進步的問題 | 整理紀錄、標出異常 | 承認問題存在 |
| **3 診斷根本原因** | 區分症狀與原因，看清自己與他人的盲點 | 從多次錯誤中找出模式 | 面對自己的盲點與 ego |
| **4 設計解決方案** | 依根因拆出步驟、資源與預期成果 | 拆解步驟、估算資源 | 為計畫負責 |
| **5 推動到底** | 用 metrics 追蹤，依結果調整 | 追蹤進度、提醒 | 紀律與執行 |

## 3. 把 AI 當成受訓中的助理

| 原則 | 實務意義 |
| --- | --- |
| **Know what good looks like** | 定義成果、受眾、限制與成功標準 |
| **Maintain high standards** | 把 AI 的產出當草稿；審閱並修改 |
| **Try replacing parts of your work with AI** | 找出適合自動化的任務，也學會哪裡仍需人的監督 |

AI 就像一位新進員工，需要範例、脈絡、清楚的指示、回饋與品質檢查。

## 4. AI 的能力邊界是鋸齒狀的

AI 的能力邊界呈鋸齒狀：它可能在很難的事情上表現驚人，卻在看似簡單的事情上出錯。2025 年 7 月，OpenAI 與 Google DeepMind 的模型在國際數學奧林匹亞（IMO）達到金牌等級（[Google DeepMind](https://deepmind.google/discover/blog/advanced-version-of-gemini-with-deep-think-officially-achieves-gold-medal-standard-at-the-international-mathematical-olympiad/)）；根據 Stanford HAI《AI Index 2026》，最好的模型讀類比時鐘的正確率卻只有 50.1%（[Stanford HAI](https://hai.stanford.edu/ai-index/2026-ai-index-report)）。

**Jagged technological frontier** 一詞來自 Harvard Business School 與 BCG 在 2023 年的實驗（758 位顧問）。在 AI 擅長的任務上，使用 AI 的顧問多完成 12.2% 的任務、快 25.1%、品質高約 40%；在研究者刻意設計、超出 AI 能力的任務上，使用 AI 的人答對率反而低了約 19 個百分點（[Dell'Acqua et al.](https://mitsloan.mit.edu/sites/default/files/2023-10/SSRN-id4573321.pdf)）。

鋸齒的位置會隨模型更新而移動，所以每次都要先判斷：這個任務在邊界內，還是邊界外？

## 5. 辨識兩種錯誤：模型答錯，與 agent 做錯

模型可能在單輪問答中，就生成沒有根據的細節，語氣卻十分篤定。這通常稱為 **hallucination（幻覺）**。

另一個傾向是 **sycophancy（討好）**：記憶越多、使用者越堅持，模型越容易附和。2025 年 4 月，OpenAI 曾因 GPT-4o 的一次更新過度附和使用者而撤回該版本（[OpenAI](https://openai.com/index/sycophancy-in-gpt-4o/)）。

Agent 還有另一類錯誤：某一步建立在錯誤前提上，後面十個步驟跟著偏離；或系統宣稱已完成，實際上沒有可用的成果。常見情境：

* 目標不明確，系統自行猜測預期結果。
* 起初一步出錯，後續工作沿用錯誤。
* 中間資料被壓縮、遺失或混入無關資訊。
* 產出表面完整，卻沒通過實際檢查。
* 出現偏差時，系統沒有足夠的檢驗方式發現。

解法是改善原始 context、限制權限，並把驗證設計進流程（見[用 AI 創造 §4](04-creating-with-ai.md#4-讓驗收成為工作的一部分)）。寫程式時，「代理說完成了」的問題見[完成陷阱](../part-1-build/02-holy-trinity-plus-one/README.md#完成陷阱以及如何堵住它)。

## 6. 主觀感受與實際效率

「我覺得 AI 幫到我了」也可能不準。METR 在 2025 年做了一項隨機對照實驗：16 位資深 open-source 開發者在自己熟悉的專案上完成 246 個真實任務，隨機決定哪些可以用 AI。他們事前預期快 24%，事後估計快了 20%，實際測量是慢了 19%（[METR](https://metr.org/blog/2025-07-10-early-2025-ai-experienced-os-dev-study/)）。

樣本限於資深開發者與他們熟悉的大型專案，工具也持續進步。METR 2026 年的後續研究沒能得到可靠的估計：許多開發者不願在沒有 AI 的情況下工作，不肯參加或跳過了部分任務（[METR](https://metr.org/blog/2026-02-24-uplift-update/)；另見[與程式代理協作](../part-1-build/03-working-with-coding-agents.md#證據怎麼說)）。

Microsoft Research 與 Carnegie Mellon University 在 CHI 2025 發表的調查（319 位知識工作者）也發現：越信任 AI 的人，越少做批判性思考；越相信自己能力的人，越常做（[Lee et al.](https://www.microsoft.com/en-us/research/publication/the-impact-of-generative-ai-on-critical-thinking-self-reported-reductions-in-cognitive-effort-and-confidence-effects-from-a-survey-of-knowledge-workers/)）。

## 7. 交叉質疑：AI council

對重要答案，可以讓模型 A 提出初步結論，再交給模型 B 找出錯誤、缺漏或不一致，也就是「AI 對峙」或 **AI model council**。不同模型可能犯同樣的錯，所以仍要回到原始資料查核。

盡量換一家的模型，因為訓練資料與盲點不同；只有一個模型時，就開新對話，在乾淨的 context 中重新檢查，避免它替先前的答案辯護。

研究類任務要求可開啟、可追溯的引用。

## 8. 讓 AI 幫你多想一層

以下用法替思考加一點摩擦，道理與[用 AI 學習](02-learning-with-ai.md#6-何時不該用-ai)一章的 desirable difficulties 相同：

* **Devil's advocate（反方律師）**：「用最強的論點反駁我的想法，不要客氣。」可以抵銷模型討好的傾向。
* **Pre-mortem（事前驗屍）**：「假設一年後這個計畫失敗了，最可能的三個原因是什麼？」方法來自心理學家 Gary Klein。
* **Ask me first（先問我）**：「給建議之前，先問我五個你需要知道的問題。」
* **Tough editor（嚴格的編輯）**：請它像嚴格的編輯與真實使用者一樣批評草稿，不要奉承（見[用 AI 創造 §8](04-creating-with-ai.md#8-邊做邊學的三個-prompt)）。

## 9. 區分預測與已確立的事實

談 AI 與工作時，實用建議常和強烈的預測混在一起，可以這樣分開看：

| 說法 | 如何使用 |
| --- | --- |
| AI 讓一個人能做到大得多的團隊的工作 | 視為依任務而定的可能性；測試實際品質與極限 |
| 特定工具的技術能力將變得不那麼值錢 | 視為方向性預測；技術基礎仍要練 |
| Creator 與受眾將取代機構與雇主 | 把獨立發行視為多一個選項 |
| 小團隊借助 AI 可產出更多 | 以專案、使用者回饋與成本驗證 |
| AI 的產出透過反覆修改才有價值 | 直接應用：定義標準、檢查草稿、持續改進 |

---

[← 用 AI 學習](02-learning-with-ai.md) · [第四部：學習與思考](README.md) · [目錄](../../README.zh-TW.md#目錄) · [用 AI 創造 →](04-creating-with-ai.md)
