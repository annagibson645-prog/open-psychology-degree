"""Make the favicon and link-preview images. Run once: python gen_assets.py"""
from PIL import Image, ImageDraw, ImageFont
import pathlib
here = pathlib.Path(__file__).parent
NAVY, BLUE, WHITE, MUTED = (15, 29, 68), (24, 53, 138), (255, 255, 255), (170, 190, 235)

SVG = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 100 100"><rect width="100" height="100" rx="22" fill="#18358A"/><g fill="none" stroke="#fff" stroke-width="7" stroke-linecap="round" stroke-linejoin="round"><path d="M50 14V84"/><path d="M26 16V30a24 24 0 0 0 48 0V16"/><path d="M36 84H64"/></g></svg>
'''
(here / "favicon.svg").write_text(SVG, encoding="utf-8")

def psi(size, bg=BLUE, radius=0.22, pad=0.0):
    S = size * 4
    im = Image.new("RGBA", (S, S), (0, 0, 0, 0))
    d = ImageDraw.Draw(im)
    d.rounded_rectangle((0, 0, S - 1, S - 1), radius=int(S * radius), fill=bg)
    k = S / 100.0
    w = int(7 * k)
    def L(x1, y1, x2, y2): d.line((x1 * k, y1 * k, x2 * k, y2 * k), fill=WHITE, width=w)
    L(50, 14, 50, 84); L(26, 16, 26, 30); L(74, 16, 74, 30); L(36, 84, 64, 84)
    d.arc((26 * k, 6 * k, 74 * k, 54 * k), 0, 180, fill=WHITE, width=w)
    for x, y in [(50, 14), (50, 84), (26, 16), (74, 16), (36, 84), (64, 84)]:  # round caps
        d.ellipse((x * k - w / 2, y * k - w / 2, x * k + w / 2, y * k + w / 2), fill=WHITE)
    return im.resize((size, size), Image.LANCZOS)

psi(32).save(here / "favicon-32.png")
psi(180, radius=0.0).convert("RGB").save(here / "apple-touch-icon.png")

# link preview 1200x630
W, H = 1200, 630
img = Image.new("RGB", (W, H), NAVY)
d = ImageDraw.Draw(img)
d.rectangle((0, 0, 14, H), fill=(199, 216, 255))
F = "C:/Windows/Fonts/"
title = ImageFont.truetype(F + "georgia.ttf", 92)
title_i = ImageFont.truetype(F + "georgiai.ttf", 92)
sub = ImageFont.truetype(F + "segoeui.ttf", 34)
small = ImageFont.truetype(F + "segoeui.ttf", 28)
img.paste(psi(120), (84, 84), psi(120))
d.text((84, 250), "Study Psychology,", font=title, fill=WHITE)
d.text((84, 356), "Tuition Free", font=title_i, fill=WHITE)
d.text((84, 492), "A free, self-directed degree built from open lectures and free textbooks.", font=sub, fill=MUTED)
d.text((84, 548), "Pick your classes. Track your progress. Everything saves in your browser.", font=small, fill=MUTED)
img.save(here / "og-image.png", optimize=True)
print("assets ok")
