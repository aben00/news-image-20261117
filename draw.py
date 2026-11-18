#!/usr/bin/env python3
"""Draw the news-image-20261117 entry: one infographic summing up
Tuesday 17 November 2026.

Renders a 1024x1024 PNG: a newspaper front page, "THE WORLD TODAY", with
six flat-illustration story tiles, each with a small drawn picture, a
headline and a one-line label, so the day reads from the image alone.

Run:  python3 draw.py            (writes entry.png next to this script)
Uses only Pillow and the DejaVu fonts present on this machine.
"""
import math
import textwrap
from PIL import Image, ImageDraw, ImageFont

W, H = 1024, 1024
BOLD = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"
REG = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"

NAVY = (19, 35, 63)
AMBER = (232, 163, 23)
PAPER = (247, 245, 240)
INK = (24, 28, 34)
GREY = (90, 96, 104)
CARD = (255, 255, 255)
BORDER = (214, 212, 206)


def font(path, size):
    return ImageFont.truetype(path, size)


def wrap(draw, text, fnt, max_w):
    """Greedy word wrap returning a list of lines that fit max_w."""
    lines = []
    for para in text.split("\n"):
        words = para.split()
        cur = ""
        for w in words:
            trial = (cur + " " + w).strip()
            if draw.textlength(trial, font=fnt) <= max_w:
                cur = trial
            else:
                if cur:
                    lines.append(cur)
                cur = w
        if cur:
            lines.append(cur)
    return lines


def center_text(draw, cx, y, text, fnt, fill):
    draw.text((cx - draw.textlength(text, font=fnt) / 2, y), text, font=fnt, fill=fill)


def flames(d, x, y, size):
    """A small orange flame shape centred at (x, y)."""
    d.polygon([(x, y - size), (x + size * 0.55, y - size * 0.1),
               (x + size * 0.3, y + size * 0.5), (x - size * 0.3, y + size * 0.5),
               (x - size * 0.55, y - size * 0.1)], fill=(235, 130, 40))
    d.polygon([(x, y - size * 0.55), (x + size * 0.3, y),
               (x, y + size * 0.4), (x - size * 0.3, y)], fill=(255, 200, 60))


def smoke(d, x, y):
    for i, r in enumerate((16, 12, 9)):
        d.ellipse([x + i * 8 - r, y + i * 12 - r, x + i * 8 + r, y + i * 12 + r],
                  fill=(150, 156, 162))


# ---------------------------------------------------------------- header
def draw_header(d):
    d.rectangle([0, 0, W, 148], fill=NAVY)
    d.rectangle([0, 148, W, 152], fill=AMBER)
    center_text(d, W // 2, 16, "T U E S D A Y   1 7   N O V E M B E R   2 0 2 6",
                font(BOLD, 25), AMBER)
    center_text(d, W // 2, 50, "THE WORLD TODAY", font(BOLD, 64), (255, 255, 255))
    center_text(d, W // 2, 120, "Six stories that defined the day",
                font(REG, 22), (196, 205, 220))


# ---------------------------------------------------------------- tile art
def art_bridge(d, x, y, w, h):
    """A long bridge over the sea; its middle road span has fallen."""
    d.rectangle([x, y, x + w, y + h], fill=(198, 219, 233))
    d.rectangle([x, y + 128, x + w, y + h], fill=(110, 160, 190))
    d.line([(x + 14, y + 152), (x + 90, y + 152)], fill=(255, 255, 255), width=3)
    d.line([(x + w - 120, y + 168), (x + w - 30, y + 168)], fill=(255, 255, 255), width=3)
    # bridge deck: left and right spans, gap in the middle
    d.rectangle([x + 8, y + 96, x + w // 2 - 34, y + 108], fill=(74, 85, 96))
    d.rectangle([x + w // 2 + 34, y + 96, x + w - 8, y + 108], fill=(74, 85, 96))
    # fallen span, tilted down into the water
    d.polygon([(x + w // 2 - 34, y + 104), (x + w // 2 + 30, y + 108),
               (x + w // 2 + 22, y + 138), (x + w // 2 - 26, y + 136)],
              fill=(52, 60, 70))
    # two towers with cables
    for tx in (x + 52, x + w - 52):
        d.rectangle([tx - 5, y + 34, tx + 5, y + 96], fill=(90, 101, 112))
        d.rectangle([tx - 14, y + 28, tx + 14, y + 38], fill=(90, 101, 112))
    d.line([(x + 52, y + 38), (x + w // 2 - 34, y + 96)], fill=(140, 148, 156), width=3)
    d.line([(x + w - 52, y + 38), (x + w // 2 + 34, y + 96)], fill=(140, 148, 156), width=3)
    d.line([(x + 52, y + 38), (x + 8, y + 96)], fill=(140, 148, 156), width=3)
    d.line([(x + w - 52, y + 38), (x + w - 8, y + 96)], fill=(140, 148, 156), width=3)
    # fire and smoke where the span fell
    flames(d, x + w // 2, y + 118, 18)
    smoke(d, x + w // 2 + 14, y + 62)


def art_tankers(d, x, y, w, h):
    """Two oil tankers on fire on a narrow strait, a mine in the water."""
    d.rectangle([x, y, x + w, y + h], fill=(223, 231, 236))
    d.rectangle([x, y + 118, x + w, y + h], fill=(96, 140, 168))
    d.line([(x + 14, y + 150), (x + 90, y + 150)], fill=(255, 255, 255), width=3)
    d.line([(x + w - 120, y + 164), (x + w - 30, y + 164)], fill=(255, 255, 255), width=3)
    # tanker 1 (left): red hull, white deck, fire amidships
    d.polygon([(x + 16, y + 118), (x + 150, y + 118), (x + 138, y + 148),
               (x + 28, y + 148)], fill=(150, 52, 44))
    d.rectangle([x + 22, y + 104, x + 144, y + 118], fill=(235, 235, 235))
    d.rectangle([x + 96, y + 84, x + 128, y + 104], fill=(200, 200, 200))
    flames(d, x + 82, y + 96, 20)
    smoke(d, x + 96, y + 46)
    # tanker 2 (right, further off): dark hull, smoke
    d.polygon([(x + 176, y + 124), (x + w - 18, y + 124), (x + w - 30, y + 150),
               (x + 188, y + 150)], fill=(52, 60, 70))
    d.rectangle([x + 182, y + 112, x + w - 24, y + 124], fill=(220, 220, 220))
    flames(d, x + w - 74, y + 108, 15)
    smoke(d, x + w - 60, y + 58)
    # spiked naval mine floating between them
    mx, my = x + w // 2 + 6, y + 162
    for ang in range(0, 360, 45):
        a = math.radians(ang)
        d.line([(mx + 10 * math.cos(a), my + 10 * math.sin(a)),
                (mx + 18 * math.cos(a), my + 18 * math.sin(a))],
               fill=(40, 40, 44), width=4)
    d.ellipse([mx - 11, my - 11, mx + 11, my + 11], fill=(40, 40, 44))


def art_manila(d, x, y, w, h):
    """Airliner landing over a city skyline, Philippine and Thai flags."""
    d.rectangle([x, y, x + w, y + h], fill=(224, 237, 247))
    # sun
    d.ellipse([x + w - 62, y + 12, x + w - 24, y + 50], fill=(245, 200, 90))
    # skyline
    d.rectangle([x, y + 118, x + w, y + h], fill=(168, 178, 188))
    for bx, bw, bh in ((14, 44, 42), (66, 30, 62), (104, 52, 34), (164, 36, 54),
                       (208, 46, 40), (262, 34, 58)):
        d.rectangle([x + bx, y + 118 - bh, x + bx + bw, y + 118], fill=(120, 132, 146))
        for wy in range(y + 122 - bh, y + 112, 14):
            for wx in range(x + bx + 6, x + bx + bw - 6, 12):
                d.rectangle([wx, wy, wx + 5, wy + 7], fill=(255, 220, 120))
    # airliner: slim fuselage, tail fin at the rear, wing below
    px, py = x + 48, y + 66
    d.ellipse([px, py - 12, px + 158, py + 12], fill=(30, 50, 80))
    d.polygon([(px + 148, py - 10), (px + 188, py), (px + 148, py + 10)], fill=(30, 50, 80))
    d.polygon([(px + 6, py - 8), (px + 24, py - 38), (px + 40, py - 8)], fill=(24, 42, 68))
    d.polygon([(px + 78, py + 8), (px + 106, py + 36), (px + 122, py + 8)], fill=(24, 42, 68))
    for wx in range(6):
        d.ellipse([px + 16 + wx * 17, py - 5, px + 24 + wx * 17, py + 2], fill=(180, 210, 235))
    # two small flags on poles at the runway
    for fx0, bands in ((x + 26, [(0, 56, 147), (255, 255, 255)]),
                       (x + w - 74, [(178, 34, 34), (255, 255, 255)])):
        d.line([(fx0 + 24, y + 128), (fx0 + 24, y + 176)], fill=(80, 70, 60), width=4)
        d.rectangle([fx0, y + 128, fx0 + 48, y + 148], fill=bands[0])
        d.rectangle([fx0, y + 148, fx0 + 48, y + 168], fill=bands[1])
        if bands[0] == (0, 56, 147):
            d.polygon([(fx0, y + 128), (fx0 + 20, y + 138), (fx0, y + 148)],
                      fill=(255, 255, 255))
            d.ellipse([fx0 + 8, y + 134, fx0 + 14, y + 140], fill=(255, 200, 60))
        else:
            d.rectangle([fx0, y + 138, fx0 + 48, y + 158], fill=(0, 40, 120))


def art_summit(d, x, y, w, h):
    """Three flags — China, USA, Russia — over a round summit table."""
    d.rectangle([x, y, x + w, y + h], fill=(227, 236, 245))
    # table
    d.ellipse([x + 58, y + 122, x + w - 58, y + 170], fill=(146, 104, 66))
    d.rectangle([x + w // 2 - 12, y + 160, x + w // 2 + 12, y + h - 8], fill=(122, 84, 52))
    d.ellipse([x + 58, y + 116, x + w - 58, y + 160], fill=(176, 130, 84))
    # three flag poles: China red, USA red/white, Russia white/blue/red
    flag_defs = [
        ([(222, 41, 16), (255, 215, 0)], "CN"),
        ([(178, 34, 34), (255, 255, 255)], "US"),
        ([(255, 255, 255), (0, 57, 166)], "RU"),
    ]
    fx = [x + 78, x + w // 2 - 24, x + w - 126]
    for (bands, label), fx0 in zip(flag_defs, fx):
        d.line([(fx0 + 24, y + 30), (fx0 + 24, y + 118)], fill=(80, 70, 60), width=4)
        d.rectangle([fx0, y + 30, fx0 + 48, y + 52], fill=bands[0])
        d.rectangle([fx0, y + 52, fx0 + 48, y + 74], fill=bands[1])
        if label == "CN":
            for sx, sy in ((8, 36), (20, 34), (28, 42), (20, 50)):
                d.ellipse([fx0 + sx, y + sy, fx0 + sx + 6, y + sy + 6], fill=(255, 215, 0))
        if label == "US":
            for sy in (34, 44, 54, 64):
                d.rectangle([fx0, y + sy, fx0 + 48, y + sy + 5], fill=(178, 34, 34))
            d.rectangle([fx0, y + 30, fx0 + 20, y + 50], fill=(30, 50, 110))
        if label == "RU":
            d.rectangle([fx0, y + 52, fx0 + 48, y + 74], fill=(210, 16, 52))
    # three chairs around the table
    for cx0 in (x + 66, x + w // 2 - 24, x + w - 114):
        d.rectangle([cx0, y + 132, cx0 + 48, y + 142], fill=(94, 80, 66))
        d.rectangle([cx0 + 4, y + 142, cx0 + 10, y + 168], fill=(58, 48, 40))
        d.rectangle([cx0 + 38, y + 142, cx0 + 44, y + 168], fill=(58, 48, 40))


def art_bank(d, x, y, w, h):
    """A bank building with columns and a phone showing an error, plus a bug."""
    d.rectangle([x, y, x + w, y + h], fill=(232, 236, 240))
    # bank: pediment, columns, steps
    bx = x + 22
    d.polygon([(bx, y + 66), (bx + 130, y + 22), (bx + 260, y + 66)], fill=(140, 148, 156))
    d.ellipse([bx + 118, y + 38, bx + 142, y + 62], fill=(232, 163, 23))
    d.rectangle([bx, y + 66, bx + 260, y + 76], fill=(120, 128, 136))
    for cx0 in range(4):
        cx = bx + 16 + cx0 * 62
        d.rectangle([cx, y + 76, cx + 22, y + 138], fill=(200, 206, 212))
        d.rectangle([cx - 4, y + 70, cx + 26, y + 78], fill=(180, 186, 192))
        d.rectangle([cx - 4, y + 138, cx + 26, y + 146], fill=(180, 186, 192))
    d.rectangle([bx, y + 146, bx + 260, y + 156], fill=(120, 128, 136))
    d.rectangle([bx - 8, y + 156, bx + 268, y + 164], fill=(100, 108, 116))
    # phone with a red error cross, held at the right
    px0, py0 = x + w - 92, y + 84
    d.rounded_rectangle([px0, py0, px0 + 64, py0 + 96], radius=10, fill=(30, 34, 40))
    d.rounded_rectangle([px0 + 5, py0 + 5, px0 + 59, py0 + 80], radius=6, fill=(255, 255, 255))
    d.ellipse([px0 + 20, py0 + 30, px0 + 44, py0 + 54], outline=(201, 45, 45), width=5)
    d.line([(px0 + 28, py0 + 38), (px0 + 36, py0 + 46)], fill=(201, 45, 45), width=4)
    d.line([(px0 + 36, py0 + 38), (px0 + 28, py0 + 46)], fill=(201, 45, 45), width=4)
    center_text(d, px0 + 32, py0 + 62, "ERROR", font(BOLD, 12), (201, 45, 45))
    # a beetle (software bug) crawling on the steps
    bugx, bugy = bx + 52, y + 158
    d.ellipse([bugx - 14, bugy - 10, bugx + 14, bugy + 10], fill=(40, 40, 44))
    d.line([(bugx, bugy - 10), (bugx, bugy + 10)], fill=(90, 90, 96), width=2)
    for s in (-1, 1):
        for ly in (-6, 0, 6):
            d.line([(bugx + s * 12, bugy + ly), (bugx + s * 24, bugy + ly + 4)],
                   fill=(40, 40, 44), width=3)
    d.line([(bugx - 6, bugy - 10), (bugx - 12, bugy - 18)], fill=(40, 40, 44), width=3)
    d.line([(bugx + 6, bugy - 10), (bugx + 12, bugy - 18)], fill=(40, 40, 44), width=3)


def art_rocket(d, x, y, w, h):
    """A rocket breaking apart in the sky; satellites tumble below it."""
    d.rectangle([x, y, x + w, y + h], fill=(214, 228, 240))
    # stars
    for sx, sy in ((30, 20), (90, 44), (250, 18), (290, 52), (180, 14)):
        d.ellipse([x + sx, y + sy, x + sx + 5, y + sy + 5], fill=(255, 255, 255))
    # upper stage: red nose, white body, orange band, still climbing
    rx, ry = x + w // 2 + 18, y + 58
    d.polygon([(rx - 18, ry - 26), (rx, ry - 54), (rx + 18, ry - 26)], fill=(201, 60, 40))
    d.rectangle([rx - 18, ry - 26, rx + 18, ry + 16], fill=(240, 240, 238))
    d.rectangle([rx - 18, ry - 26, rx + 18, ry - 26], fill=(240, 240, 238))
    d.rectangle([rx - 18, ry - 2, rx + 18, ry + 8], fill=(232, 163, 23))
    d.line([(rx - 18, ry - 26), (rx - 18, ry + 16)], fill=(180, 180, 178), width=2)
    d.line([(rx + 18, ry - 26), (rx + 18, ry + 16)], fill=(180, 180, 178), width=2)
    # explosion burst where the rocket broke apart
    bx, by = rx - 6, ry + 34
    for ang in range(0, 360, 30):
        a = math.radians(ang)
        r1 = 26 if ang % 60 == 0 else 16
        d.line([(bx + 8 * math.cos(a), by + 8 * math.sin(a)),
                (bx + r1 * math.cos(a), by + r1 * math.sin(a))],
               fill=(235, 130, 40), width=4)
    d.ellipse([bx - 12, by - 12, bx + 12, by + 12], fill=(255, 200, 60))
    # lower stage tumbling away down-left, trailing smoke
    lx, ly = rx - 62, ry + 66
    d.polygon([(lx - 16, ly - 14), (lx + 10, ly - 20), (lx + 16, ly + 2),
               (lx - 10, ly + 8)], fill=(160, 164, 168))
    d.polygon([(lx - 16, ly - 14), (lx - 28, ly - 2), (lx - 14, ly - 2)],
              fill=(140, 144, 148))
    smoke(d, lx - 44, ly - 34)
    # two satellites tumbling down, solar panels askew
    for sx, sy, tilt in ((x + 52, y + 128, 1), (x + w - 76, y + 138, -1)):
        d.rectangle([sx - 26, sy - 6, sx - 8, sy + 6], fill=(30, 90, 160))
        d.rectangle([sx + 8, sy - 6, sx + 26, sy + 6], fill=(30, 90, 160))
        d.rectangle([sx - 8, sy - 8, sx + 8, sy + 8], fill=(200, 206, 212))
        d.line([(sx - 26, sy + tilt * 6), (sx + 26, sy - tilt * 6)],
               fill=(120, 124, 128), width=2)


# ---------------------------------------------------------------- tiles
STORIES = [
    ("UKRAINE · WAR", "KERCH BRIDGE SPAN FALLS",
     "A road span falls after a second night of strikes; Russia vows to rebuild.",
     (120, 60, 30), art_bridge),
    ("MIDDLE EAST · HORMUZ", "TANKERS HIT MINES",
     "Iran says two tankers struck mines and caught fire; a third carrier arrives.",
     (150, 52, 44), art_tankers),
    ("USA · ASEAN", "TRUMP LANDS IN MANILA",
     "Trump arrives for ASEAN and signs a joint trade statement with Thailand.",
     (0, 90, 140), art_manila),
    ("CHINA · DIPLOMACY", "XI-TRUMP-PUTIN MEETING SET",
     "China confirms the first three-way meeting, set for Thursday in Shenzhen.",
     (178, 34, 34), art_summit),
    ("USA · BANKING", "JPMORGAN BLAMES A BUG",
     "A bug, not a cyberattack, hit online banking, branches and Zelle.",
     (30, 122, 52), art_bank),
    ("USA · SPACE", "VULCAN ROCKET FAILS",
     "A ULA Vulcan rocket fails in flight, destroying 40 Amazon Leo satellites.",
     (90, 110, 130), art_rocket),
]


def draw_tile(d, x, y, w, h, kicker, headline, sub, accent, art):
    d.rounded_rectangle([x, y, x + w, y + h], radius=10, fill=CARD, outline=BORDER, width=2)
    art_h = 180
    art(d, x + 2, y + 2, w - 4, art_h)
    ty = y + art_h + 14
    d.text((x + 18, ty), kicker, font=font(BOLD, 17), fill=accent)
    hl = wrap(d, headline, font(BOLD, 30), w - 36)
    hy = ty + 26
    for line in hl:
        d.text((x + 18, hy), line, font=font(BOLD, 30), fill=INK)
        hy += 36
    sl = wrap(d, sub, font(REG, 20), w - 36)
    sy = hy + 6
    for line in sl[:3]:
        d.text((x + 18, sy), line, font=font(REG, 20), fill=GREY)
        sy += 26


def main():
    img = Image.new("RGB", (W, H), PAPER)
    d = ImageDraw.Draw(img)
    draw_header(d)
    margin, gap = 12, 12
    cols, rows = 3, 2
    tw = (W - 2 * margin - (cols - 1) * gap) // cols
    th = (984 - 164 - (rows - 1) * gap) // rows
    for i, (kicker, headline, sub, accent, art) in enumerate(STORIES):
        cx = i % cols
        cy = i // cols
        tx = margin + cx * (tw + gap)
        ty = 164 + cy * (th + gap)
        draw_tile(d, tx, ty, tw, th, kicker, headline, sub, accent, art)
    center_text(d, W // 2, 992, "Sources: BBC, Al Jazeera, Reuters, AP  ·  Tuesday 17 November 2026",
                font(REG, 17), GREY)
    img.save("entry.png", format="PNG", optimize=True)
    print("wrote entry.png")


if __name__ == "__main__":
    main()
