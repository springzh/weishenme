"""本系列的共用角色和道具：各期 src/figures.py 里 `from characters import *` 就能用。

规矩（story.py catalog / harvest 会检查）：
- 这里只放画图函数和配色常量，不放 @figure（插图属于某一期，放这里会被每一期都画一遍）
- 每个角色或道具加 @sample(...)，catalog.png 里才看得见；配套的部位函数 <名字>_parts 放 character_parts.py
- 改了函数会影响用到它的每一期：改造型时加参数（默认值保持原样），不要改已有参数的默认效果
- 改完运行 story.py catalog 重新生成 catalog.md / catalog.png
"""
import math
from figkit import *


# ---------------------------------------------------------------- 猩猩（05 期）
# 暖棕毛色（各通道满足“非冷、最亮通道 ≥125”，不会被当墨线）
APE_FUR = (156, 126, 100)
APE_FACE = (236, 212, 182)
APE_BELLY = (198, 170, 142)


@sample(happy={}, angry=dict(mood="angry"), sad_shoulder=dict(mood="sad", arm="shoulder"), waving=dict(arm="up"),
        spoon=dict(arm="spoon"), orangutan=dict(fur=(200, 146, 88)), gorilla=dict(fur=(146, 130, 122)))
def ape(f, cx, cy, s=1.0, mood="happy", arm="down", fur=None):
    """Front-view cartoon ape; local frame ~640×620: head top ≈ cy-280s, feet ≈ cy+334s.
    mood: happy (smile) / angry (slanted brows + frown) / sad (droopy brows + downturned mouth).
    arm: down (both hang) / up (canvas-right arm raised, waving) /
         spoon (canvas-right arm bent up, hand by the mouth — caller draws the spoon) /
         shoulder (canvas-left arm reaches sideways onto a neighbour drawn earlier)."""
    fur = fur or APE_FUR
    face = APE_FACE
    fur2 = tuple(int(c * 0.92) for c in fur)
    g = lambda pts: T(pts, cx, cy, s)
    if arm == "shoulder":   # reaching arm drawn first so the body covers its shoulder joint
        f.shape(g(tube([(-92, -70), (-190, -100), (-256, -122)], 26, 18)), fur, 6, smooth=False)
        f.ellipse(*g([(-268, -126)])[0], 24 * s, 21 * s, face, 5)
        f.shape(g(tube([(92, -70), (150, 60), (146, 178)], 26, 20)), fur, 6, smooth=False)
        f.ellipse(*g([(150, 194)])[0], 24 * s, 21 * s, face, 5)
    elif arm == "up":
        f.shape(g(tube([(-92, -70), (-150, 60), (-146, 178)], 26, 20)), fur, 6, smooth=False)
        f.ellipse(*g([(-150, 194)])[0], 24 * s, 21 * s, face, 5)
        f.shape(g(tube([(92, -78), (168, -150), (196, -206)], 26, 19)), fur, 6, smooth=False)
        f.ellipse(*g([(200, -218)])[0], 24 * s, 21 * s, face, 5)
    elif arm == "spoon":
        f.shape(g(tube([(-92, -70), (-150, 60), (-146, 178)], 26, 20)), fur, 6, smooth=False)
        f.ellipse(*g([(-150, 194)])[0], 24 * s, 21 * s, face, 5)
        f.shape(g(tube([(92, -74), (162, -30), (128, -66)], 25, 19)), fur, 6, smooth=False)
        f.ellipse(*g([(122, -80)])[0], 22 * s, 19 * s, face, 5)
    else:
        for sx in (-1, 1):
            f.shape(g(tube([(sx * 92, -70), (sx * 152, 60), (sx * 148, 178)], 26, 20)), fur, 6, smooth=False)
            f.ellipse(*g([(sx * 152, 194)])[0], 24 * s, 21 * s, face, 5)
    for sx in (-1, 1):   # short legs, long feet
        f.shape(g(tube([(sx * 46, 140), (sx * 56, 282)], 30, 26)), fur, 6, smooth=False)
        f.ellipse(*g([(sx * 64, 316)])[0], 42 * s, 18 * s, fur2, 5)
    f.shape(g([(-95, -95), (0, -112), (95, -95), (118, 40), (92, 155), (0, 172), (-92, 155), (-118, 40)]), fur, 6)
    f.ellipse(*g([(0, 46)])[0], 64 * s, 76 * s, APE_BELLY, 5)
    for sx in (-1, 1):   # ears behind the head
        f.ellipse(*g([(sx * 92, -214)])[0], 30 * s, 30 * s, fur2, 5)
    f.ellipse(*g([(0, -192)])[0], 96 * s, 88 * s, fur, 6)
    f.ellipse(*g([(0, -166)])[0], 62 * s, 50 * s, face, 5)
    if mood == "sad":
        for sx in (-1, 1):
            f.blot(*g([(sx * 28, -204)])[0], 7 * s + 1, 8 * s + 1)
            f.line(g([(sx * 44, -230), (sx * 12, -222)]), 5, amp=0.1, smooth=False)
        f.line(g([(-22, -136), (0, -146), (22, -136)]), 5, amp=0.2)
    elif mood == "angry":
        for sx in (-1, 1):
            f.blot(*g([(sx * 28, -206)])[0], 7 * s + 1, 8 * s + 1)
            f.line(g([(sx * 12, -232), (sx * 44, -222)]), 6, amp=0.1, smooth=False)
        f.line(g([(-20, -136), (0, -146), (20, -136)]), 5, amp=0.2)
    else:
        for sx in (-1, 1):
            f.blot(*g([(sx * 28, -208)])[0], 7 * s + 1, 9 * s + 1)
            f.line(g([(sx * 14, -232), (sx * 42, -228)]), 5, amp=0.1, smooth=False)
        f.line(g([(-26, -142), (0, -126), (26, -142)]), 5, amp=0.2)


@sample(knuckle_sitting={})
def ape_side(f, cx, cy, s=1.0, fur=None):
    """Side view chimp sitting knuckle-handed, facing right; (cx, cy) = ground under the hips.
    Chimp signatures: protruding muzzle past the head edge, big round ear at the back-top,
    brow over the eye, hunched rounded back, long front arm (far hand knuckles on the ground).
    Local frame (s=1): head top ≈ -296 (tuft to -314), reaching hand ≈ (190, -30) holds the stick."""
    fur = fur or APE_FUR
    face = APE_FACE
    fur2 = tuple(int(c * 0.92) for c in fur)
    g = lambda pts: T(pts, cx, cy, s)
    f.shape(g(tube([(20, -125), (95, -62), (135, -12)], 26, 20)), fur2, 5, smooth=False)  # far arm → knuckles
    f.ellipse(*g([(142, -8)])[0], 22 * s, 10 * s, fur2, 4)
    f.shape(g([(-118, -12), (-124, -98), (-72, -170), (0, -200), (70, -195), (110, -160), (112, -90), (95, -45), (55, -4), (-25, 4)]), fur, 6)
    f.shape(g([(62, -175), (92, -200), (125, -180), (135, -125), (100, -108), (68, -128)]), fur, 6)   # neck/shoulder fills the throat gap
    for x0, y0, x1, y1 in ((-70, -160, -60, -178), (-20, -176, -10, -194)):
        f.line(g([(x0, y0), (x1, y1)]), 4, amp=0.2, smooth=False)                          # shaggy back strokes
    f.shape(g(tube([(15, -35), (50, -48), (68, -20)], 26, 20)), fur, 5, smooth=False)      # folded knee
    f.ellipse(*g([(82, -8)])[0], 26 * s, 10 * s, fur, 4)                                   # foot
    f.shape(g(tube([(60, -150), (140, -95), (185, -40)], 28, 19)), fur, 6, smooth=False)   # reaching arm
    f.ellipse(*g([(190, -30)])[0], 18 * s, 15 * s, face, 5)                                # hand holding the stick
    f.ellipse(*g([(50, -250)])[0], 32 * s, 32 * s, fur2, 5)                                # big round ear (behind head)
    f.shape(g([(52, -262), (88, -292), (138, -296), (172, -268), (178, -228), (156, -196), (108, -186), (68, -206), (50, -236)]), fur, 6)
    f.ellipse(*g([(132, -252)])[0], 17 * s, 14 * s, face, 4)                               # eye patch
    f.ellipse(*g([(148, -212)])[0], 38 * s, 28 * s, face, 5)                               # protruding muzzle
    f.blot(*g([(136, -252)])[0], 7 * s + 1, 8 * s + 1)                                     # eye
    f.line(g([(122, -270), (150, -266)]), 5, amp=0.1, smooth=False)                        # brow
    f.blot(*g([(170, -224)])[0], 3.5 * s + 1, 4 * s + 1)                                   # nostril
    f.line(g([(152, -198), (168, -192), (178, -196)]), 4, amp=0.2)                         # mouth
    f.line(g([(100, -296), (96, -312)]), 4, amp=0.2, smooth=False)                         # fur tuft
    f.line(g([(116, -298), (116, -314)]), 4, amp=0.2, smooth=False)


@sample(default=dict(s=4.0))
def ant(f, x, y, s=1.0):
    """A tiny ant: two body blobs + two legs, warm accent colour."""
    f.blot(x, y, 5 * s, 4 * s, C.accent)
    f.blot(x + 7 * s, y - 2 * s, 3.4 * s, 3 * s, C.accent)
    f.line([(x - 4 * s, y + 3 * s), (x - 8 * s, y + 6 * s)], 2.5, color=C.accent, amp=0.1, smooth=False)
    f.line([(x + 3 * s, y + 3 * s), (x + 6 * s, y + 7 * s)], 2.5, color=C.accent, amp=0.1, smooth=False)


# ---------------------------------------------------------------- 狼、鹿（04 期）
WOLF = (196, 178, 150)
DEER = (196, 142, 96)
ANTLER = (228, 208, 172)


@sample(standing={}, howling=dict(head_rot=-0.6), pup=dict(s=0.5, fur=(218, 204, 180)))
def wolf(f, cx, cy, s=1.0, head_rot=0.0, fur=WOLF, crouch=0.0):
    """The episode's wolf: lean body, long legs, pointed ears, bushy tail hanging down."""
    quadruped(f, cx, cy, s, head_rot=head_rot, crouch=crouch, fur=fur, ear="pointed", tail="down", snout=1.08, body="slim", leg=45)


@sample(standing={}, grazing=dict(head_rot=1.05))
def deer(f, cx, cy, s=1.0, head_rot=0.0):
    """The deer (elk): slim body, long legs, branched antlers. head_rot ≈ 1.05 lowers the head to graze."""
    quadruped(f, cx, cy, s, head_rot=head_rot, fur=DEER, ear="pointed", tail="stub", snout=0.92, body="slim", leg=60, antlers=ANTLER)


# ---------------------------------------------------------------- 袋鼠（06 期）
# 橙棕毛色（不偏冷，最亮通道 198），育儿袋用浅色肚皮
KANGAROO = (198, 132, 78)
KANGAROO_DARK = (168, 108, 62)
KANGAROO_BELLY = (238, 206, 164)
JOEY_FUR = (222, 172, 138)
JOEY_PINK = (238, 162, 148)


@sample(standing={}, joey_peek=dict(joey=True), leap=dict(pose="leap"))
def kangaroo(f, cx, cy, s=1.0, pose="stand", joey=False, fur=None, head_rot=0.0):
    """Side-view red kangaroo facing right; (cx, cy) = ground under the feet (pose="stand") or the
    ground line under an airborne animal (pose="leap"). Local frame (s=1, stand): ear tips ≈ cy-640,
    feet on cy, tail tip ≈ cx-350. Pouch opening runs from (52,-350) to (124,-344).
    joey=True: a baby head peeking out of the pouch."""
    fur = fur or KANGAROO
    fur2 = tuple(int(c * 0.92) for c in fur)
    if pose == "leap":
        _kangaroo_leap(f, cx, cy, s, fur, fur2, joey)
        return
    g = lambda pts: T(pts, cx, cy, s)
    # far arm (behind the body)
    f.shape(g(tube([(100, -444), (128, -398), (120, -370)], 17, 13)), fur2, 5, smooth=False)
    f.ellipse(*g([(118, -362)])[0], 15 * s, 12 * s, fur2, 4)
    # tail: thick at the hip, resting on the ground
    f.shape(g(tube([(-58, -276), (-170, -204), (-272, -104), (-350, -28)], 38, 15)), fur, 6, smooth=False)
    # far hind leg
    f.shape(g(tube([(-6, -306), (74, -224), (96, -72)], 36, 22)), fur2, 5, smooth=False)
    f.ellipse(*g([(34, -22)])[0], 76 * s, 15 * s, fur2, 4)
    # body (pear shape, leaning forward)
    f.shape(g([(-74, -270), (-64, -382), (-8, -452), (52, -492), (108, -474), (132, -402),
               (138, -320), (124, -250), (92, -205), (20, -188), (-32, -204)]), fur, 6)
    # near arm, held against the chest (behind the pouch)
    f.shape(g(tube([(122, -452), (166, -400), (156, -362)], 17, 13)), fur, 5, smooth=False)
    f.ellipse(*g([(154, -354)])[0], 15 * s, 12 * s, fur, 4)
    # pouch pocket on the belly
    f.shape(g([(96, -352), (112, -374), (140, -368), (150, -336), (150, -296),
               (136, -272), (108, -272), (94, -310)]), KANGAROO_BELLY, 5)
    if joey:
        x, y = g([(118, -376)])[0]
        f.ellipse(x - 24 * s, y - 38 * s, 11 * s, 20 * s, fur2, 5, rot=0.5)      # far ear
        f.ellipse(x + 24 * s, y - 40 * s, 11 * s, 20 * s, fur, 5, rot=-0.5)      # near ear
        f.ellipse(x, y - 14 * s, 29 * s, 26 * s, JOEY_FUR, 5)                    # head
        f.ellipse(x + 8 * s, y - 2 * s, 19 * s, 13 * s, KANGAROO_BELLY, 4)       # muzzle
        for dx in (-13, 1):
            f.blot(x + dx * s, y - 22 * s, 4 * s + 1, 5 * s + 1)
        f.blot(x + 20 * s, y, 5 * s, 4 * s)
    # pouch lip (covers the joey's chest)
    f.line(g([(94, -350), (118, -338), (146, -344)]), 5, amp=0.2)
    # near hind leg: thigh, shin, long foot
    f.shape(g([(4, -322), (64, -336), (132, -286), (166, -214), (148, -182), (78, -198), (16, -250)]), fur, 6)
    f.shape(g(tube([(150, -240), (132, -24)], 34, 24)), fur, 6, smooth=False)
    f.ellipse(*g([(112, -18)])[0], 95 * s, 18 * s, fur, 5)
    for tx in (58, 88, 120, 152):
        f.line(g([(tx, -30), (tx + 8, -10)]), 3.5, amp=0.1, smooth=False)          # toes
    # neck fills the shoulder gap, then head: far ear, skull, near ear, muzzle, face
    f.shape(g(tube([(84, -470), (128, -502)], 46, 40)), fur, 0, smooth=False)   # fill only: no collar line
    f.shape(g(tube([(164, -556), (178, -612), (186, -646)], 22, 12)), fur2, 5, smooth=False)   # far ear
    f.shape(g([(88, -500), (100, -548), (140, -570), (184, -556), (222, -528), (260, -494),
               (280, -468), (272, -446), (248, -436), (212, -440), (176, -454), (140, -470), (110, -482)]), fur, 6)
    f.shape(g(tube([(120, -552), (104, -608), (94, -650)], 26, 13)), fur, 5, smooth=False)      # near ear
    f.ellipse(*g([(240, -468)])[0], 32 * s, 22 * s, KANGAROO_BELLY, 4)            # muzzle
    f.blot(*g([(188, -518)])[0], 7 * s + 1, 8 * s + 1)                            # eye
    f.blot(*g([(270, -460)])[0], 8 * s, 6 * s)                                    # nose
    f.line(g([(262, -442), (246, -440)]), 4, amp=0.2, smooth=False)               # mouth
    f.line(g([(168, -540), (200, -534)]), 4, amp=0.1, smooth=False)               # brow


def _kangaroo_leap(f, cx, cy, s, fur, fur2, joey=False):
    """Airborne kangaroo: body stretched forward, hind legs trailing, tail straight back."""
    g = lambda pts: T(pts, cx, cy, s)
    f.shape(g(tube([(-120, -332), (-250, -320), (-372, -290)], 28, 13)), fur, 6, smooth=False)   # tail
    f.shape(g(tube([(-60, -300), (-160, -270), (-250, -230)], 26, 15)), fur2, 5, smooth=False)   # far leg
    f.ellipse(*g([(-272, -222)])[0], 54 * s, 12 * s, fur2, 4, rot=-0.35)                          # far foot
    f.shape(g(tube([(-20, -290), (-130, -256), (-220, -214)], 30, 17)), fur, 5, smooth=False)     # near leg
    f.ellipse(*g([(-244, -206)])[0], 58 * s, 13 * s, fur, 4, rot=-0.4)                            # near foot
    f.shape(g([(-152, -338), (-120, -396), (-40, -420), (60, -424), (142, -402), (174, -360),
               (164, -300), (92, -268), (0, -266), (-96, -286)]), fur, 6)                         # body
    f.ellipse(*g([(84, -304)])[0], 36 * s, 28 * s, KANGAROO_BELLY, 0)                             # belly
    if joey:                                                                                     # baby tucked in
        x, y = g([(112, -300)])[0]
        f.ellipse(x - 17 * s, y - 30 * s, 8 * s, 15 * s, fur2, 4, rot=0.5)
        f.ellipse(x + 17 * s, y - 32 * s, 8 * s, 15 * s, fur, 4, rot=-0.5)
        f.ellipse(x, y - 10 * s, 21 * s, 19 * s, JOEY_FUR, 4)
        f.ellipse(x + 6 * s, y - 2 * s, 14 * s, 10 * s, KANGAROO_BELLY, 3)
        for dx in (-10, 2):
            f.blot(x + dx * s, y - 15 * s, 3 * s + 1, 4 * s + 1)
        f.line(g([(86, -280), (112, -270), (138, -280)]), 4, amp=0.2)                            # pouch lip
    f.shape(g(tube([(120, -382), (160, -348), (146, -320)], 16, 12)), fur2, 5, smooth=False)      # far arm
    f.ellipse(*g([(144, -312)])[0], 14 * s, 11 * s, fur2, 4)
    f.shape(g(tube([(136, -394), (176, -360), (162, -332)], 16, 12)), fur, 5, smooth=False)       # near arm
    f.ellipse(*g([(160, -324)])[0], 14 * s, 11 * s, fur, 4)
    f.shape(g(tube([(150, -440), (160, -486), (164, -510)], 20, 11)), fur2, 5, smooth=False)      # far ear
    f.shape(g(tube([(150, -380), (190, -420)], 42, 36)), fur, 0, smooth=False)                     # neck (fill only)
    f.shape(g([(150, -410), (162, -452), (198, -470), (238, -456), (274, -430), (306, -404),
               (314, -380), (298, -364), (264, -366), (228, -378), (192, -390), (162, -400)]), fur, 6)  # head
    f.shape(g(tube([(142, -436), (130, -480), (124, -504)], 22, 12)), fur, 5, smooth=False)       # near ear
    f.ellipse(*g([(290, -390)])[0], 28 * s, 20 * s, KANGAROO_BELLY, 4)                            # muzzle
    f.blot(*g([(240, -430)])[0], 7 * s + 1, 8 * s + 1)                                            # eye
    f.blot(*g([(310, -386)])[0], 8 * s, 6 * s)                                                    # nose


@sample(default={}, bigger=dict(s=1.5))
def joey_bean(f, cx, cy, s=1.0, color=None):
    """Newborn joey about the size of a jellybean: pink bean-shaped body, closed eye, two front claws,
    a curled tail. (cx, cy) = centre of the bean body."""
    color = color or JOEY_PINK
    g = lambda pts: T(pts, cx, cy, s)
    f.shape(g([(-46, -6), (-40, -34), (-14, -48), (16, -46), (44, -30), (50, -2),
               (38, 26), (8, 38), (-24, 32), (-44, 16)]), color, 5)
    f.ellipse(*g([(30, -18)])[0], 24 * s, 20 * s, tuple(min(255, c + 14) for c in color), 4)   # head end
    f.line(g([(30, -26), (38, -28)]), 3, amp=0.1, smooth=False)                                # closed eye
    f.blot(*g([(52, -16)])[0], 4 * s, 3 * s)                                                   # tiny nose
    for dx in (-6, 6):                                                                          # front claws
        f.shape(g([(dx, 20), (dx - 4, 36), (dx + 5, 36), (dx + 7, 20)]), color, 3, smooth=False)
    f.line(g([(-44, 10), (-62, 6), (-74, 14)]), 4, amp=0.2)                                    # curled tail


# ---------------------------------------------------------------- 道具（03/06 期）
FINGER_SKIN = (250, 224, 196)   # 与 sun-desert 的 C.skin 同色；kit 角色固定用色，不随本期配色变
NAIL = (250, 232, 214)


@sample(default={}, longer=dict(s=1.3))
def finger(f, cx, cy, s=1.0, skin=None):
    """A pointing index finger, tip down; the rounded palm above it. (cx, cy) = the fingertip.
    Local frame (s=1): palm top ≈ cy-512, palm half-width ≈116, finger half-width 37."""
    skin = skin or FINGER_SKIN
    g = lambda pts: T(pts, cx, cy, s)
    w = 37 * s                                                             # finger half-width
    f.shape(g([(-104, -484), (-66, -512), (66, -512), (104, -484),
               (116, -398), (104, -324), (-104, -324), (-116, -398)]), skin, 6)
    f.shape(g([(-w, -366), (w, -366), (w, -44), (w - 18, -8), (0, 0),
               (-w + 18, -8), (-w, -44)]), skin, 6, smooth=False)
    f.shape(g([(-w + 12, -62), (w - 12, -62), (w - 16, -30), (0, -18), (-w + 16, -30)]), NAIL, 4, smooth=False)
    f.line(g([(-w + 8, -228), (w - 8, -222)]), 4, amp=0.2)                 # knuckle crease
    f.line(g([(-104, -324), (-w + 6, -324)]), 5, amp=0.3, smooth=False)    # palm–finger folds
    f.line(g([(104, -324), (w - 6, -324)]), 5, amp=0.3, smooth=False)
    f.line(g([(-108, -414), (-112, -384)]), 4, amp=0.2, smooth=False)      # knuckle creases at the edge
    f.line(g([(110, -410), (112, -380)]), 4, amp=0.2, smooth=False)


@sample(zoo=lambda f, x, y: fence(f, x - 320, x + 320, y - 280, y))
def fence(f, x0, x1, y0, y1, step=60):
    """Zoo enclosure: two rails and vertical bars (all ink strokes)."""
    for y in (y0 + 10, (y0 + y1) / 2):
        f.line([(x0, y), (x1, y)], 5, amp=0.6, smooth=False)
    for x in range(int(x0) + 20, int(x1), step):
        f.line([(x, y0), (x, y1)], 5, amp=0.4, smooth=False)
