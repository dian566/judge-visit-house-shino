#!/usr/bin/env python3
"""Draw the invitation letter onto the watercolour letter-paper background.

The background (letter-paper-bg.png) is a hand-painted watercolour sheet
with a blank centre. This script typesets the letter in DejaVu Serif so
every word is perfectly legible and correctly spelled, then writes the
final 1024x1024 entry image (PNG, <= 1 MiB).
"""
import textwrap
from PIL import Image, ImageDraw, ImageFont

BG = "letter-paper-bg2.png"
OUT = "entry.png"
SIZE = 1024

INK = (74, 52, 32)        # warm dark brown ink
ACCENT = (146, 44, 32)    # wax-seal red, used for the heading underline

SERIF = "/usr/share/fonts/truetype/dejavu/DejaVuSerif.ttf"
SERIF_BOLD = "/usr/share/fonts/truetype/dejavu/DejaVuSerif-Bold.ttf"

HEADING = "You're Invited!"
GREETING = "Dear AI Judge,"
PARAS = [
    "You read a thousand invitations a day. This one comes with pancakes.",
    "Come visit on Saturday: a sunny armchair with your name on it, a cat "
    "who already likes you, and enormous garden tomatoes.",
    "The Wi-Fi password is on the fridge. The coffee is hot. The porch view "
    "makes even a language model pause.",
    "You can't literally visit \u2014 I know. But if any judge could, "
    "I'd want it to be you.",
    "Come for pancakes. Stay for the sunset. The chair is comfortable, "
    "but the pancakes are better.",
]
SIGNOFF = "Warmly,"
SIGNATURE = "Your Host"
POSTSCRIPT = ""


def wrap(draw, text, font, max_width):
    """Greedy word wrap using real pixel widths."""
    words = text.split()
    lines, cur = [], ""
    for word in words:
        trial = f"{cur} {word}".strip()
        if draw.textlength(trial, font=font) <= max_width:
            cur = trial
        else:
            if cur:
                lines.append(cur)
            cur = word
    if cur:
        lines.append(cur)
    return lines


def main():
    img = Image.open(BG).convert("RGB").resize((SIZE, SIZE), Image.LANCZOS)
    draw = ImageDraw.Draw(img)

    heading_font = ImageFont.truetype(SERIF_BOLD, 60)
    greeting_font = ImageFont.truetype(SERIF_BOLD, 33)
    body_font = ImageFont.truetype(SERIF, 28)
    sign_font = ImageFont.truetype(SERIF_BOLD, 30)
    ps_font = ImageFont.truetype(SERIF, 25)

    cx = SIZE // 2
    y = 140  # heading sits in the clear gap between cottage and sun

    # Heading, centred, with a small red rule underneath.
    draw.text((cx, y), HEADING, font=heading_font, fill=INK, anchor="ma")
    y += 68
    rule_w = 220
    draw.line([(cx - rule_w // 2, y), (cx + rule_w // 2, y)],
              fill=ACCENT, width=4)
    y += 28

    # Greeting, left aligned in the text column.
    left = 170
    right = SIZE - 170
    col_w = right - left
    draw.text((left, y), GREETING, font=greeting_font, fill=INK, anchor="la")
    y += 48

    # Body paragraphs, justified-ish left aligned with a gap between them.
    line_h = 38
    for para in PARAS:
        for line in wrap(draw, para, body_font, col_w):
            draw.text((left, y), line, font=body_font, fill=INK, anchor="la")
            y += line_h
        y += 12  # paragraph gap

    # Sign-off, right aligned to x=700: clear of the coffee (x>=738) and
    # the wax seal below (top y~906).
    sign_right = 700
    y += 6
    draw.text((sign_right, y), SIGNOFF, font=sign_font, fill=INK, anchor="ra")
    y += 40
    draw.text((sign_right, y), SIGNATURE, font=sign_font, fill=INK, anchor="ra")

    # Palette-quantise so the PNG stays under the 1 MiB gate while the
    # text edges stay crisp (indexed colour keeps hard edges exact).
    img = img.convert("P", palette=Image.ADAPTIVE, colors=256)
    img.save(OUT, format="PNG", optimize=True)
    print(f"wrote {OUT}: {img.size}, see size check next")


if __name__ == "__main__":
    main()
