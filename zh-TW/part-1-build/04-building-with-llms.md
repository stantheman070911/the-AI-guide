[目錄](../../README.zh-TW.md#目錄) › [第一部：打造](README.md) · [English](../../en/part-1-build/04-building-with-llms.md) | **繁體中文**

# 用 LLM 打造功能

上線 LLM 功能時要做的決定：用哪個模型、怎麼呼叫、如何讓它根據你的資料回答、成本多少，以及怎麼知道它有效。這些功能的資安問題，請見[保護 AI 功能與程式代理](../part-2-ship/03-securing-ai-features-and-agents.md)。

> 最後查證：2026-10-11。模型名稱與價格每個月都在變，所以本章不列出任何模型。請查看你的供應商價格頁面。

## 從比你想像更簡單的做法開始

Anthropic 對代理的建議：從「最簡單的解法開始，只在需要時才增加複雜度」（[Anthropic](https://www.anthropic.com/engineering/building-effective-agents)）。實務上：

1. **一次模型呼叫**，搭配好的指示、範例與檢索來的上下文。大多數功能到這裡就夠了。
2. **固定的工作流程**，由數次呼叫組成，適用於步驟事先已知的情況（先擷取，再分類，再起草）。
3. **代理迴圈**，由模型決定下一個工具呼叫，只在步驟無法事先決定時才使用。代理成本更高、速度更慢，錯誤也會累積。

## 用你自己的評估集選模型

公開排行榜量測的是別人的任務。

* 收集 20 到 100 筆真實輸入，附上預期輸出或評分標準。包含困難與對抗性的案例。
* 先用能力強的模型建立品質基準，再用同一組資料測試更小、更便宜的模型。上線通過標準中最便宜的那一個。
* 每次更換模型、提示詞或檢索設定時，都重新執行評估集。[promptfoo](https://github.com/promptfoo/promptfoo) 是用來執行評估的開源工具。
* 模型 ID 放在設定中，不要散落在程式碼各處。你一定會換。

## 呼叫 API

* **結構化輸出。** 凡是程式碼要解析的內容，都使用供應商的 schema 約束輸出或工具呼叫，然後照樣用 Zod 或 Pydantic 驗證。
* **串流**：任何使用者需要等待的內容。
* **逾時與重試**：遇到速率限制與伺服器錯誤時以退避方式重試。每次呼叫都設定最大輸出長度。
* **金鑰留在伺服器端。** 見[修補手冊第 13 項](../part-2-ship/02-security-remediation-playbook.md#13-用戶端程式碼中的機密金鑰---嚴重)。
* **提示詞放在版本控制中**，與程式碼放在一起，而且只在跑過評估之後才修改。

## 檢索（RAG）

1. **先確認你是否需要它。** 如果原始資料放得進上下文視窗，而且搭配 prompt caching 的成本可以接受，整份送進去更簡單，效果也往往更好。（判斷；請用你的評估集測試兩種做法。）
2. **從 Postgres 開始。** Supabase 或 Neon 中的 pgvector，讓向量與資料及其權限放在一起。專用向量資料庫什麼時候值得，見[技術堆疊決策](01-stack-decision.md#3-特定情境的替代方案)。
3. **使用混合搜尋。** Embedding 會漏掉錯誤代碼、SKU 與名稱這類精確字串；全文搜尋可以抓到它們。合併兩份結果清單。
4. **為段落加上上下文，再重新排序。** 在 Anthropic 的測試中，於每個段落前面加上一小段專屬上下文，讓前 20 名檢索的失敗率下降 35%；加上 BM25 後降幅達 49%；再加上重新排序模型，降幅達 67%（[Anthropic](https://www.anthropic.com/engineering/contextual-retrieval)）。
5. **在檢索查詢中依權限篩選。** 不是之後才篩。見[AI 資安第 3 項](../part-2-ship/03-securing-ai-features-and-agents.md#3-在檢索之前執行存取控制)。
6. **分開評估檢索。** 在評判生成的答案之前，先檢查正確的段落是否出現在前幾名結果中。

## 成本

* **Prompt caching**：用於重複出現的前綴，例如系統提示詞、工具定義與長文件。
* **Batch API**：用於可以等待的工作。Anthropic 與 OpenAI 的批次請求都是一般價格的一半（[Anthropic](https://platform.claude.com/docs/en/build-with-claude/batch-processing)）。
* **依難度分流。** 把簡單、量大的任務交給小模型。
* **依功能量測。** 記錄每個請求的 token 與成本，並標記功能與使用者，讓你在帳單出現之前就知道什麼最貴。
* **設定上限。** 每位使用者配額與供應商每月上限（[修補手冊第 19 項](../part-2-ship/02-security-remediation-playbook.md#19-缺少速率限制與支出控制---高)）。

## 可觀測性

每次呼叫都記錄：提示詞版本、模型、輸入與輸出 token、延遲、成本，以及任何使用者回饋。每週審閱一批真實對話紀錄；它們會顯示指標看不出來的失敗。個人資料在進入日誌前先遮蔽。

如果你已經在用 PostHog，[PostHog AI observability](https://posthog.com/ai-observability) 很合適。[Langfuse](https://github.com/langfuse/langfuse) 是開源的替代方案，提供追蹤、評估與提示詞管理。

## 本機模型

適合的情況：資料不能離開電腦、需要離線使用，或在大量使用下需要可預測的成本。[Ollama](https://ollama.com) 是在本機執行開放權重模型最簡單的方式。在複雜推理上，品質會低於頂尖的託管模型，而記憶體會限制可用的模型大小。決定之前先跑評估集。

## 正式環境中的代理

* 設計一小組範圍明確的工具，附上有幫助的錯誤訊息與精簡的輸出。功能重疊的工具會讓模型混淆（[Anthropic](https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents)）。
* 為每次執行設定步數、時間與支出上限。
* 長時間的任務使用持久執行，讓當機或部署不會讓進度消失。見[背景工作](01-stack-decision.md#6-背景工作)。
* 不可逆的動作之前，要求人類核准。

---

[← 與程式代理協作](03-working-with-coding-agents.md) · [第一部：打造](README.md) · [目錄](../../README.zh-TW.md#目錄) · [網站上線準備檢查清單 →](../part-2-ship/01-production-readiness-checklist.md)
