#!/usr/bin/env python3
"""Draw the news-image-20261117 entry: one infographic summing up
Tuesday 17 November 2026.

Renders a 1024x1024 PNG: a newspaper front page, "THE WORLD TODAY",
with three large illustrated lead stories and a dense index of thirty
more verified stories from the same day, so the day reads from the
image alone. Every story below was checked against reporting dated
17 November 2026 (BBC, Reuters, AP, CNN, NYT, NPR, Al Jazeera and
others); each either happened or was first reported on that day.

Run:  python3 draw.py            (writes entry.png next to this script)
Uses only Pillow and the DejaVu fonts present on this machine.
The drawing is deterministic: same code, same bytes, every run.
"""
import math
import textwrap
from PIL import Image, ImageDraw, ImageFont

W, H = 1024, 1024
BOLD = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"
REG = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"

NAVY = (19, 35, 63)
NAVY_DARK = (13, 25, 46)
AMBER = (232, 163, 23)
PAPER = (247, 245, 240)
INK = (24, 28, 34)
GREY = (88, 94, 102)
CARD = (255, 255, 255)
BORDER = (214, 212, 206)
RULE = (226, 224, 218)


def fnt(path, size):
    return ImageFont.truetype(path, size)


def wrap_lines(draw, text, font, max_w):
    """Greedy word wrap; returns the lines that fit inside max_w."""
    out = []
    for chunk in text.split("\n"):
        words = chunk.split()
        cur = ""
        for word in words:
            trial = (cur + " " + word).strip()
            if draw.textlength(trial, font=font) <= max_w:
                cur = trial
            else:
                if cur:
                    out.append(cur)
                cur = word
        if cur:
            out.append(cur)
    return out


def fit_one_line(draw, text, font, max_w, ell="..."):
    """Shorten text with an ellipsis until it fits max_w on one line."""
    if draw.textlength(text, font=font) <= max_w:
        return text
    while text and draw.textlength(text + ell, font=font) > max_w:
        text = text[:-1].rstrip()
    return text + ell if text else ell


def centred(draw, cx, y, text, font, fill):
    draw.text((cx - draw.textlength(text, font=font) / 2, y),
              text, font=font, fill=fill)


def flame(d, x, y, s):
    """A small orange flame centred at (x, y), size s."""
    d.polygon([(x, y - s), (x + s * 0.55, y - s * 0.1),
               (x + s * 0.3, y + s * 0.5), (x - s * 0.3, y + s * 0.5),
               (x - s * 0.55, y - s * 0.1)], fill=(235, 130, 40))
    d.polygon([(x, y - s * 0.55), (x + s * 0.3, y),
               (x, y + s * 0.4), (x - s * 0.3, y)], fill=(255, 200, 60))


def puff(d, x, y):
    for i, r in enumerate((15, 11, 8)):
        d.ellipse([x + i * 8 - r, y + i * 11 - r,
                   x + i * 8 + r, y + i * 11 + r], fill=(148, 154, 160))


# ---------------------------------------------------------------- header
def draw_header(d):
    d.rectangle([0, 0, W, 104], fill=NAVY)
    d.rectangle([0, 104, W, 108], fill=AMBER)
    centred(d, W // 2, 12, "T U E S D A Y   1 7   N O V E M B E R   2 0 2 6",
            fnt(BOLD, 21), AMBER)
    centred(d, W // 2, 32, "THE WORLD TODAY", fnt(BOLD, 46), (255, 255, 255))
    centred(d, W // 2, 86,
            "33 verified stories from the day \u2014 every region, every beat",
            fnt(REG, 15), (196, 205, 220))


# ---------------------------------------------------------------- lead art
def art_kerch(d, x, y, w, h):
    """A long sea bridge; its middle road span has collapsed."""
    d.rectangle([x, y, x + w, y + h], fill=(196, 217, 232))
    d.rectangle([x, y + 78, x + w, y + h], fill=(104, 156, 188))
    d.line([(x + 12, y + 96), (x + 80, y + 96)], fill=(255, 255, 255), width=3)
    d.line([(x + w - 110, y + 106), (x + w - 26, y + 106)], fill=(255, 255, 255), width=3)
    # deck: left and right spans, a gap in the middle
    d.rectangle([x + 8, y + 58, x + w // 2 - 30, y + 68], fill=(74, 85, 96))
    d.rectangle([x + w // 2 + 30, y + 58, x + w - 8, y + 68], fill=(74, 85, 96))
    # fallen span, tilted down into the water
    d.polygon([(x + w // 2 - 30, y + 66), (x + w // 2 + 26, y + 68),
               (x + w // 2 + 18, y + 92), (x + w // 2 - 22, y + 90)],
              fill=(52, 60, 70))
    # two towers with cables
    for tx in (x + 48, x + w - 48):
        d.rectangle([tx - 5, y + 12, tx + 5, y + 58], fill=(90, 101, 112))
        d.rectangle([tx - 13, y + 8, tx + 13, y + 16], fill=(90, 101, 112))
    d.line([(x + 48, y + 16), (x + w // 2 - 30, y + 58)], fill=(140, 148, 156), width=3)
    d.line([(x + w - 48, y + 16), (x + w // 2 + 30, y + 58)], fill=(140, 148, 156), width=3)
    d.line([(x + 48, y + 16), (x + 8, y + 58)], fill=(140, 148, 156), width=3)
    d.line([(x + w - 48, y + 16), (x + w - 8, y + 58)], fill=(140, 148, 156), width=3)
    flame(d, x + w // 2, y + 76, 15)
    puff(d, x + w // 2 + 12, y + 30)


def art_radar(d, x, y, w, h):
    """A radar dish at night; drones approach and one is intercepted."""
    d.rectangle([x, y, x + w, y + h], fill=(22, 32, 54))
    for sx, sy in ((28, 18), (88, 40), (250, 16), (292, 46), (180, 12), (140, 52)):
        d.ellipse([x + sx, y + sy, x + sx + 4, y + sy + 4], fill=(255, 255, 255))
    # ground
    d.rectangle([x, y + 92, x + w, y + h], fill=(38, 48, 66))
    # radar pedestal and dish
    bx = x + 64
    d.rectangle([bx - 4, y + 66, bx + 4, y + 92], fill=(150, 158, 166))
    d.rectangle([bx - 34, y + 88, bx + 34, y + 96], fill=(120, 128, 136))
    d.pieslice([bx - 52, y + 8, bx + 52, y + 92], start=200, end=340,
               fill=(210, 216, 222))
    d.line([(bx, y + 50), (bx + 44, y + 22)], fill=(232, 163, 23), width=3)
    # sweeping beam
    d.polygon([(bx, y + 50), (bx + 88, y + 12), (bx + 96, y + 34)],
              fill=(232, 163, 23))
    # three drones: small dark quadcopters with red lights
    for dx, dy in ((x + 208, y + 30), (x + 252, y + 52), (x + 296, y + 24)):
        d.rectangle([dx - 12, dy - 3, dx + 12, dy + 3], fill=(16, 18, 22))
        d.line([(dx - 18, dy - 6), (dx - 6, dy - 6)], fill=(120, 124, 128), width=3)
        d.line([(dx + 6, dy - 6), (dx + 18, dy - 6)], fill=(120, 124, 128), width=3)
        d.ellipse([dx - 2, dy - 2, dx + 2, dy + 2], fill=(230, 60, 50))
    # interception burst near the closest drone
    ix, iy = x + 214, y + 44
    for ang in range(0, 360, 45):
        a = math.radians(ang)
        d.line([(ix + 5 * math.cos(a), iy + 5 * math.sin(a)),
                (ix + 16 * math.cos(a), iy + 16 * math.sin(a))],
               fill=(255, 200, 60), width=3)
    d.ellipse([ix - 6, iy - 6, ix + 6, iy + 6], fill=(255, 220, 120))


def art_manila(d, x, y, w, h):
    """An airliner landing over a harbour city skyline at dusk."""
    d.rectangle([x, y, x + w, y + h], fill=(222, 235, 246))
    d.ellipse([x + w - 58, y + 10, x + w - 22, y + 46], fill=(245, 200, 90))
    # skyline
    d.rectangle([x, y + 84, x + w, y + h], fill=(168, 178, 188))
    for bx, bw, bh in ((12, 42, 30), (62, 28, 46), (98, 48, 26), (154, 34, 40),
                       (196, 44, 30), (248, 32, 44), (288, 26, 34)):
        d.rectangle([x + bx, y + 84 - bh, x + bx + bw, y + 84], fill=(118, 130, 144))
        for wy in range(y + 88 - bh, y + 78, 13):
            for wx in range(x + bx + 5, x + bx + bw - 5, 11):
                d.rectangle([wx, wy, wx + 4, wy + 6], fill=(255, 220, 120))
    # airliner: slim fuselage, tail fin, wing below
    px, py = x + 46, y + 48
    d.ellipse([px, py - 11, px + 152, py + 11], fill=(30, 50, 80))
    d.polygon([(px + 142, py - 9), (px + 180, py), (px + 142, py + 9)],
              fill=(30, 50, 80))
    d.polygon([(px + 6, py - 7), (px + 22, py - 34), (px + 36, py - 7)],
              fill=(24, 42, 68))
    d.polygon([(px + 74, py + 7), (px + 100, py + 32), (px + 114, py + 7)],
              fill=(24, 42, 68))
    for wx in range(6):
        d.ellipse([px + 14 + wx * 16, py - 4, px + 22 + wx * 16, py + 2],
                  fill=(180, 210, 235))
    # two small flags on poles at the runway: Philippines, then China.
    # Kept inside the art box (which is 118 tall) so they never touch
    # the kicker line below the picture.
    for fx0, top, mid, bot, stars in (
            (x + 22, (0, 56, 147), (255, 255, 255), (206, 17, 38), False),
            (x + w - 68, (222, 41, 16), (222, 41, 16), (222, 41, 16), True)):
        d.line([(fx0 + 22, y + 62), (fx0 + 22, y + 98)], fill=(80, 70, 60), width=4)
        d.rectangle([fx0, y + 62, fx0 + 44, y + 68], fill=top)
        d.rectangle([fx0, y + 68, fx0 + 44, y + 74], fill=mid)
        d.rectangle([fx0, y + 74, fx0 + 44, y + 80], fill=bot)
        if stars:
            for sx, sy in ((8, 66), (18, 64), (26, 70), (18, 74)):
                d.ellipse([fx0 + sx, y + sy, fx0 + sx + 5, y + sy + 5],
                          fill=(255, 215, 0))


# ---------------------------------------------------------------- stories
# (kicker, headline, sub, accent, art) for the three lead tiles.
LEADS = [
    ("UKRAINE \u00b7 WAR", "KERCH BRIDGE FALLS",
     "Second night of strikes downs a road span; Russia vows to rebuild.",
     (120, 60, 30), art_kerch),
    ("MIDDLE EAST \u00b7 IRAN", "IRAN DRONES HIT RADAR",
     "US radar base in Bahrain attacked by drones; 'dirty bomb' plot warned.",
     (150, 52, 44), art_radar),
    ("ASIA \u00b7 DIPLOMACY", "TRUMP LANDS IN MANILA",
     "Trump opens Asia trip at ASEAN, then Shenzhen for Xi\u2013Trump\u2013Putin talks.",
     (0, 90, 140), art_manila),
]

# (category, headline, one-line sub, accent) for the thirty index items.
# Headlines are kept to one line; subs are kept short enough for one line.
INDEX = [
    ("MIDDLE EAST \u00b7 HORMUZ", "TANKERS HIT MINES",
     "Two tankers hit mines and burned off Hormuz.", (150, 52, 44)),
    ("UKRAINE \u00b7 WAR", "KYIV BRIDGES STRUCK",
     "Russian strikes shut Kyiv's river bridges.", (120, 60, 30)),
    ("ASIA \u00b7 AIRSPACE", "JAPAN SCRAMBLES JETS",
     "Suspected Russian jets enter Japan's airspace.", (0, 90, 140)),
    ("UK \u00b7 WEST BANK", "UK SANCTIONS SETTLERS",
     "UK sanctions 8 West Bank settlement builders.", (178, 34, 34)),
    ("WEST BANK \u00b7 VIOLENCE", "WEST BANK KILLING",
     "Settlers kill a 72-year-old woman in Jericho.", (178, 34, 34)),
    ("MIDDLE EAST \u00b7 GAZA", "GAZA AID CALL",
     "Four nations urge Israel to open Gaza crossings.", (150, 52, 44)),
    ("ISRAEL \u00b7 ELECTIONS", "ISRAEL VOTE PROBE",
     "Netanyahu camp accused over election arrests.", (178, 34, 34)),
    ("YEMEN \u00b7 WAR", "HOUTHI ADVANCE",
     "Yemen forces retreat from Red Sea coast to Aden.", (120, 60, 30)),
    ("EUROPE \u00b7 BALTICS", "ESTONIA CLOSES BORDER",
     "Estonia shuts Russia border Dec 1 over plot.", (0, 90, 140)),
    ("UN \u00b7 GENEVA", "AUTONOMOUS WEAPONS",
     "128 states meet in Geneva over killer-robot ban.", (0, 90, 140)),
    ("CHINA \u00b7 CANADA", "XI\u2013CARNEY TARIFF CUTS",
     "China and Canada agree tariff cuts worth $280m.", (178, 34, 34)),
    ("ASIA \u00b7 MONGOLIA", "MONGOLIA PRESIDENT QUITS",
     "President quits after $25m railway graft claim.", (120, 60, 30)),
    ("USA \u00b7 EMERGENCY", "FEMA ALERT TEST",
     "US alert test 2:20pm ET; FEMA: 'No blackouts.'", (30, 122, 52)),
    ("USA \u00b7 NEW YORK", "MAMDANI DISBANDS SRG",
     "NYC mayor disbands NYPD protest-response unit.", (30, 122, 52)),
    ("USA \u00b7 CALIFORNIA", "NEWSOM SUED",
     "Suit fights commutation of 548 death sentences.", (30, 122, 52)),
    ("USA \u00b7 COURTS", "SUPREME COURT: DEI",
     "Court declines DEI appeals, stalling grant cuts.", (30, 122, 52)),
    ("USA \u00b7 HEALTH", "MEASLES STATUS LOST",
     "US loses measles-free status held for 30 years.", (30, 122, 52)),
    ("USA \u00b7 MARKETS", "NVIDIA BEATS, STOCKS FALL",
     "Nvidia beats on $115.8bn; S&P falls 1.03%.", (90, 110, 130)),
    ("USA \u00b7 TECH", "CHIP EXPORT CURBS",
     "US curbs China chip access via foreign centres.", (90, 110, 130)),
    ("USA \u00b7 AI", "CALIFORNIA SUES OPENAI",
     "California sues OpenAI over unsafe AI models.", (90, 110, 130)),
    ("USA \u00b7 TECH", "MICROSOFT OUTAGE CAUSE",
     "Microsoft blames defect for 80%-server outage.", (90, 110, 130)),
    ("USA \u00b7 SPACE", "VULCAN ROCKET FAILS",
     "ULA Vulcan fails; Amazon satellite payload lost.", (90, 110, 130)),
    ("EU \u00b7 TECH", "EU CHARGES TEMU",
     "EU charges Temu over illegal goods on platform.", (0, 90, 140)),
    ("CLIMATE \u00b7 COP31", "COP31: IPCC FIGHT",
     "COP31: Europe, China resist IPCC report delay.", (30, 122, 52)),
    ("CLIMATE \u00b7 ENERGY", "DATA CENTRES EMIT",
     "US data centres emit 25.7m tonnes CO2 a year.", (30, 122, 52)),
    ("AFRICA \u00b7 HEALTH", "EBOLA: 5,500 DEAD",
     "DR Congo Ebola: 11,200 cases and 5,500 dead.", (120, 60, 30)),
    ("AFRICA \u00b7 CRIME", "17 DEAD IN SA SHOOTINGS",
     "17 dead in two mass shootings in South Africa.", (120, 60, 30)),
    ("EUROPE \u00b7 CULTURE", "DEPARDIEU PLEADS GUILTY",
     "Depardieu admits sexual assault charge in Paris.", (178, 34, 34)),
    ("ASIA \u00b7 SPORT", "INDIA WIN SAFF CUP",
     "India beat Pakistan 2-1; record 10th SAFF title.", (0, 90, 140)),
    ("EUROPE \u00b7 SPORT", "ALCARAZ WINS IN TURIN",
     "Alcaraz beats Tiafoe 6-2, 6-2 at ATP Finals.", (0, 90, 140)),
]


def draw_lead(d, x, y, w, h, kicker, headline, sub, accent, art):
    d.rounded_rectangle([x, y, x + w, y + h], radius=10,
                        fill=CARD, outline=BORDER, width=2)
    art_h = 118
    art(d, x + 2, y + 2, w - 4, art_h)
    ty = y + art_h + 8
    d.text((x + 16, ty), kicker, font=fnt(BOLD, 13), fill=accent)
    hl = wrap_lines(d, headline, fnt(BOLD, 20), w - 32)
    hy = ty + 18
    for line in hl[:2]:
        d.text((x + 16, hy), line, font=fnt(BOLD, 20), fill=INK)
        hy += 25
    sl = wrap_lines(d, sub, fnt(REG, 15), w - 32)
    sy = hy + 2
    for line in sl[:2]:
        d.text((x + 16, sy), line, font=fnt(REG, 15), fill=GREY)
        sy += 19


def draw_index_cell(d, x, y, w, cat, headline, sub, accent):
    """One compact index entry: category, one-line headline, one-line sub."""
    d.text((x, y), cat, font=fnt(BOLD, 11), fill=accent)
    hl_font = fnt(BOLD, 15)
    headline = fit_one_line(d, headline, hl_font, w)
    d.text((x, y + 15), headline, font=hl_font, fill=INK)
    sub_font = fnt(REG, 13)
    sub = fit_one_line(d, sub, sub_font, w)
    d.text((x, y + 34), sub, font=sub_font, fill=GREY)


def main():
    img = Image.new("RGB", (W, H), PAPER)
    d = ImageDraw.Draw(img)
    draw_header(d)

    margin, gap = 12, 12
    cols = 3
    tw = (W - 2 * margin - (cols - 1) * gap) // cols
    lead_y, lead_h = 118, 236
    for i, (kicker, headline, sub, accent, art) in enumerate(LEADS):
        tx = margin + i * (tw + gap)
        draw_lead(d, tx, lead_y, tw, lead_h, kicker, headline, sub, accent, art)

    # section divider
    div_y = 366
    d.rectangle([margin, div_y, W - margin, div_y + 2], fill=AMBER)
    d.text((margin, div_y + 8), "MORE FROM THE DAY \u2014 30 STORIES",
           font=fnt(BOLD, 16), fill=NAVY)
    d.text((W - margin - d.textlength("WAR \u00b7 DIPLOMACY \u00b7 MARKETS \u00b7 TECH \u00b7 CLIMATE \u00b7 SPORT",
                                     font=fnt(REG, 14)), div_y + 10),
           "WAR \u00b7 DIPLOMACY \u00b7 MARKETS \u00b7 TECH \u00b7 CLIMATE \u00b7 SPORT",
           font=fnt(REG, 14), fill=GREY)

    # index grid: 3 columns x 10 rows
    grid_y, row_h = 398, 58
    for i, (cat, headline, sub, accent) in enumerate(INDEX):
        cx = i % cols
        cy = i // cols
        tx = margin + cx * (tw + gap)
        ty = grid_y + cy * row_h
        draw_index_cell(d, tx, ty, tw, cat, headline, sub, accent)
        if cy < 9:
            d.line([(margin, ty + row_h - 6), (W - margin, ty + row_h - 6)],
                   fill=RULE, width=1)

    centred(d, W // 2, 988,
            "Sources: BBC, Reuters, AP, CNN, NYT, NPR, Al Jazeera  \u00b7  "
            "Tuesday 17 November 2026",
            fnt(REG, 14), GREY)
    img.save("entry.png", format="PNG", optimize=True)
    print("wrote entry.png")


if __name__ == "__main__":
    main()
