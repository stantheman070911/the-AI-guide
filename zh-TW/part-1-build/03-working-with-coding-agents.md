[目錄](../../README.zh-TW.md#目錄) › [第一部：打造](README.md) · [English](../../en/part-1-build/03-working-with-coding-agents.md) | **繁體中文**

# 與程式代理協作

如何在每一個工作階段中，讓 AI 程式代理穩定地交出可靠的成果。[神聖三位一體 + 1](02-holy-trinity-plus-one/README.md) 談的是跨工作階段保存的文件；本章談的是單一工作階段之內的事。

> 最後查證：2026-10-11。

## 證據怎麼說

* **感覺快不等於真的快。** 在 METR 2025 年的隨機對照試驗中，16 位資深開發者在自己的儲存庫中工作，使用 2025 年初的 AI 工具反而多花了 19% 的時間，卻認為自己快了 20%（[METR](https://metr.org/blog/2025-07-10-early-2025-ai-experienced-os-dev-study/)）。METR 2026 年 2 月的後續研究顯示，較新的工具確實讓開發者變快，但它自己也說，這些資料對於「快了多少」只是「非常薄弱的證據」（[更新](https://metr.org/blog/2026-02-24-uplift-update/)）。相信這種印象之前，先在你自己的工作上量測。
* **AI 放大的是你原本的團隊。** 2025 年 DORA 報告發現約 90% 的開發者使用 AI，而 AI 會放大既有的優勢與失能，不會自己修好交付流程（[Google](https://blog.google/technology/developers/dora-report-2025/)）。有了代理，測試、小幅修改與審查變得更重要，而不是更不重要。
* **程式碼需要資安審查。** 見[資安修補手冊](../part-2-ship/02-security-remediation-playbook.md#為什麼-ai-寫的程式碼更需要這些)。

## 工作循環

1. **探索。** 讓代理先閱讀相關程式碼，在修改任何東西之前，先說明它如何運作。修正錯誤的理解，比修正錯誤的程式碼便宜。
2. **規劃。** 要求一份計畫：要動哪些檔案、做法、風險，以及如何驗證。修正的是計畫，而不是 diff。
3. **實作一小段。** 一次就能審查完的修改。
4. **驗證。** 代理執行測試、型別檢查、lint 與應用程式，並展示輸出。「現在應該可以了」不是證據。
5. **審查並 commit。** 自己讀 diff。Commit。下一個任務在全新或已壓縮的工作階段中開始。

讓代理有辦法檢查自己的工作：測試套件、型別檢查器、能重現 bug 的腳本、可以開啟的瀏覽器。沒有可以執行的檢查，「看起來完成了」就是代理唯一的訊號，而你就成了驗證迴圈（[Claude Code 文件](https://code.claude.com/docs/en/best-practices)）。

## 上下文工程

模型只知道上下文視窗中的內容，而且視窗越滿，品質越差。Anthropic 稱之為「context rot」，並把上下文視為有限的預算（[Anthropic](https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents)）。

* **專案指示檔。** 使用 [AGENTS.md](https://agents.md)——現在由 Linux Foundation 旗下 Agentic AI Foundation 管理的跨工具格式——或你所用工具的對應檔案（`CLAUDE.md`）。寫進建置與測試指令、慣例，以及代理一再犯的錯。保持簡短；它會載入每一個工作階段。[附錄 B](../appendix/02-claude-md-coding-rules.md) 可以作為起點。
* **需要時才載入。** 指向檔案與路徑，而不是貼上內容。讓代理自己搜尋。
* **一個工作階段一個任務。** 任務之間清除或壓縮上下文。充滿已放棄做法的冗長工作階段，會誤導模型。
* **把狀態存在視窗之外。** 進度、決策與下一步寫進檔案（`LOG.md`，或暫用的 `NOTES.md`），讓全新的工作階段可以讀取。
* **把探索交出去。** 子代理可以搜尋程式碼庫或網路，回傳簡短摘要，讓主要上下文保持乾淨。
* **把重複的工作流程包成 skills。** [Agent Skill](https://agentskills.io) 是一個含有 `SKILL.md` 檔案與選用腳本的資料夾。在任務需要它之前，代理只會讀取它的名稱與描述，所以有很多 skills 也只佔用少量上下文。主要的程式代理大多支援這個格式。第三方 skills 要先審查（[附錄 D](../appendix/04-evaluating-tools-and-skills.md)）。
* **需要時才連接 MCP 伺服器。** 每一個伺服器都會在上下文中加入工具定義，並擴大攻擊面。

## 撰寫任務

好的任務會說明目標、限制，以及怎麼知道完成了：

```text
Add rate limiting to POST /api/generate.
Limit: 20 requests per user per hour, using the existing Upstash client in lib/redis.ts.
Return 429 with Retry-After. Do not change the response format for successful requests.
Done when: a new test in tests/api/generate.test.ts sends 21 requests and the last one gets 429,
and the existing test suite passes.
```

（範例：為 `POST /api/generate` 加上速率限制，每位使用者每小時 20 次，沿用 `lib/redis.ts` 中既有的 Upstash client；回傳 `429` 並附 `Retry-After`；不改變成功回應的格式。完成條件：新測試送出 21 次請求，最後一次得到 `429`，且既有測試全部通過。）

指出一個既有檔案作為要遵循的範例。說明哪些不能改。需求模糊時，要求代理在寫程式之前先列出它的問題。

## 測試

* 核心邏輯的測試，先由你撰寫或核准。一個失敗的測試，是代理無法爭辯的目標。
* 絕不接受為了變綠而弱化、略過或刪除失敗測試的修改。
* 寫出程式碼的那個工作階段，不適合判斷它是否完成。在全新的工作階段中審查，或執行[神聖三位一體 + 1](02-holy-trinity-plus-one/README.md#完成陷阱以及如何堵住它) 中的完成稽核。
* UI 修改要在真正的瀏覽器、真實的寬度下檢查。

## 除錯

* 給代理確切的錯誤訊息、日誌與重現步驟。
* 讓它先重現 bug，再排列假設，一次測試一個。
* 如果它第二次提出同一個修正，就停下來。清除上下文，重述已知的事實，重新開始。

## 重構

只在重構前後測試都通過時才重構。重構的 commit 與行為變更的 commit 分開，讓審查者分得出哪個是哪個。

## 審查

像審查一位能幹新人的 pull request 一樣，審查代理的 diff。把注意力放在犯錯代價高的地方：授權、資料存取、新的相依套件、遷移、錯誤處理與 CI 設定。AI 審查工具是有用的第二道檢查，不是替代品。

## 權限與安全

代理用你的憑證執行指令。沙箱、機密處理、MCP 審查與不可信任的輸入，請見[保護 AI 功能與程式代理](../part-2-ship/03-securing-ai-features-and-agents.md#你執行的程式代理)。

## 部署

代理開 pull request；CI 執行測試與資安檢查；預覽部署由人看過；正式環境由人核准。遷移與基礎設施修改要經過明確審查，並備有回退計畫（[RUNBOOK 範本](02-holy-trinity-plus-one/RUNBOOK.md)）。

## Vibe 模式與工程模式

對沒有使用者、沒有真實資料的本機原型來說，鬆散快速的迭代沒有問題。一旦牽涉到真實使用者、資料、金流或憑證，就切換到工程模式：驗收標準、測試、資安審查、完整的 diff 審查。對那個面向而言，這是單向的切換（[憲章第五條](02-holy-trinity-plus-one/CONSTITUTION.md#第五條兩種風險模式)）。

---

[← 神聖三位一體 + 1](02-holy-trinity-plus-one/README.md) · [第一部：打造](README.md) · [目錄](../../README.zh-TW.md#目錄) · [用 LLM 打造功能 →](04-building-with-llms.md)
