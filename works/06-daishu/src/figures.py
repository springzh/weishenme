"""袋鼠为什么有袋 — every illustration of the episode (palette: sun-desert)."""
import math
from figkit import *
from characters import *        # 系列素材库 kit/：kangaroo、joey_bean……（kit/catalog.md）

POUCH_IN = (248, 228, 204)      # 育儿袋内壁（暖浅色，比纸略深）
MILK = (252, 250, 244)
TEAT = (226, 150, 132)


@figure("australia", 1000, 640)
def australia(f):
    """Australian grassland: sun, low hills, a big kangaroo with a joey and a smaller one."""
    sun(f, 880, 92, 46)
    f.shape([(0, 520), (120, 452), (260, 500), (390, 470), (520, 512), (700, 480), (860, 508),
             (1000, 486), (1000, 560), (0, 560)], C.sand, 5)
    ground(f, 20, 980, 518, 620, fill=C.ground)
    for x in (80, 330, 560, 790, 930):
        grass(f, x, 522, n=3, h=26)
    kangaroo(f, 250, 522, 0.45)
    kangaroo(f, 660, 522, 0.72, joey=True)


@figure("emblem", 700, 760)
def emblem(f):
    """A coat-of-arms shield with the kangaroo inside it, a star above (labels from the text layer)."""
    f.shape([(350, 40), (600, 110), (600, 420), (500, 560), (350, 700), (200, 560), (100, 420), (100, 110)], C.sand, 6)
    star(f, 350, 150, 36)
    kangaroo(f, 350, 620, 0.55)


@figure("kangaroo_full", 900, 760)
def kangaroo_full(f):
    """One standing kangaroo on grass, the pouch plain to see."""
    ground(f, 20, 880, 690, 745, fill=C.ground)
    for x in (120, 780):
        grass(f, x, 694, n=3, h=24)
    kangaroo(f, 450, 690, 0.95)


@figure("belly_cutaway", 900, 760)
def belly_cutaway(f):
    """The mother, plus a round inset showing the tiny bean-like baby inside her belly."""
    ground(f, 20, 880, 690, 745, fill=C.ground)
    kangaroo(f, 400, 690, 0.88)
    f.line([(520, 368), (666, 286)], 5, amp=0.2, smooth=False)          # pointer to the belly
    f.blot(516, 370, 8, 8)
    f.ellipse(758, 232, 104, 104, POUCH_IN, 6)                          # inset
    joey_bean(f, 758, 236, 1.15)


@figure("bean_scale", 1000, 620)
def bean_scale(f):
    """A pointing finger, the newborn beside it at true size, and a magnifier with the baby enlarged."""
    finger(f, 250, 548)
    joey_bean(f, 470, 440, 1.35)                                        # true size next to the finger
    joey_bean(f, 800, 296, 2.0)                                         # magnified
    magnifier(f, 800, 300, 152)


@figure("climb", 1000, 760)
def climb(f):
    """The mother standing; a wet dotted trail runs up her front to the pouch, the baby crawling on it."""
    ground(f, 20, 980, 690, 745, fill=C.ground)
    kangaroo(f, 560, 690, 0.9)
    trail = [(736, 686), (722, 632), (710, 580), (700, 528), (692, 478), (686, 436), (680, 398)]
    for k, (x, y) in enumerate(trail):
        for dx in ((0, 14) if k % 2 else (-8, 6)):
            f.line([(x + dx, y), (x + dx + 10, y + 4)], 5, amp=0.4, smooth=False)   # wet path: short dashes
    joey_bean(f, 712, 566, 0.42)


@figure("pouch_milk", 800, 620)
def pouch_milk(f):
    """Cross-section of the pouch: the baby inside, mouth on the teat."""
    _pouch(f, milk=False)


@figure("milk_spray", 800, 620)
def milk_spray(f):
    """Same pouch cross-section, now with milk jetting out of the teat into the baby's mouth."""
    _pouch(f, milk=True)


@figure("grow", 900, 700)
def grow(f):
    """The mother with a grown baby's head out of the pouch, a sparkle beside it."""
    ground(f, 20, 880, 636, 690, fill=C.ground)
    kangaroo(f, 460, 636, 0.9, joey=True)
    sparkle(f, 300, 250, 22)
    sparkle(f, 330, 200, 14)


@figure("leap", 1100, 600)
def leap(f):
    """The mother leaping flat out with the baby tucked in the pouch; speed lines behind."""
    ground(f, 30, 1070, 560, 592, fill=C.ground)
    for k in range(4):
        motion_lines(f, 250 + k * 40, 300 + k * 62, n=1, length=120, angle=0.2)
    kangaroo(f, 700, 520, 0.78, pose="leap", joey=True)
    for x in (250, 268, 286):
        f.blot(x, 548 - (x - 250) * 0.6, 18, 9, C.sand)


@figure("leap_far", 1100, 600)
def leap_far(f):
    """Two ground marks far apart with a dashed hop arc between them; the mother in mid-leap."""
    ground(f, 30, 1070, 560, 592, fill=C.ground)
    for x in (120, 980):
        f.line([(x, 430), (x, 556)], 6, amp=0.4, smooth=False)           # distance posts
    for k in range(9):
        t = k / 8
        x = 140 + t * 820
        y = 300 - 120 * math.sin(math.pi * t)
        f.line([(x - 14, y), (x + 14, y)], 5, amp=0.2, smooth=False)     # dashed arc
    kangaroo(f, 700, 470, 0.62, pose="leap", joey=True)


@figure("kangaroo_bean", 640, 620)
def kangaroo_bean(f):
    """Cover hero: the bean-sized newborn on a soft round backdrop, sparkles around it."""
    f.ellipse(320, 310, 250, 238, C.sand, 6)
    joey_bean(f, 320, 322, 2.9)
    sparkle(f, 92, 130, 22)
    sparkle(f, 552, 190, 16)
    sparkle(f, 560, 470, 20)


@figure("sanlian", 430, 170)
def sanlian_icons(f):
    sanlian(f, 215, 80, gap=130, r=44)


# ---------------------------------------------------------------- helpers
def _pouch(f, milk=False):
    """Pouch cross-section, open at the top: outer wall, inner cavity, teat, baby."""
    f.shape([(60, 108), (740, 108), (700, 430), (560, 544), (240, 544), (100, 430)], C.fur, 6)
    f.shape([(130, 166), (670, 166), (632, 408), (522, 492), (278, 492), (168, 408)], POUCH_IN, 5)
    for x in (196, 604):                                                # wall hairs
        for k in range(3):
            f.line([(x + k * 10, 300 + k * 40), (x + k * 10 - 14, 306 + k * 40)], 4, amp=0.2, smooth=False)
    f.shape(tube([(660, 320), (540, 322), (512, 328)], 18, 13), TEAT, 5, smooth=False)  # teat from the wall
    f.ellipse(504, 330, 20, 17, TEAT, 5)
    f.blot(504, 326, 6, 5, C.ink)
    joey_bean(f, 404, 356, 1.45)
    if milk:
        for (x, y) in ((492, 348), (476, 362), (508, 356), (462, 350)):
            f.ellipse(x, y, 8, 8, MILK, 3)
        for (x, y) in ((478, 392), (500, 390), (462, 384)):
            f.line([(x, y), (x + 4, y + 10)], 4, color=C.accent, amp=0.1, smooth=False)
