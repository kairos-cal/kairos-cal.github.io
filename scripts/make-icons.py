"""Derive every icon size from brand/logo-source.jpg.

The source is a 1024px JPEG of a rounded terracotta tile on a white ground with a soft shadow.
Two families come out of it:

- rounded: the tile cut out along its squircle edge, transparent outside (favicons, PWA icons,
  the header mark);
- square: the same tile on a flat terracotta ground, full-bleed, for surfaces that apply their
  own mask (apple-touch-icon) or want a plain square (Google's OAuth consent screen, 120x120).

Run: uv run --with pillow python3 scripts/make-icons.py [out_dir]
"""

import math
import sys
from pathlib import Path

from PIL import Image, ImageDraw

SRC = Path(__file__).resolve().parent.parent / "brand" / "logo-source.jpg"
TILE = (70, 70, 954, 954)  # the tile's bounding box in the source, measured once
INSET = 4  # trims the anti-aliased rim and the shadow bleeding into it
EXPONENT = 4.6  # superellipse exponent that matches the source's corners
SUPERSAMPLE = 4
GROUND_PATCH = (10, 600, 60, 700)  # tile coordinates, below the bow and left of the figure


def squircle_mask(size: int) -> Image.Image:
    big = size * SUPERSAMPLE
    mask = Image.new("L", (big, big), 0)
    half = big / 2
    points = []
    steps = 2048
    for i in range(steps):
        t = 2 * math.pi * i / steps
        c, s = math.cos(t), math.sin(t)
        x = half + half * math.copysign(abs(c) ** (2 / EXPONENT), c)
        y = half + half * math.copysign(abs(s) ** (2 / EXPONENT), s)
        points.append((x, y))
    ImageDraw.Draw(mask).polygon(points, fill=255)
    return mask.resize((size, size), Image.LANCZOS)


def main() -> None:
    out = Path(sys.argv[1]) if len(sys.argv) > 1 else Path("public")
    out.mkdir(parents=True, exist_ok=True)

    src = Image.open(SRC).convert("RGB")
    left, top, right, bottom = TILE
    tile = src.crop((left + INSET, top + INSET, right - INSET, bottom - INSET))
    size = tile.width

    rounded = tile.convert("RGBA")
    rounded.putalpha(squircle_mask(size))

    # Flat ground for the square family: the mean of a figure-free patch on the tile's left
    # edge, so the filled corners are indistinguishable at icon sizes.
    ground = tile.crop(GROUND_PATCH).resize((1, 1), Image.BOX).getpixel((0, 0))
    square = Image.new("RGBA", (size, size), ground + (255,))
    square.alpha_composite(rounded)

    def save(img: Image.Image, px: int, name: str) -> None:
        img.resize((px, px), Image.LANCZOS).save(out / name, optimize=True)

    for px in (16, 32, 192, 512):
        save(rounded, px, f"icon-{px}.png")
    save(rounded, 64, "logo-mark.png")
    save(square.convert("RGB"), 180, "apple-touch-icon.png")
    save(square.convert("RGB"), 120, "consent-logo-120.png")
    save(square.convert("RGB"), 512, "logo-square-512.png")
    rounded.resize((48, 48), Image.LANCZOS).save(
        out / "favicon.ico", sizes=[(16, 16), (32, 32), (48, 48)]
    )
    print(f"icons written to {out}/ (ground colour #{ground[0]:02x}{ground[1]:02x}{ground[2]:02x})")


if __name__ == "__main__":
    main()
