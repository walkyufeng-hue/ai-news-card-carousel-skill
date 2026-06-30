---
name: ai-news-card-carousel-skill
description: Turn AI hot news, AI tool updates, and AI product changes into Douyin and Xiaohongshu-friendly Chinese carousel scripts and optional 1080x1440 dark prompt-style PNG cards branded YF拾光机. Use when creating AI hotspot visual-note content, page-by-page card copy, source-grounded social captions, or rendered image cards.
---

# AI News Card Carousel Skill

## Purpose

Turn one AI news item, AI tool update, AI product change, AI industry event, or AI concept into a concise Chinese carousel script and, when requested, rendered `1080x1440` PNG cards.

Default style: dark AI prompt-card aesthetic, subtle green glow, thin borders, compact information blocks, fixed `YF拾光机` brand label at the top-left of every card, and page number such as `2/6` retained at the bottom-right.

## What This Skill Does

- Select one AI topic suitable for carousel storytelling.
- Verify current facts from reliable sources when the user asks for today/latest/recent AI hotspots.
- Check topic repetition internally when history is available, but do not output a separate duplicate-judgment section unless the user asks.
- Convert facts into short, plain-language Chinese card copy.
- Generate default 6-page carousel content.
- Generate 3 cover-title options.
- Generate Douyin/Xiaohongshu post copy.
- When asked for images, create a JSON input and run `scripts/render_cards.py` to output PNG cards.

## What This Skill Does Not Do

- Do not invent news, dates, product capabilities, quotes, or sources.
- Do not copy long passages from source articles.
- Do not use exaggerated clickbait or fear hooks.
- Do not publish to Douyin, Xiaohongshu, or any other platform.
- Do not save platform drafts.

## Core Workflow

1. Gather candidate material.
   - If the user provides news, use it and verify risky claims.
   - If the user asks for current AI hotspots, search reliable recent sources and compare dates.
   - Prefer official blogs, release notes, research papers, company announcements, reputable media, and primary demos.

2. Select one topic.
   - Use `references/topic-selection-rules.md` when comparing candidates.
   - Prefer topics with clear user impact, product meaning, and card readability.
   - Avoid topics that require too much technical background to explain in six short pages.

3. Check repetition internally.
   - Compare against any user-provided history.
   - If no history is available, do not expose a full duplicate section; mention repetition risk only if it affects the recommendation.
   - Use `references/dedupe-rules.md` for title, keyword, and semantic checks.

4. Extract and explain facts.
   - Separate confirmed facts from interpretation.
   - Keep source links and dates in the output.
   - Label uncertain points as source-check reminders in the source section only when necessary.

5. Generate the carousel script.
   - Default to 6 pages: cover, misconception, metaphor, breakdown, impact, recap.
   - Keep each page focused on one idea.
   - Keep page body copy short enough for visual layout.
   - Use `YF拾光机` as the fixed top-left brand label for every page.

6. Render images when requested.
   - Create a JSON file matching the `scripts/render_cards.py` input shape.
   - Run:

```bash
python3 scripts/render_cards.py path/to/cards.json --output output/topic-cards
```

   - The script requires Pillow. If missing, install it:

```bash
python3 -m pip install Pillow
```

## Output Format

Always use this simplified Markdown structure:

```markdown
# AI 热点图文卡片脚本

## 1. 热点标题

## 2. 新闻来源
- 来源：
- 链接：
- 时间：
- 核查状态：

## 3. 推荐封面标题
1.
2.
3.

## 4. 图文页内容

### 第 1 页｜封面
- 品牌标识：YF拾光机
- 主标题：
- 副标题：
- 正文：
- 重点词：
- 图片说明：

### 第 2 页｜误区
- 品牌标识：YF拾光机
- 主标题：
- 正文：
- 重点词：
- 图片说明：

### 第 3 页｜比喻
- 品牌标识：YF拾光机
- 主标题：
- 正文：
- 重点词：
- 图片说明：

### 第 4 页｜拆解
- 品牌标识：YF拾光机
- 主标题：
- 正文：
- 重点词：
- 图片说明：

### 第 5 页｜影响
- 品牌标识：YF拾光机
- 主标题：
- 正文：
- 重点词：
- 图片说明：

### 第 6 页｜总结
- 品牌标识：YF拾光机
- 主标题：
- 正文：
- 重点词：
- 图片说明：

## 5. 抖音 / 小红书发布文案
- 正文：
- 话题标签：
- 评论区引导：
```

Do not output legacy analysis, caption, or checklist sections unless the user explicitly asks for them.

## Image Card Defaults

- Size: `1080x1440` pixels.
- Ratio: `3:4`.
- Style: dark AI prompt-card, inspired by technical prompt-note pages.
- Brand: `YF拾光机` fixed at the top-left of every page.
- Page number: keep `1/6`, `2/6`, etc. at the bottom-right.
- Do not include footer text such as `适合抖音图文 · 小红书笔记`.
- Use deep black, dark green, translucent panels, fine green borders, and restrained neon-green highlights.
- Prefer structured content blocks over long paragraphs.
- Keep text legible on mobile.

Read `references/visual-style-guide.md` for detailed image styling.

## Writing Rules

- Write in Chinese by default.
- Sound like a thoughtful AI practitioner explaining the point to a smart non-expert.
- Be conversational, clear, and calm.
- Have a point of view, but do not overstate certainty.
- Explain technical terms the first time they appear.
- Avoid press-release tone.
- Avoid long source summaries.
- Avoid "震惊", "颠覆", "炸裂", "普通人必须知道", and similar clickbait patterns.
- Keep every page easy to render as a card image.
