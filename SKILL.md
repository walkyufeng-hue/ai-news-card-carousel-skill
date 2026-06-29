---
name: ai-news-card-carousel-skill
description: Turn AI hot news, AI tool updates, and AI product changes into Douyin and Xiaohongshu-friendly visual note carousel scripts, with page-by-page copy, visual layout guidance, sources, deduplication checks, and a 20–30 Chinese character summary caption.
---

# AI News Card Carousel Skill

## Purpose

Turn one AI news item, AI tool update, AI product change, AI industry event, or AI concept into a concise Chinese carousel script for Douyin image posts and Xiaohongshu notes.

The output should feel like a clean AI knowledge card series: light paper background, subtle dot grid, deep green emphasis, large titles, short explanations, and one idea per page.

## When To Use

Use this skill when the user asks to:

- Turn AI news into Douyin or Xiaohongshu carousel copy.
- Create AI hotspot image-text scripts, visual-note scripts, card scripts, or AI knowledge cards.
- Explain an AI product update in a way ordinary readers can understand.
- Pick one AI topic from multiple AI updates and package it for short-form social posting.
- Generate a 5-7 page AI carousel with cover titles, page copy, layout notes, captions, hashtags, source notes, and a publishing checklist.

If the user asks for "today", "latest", "recent", or current AI hot topics, verify current facts with reliable sources before selecting the topic.

## What This Skill Does

- Select one topic that is suitable for carousel storytelling.
- Check whether it repeats a provided or available topic history.
- Extract core facts and explain the meaning in plain Chinese.
- Produce a default 6-page carousel script, or 5-7 pages when the user asks.
- Include page number, column label, main title, body copy, key terms, layout direction, and visual hints for every page.
- Provide 3 cover-title options.
- Provide one 20–30 Chinese character summary caption, never over 35 Chinese characters.
- Provide Douyin/Xiaohongshu post copy, hashtags, comment prompt, source notes, and pre-publishing checks.

## What This Skill Does Not Do

- Do not directly generate images.
- Do not publish to Douyin, Xiaohongshu, or any other platform.
- Do not save platform drafts.
- Do not invent news, dates, product capabilities, quotes, or sources.
- Do not copy long passages from source articles.
- Do not use exaggerated clickbait, marketing-account language, or alarmist claims.
- Do not imitate any real account name, avatar, visual asset, or proprietary style.

## Core Workflow

1. Gather candidate material.
   - If the user provides news, use that material and ask for missing source links only when the factual risk is high.
   - If the user asks for current AI hotspots, search reliable recent sources and compare dates.
   - Prefer official blogs, release notes, research papers, company announcements, reputable media, and primary demos.

2. Select one topic.
   - Use `references/topic-selection-rules.md` when judging multiple candidates.
   - Prefer topics with clear user impact, product meaning, and visual-card readability.
   - Avoid topics that require too much technical background to explain in six short pages.

3. Check for repetition.
   - Compare against any history supplied by the user.
   - If no history is available, state that the duplicate check is limited.
   - Use `references/dedupe-rules.md` for title, keyword, and semantic checks.

4. Extract facts.
   - Separate confirmed facts from interpretation.
   - Keep source links and dates visible in the output.
   - When a fact is uncertain, label it as a point to verify before publishing.

5. Translate facts into reader meaning.
   - Explain what changed, why it matters, who is affected, and what signal it sends.
   - Use analogies and product-thinking language, not technical jargon.

6. Generate the carousel.
   - Default to 6 pages: cover, myth, metaphor, breakdown, impact, recap.
   - Keep each page focused on one idea.
   - Keep page body copy under 80 Chinese characters when possible.
   - Add layout and visual prompts for manual design in Figma, Canva, Gaoding, Xingtu, or similar tools.

7. Finish with publishing support.
   - Add 3 cover-title options.
   - Add one 20–30 Chinese character summary caption.
   - Add Douyin/Xiaohongshu body copy, hashtags, comment prompt, sources, verification reminders, and a checklist.

## Content Structure

Use the default 6-page structure unless the user asks for another page count or the topic clearly needs a different structure.

1. Cover
   - Purpose: make the reader stop.
   - Include main title, subtitle, column name, and small tags.
   - Keep the title knowledge-card-like, not sales-like.

2. Misconception / THE MYTH
   - Purpose: name the common misunderstanding.
   - Use a "你以为 / 其实" contrast.
   - Mark one or two key terms.

3. Metaphor / THE METAPHOR
   - Purpose: explain the change with a daily-life analogy.
   - Avoid dense model or engineering terms.

4. Breakdown / THE BREAKDOWN
   - Purpose: split the change into 2-3 short points.
   - Use bullet-friendly copy.

5. Impact / THE IMPACT
   - Purpose: explain why this deserves attention.
   - Pick the most relevant angle: ordinary users, product managers, designers, creators, developers, or industry signals.

6. Recap / RECAP
   - Purpose: close with a memorable idea.
   - Use 3-4 mini recap cards plus one final sentence or comment question.

For alternatives such as AI news quick read, tool update, concept explainer, or product-manager analysis, read `references/carousel-page-structure.md`.

## Visual Style Guidance

- Main ratio: 9:16 for Douyin image posts.
- Compatible ratio: 3:4 for Xiaohongshu.
- Background: off-white or light gray-white.
- Texture: very subtle dot grid.
- Main accent: deep green.
- Text: black or dark gray.
- Secondary color: light gray.
- Typography feel: modern, clean, restrained, editorial note-like.
- Layout: large title, short body, emphasized key terms.
- Whitespace: generous; do not fill the page.
- Decoration: minimal; no complex illustration, busy stickers, heavy emoji, or aggressive gradients.
- Per page: highlight only 1-3 key terms.

Read `references/visual-style-guide.md` when the user asks for more detailed layout direction.

## Writing Rules

- Write like a person who understands AI explaining it to a smart non-expert.
- Be conversational but not sloppy.
- Have a point of view, but do not overstate certainty.
- Explain technical terms the first time they appear.
- Use short sentences and short paragraphs.
- Avoid press-release tone.
- Avoid long source summaries.
- Avoid "震惊", "颠覆", "炸裂", "普通人必须知道", and similar clickbait patterns unless quoting a source for critique.
- Keep every page copy easy to paste into a visual design tool.

Read `references/writing-style-rules.md` for the stricter copy checklist.

## Output Format

Always output in this structure:

```markdown
# AI 热点图文卡片脚本

## 1. 热点标题

## 2. 新闻来源
- 来源：
- 链接：
- 时间：
- 核查状态：

## 3. 是否重复判断
- 是否与历史选题重复：
- 判断原因：

## 4. 为什么值得做成图文

## 5. 推荐封面标题
1.
2.
3.

## 6. 图文页内容

### 第 1 页｜封面
- 栏目小标题：
- 主标题：
- 副标题：
- 重点词：
- 版式说明：
- 视觉提示：

### 第 2 页｜误区 / THE MYTH
- 栏目小标题：
- 主标题：
- 正文：
- 重点词：
- 版式说明：
- 视觉提示：

### 第 3 页｜比喻 / THE METAPHOR
- 栏目小标题：
- 主标题：
- 正文：
- 重点词：
- 版式说明：
- 视觉提示：

### 第 4 页｜拆解 / THE BREAKDOWN
- 栏目小标题：
- 主标题：
- 正文：
- 重点词：
- 版式说明：
- 视觉提示：

### 第 5 页｜影响 / THE IMPACT
- 栏目小标题：
- 主标题：
- 正文：
- 重点词：
- 版式说明：
- 视觉提示：

### 第 6 页｜总结 / RECAP
- 栏目小标题：
- 主标题：
- 正文：
- 重点词：
- 版式说明：
- 视觉提示：

## 7. 20–30 字概述文案

## 8. 抖音 / 小红书发布文案
- 正文：
- 话题标签：
- 评论区引导：

## 9. 发布前检查
- 是否有可靠来源：
- 是否避免夸大：
- 是否适合普通人理解：
- 是否每页只讲一个重点：
- 是否适合抖音图文：
- 是否适合小红书图文：
- 是否可以直接复制使用：
```

## Publishing Checklist

Before finalizing, check:

- Sources are reliable and linked.
- Dates are clear, especially for current news.
- The duplicate judgment is explained.
- The script does not exaggerate or invent claims.
- Technical terms are explained.
- Every page has only one main point.
- The summary caption is 20–30 Chinese characters when possible and under 35.
- Douyin/Xiaohongshu copy is easy to paste and not overloaded with hashtags.
- The output includes clear manual layout guidance but does not claim to generate images.
