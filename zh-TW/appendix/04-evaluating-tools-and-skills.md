[目錄](../../README.zh-TW.md#目錄) › [附錄](README.md) · [English](../../en/appendix/04-evaluating-tools-and-skills.md) | **繁體中文**

# 附錄 D：評估工具與 Skills

如何判斷一個工具、agent skill 或 MCP 伺服器值不值得安裝，以及在常見工作中通過評估的選擇。熱門程度、贊助與發表影片都不是品質的證據。

> 最後查證：2026-10-11。

## 信任等級

| 等級 | 意思 | 預設立場 |
| --- | --- | --- |
| 官方 | 由它所整合之平台的廠商發布。 | 了解它做什麼之後再使用。 |
| 社群 | 原始碼公開，維護者可辨識且仍在活動。 | 安裝前審查程式碼並固定版本。 |
| 實驗性 | 還很年輕、維護者很少，或只有開發者自己回報效益。 | 在沙箱中、用拋棄式專案試用。 |
| 未經查證 | 發布者不明、沒有原始碼，或宣稱的內容無法查證。 | 不要安裝。 |

## 審查清單

安裝 skill、MCP 伺服器或代理外掛之前：

1. **發布者。** 你能辨識維護者並閱讀原始碼嗎？
2. **維護狀況。** 近期有發布、issue 有回應、不只一位貢獻者。
3. **它執行什麼。** 閱讀 `SKILL.md`、附帶的腳本、安裝 hook，以及每一個 MCP 工具描述。就這件事而言，給模型的指示也是程式碼。
4. **它能接觸什麼。** 檔案路徑、網路主機與憑證。只給最小權限。
5. **固定版本。** 固定版本或 commit。在你核准之後才改變描述的工具，是已知的攻擊手法（[保護 AI 功能與程式代理](../part-2-ship/03-securing-ai-features-and-agents.md#9-mcp-伺服器與-skills-都是你安裝的程式碼)）。
6. **組合。** 它會不會和你已經在用的工具，一起湊成致命三要素？
7. **證據。** 開發者提出的速度與省 token 數字只是假設。在你自己的工作上量測。
8. **退場。** 你能在不破壞專案的情況下移除它嗎？

## 依使用情境

### 程式代理

選一個並把它用熟。Claude Code 與 Codex 是預設的終端代理（[技術堆疊決策](../part-1-build/01-stack-decision.md#1-預設技術堆疊)）。Cursor 與 GitHub Copilot 適合以編輯器為中心的工作；JetBrains Junie 適合 IntelliJ 使用者；[OpenHands](https://github.com/OpenHands/OpenHands) 是自行託管代理的開源選擇。自 2026 年 6 月起，Gemini CLI 不再為免費與個人 Google AI 方案提供服務；取代它的 Antigravity CLI 仍屬實驗性。

### 規劃

[神聖三位一體文件](../part-1-build/02-holy-trinity-plus-one/README.md)不需要任何工具。Traycer 是專為代理設計的規劃層，屬於實驗性。

### 程式碼審查

CodeRabbit 與 Greptile 是最常被拿來比較的 AI 審查工具。公開的比較大多由廠商進行，結果也互相矛盾，所以請在你自己兩週份的 pull request 上試用兩者，並計算你實際採納了多少則留言。核准者仍然是人。

### 測試與評估

* 端對端測試用 [Playwright](https://playwright.dev)。Microsoft 官方的 [Playwright MCP 伺服器](https://github.com/microsoft/playwright-mcp)讓代理透過無障礙快照操作瀏覽器，因此能檢查自己做的 UI。
* LLM 評估與紅隊測試用 [promptfoo](https://github.com/promptfoo/promptfoo)。

### 資安

| 工作 | 工具 |
| --- | --- |
| 程式碼與歷史中的機密 | `gitleaks`、`trufflehog`、具推送保護的 GitHub secret scanning |
| 靜態分析 | Semgrep、GitHub code scanning |
| 相依套件 | `npm audit`、`pip-audit`、Dependabot 或 Renovate |
| 資料庫政策 | Supabase Security Advisor |
| 經授權的動態測試 | ZAP；`nmap` 與 `sqlmap` 只用於你自己的預備環境 |

### 資料庫

依[技術堆疊決策](../part-1-build/01-stack-decision.md)選擇資料庫。如果透過 Supabase 官方 MCP 伺服器把代理連上 Supabase，請把它限定在單一專案、使用唯讀模式，並指向開發用專案；唯讀模式仍會讓可讀取的資料列進入模型的上下文，而提示詞注入依然是主要風險（[Supabase](https://supabase.com/docs/guides/ai-tools/mcp)）。

### 代理的瀏覽與網路資料

本機瀏覽用 Playwright MCP。代理需要大量存取網路時，使用託管瀏覽器（Browserbase）與搜尋 API（Exa、SerpAPI）。抓回來的一切都是不可信任的內容。

### 設計

Impeccable 是社群 skill，為前端工作加入設計評論與打磨指令。Mobbin 是收錄真實 App 畫面的付費資料庫；對互動模式有幫助，但它也是大家都在看的同一個視覺來源（[如何不像 AI 生成第 13 節](../part-3-craft/01-how-to-not-look-ai-generated.md#13-從同一個視覺回饋迴圈之外尋找參考)）。

### LLM 應用程式建構工具

Dify 是開源的視覺化 LLM 工作流程建構工具，適合內部工具與原型。產品功能則優先使用你自己擁有、可以測試的程式碼。

### 角色包

像 The Agency 這類代理「角色」集合，加入的是角色描述，而不是能力。優先選擇把流程與檢查方式寫進去的 skills。

---

[← 附錄 C：我使用的 Skills 與工具](03-skills-and-tools.md) · [附錄](README.md) · [目錄](../../README.zh-TW.md#目錄)
