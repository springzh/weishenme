"""为什么狮、虎、豹在白天老睡觉 — every illustration of the episode (palette: sun-desert)."""
from figkit import *
from characters import *        # 系列素材库 kit/：fence……（kit/catalog.md）

LION = (232, 190, 120)
MANE = (196, 122, 66)
TIGER = (240, 160, 80)
LEOPARD = (238, 206, 142)
SPOT = (196, 146, 84)
CAT = (240, 176, 110)
NIGHT_GROUND = (128, 112, 118)
GOLD = (240, 196, 80)
EYEBALL = (248, 242, 228)
CUSHION = (240, 168, 168)


@figure("kid", 520, 720)
def kid_curious(f):
    kid(f, 260, 360, mood="curious", hat=False, scarf=False)


@figure("zoo_sleep", 1300, 560)
def zoo_sleep(f):
    fence(f, 30, 1270, 50, 330)
    ground(f, 20, 1280, 330, 540, fill=C.sand)
    lying(f, 225, 486, 0.82, fur=LION, mane=MANE, tail_tip=MANE)
    lying(f, 650, 486, 0.82, fur=TIGER, pattern="stripes", pattern_color=C.ink)
    lying(f, 1070, 486, 0.82, fur=LEOPARD, pattern="spots", pattern_color=SPOT)


@figure("day_rest", 900, 600)
def day_rest(f):
    ground(f, 20, 880, 460, 585, fill=C.sand)
    tree(f, 300, 470, 420, crown=C.leaf, trunk=C.wood)
    f.blot(330, 492, 250, 26, C.shade)
    lying(f, 320, 488, 0.74, fur=TIGER, pattern="stripes", pattern_color=C.ink)
    sun(f, 770, 110, 55)
    for x in (640, 720, 800):
        wavy_arrow(f, x, 210, 300, color=C.heat)


@figure("night_hunt", 900, 600)
def night_hunt(f):
    f.shape([(20, 20), (880, 20), (880, 580), (20, 580)], C.night, 6, smooth=False)
    f.shape([(20, 470), (300, 455), (600, 468), (880, 450), (880, 580), (20, 580)], NIGHT_GROUND, 0, smooth=False)
    f.ellipse(120, 110, 48, 48, C.sun, 5)
    f.blot(146, 96, 44, 44, C.night)
    for x, y in ((280, 70), (420, 120), (560, 60), (840, 90), (250, 190), (700, 50)):
        sparkle(f, x, y, 12, color=C.sun, width=4)
    quadruped(f, 420, 290, s=0.95, fur=LION, mane=MANE, tail="long", head="round", eye_glow=GOLD)


@figure("eye_mirror", 900, 560)
def eye_mirror(f):
    f.ellipse(95, 95, 46, 46, C.sun, 5)
    f.blot(118, 80, 40, 40, (255, 255, 255))
    f.ellipse(560, 285, 210, 210, EYEBALL, 7)
    ring_out = [(560 + 205 * math.cos(t), 285 + 205 * math.sin(t)) for t in np.linspace(-1.0, 1.0, 20)]
    ring_in = [(560 + 172 * math.cos(t), 285 + 172 * math.sin(t)) for t in np.linspace(1.0, -1.0, 20)]
    f.shape(ring_out + ring_in, GOLD, 5, smooth=False)
    f.ellipse(372, 285, 30, 78, C.glass, 5)
    arrow(f, [(40, 250), (372, 268), (725, 250)], color=C.ray, width=6, head=22)
    arrow(f, [(725, 262), (372, 304), (60, 340)], color=C.heat, width=6, head=22)
    sparkle(f, 742, 256, 20, color=C.ray, width=5)


@figure("heat", 820, 560)
def heat(f):
    ground(f, 20, 800, 450, 545, fill=C.sand)
    sun(f, 300, 180, 95)
    for x in (180, 300, 420):
        wavy_arrow(f, x, 320, 430, color=C.heat)
    thermometer(f, 640, 120, 460, 0.9)


@figure("ambush", 760, 420)
def ambush(f):
    ground(f, 20, 740, 330, 410, fill=C.sand)
    quadruped(f, 330, 230, s=0.8, fur=LEOPARD, pattern="spots", pattern_color=SPOT, crouch=1.2, head_rot=0.12, tail="long", head="round")
    for x in range(60, 720, 34):
        grass(f, x, 345, n=3, h=70 + 30 * ((x // 34) % 3), color=C.leaf)


@figure("pounce", 1000, 560)
def pounce(f):
    ground(f, 20, 980, 470, 545, fill=C.sand)
    quadruped(f, 520, 235, s=0.88, fur=LEOPARD, pattern="spots", pattern_color=SPOT, rot=-0.18, stride=1.0, tail="long", head="round")
    motion_lines(f, 170, 300, n=4, length=110, gap=26, angle=-0.18)


@figure("charge", 900, 520)
def charge(f):
    ground(f, 20, 880, 430, 505, fill=C.sand)
    lying(f, 400, 455, 0.95, fur=LEOPARD, pattern="spots", pattern_color=SPOT)
    f.shape([(560, 60), (800, 60), (800, 170), (560, 170)], (250, 246, 236), 6, smooth=False)
    f.shape([(800, 92), (826, 92), (826, 138), (800, 138)], (250, 246, 236), 5, smooth=False)
    for k in range(4):
        x = 578 + k * 54
        f.shape([(x, 78), (x + 42, 78), (x + 42, 152), (x, 152)], C.leaf, 4, smooth=False)


@figure("walk_lion", 900, 560)
def walk_lion(f):
    fence(f, 30, 870, 40, 300)
    ground(f, 20, 880, 300, 545, fill=C.sand)
    quadruped(f, 420, 330, s=0.95, fur=LION, mane=MANE, tail="long", head="round")


@figure("cat", 560, 380)
def cat(f):
    f.ellipse(280, 310, 250, 48, CUSHION, 6)
    lying(f, 250, 300, 0.9, fur=CAT, pattern="stripes", pattern_color=(210, 130, 70), ear="pointed")


@figure("lion_sleep", 760, 420)
def lion_sleep(f):
    ground(f, 20, 740, 330, 405, fill=C.sand)
    lying(f, 360, 352, 1.25, fur=LION, mane=MANE, tail_tip=MANE)


@figure("sanlian", 440, 140)
def sanlian_icons(f):
    sanlian(f, 220, 72, gap=135, r=46)
