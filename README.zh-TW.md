[English](README.md) | **繁體中文**

# AI 指南

用 AI 輔助（「vibecoded」）開發、交付真正產品的實用筆記，帶有明確觀點——該用什麼技術堆疊、如何判斷網站是否真的可以上線、如何補上 AI 程式工具常常留下的資安漏洞，以及如何讓 AI 輔助的設計與寫作看起來不像 AI 生成。第四部談如何用 AI 學習、思考與工作。

## 適合誰閱讀

* **個人創業者與小團隊**：用 AI 程式工具打造產品，並想交付真正能用的東西。
* **審查或接手 vibecoded 專案的人**：需要一份該檢查什麼的清單。
* **設計師與寫作者**：使用 AI，但希望成果依然有作者的痕跡。
* **學生與剛開始使用 AI 的人**：想用 AI 學習、思考與工作。

第二部假設讀者對網頁開發有基本認識；第三部、第四部與附錄則不需要。

## 目錄

### [第一部：打造](zh-TW/part-1-build/README.md)

1. [技術堆疊決策](zh-TW/part-1-build/01-stack-decision.md)——能安全上線 SaaS 的最小技術堆疊，以及選配升級、特定情境的替代方案與應避免的選擇。
2. [神聖三位一體 + 1](zh-TW/part-1-build/02-holy-trinity-plus-one/README.md)——可重複使用的 CONSTITUTION／BRIEF／PLAN／LOG（＋RUNBOOK）文件範本，讓 AI 程式代理在專案整個生命週期中保持對齊。
3. [與程式代理協作](zh-TW/part-1-build/03-working-with-coding-agents.md)——證據怎麼說、工作循環、上下文工程、測試、審查與部署。
4. [用 LLM 打造功能](zh-TW/part-1-build/04-building-with-llms.md)——以評估選模型、結構化輸出、檢索、成本、可觀測性與本機模型。

### [第二部：上線](zh-TW/part-2-ship/README.md)

1. [網站上線準備檢查清單](zh-TW/part-2-ship/01-production-readiness-checklist.md)——vibecoded 網站上線前要檢查的一切：行動裝置、SEO、表單、效能、無障礙等等。
2. [資安修補手冊](zh-TW/part-2-ship/02-security-remediation-playbook.md)——AI 生成的程式碼最常引入之漏洞的修正方法，依 OWASP Top 10:2025 分類。
3. [保護 AI 功能與程式代理](zh-TW/part-2-ship/03-securing-ai-features-and-agents.md)——提示詞注入、致命三要素、工具權限、MCP 伺服器，以及如何安全地執行代理。

### [第三部：打磨](zh-TW/part-3-craft/README.md)

1. [如何不像 AI 生成](zh-TW/part-3-craft/01-how-to-not-look-ai-generated.md)——給設計師的指南：在 AI 輔助的設計工作中保有作者性與觀點。
2. [文案寫作指南](zh-TW/part-3-craft/02-copywriting-guide.md)——十堂經典文案課、八項 AI 與社群時代的補充，以及一份發布前檢查清單。
3. [用 AI 寫作](zh-TW/part-3-craft/03-writing-with-ai.md)——編修 AI 起草文字的流程，以及不捏造來源的研究方法。

### [第四部：學習與思考](zh-TW/part-4-learn-think/README.md)

1. [AI 基礎](zh-TW/part-4-learn-think/01-ai-fundamentals.md)——Outcome 與 Context、模型、tools、MCP、skills 與 agent。
2. [用 AI 學習](zh-TW/part-4-learn-think/02-learning-with-ai.md)——active production、研究證據、讓 AI 當學習教練的十種角色，以及間隔複習。
3. [用 AI 思考](zh-TW/part-4-learn-think/03-thinking-with-ai.md)——判斷、鋸齒狀的能力邊界、幻覺與討好，以及交叉檢查 AI 產出。
4. [用 AI 創造](zh-TW/part-4-learn-think/04-creating-with-ai.md)——Second Brain、agent 授權、驗收，以及選對要做的東西。
5. [與 AI 一起生活](zh-TW/part-4-learn-think/05-living-with-ai.md)——四個生命維度、skill stack、一門 craft、專注與休息。
6. [AI 的影響](zh-TW/part-4-learn-think/06-impact-of-ai.md)——工作、新人、新創、學術誠信、資料安全與社會。

### [附錄](zh-TW/appendix/README.md)

* [A. 核心撰寫原則](zh-TW/appendix/01-writing-principles.md)——我請 AI 工具撰寫或編修文字時提供的寫作規則。
* [B. CLAUDE.md 預設範本——程式開發規則](zh-TW/appendix/02-claude-md-coding-rules.md)——一份起始 `CLAUDE.md`，包含一條首要指令與十二條程式開發規則。
* [C. 我使用的 Skills 與工具](zh-TW/appendix/03-skills-and-tools.md)——我持續更新的清單，記錄我使用的 skills 與工具。
* [D. 評估工具與 Skills](zh-TW/appendix/04-evaluating-tools-and-skills.md)——信任等級、審查清單，以及依使用情境整理、通過審查的選擇。
* [E. 程式碼庫稽核提示詞](zh-TW/appendix/05-codebase-audit-prompt.md)——一份只做審查的提示詞，請代理找出最少、但值得進行的修改。

## 建議閱讀路徑

| 如果你是…… | 建議閱讀 |
| --- | --- |
| 第一次用 AI 交付產品 | 依序讀第一部到第三部 |
| 剛開始使用 AI | [AI 基礎](zh-TW/part-4-learn-think/01-ai-fundamentals.md)，接著讀[用 AI 學習](zh-TW/part-4-learn-think/02-learning-with-ai.md)與[用 AI 思考](zh-TW/part-4-learn-think/03-thinking-with-ai.md) |
| 即將上線 | [檢查清單](zh-TW/part-2-ship/01-production-readiness-checklist.md)（先處理 P0 項目），接著讀[資安修補手冊](zh-TW/part-2-ship/02-security-remediation-playbook.md) |
| 正要和 AI 程式代理一起開始新專案 | [與程式代理協作](zh-TW/part-1-build/03-working-with-coding-agents.md)、[神聖三位一體 + 1](zh-TW/part-1-build/02-holy-trinity-plus-one/README.md)，接著讀[附錄 B](zh-TW/appendix/02-claude-md-coding-rules.md) |
| 要在產品中加入 AI 功能 | [用 LLM 打造功能](zh-TW/part-1-build/04-building-with-llms.md)，接著讀[保護 AI 功能與程式代理](zh-TW/part-2-ship/03-securing-ai-features-and-agents.md) |
| 設計師或寫作者 | [如何不像 AI 生成](zh-TW/part-3-craft/01-how-to-not-look-ai-generated.md)、[文案寫作指南](zh-TW/part-3-craft/02-copywriting-guide.md)、[用 AI 寫作](zh-TW/part-3-craft/03-writing-with-ai.md)，接著讀[附錄 A](zh-TW/appendix/01-writing-principles.md) |

## 快速查詢

| 主題 | 位置 |
| --- | --- |
| 一開始該用哪些服務 | [技術堆疊決策](zh-TW/part-1-build/01-stack-decision.md#1-預設技術堆疊) |
| 背景工作與佇列 | [技術堆疊決策 §6](zh-TW/part-1-build/01-stack-decision.md#6-背景工作) |
| 撰寫 AGENTS.md 或 CLAUDE.md | [上下文工程](zh-TW/part-1-build/03-working-with-coding-agents.md#上下文工程) · [附錄 B](zh-TW/appendix/02-claude-md-coding-rules.md) |
| 讓 AI 代理與需求保持對齊 | [神聖三位一體 + 1](zh-TW/part-1-build/02-holy-trinity-plus-one/README.md) |
| 撰寫可測試的驗收標準 | [BRIEF 範本](zh-TW/part-1-build/02-holy-trinity-plus-one/BRIEF.md#驗收標準) |
| 選擇模型 | [用 LLM 打造功能](zh-TW/part-1-build/04-building-with-llms.md#用你自己的評估集選模型) |
| 檢索（RAG） | [用 LLM 打造功能](zh-TW/part-1-build/04-building-with-llms.md#檢索rag) |
| 上線前先修什麼（P0／P1／P2） | [檢查清單：更高層次的稽核](zh-TW/part-2-ship/01-production-readiness-checklist.md#更高層次的稽核) |
| API 金鑰與機密 | [檢查清單 §18](zh-TW/part-2-ship/01-production-readiness-checklist.md#18-機密與-api-金鑰) · [修補手冊](zh-TW/part-2-ship/02-security-remediation-playbook.md#機密與金鑰) |
| 授權與資料庫政策（RLS） | [修補手冊](zh-TW/part-2-ship/02-security-remediation-playbook.md#a01-存取控制失效) |
| 速率限制與支出上限 | [檢查清單 §22](zh-TW/part-2-ship/01-production-readiness-checklist.md#22-濫用防範與成本保護) · [修補手冊第 19 項](zh-TW/part-2-ship/02-security-remediation-playbook.md#19-缺少速率限制與支出控制---高) |
| 供應鏈與 CI/CD | [修補手冊](zh-TW/part-2-ship/02-security-remediation-playbook.md#a03-軟體供應鏈失效) |
| 提示詞注入 | [保護 AI 功能與程式代理](zh-TW/part-2-ship/03-securing-ai-features-and-agents.md#致命三要素) |
| 稽核既有的程式碼庫 | [附錄 E](zh-TW/appendix/05-codebase-audit-prompt.md) |
| 審查 skill 或 MCP 伺服器 | [附錄 D](zh-TW/appendix/04-evaluating-tools-and-skills.md#審查清單) |
| 無障礙 | [設計第 23 節](zh-TW/part-3-craft/01-how-to-not-look-ai-generated.md#23-把無障礙當成設計限制) |
| 檢驗設計是否太通用 | [三個最終測試](zh-TW/part-3-craft/01-how-to-not-look-ai-generated.md#三個最終測試) |
| 標題、offer 與證據 | [文案寫作指南](zh-TW/part-3-craft/02-copywriting-guide.md) |
| 用 AI 學習而不依賴它 | [用 AI 學習](zh-TW/part-4-learn-think/02-learning-with-ai.md) |
| 檢查 AI 的回答與 agent 的工作 | [用 AI 思考 §5](zh-TW/part-4-learn-think/03-thinking-with-ai.md#5-辨識兩種錯誤模型答錯與-agent-做錯) |
| 個人知識庫（Second Brain） | [用 AI 創造 §1](zh-TW/part-4-learn-think/04-creating-with-ai.md#1-建立自己的-second-brain) |
| 學術誠信與揭露 AI 的使用 | [AI 的影響 §8](zh-TW/part-4-learn-think/06-impact-of-ai.md#8-學術誠信先遵守具體規範) |

## 本指南的組織方式

* 英文頁面位於 [`en/`](en/)，中文頁面位於 [`zh-TW/`](zh-TW/)，兩者路徑相同。每一章頂端都有連到另一種語言版本的連結。
* 含有產品細節的章節都標有「最後查證」日期。原則在前，有時效性的表格在後。
* 尚未解決的問題記錄在[研究待辦清單](RESEARCH_BACKLOG.zh-TW.md)。

## 參與貢獻

歡迎以中文或英文提出 issue 與 pull request。

* [貢獻指南](CONTRIBUTING.zh-TW.md)——如何提出修改、新增章節，以及保持翻譯同步。
* [風格指南](STYLE_GUIDE.zh-TW.md)與[詞彙表](GLOSSARY.md)——寫作與翻譯慣例。
* [行為準則](CODE_OF_CONDUCT.zh-TW.md)——我們在這裡如何對待彼此。

## 授權

文字內容 © 2026 Stanley Lu，採用 [CC BY 4.0](LICENSE) 授權。程式碼、程式碼範例、[神聖三位一體 + 1](zh-TW/part-1-build/02-holy-trinity-plus-one/README.md) 範本，以及[附錄 B](zh-TW/appendix/02-claude-md-coding-rules.md) 的預設範本，採用 [MIT 授權條款](LICENSE-CODE)。授權條款以英文原文為準。
