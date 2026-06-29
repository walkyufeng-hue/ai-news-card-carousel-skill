#!/usr/bin/env python3
"""Check a candidate AI topic against local JSON history.

The history can be supplied with --history. If omitted, a small in-file JSON
history is used so the script can run in a freshly cloned repository.
"""

from __future__ import annotations

import argparse
import json
import re
from pathlib import Path
from typing import Any


DEFAULT_HISTORY_JSON = """
[
  {
    "title": "AI 搜索正在改变信息入口",
    "published_at": "2026-06-01",
    "keywords": ["AI 搜索", "信息入口", "答案页"],
    "core_viewpoint": "搜索结果页正在变成可继续操作的答案入口。"
  },
  {
    "title": "多模态模型让交互更像对话",
    "published_at": "2026-05-28",
    "keywords": ["多模态", "语音", "图片", "模型交互"],
    "core_viewpoint": "AI 不只是理解文字，而是在靠近真实沟通。"
  }
]
"""


def normalize_text(value: str) -> str:
    value = value.lower()
    value = re.sub(r"[\s,，。.!！?？:：;；'\"“”‘’（）()【】\[\]-]+", "", value)
    return value


def load_json_file(path: str | None) -> Any:
    if not path:
        return json.loads(DEFAULT_HISTORY_JSON)
    return json.loads(Path(path).read_text(encoding="utf-8"))


def load_candidate(args: argparse.Namespace) -> dict[str, Any]:
    if args.news_file:
        data = load_json_file(args.news_file)
        if isinstance(data, list):
            if not data:
                raise SystemExit("news file contains an empty list")
            data = data[0]
        if not isinstance(data, dict):
            raise SystemExit("news file must contain a JSON object or a non-empty list")
        return data

    return {
        "title": args.title,
        "keywords": args.keywords,
    }


def keyword_overlap(left: list[str], right: list[str]) -> float:
    left_set = {normalize_text(item) for item in left if item}
    right_set = {normalize_text(item) for item in right if item}
    if not left_set or not right_set:
        return 0.0
    return len(left_set & right_set) / max(len(left_set), len(right_set))


def check_duplicate(
    candidate: dict[str, Any],
    history: list[dict[str, Any]],
    threshold: float,
) -> dict[str, Any]:
    candidate_title = normalize_text(str(candidate.get("title", "")))
    candidate_keywords = [str(item) for item in candidate.get("keywords", [])]
    matches: list[dict[str, Any]] = []

    for item in history:
        history_title = normalize_text(str(item.get("title", "")))
        history_keywords = [str(keyword) for keyword in item.get("keywords", [])]
        reasons: list[str] = []

        if candidate_title and candidate_title == history_title:
            reasons.append("标题完全重复")
        elif candidate_title and history_title and (
            candidate_title in history_title or history_title in candidate_title
        ):
            reasons.append("标题高度相似")

        overlap = keyword_overlap(candidate_keywords, history_keywords)
        if overlap >= threshold:
            reasons.append(f"关键词重合度 {overlap:.0%}")

        if reasons:
            matches.append(
                {
                    "title": item.get("title", ""),
                    "published_at": item.get("published_at", ""),
                    "reasons": reasons,
                    "core_viewpoint": item.get("core_viewpoint", ""),
                }
            )

    return {
        "is_duplicate": bool(matches),
        "candidate_title": candidate.get("title", ""),
        "matches": matches,
        "note": "未提供 --history 时使用脚本内置示例历史，仅用于演示。",
    }


def main() -> None:
    parser = argparse.ArgumentParser(description="Run a basic local topic dedupe check.")
    parser.add_argument("--history", help="Path to a JSON history file.")
    parser.add_argument("--news-file", help="Path to a candidate news JSON file.")
    parser.add_argument("--title", default="OpenAI 更新多模态交互体验")
    parser.add_argument("--keywords", nargs="*", default=["OpenAI", "多模态", "语音"])
    parser.add_argument("--threshold", type=float, default=0.5)
    args = parser.parse_args()

    history = load_json_file(args.history)
    if not isinstance(history, list):
        raise SystemExit("history must be a JSON list")

    candidate = load_candidate(args)
    result = check_duplicate(candidate, history, args.threshold)
    print(json.dumps(result, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
