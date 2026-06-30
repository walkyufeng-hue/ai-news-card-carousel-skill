#!/usr/bin/env python3
"""Format one AI news item as the simplified carousel Markdown output."""

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
    "keywords": ["AI 写作", "知识库", "团队协作"],
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


def render_markdown(news: dict[str, Any]) -> str:
    title = str(news.get("title", "未命名 AI 热点"))
    source = str(news.get("source", "待补充"))
    url = str(news.get("url", "待补充"))
    published_at = str(news.get("published_at", "待补充"))
    summary = str(news.get("summary", "待补充"))
    keywords = "、".join(str(item) for item in (news.get("keywords") or [])[:3])

    return f"""# AI 热点图文卡片脚本

## 1. 热点标题
{title}

## 2. 新闻来源
- 来源：{source}
- 链接：{url}
- 时间：{published_at}
- 核查状态：示例脚本输出，发布前请复核原始来源。

## 3. 推荐封面标题
1. AI 工具真正变了
2. 重点不是更会写
3. 它开始懂你的上下文

## 4. 图文页内容

### 第 1 页｜封面
- 品牌标识：YF拾光机
- 主标题：AI 工具真正变了
- 副标题：重点不是功能更多，而是更懂你的上下文
- 正文：这次更新可以理解为，AI 工具正在从“单次生成”靠近“持续协作”。
- 重点词：{keywords}
- 图片说明：1080x1440 暗色 prompt 卡片，顶部固定 YF拾光机，底部保留 1/6 页码。

### 第 2 页｜误区
- 品牌标识：YF拾光机
- 主标题：你以为只是多了个按钮
- 正文：你以为它只是功能升级，其实它在把资料、写作和协作放进同一个流程。
- 重点词：功能升级、同一个流程
- 图片说明：用两个暗色内容块做“你以为 / 其实”对比。

### 第 3 页｜比喻
- 品牌标识：YF拾光机
- 主标题：它更像一个随身资料员
- 正文：你不用每次重新解释背景，它能先拿到资料，再帮你组织表达。
- 重点词：资料员、背景
- 图片说明：一个 prompt 风内容卡片，绿色强调关键词。

### 第 4 页｜拆解
- 品牌标识：YF拾光机
- 主标题：这件事可以拆成 3 点
- 正文：1. 资料接入更近。2. 写作上下文更完整。3. 团队表达更容易统一。
- 重点词：资料、上下文、统一
- 图片说明：三条编号信息块纵向排列。

### 第 5 页｜影响
- 品牌标识：YF拾光机
- 主标题：产品经理尤其值得看
- 正文：AI 工具的竞争，正在从“生成得好不好”转向“能不能进入真实工作流”。
- 重点词：真实工作流
- 图片说明：单个大观点卡片，下面放 2-3 个标签。

### 第 6 页｜总结
- 品牌标识：YF拾光机
- 主标题：这不是单点功能更新
- 正文：{summary} 你会把 AI 接进团队知识库吗？
- 重点词：资料更近、上下文更全
- 图片说明：总结卡片加评论区引导，底部保留 6/6 页码。

## 5. 抖音 / 小红书发布文案
- 正文：{summary} 这类更新值得关注，因为它让 AI 从“单次生成”更靠近“持续协作”。
- 话题标签：#AI工具 #AI产品 #产品经理 #小红书图文
- 评论区引导：你更希望 AI 帮你写内容，还是先读懂资料？
"""


def main() -> None:
    parser = argparse.ArgumentParser(description="Format AI news as simplified Markdown.")
    parser.add_argument("--news-file", help="Path to a news JSON file.")
    args = parser.parse_args()
    print(render_markdown(load_news(args.news_file)))


if __name__ == "__main__":
    main()
