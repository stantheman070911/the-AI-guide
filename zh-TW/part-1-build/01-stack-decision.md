[目錄](../../README.zh-TW.md#目錄) › [第一部：打造](README.md) · [English](../../en/part-1-build/01-stack-decision.md) | **繁體中文**

# 技術堆疊決策

能讓個人創業者或小團隊安全上線並擴展 SaaS 的最小技術堆疊、什麼時候該加東西，以及哪些可以略過。

> **建議。** 從八項服務開始：一個程式代理、GitHub、Vercel、Supabase、Stripe、Resend、Cloudflare 與 PostHog。其他一切都視為升級選項，等到出現經過量測的需求時再加入。下方的原則是持久的；表格則有時效性。

> 最後查證：2026-10-11。價格與方案限制會改變；做決定前請查看所附連結。

## 原則

* 只保留一個記錄系統（system of record）。凡是可行，持久性的應用資料都應由 Postgres 持有。
* 在通用資料庫未能滿足某個經過量測的需求之前，不要引入專用資料庫。
* 讓同步請求路徑保持精簡。把郵件、embedding、檔案處理、報表與長時間執行的 AI 工作移到佇列或工作流程。
* 依據你實際面對的負載、可靠性或產品需求增加基礎設施，而不是依據預期中的規模。
* 為可逆性最佳化。以 Postgres 為中心、樸素、可攜的架構，通常勝過優雅的專有架構。
* 每個供應商都有持有成本：SDK、機密、webhook、帳單、服務中斷、權限、監控與資料同步。
* 優先選擇廣泛使用、文件完整的工具。對於在公開程式碼與文件中出現較多的框架與服務，程式代理產出的程式碼品質較好。（判斷，而非量測結果。）
* 第一天就在每個平台與模型供應商上設定支出上限。

## 1. 預設技術堆疊

| 層級 | 預設 | 為什麼 | 注意事項 |
| --- | --- | --- | --- |
| 程式代理 | Claude Code 或 Codex | 成熟的終端代理，具備沙箱、MCP 與專案指示檔。選一個並把它用熟。 | 見[與程式代理協作](03-working-with-coding-agents.md)。Gemini CLI 已於 2026 年 6 月 18 日停止服務（[Google](https://developers.googleblog.com/an-important-update-transitioning-gemini-cli-to-antigravity-cli/)）。 |
| 程式碼與 CI | GitHub | 程式碼、審查、issue 與 Actions 的單一事實來源。 | 強化 Actions：[修補手冊第 11 項](../part-2-ship/02-security-remediation-playbook.md#11-cicd-與發布憑證---高)。 |
| 託管 | Vercel | Next.js 維運負擔最低的選擇。 | 除非開啟 **Pause Production Deployments**，否則 on-demand budget 不會停止用量（[文件](https://vercel.com/docs/spend-management)）。 |
| 資料庫、身分驗證、儲存 | Supabase | Postgres、身分驗證、儲存、即時功能、佇列、排程與 pgvector 集中在同一個平台。Free：500 MB、50,000 MAU，閒置一週後暫停。Pro 每月 25 美元起，預設開啟支出上限（[價格](https://supabase.com/pricing)）。 | 列層級安全性就是你的安全邊界：[修補手冊第 4 項](../part-2-ship/02-security-remediation-playbook.md#4-租戶隔離與資料庫政策---嚴重)。 |
| 金流 | Stripe | Checkout、Billing、webhook、客戶入口網站。 | 跨國銷售數位產品：見下方的記錄商家。 |
| 電子郵件 | Resend | API 簡單的交易型郵件。 | 上線前設定 SPF、DKIM 與 DMARC。 |
| DNS 與邊緣 | Cloudflare | DNS、CDN、WAF，也可兼作網域註冊商。 | 把註冊商分開，是說得通的帳號隔離選擇。 |
| 數據分析與錯誤追蹤 | PostHog | 數據分析、工作階段重播、功能旗標、實驗與錯誤追蹤；每月前 100,000 筆例外免費（[價格](https://posthog.com/docs/error-tracking/pricing)）。 | 排除內部流量；避免在重播中記錄個人資料。 |

## 2. 選配升級

觸發條件真的出現時才加入。

| 升級 | 什麼時候加入 | 備註 |
| --- | --- | --- |
| 記錄商家：Stripe Managed Payments 或 Paddle | 在多個國家登記與申報 VAT 或銷售稅的成本，高於這筆費用時。 | Managed Payments 於 2026 年 4 月全面推出，適用於數位產品，每筆交易收取 3.5%，另加標準 Stripe 手續費（[價格](https://support.stripe.com/questions/managed-payments-pricing)）。 |
| Sentry | 除錯需求超出 PostHog：追蹤、版本健康度、更深入的 stack 分析。 | PostHog 解釋使用者行為；Sentry 解釋應用程式故障。 |
| Upstash Redis | 資料庫不擅長處理的快取、速率限制或暫態狀態。 | 不是因為「每個 SaaS 都需要 Redis」。 |
| Vercel Workflows | 多步驟工作必須撐過當機、重試，以及長達數小時或數天的等待。 | 建立在開源的 Workflow SDK 之上；依用量計價（[文件](https://vercel.com/docs/workflows)）。 |
| Clerk | 你想要現成的身分驗證 UI、組織與邀請功能，而不想自己做。 | 每月留存使用者 50,000 人以內免費；包含基本組織功能，進階 B2B 功能每月 100 美元（[價格](https://clerk.com/pricing)）。 |
| AI gateway：Vercel AI Gateway 或 OpenRouter | 你使用多家模型供應商，需要備援、路由或統一帳單。 | 多一個網路節點，也多一方會看到你的提示詞。 |
| AI 程式碼審查：CodeRabbit 或 Greptile | Pull request 數量超出人力能仔細審查的程度。 | 公開的比較結果互相矛盾，而且多由廠商自行進行。在你自己的 pull request 上試用兩者。 |

## 3. 特定情境的替代方案

在特定需求下優於預設選項，但並非整體更好。

| 替代方案 | 適合的情況 |
| --- | --- |
| Better Auth | 你想把身分驗證放在自己的資料庫中、不使用託管服務，特別是沒有使用 Supabase 時。它的團隊自 2025 年 9 月起維護 Auth.js（現在只做安全修補）（[公告](https://www.better-auth.com/blog/authjs-joins-better-auth)）。 |
| Neon | 你想要可以為每個 pull request 即時建立分支的 serverless Postgres。Databricks 於 2025 年 5 月收購了它。 |
| Convex | 你的應用程式大量使用即時功能，而且比起 SQL 更偏好反應式的 TypeScript 後端。 |
| Railway、Render 或 Fly.io | 你需要長時間執行的行程、WebSocket、容器或背景 worker，而它們不適合 serverless 函式。 |
| Cloudflare Workers 與 R2 | 你需要邊緣運算，或需要承受大量公開流量的儲存空間。 |
| Firebase | 已經綁定 Google 服務的行動優先應用程式。 |
| Turso | 邊緣上的 SQLite，或每個租戶一個資料庫。 |
| Pinecone | 檢索是核心工作負載，而且 pgvector 已被量測為瓶頸。 |
| Ollama | 資料不能離開電腦，或需要離線推論。見[用 LLM 打造功能](04-building-with-llms.md)。 |
| MongoDB Atlas | 你的資料是文件形態，而且團隊已經熟悉 MongoDB。 |

## 4. 實驗性

有潛力、還很年輕，或目前只有開發者自己回報效益。

* **Antigravity CLI**——Google 用來取代 Gemini CLI 的閉源工具，2026 年 5 月推出。
* **Traycer**——為程式代理撰寫檔案層級計畫的規劃層。
* **Headroom**——在工具輸出與上下文送到模型之前先壓縮。
* **OpenViking**——Volcengine 推出的代理上下文資料庫。
* **把 AI 應用程式建構工具當成正式環境後端**（Lovable、Emergent、Dreamflow）——做原型沒有問題。真實資料進來之前，先稽核資料庫政策。

## 5. 不建議或未經查證

* **Gemini CLI**——已停止服務；請遷移。
* **9Router**——把你的程式碼與憑證送經數十家第三方供應商，包括免費方案。資料與服務條款的風險大於省下的 token。
* **共享 PHP 主機**——對這套技術堆疊而言，是錯誤的執行環境模型，不適合 Next.js 與 Postgres 應用程式。
* **預設就加入 Pinecone、Clerk、Redis 或 Sentry**——每一項都在解決你可能還沒遇到的問題。

## 6. 背景工作

非同步執行比多一個資料庫更重要。典型工作：Stripe webhook、電子郵件、embedding、檔案轉換、排程清理、外部同步，以及長時間執行的 AI 任務。

| 需求 | 優先使用 |
| --- | --- |
| 簡單的排程任務 | Vercel Cron 或 Supabase Cron |
| 由資料庫驅動的非同步工作 | Supabase Queues |
| 長時間執行或多步驟的工作流程 | Vercel Workflows |
| 快取、速率限制、暫態狀態 | Upstash Redis |

> **營運原則。** 只有當某個供應商能消除一個經過量測的限制，或創造的產品優勢大於它持續的維運成本時，才加入它。

---

[第一部：打造](README.md) · [目錄](../../README.zh-TW.md#目錄) · [神聖三位一體 + 1 →](02-holy-trinity-plus-one/README.md)
