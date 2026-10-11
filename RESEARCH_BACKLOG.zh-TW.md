[English](RESEARCH_BACKLOG.md) | **繁體中文**

# 研究待辦清單

查證程度不足以寫進章節的主張與主題。挑一項、找到第一手來源，然後開 pull request。問題解決後就把該項移除。

最後檢視：2026-10-11。

## 未經查證的主張

* **AI 程式碼審查基準測試。** 被廣泛引用的比較是 Martian 的 [Code Review Bench](https://codereview.withmartian.com/)；無法取得它的方法說明頁面，而 20 萬至 30 萬個 pull request 的規模只出現在廠商文章中。Macroscope 沒有任何獨立評估。
* **Shai-Hulud 2.0。** 2025 年 11 月的第二波攻擊由廠商回報，而不是 CISA。
* **Codex 網路存取預設值。** 沙箱模式（`read-only`、`workspace-write`、`danger-full-access`）與核准政策（`on-request`、`never`）記載於 [learn.chatgpt.com/docs/sandboxing](https://learn.chatgpt.com/docs/sandboxing)；網路存取的預設值沒有說明。
* **文案寫作指南的引言。** 由於找不到第一手來源，各課改標為轉述：Halbert 關於 offer 的那句話（第 1 課）、Caples 關於標題的那句話（第 9 課），以及「人們買的不是產品；他們買的是更好的自己」（第 10 課）。找到書名與頁碼後，才能恢復為引言。

## 尚未評估

* 背景工作方面，Inngest 與 Trigger.dev 相較於 Vercel Workflows 與 Supabase Queues 的優劣。
* Convex、Railway、Render、Fly.io、Neon 與 Turso 目前的價格與限制。
* 對 Augment Code、Warp、Coder、Lovable 與 Dreamflow 的深入評估。
* 代理角色包是否能可量測地改善產出。

## 無法辨識的產品

研究清單中無法有把握地對應到特定產品的名稱：Mirrorish、Hyperagent、Oz.dev、Dockr。Fastino 與其「Pioneer」產品在不同來源中的描述不一致。
