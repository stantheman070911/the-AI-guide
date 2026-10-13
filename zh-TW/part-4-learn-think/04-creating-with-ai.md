[目錄](../../README.zh-TW.md#目錄) › [第四部：學習與思考](README.md) · [English](../../en/part-4-learn-think/04-creating-with-ai.md) | **繁體中文**

# 用 AI 創造

Second Brain、agent 工作流、授權與安全，以及該做什麼。寫程式的細節在[第一部](../part-1-build/README.md)，程式代理的安全在[保護 AI 功能與程式代理](../part-2-ship/03-securing-ai-features-and-agents.md)；本章寫給所有用 AI 做東西的人。

> 最後查證：2026-10-13。

> **原文語言**：繁體中文。這是原文；[英文版](../../en/part-4-learn-think/04-creating-with-ai.md)為翻譯。兩者不一致時，以本中文原文為準。

## 1. 建立自己的 Second Brain

### 為什麼要擁有自己的 context

通用模型人人可用；你累積的文件、歷史、決策、工作習慣與品質標準，則是你自己的。把它們整理成一個長期維護的個人知識庫，就是 **Second Brain（第二大腦）**。

Second Brain 可以只是一個資料夾，加上持續整理的習慣。裡面放筆記、模板、SOP、決策紀錄、研究資料與專案說明，自己和不同的 AI 工具都讀得懂。

### 為什麼選純文字與 Markdown

純文字簡單、耐用、容易搜尋，也不依賴單一軟體。Markdown 用少量符號就能表達標題、清單、連結與表格，適合當文件的基本格式。長期好處：

* 不同工具都能讀取，不易被單一平台鎖定。
* 可以版本管理，保留修改紀錄。
* 新工具或新同事可以直接使用既有資料，不必從零建立脈絡。
* 一份文件修正後，日後依據它做的工作也更可能跟著改善。

### 讓知識庫保持可用

可靠的原則是 **structure over quantity（結構勝過數量）**：一個檔案聚焦一個主題，標題清楚，相關文件互相連結，定期刪除重複、過期或互相矛盾的內容。

一個簡單的結構示例（可依需要調整）：

```text
Second-Brain/
├── Projects/    # 進行中的專案與需求
├── Knowledge/   # 筆記、研究與參考資料
├── Processes/   # SOP、Skill、固定工作流程
├── Decisions/   # 重要決策與理由
└── Templates/   # 可重複使用的文件格式
```

工具可以用 [Obsidian](https://obsidian.md) 這類以純文字為基礎的編輯器，也可以直接用檔案系統；有程式經驗的人可以用 Claude Code 或 Codex 協助建立、整理與維護。

一開始不必做出複雜的系統，讓文件在每次任務後都能更新、查找、再利用即可。這批資料的壽命，可能比任何一款當下流行的 AI 工具都長。

參考：[LLM Wiki](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f)（Andrej Karpathy；個人知識整理的方向）、[Vault for Founders](https://github.com/cwlin0131/Vault-for-Founders)（知識庫結構範例）。

## 2. Agent：從回答問題到執行工作

傳統對話以單次回答為主。Agent 則圍繞目標持續處理任務：

> **規劃 → 行動 → 核查 → 調整 → 完成**

它可能先拆解問題，再操作工具，確認結果是否達標，遇到問題就修正路徑。OpenClaw、Hermes 都屬於這類產品，但自主程度、記憶能力與權限管理各不相同。

Agent 特別適合大量文件整理、重複的格式轉換、批次核對，或需要多步驟探索的工作。它也讓沒有程式背景的人能做出小型個人工具，或從一個不知如何著手的問題開始找方法。

## 3. 授權是一道光譜

Agent 的授權有不同程度：

| 授權程度 | 行動模式 | 例子 |
| --- | --- | --- |
| **建議為主** | AI 提建議，由人決定並執行 | 草擬郵件，使用者審閱後寄出 |
| **準備後核准** | AI 先準備，關鍵動作等待批准 | 整理好待發文件，交負責人核准 |
| **執行後回報** | AI 在事先授權範圍內完成，事後彙報 | 更新例行表格，定時報告變更 |
| **高度自主** | AI 在既定權限內執行外部動作 | 不經逐件審核，對外發送訊息 |

決定授權程度時，把它想成帶一位剛加入團隊的同事：他能處理什麼資料、可能犯什麼錯、出錯能否回復、哪些決定必須有人核准？

授權也是資訊安全問題。能讀取訊息、修改檔案、呼叫外部服務或以你名義行動的 agent，一旦被誤導、遭入侵或誤解指令，造成的損害與它的權限相當。授權範圍要配合資料敏感度、行動是否可逆，以及你的監督能力。

2026 年初爆紅的開源個人助理 [OpenClaw](https://github.com/openclaw/openclaw) 是一個具體案例。它能接上 WhatsApp、Slack、Telegram 等訊息平台，讀取訊息、操作檔案、以使用者名義發送訊息，並有自己的 skill 市集 ClawHub。2026 年 2 月，資安公司 Koi Security 稽核 ClawHub 上的 2,857 個 skills，發現其中 341 個是惡意的（約 12%），會竊取帳號密碼、API key 與加密貨幣錢包等資料（[The Hacker News](https://thehackernews.com/2026/02/researchers-find-341-malicious-clawhub.html)）。

三條基本規則：只給完成任務所需的最小權限；安裝 skill 或 plugin 前先確認來源；敏感資料走有權限控管的連接方式，不要把整台機器交給 agent。程式代理的做法見[保護 AI 功能與程式代理](../part-2-ship/03-securing-ai-features-and-agents.md#你執行的程式代理)。

## 4. 讓驗收成為工作的一部分

交付任務時，除了說明「要做什麼」，也要說明「完成後如何證明」。寫程式就安排測試；整理文件就檢查數量、格式與來源；研究任務就要求可追溯的引用。

實務技巧：

1. **先試一次，再決定是否拆小。** 低風險、可重試的任務，先讓系統嘗試；失敗後再逐步引導。
2. **保留可回復的狀態。** 經常存檔，出錯時能退回乾淨的版本。
3. **要求簡化。** AI 把解法弄得過度複雜時，直接要它說明原因，並提出更簡單的方案。
4. **提供具體的視覺資料。** 處理介面與儀表板時，截圖或設計稿往往比冗長描述更直接。
5. **交給它可驗證的檢查。** 執行測試、比對輸出、檢查條件；不要只接受「已完成」的文字回覆。
6. **依風險分配監督。** 可回復的周邊工作可以給較多自主；核心邏輯與不可逆的動作則加強審查。

也有團隊採用「存檔後讓系統跑一段時間，再決定接受或重來」的方式（[Anthropic](https://www-cdn.anthropic.com/58284b19e702b49db9302d5b6f135ad8871e7658.pdf)）；適不適合，要看任務。寫程式時的完整循環見[與程式代理協作](../part-1-build/03-working-with-coding-agents.md#工作循環)。

## 5. 選一個符合工作型態的工具

不必同時用所有工具。先選目前最常做的一種工作，把它做好，再增加新能力。

Claude Code 與 Codex 適合資料夾、程式專案與多步驟任務；OpenClaw 與 Hermes 這類個人助理 agent 適合訊息平台整合與排程。各工具的定位與信任等級見[附錄 D](../appendix/04-evaluating-tools-and-skills.md#依使用情境)。功能、方案與價格變動很快，採用前請查閱官方資訊。

## 6. 程式與非程式工作

對會寫程式的人，AI 是加速器：協助理解程式碼、除錯、寫測試、修改既有功能。這是 **augmented workflow（增強既有流程）**。

對不會寫程式的人，變化可能更大：過去無法獨力完成的小工具、資料轉換或簡單原型，現在有機會在 AI 協助下做出來。可靠性、維護、安全與部署仍需檢驗。

Anthropic 產品設計團隊把兩者分別稱為「augmented workflow」與「holy crap, I'm a developer」，並認為差距最大的是第二種人（[Anthropic](https://www-cdn.anthropic.com/58284b19e702b49db9302d5b6f135ad8871e7658.pdf)）。Vibe coding 一詞由 Andrej Karpathy 在 2025 年 2 月提出（[Karpathy](https://x.com/karpathy/status/1886192184808149383)），同年 11 月被 Collins 詞典選為年度詞彙（[Collins](https://blog.collinsdictionary.com/language-lovers/collins-word-of-the-year-2025-ai-meets-authenticity-as-society-shifts/)）。

日常可以嘗試的任務：

* 從一批文件擷取關鍵事實，整理成表格。
* 把混亂的資料改成一致格式，或做語言轉換。
* 對大量檔案套用同一套規則明確的操作。
* 製作市面上沒有現成方案的小型私人工具。
* 用固定流程產生例行簡報或工作摘要。
* 研究與解決問題時，讓 AI 先提出方法，再依資料與結果反覆修正。

**GitHub** 是程式與專案檔案的託管平台，可以理解成「程式碼的雲端硬碟」。它支援版本歷史與協作，是保存、回復 AI 輔助開發成果的重要工具。

參考：[附錄 A：核心撰寫原則](../appendix/01-writing-principles.md)與[附錄 C：我使用的 Skills 與工具](../appendix/03-skills-and-tools.md)（prompt 與筆記）、[Loot Drop](https://www.loot-drop.io/)（失敗新創的產品案例）。

## 7. 從單次指令升級為可維護的工作流

比「把一件事交給 AI」更成熟的做法，是留下可重複執行的工作規格：

1. 定義輸入資料與預期輸出。
2. 固定必要的規則、模板與判斷標準。
3. 指定哪些步驟 AI 可以自行操作。
4. 加入可實際執行的驗收機制。
5. 保留輸出、修改紀錄與錯誤經驗。
6. 流程穩定後，再考慮排程或自動執行。

軟體專案的完整版本，是[神聖三位一體 + 1](../part-1-build/02-holy-trinity-plus-one/README.md) 的文件範本。

## 8. 邊做邊學的三個 prompt

### Build while learning

```text
I want to build [PROJECT], but I have limited experience.

Act as my mentor. Break it into the smallest practical steps. Tell me only what I need to understand for the next step. Explain important decisions, let me choose, and help me troubleshoot as I build.

If you do something I don't understand, explain what you did and why.

Do not complete the entire project without involving me.
```

### Identify automation opportunities

```text
Review this list of my recurring tasks:

[TASK LIST]

Classify each as:

1. Suitable for AI automation
2. Suitable for AI-assisted work with human review
3. Best kept human-led

Estimate implementation difficulty and practical benefit. Recommend one low-risk task to automate first. Provide a step-by-step setup and testing plan, including how to check for errors.
```

### Improve your first draft

```text
Critique this draft as a demanding editor and experienced end user:

[DRAFT]

Target audience: [AUDIENCE]
Intended outcome: [OUTCOME]

Identify unclear assumptions, weak logic, generic content, usability problems, and missing evidence. Rank the five most important improvements.

Then help me revise one issue at a time. Do not flatter the draft.
```

## 9. 做軟體越容易，選對要做的軟體越重要

AI 讓「做出來」變得便宜，功能本身就很難構成護城河。[Reverse Engineer Anything（REA）](https://github.com/morluto/rea)是一個 MCP server，讓 AI coding agent 調用 Ghidra、Hopper、IDA 等既有的逆向工程工具，分析既有軟體並重建相容的行為。

從這類 demo 可以得到兩個教訓：別把 demo 當成 benchmark，也別用 GitHub 星數判斷工具；先用最簡單、能完成任務的方法。

| 容易被複製 | 比較守得住 |
| --- | --- |
| 通用的 AI 聊天套殼 | 深入特定領域、整合好的工作流程 |
| 常見的介面樣式 | 具合法使用權的專屬資料 |
| 單純的便利功能 | 可靠的端到端任務完成 |
| 一次性爆紅的 demo | 使用者反覆回來使用 |
| 只有功能本身 | 通路、信任、支援與執行力 |

更好的產品問題是：哪一個讓人挫折的流程，可以用幾個成熟的能力改善？

**法律與安全提醒**：只分析你有權檢視的軟體與環境；安裝第三方 MCP server 前，先檢查它要求的權限與依賴；尊重授權、智慧財產權與保密義務。重建行為不會讓你取得原始碼或授權，只適合用來學習與做原創實作。

---

[← 用 AI 思考](03-thinking-with-ai.md) · [第四部：學習與思考](README.md) · [目錄](../../README.zh-TW.md#目錄) · [與 AI 一起生活 →](05-living-with-ai.md)
