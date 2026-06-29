#!/usr/bin/env python3
"""Format one mock AI news item as a carousel-script Markdown skeleton."""

from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any


SAMPLE_NEWS = {
    "title": "AI 写作工具加入团队知识库能力",
    "source": "Product Release Notes",
    "url": "https://example.com/release-notes",
    "published_at": "2026-06-18",
    "summary": "某 AI 写作工具允许团队把内部文档接入写作流程，让输出更贴近公司语境。",
    "keywords": ["AI 写作", "知识库", "团队协作", "上下文"],
}


def load_news(path: str | None) -> dict[str, Any]:
    if not path:
        return SAMPLE_NEWS
    data = json.loads(Path(path).read_text(encoding="utf-8"))
    if isinstance(data, list):
        if not data:
            raise SystemExit("news file contains an empty list")
        data = data[0]
    if not isinstance(data, dict):
        raise SystemExit("news file must contain a JSON object or a non-empty list")
    return data


def keywords_text(news: dict[str, Any]) -> str:
    keywords = news.get("keywords") or []
    return "、".join(str(item) for item in keywords[:3])


def render_markdown(news: dict[str, Any]) -> str:
    title = str(news.get("title", "未命名 AI 热点"))
    source = str(news.get("source", "待补充"))
    url = str(news.get("url", "待补充"))
    published_at = str(news.get("published_at", "待补充"))
    summary = str(news.get("summary", "待补充"))
    keywords = keywords_text(news)

    return f"""# AI 热点图文卡片脚本

## 1. 热点标题
{title}

## 2. 新闻来源
- 来源：{source}
- 链接：{url}
- 时间：{published_at}
- 核查状态：示例脚本输出，发布前请复核原始来源。

## 3. 是否重复判断
- 是否与历史选题重复：未接入历史记录，无法完整判断。
- 判断原因：请用 dedupe_topics.py 或人工历史选题表继续核查。

## 4. 为什么值得做成图文
这条热点适合拆成图文，因为它不只是功能变化，也涉及用户工作流的变化。普通读者能通过“少切换工具、少补充背景”的角度理解它。

## 5. 推荐封面标题
1. AI 工具真正变了
2. 重点不是更会写
3. 它开始懂你的上下文

## 6. 图文页内容

### 第 1 页｜封面
- 栏目小标题：AI PRODUCT NOTE
- 主标题：AI 工具真正变了
- 副标题：重点不是功能更多，而是更懂你的上下文
- 重点词：{keywords}
- 版式说明：大标题居中偏上，副标题分两行放在下方。
- 视觉提示：米白底、浅点阵、深绿色标出关键词。

### 第 2 页｜误区 / THE MYTH
- 栏目小标题：THE MYTH
- 主标题：你以为只是多了个按钮
- 正文：你以为它只是功能升级，其实它在把资料、写作和协作放进同一个流程。
- 重点词：功能升级、同一个流程
- 版式说明：上下分区写“你以为 / 其实”。
- 视觉提示：用细线分隔两块内容，重点词用深绿色。

### 第 3 页｜比喻 / THE METAPHOR
- 栏目小标题：THE METAPHOR
- 主标题：它更像一个随身资料员
- 正文：你不用每次重新解释背景，它能先拿到资料，再帮你组织表达。
- 重点词：资料员、背景
- 版式说明：主标题放大，正文控制在三行以内。
- 视觉提示：保留大面积留白，右下角放小标签。

### 第 4 页｜拆解 / THE BREAKDOWN
- 栏目小标题：THE BREAKDOWN
- 主标题：这件事可以拆成 3 点
- 正文：1. 资料接入更近。2. 写作上下文更完整。3. 团队表达更容易统一。
- 重点词：资料、上下文、统一
- 版式说明：三条项目符号纵向排列。
- 视觉提示：每条前面用小圆点或短横线，不加复杂插画。

### 第 5 页｜影响 / THE IMPACT
- 栏目小标题：THE IMPACT
- 主标题：对产品经理尤其值得看
- 正文：AI 工具的竞争，正在从“生成得好不好”转向“能不能进入真实工作流”。
- 重点词：真实工作流
- 版式说明：一句大观点加一行解释。
- 视觉提示：把“真实工作流”做成深绿色强调。

### 第 6 页｜总结 / RECAP
- 栏目小标题：RECAP
- 主标题：这不是单点功能更新
- 正文：复盘：资料更近、上下文更全、协作更顺。你会把 AI 接进团队知识库吗？
- 重点词：资料更近、上下文更全
- 版式说明：上方三张小复盘卡，下方放评论问题。
- 视觉提示：小卡片用浅灰边框，整体保持清爽。

## 7. 20–30 字概述文案
AI 工具变化，重点正在转向真实工作流

## 8. 抖音 / 小红书发布文案
- 正文：{summary} 这类更新值得关注，因为它让 AI 从“单次生成”更靠近“持续协作”。
- 话题标签：#AI工具 #AI产品 #产品经理 #小红书图文
- 评论区引导：你更希望 AI 帮你写内容，还是先读懂资料？

## 9. 发布前检查
- 是否有可靠来源：待复核
- 是否避免夸大：是
- 是否适合普通人理解：是
- 是否每页只讲一个重点：是
- 是否适合抖音图文：是
- 是否适合小红书图文：是
- 是否可以直接复制使用：是
"""


def main() -> None:
    parser = argparse.ArgumentParser(description="Format mock AI news as Markdown.")
    parser.add_argument("--news-file", help="Path to a news JSON file.")
    args = parser.parse_args()

    print(render_markdown(load_news(args.news_file)))


if __name__ == "__main__":
    main()
