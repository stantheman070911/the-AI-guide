[目錄](../../README.zh-TW.md#目錄) › [第二部：上線](README.md) · [English](../../en/part-2-ship/02-security-remediation-playbook.md) | **繁體中文**

# 資安修補手冊

針對[網站上線準備檢查清單](01-production-readiness-checklist.md)中風險最高的項目提供修正方法，依 [OWASP Top 10:2025](https://owasp.org/Top10/2025/0x00_2025-Introduction/) 分類。每一項都說明如何找出問題、如何修正，以及如何證明修正有效。LLM 功能與程式代理特有的風險，請見[保護 AI 功能與程式代理](03-securing-ai-features-and-agents.md)。

嚴重等級：🚨 嚴重（上線前修正）· 🔴 高（上線後盡快修正）· 🟠 中（排入時程）。🚨 與 🔴 項目屬於檢查清單分級中的 P0。

只測試你擁有或獲得授權測試的系統。

> 最後查證：2026-10-11。

## 為什麼 AI 寫的程式碼更需要這些

Veracode 在 2025 年以 80 個資安敏感任務測試了 100 多個模型，45% 的生成程式碼樣本引入了已知漏洞，而且較大的模型表現並沒有比較好（[新聞稿](https://www.veracode.com/press-release/ai-generated-code-poses-major-security-risks-in-nearly-half-of-all-development-tasks-veracode-research-reveals/)）。代理會把正常流程寫出來。存取控制、輸入處理與失敗時的行為，才是你要審查的地方。

## A01 存取控制失效

### 1. 用戶端身分驗證 — 🚨 嚴重

寫在瀏覽器 JavaScript 裡的登入檢查，可以被讀取並略過。

* **偵測**：在前端程式碼中搜尋密碼比對、角色檢查與 token 驗證。
* **修正**：在伺服器端驗證憑證並判斷角色。用戶端只拿到 session cookie 或 token。
* **驗證**：不透過 UI，以匿名身分直接呼叫每一個受保護的 API。每一次呼叫都失敗。

### 2. 缺少物件層級授權（IDOR）— 🚨 嚴重

已登入不代表被允許。任何接受 ID 的端點，都必須檢查呼叫者是否可以存取那個物件。

* **偵測**：列出每一個接受 `userId`、`orderId`、`documentId` 等參數的路由。找出只用 ID 篩選的查詢。
* **修正**：每一個查詢都限定在已驗證的使用者或租戶範圍內（`WHERE id = $1 AND owner_id = $2`）。否則回傳 `404` 或 `403`。
* **驗證**：用兩個測試帳號，以 A 登入後請求 B 的物件。讀取與寫入的每一個請求都失敗。

### 3. 缺少功能層級授權 — 🚨 嚴重

一般使用者也能觸及管理員功能與寫入操作。

* **偵測**：列出所有 `POST`／`PUT`／`PATCH`／`DELETE` 路由與管理頁面。記下哪些在伺服器端檢查角色。
* **修正**：在伺服器程式碼中，對每一個操作強制執行角色與擁有權檢查。隱藏按鈕不是權限檢查。
* **驗證**：用一般使用者的 session 重送管理員請求。全部回傳 `403`。

### 4. 租戶隔離與資料庫政策 — 🚨 嚴重

AI 打造的應用程式最常見的嚴重缺陷。Supabase 與 Firebase 的設計就是讓瀏覽器直接存取資料庫；用戶端的金鑰是公開的，資料與外界之間只隔著列層級政策。在 CVE-2025-48757 中，掃描 Lovable 展示區的 1,645 個應用程式，發現其中 170 個的資料表任何人都能讀取或寫入（[紀錄](https://cvemon.intruder.io/cves/CVE-2025-48757)）。

* **偵測**：執行 Supabase Security Advisor（`supabase db advisors`，或在 dashboard 中）。把 `rls_disabled_in_public`、`permissive_rls_policy`（`USING (true)`）、`security_definer_view` 與 `rls_references_user_metadata` 視為阻擋上線的問題（[lint 清單](https://supabase.com/docs/guides/database/database-advisors)）。Firebase 則檢查 Security Rules 中是否有 `allow read, write: if true`。
* **修正**：在每一個對外公開的資料表上啟用 RLS。政策依據 `auth.uid()` 或來自可信來源的租戶 ID 撰寫，絕不依據使用者可編輯的 metadata。`service_role` 金鑰只放在伺服器端。
* **驗證**：只用公開網址與 anon key，先在沒有 session 的情況下，再以帳號 A 對帳號 B 的資料列，嘗試讀寫每一個資料表。把這些加成自動化測試，避免之後的遷移悄悄重新打開漏洞。

### 5. 身分驗證繞過路徑 — 🚨 嚴重

略過身分驗證的路由，或可以被略過的單一檢查。在 CVE-2025-29927 中，一個精心構造的 `x-middleware-subrequest` 標頭，讓自行託管的應用程式完全略過 Next.js middleware；只在 middleware 中執行身分驗證的應用程式因此暴露（[OSV](https://osv.dev/vulnerability/CVE-2025-29927)）。

* **偵測**：建立路由清單，標出哪些需要身分驗證。測試路徑變體：結尾斜線、編碼、大小寫。
* **修正**：在存取資料的地方（路由處理器、server action 或資料庫政策）檢查授權，而不只在 middleware 中。保持框架更新。
* **驗證**：在沒有 session 的情況下請求每一個受保護的路由，包括 API 路由與 server action。全部失敗。

### 6. 伺服器端請求偽造（SSRF）— 🔴 高

任何會去抓取使用者可控網址的功能：連結預覽、圖片匯入、webhook，以及會上網瀏覽的 AI 工具。攻擊者把它指向 `169.254.169.254` 或內部服務。OWASP 2025 把 SSRF 併入存取控制失效。

* **偵測**：搜尋接受使用者輸入的伺服器端 `fetch`、`axios`、`requests` 或 `curl` 呼叫。
* **修正**：盡可能以允許清單限制目的主機。否則先解析 DNS，拒絕私有、loopback 與 link-local 位址範圍，並在每次重新導向後重新檢查。抓取程式不帶任何內部系統的憑證。
* **驗證**：提交 `http://127.0.0.1`、`http://169.254.169.254/`、一個解析到私有 IP 的主機名稱，以及一個會重新導向到私有 IP 的網址。全部被拒絕。

## A02 安全設定錯誤

### 7. 安全標頭 — 🟠 中

成本很低，而大多數 vibecoded 應用程式上線時都沒有。

* **修正**：全域設定 `Content-Security-Policy`（從 `default-src 'self'` 開始，避免 `unsafe-inline` 與 `unsafe-eval`）、在 CSP 中用 `frame-ancestors` 控制框架嵌入（`X-Frame-Options` 只為舊瀏覽器保留）、`Strict-Transport-Security`、`X-Content-Type-Options: nosniff`、`Referrer-Policy` 與 `Permissions-Policy`。不要加 `X-XSS-Protection`，它已經過時。CSP 先以 `Content-Security-Policy-Report-Only` 上線，再改為強制執行。
* **驗證**：檢查正式環境的回應標頭（`curl -I`），而不是本機開發環境。

### 8. 暴露的環境與雲端設定錯誤 — 🔴 高

帶有正式資料的預覽與預備環境、公開的儲存 bucket、除錯端點、預設憑證、暴露的 source map，以及在需要驗證的 API 上把 CORS 設為 `*`。

* **偵測**：列出每一個部署網址與儲存 bucket。檢查 bucket 與儲存政策。搜尋同時出現 `Access-Control-Allow-Origin: *` 與憑證的設定。
* **修正**：保護預覽部署（平台的部署保護或身分驗證），給它們獨立的憑證與資料，bucket 預設為私有，CORS 來源使用允許清單。
* **驗證**：在未登入的瀏覽器中開啟預覽網址、bucket 物件網址與 `/.map` 檔案。都不會暴露私密資料。

## A03 軟體供應鏈失效

### 9. 幻覺套件與惡意套件 — 🔴 高

模型會編造套件名稱，攻擊者則搶先註冊這些名稱（「slopsquatting」）。在 16 個模型產生的 576,000 個程式碼樣本中，商業模型的幻覺套件平均至少 5.2%，開源模型為 21.7%，共出現 205,474 個不重複的捏造名稱（[USENIX Security 2025](https://www.usenix.org/conference/usenixsecurity25/presentation/spracklen)）。

* **偵測**：審查 diff 中每一個新增的相依套件。確認它以完全相同的名稱存在，並檢查它的年齡、維護者與下載紀錄。
* **修正**：相依套件由你自己加入，不要透過代理未經審查的安裝指令。設定發布時間冷卻期，讓剛發布的版本不會被自動安裝（pnpm 的 `minimumReleaseAge`、Yarn 的 `npmMinimalAgeGate`；請查閱你的套件管理工具文件）。
* **驗證**：lockfile 變更卻沒有對應的清單檔變更時，CI 會失敗；安裝時使用 `npm ci` 或同等的凍結 lockfile 模式。

### 10. 有漏洞的相依套件 — 🔴 高

* **偵測**：在 CI 中執行該生態系的稽核工具（`npm audit`、`pip-audit`、`cargo audit`、`govulncheck`）。
* **修正**：先修補嚴重與高風險的發現。啟用 Dependabot 或 Renovate，並設定冷卻期，讓更新以可審查的 pull request 形式出現。
* **驗證**：稽核步驟在每一個 pull request 上執行，遇到嚴重發現時阻擋合併。

### 11. CI/CD 與發布憑證 — 🔴 高

2025 年的兩起事件說明了這種模式。在 tj-actions/changed-files 遭入侵事件（CVE-2025-30066）中，攻擊者把既有的版本標籤移到惡意 commit；固定到 commit SHA 的 workflow 不受影響（[詳情](https://www.sentinelone.com/vulnerability-database/cve-2025-30066)）。Shai-Hulud 蠕蟲從開發者電腦竊取 npm 與雲端 token，並用它們發布了 500 多個套件的受感染版本（[CISA](https://www.cisa.gov/news-events/alerts/2025/09/23/widespread-supply-chain-compromise-impacting-npm-ecosystem)）。

* **修正**：把第三方 action 固定到完整的 commit SHA；GitHub 稱這是「目前唯一能把 action 當作不可變版本使用的方法」（[GitHub](https://docs.github.com/en/actions/reference/security/secure-use)）。`GITHUB_TOKEN` 預設為唯讀，再依 job 給予更多權限。避免讓 `pull_request_target` 處理不可信任的程式碼。用 OIDC 取代長期有效的雲端金鑰。透過 trusted publishing 發布套件，而不是個人 token。開啟具推送保護的 secret scanning。
* **驗證**：用腳本或 linter 標出任何沒有固定到 SHA 的 `uses:`。workflow 檔案明確宣告 `permissions:`。

## 機密與金鑰

### 12. 寫死與外洩的憑證 — 🚨 嚴重

* **偵測**：用 `gitleaks` 或 `trufflehog` 掃描完整的 Git 歷史，而不只是目前的檔案。檢查建置日誌與 CI 輸出。
* **修正**：輪替所有找到的機密；刪除 commit 並不會撤銷金鑰。把機密移到環境變數或機密管理工具，commit 一份 `.env.example`，並把 `.env*` 加入 `.gitignore`。
* **驗證**：掃描工具在 CI 中與 pre-commit hook 中執行，並且對完整歷史通過檢查。

### 13. 用戶端程式碼中的機密金鑰 — 🚨 嚴重

瀏覽器 bundle 裡的任何東西都是公開的。要分清楚哪些金鑰本來就設計成公開（Supabase anon key、Stripe publishable key），哪些不是（Supabase `service_role`、Stripe secret key、任何 LLM 供應商的金鑰）。

* **偵測**：搜尋建置後的 bundle，而不只是原始碼，找出 `sk_`、`sk-`、`service_role` 等金鑰前綴。檢查哪些環境變數帶有公開前綴（`NEXT_PUBLIC_`、`VITE_`）。
* **修正**：從伺服器路由呼叫第三方 API；由它持有金鑰、驗證使用者、限制速率，並只回傳用戶端需要的內容。
* **驗證**：在正式環境的建置輸出中搜尋每一個機密的前綴。都不會出現。

## A04 加密機制失效

### 14. 密碼儲存與政策 — 🚨 嚴重

優先使用託管的身分驗證服務。如果要自己儲存密碼：

* **修正**：用 Argon2id 雜湊（記憶體至少 19 MiB、迭代 2 次、平行度 1）。無法使用 Argon2id 時用 scrypt。bcrypt 只適用於舊系統：work factor 10 以上，而且它會忽略超過 72 位元組的輸入（[OWASP](https://cheatsheetseries.owasp.org/cheatsheets/Password_Storage_Cheat_Sheet.html)）。舊的雜湊在使用者下次登入時重新雜湊。
* **政策**：NIST SP 800-63B-4 要求只靠密碼登入時至少 15 個字元（搭配 MFA 時 8 個字元），必須比對外洩與常見密碼清單，並禁止組成規則與強制定期更換（[NIST](https://pages.nist.gov/800-63-4/sp800-63b.html)）。
* **驗證**：資料庫中沒有明文、MD5、SHA-1 或未加鹽的 SHA-256 雜湊。

### 15. 網址、日誌與錯誤訊息中的敏感資料 — 🟠 中

查詢字串中的 token 會留在瀏覽器歷史與 CDN 日誌中。完整傾印請求，會讓憑證在日誌裡留存好幾個月。

* **修正**：用標頭或 POST body 傳送 token。在日誌中遮蔽憑證與個人資料欄位。對使用者回傳一般性的錯誤訊息。
* **驗證**：在一天份的正式環境日誌中搜尋 `password`、`token`、`authorization` 與金鑰前綴。

## A05 注入

### 16. SQL 注入 — 🚨 嚴重

* **偵測**：搜尋以字串組成的 SQL，以及 ORM 的逃生口（`$queryRawUnsafe`、`sequelize.literal`、用 template string 呼叫原始 `execute`），包括資料庫函式中的 SQL。
* **修正**：使用參數化查詢或 ORM 的安全查詢產生器。應用程式的資料庫使用者採最小權限。
* **驗證**：對每一個動態查詢用 `' OR 1=1 --` 與引號字元做單元測試。在獲得授權的情況下，可用 `sqlmap` 等掃描工具對預備環境的副本確認。

### 17. 跨站腳本攻擊（XSS）— 🔴 高

包括以 HTML 或 Markdown 渲染的模型輸出。

* **偵測**：搜尋 `dangerouslySetInnerHTML`、`innerHTML`、`v-html`、`document.write`，以及啟用原始 HTML 的 Markdown 渲染器。
* **修正**：透過框架的跳脫機制渲染文字。無法避免 HTML 時，用 DOMPurify 清理。強制執行 CSP（第 7 項）。
* **驗證**：在每一個使用者可編輯的欄位，以及一個會讓模型照抄的提示詞中，存入 `<img src=x onerror=alert(1)>`。都不會執行。

### 18. 命令注入 — 🚨 嚴重

* **偵測**：搜尋 `exec`、`system`、帶 `shell: true` 的 `spawn`、帶 `shell=True` 的 `subprocess` 與 `os.system`，並追蹤使用者或模型的輸入是否會流到這些地方。
* **修正**：用函式庫取代 shell。如果一定要啟動行程，傳入參數陣列並停用 shell。
* **驗證**：讓 `; id` 與 `$(id)` 經過每一條路徑。都不會執行。

## A06 不安全的設計

### 19. 缺少速率限制與支出控制 — 🔴 高

暴力破解、爬取資料，以及把小帳單變成大帳單的 AI 端點。

* **修正**：依 IP 與帳號設定速率限制，使用共用儲存（Redis，或平台內建的限制器）：登入約每 15 分鐘 5 次、密碼重設每小時 3–5 次，AI 與其他昂貴端點設定每位使用者配額。回傳 `429` 並附上 `Retry-After`。接著在供應商允許的地方設定支出上限：Vercel 的 on-demand budget 除非開啟 **Pause Production Deployments**，否則不會停止用量，而且每隔幾分鐘才檢查一次（[Vercel](https://vercel.com/docs/spend-management)）；Supabase Pro 預設開啟支出上限（[價格](https://supabase.com/pricing)）；每一把 LLM 供應商金鑰都設定每月上限。
* **驗證**：用腳本對同一個帳號快速發出 50 次登入嘗試與 50 次 AI 請求。兩者都被限流。確認每一個供應商的警示都會送到真人手上。

### 20. 未經驗證就信任的金流與 webhook — 🚨 嚴重

* **修正**：只依據經過驗證的伺服器端事件開通付費權限。驗證 webhook 簽章（Stripe 要用該端點的簽章密鑰，對原始 body 驗證），拒絕過期的時間戳，並且每個事件 ID 只處理一次。
* **驗證**：送出沒有簽章或簽章錯誤的偽造 webhook：被拒絕。重送一個有效的 webhook：沒有重複效果。在用戶端請求中修改價格或方案：被忽略。

## A07 身分驗證失效

### 21. Session 處理 — 🔴 高

* **修正**：使用框架或身分驗證服務提供的 session。Cookie 設定 `HttpOnly`、`Secure` 與 `SameSite=Lax` 或 `Strict`。登入與權限變更時更換 session ID，設定閒置與絕對過期時間，登出時在伺服器端銷毀 session。Token 不放在 `localStorage`。Chrome 的 Device Bound Session Credentials 自 Chrome 146 起已在 Windows 上提供，會把 cookie 綁定到硬體金鑰；等你的身分驗證服務支援後，值得採用（[Google](https://blog.google/security/protecting-cookies-with-device-bound-session-credentials/)）。
* **驗證**：登出後，舊的 cookie 會被 API 拒絕。

### 22. 跨站請求偽造（CSRF）— 🔴 高

適用於以 cookie 驗證、會改變狀態的請求。

* **修正**：優先使用框架內建的防護。否則使用 synchronizer token（有狀態的應用程式）或以 HMAC 簽章的 double-submit cookie（無狀態的應用程式）。對新式瀏覽器，依 `Sec-Fetch-Site` 拒絕不安全的跨站請求，並以 `Origin` 檢查作為後備，也是被接受的做法。`SameSite` cookie 是縱深防禦，不是完整的防護（[OWASP](https://cheatsheetseries.owasp.org/cheatsheets/Cross-Site_Request_Forgery_Prevention_Cheat_Sheet.html)）。npm 套件 `csurf` 已被棄用，不要加入。
* **驗證**：從其他來源送出每一個會改變狀態的表單。全部被拒絕。

### 23. 密碼重設與帳號復原 — 🔴 高

* **修正**：重設 token 必須一次性、短效且隨機；不論帳號是否存在都回傳相同的回應；重設後讓既有 session 失效；設定速率限制（第 19 項）。
* **驗證**：已使用或已過期的 token 會失敗。對真實與不存在的電子郵件，重設回應完全相同。

## A08 軟體或資料完整性失效

### 24. 不安全的反序列化 — 🔴 高

* **偵測**：搜尋對不可信任輸入使用的 `pickle.loads`、`marshal.loads`、`yaml.load`、Java `ObjectInputStream` 與 PHP `unserialize()`。
* **修正**：使用 JSON 與 `yaml.safe_load()`。使用前先依 schema（Zod、Pydantic、JSON Schema）驗證輸入。
* **驗證**：單元測試送入格式錯誤與過大的 payload；它們在進入商業邏輯之前就被拒絕。

## A09 資安日誌與警示失效

### 25. 出事時沒有任何警示 — 🟠 中

* **修正**：記錄身分驗證事件、權限拒絕、管理員操作與金流事件，附上使用者與請求 ID，不含機密。登入失敗、`403` 與支出出現異常時通知真人。
* **驗證**：在預備環境中觸發每一個警示一次，確認有人收到。

## A10 例外狀況處理不當

### 26. 失敗時放行 — 🔴 高

檢查拋出例外時反而放行的程式碼：回傳 `true` 的 `try/catch`、缺少角色時被當成管理員、政策服務逾時就被略過。

* **修正**：預設拒絕。身分驗證、金流與政策檢查中的錯誤一律視為失敗。
* **驗證**：在測試中讓身分驗證服務、資料庫或政策服務無法使用。受保護的操作會被拒絕。

## 進階強化

完成上面各項之後值得加上的：

* 比對機密與簽章時使用常數時間比較。
* GraphQL API 設定查詢深度與複雜度限制。
* 管理後台前加上 IP 允許清單或 SSO。
* 設定 CAA DNS 記錄，只讓你選定的憑證機構能為該網域簽發憑證。
* 網域註冊商、DNS 與雲端 root 帳號使用獨立的硬體金鑰 MFA。
* 在入侵者會去找的地方佈下 canary token。

---

[← 網站上線準備檢查清單](01-production-readiness-checklist.md) · [第二部：上線](README.md) · [目錄](../../README.zh-TW.md#目錄) · [保護 AI 功能與程式代理 →](03-securing-ai-features-and-agents.md)
