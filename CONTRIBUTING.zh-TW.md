[English](CONTRIBUTING.md) | **繁體中文**

# 貢獻指南

歡迎修正錯誤、讓用字更清楚、翻譯，以及提議新主題。

參與本專案，即表示你同意遵守[行為準則](CODE_OF_CONDUCT.zh-TW.md)。

## 貢獻方式

| 你想要…… | 請這樣做 |
| --- | --- |
| 修正錯字、失效連結或小錯誤 | 直接開 pull request。 |
| 回報錯誤或過時的內容 | [開一個 issue](https://github.com/stantheman070911/the-AI-guide/issues/new/choose)，註明頁面，可以的話附上來源。 |
| 改善或修正翻譯 | 開 pull request；如果不確定，先開 issue。 |
| 提議新主題或新章節 | 先開 issue，讓我們在你動筆前，先對範圍與位置達成共識。 |
| 重新調整既有內容的結構 | 先開 issue。搬動內容會破壞連結與翻譯，因此需要事先取得共識。 |

## 儲存庫的組織方式

```text
README.md, README.zh-TW.md     首頁與目錄
CONTRIBUTING*.md               本指南
CODE_OF_CONDUCT*.md            社群規範
STYLE_GUIDE*.md                寫作與格式慣例
GLOSSARY.md                    英文 ↔ 繁體中文術語對照
en/                            英文頁面
  part-1-build/                第一部：打造
  part-2-ship/                 第二部：上線
  part-3-craft/                第三部：打磨
  appendix/                    提示詞與筆記
zh-TW/                         繁體中文頁面，路徑與 en/ 相同
scripts/check_docs.py          連結與雙語對應檢查工具
.github/                       Issue 與 pull request 範本、CI
```

每個「部」的資料夾都有一個 `README.md`，介紹該部並列出它的章節。

## 雙語規則

每一頁都有英文與繁體中文兩個版本。

* **`en/` 與 `zh-TW/` 中的頁面互相對應。** 相同的路徑、相同的檔名，標題相同且順序一致。
* **根目錄的檔案使用後綴。** `README.md` 對應 `README.zh-TW.md`，`CONTRIBUTING.md` 對應 `CONTRIBUTING.zh-TW.md`，以此類推。`GLOSSARY.md` 是單一的雙語檔案。`LICENSE` 與 `LICENSE-CODE` 只保留英文。
* **英文是來源語言**，除非頁面頂端另有標示。[附錄 A](zh-TW/appendix/01-writing-principles.md) 原本以中文撰寫，因此該頁以中文版為準。
* **兩個版本必須說同樣的事。** 措辭可以不同，但事實、主張、確定程度與結構必須一致。

### 保持翻譯同步

修改頁面時，請盡量在同一個 pull request 中同時更新兩種語言。

如果你只用其中一種語言寫作：

1. 用你熟悉的語言完成修改。
2. 在另一種語言版本的頂端、導覽列下方，加上提示：

   在中文頁面中：

   ```markdown
   > **翻譯待更新**：英文版已於 YYYY-MM-DD 更新，此翻譯尚未同步。請參考[英文版](../../en/path/to/page.md)。
   ```

   在英文頁面中：

   ```markdown
   > **Translation pending:** The Chinese version was updated on YYYY-MM-DD and this translation has not caught up yet. See the [Chinese version](../../zh-TW/path/to/page.md).
   ```

3. 在 pull request 範本中勾選「翻譯待更新」。維護者或其他貢獻者會完成翻譯並移除提示。

### 翻譯準則

* 翻譯意思，而不是逐字翻譯。先讀懂整段，再用母語者會用的方式寫出來。
* 主張要精確。不要加強、弱化、增加或刪減任何內容。
* 使用[詞彙表](GLOSSARY.md)中的術語。如果缺少某個術語，請在你的 pull request 中加上。
* 以下內容保留原文：程式碼、指令、檔名、產品與公司名稱、skill 名稱，以及 `[PROJECT_NAME]` 這類範本佔位符。
* 遵守[風格指南](STYLE_GUIDE.zh-TW.md#中文慣例)中的中文規則。

## 提出修改

1. Fork 這個儲存庫，並建立一個名稱簡短、具描述性的分支，例如 `fix-checklist-typo` 或 `translate-copywriting`。
2. 編輯 Markdown 檔案。[風格指南](STYLE_GUIDE.zh-TW.md)說明了語氣、結構與格式。
3. 在儲存庫根目錄執行檢查工具。它只需要 Python 3：

   ```bash
   python3 scripts/check_docs.py
   ```

   它會回報失效的連結、不存在的錨點、缺少對應版本的頁面，以及兩個語言版本標題結構不同的頁面。
4. 開 pull request 並填寫範本。每個 pull request 只聚焦在一項修改。

同一個檢查工具會在每個 pull request 上自動執行。當某一頁只改了其中一種語言時，它也會發出警告。警告不會阻擋合併；它只是提醒你補上翻譯，或加上「翻譯待更新」提示。

## 新增章節

1. 開一個 issue，提出章節、所屬的部，以及簡短大綱。
2. 在 `en/` 與 `zh-TW/` 中、選定的部資料夾內建立檔案。檔名使用下一個兩位數編號，加上小寫、以連字號連接的英文標題，例如 `03-observability.md`。
3. 從相鄰的章節複製導覽列：頂端的麵包屑與語言連結，以及底部的上一章／下一章連結。也要一併更新相鄰章節的上一章／下一章連結。
4. 把章節加入該部的 `README.md`，以及 `README.md` 與 `README.zh-TW.md` 的目錄。如果這一章能回答常見問題，也在「快速查詢」加上一列。
5. 執行檢查工具。

新增一個部的方式相同：在兩種語言中各建立 `part-N-name/` 資料夾與 `README.md`，然後把它加入兩份根目錄 README。

## 內容標準

* **準確優先於完整。** 不要加入你無法佐證的主張。不確定的事，就直說不確定。
* **事實要附來源。** 盡可能連結到第一手來源（官方文件、標準、原始研究）。直接引言要加引號並註明說話者；轉述要標明是轉述。
* **保持實用。** 比起泛泛而談，優先寫該做什麼、如何檢查。
* **不做推銷。** 能幫助決策時，提到供應商名稱沒有問題。不接受聯盟行銷連結、付費置入與未揭露的關係。若你與所撰寫的產品有任何關係，請揭露。贊助、熱門程度與出現在影片中都不是品質的證據；推薦必須經過[附錄 D](zh-TW/appendix/04-evaluating-tools-and-skills.md)的審查。
* **不含敏感資料。** 絕不放入真實的憑證、API 金鑰、私人網址或個人資訊，即使作為範例也不行。請使用明顯的佔位內容。

## 審查

維護者會審查每個 pull request 的準確性、清晰度、與風格指南的一致性，以及雙語對應。

## 授權

貢獻內容即表示你同意你的貢獻以相同條件發布：文字內容採用 [CC BY 4.0](LICENSE)，程式碼與範本採用 [MIT 授權條款](LICENSE-CODE)。
