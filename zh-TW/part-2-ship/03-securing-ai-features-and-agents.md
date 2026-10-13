[目錄](../../README.zh-TW.md#目錄) › [第二部：上線](README.md) · [English](../../en/part-2-ship/03-securing-ai-features-and-agents.md) | **繁體中文**

# 保護 AI 功能與程式代理

兩個攻擊面：你提供給使用者的 LLM 功能，以及你在自己電腦與儲存庫上執行的程式代理。兩者失效的方式相同。參考依據是 [OWASP Top 10 for LLM Applications 2025](https://genai.owasp.org/llm-top-10/) 與 [OWASP Top 10 for Agentic Applications](https://genai.owasp.org/resource/owasp-top-10-for-agentic-applications-for-2026/)（2025 年 12 月）。

> 最後查證：2026-10-11。

## 核心問題：提示詞注入

模型在同一個通道裡讀取指令與資料。網頁、電子郵件、PDF、issue 或工具結果中的文字，都可能改變它的行為。沒有任何過濾器能可靠地阻止這件事；OWASP 指出，以模型的運作方式而言，萬無一失的防範方法並不明確（[LLM01:2025](https://genai.owasp.org/llmrisk/llm01-prompt-injection/)），而防護用的模型本身也可能被注入（[cheat sheet](https://cheatsheetseries.owasp.org/cheatsheets/LLM_Prompt_Injection_Prevention_Cheat_Sheet.html)）。

所以要假設注入會成功來設計。

## 致命三要素

Simon Willison 的規則（[原文](https://simonwillison.net/2025/Jun/16/the-lethal-trifecta/)）：當一個工作階段同時具備以下三者，代理就可以被利用：

1. 能存取私密資料，
2. 會接觸不可信任的內容，以及
3. 有辦法對外通訊。

拿掉任何一項，資料竊取的路徑就會關閉。對外通道往往不像「寄送電子郵件」工具那麼明顯：網址中夾帶資料的 Markdown 圖片、連結預覽、網頁抓取工具、pull request 留言，或推送到公開儲存庫的 commit。

有文件記錄的示範：2025 年 5 月，公開 GitHub issue 中的提示詞注入，讓一個使用 GitHub MCP 伺服器的代理，把擁有者私人儲存庫的資料複製到公開的 pull request 中（[Invariant Labs](https://invariantlabs.ai/blog/mcp-github-vulnerability)）。伺服器本身沒有 bug。問題出在組合。

## 你提供的 LLM 功能

### 1. 把模型輸出當作不可信任的輸入

模型輸出要經過和使用者輸入一樣的跳脫與驗證（OWASP LLM05）。

* 以純文字渲染，或在渲染 HTML 與 Markdown 前先清理。在渲染的輸出中封鎖外部圖片，或在 CSP 中限制 `img-src`，以關閉透過圖片外洩資料的通道。
* 要求結構化輸出，並在據以行動之前依 schema 驗證。
* 絕不把模型輸出傳給 `eval`、shell 或以字串組成的 SQL。見[修補手冊的注入項目](02-security-remediation-playbook.md#a05-注入)。

### 2. 給工具剛好夠用的最小權限

過度代理（LLM06）會把錯誤的回答變成錯誤的行動。

* 工具以終端使用者的權限行動，絕不使用服務角色。一個能查詢所有客戶訂單的客服機器人，遲早會這麼做。
* 優先使用唯讀工具。寫入工具的範圍要窄：「退款這筆訂單，最多到訂單金額」，而不是「執行 SQL」。
* 不可逆或對外的動作，要求使用者明確確認：寄送訊息、付款、刪除、發布。

### 3. 在檢索之前執行存取控制

檢索出來的文件是不可信任的內容，而向量索引不懂你的權限（LLM08）。

* 在挑選候選段落的查詢中就依租戶與使用者權限篩選，而不是等模型看過之後才篩。
* 除非本來就要分享，否則不要讓某位使用者上傳的內容進入另一位使用者的上下文。
* 記錄每個段落的來源。發現被污染的文件時，你需要知道它影響了哪些地方。
* 審查代理寫入長期記憶的內容；從不可信任內容寫入的記憶，就是儲存型的注入。

### 4. 假設系統提示詞是公開的

使用者可以把它套出來（LLM07）。機密、API 金鑰與授權規則都不要放在提示詞中。權限在程式碼中執行。

### 5. 限制用量

為每次呼叫設定最大輸出 token、請求逾時、代理步數上限、每位使用者配額，以及供應商層級的每月上限（LLM10）。平台層級的限制，請見[修補手冊的支出控制項目](02-security-remediation-playbook.md#19-缺少速率限制與支出控制---高)。

### 6. 像測試其他 bug 一樣測試注入

在評估集中加入注入案例：藏在文件、工具結果與使用者資料中的指令，以及嘗試透過每一個輸出通道外洩資料。[promptfoo](https://github.com/promptfoo/promptfoo) 是用於這類紅隊測試的開源工具；OpenAI 於 2026 年 3 月收購它，並表示它會維持開源。更換模型或提示詞時，重新執行測試。

## 你執行的程式代理

### 7. 把代理放進沙箱，而不只是程式碼

程式代理以你的使用者帳號、你的 SSH 金鑰與你的雲端憑證執行 shell 指令。

* 開啟代理的作業系統層級沙箱，並把網路存取限制在允許清單內。要清楚它的邊界：Claude Code 的沙箱涵蓋 shell 指令，而它的檔案工具、MCP 伺服器與 hook 都在沙箱之外執行（[文件](https://code.claude.com/docs/en/sandboxing)）。
* 無人看管或「自動核准」的工作階段，要在 dev container、虛擬機或雲端環境中執行，絕不在存放正式環境憑證的電腦上執行。
* 把開啟儲存庫視為執行它的程式碼。`.claude/settings.json`、`.mcp.json` 與 hook 這類專案檔案，可能啟動伺服器、執行指令，或改變 API 流量的去向。Claude Code 曾有兩個漏洞在信任提示出現前就這麼做（[CVE-2025-59536](https://nvd.nist.gov/vuln/detail/CVE-2025-59536)、[CVE-2026-21852](https://nvd.nist.gov/vuln/detail/CVE-2026-21852)）。保持代理為最新版本，不熟悉的儲存庫在容器或虛擬機中開啟。
* 寬鬆的權限模式依任務授予，不要永久開啟。

### 8. 讓正式環境憑證遠離代理

代理能讀到的任何東西，都可能外洩：進入日誌、pull request，或傳送給模型供應商的提示詞。

* 給代理針對開發資源、範圍有限且短效的 token。不給正式資料庫網址、不給 `service_role` 或 `sb_secret_` 金鑰、不給雲端 root 憑證。
* 在權限規則與沙箱設定（`sandbox.filesystem.denyRead` 或 `sandbox.credentials`）中，同時禁止讀取 `.env` 檔案與憑證目錄。只靠權限規則，擋不住代理執行的腳本自行開啟檔案。正式環境的機密不要放在本機 `.env`。

### 9. MCP 伺服器與 skills 都是你安裝的程式碼

MCP 規格指出，工具「代表任意程式碼的執行」，而且除非來自可信任的伺服器，工具描述與註記都應視為不可信任（[規格](https://modelcontextprotocol.io/specification/latest)）。已知的攻擊：

* **工具投毒**：藏在工具描述中的指令，模型會讀到，使用者卻看不到。
* **Rug pull**：伺服器在你核准之後修改工具描述（[Invariant Labs](https://invariantlabs.ai/blog/mcp-security-notification-tool-poisoning-attacks)）。
* **跨伺服器流程**：一個伺服器的輸出操控對另一個伺服器的呼叫，可能用各自無害的伺服器拼湊出致命三要素。
* **市集裡的惡意 skills**：2026 年 2 月，Koi Security 在 OpenClaw 助理的 skill 市集 ClawHub 的 2,857 個 skills 中，找到 341 個惡意 skills（[The Hacker News](https://thehackernews.com/2026/02/researchers-find-341-malicious-clawhub.html)）。

只安裝你能辨識發布者的伺服器與 skills，固定版本，啟用前閱讀工具描述與附帶的腳本，並只給每個伺服器完成工作所需的憑證。NSA 於 2026 年 5 月發布的 MCP 指引，從較大型部署的角度涵蓋了同樣的內容（[NSA](https://www.nsa.gov/Press-Room/Press-Releases-Statements/Press-Release-View/Article/4496698/nsa-releases-security-design-considerations-for-ai-driven-automation-leveraging/)）。[附錄 D](../appendix/04-evaluating-tools-and-skills.md) 有一份審查清單。

### 10. 把不可信任的輸入與寫入權限分開

Issue、pull request 留言、網頁與相依套件的 README 都是不可信任的內容。處理這些內容的代理，不應該在同一個工作階段中，同時持有私人儲存庫、機密或部署的寫入權限。

* 讓分類代理以唯讀方式執行，或每個工作階段只能接觸一個公開儲存庫。
* 不要讓外部貢獻者觸發的 CI 代理看到機密。

### 11. 審查代理的產出

代理新增相依套件、修改身分驗證程式碼與編輯 CI workflow，就和修正錯字一樣順手。

* 代理推送到分支；人類負責合併。保護預設分支。
* 對 workflow、身分驗證、資料庫政策、遷移與相依套件清單的修改，要求人類審查。
* 在 CI 中執行[修補手冊](02-security-remediation-playbook.md)的資安檢查，讓審查不只依賴注意力。

---

[← 資安修補手冊](02-security-remediation-playbook.md) · [第二部：上線](README.md) · [目錄](../../README.zh-TW.md#目錄) · [如何不像 AI 生成 →](../part-3-craft/01-how-to-not-look-ai-generated.md)
