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


# ---------------------------------------------------------------- 道具（03 期）
@sample(zoo=lambda f, x, y: fence(f, x - 320, x + 320, y - 280, y))
def fence(f, x0, x1, y0, y1, step=60):
    """Zoo enclosure: two rails and vertical bars (all ink strokes)."""
    for y in (y0 + 10, (y0 + y1) / 2):
        f.line([(x0, y), (x1, y)], 5, amp=0.6, smooth=False)
    for x in range(int(x0) + 20, int(x1), step):
        f.line([(x, y0), (x, y1)], 5, amp=0.4, smooth=False)
