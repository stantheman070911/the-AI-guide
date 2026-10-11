**English** | [繁體中文](CONTRIBUTING.zh-TW.md)

# Contributing

Thank you for helping improve the Vibecoding Guide. Corrections, clearer wording, translations, and new topics are all welcome. You do not need to be an engineer to contribute: many of the most useful changes are a sentence made clearer or a translation made more natural.

By taking part, you agree to follow the [Code of Conduct](CODE_OF_CONDUCT.md).

## Ways to contribute

| You want to… | Do this |
| --- | --- |
| Fix a typo, broken link, or small error | Open a pull request directly. |
| Report something wrong or outdated | [Open an issue](https://github.com/stantheman070911/vibecoding-guide/issues/new/choose) with the page and, if possible, a source. |
| Improve or fix a translation | Open a pull request, or an issue if you are unsure. |
| Propose a new topic or chapter | Open an issue first, so we can agree on scope and placement before you write. |
| Restructure existing content | Open an issue first. Moving content breaks links and translations, so it needs agreement. |

## How the repository is organized

```text
README.md, README.zh-TW.md     Landing page and table of contents
CONTRIBUTING*.md               This guide
CODE_OF_CONDUCT*.md            Community rules
STYLE_GUIDE*.md                Writing and formatting conventions
GLOSSARY.md                    English ↔ Traditional Chinese terminology
en/                            English pages
  part-1-build/                Part 1: Build
  part-2-ship/                 Part 2: Ship
  part-3-craft/                Part 3: Craft
  appendix/                    Prompts and notes
zh-TW/                         Traditional Chinese pages, same paths as en/
scripts/check_docs.py          Link and language-parity checker
.github/                       Issue and pull request templates, CI
```

Each part folder has a `README.md` that introduces the part and lists its chapters.

## The bilingual rule

Every page exists in English and Traditional Chinese (繁體中文).

* **Pages in `en/` and `zh-TW/` mirror each other.** The same file name at the same path, with the same headings in the same order.
* **Root files use a suffix.** `README.md` pairs with `README.zh-TW.md`, `CONTRIBUTING.md` with `CONTRIBUTING.zh-TW.md`, and so on. `GLOSSARY.md` is a single bilingual file. `LICENSE` stays in English only.
* **English is the source language**, except for pages marked otherwise at the top. [Appendix A](en/appendix/01-writing-principles.md) was written in Chinese, so the Chinese version is authoritative there.
* **Both versions must say the same thing.** They may phrase it differently, but they must carry the same facts, claims, degree of certainty, and structure.

### Keeping translations in sync

When you change a page, try to update both languages in the same pull request.

If you can only write in one language, that is fine. Do this instead:

1. Make your change in the language you know.
2. At the top of the other-language version, under the navigation line, add a notice:

   In a Chinese page:

   ```markdown
   > **翻譯待更新**：英文版已於 YYYY-MM-DD 更新，此翻譯尚未同步。請參考[英文版](../../en/path/to/page.md)。
   ```

   In an English page:

   ```markdown
   > **Translation pending:** The Chinese version was updated on YYYY-MM-DD and this translation has not caught up yet. See the [Chinese version](../../zh-TW/path/to/page.md).
   ```

3. In the pull request template, tick "Translation pending". A maintainer or another contributor will finish the translation and remove the notice.

### Translation guidelines

* Translate the meaning, not the words. Read the paragraph, then write it the way a native speaker would.
* Keep the claims exact. Do not strengthen, soften, add, or drop anything.
* Use the terms in the [glossary](GLOSSARY.md). If a term is missing, add it in your pull request.
* Leave these in their original form: code, commands, file names, product and company names, skill names, and template placeholders such as `[PROJECT_NAME]`.
* Follow the language-specific rules in the [style guide](STYLE_GUIDE.md#chinese-conventions).

## Making a change

1. Fork the repository and create a branch with a short descriptive name, such as `fix-checklist-typo` or `translate-copywriting`.
2. Edit the Markdown files. The [style guide](STYLE_GUIDE.md) covers voice, structure, and formatting.
3. Run the checker from the repository root. It needs only Python 3:

   ```bash
   python3 scripts/check_docs.py
   ```

   It reports broken links, missing anchors, pages without a counterpart, and pages whose two versions have different heading structures.
4. Open a pull request and fill in the template. Keep each pull request focused on one change.

The same checker runs automatically on every pull request. It also warns when only one language of a page changed. A warning does not block merging; it is a reminder to add the translation or the "translation pending" notice.

## Adding a chapter

1. Open an issue proposing the chapter, its part, and a short outline.
2. Create the file in both `en/` and `zh-TW/`, in the chosen part folder. Name it with the next two-digit number and a lowercase, hyphenated English title, such as `03-observability.md`.
3. Copy the navigation lines from a neighboring chapter: the breadcrumb and language link at the top, and the previous/next links at the bottom. Update the previous/next links on the neighboring chapters too.
4. Add the chapter to the part's `README.md` and to the table of contents in `README.md` and `README.zh-TW.md`. Add a row to "Quick lookup" if the chapter answers a common question.
5. Run the checker.

Adding a new part follows the same pattern: create `part-N-name/` in both languages with a `README.md`, then add it to both root READMEs.

## Content standards

* **Accuracy over completeness.** Do not add claims you cannot support. If something is uncertain, say so.
* **Cite sources for facts.** Link to primary sources (official documentation, standards, original research) where possible. Mark direct quotes with quotation marks and name the speaker; label paraphrases as paraphrases.
* **Keep it practical.** Prefer what to do and how to check it over general commentary.
* **No promotion.** Vendor names are fine when they help a decision. Affiliate links, sponsored placements, and undisclosed relationships are not accepted. Disclose any affiliation with a product you write about.
* **No sensitive data.** Never include real credentials, API keys, private URLs, or personal information, even as examples. Use obvious placeholders.

## Reviews

A maintainer reviews every pull request for accuracy, clarity, consistency with the style guide, and language parity. Expect questions; they are part of making the guide reliable, not a judgment of your work. Small fixes are usually merged quickly. Larger changes may take a few rounds.

## License

By contributing, you agree that your contributions are released under the repository's [license](LICENSE).
