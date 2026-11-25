#!/usr/bin/env python3
"""Draw the 25 November 2026 news-image entry: a newspaper front page.

Six verified stories from Wednesday 25 November 2026, drawn with PIL
into a single 1024x1024 PNG. No network, no outside files: every word
and every shape is in this file.
"""

from PIL import Image, ImageDraw, ImageFont

W, H = 1024, 1024
PAPER = (248, 244, 236)
NAVY = (26, 42, 74)
INK = (30, 30, 30)
GREY = (90, 88, 82)
CARD = (255, 255, 255)
CARD_LINE = (205, 198, 182)
RED = (178, 58, 48)

SERIF = "/usr/share/fonts/truetype/dejavu/DejaVuSerif.ttf"
SERIF_B = "/usr/share/fonts/truetype/dejavu/DejaVuSerif-Bold.ttf"
SANS = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"
SANS_B = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"
SERIF_I = "/usr/share/fonts/truetype/liberation/LiberationSerif-Italic.ttf"


def font(path, size):
    return ImageFont.truetype(path, size)


def wrap(draw, text, fnt, width):
    """Greedy word wrap, measured with the real font."""
    words, lines, cur = text.split(), [], ""
    for word in words:
        trial = (cur + " " + word).strip()
        if draw.textlength(trial, font=fnt) <= width:
            cur = trial
        else:
            if cur:
                lines.append(cur)
            cur = word
    if cur:
        lines.append(cur)
    return lines


def draw_icon(draw, kind, x, y, s, color):
    """A small pictogram, drawn from shapes, inside a s x s box."""
    if kind == "port":
        # anchor: ring, shaft, crossbar, flukes
        cx, cy = x + s // 2, y + s // 2
        draw.ellipse([cx - 6, y + 2, cx + 6, y + 14], outline=color, width=3)
        draw.line([cx, y + 14, cx, y + s - 8], fill=color, width=3)
        draw.line([cx - 12, y + 20, cx + 12, y + 20], fill=color, width=3)
        draw.arc([x + 2, y + s - 22, x + s - 2, y + s], 0, 180, fill=color, width=3)
        draw.line([x + 4, y + s - 8, x + 12, y + s - 16], fill=color, width=3)
        draw.line([x + s - 4, y + s - 8, x + s - 12, y + s - 16], fill=color, width=3)
    elif kind == "tanker":
        # ship hull, containers, waves
        draw.polygon([(x + 2, y + s - 16), (x + s - 2, y + s - 16),
                      (x + s - 10, y + s - 4), (x + 10, y + s - 4)],
                     outline=color, width=3)
        draw.rectangle([x + 10, y + 8, x + 22, y + s - 18], outline=color, width=2)
        draw.rectangle([x + 26, y + 12, x + 38, y + s - 18], outline=color, width=2)
        draw.line([x + s - 14, y + 6, x + s - 14, y + s - 18], fill=color, width=2)
        draw.arc([x, y + s - 8, x + 16, y + s + 2], 180, 360, fill=color, width=2)
        draw.arc([x + s - 16, y + s - 8, x + s, y + s + 2], 180, 360, fill=color, width=2)
    elif kind == "rocket":
        # nose cone, body, fins, flame
        cx = x + s // 2
        draw.polygon([(cx, y + 2), (cx + 9, y + 18), (cx - 9, y + 18)], fill=color)
        draw.rectangle([cx - 9, y + 18, cx + 9, y + s - 14], outline=color, width=3)
        draw.ellipse([cx - 4, y + 24, cx + 4, y + 32], outline=color, width=2)
        draw.polygon([(cx - 9, y + s - 14), (cx - 16, y + s - 4), (cx - 9, y + s - 6)],
                     fill=color)
        draw.polygon([(cx + 9, y + s - 14), (cx + 16, y + s - 4), (cx + 9, y + s - 6)],
                     fill=color)
        draw.polygon([(cx - 4, y + s - 12), (cx + 4, y + s - 12), (cx, y + s - 1)],
                     fill=RED)
    elif kind == "train":
        # front of a train: body, window, stripe, wheels
        draw.rounded_rectangle([x + 2, y + 4, x + s - 2, y + s - 10], radius=8,
                               outline=color, width=3)
        draw.rounded_rectangle([x + 8, y + 10, x + s - 8, y + 22], radius=4,
                               outline=color, width=2)
        draw.line([x + 4, y + s - 18, x + s - 4, y + s - 18], fill=color, width=3)
        draw.ellipse([x + 8, y + s - 12, x + 16, y + s - 4], outline=color, width=2)
        draw.ellipse([x + s - 16, y + s - 12, x + s - 8, y + s - 4],
                     outline=color, width=2)
    elif kind == "chess":
        # 3x3 board with a pawn
        cell = s // 3
        for r in range(3):
            for c in range(3):
                if (r + c) % 2 == 0:
                    draw.rectangle([x + c * cell, y + r * cell,
                                    x + (c + 1) * cell, y + (r + 1) * cell],
                                   fill=color)
        cx, cy = x + s // 2, y + s // 2
        draw.ellipse([cx - 7, cy - 12, cx + 7, cy + 2], fill=PAPER,
                     outline=NAVY, width=2)
        draw.polygon([(cx - 10, cy + 12), (cx + 10, cy + 12),
                      (cx + 5, cy + 1), (cx - 5, cy + 1)], fill=PAPER,
                     outline=NAVY, width=2)
    elif kind == "wave":
        # three stacked wave arcs
        for i, yy in enumerate([y + 6, y + 18, y + 30]):
            draw.arc([x, yy, x + s // 2, yy + 14], 180, 360, fill=color, width=3)
            draw.arc([x + s // 2, yy, x + s, yy + 14], 180, 360, fill=color, width=3)


STORIES = [
    ("HODEIDAH", "Coalition strikes Yemen port",
     "Saudi-led warplanes hit Hodeidah port early Wednesday, after an "
     "evacuation order. The Houthis threaten Saudi Red Sea ports, "
     "including Jeddah.", "port"),
    ("HORMUZ", "Iran says tankers hit mines",
     "Iran says two oil tankers struck naval mines and caught fire early "
     "Wednesday in the Strait of Hormuz, on what it calls an "
     "unauthorised route.", "tanker"),
    ("JIUQUAN", "Shenzhou-24 lifts off",
     "China launches Shenzhou-24, carrying Pakistan's Muhammad Zeeshan "
     "Ali, the first foreign astronaut to visit the Tiangong space "
     "station.", "rocket"),
    ("SEOUL", "Subway strike called off",
     "Seoul Metro unions call off a strike hours before the morning rush "
     "after a last-minute deal: a 3.5% pay rise, 500 new hires, and job "
     "cuts shelved.", "train"),
    ("GENEVA", "Chess crown: Game 2",
     "Gukesh and Sindarov play Game 2 of the world title match, level at "
     "half a point each after a 38-move draw in the opener. Gukesh has "
     "White.", "chess"),
    ("CALIFORNIA", "King tides peak",
     "Near-record king tides peak Wednesday on California's coast, "
     "flooding low streets as a storm hits Thanksgiving travel. San "
     "Francisco airport is on alert.", "wave"),
]


def main():
    img = Image.new("RGB", (W, H), PAPER)
    d = ImageDraw.Draw(img)

    # Masthead
    title_f = font(SERIF_B, 62)
    d.text((W // 2, 30), "THE WORLD IN ONE DAY", font=title_f, fill=NAVY,
           anchor="ma")
    d.line([(36, 108), (W - 36, 108)], fill=NAVY, width=3)
    d.line([(36, 114), (W - 36, 114)], fill=NAVY, width=1)

    # Navy date band
    d.rectangle([36, 128, W - 36, 172], fill=NAVY)
    date_f = font(SANS_B, 26)
    d.text((W // 2, 150), "WEDNESDAY  •  25 NOVEMBER 2026", font=date_f,
           fill=(255, 255, 255), anchor="mm")

    # Subhead
    sub_f = font(SERIF_I, 23)
    d.text((W // 2, 200), "Six stories from around the world — in one picture.",
           font=sub_f, fill=GREY, anchor="ma")

    # Story grid: 2 columns x 3 rows
    gx, gy = 36, 228
    gap = 20
    cw = (W - 2 * gx - gap) // 2
    ch = (950 - gy - 2 * gap) // 3
    kick_f = font(SANS_B, 16)
    head_f = font(SERIF_B, 25)
    body_f = font(SANS, 17)

    for i, (city, headline, body, icon) in enumerate(STORIES):
        row, col = divmod(i, 2)
        x0 = gx + col * (cw + gap)
        y0 = gy + row * (ch + gap)
        d.rectangle([x0, y0, x0 + cw, y0 + ch], fill=CARD, outline=CARD_LINE,
                    width=1)
        # kicker: city + icon, with a short red rule under the city
        pad = 16
        d.text((x0 + pad, y0 + 14), city, font=kick_f, fill=RED, anchor="la")
        d.line([(x0 + pad, y0 + 38), (x0 + pad + 34, y0 + 38)], fill=RED,
               width=2)
        draw_icon(d, icon, x0 + cw - pad - 40, y0 + 10, 40, NAVY)
        # headline, up to 2 lines
        lines = wrap(d, headline, head_f, cw - 2 * pad)[:2]
        hy = y0 + 48
        for ln in lines:
            d.text((x0 + pad, hy), ln, font=head_f, fill=INK, anchor="la")
            hy += 30
        # body, up to 4 lines
        blines = wrap(d, body, body_f, cw - 2 * pad)[:4]
        by = hy + 6
        for ln in blines:
            d.text((x0 + pad, by), ln, font=body_f, fill=INK, anchor="la")
            by += 23

    # Footer
    d.line([(36, 968), (W - 36, 968)], fill=CARD_LINE, width=1)
    foot_f = font(SANS, 15)
    d.text((W // 2, 986),
           "All six stories above happened or were first reported on 25 November 2026.",
           font=foot_f, fill=GREY, anchor="ma")

    img.save("entry.png", "PNG")
    print("wrote entry.png", img.size)


if __name__ == "__main__":
    main()
