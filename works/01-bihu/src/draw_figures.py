"""Code-drawn cartoon figures for the gecko explainer (十万个为什么).

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
SKIN = (207, 220, 138)      # gecko yellow-green
SPOT = (169, 184, 92)
BELLY = (244, 231, 168)
EYE = (250, 210, 92)
GREY = (210, 206, 200)
WING = (238, 236, 230)
WALL = (242, 201, 160)
WALL2 = (230, 180, 136)
WALL_INK = (120, 92, 66)
DARK_RED = (122, 40, 30)
RED = (224, 106, 78)
CUP = (232, 120, 96)
TAPE = (246, 214, 130)
METAL = (222, 214, 196)
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


# ---------------------------------------------------------------- gecko (top view, facing up)
def foot(f, wrist, ang, s, rot, cx, cy, spread=1.0):
    """Five splayed toes with round toe pads, starting at wrist (local coords)."""
    for k in range(5):
        a = ang + (k - 2) * 0.42 * spread
        L = 34 if k in (1, 2, 3) else 28
        tip = (wrist[0] + L * math.cos(a), wrist[1] + L * math.sin(a))
        f.shape(T(tube([wrist, ((wrist[0] + tip[0]) / 2, (wrist[1] + tip[1]) / 2), tip], 5.5, 5), cx, cy, s, rot), SKIN, 4.5, closed_spline=False)
        px, py = T([tip], cx, cy, s, rot)[0]
        f.ellipse(px, py, 10 * s, 8 * s, SKIN, 4.5, rot=a + rot)


def leg(f, pts, wrist_ang, s, rot, cx, cy):
    f.shape(T(tube(pts, 15, 10), cx, cy, s, rot), SKIN, 6, closed_spline=False)
    foot(f, pts[-1], wrist_ang, s, rot, cx, cy)


def gecko_top(f, cx, cy, s=1.0, rot=0.0, mouth_open=False, tail_curl=1.0):
    t = lambda pts: T(pts, cx, cy, s, rot)
    # tail first (under body)
    tail_c = [(0, 90), (8 * tail_curl, 190), (40 * tail_curl, 270), (20 * tail_curl, 340), (-30 * tail_curl, 360), (-55 * tail_curl, 330)]
    f.shape(t(tube(tail_c, 30, 4)), SKIN, 6, closed_spline=False)
    # legs (under body)
    leg(f, [(-40, -95), (-95, -110), (-120, -160)], -math.pi / 2 - 0.5, s, rot, cx, cy)
    leg(f, [(40, -95), (95, -110), (120, -160)], -math.pi / 2 + 0.5, s, rot, cx, cy)
    leg(f, [(-42, 60), (-105, 70), (-125, 125)], math.pi / 2 + 0.6, s, rot, cx, cy)
    leg(f, [(42, 60), (105, 70), (125, 125)], math.pi / 2 - 0.6, s, rot, cx, cy)
    # body
    body = [(0, -150), (40, -130), (55, -60), (55, 20), (40, 90), (0, 115), (-40, 90), (-55, 20), (-55, -60), (-40, -130)]
    f.shape(t(body), SKIN, 6)
    for (x, y, r) in [(-18, -80, 9), (20, -40, 8), (-15, 5, 10), (18, 50, 8), (-10, 85, 7), (10, 150, 7), (15, 230, 6)]:
        px, py = t([(x, y)])[0]
        f.blot(px, py, r * s, r * s * 0.8, SPOT)
    # head
    head = [(0, -280), (35, -268), (58, -225), (55, -175), (30, -145), (0, -138), (-30, -145), (-55, -175), (-58, -225), (-35, -268)]
    f.shape(t(head), SKIN, 6)
    if mouth_open:
        pass
    else:
        f.line(t([(-30, -262), (0, -255), (30, -262)]), 4.5)
    # eyes bulging at the sides
    for sx in (-1, 1):
        ex, ey = t([(sx * 50, -222)])[0]
        f.ellipse(ex, ey, 21 * s, 21 * s, EYE, 5)
        f.blot(ex, ey, 4.5 * s, 14 * s, INK, rot=rot)
        hx, hy = t([(sx * 50 - 7, -230)])[0]
        f.blot(hx, hy, 4 * s, 4 * s, (255, 255, 255))


def fig_gecko_wait():
    f = Fig(800, 980)
    # wall corner: two light lines meeting (environment)
    f.line([(40, 40), (40, 940)], 5, color=WALL_INK, amp=1.2)
    f.line([(40, 940), (760, 940)], 5, color=WALL_INK, amp=1.2)
    gecko_top(f, 420, 450, s=1.05, rot=0.3)
    f.save("gecko_wait")


def mosquito(f, cx, cy, s=1.0, rot=0.0):
    t = lambda pts: T(pts, cx, cy, s, rot)
    # legs
    for sx in (-1, 1):
        for k, (ax, ay) in enumerate([(10, -10), (12, 5), (10, 20)]):
            f.line(t([(sx * ax, ay), (sx * (ax + 40), ay + 10 + k * 8), (sx * (ax + 60), ay + 45 + k * 10)]), 4)
    # wings
    for sx in (-1, 1):
        f.shape(t([(sx * 8, -12), (sx * 70, -60), (sx * 95, -40), (sx * 60, -5), (sx * 10, 0)]), WING, 5)
    # abdomen (full of blood -> red)
    f.shape(t([(0, 10), (16, 30), (18, 75), (0, 105), (-18, 75), (-16, 30)]), RED, 5)
    f.ellipse(*t([(0, -5)])[0], 15 * s, 15 * s, GREY, 5)
    f.ellipse(*t([(0, -32)])[0], 11 * s, 11 * s, GREY, 5)
    f.line(t([(0, -42), (0, -85)]), 4)  # proboscis
    for sx in (-1, 1):
        f.line(t([(sx * 5, -40), (sx * 22, -70)]), 3.5)


def fig_mosquito():
    f = Fig(380, 360)
    mosquito(f, 190, 185, s=1.35)
    f.save("mosquito")


def fig_gecko_catch():
    f = Fig(1000, 700)
    # speed lines behind the gecko (lower-left)
    for i, (x0, y0) in enumerate([(70, 520), (110, 600), (60, 440), (150, 650)]):
        f.line([(x0, y0), (x0 + 120, y0 - 70)], 5, color=WALL_INK, amp=0.6)
    gecko_top(f, 520, 380, s=1.0, rot=0.95, tail_curl=-0.6)
    # mosquito caught at the snout: wings/legs sticking out of the mouth
    mosquito(f, 812, 222, s=0.72, rot=0.95 + math.pi)
    f.save("gecko_catch")


# ---------------------------------------------------------------- science figures
def fig_suction():
    f = Fig(420, 420)
    # suction cup hook: dome + rim + hook
    f.shape([(80, 300), (120, 200), (210, 160), (300, 200), (340, 300)], CUP, 6)
    f.shape([(60, 300), (360, 300), (370, 330), (50, 330)], CUP, 6, closed_spline=False, amp=0.8)
    f.line([(210, 160), (210, 100), (230, 70), (265, 75), (270, 110)], 9)
    f.save("suction")


def fig_foot():
    """Big gecko foot (underside) with lamellae across each toe pad."""
    f = Fig(820, 760)
    cx, cy = 410, 600
    palm = [(cx - 110, cy - 40), (cx - 60, cy - 110), (cx, cy - 125), (cx + 60, cy - 110), (cx + 110, cy - 40), (cx + 70, cy + 40), (cx, cy + 60), (cx - 70, cy + 40)]
    # arm going down out of frame
    f.shape([(cx - 70, cy + 30), (cx + 70, cy + 30), (cx + 60, 760), (cx - 60, 760)], SKIN, 6, closed_spline=False, amp=1.0)
    toes = []
    for k in range(5):
        a = -math.pi / 2 + (k - 2) * 0.48
        base = (cx + 70 * math.cos(a), cy - 40 + 70 * math.sin(a))
        L = 300 if k in (1, 2, 3) else 240
        tip = (cx + (70 + L) * math.cos(a), cy - 40 + (70 + L) * math.sin(a))
        toes.append((a, base, tip, L))
    for a, base, tip, L in toes:
        ux, uy = math.cos(a), math.sin(a)
        nx, ny = -uy, ux
        w0, w1 = 20, 52  # slim toes widen into broad pads
        pts = [(base[0] + nx * w0, base[1] + ny * w0),
               (base[0] + ux * L * .3 + nx * w0 * 1.1, base[1] + uy * L * .3 + ny * w0 * 1.1),
               (base[0] + ux * L * .6 + nx * w1, base[1] + uy * L * .6 + ny * w1),
               (tip[0] - ux * 20 + nx * w1 * .9, tip[1] - uy * 20 + ny * w1 * .9),
               (tip[0] + ux * 18, tip[1] + uy * 18),
               (tip[0] - ux * 20 - nx * w1 * .9, tip[1] - uy * 20 - ny * w1 * .9),
               (base[0] + ux * L * .6 - nx * w1, base[1] + uy * L * .6 - ny * w1),
               (base[0] + ux * L * .3 - nx * w0 * 1.1, base[1] + uy * L * .3 - ny * w0 * 1.1),
               (base[0] - nx * w0, base[1] - ny * w0)]
        f.shape(pts, BELLY, 6)
        cl = (tip[0] + ux * 18, tip[1] + uy * 18)
        f.line([cl, (cl[0] + ux * 22 - nx * 8, cl[1] + uy * 22 - ny * 8)], 5)  # tiny claw
    f.shape(palm, BELLY, 6)
    # lamellae: curved ridges across each toe pad (drawn after all outlines exist in image)
    for a, base, tip, L in toes:
        ux, uy = math.cos(a), math.sin(a)
        nx, ny = -uy, ux
        for j in range(6):
            d = L * (0.5 + j * 0.08)
            w = 44 if j < 5 else 36
            c = (base[0] + ux * d, base[1] + uy * d)
            f.line([(c[0] + nx * w, c[1] + ny * w), (c[0] + ux * 12, c[1] + uy * 12), (c[0] - nx * w, c[1] - ny * w)], 4.5, color=(196, 160, 96), amp=0.5)
    f.save("foot")


def fig_setae():
    """Magnified ridge: a dense brush of hairs standing on a ridge (inside a magnifier circle)."""
    f = Fig(620, 620)
    cx, cy, R = 310, 300, 250
    f.ellipse(cx, cy, R, R, (255, 255, 255), 8)
    # ridge
    f.shape([(cx - 205, cy + 120), (cx - 120, cy + 70), (cx, cy + 55), (cx + 120, cy + 70), (cx + 205, cy + 120), (cx + 170, cy + 175), (cx - 170, cy + 175)], BELLY, 6)
    # hairs: many thin curved strokes standing on the ridge
    xs = np.linspace(cx - 170, cx + 170, 19)
    for i, x in enumerate(xs):
        y0 = cy + 70 + 0.0009 * (x - cx) ** 2 * 1.1
        h = 170 + 25 * math.sin(i * 1.7)
        bend = 18 * math.sin(i * 0.9)
        f.line([(x, y0), (x + bend * .4, y0 - h * .5), (x + bend, y0 - h)], 4, color=(150, 120, 70), amp=0.5)
    # handle
    f.shape([(cx + 165, cy + 190), (cx + 190, cy + 168), (cx + 290, cy + 268), (cx + 268, cy + 292)], (196, 150, 98), 6, closed_spline=False, amp=0.6)
    f.save("setae")


def fig_spatula():
    """One seta: a stalk that branches, and branches again, ending in tiny flat pads."""
    f = Fig(640, 640)
    stalk = [(320, 620), (318, 470), (322, 330)]
    f.shape(tube(stalk, 13, 10), (232, 214, 170), 6, closed_spline=False)
    tips = []
    for i, a in enumerate(np.linspace(-1.05, 1.05, 5)):
        p1 = (322 + 120 * math.sin(a), 330 - 120 * math.cos(a))
        f.line([(322, 336), ((322 + p1[0]) / 2 + 6 * math.sin(i), (330 + p1[1]) / 2), p1], 5, color=(150, 120, 70), amp=0.4)
        for j, b in enumerate(np.linspace(-0.45, 0.45, 4)):
            q = (p1[0] + 95 * math.sin(a + b), p1[1] - 95 * math.cos(a + b))
            f.line([p1, q], 3.5, color=(150, 120, 70), amp=0.3)
            tips.append((q, a + b))
    for (qx, qy), ang in tips:
        f.ellipse(qx + 5 * math.sin(ang), qy - 5 * math.cos(ang), 10, 4.5, RED, 3, rot=ang)
    f.save("spatula")


def fig_force():
    """Tiny pads hovering just above a wall surface; small red arrows = attraction between molecules."""
    f = Fig(1000, 440)
    # wall surface at bottom (bumpy line + fill)
    top = [(30, 330), (200, 322), (380, 334), (560, 324), (740, 333), (970, 326)]
    f.shape(top + [(970, 420), (30, 420)], WALL, 6, closed_spline=False, amp=0.8)
    # wall molecules: little circles inside the wall
    for x in range(90, 960, 110):
        f.ellipse(x, 372, 14, 14, WALL2, 4)
    # pads (seta branch tips) coming from above
    for k, x in enumerate(range(110, 960, 110)):
        f.line([(x + 30, 60), (x + 14, 200), (x, 285)], 4.5, color=(150, 120, 70), amp=0.4)
        f.ellipse(x, 296, 30, 9, (232, 214, 170), 4.5)
        # attraction arrows between pad and wall
        f.line([(x + 46, 300), (x + 46, 316)], 4, color=DARK_RED, amp=0.1, smooth=False)
        f.arrowhead((x + 46, 318), (0, 1), size=9, width=4, color=DARK_RED)
    f.save("force")


def fig_ceiling():
    """Side view: gecko hanging upside-down from the ceiling."""
    f = Fig(960, 560)
    f.shape([(20, 20), (940, 20), (940, 95), (20, 95)], WALL, 6, closed_spline=False, amp=0.8)
    # tail (right) curling down
    f.shape(tube([(600, 205), (720, 215), (800, 250), (830, 320), (800, 360)], 26, 4), SKIN, 6, closed_spline=False)
    # legs reaching up to the ceiling
    for x0, x1 in ((330, 300), (390, 410), (540, 520), (600, 630)):
        f.shape(tube([(x0, 200), ((x0 + x1) / 2 + 12, 150), (x1, 110)], 13, 9), SKIN, 6, closed_spline=False)
        f.ellipse(x1, 101, 34, 9, SKIN, 5)
    # body (belly down toward viewer's floor)
    f.shape([(280, 200), (360, 165), (480, 160), (600, 175), (640, 210), (590, 250), (460, 262), (330, 248)], SKIN, 6)
    f.shape([(330, 238), (460, 250), (585, 238), (560, 252), (460, 262), (345, 252)], BELLY, 0)
    # head (left), looking down
    f.shape([(150, 250), (180, 205), (240, 185), (300, 200), (310, 245), (270, 275), (200, 280)], SKIN, 6)
    f.ellipse(245, 220, 20, 20, EYE, 5)
    f.blot(245, 220, 5, 14, INK)
    f.blot(240, 213, 4, 4, (255, 255, 255))
    f.line([(160, 255), (195, 262), (225, 258)], 4.5)
    for (x, y, r) in [(400, 195, 10), (470, 185, 9), (540, 200, 9), (700, 220, 7)]:
        f.blot(x, y, r, r * .8, SPOT)
    f.save("ceiling")


def fig_peel():
    """Side view of one toe peeling off the wall from the tip back, with a curling arrow."""
    f = Fig(1000, 500)
    f.shape([(20, 380), (980, 380), (980, 470), (20, 470)], WALL, 6, closed_spline=False, amp=0.8)
    # toe: flat on the wall at left, curling up toward the right tip
    toe_c = [(60, 330), (260, 340), (440, 335), (560, 300), (640, 220), (660, 140), (620, 90)]
    f.shape(tube(toe_c, 40, 26), SKIN, 6, closed_spline=False)
    # lamellae on the underside of the flat part
    for x in (180, 260, 340, 420):
        f.line([(x, 360), (x + 8, 378)], 4, color=(196, 160, 96), amp=0.2, smooth=False)
    # curling arrow
    arc = [(760, 330), (820, 250), (812, 160), (765, 108)]
    f.shape(tube(arc, 11, 9), RED, 5, closed_spline=False, amp=0.5)
    f.shape([(790, 120), (712, 70), (740, 152)], RED, 5, closed_spline=False, amp=0.3)
    f.save("peel")


def fig_tape():
    f = Fig(560, 460)
    # roll
    f.ellipse(200, 210, 150, 150, TAPE, 6)
    f.ellipse(200, 210, 70, 70, (255, 255, 255), 6)
    # strip coming off, with tiny footprint pattern
    f.shape([(330, 290), (540, 330), (530, 400), (300, 345)], TAPE, 6, closed_spline=False, amp=0.8)
    for x in (380, 440, 495):
        for k in range(3):
            a = -1.9 + k * 0.6
            f.line([(x, 352 + (x - 330) * .19), (x + 14 * math.cos(a), 352 + (x - 330) * .19 + 14 * math.sin(a))], 3.5, color=(196, 160, 96), amp=0.1, smooth=False)
    f.save("tape")


def fig_robot():
    """Wall-climbing robot with gecko-like pads, on a wall (front view)."""
    f = Fig(600, 600)
    cx, cy = 300, 310
    for sx in (-1, 1):
        for sy in (-1, 1):
            p0 = (cx + sx * 50, cy + sy * 60)
            p1 = (cx + sx * 150, cy + sy * 90)
            p2 = (cx + sx * 175, cy + sy * 175)
            f.shape(tube([p0, p1, p2], 13, 11), METAL, 5, closed_spline=False)
            f.ellipse(p2[0], p2[1] + sy * 12, 34, 26, RED, 5)
    f.shape([(cx - 80, cy - 120), (cx + 80, cy - 120), (cx + 95, cy + 110), (cx, cy + 150), (cx - 95, cy + 110)], METAL, 6)
    for sx in (-1, 1):
        f.ellipse(cx + sx * 34, cy - 70, 20, 20, EYE, 5)
        f.blot(cx + sx * 34, cy - 70, 7, 7, INK)
    f.line([(cx - 30, cy - 10), (cx, cy + 8), (cx + 30, cy - 10)], 5)
    f.save("robot")


ALL = {"gecko_wait": fig_gecko_wait, "mosquito": fig_mosquito, "gecko_catch": fig_gecko_catch, "suction": fig_suction,
       "foot": fig_foot, "setae": fig_setae, "spatula": fig_spatula, "force": fig_force, "ceiling": fig_ceiling,
       "peel": fig_peel, "tape": fig_tape, "robot": fig_robot}

if __name__ == "__main__":
    import sys
    for k in (sys.argv[1:] or ALL):
        ALL[k]()
