"""Code-drawn cartoon figures for the polar-bear explainer (十万个为什么·为什么北极熊不怕冷).

Hand-drawn feel: every outline is a smooth spline with low-frequency wobble, ~6px dark ink,
round caps; warm flat fills (no blue: the renderer treats cool colors as ink).
Each shape is filled then outlined, so later shapes overlap earlier ones cleanly.
Rendered 2x and downsampled. White background.
"""
import math
from pathlib import Path
import numpy as np
from PIL import Image, ImageDraw

import os
OUT = Path(os.environ.get("FIG_OUT") or Path(__file__).resolve().parents[1] / "inputs" / "figures")
OUT.mkdir(parents=True, exist_ok=True)
SS = 2
INK = (42, 38, 34)
BEAR = (246, 238, 218)      # cream polar-bear fur (min channel <235 so it stays opaque)
BEAR2 = (230, 220, 196)     # far-side legs, a shade darker
SKINK = (64, 58, 56)        # black skin / pads
FACE = (250, 224, 196)
CHEEK = (240, 170, 150)
COAT = (240, 160, 96)
COAT2 = (214, 132, 74)
SCARF = (246, 214, 130)
BOOT = (150, 100, 70)
EYE = (250, 210, 92)
RED = (224, 106, 78)
RAY = (238, 168, 72)
ICE = (226, 238, 242)       # pale ice: red>=218 so the renderer never treats it as cool ink
WATER = (220, 234, 242)
SNOW = (232, 238, 240)
HAIRC = (238, 242, 242)
CORE = (226, 236, 240)
FAT = (248, 222, 140)
FATC = (232, 196, 108)
MEAT = (238, 172, 152)
SEAL = (176, 164, 150)
rng = np.random.default_rng(2026)


def spline(pts, closed=False, n=14):
    """Catmull-Rom through control points."""
    P = np.asarray(pts, float)
    if closed:
        P = np.vstack([P[-1], P, P[0], P[1]])
    else:
        P = np.vstack([P[0], P, P[-1]])
    out = []
    for i in range(1, len(P) - 2):
        p0, p1, p2, p3 = P[i - 1], P[i], P[i + 1], P[i + 2]
        for t in np.linspace(0, 1, n, endpoint=False):
            t2, t3 = t * t, t * t * t
            out.append(0.5 * ((2 * p1) + (-p0 + p2) * t + (2 * p0 - 5 * p1 + 4 * p2 - p3) * t2 + (-p0 + 3 * p1 - 3 * p2 + p3) * t3))
    out.append(P[-2])
    return [tuple(p) for p in out]


def wobble(points, amp=1.8, step=8):
    pts = np.asarray(points, float)
    seg = np.r_[0, np.cumsum(np.linalg.norm(np.diff(pts, axis=0), axis=1))]
    if seg[-1] < 1:
        return [tuple(p) for p in pts]
    n = max(int(seg[-1] / step), 2)
    s = np.linspace(0, seg[-1], n)
    x, y = np.interp(s, seg, pts[:, 0]), np.interp(s, seg, pts[:, 1])
    phase, freq = rng.uniform(0, 6.28, 2), rng.uniform(0.008, 0.018, 2)
    noise = amp * (np.sin(s * freq[0] + phase[0]) + 0.5 * np.sin(s * freq[1] * 2.3 + phase[1])) / 1.5
    d = np.gradient(np.c_[x, y], axis=0)
    d /= np.linalg.norm(d, axis=1, keepdims=True) + 1e-9
    taper = np.minimum(1, np.minimum(s, seg[-1] - s) / 25 + 0.2)
    return [(float(a), float(b)) for a, b in zip(x - d[:, 1] * noise * taper, y + d[:, 0] * noise * taper)]


class Fig:
    def __init__(self, w, h):
        self.w, self.h = w, h
        self.im = Image.new("RGB", (w * SS, h * SS), "white")
        self.d = ImageDraw.Draw(self.im)

    def S(self, pts):
        return [(x * SS, y * SS) for x, y in pts]

    def line(self, pts, width=6, color=INK, amp=1.8, smooth=True):
        p = spline(pts) if smooth and len(pts) > 2 else list(pts)
        p = self.S(wobble(p, amp))
        self.d.line(p, fill=color, width=int(width * SS), joint="curve")
        r = width * SS / 2
        for x, y in (p[0], p[-1]):
            self.d.ellipse([x - r, y - r, x + r, y + r], fill=color)

    def shape(self, pts, fill, width=6, closed_spline=True, amp=1.6):
        """Filled closed shape with a single wobbly outline."""
        p = spline(pts, closed=True) if closed_spline else list(pts) + [pts[0]]
        self.d.polygon(self.S(p), fill=fill)
        if width:
            self.line(p + [p[0]], width, amp=amp, smooth=False)

    def ellipse(self, cx, cy, rx, ry, fill, width=6, rot=0):
        pts = [(cx + rx * math.cos(t) * math.cos(rot) - ry * math.sin(t) * math.sin(rot),
                cy + rx * math.cos(t) * math.sin(rot) + ry * math.sin(t) * math.cos(rot)) for t in np.linspace(0, 2 * math.pi, 40, endpoint=False)]
        self.shape(pts, fill, width, closed_spline=False, amp=0.8)

    def blot(self, cx, cy, rx, ry, color, rot=0):
        """Fill only (no outline) — used for pupils / spots."""
        pts = [(cx + rx * math.cos(t) * math.cos(rot) - ry * math.sin(t) * math.sin(rot),
                cy + rx * math.cos(t) * math.sin(rot) + ry * math.sin(t) * math.cos(rot)) for t in np.linspace(0, 2 * math.pi, 40)]
        self.d.polygon(self.S(pts), fill=color)

    def arrowhead(self, tip, direction, size=20, width=6, color=INK):
        ang = math.atan2(direction[1], direction[0])
        for da in (2.6, -2.6):
            self.line([tip, (tip[0] + size * math.cos(ang + da), tip[1] + size * math.sin(ang + da))], width, color=color, amp=0.4)

    def save(self, name):
        self.im.resize((self.w, self.h), Image.Resampling.LANCZOS).save(OUT / f"{name}.png")
        print(name, self.w, self.h)


def tube(center, w0, w1):
    """Polygon around a centerline, tapering from half-width w0 to w1."""
    c = np.asarray(spline(center, n=8), float)
    d = np.gradient(c, axis=0)
    d /= np.linalg.norm(d, axis=1, keepdims=True) + 1e-9
    nrm = np.c_[-d[:, 1], d[:, 0]]
    w = np.linspace(w0, w1, len(c))[:, None]
    left, right = c + nrm * w, c - nrm * w
    return [tuple(p) for p in np.vstack([left, right[::-1]])]


def T(pts, cx, cy, s=1.0, rot=0.0):
    ca, sa = math.cos(rot), math.sin(rot)
    return [(cx + s * (x * ca - y * sa), cy + s * (x * sa + y * ca)) for x, y in pts]


# ---------------------------------------------------------------- polar bear (side view, facing right)
HEAD_PIVOT = (175, -70)


def rot_about(pts, pivot, a):
    ca, sa = math.cos(a), math.sin(a)
    px, py = pivot
    return [(px + (x - px) * ca - (y - py) * sa, py + (x - px) * sa + (y - py) * ca) for x, y in pts]


def leg_len(crouch):
    return 165 - 45 * crouch


def bear(f, cx, cy, s=1.0, head_rot=0.0, crouch=0.0, lw=6):
    """Side-view polar bear. Local frame: feet near y=leg_len+17, nose at x~384."""
    g = lambda pts: T(pts, cx, cy, s)
    hp = lambda pts: g(rot_about(pts, HEAD_PIVOT, head_rot))
    ly = leg_len(crouch)
    lw2 = max(lw - 1, 3)
    # far-side legs (behind the body)
    f.shape(g(tube([(110, 20), (116, 90), (120, ly)], 25, 22)), BEAR2, lw2, closed_spline=False)
    x, y = g([(134, ly + 4)])[0]; f.ellipse(x, y, 32 * s, 12 * s, BEAR2, lw2)
    f.shape(g(tube([(-128, 30), (-126, 100), (-124, ly)], 30, 24)), BEAR2, lw2, closed_spline=False)
    x, y = g([(-110, ly + 4)])[0]; f.ellipse(x, y, 34 * s, 12 * s, BEAR2, lw2)
    # near-side legs (their tops tuck under the body)
    f.shape(g(tube([(152, 30), (160, 95), (166, ly)], 27, 24)), BEAR, lw, closed_spline=False)
    x, y = g([(182, ly + 4)])[0]; f.ellipse(x, y, 36 * s, 13 * s, BEAR, lw)
    f.shape(g(tube([(-188, 25), (-182, 100), (-176, ly)], 33, 26)), BEAR, lw, closed_spline=False)
    x, y = g([(-160, ly + 4)])[0]; f.ellipse(x, y, 38 * s, 13 * s, BEAR, lw)
    # tail, then body over the leg tops
    x, y = g([(-250, -44)])[0]; f.ellipse(x, y, 18 * s, 14 * s, BEAR, lw2)
    f.shape(g([(-255, -20), (-225, -100), (-130, -140), (10, -138), (140, -115), (205, -70), (205, 20), (130, 65), (-40, 72), (-205, 55)]), BEAR, lw)
    # head: small ear, long head, eye, black nose, mouth
    x, y = hp([(224, -112)])[0]; f.ellipse(x, y, 15 * s, 12 * s, BEAR, lw2)
    f.shape(hp([(165, -95), (215, -122), (280, -110), (330, -88), (372, -70), (386, -54), (372, -38), (330, -28), (265, -14), (200, -12), (160, -40)]), BEAR, lw)
    x, y = hp([(300, -82)])[0]; f.blot(x, y, 7 * s + 1, 7 * s + 1, INK)
    x, y = hp([(377, -56)])[0]; f.blot(x, y, 13 * s, 10 * s, INK, rot=head_rot)
    f.line(hp([(356, -34), (334, -29)]), max(lw - 2, 3), amp=0.2, smooth=False)


def flake(f, x, y, r=14):
    for k in range(3):
        a = k * math.pi / 3
        f.line([(x - r * math.cos(a), y - r * math.sin(a)), (x + r * math.cos(a), y + r * math.sin(a))], 4, amp=0.1, smooth=False)


def fig_bear_side():
    f = Fig(900, 560)
    f.shape([(30, 468), (870, 462), (840, 540), (70, 545)], ICE, 6, closed_spline=False)
    bear(f, 430, 300)
    f.save("bear_side")


def fig_bear_swim():
    f = Fig(900, 480)
    bear(f, 380, 300, head_rot=-0.14, crouch=1.0)
    top = [(x, 292 + 7 * math.sin(x / 38)) for x in range(20, 881, 20)]
    f.shape(top + [(880, 460), (20, 460)], WATER, 6, closed_spline=False)
    for x0, y0 in ((90, 350), (300, 395), (560, 345), (700, 410), (170, 425)):
        f.line([(x0, y0), (x0 + 22, y0 - 8), (x0 + 44, y0), (x0 + 66, y0 - 8)], 4.5, amp=0.3)
    f.save("bear_swim")


def fig_bear_hunt():
    f = Fig(1000, 580)
    f.shape([(20, 380), (980, 370), (980, 560), (20, 560)], ICE, 6, closed_spline=False)
    f.ellipse(790, 432, 120, 36, WATER, 6)
    # seal head rising out of the breathing hole
    f.shape([(742, 440), (738, 380), (760, 345), (790, 336), (820, 345), (842, 380), (838, 440)], SEAL, 6)
    for sx in (-1, 1):
        f.blot(790 + sx * 18, 372, 8, 9, INK)
        for k in (-1, 0, 1):
            f.line([(790 + sx * 16, 398 + k * 6), (790 + sx * 46, 392 + k * 10)], 3, amp=0.1, smooth=False)
    f.blot(790, 392, 9, 6, INK)
    bear(f, 330, 243, head_rot=0.35, crouch=1.0)
    f.save("bear_hunt")


def fig_bear_snow():
    f = Fig(900, 600)
    f.shape([(20, 470), (880, 462), (880, 580), (20, 585)], SNOW, 6, closed_spline=False)
    for x, y in ((70, 60), (190, 120), (330, 45), (470, 105), (610, 50), (720, 118), (840, 66), (260, 90)):
        flake(f, x, y)
    for k, x in enumerate((60, 110, 160)):
        f.blot(x, 520 + (k % 2) * 22, 14, 8, (196, 196, 192))
    bear(f, 430, 300)
    f.save("bear_snow")


def fig_ice_melt():
    f = Fig(900, 560)
    f.ellipse(770, 110, 60, 60, EYE, 6)
    for k in range(8):
        a = k * math.pi / 4
        f.line([(770 + 78 * math.cos(a), 110 + 78 * math.sin(a)), (770 + 102 * math.cos(a), 110 + 102 * math.sin(a))], 5, amp=0.1, smooth=False)
    top = [(x, 332 + 6 * math.sin(x / 34)) for x in range(20, 881, 20)]
    f.shape(top + [(880, 545), (20, 545)], WATER, 6, closed_spline=False)
    for x0, y0 in ((80, 470), (640, 500), (260, 505)):
        f.line([(x0, y0), (x0 + 22, y0 - 8), (x0 + 44, y0), (x0 + 66, y0 - 8)], 4.5, amp=0.3)
    f.shape([(150, 392), (200, 386), (212, 404), (160, 410)], ICE, 5, closed_spline=False)
    f.shape([(700, 430), (770, 424), (782, 446), (708, 452)], ICE, 5, closed_spline=False)
    f.shape([(330, 336), (570, 328), (592, 352), (562, 376), (352, 380), (318, 356)], ICE, 6, closed_spline=False)
    bear(f, 452, 270, s=0.36, lw=5)
    f.save("ice_melt")


def fig_bear_head():
    """Front view of the head: small round ears, small eyes, black nose."""
    f = Fig(520, 460)
    for x in (150, 370):
        f.ellipse(x, 112, 42, 38, BEAR, 6)
        f.blot(x, 116, 20, 17, (214, 196, 176))
    f.shape([(260, 70), (380, 95), (450, 190), (440, 300), (370, 380), (260, 410), (150, 380), (80, 300), (70, 190), (140, 95)], BEAR, 6)
    for x in (205, 315):
        f.blot(x, 222, 10, 11, INK)
    f.ellipse(260, 322, 76, 56, (240, 230, 206), 5)
    f.blot(260, 296, 30, 20, INK)
    f.line([(260, 314), (260, 342)], 5, amp=0.1, smooth=False)
    f.line([(236, 356), (260, 342), (284, 356)], 5, amp=0.2)
    f.save("bear_head")


def fig_paw():
    """Underside of a paw: furry sole with small black pads."""
    f = Fig(560, 540)
    sole = [(110, 200), (150, 120), (280, 92), (410, 120), (450, 200), (462, 330), (420, 450), (280, 502), (140, 450), (98, 330)]
    f.shape(sole, BEAR, 6)
    for k in range(5):
        a = math.pi + (k + 0.5) * math.pi / 5
        f.ellipse(280 + 128 * math.cos(a), 262 + 105 * math.sin(a), 24, 20, SKINK, 5, rot=a)
    f.shape([(190, 330), (240, 290), (320, 290), (370, 330), (360, 395), (280, 420), (200, 395)], SKINK, 6)
    for x, y in ((140, 290), (420, 290), (150, 360), (410, 360), (175, 430), (385, 430), (240, 465), (320, 465), (280, 235)):
        f.line([(x - 10, y + 8), (x - 2, y - 8)], 3.5, color=(206, 190, 162), amp=0.1, smooth=False)
        f.line([(x + 4, y + 8), (x + 12, y - 8)], 3.5, color=(206, 190, 162), amp=0.1, smooth=False)
    f.save("paw")


def fig_fur_layers():
    """Cross-section: black skin, soft curly underfur, long guard hairs with air between them."""
    f = Fig(900, 520)
    xs = list(range(70, 860, 56))
    for i, x in enumerate(xs):
        lean = 26 * math.sin(i * 1.7)
        f.shape(tube([(x, 400), (x + lean * 0.5, 250), (x + lean, 70 + 25 * (i % 3))], 7, 2.5), BEAR, 4, closed_spline=False)
    for k, (x, y) in enumerate(((120, 160), (210, 230), (330, 140), (400, 260), (520, 190), (610, 280), (700, 150), (790, 240), (260, 310), (560, 320))):
        f.ellipse(x, y, 11, 11, HAIRC, 3)
    top = [(x, 336 + 6 * math.sin(x / 18)) for x in range(40, 861, 20)]
    f.shape(top + [(860, 405), (40, 405)], BEAR, 5, closed_spline=False)
    for x in range(58, 850, 26):
        y = 372 + 10 * ((x // 26) % 2)
        f.line([(x, y + 8), (x + 6, y - 6), (x + 14, y + 2), (x + 10, y + 12)], 3.5, amp=0.2)
    f.shape([(40, 405), (860, 405), (860, 460), (40, 460)], SKINK, 6, closed_spline=False)
    f.save("fur_layers")


def fig_sun_hair():
    """Sun light on one transparent, hollow hair; dark skin below soaks up the heat."""
    f = Fig(900, 560)
    f.ellipse(120, 110, 66, 66, EYE, 6)
    for k in range(8):
        a = k * math.pi / 4
        f.line([(120 + 82 * math.cos(a), 110 + 82 * math.sin(a)), (120 + 106 * math.cos(a), 110 + 106 * math.sin(a))], 5, amp=0.1, smooth=False)
    c = [(300, 210), (560, 236), (860, 220)]
    f.shape(tube(c, 34, 26), HAIRC, 6, closed_spline=False)
    f.shape(tube(c, 10, 7), CORE, 3, closed_spline=False)
    for (x0, y0), (x1, y1) in (((200, 150), (420, 196)), ((185, 175), (300, 380)), ((160, 200), (210, 380))):
        f.line([(x0, y0), (x1, y1)], 5, color=RAY, amp=0.3, smooth=False)
        f.arrowhead((x1, y1), (x1 - x0, y1 - y0), 18, 5, RAY)
    for x in (420, 560, 700):
        f.line([(x, 330), (x + 8, 350), (x, 370), (x + 8, 392)], 6, color=RED, amp=0.2)
        f.arrowhead((x + 8, 396), (0, 1), 16, 6, RED)
    f.shape([(30, 430), (870, 425), (870, 520), (30, 525)], SKINK, 6, closed_spline=False)
    f.save("sun_hair")


def fig_fat_layers():
    """Cross-section: fur, black skin, thick fat, body; red heat arrows turn back at the fat."""
    f = Fig(720, 560)
    f.shape([(30, 60), (650, 60), (650, 135), (30, 135)], BEAR, 5, closed_spline=False)
    for x in range(48, 640, 30):
        f.line([(x, 132), (x + 6, 90), (x + 14, 46 + 10 * ((x // 30) % 3))], 3.5, amp=0.2)
    f.shape([(30, 135), (650, 135), (650, 168), (30, 168)], SKINK, 5, closed_spline=False)
    f.shape([(30, 168), (650, 168), (650, 360), (30, 360)], FAT, 6, closed_spline=False)
    for x, y in ((90, 210), (180, 300), (260, 220), (350, 300), (440, 215), (520, 300), (600, 230), (130, 320), (400, 330)):
        f.line([(x - 22, y), (x, y - 16), (x + 22, y), (x, y + 16), (x - 22, y)], 3, color=FATC, amp=0.2)
    f.shape([(30, 360), (650, 360), (650, 530), (30, 530)], MEAT, 6, closed_spline=False)
    for x in (110, 300, 490):
        f.line([(x, 505), (x, 400), (x + 25, 380), (x + 50, 400), (x + 50, 455)], 6, color=RED, amp=0.3)
        f.arrowhead((x + 50, 460), (0, 1), 18, 6, RED)
    f.line([(682, 172), (682, 356)], 5, amp=0.1, smooth=False)
    for y in (172, 356):
        f.line([(668, y), (696, y)], 5, amp=0.1, smooth=False)
    f.save("fat_layers")


# ---------------------------------------------------------------- winter child & jacket
def fig_kid():
    f = Fig(520, 720)
    # arms behind the jacket edge, mittens
    for sx in (-1, 1):
        f.shape(tube([(260 + sx * 95, 345), (260 + sx * 160, 470), (260 + sx * 130, 540)], 30, 26), COAT, 6, closed_spline=False)
        f.ellipse(260 + sx * 128, 556, 30, 26, RED, 6)
    # legs and boots
    for sx in (-1, 1):
        f.shape(tube([(260 + sx * 45, 550), (260 + sx * 48, 645)], 24, 22), (120, 112, 104), 6, closed_spline=False)
        f.ellipse(260 + sx * 56, 666, 44, 22, BOOT, 6)
    # puffy jacket
    f.shape([(160, 320), (360, 320), (385, 560), (135, 560)], COAT, 6, closed_spline=False)
    for y in (400, 480):
        f.line([(150, y), (260, y + 10), (372, y)], 4, color=COAT2, amp=0.3)
    f.line([(260, 330), (260, 555)], 4, color=COAT2, amp=0.2, smooth=False)
    # head
    f.ellipse(260, 205, 92, 88, FACE, 6)
    for x in (226, 294):
        f.blot(x, 214, 7, 8, INK)
    for x in (204, 316):
        f.blot(x, 244, 16, 10, CHEEK)
    f.ellipse(260, 262, 10, 8, (200, 90, 80), 3)
    # knitted hat with pompom
    f.shape([(162, 186), (176, 112), (260, 82), (344, 112), (358, 186), (260, 172)], RED, 6)
    f.ellipse(260, 76, 26, 24, (246, 238, 218), 5)
    # scarf over the neck, one end hanging down
    f.shape([(170, 284), (260, 300), (350, 284), (356, 326), (260, 340), (164, 326)], SCARF, 6)
    f.shape(tube([(306, 322), (318, 380), (316, 430)], 20, 18), SCARF, 6, closed_spline=False)
    f.save("kid")


def fig_jacket():
    f = Fig(380, 400)
    for sx in (-1, 1):
        f.shape(tube([(190 + sx * 80, 80), (190 + sx * 140, 220), (190 + sx * 150, 330)], 30, 26), COAT, 6, closed_spline=False)
    f.shape([(110, 60), (165, 48), (190, 70), (215, 48), (270, 60), (290, 360), (90, 360)], COAT, 6, closed_spline=False)
    for y in (140, 220, 300):
        f.line([(100, y), (190, y + 10), (282, y)], 4, color=COAT2, amp=0.3)
    f.line([(190, 72), (190, 356)], 4, color=COAT2, amp=0.2, smooth=False)
    f.save("jacket")


ALL = {"kid": fig_kid, "jacket": fig_jacket, "bear_side": fig_bear_side, "fur_layers": fig_fur_layers, "sun_hair": fig_sun_hair,
       "fat_layers": fig_fat_layers, "bear_head": fig_bear_head, "paw": fig_paw, "bear_swim": fig_bear_swim,
       "bear_hunt": fig_bear_hunt, "bear_snow": fig_bear_snow, "ice_melt": fig_ice_melt}

if __name__ == "__main__":
    import sys
    for k in (sys.argv[1:] or ALL):
        ALL[k]()
