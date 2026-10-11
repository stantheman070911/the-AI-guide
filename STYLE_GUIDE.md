**English** | [繁體中文](STYLE_GUIDE.zh-TW.md)

# Style Guide

Conventions that keep the guide consistent as it grows. When this guide is silent, match the file you are editing.

## Voice

* **Practical and opinionated.** Say what to do and why. A clear recommendation is more useful than a neutral survey.
* **Conclusion first.** Put the most important point in the first sentence of a section.
* **Short and concrete.** Short sentences, common words, specific nouns and verbs. Cut filler and hype.
* **Address the reader as "you."**
* **Honest about uncertainty.** Separate facts, judgments, and guesses. Do not present a guess as a fact.

[Appendix A: Core Writing Principles](en/appendix/01-writing-principles.md) describes the same voice in more detail.

## Page structure

Every chapter follows the same shape:

1. **Navigation line** — a breadcrumb back to the contents and the part, plus the language switch.
2. **One `#` title** — the chapter name. Only one per file.
3. **Introduction** — one or two sentences on what the chapter covers and who it is for.
4. **Sections** — `##` for main sections, `###` for subsections. Number sections when order or cross-references matter.
5. **Footer navigation** — after a `---` rule: previous chapter, part, contents, next chapter.

Templates in [The Holy Trinity + 1](en/part-1-build/02-holy-trinity-plus-one/README.md) are meant to be copied into other projects, so they have no navigation lines.

## Markdown

* Use `*` for bullet lists in chapters. Keep each file consistent.
* Use bold for lead-in labels such as **Fix:** or **Principle:**. Do not bold whole sentences for emphasis.
* Use backticks for code, commands, file names, HTTP headers, and environment variables.
* Use relative links between pages, for example `../part-2-ship/01-production-readiness-checklist.md#18-secrets--api-keys`. Use full URLs only for external sites.
* Changing a heading changes its anchor. Run `python3 scripts/check_docs.py` after editing headings.
* Keep tables simple: short cells, no line breaks inside cells.
* Use the severity markers 🚨 Critical, 🔴 High, and 🟠 Medium only in the security playbook. Avoid other emoji.
* Use Markdown that GitHub renders natively. No HTML layouts, no build step.

## File names

* Lowercase English, words joined by hyphens: `02-security-remediation-playbook.md`.
* Chapters inside a part start with a two-digit number that sets the reading order.
* The English and Chinese versions use the same file name.
* Template files keep their upper-case names (`BRIEF.md`, `PLAN.md`), because other files refer to them by name.

## Facts, sources, and time

* Attribute quotations to a named person and use quotation marks only for exact wording. Label paraphrases as paraphrases.
* Link to primary sources for factual and legal claims where possible.
* Vendor features, prices, and limits change. When a statement depends on the current state of a product, write it so a reader can tell, and open an issue when you notice it has gone stale.
* Do not invent examples that look like real data, people, or companies. Use obvious placeholders.

## Chinese conventions

These apply to every page in `zh-TW/` and every `.zh-TW.md` file.

* **Traditional Chinese as used in Taiwan.** Use Taiwanese technical terms: 程式碼, 資料庫, 伺服器, 使用者, 預設, 範本, 介面. The [glossary](GLOSSARY.md) lists the agreed terms.
* **Full-width punctuation** in Chinese text: ，。：；！？、（）. Use 「」 for quotations and 『』 for quotations inside quotations.
* **Spaces between Chinese and Latin text or numbers**: 使用 Supabase Auth、每 15 分鐘 5 次. No space between Chinese text and full-width punctuation.
* **Move punctuation outside bold markers when text follows directly.** Write `**原則**：不要…`, not `**原則：**不要…`. GitHub's Markdown parser does not close a bold span that ends in full-width punctuation followed directly by Chinese text, and the asterisks show up as literal characters. A bold span that ends a line, or is followed by a space, is fine.
* **No italics for Chinese text.** Italic Chinese renders poorly and the same parser problem applies. Use 「」 to mark quoted phrases instead.
* **Keep the original form** of code, commands, file names, product names, skill names, and template placeholders.
* **Em dashes** in Chinese are written as a double dash: ——.
