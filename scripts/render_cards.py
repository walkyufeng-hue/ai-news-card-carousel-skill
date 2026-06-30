#!/usr/bin/env python3
"""Render AI carousel cards as 1080x1440 PNG images.

Input JSON shape:
{
  "brand": "YF拾光机",
  "cards": [
    {
      "title": "AI 模型发布方式变了",
      "subtitle": "GPT-5.6 Sol 的重点，不只是更强",
      "blocks": [
        {"label": "PROMPT", "text": "这页要表达的正文。"},
        {"label": "NOTE", "text": "可选补充说明。"}
      ],
      "tags": ["模型发布", "分阶段开放"]
    }
  ]
}
"""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path
from typing import Any

try:
    from PIL import Image, ImageDraw, ImageFont
except ImportError as exc:  # pragma: no cover - exercised by missing dependency
    raise SystemExit(
        "Pillow is required. Install it with: python3 -m pip install Pillow"
    ) from exc


WIDTH = 1080
HEIGHT = 1440
BG = "#070B0B"
PANEL = "#101515"
PANEL_2 = "#0C1111"
TEXT = "#F2F4EF"
MUTED = "#A6ADA8"
DIM = "#68716E"
GREEN = "#36D69A"
GREEN_DARK = "#0B3B2F"
GREEN_LINE = "#155D49"

FONT_CANDIDATES = [
    "/System/Library/Fonts/STHeiti Medium.ttc",
    "/System/Library/Fonts/PingFang.ttc",
    "/System/Library/Fonts/Supplemental/Songti.ttc",
    "/Library/Fonts/Arial Unicode.ttf",
]


def find_font() -> str | None:
    for item in FONT_CANDIDATES:
        if Path(item).exists():
            return item
    return None


FONT_PATH = find_font()


def font(size: int) -> ImageFont.ImageFont:
    if FONT_PATH:
        return ImageFont.truetype(FONT_PATH, size)
    return ImageFont.load_default()


F_BRAND = font(30)
F_PAGE = font(30)
F_NUMBER = font(46)
F_TITLE = font(62)
F_SUBTITLE = font(34)
F_BLOCK_LABEL = font(25)
F_BODY = font(34)
F_TAG = font(25)


def text_width(draw: ImageDraw.ImageDraw, text: str, face: ImageFont.ImageFont) -> int:
    if not text:
        return 0
    box = draw.textbbox((0, 0), text, font=face)
    return box[2] - box[0]


def wrap_text(
    draw: ImageDraw.ImageDraw,
    text: str,
    face: ImageFont.ImageFont,
    max_width: int,
) -> list[str]:
    lines: list[str] = []
    current = ""
    for char in text:
        candidate = current + char
        if char == "\n":
            if current:
                lines.append(current)
            current = ""
            continue
        if text_width(draw, candidate, face) <= max_width or not current:
            current = candidate
        else:
            lines.append(current)
            current = char
    if current:
        lines.append(current)
    return lines


def draw_wrapped(
    draw: ImageDraw.ImageDraw,
    xy: tuple[int, int],
    text: str,
    face: ImageFont.ImageFont,
    fill: str,
    max_width: int,
    line_gap: int = 14,
) -> int:
    x, y = xy
    for line in wrap_text(draw, text, face, max_width):
        draw.text((x, y), line, font=face, fill=fill)
        y += face.size + line_gap
    return y


def draw_background(draw: ImageDraw.ImageDraw) -> None:
    for y in range(HEIGHT):
        ratio = y / HEIGHT
        green = int(11 + ratio * 12)
        draw.line((0, y, WIDTH, y), fill=(7, green, green))
    for x in range(40, WIDTH, 42):
        for y in range(40, HEIGHT, 42):
            draw.point((x, y), fill="#13221D")
    draw.rounded_rectangle((54, 52, WIDTH - 54, HEIGHT - 52), radius=30, outline="#101E1A", width=2)


def rounded_text_chip(
    draw: ImageDraw.ImageDraw,
    xy: tuple[int, int],
    text: str,
    face: ImageFont.ImageFont,
    fill: str = "#111A18",
    outline: str = GREEN_LINE,
    text_fill: str = GREEN,
) -> tuple[int, int]:
    x, y = xy
    width = text_width(draw, text, face) + 42
    height = face.size + 24
    draw.rounded_rectangle((x, y, x + width, y + height), radius=height // 2, fill=fill, outline=outline, width=1)
    draw.text((x + 21, y + 11), text, font=face, fill=text_fill)
    return x + width, y + height


def draw_header(draw: ImageDraw.ImageDraw, brand: str, index: int, total: int) -> None:
    rounded_text_chip(draw, (96, 72), brand, F_BRAND, fill="#0D1815", outline="#173C31")
    draw.text((WIDTH - 164, 78), f"{index:02d}", font=F_NUMBER, fill=GREEN)
    draw.line((WIDTH - 165, 138, WIDTH - 105, 138), fill=GREEN, width=3)
    rounded_text_chip(
        draw,
        (WIDTH - 440, 74),
        "AI HOT NOTE",
        F_TAG,
        fill="#0B1111",
        outline="#222A29",
        text_fill=MUTED,
    )


def draw_block(
    draw: ImageDraw.ImageDraw,
    top: int,
    label: str,
    text: str,
    height: int,
    highlight: bool = False,
) -> int:
    left = 116
    right = WIDTH - 116
    fill = "#0D1714" if highlight else PANEL
    outline = "#1A6B54" if highlight else "#1A2522"
    draw.rounded_rectangle((left, top, right, top + height), radius=24, fill=fill, outline=outline, width=2)
    rounded_text_chip(
        draw,
        (left + 34, top - 24),
        label.upper(),
        F_BLOCK_LABEL,
        fill="#0B1111",
        outline=GREEN_LINE if highlight else "#222C2A",
        text_fill=GREEN if highlight else MUTED,
    )
    draw_wrapped(draw, (left + 42, top + 54), text, F_BODY, TEXT, right - left - 84, line_gap=16)
    return top + height


def draw_tags(draw: ImageDraw.ImageDraw, tags: list[str], top: int) -> int:
    x = 116
    y = top
    for tag in tags[:4]:
        next_x, _ = rounded_text_chip(
            draw,
            (x, y),
            f"◎  {tag}",
            F_TAG,
            fill="#121616",
            outline="#202927",
            text_fill="#C7CEC9",
        )
        x = next_x + 22
        if x > WIDTH - 260:
            x = 116
            y += 64
    return y + 64


def render_card(card: dict[str, Any], index: int, total: int, brand: str) -> Image.Image:
    image = Image.new("RGB", (WIDTH, HEIGHT), BG)
    draw = ImageDraw.Draw(image)
    draw_background(draw)
    draw_header(draw, brand, index, total)

    badge_x, badge_y = 116, 192
    draw.rounded_rectangle((badge_x, badge_y, badge_x + 78, badge_y + 78), radius=20, fill=GREEN_DARK, outline="#164C3D", width=2)
    draw.text((badge_x + 21, badge_y + 16), f"{index:02d}", font=F_NUMBER, fill=GREEN)

    title_x = badge_x + 110
    y = badge_y + 4
    y = draw_wrapped(draw, (title_x, y), str(card.get("title", "")), F_TITLE, TEXT, WIDTH - title_x - 110, line_gap=18)

    subtitle = str(card.get("subtitle", "")).strip()
    if subtitle:
        y += 22
        y = draw_wrapped(draw, (title_x, y), subtitle, F_SUBTITLE, MUTED, WIDTH - title_x - 110, line_gap=12)

    y = max(y + 72, 360)
    blocks = card.get("blocks") or []
    if not blocks:
        body = str(card.get("body", "")).strip()
        if body:
            blocks = [{"label": "NOTE", "text": body}]

    remaining = HEIGHT - y - 270
    block_count = max(1, len(blocks))
    block_height = min(300, max(185, (remaining - (block_count - 1) * 52) // block_count))
    for block_index, block in enumerate(blocks[:3]):
        label = str(block.get("label", "NOTE"))
        text = str(block.get("text", ""))
        y = draw_block(draw, y, label, text, block_height, highlight=block_index == 0)
        y += 52

    tags = [str(tag) for tag in card.get("tags", []) if str(tag).strip()]
    if tags:
        y = min(y + 8, HEIGHT - 210)
        draw_tags(draw, tags, y)

    draw.line((116, HEIGHT - 116, WIDTH - 116, HEIGHT - 116), fill="#16201D", width=1)
    draw.text((WIDTH - 178, HEIGHT - 86), f"{index}/{total}", font=F_PAGE, fill=MUTED)
    return image


def make_contact_sheet(paths: list[Path], output: Path) -> None:
    thumb_w, thumb_h = 270, 360
    sheet = Image.new("RGB", (thumb_w * 3 + 80, thumb_h * 2 + 100), "#080C0C")
    for index, path in enumerate(paths):
        image = Image.open(path)
        image.thumbnail((thumb_w, thumb_h))
        x = 20 + (index % 3) * (thumb_w + 20)
        y = 20 + (index // 3) * (thumb_h + 40)
        sheet.paste(image, (x, y))
    sheet.save(output / "preview-contact-sheet.png", quality=95)


def load_input(path: Path) -> dict[str, Any]:
    data = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(data, dict):
        raise SystemExit("Input JSON must be an object.")
    cards = data.get("cards")
    if not isinstance(cards, list) or not cards:
        raise SystemExit("Input JSON must include a non-empty cards list.")
    return data


def main() -> None:
    parser = argparse.ArgumentParser(description="Render 1080x1440 YF拾光机 AI carousel PNG cards.")
    parser.add_argument("input", type=Path, help="Path to cards JSON.")
    parser.add_argument("--output", type=Path, default=Path("output/rendered-cards"))
    args = parser.parse_args()

    data = load_input(args.input)
    brand = str(data.get("brand", "YF拾光机"))
    cards = data["cards"]
    args.output.mkdir(parents=True, exist_ok=True)

    paths: list[Path] = []
    total = len(cards)
    for index, card in enumerate(cards, 1):
        image = render_card(card, index, total, brand)
        path = args.output / f"card-{index:02d}.png"
        image.save(path, quality=95)
        paths.append(path)

    make_contact_sheet(paths, args.output)
    for path in paths:
        print(path)
    print(args.output / "preview-contact-sheet.png")


if __name__ == "__main__":
    main()
