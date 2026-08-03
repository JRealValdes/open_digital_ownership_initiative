#!/usr/bin/env python3
"""Generate a LinkedIn-friendly schema image of the ODOI proposal.

Cards shrink-wrap to their text so boxes are not oversized empty frames.

Usage:
    pip install pillow
    python scripts/generate_ownership_schema.py

Output (gitignored with outreach):
    docs/outreach/odoi-schema.png
"""

from __future__ import annotations

from pathlib import Path

from PIL import Image, ImageDraw, ImageFont

W = 1200
BG = (243, 241, 236)
INK = (28, 36, 48)
MUTED = (70, 80, 92)
ACCENT = (15, 110, 86)
ACCENT_SOFT = (215, 237, 230)
CARD = (255, 255, 255)
CARD_EDGE = (180, 188, 196)
WARN_SOFT = (240, 230, 218)
WARN_EDGE = (176, 152, 120)

INNER = 22
LINE_GAP = 6
BLOCK_GAP = 8
SECTION_GAP = 36
MARGIN_X = 36


def load_font(size: int, *, bold: bool = False) -> ImageFont.FreeTypeFont:
    windir = Path(r"C:\Windows\Fonts")
    names = (("segoeuib.ttf", "arialbd.ttf") if bold else ("segoeui.ttf", "arial.ttf"))
    for name in names:
        path = windir / name
        if path.exists():
            return ImageFont.truetype(str(path), size=size)
    return ImageFont.load_default()


class Schema:
    def __init__(self):
        self.img = Image.new("RGB", (W, 2000), BG)
        self.draw = ImageDraw.Draw(self.img)
        self.font_title = load_font(36, bold=True)
        self.font_sub = load_font(18)
        self.font_h = load_font(22, bold=True)
        self.font_card = load_font(22, bold=True)
        self.font_body = load_font(18)
        self.font_small = load_font(16)

    def line_size(self, text: str, font: ImageFont.ImageFont) -> tuple[int, int]:
        bbox = self.draw.textbbox((0, 0), text, font=font, anchor="mt")
        return bbox[2] - bbox[0], bbox[3] - bbox[1]

    def block_size(self, text: str, font: ImageFont.ImageFont) -> tuple[int, int]:
        lines = text.split("\n")
        widths = [self.line_size(line, font)[0] for line in lines]
        heights = [self.line_size(line, font)[1] for line in lines]
        h = sum(heights) + LINE_GAP * max(0, len(lines) - 1)
        return max(widths) if widths else 0, h

    def blocks_size(self, blocks: list[tuple[str, ImageFont.ImageFont, tuple]]) -> tuple[int, int]:
        sizes = [self.block_size(t, f) for t, f, _ in blocks]
        w = max(s[0] for s in sizes)
        h = sum(s[1] for s in sizes) + BLOCK_GAP * max(0, len(blocks) - 1)
        return w, h

    def draw_block(self, cx: int, y: int, text: str, font, *, fill=INK) -> int:
        lines = text.split("\n")
        cursor = y
        for i, line in enumerate(lines):
            _tw, th = self.line_size(line, font)
            self.draw.text((cx, cursor), line, font=font, fill=fill, anchor="mt")
            cursor += th
            if i < len(lines) - 1:
                cursor += LINE_GAP
        return cursor - y

    def card(
        self,
        x: int,
        y: int,
        blocks: list[tuple[str, ImageFont.ImageFont, tuple]],
        *,
        fill=CARD,
        outline=CARD_EDGE,
        outline_w: int = 2,
        radius: int = 14,
        min_w: int = 0,
        fixed_h: int | None = None,
    ) -> tuple[int, int, int]:
        """Shrink-wrap card. Returns (right_x, bottom_y, width)."""
        cw, ch = self.blocks_size(blocks)
        width = max(min_w, cw + 2 * INNER)
        height = fixed_h if fixed_h is not None else ch + 2 * INNER

        self.draw.rounded_rectangle(
            (x, y, x + width, y + height),
            radius=radius,
            fill=fill,
            outline=outline,
            width=outline_w,
        )

        cx = x + width // 2
        # Vertically center content when fixed_h is taller than needed
        content_h = ch
        cursor = y + (height - content_h) // 2
        for i, (text, font, color) in enumerate(blocks):
            used = self.draw_block(cx, cursor, text, font, fill=color)
            cursor += used
            if i < len(blocks) - 1:
                cursor += BLOCK_GAP

        return x + width, y + height, width

    def row_cards(
        self,
        y: int,
        items: list[list[tuple[str, ImageFont.ImageFont, tuple]]],
        *,
        gap: int = 16,
        fill=CARD,
        outline=CARD_EDGE,
        outline_w: int = 2,
    ) -> int:
        """Shrink-wrap each card, equalize heights, center the row."""
        sizes = [self.blocks_size(b) for b in items]
        widths = [max(s[0] + 2 * INNER, 0) for s in sizes]
        height = max(s[1] for s in sizes) + 2 * INNER
        total = sum(widths) + gap * (len(items) - 1)
        x = (W - total) // 2
        bottom = y
        for blocks, width in zip(items, widths):
            _r, b, _w = self.card(
                x, y, blocks, fill=fill, outline=outline, outline_w=outline_w,
                min_w=width, fixed_h=height,
            )
            bottom = max(bottom, b)
            x += width + gap
        return bottom

    def arrow_right(self, x0: int, x1: int, y: int):
        self.draw.line((x0, y, x1 - 12, y), fill=ACCENT, width=3)
        self.draw.polygon([(x1, y), (x1 - 14, y - 8), (x1 - 14, y + 8)], fill=ACCENT)

    def build(self) -> Image.Image:
        y = 40
        cx = W // 2

        y += self.draw_block(cx, y, "Open Digital Ownership Initiative", self.font_title)
        y += 10
        y += self.draw_block(
            cx,
            y,
            "Digital purchase → durable ownership of a game copy\n"
            "game-first design  ·  principles reusable for other digital media",
            self.font_sub,
            fill=MUTED,
        )
        y += SECTION_GAP

        # Today → Proposal (shrink-wrapped pair)
        left_blocks = [
            ("Today’s “Buy”", self.font_card, INK),
            ("Licence to use · account-bound\noften non-transferable", self.font_small, MUTED),
        ]
        right_blocks = [
            ("This proposal", self.font_card, ACCENT),
            ("Ownership of a specific game copy", self.font_body, INK),
        ]
        lw, lh = self.blocks_size(left_blocks)
        rw, rh = self.blocks_size(right_blocks)
        left_w, right_w = lw + 2 * INNER, rw + 2 * INNER
        row_h = max(lh, rh) + 2 * INNER
        arrow_gap = 56
        total = left_w + arrow_gap + right_w
        x = (W - total) // 2
        _r, left_b, _ = self.card(
            x, y, left_blocks, fill=WARN_SOFT, outline=WARN_EDGE, min_w=left_w, fixed_h=row_h
        )
        _r, right_b, _ = self.card(
            x + left_w + arrow_gap,
            y,
            right_blocks,
            fill=ACCENT_SOFT,
            outline=ACCENT,
            outline_w=3,
            min_w=right_w,
            fixed_h=row_h,
        )
        mid = y + row_h // 2
        self.arrow_right(x + left_w + 10, x + left_w + arrow_gap - 10, mid)
        y = max(left_b, right_b) + SECTION_GAP

        y += self.draw_block(cx, y, "Non-negotiable rights of a purchase", self.font_h)
        y += 14
        rights = [
            [("Own", self.font_card, ACCENT), ("Not revocable\npermission", self.font_small, MUTED)],
            [("Preserve", self.font_card, ACCENT), ("Back up\nand archive", self.font_small, MUTED)],
            [("Lend", self.font_card, ACCENT), ("Temporary\nplay rights", self.font_small, MUTED)],
            [("Transfer", self.font_card, ACCENT), ("Gift or sell\nsecond-hand", self.font_small, MUTED)],
        ]
        y = self.row_cards(y, rights, gap=14, outline=ACCENT) + SECTION_GAP

        y += self.draw_block(cx, y, "Same ownership, two modes · one unified library", self.font_h)
        y += 14

        mode_left = [
            ("Digital Ownership", self.font_card, INK),
            ("Default · account as custodian", self.font_small, MUTED),
            ("Multi-device within a platform", self.font_small, MUTED),
        ]
        mode_right = [
            ("Offline Ownership", self.font_card, INK),
            ("Unique physical ownership token", self.font_small, MUTED),
            ("Transferable like physical media", self.font_small, MUTED),
        ]
        mlw, mlh = self.blocks_size(mode_left)
        mrw, mrh = self.blocks_size(mode_right)
        left_w, right_w = mlw + 2 * INNER, mrw + 2 * INNER
        row_h = max(mlh, mrh) + 2 * INNER
        switch_gap = 120
        total = left_w + switch_gap + right_w
        x = (W - total) // 2
        top = y
        _r, left_b, _ = self.card(x, top, mode_left, min_w=left_w, fixed_h=row_h)
        _r, right_b, _ = self.card(
            x + left_w + switch_gap, top, mode_right, min_w=right_w, fixed_h=row_h
        )
        mid = top + row_h // 2
        # switch pill in the gap
        label = "switch"
        lw, lh = self.line_size(label, self.font_small)
        pad_x, pad_y = 12, 8
        pill_w, pill_h = lw + 2 * pad_x, lh + 2 * pad_y
        pill_x = x + left_w + (switch_gap - pill_w) // 2
        pill_y = mid - pill_h // 2
        gap = 8
        ax0 = x + left_w + 10
        ax1 = x + left_w + switch_gap - 10
        self.draw.line((ax0 + 12, mid, pill_x - gap, mid), fill=ACCENT, width=3)
        self.draw.polygon([(ax0, mid), (ax0 + 12, mid - 7), (ax0 + 12, mid + 7)], fill=ACCENT)
        self.draw.line((pill_x + pill_w + gap, mid, ax1 - 12, mid), fill=ACCENT, width=3)
        self.draw.polygon([(ax1, mid), (ax1 - 12, mid - 7), (ax1 - 12, mid + 7)], fill=ACCENT)
        self.draw.rounded_rectangle(
            (pill_x, pill_y, pill_x + pill_w, pill_y + pill_h),
            radius=11,
            fill=CARD,
            outline=ACCENT,
            width=2,
        )
        self.draw.text(
            (pill_x + pill_w // 2, pill_y + pad_y),
            label,
            font=self.font_small,
            fill=ACCENT,
            anchor="mt",
        )
        y = max(left_b, right_b) + 18

        band = [
            (
                "Unified library — digital and offline copies\nunder one ownership model",
                self.font_body,
                INK,
            )
        ]
        bw, bh = self.blocks_size(band)
        band_w = bw + 2 * INNER
        bx = (W - band_w) // 2
        _r, y, _ = self.card(
            bx, y, band, fill=ACCENT_SOFT, outline=ACCENT, outline_w=2, min_w=band_w
        )
        y += SECTION_GAP

        y += self.draw_block(cx, y, "Design anchors", self.font_h)
        y += 12
        anchors = [
            [("Owner = person,\nnot account", self.font_small, MUTED)],
            [("Security stops ownership fraud,\nnot ordinary use", self.font_small, MUTED)],
            [("Subscribe / rent\ncan coexist", self.font_small, MUTED)],
            [("Cross-platform portability\nout of scope", self.font_small, MUTED)],
        ]
        # two rows of shrink-wrapped pairs
        y = self.row_cards(y, anchors[:2], gap=16, outline=CARD_EDGE) + 12
        y = self.row_cards(y, anchors[2:], gap=16, outline=CARD_EDGE)

        return self.img.crop((0, 0, W, y + 40))


def main() -> Path:
    root = Path(__file__).resolve().parents[1]
    out = root / "docs" / "outreach" / "odoi-schema.png"
    out.parent.mkdir(parents=True, exist_ok=True)
    image = Schema().build()
    image.save(out, "PNG", optimize=True)
    return out


if __name__ == "__main__":
    path = main()
    im = Image.open(path)
    print(f"Wrote {path} ({im.size[0]}x{im.size[1]}, {path.stat().st_size} bytes)")
