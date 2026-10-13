[English](RESEARCH_BACKLOG.md) | **繁體中文**

# 研究待辦清單

查證程度不足以寫進章節的主張與主題。挑一項、找到第一手來源，然後開 pull request。問題解決後就把該項移除。

最後檢視：2026-10-11。

## 未經查證的主張

* **AI 程式碼審查基準測試。** 被廣泛引用的比較是 Martian 的 [Code Review Bench](https://codereview.withmartian.com/)；無法取得它的方法說明頁面，而 20 萬至 30 萬個 pull request 的規模只出現在廠商文章中。Macroscope 沒有任何獨立評估。
* **Shai-Hulud 2.0。** 2025 年 11 月的第二波攻擊由廠商回報，而不是 CISA。
* **Codex 網路存取預設值。** 沙箱模式（`read-only`、`workspace-write`、`danger-full-access`）與核准政策（`on-request`、`never`）記載於 [learn.chatgpt.com/docs/sandboxing](https://learn.chatgpt.com/docs/sandboxing)；網路存取的預設值沒有說明。
* **文案寫作指南的引言。** 由於找不到第一手來源，各課改標為轉述：Halbert 關於 offer 的那句話（第 1 課）、Caples 關於標題的那句話（第 9 課），以及「人們買的不是產品；他們買的是更好的自己」（第 10 課）。找到書名與頁碼後，才能恢復為引言。
* **ClawHub 惡意 skills 的總數。** Koi Security 在 2,857 個 skills 中找到 341 個惡意 skills（2026 年 2 月）已經查證。歸於 IBM X-Force、超過 1,100 個惡意 skills 的數字找不到出處；Antiy CERT 回報歷來至少 1,184 個，Securelist 則回報超過 1,100 個惡意帳號。
* **AI Index 2026 讀時鐘的人類基準。** 最佳模型 50.1% 的數字廣為報導；人類 90.1% 的基準只出現在二手報導中。
* **用 REA 重建 macOS 預覽程式。** 比較有無 REA 的 agent 重建預覽程式的 demo，找不到出處。
* **Anthropic 成長行銷團隊的規模。** Anthropic 的報告沒有提到該團隊只有一人、沒有專職工程師。
* **第四部引用的影片來源。** 第四部轉述的影片 The Digital Renaissance 與 How to Use AI to Learn Anything Faster，尚未找到作者或網址。

## 尚未評估

* 背景工作方面，Inngest 與 Trigger.dev 相較於 Vercel Workflows 與 Supabase Queues 的優劣。
* Convex、Railway、Render、Fly.io、Neon 與 Turso 目前的價格與限制。
* 對 Augment Code、Warp、Coder、Lovable 與 Dreamflow 的深入評估。
* 代理角色包是否能可量測地改善產出。

## 無法辨識的產品

研究清單中無法有把握地對應到特定產品的名稱：Mirrorish、Hyperagent、Oz.dev、Dockr。Fastino 與其「Pioneer」產品在不同來源中的描述不一致。
