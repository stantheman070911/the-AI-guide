[目錄](../../README.zh-TW.md#目錄) › [附錄](README.md) · [English](../../en/appendix/03-skills-and-tools.md) | **繁體中文**

# 附錄 C：我使用的 Skills 與工具

這是我持續更新的清單，列出我安裝的 Claude Code skills、外掛與命令列工具。

Skill 名稱保留工具中顯示的原樣，因此不翻譯。分組依照每個 skill 的來源。這是個人清單，不是推薦；安裝工具前如何審查，請見[附錄 D](04-evaluating-tools-and-skills.md)。

## Claude Code／設定

* update-config, keybindings-help, fewer-permission-prompts, init, run, claude-api

## 程式碼審查

* code-review, simplify, security-review

## 排程／自動化

* loop, schedule

## Artifacts 與資料視覺化

* artifact-design, artifact-diagramming, artifact-capabilities, dataviz, design（Claude Design 畫布）

## 文件／辦公

* docx, pptx, xlsx, pdf

## Anthropic 其他

* consolidate-memory, explain-usage, import-memory, morning, schedule, setup-cowork, setup-writing-style, skill-creator

## Vercel

* bootstrap, deploy, env, marketplace, status, ai-gateway, ai-sdk, auth, chat-sdk, deployments-cicd, env-vars, knowledge-update, microfrontends, next-cache-components, next-forge, next-upgrade, nextjs, react-best-practices, routing-middleware, runtime-cache, shadcn, turbopack, vercel-agent, vercel-cli, vercel-connect, vercel-firewall, vercel-functions, vercel-sandbox, vercel-storage, verification, workflow

## Context7（文件）

* context7, docs, context7-mcp, docs-researcher（agent）

## Superpowers（工作流程／流程）

* brainstorming, dispatching-parallel-agents, executing-plans, finishing-a-development-branch, receiving-code-review, requesting-code-review, subagent-driven-development, systematic-debugging, test-driven-development, using-git-worktrees, using-superpowers, verification-before-completion, writing-plans, writing-skills

## UI/UX

* ui-ux-pro-max

## Ponytail

強迫採用仍然可行的最簡單、最省力的解法。在寫程式碼之前，先質疑它是否根本需要存在。

* ponytail, ponytail-review, ponytail-audit, ponytail-gain, ponytail-debt, ponytail-help

## Impeccable

前端工作的設計素養：打磨、稽核、評論、動畫，總共 23 個提升 UI 品質的指令（`/impeccable polish`、`/impeccable audit` 等）。

* impeccable

## Sepia

去 AI 味的寫作：讓 AI 生成的文字讀起來像人寫的。針對小說的敘事架構修復（StoryScope，arXiv:2604.03136），另有適用於版本發布說明、PR／issue 回覆、事後檢討、工單與技術文章的領域模式。可撰寫、審查、重構、重寫。來源：[Nanako0129/sepia](https://github.com/Nanako0129/sepia)。

* sepia

## 動畫與動態

* animate, animate-expo, animation-vocabulary, apple-design, find-animation-opportunities, improve-animations, review-animations, gsap-core, gsap-frameworks, gsap-performance, gsap-plugins, gsap-react, gsap-scrolltrigger, gsap-timeline, gsap-utils

## 設計／UI（前端與視覺）

* design-taste-frontend, design-taste-frontend-v1, hallmark, high-end-visual-design, minimalist-ui, industrial-brutalist-ui, gpt-taste, stitch-design-taste, redesign-existing-projects, emil-design-eng

## 圖片生成

* brandkit, imagegen-frontend-mobile, imagegen-frontend-web, image-to-code

## 影片／HyperFrames

* hyperframes, hyperframes-animation, hyperframes-cli, hyperframes-core, hyperframes-creative, hyperframes-keyframes, hyperframes-registry, general-video, media-use

## Toast／通知

* ask-sonner, telegram-notify

## 寫作／語言

* speak-human-zh-tw, full-output-enforcement

## Swift

* write-swift

## graphify

把任何輸入（程式碼、文件、論文、圖片、影片）轉成一個持久的知識圖譜，具備 god nodes、社群偵測，以及 query／path／explain 工具。

## eli5

針對特定受眾（年齡、年級、職務或關係）解釋任何主題、程式碼或錯誤。來源：[DreambigOu/ELI5](https://github.com/DreambigOu/ELI5)。

## open-slide

這是命令列工具，不是 skill。執行 `npx @open-slide/cli init <name>`，會建立一個預先設定好 Claude Code skills 的簡報工作區。網站：[open-slide.dev](https://open-slide.dev)。

---

[← 附錄 B：CLAUDE.md 預設範本](02-claude-md-coding-rules.md) · [附錄](README.md) · [目錄](../../README.zh-TW.md#目錄) · [附錄 D：評估工具與 Skills →](04-evaluating-tools-and-skills.md)
