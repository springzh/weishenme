"""为什么不把狼都消灭光 — every illustration of the episode (palette: forest)."""
from figkit import *

WOLF = (196, 178, 150)
PUP = (218, 204, 180)
DOG = (232, 196, 140)
DEER = (196, 142, 96)
ANTLER = (228, 208, 172)
FOX = (232, 146, 78)
HARE = (206, 182, 150)
SHEEP = (238, 234, 222)
PAGE = (250, 246, 236)
SHIELD = (242, 214, 120)


def wolf(f, cx, cy, s=1.0, head_rot=0.0, fur=WOLF, crouch=0.0):
    """The episode's wolf: lean body, long legs, pointed ears, bushy tail hanging down."""
    quadruped(f, cx, cy, s, head_rot=head_rot, crouch=crouch, fur=fur, ear="pointed", tail="down", snout=1.08, body="slim", leg=45)


def deer(f, cx, cy, s=1.0, head_rot=0.0):
    quadruped(f, cx, cy, s, head_rot=head_rot, fur=DEER, ear="pointed", tail="stub", snout=0.92, body="slim", leg=60, antlers=ANTLER)


@figure("storybook", 900, 600)
def storybook(f):
    f.shape([(60, 130), (450, 100), (450, 530), (70, 550)], PAGE, 6, smooth=False)
    f.shape([(450, 100), (840, 130), (830, 550), (450, 530)], PAGE, 6, smooth=False)
    f.ellipse(170, 230, 40, 40, C.sun, 5)
    tree(f, 300, 470, 260)
    ground(f, 100, 420, 470, 510)
    wolf(f, 650, stand(450, 0.42, leg=45), 0.42)
    ground(f, 480, 800, 445, 510)


@figure("kid", 520, 720)
def kid_curious(f):
    kid(f, 260, 360, mood="curious", hat=False, scarf=False)


@figure("wolf_dog", 1300, 560)
def wolf_dog(f):
    ground(f, 20, 1280, 470, 545)
    wolf(f, 360, stand(475, 0.78, leg=45), 0.78)
    quadruped(f, 960, stand(475, 0.72, leg=30), 0.72, fur=DOG, ear="floppy", tail="curl", snout=0.9, body="slim", leg=30)


@figure("pack", 1340, 520)
def pack(f):
    ground(f, 20, 1320, 440, 505)
    wolf(f, 230, stand(445, 0.6, leg=45), 0.6)
    wolf(f, 660, stand(445, 0.6, leg=45), 0.6, head_rot=0.12)
    wolf(f, 1000, stand(445, 0.36, leg=45), 0.36, fur=PUP)
    wolf(f, 1180, stand(445, 0.34, leg=45), 0.34, fur=PUP, head_rot=-0.15)


@figure("howl", 820, 600)
def howl(f):
    f.ellipse(110, 100, 52, 52, C.sun, 5)
    ground(f, 20, 800, 500, 585)
    cy = stand(505, 0.8, leg=45)
    wolf(f, 360, cy, 0.8, head_rot=-0.6)
    nx, ny = T(rot_about([(384 * 1.08, -56)], QUAD_PIVOT, -0.6), 360, cy, 0.8)[0]
    for k, r in enumerate((40, 75, 110)):
        a0, a1 = -1.35, -0.25
        f.line([(nx + 20 + r * math.cos(t), ny + 10 + r * math.sin(t)) for t in np.linspace(a0, a1, 7)], 5, color=C.accent, amp=0.1)


@figure("eat", 1300, 480)
def eat(f):
    ground(f, 20, 1280, 400, 465)
    deer(f, 230, stand(405, 0.55, leg=60), 0.55, head_rot=0.1)
    hare(f, 560, 405, 0.95, fur=HARE)
    mouse(f, 790, 405, 1.2)
    sheep(f, 1080, stand(405, 0.5, leg=10), 0.5)


def river_scene(f):
    ground(f, 20, 1280, 360, 470)
    water(f, 20, 1280, 470, 585)


@figure("gone", 1300, 600)
def gone(f):
    river_scene(f)
    for cx, s in ((260, 0.48), (680, 0.5), (1060, 0.48)):
        deer(f, cx, stand(372, s, leg=60), s, head_rot=1.05)
    for x in (120, 470, 560, 880, 960, 1240):
        stump(f, x, 380)


@figure("back", 1300, 600)
def back(f):
    river_scene(f)
    for x in (430, 740, 1180):
        tree(f, x, 470, 300)
    sapling(f, 600, 470, 120); sapling(f, 950, 470, 110)
    wolf(f, 175, stand(372, 0.42, leg=45), 0.42)
    deer(f, 1000, stand(372, 0.3, leg=60), 0.3)
    beaver(f, 300, 488, 0.8)
    bird(f, 470, 210, 0.9)
    bird(f, 1150, 205, 0.9, color=C.sun)
    bird(f, 820, 110, 1.2, flying=True); bird(f, 900, 70, 1.0, flying=True)


@figure("chain", 1300, 440)
def chain(f):
    ground(f, 20, 1280, 380, 425)
    wolf(f, 200, stand(385, 0.42, leg=45), 0.42)
    deer(f, 650, stand(385, 0.38, leg=60), 0.38)
    tree(f, 1100, 385, 300)
    arrow(f, [(400, 260), (500, 260)], width=6, head=20)
    arrow(f, [(850, 260), (950, 260)], width=6, head=20)


@figure("protect", 620, 620)
def protect(f):
    f.shape([(310, 40), (540, 110), (520, 360), (310, 570), (100, 360), (80, 110)], SHIELD, 7)
    wolf(f, 300, stand(390, 0.38, leg=45), 0.38)
    for x, y in ((180, 150), (440, 150)):
        sparkle(f, x, y, 18, color=C.accent, width=5)


@figure("safe", 1240, 600)
def safe(f):
    ground(f, 20, 1220, 520, 585)
    wolf(f, 240, stand(525, 0.42, leg=45), 0.42)
    kid(f, 900, 300, 0.62, mood="curious", hat=False, scarf=False)
    arrow(f, [(1000, 560), (1170, 560)], color=C.accent, width=6, head=22)


@figure("wolf_tree", 760, 560)
def wolf_tree(f):
    ground(f, 20, 740, 470, 545)
    tree(f, 600, 475, 400)
    bird(f, 660, 120, 0.8)
    wolf(f, 245, stand(475, 0.62, leg=45), 0.62)
    for x in (60, 120, 470, 700):
        grass(f, x, 480, n=3, h=34, color=C.leaf)


@figure("fox_hare", 900, 440)
def fox_hare(f):
    ground(f, 20, 880, 380, 425)
    quadruped(f, 330, stand(385, 0.42, leg=20), 0.42, fur=FOX, ear="pointed", tail="bushy", snout=1.0, body="slim", leg=20)
    hare(f, 700, 385, 1.0, fur=HARE)


@figure("sanlian", 440, 140)
def sanlian_icons(f):
    sanlian(f, 220, 72, gap=135, r=46)
