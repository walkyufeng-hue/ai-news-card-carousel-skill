#!/usr/bin/env python3
"""Return mock AI news items for local skill demos.

This script intentionally does not access the network. It provides predictable
sample data that can be piped into the formatter or used in README examples.
"""

from __future__ import annotations

import argparse
import json
from typing import Any


MOCK_NEWS: list[dict[str, Any]] = [
    {
        "title": "OpenAI 更新多模态交互体验",
        "source": "OpenAI Blog",
        "url": "https://openai.com/",
        "published_at": "2026-06-20",
        "summary": "OpenAI 展示了更自然的文字、图像和语音交互方式，强调让用户少切换工具、少等待结果。",
        "keywords": ["OpenAI", "多模态", "语音", "产品入口"],
    },
    {
        "title": "AI 写作工具加入团队知识库能力",
        "source": "Product Release Notes",
        "url": "https://example.com/release-notes",
        "published_at": "2026-06-18",
        "summary": "某 AI 写作工具允许团队把内部文档接入写作流程，让输出更贴近公司语境。",
        "keywords": ["AI 写作", "知识库", "团队协作", "上下文"],
    },
    {
        "title": "AI 搜索产品强化答案页交互",
        "source": "Official Product Blog",
        "url": "https://example.com/blog/ai-search",
        "published_at": "2026-06-15",
        "summary": "AI 搜索产品把答案、追问、引用和操作入口放在同一页面，弱化传统搜索结果列表。",
        "keywords": ["AI 搜索", "答案页", "信息入口", "产品设计"],
    },
]


def filter_items(items: list[dict[str, Any]], keyword: str | None) -> list[dict[str, Any]]:
    if not keyword:
        return items

    keyword_lower = keyword.lower()
    matched: list[dict[str, Any]] = []
    for item in items:
        haystack = " ".join(
            [
                item.get("title", ""),
                item.get("summary", ""),
                " ".join(item.get("keywords", [])),
            ]
        ).lower()
        if keyword_lower in haystack:
            matched.append(item)
    return matched


def main() -> None:
    parser = argparse.ArgumentParser(description="Return mock AI news as JSON.")
    parser.add_argument("--keyword", help="Filter mock news by keyword.")
    parser.add_argument("--limit", type=int, default=3, help="Maximum items to return.")
    parser.add_argument(
        "--first",
        action="store_true",
        help="Return only the first matching object instead of a list.",
    )
    args = parser.parse_args()

    items = filter_items(MOCK_NEWS, args.keyword)[: max(args.limit, 0)]
    output: Any = items[0] if args.first and items else items
    print(json.dumps(output, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
