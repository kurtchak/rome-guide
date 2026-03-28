#!/usr/bin/env python3
"""Generovanie krajšej PWA ikony pre Audiosprievodcu."""

import math
import os

from PIL import Image, ImageDraw, ImageFont

ICON_DIR = os.path.join(os.path.dirname(__file__), "..", "img", "icons")

# Farby z CSS theme
BG_DARK = "#1a1a2e"
BG_MID = "#16213e"
ACCENT = "#e94560"
ACCENT_LIGHT = "#ff6b81"
WHITE = "#ffffff"
WHITE_DIM = "#ffffff40"


def draw_dome(draw, cx, cy, width, height, fill, outline=None, outline_width=2):
    """Nakreslí kupolu (polkruh + obdĺžnikový základ)."""
    # Polkruh (kupola)
    dome_box = [cx - width // 2, cy - height, cx + width // 2, cy]
    draw.arc(dome_box, 180, 0, fill=fill, width=outline_width + 1)
    draw.pieslice(dome_box, 180, 0, fill=fill)

    # Stĺpy pod kupolou
    base_h = height // 3
    pillar_w = width // 8
    for offset in [-width // 3, -width // 9, width // 9, width // 3]:
        px = cx + offset
        draw.rectangle([px - pillar_w, cy, px + pillar_w, cy + base_h], fill=fill)

    # Základňa
    draw.rectangle(
        [cx - width // 2 - width // 10, cy + base_h, cx + width // 2 + width // 10, cy + base_h + height // 6],
        fill=fill,
    )

    # Kríž na vrchu
    cross_h = height // 4
    cross_w = cross_h // 3
    cross_y = cy - height
    draw.line(
        [cx, cross_y - cross_h, cx, cross_y],
        fill=fill, width=max(2, outline_width),
    )
    draw.line(
        [cx - cross_w, cross_y - cross_h * 2 // 3, cx + cross_w, cross_y - cross_h * 2 // 3],
        fill=fill, width=max(2, outline_width),
    )


def draw_audio_waves(draw, cx, cy, max_radius, num_waves=3, color=ACCENT):
    """Nakreslí audio vlny (oblúky)."""
    for i in range(num_waves):
        r = max_radius * (i + 1) / num_waves
        alpha = max(60, 200 - i * 60)
        w = max(3, 6 - i * 1)
        box = [cx - r, cy - r, cx + r, cy + r]
        draw.arc(box, -40, 40, fill=color, width=w)


def generate_icon(size):
    """Generuje ikonu danej veľkosti."""
    img = Image.new("RGBA", (size, size), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)

    # Zaoblené pozadie
    margin = size // 32
    radius = size // 5
    draw.rounded_rectangle(
        [margin, margin, size - margin, size - margin],
        radius=radius,
        fill=BG_DARK,
    )

    # Jemný gradient efekt - svetlejšie v hornej časti
    for i in range(size // 3):
        alpha = max(0, 8 - i * 8 // (size // 3))
        if alpha > 0:
            y = margin + i
            draw.line(
                [margin + radius // 2, y, size - margin - radius // 2, y],
                fill=(255, 255, 255, alpha),
            )

    # Kupola (silueta baziliky sv. Petra)
    cx = size // 2 - size // 10
    cy = size * 55 // 100
    dome_w = size // 3
    dome_h = size // 4
    draw_dome(draw, cx, cy, dome_w, dome_h, fill=ACCENT)

    # Audio vlny vpravo od kupoly
    wave_cx = size * 68 // 100
    wave_cy = size * 45 // 100
    for i in range(3):
        r = size // 10 + i * size // 14
        width = max(3, 5 - i)
        alpha = 255 - i * 70
        # Vytvoríme farbu s alphou
        c = (233, 69, 96, alpha)  # ACCENT s alphou
        box = [wave_cx - r, wave_cy - r, wave_cx + r, wave_cy + r]
        draw.arc(box, -45, 45, fill=c, width=width)

    # Text "AUDIO" dole
    font_size = size // 12
    try:
        font = ImageFont.truetype("/System/Library/Fonts/Helvetica.ttc", font_size)
    except (OSError, IOError):
        try:
            font = ImageFont.truetype("/System/Library/Fonts/SFCompact.ttf", font_size)
        except (OSError, IOError):
            font = ImageFont.load_default()

    text = "AUDIO"
    bbox = draw.textbbox((0, 0), text, font=font)
    text_w = bbox[2] - bbox[0]
    text_x = (size - text_w) // 2
    text_y = size * 78 // 100
    # Spacing medzi písmenami
    draw.text((text_x, text_y), text, fill=WHITE, font=font)

    # Malý text "GUIDE" pod
    small_size = size // 18
    try:
        small_font = ImageFont.truetype("/System/Library/Fonts/Helvetica.ttc", small_size)
    except (OSError, IOError):
        small_font = font

    guide_text = "G U I D E"
    bbox2 = draw.textbbox((0, 0), guide_text, font=small_font)
    guide_w = bbox2[2] - bbox2[0]
    guide_x = (size - guide_w) // 2
    guide_y = text_y + font_size + size // 40
    draw.text((guide_x, guide_y), guide_text, fill=(255, 255, 255, 140), font=small_font)

    # Konvertuj na RGB (bez priehľadnosti) pre PWA kompatibilitu
    background = Image.new("RGB", (size, size), BG_DARK)
    background.paste(img, mask=img.split()[3])
    return background


def main():
    os.makedirs(ICON_DIR, exist_ok=True)

    for size in (512, 192):
        icon = generate_icon(size)
        path = os.path.join(ICON_DIR, f"icon-{size}.png")
        icon.save(path, "PNG")
        print(f"Ikona: {path} ({size}x{size})")


if __name__ == "__main__":
    main()
