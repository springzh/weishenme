"""为什么说猩猩最聪明 — every illustration of the episode (palette: forest)."""
import math
from figkit import *
from characters import *        # 系列素材库 kit/：ape、ape_side、ant……（kit/catalog.md）


@figure("kin", 1000, 680)
def kin(f):
    """Ape and a child standing side by side on the grass, the ape waving."""
    ground(f, 30, 970, 560, 660, fill=C.grass)
    for x in (120, 480, 860):
        grass(f, x, 560, n=3, h=24)
    kid(f, 320, 280, 0.85, mood="happy", hat=False, scarf=False)
    ape(f, 690, 276, 0.85, mood="happy", arm="up")


@figure("brain_cells", 1100, 620)
def brain_cells(f):
    """A big brain on the left; a magnifier on the right full of neuron dots."""
    f.shape(tube([(250, 455), (232, 515)], 26, 16), C.flesh, 5, smooth=False)            # brainstem
    f.ellipse(205, 420, 74, 50, C.flesh, 5)                                              # cerebellum (behind)
    blob = [(120, 300), (140, 190), (230, 130), (330, 118), (430, 158), (492, 240), (482, 352), (400, 432), (280, 452), (178, 410)]
    f.shape(blob, C.flesh, 6)
    f.line([(165, 300), (245, 262), (330, 300), (410, 262)], 5, amp=0.5)
    f.line([(190, 370), (270, 336), (355, 378), (430, 344)], 5, amp=0.5)
    f.line([(230, 200), (305, 172), (380, 208)], 5, amp=0.4)
    for x, y in ((215, 240), (300, 340), (390, 300), (255, 400), (350, 220), (430, 390)):
        f.blot(x, y, 8, 8, C.accent)
    arrow(f, [(505, 300), (625, 300)], color=C.accent, width=6, head=20)
    f.ellipse(800, 300, 138, 138, C.glass, 0)                                            # lens glass
    for x, y, r in ((740, 240, 12), (800, 220, 9), (860, 250, 13), (730, 310, 10), (800, 300, 14),
                    (870, 330, 10), (760, 370, 12), (830, 390, 9), (880, 210, 8), (715, 265, 7),
                    (835, 300, 8), (770, 330, 7), (700, 350, 7), (855, 375, 7)):
        f.blot(x, y, r, r, C.accent)
    for x, y in ((765, 255), (840, 275), (795, 350)):
        f.line([(x - 8, y + 6), (x + 8, y - 6)], 3, amp=0.1, smooth=False)
    magnifier(f, 800, 300, 150)


@figure("ant_fish", 1000, 430)
def ant_fish(f):
    """Ape squatting on the grass, holding a thin stick into an ant mound; ants climb the stick."""
    G = 332                                    # ground line: leaves 270px headroom for the ape
    ground(f, 40, 960, G + 2, 415, fill=C.grass)
    for x in (100, 430, 700, 890):
        grass(f, x, G, n=3, h=22)
    ape_side(f, 300, G, 1.0)
    f.shape([(535, G + 2), (557, G - 44), (595, G - 64), (640, G - 44), (672, G + 2)], C.ground, 6)   # ant mound
    f.line([(488, G - 36), (525, G - 42), (582, G - 52)], 8, amp=0.3)                                 # stick (ink, into the hole)
    f.line([(568, G - 56), (583, G - 50), (598, G - 56)], 5, amp=0.1, smooth=False)                   # hole at the stick tip
    ant(f, 505, G - 38, 1.1)
    ant(f, 530, G - 42, 1.0)
    ant(f, 560, G - 48, 1.0)
    ant(f, 622, G - 34, 0.9)


@figure("faces", 1000, 360)
def faces(f):
    """Three round ape faces: happy, angry, sad — labels come from the text layer."""
    for cx, mood in ((170, "happy"), (500, "angry"), (830, "sad")):
        f.ellipse(cx, 175, 96, 92, C.skin, 6)
        f.ellipse(cx, 200, 60, 48, APE_FACE, 5)
        for sx in (-1, 1):
            f.blot(cx + sx * 28, 162, 7, 9)
            f.blot(cx + sx * 58, 205, 15, 9, C.cheek)
        if mood == "happy":
            for sx in (-1, 1): f.line([(cx + sx * 14, 128), (cx + sx * 42, 124)], 5, amp=0.1, smooth=False)
            f.line([(cx - 26, 192), (cx, 212), (cx + 26, 192)], 5, amp=0.2)
        elif mood == "angry":
            for sx in (-1, 1): f.line([(cx + sx * 12, 144), (cx + sx * 44, 126)], 6, amp=0.1, smooth=False)
            f.line([(cx - 22, 204), (cx, 190), (cx + 22, 204)], 6, amp=0.2)
        else:
            for sx in (-1, 1): f.line([(cx + sx * 12, 128), (cx + sx * 44, 140)], 5, amp=0.1, smooth=False)
            f.line([(cx - 22, 196), (cx, 208), (cx + 22, 196)], 5, amp=0.2)


@figure("console", 1000, 640)
def console(f):
    """One angry ape (steam above the head); a friend lays a hand on its shoulder."""
    ground(f, 30, 970, 566, 630, fill=C.grass)
    wavy_arrow(f, 340, 66, 14, color=C.heat, width=5)
    wavy_arrow(f, 396, 60, 10, color=C.heat, width=5)
    ape(f, 400, 306, 0.8, mood="angry", arm="down")
    ape(f, 690, 306, 0.8, mood="sad", arm="shoulder")


@figure("learn_eat", 1000, 560)
def learn_eat(f):
    """Ape at a table learning to eat with a spoon; a bowl of rice on the table."""
    ape(f, 330, 232, 0.72, mood="happy", arm="spoon")
    f.line([(432, 160), (420, 136)], 7, color=C.metal, amp=0.2)                          # spoon shaft
    f.ellipse(415, 124, 13, 18, C.metal, 4, rot=-0.5)                                    # spoon bowl
    f.shape([(150, 380), (850, 380), (850, 548), (150, 548)], C.wood, 6, smooth=False)   # table
    f.ellipse(650, 376, 88, 26, C.glass, 5)                                              # bowl
    for x, y in ((610, 360), (650, 352), (690, 360), (630, 368), (668, 366)):
        f.blot(x, y, 9, 7, C.honey)
    f.line([(722, 336), (694, 358)], 6, color=C.metal, amp=0.2, smooth=False)            # spoon resting in the bowl
    f.ellipse(688, 362, 11, 15, C.metal, 3, rot=-0.9)


@figure("four_apes", 1240, 680)
def four_apes(f):
    """Four great apes side by side: orangutan, chimpanzee, bonobo, gorilla (labels from the text layer)."""
    ground(f, 30, 1210, 580, 660, fill=C.grass)
    for x in (140, 560, 900, 1150):
        grass(f, x, 580, n=3, h=22)
    ape(f, 200, 580 - 334 * 0.78, 0.78, fur=(200, 146, 88))                    # 黄猩猩
    ape(f, 500, 580 - 334 * 0.74, 0.74, fur=APE_FUR)                           # 黑猩猩
    ape(f, 780, 580 - 334 * 0.70, 0.70, fur=(168, 138, 114))                   # 侏黑猩猩
    ape(f, 1060, 580 - 334 * 0.90, 0.90, fur=(146, 130, 122))                  # 大猩猩


@figure("fossil", 1000, 580)
def fossil(f):
    """Hillside cross-section with a cave; a fossil skull by the cave mouth; shovel and brush."""
    layers(f, 40, 960, [(280, 560, C.ground)])
    for x in (80, 180, 820, 900):
        grass(f, x, 282, n=3, h=24)
    f.shape([(430, 560), (430, 440), (480, 388), (570, 388), (620, 440), (620, 560)], C.shade, 6, smooth=False)
    f.ellipse(525, 470, 46, 42, (240, 228, 205), 5)                                      # skull
    f.shape([(496, 500), (554, 500), (550, 528), (500, 528)], (240, 228, 205), 5, smooth=False)  # jaw
    f.ellipse(540, 458, 13, 14, (240, 228, 205), 4)                                      # eye socket
    f.line([(498, 500), (552, 500)], 4, amp=0.1, smooth=False)
    for x in (505, 517, 529, 541):
        f.line([(x, 500), (x, 510)], 3, amp=0.05, smooth=False)                          # teeth
    f.shape(tube([(820, 140), (812, 400)], 10, 8), C.wood, 5, smooth=False)              # shovel handle
    f.shape([(786, 400), (842, 400), (836, 492), (814, 508), (792, 492)], C.metal, 5, smooth=False)
    f.shape(tube([(180, 330), (238, 400)], 9, 7), C.metal, 5, smooth=False)              # brush
    f.shape([(222, 392), (262, 428), (240, 448), (204, 412)], C.wood, 5, smooth=False)
    sparkle(f, 640, 410, 20)


@figure("friend", 900, 680)
def friend(f):
    """The ape waving with a heart overhead — a friend worth protecting."""
    ground(f, 40, 860, 560, 660, fill=C.grass)
    ape(f, 430, 560 - 334 * 0.85, 0.85, mood="happy", arm="up")
    heart(f, 660, 180, 58)
    sparkle(f, 250, 210, 18)


@figure("sanlian", 430, 170)
def sanlian_icons(f):
    sanlian(f, 215, 80, gap=130, r=44)
