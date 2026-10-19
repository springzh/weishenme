"""为什么不把狼都消灭光 — what each figure shows, its parts, and the narration it must make visible (references/drawing.md)."""
from partkit import *
from figkit import stand


def wolf_parts(name, cx, cy, s, head_rot=0.0, prefix="", subject="wolf"):
    return quadruped_parts(name, cx, cy, s, head_rot=head_rot, leg=45, tail="down", subject=subject, prefix=prefix)


def deer_parts(name, cx, cy, s, head_rot=0.0, prefix="", subject="deer"):
    return quadruped_parts(name, cx, cy, s, head_rot=head_rot, leg=60, antlers=True, subject=subject, prefix=prefix)


def ground_part(name="ground", what="地面外框一笔"):
    return P(name, "ground", "ground", [what], FULL)


SPECS = {
 "storybook": dict(
    composition="一本打开的故事书：左页是太阳、一棵树和地面，右页画着一只灰黄色的狼——故事里的“大灰狼”。",
    why="书的两页外框、左页的太阳/树/地面、右页的狼（头、身体、腿）；每个形状独立一笔。",
    subjects=[("wolf", A), ("book", O)],
    parts=wolf_parts("storybook", 650, stand(450, 0.42, leg=45), 0.42)
          + [P("book_left", "book", "left_page", ["左页外框一笔", "太阳一圈", "树干一笔", "树冠一笔", "地面一笔"], box("storybook", 0, 0, 452, 600)),
             P("book_right", "book", "right_page", ["右页外框一笔", "地面一笔"], FULL)],
    reqs=[R("bad", "在故事里，大灰狼总是坏蛋", "打开的故事书里画着一只狼")],
    exception="先画右页的狼（头→身体→腿），再画左页，书页外框最后"),
 "kid": dict(
    composition="正面站立的小朋友（棕色短发、不戴帽子），好奇地看着前方。",
    why="人物拆为头、颈、躯干、左右臂、下半身六部分，各部分外形独立一笔。",
    subjects=[("kid", H)],
    parts=kid_parts("kid", 260, 360),
    reqs=[R("ask", "真把狼都消灭光，会发生什么呢", "一个好奇提问的小朋友")]),
 "wolf_dog": dict(
    composition="左边一只灰黄色的狼：耳朵尖尖竖着、尾巴蓬松向下垂；右边一只浅棕色的狗：耳朵耷拉、尾巴高高向上卷。两只都侧身朝右站在地面上。",
    why="狼（头、身体含垂尾、腿）、狗（头含耷拉耳、身体含卷尾、腿）、地面；每个形状独立一笔。",
    subjects=[("wolf", A), ("dog", A), ("ground", E)],
    parts=wolf_parts("wolf_dog", 360, stand(475, 0.78, leg=45), 0.78, prefix="wolf_")
          + quadruped_parts("wolf_dog", 960, stand(475, 0.72, leg=30), 0.72, leg=30, tail="curl", subject="dog", prefix="dog_") + [ground_part()],
    reqs=[R("ears", "它的耳朵总是尖尖地竖着，尾巴总是向下垂", "狼的耳朵竖着、尾巴向下垂"),
          R("dog", "很多狗的尾巴，却是高高地向上卷着", "旁边的狗尾巴向上卷着")],
    exception="先画左边的狼，再画右边的狗，地面最后"),
 "pack": dict(
    composition="一家子狼站在地面上：两只大狼（爸爸妈妈）在左边，两只小狼崽（颜色浅一些、个子小）在右边。",
    why="四只狼各分头、身体、腿三部分，地面一笔。",
    subjects=[("wolf_dad", A), ("wolf_mom", A), ("pup1", A), ("pup2", A), ("ground", E)],
    parts=wolf_parts("pack", 230, stand(445, 0.6, leg=45), 0.6, prefix="dad_", subject="wolf_dad")
          + wolf_parts("pack", 660, stand(445, 0.6, leg=45), 0.6, 0.12, prefix="mom_", subject="wolf_mom")
          + wolf_parts("pack", 1000, stand(445, 0.36, leg=45), 0.36, prefix="pup1_", subject="pup1")
          + wolf_parts("pack", 1180, stand(445, 0.34, leg=45), 0.34, -0.15, prefix="pup2_", subject="pup2") + [ground_part()],
    reqs=[R("family", "狼爸爸、狼妈妈带着孩子", "两只大狼和两只小狼崽在一起")],
    exception="从左到右：狼爸爸、狼妈妈、两只小狼，地面最后"),
 "howl": dict(
    composition="一只狼仰起头、嘴朝天嚎叫，嘴前三道红色声音弧线；右上一轮月亮。",
    why="月亮、狼（头、身体、腿）、声音弧线、地面；弧线是彩色细线，归到地面背景部位。",
    subjects=[("moon", E), ("wolf", A), ("ground", E)],
    parts=[P("moon", "moon", "moon", ["月亮一圈"], circle("howl", 110, 100, 66))]
          + wolf_parts("howl", 360, stand(505, 0.8, leg=45), 0.8, -0.6) + [ground_part("ground", "地面外框一笔；三道声音弧线")],
    reqs=[R("howl", "它们嗷呜嗷呜地嚎叫", "狼仰头张嘴嚎叫，嘴前有声音弧线")],
    exception="先画月亮，再画狼（头→身体→腿），地面和声音弧线最后"),
 "eat": dict(
    composition="一排狼的食物，站在地面上：带鹿角的鹿、坐着的野兔、小田鼠、一只羊。",
    why="鹿（头含鹿角、身体、腿）、野兔、田鼠、羊（头、身体、腿）、地面；每个形状独立一笔。",
    subjects=[("deer", A), ("hare", A), ("mouse", A), ("sheep", A), ("ground", E)],
    parts=deer_parts("eat", 230, stand(405, 0.55, leg=60), 0.55, 0.1, prefix="deer_")
          + [P("hare_ears", "hare", "ears_head", ["两只长耳朵", "头部一圈", "眼睛鼻子"], box("eat", 520, 190, 620, 340)),
             P("hare_body", "hare", "body", ["身体一笔", "短尾巴一圈", "后脚一圈"], box("eat", 480, 330, 620, 412)),
             P("mouse_head", "mouse", "head", ["头一圈", "眼睛鼻子"], box("eat", 800, 330, 880, 400)),
             P("mouse_body", "mouse", "body", ["尾巴一笔", "身体一笔"], box("eat", 660, 330, 800, 412))]
          + [P("sheep_head", "sheep", "head", ["耷拉耳", "头部外形一笔", "头顶卷毛一圈", "眼睛鼻子"], box("eat", 1120, 270, 1210, 410)),
             P("sheep_body", "sheep", "torso", ["四条腿", "卷毛身体一圈", "短尾巴"], box("eat", 920, 270, 1120, 412)), ground_part()],
    reqs=[R("menu", "常吃鹿、野兔和田鼠，有时也会偷吃农民家的羊", "鹿、野兔、田鼠和羊排成一排")],
    exception="从左到右：鹿、野兔、田鼠、羊，地面最后"),
 "gone": dict(
    composition="没有狼的黄石河边：三只带鹿角的鹿低着头啃食，河岸上只剩一排被啃断的小树桩，没有鸟，下方是浅蓝色的河。",
    why="三只鹿（头、身体、腿）、六个树桩、河岸地面、河水；每个形状独立一笔。",
    subjects=[("deer1", A), ("deer2", A), ("deer3", A), ("bank", E)],
    parts=deer_parts("gone", 260, stand(372, 0.48, leg=60), 0.48, 1.05, prefix="d1_", subject="deer1")
          + deer_parts("gone", 680, stand(372, 0.5, leg=60), 0.5, 1.05, prefix="d2_", subject="deer2")
          + deer_parts("gone", 1060, stand(372, 0.48, leg=60), 0.48, 1.05, prefix="d3_", subject="deer3")
          + [P("bank", "bank", "river_bank", ["河岸地面外框一笔", "六个被啃断的树桩（在鹿嘴边的岸上）", "河水外形一笔", "水波纹"], FULL)],
    reqs=[R("eaten", "天天在河边啃小树苗，小树长不起来了", "鹿群低头啃食，河岸上只剩被啃断的树桩"),
          R("empty", "河边没有了树，鸟儿少了", "河边没有树，也没有鸟")],
    reqs_short=[R("eaten", "把河边的小树苗都啃光了", "鹿群低头啃食，河岸上只剩被啃断的树桩")],
    exception="先画三只鹿（从左到右），河岸、树桩和河水最后"),
 "back": dict(
    composition="狼回来后的同一段河边：左边山坡上一只狼，河岸长出三棵大树和两棵小树苗，树上停着小鸟、天上飞着两只鸟，河边一只河狸，远处一只鹿。",
    why="狼、鹿（头、身体、腿）、河狸、小鸟、树、河岸与河水；每个形状独立一笔。",
    subjects=[("wolf", A), ("deer", A), ("beaver", A), ("birds", E), ("trees", E)],
    parts=wolf_parts("back", 175, stand(372, 0.42, leg=45), 0.42)
          + deer_parts("back", 1000, stand(372, 0.3, leg=60), 0.3, prefix="deer_")
          + [P("beaver_head", "beaver", "head", ["头一圈", "眼睛鼻子", "门牙"], box("back", 300, 380, 370, 440)),
             P("beaver_body", "beaver", "torso", ["扁尾巴一笔", "身体一笔"], box("back", 190, 400, 370, 505)),
             P("birds", "birds", "birds", ["两只停着的小鸟", "两只飞鸟各一笔"], box("back", 760, 40, 960, 140)),
             P("trees", "trees", "trees_bank_water", ["三棵树（树干、树冠）", "两棵树苗", "树上两只小鸟", "河岸地面", "河水"], FULL)],
    reqs=[R("wolf", "后来，人们又把狼请回了黄石公园", "河边的山坡上有一只狼"),
          R("green", "小树重新长了起来，鸟儿和河狸也回来了", "河岸长满了树，有小鸟和河狸")],
    reqs_short=[R("green", "小树又长了起来", "河岸长满了树，有小鸟和河狸，狼回来了")],
    exception="先画左边的狼，再画右边远处的鹿、河狸、天上的飞鸟，树、河岸和河水最后"),
 "chain": dict(
    composition="三格食物链：左边一只狼，箭头指向中间带鹿角的鹿，再一个箭头指向右边的一棵树。",
    why="狼（头、身体、腿）、鹿（头、身体、腿）、两支箭头、树和地面；每个形状独立一笔。",
    subjects=[("wolf", A), ("deer", A), ("tree", E)],
    parts=wolf_parts("chain", 200, stand(385, 0.42, leg=45), 0.42) + deer_parts("chain", 650, stand(385, 0.38, leg=60), 0.38, prefix="deer_")
          + [P("tree", "tree", "tree_arrows_ground", ["两支箭头", "树干一笔", "树冠一笔", "地面一笔"], FULL)],
    reqs=[R("chain", "狼吃鹿，鹿吃树", "狼 → 鹿 → 树 三格，用箭头连起来")],
    reqs_short=[R("chain", "狼吃鹿，鹿吃树", "狼 → 鹿 → 树 三格，用箭头连起来")],
    exception="从左到右：狼、鹿，箭头、树和地面最后"),
 "protect": dict(
    composition="一面金色的盾牌，中间站着一只狼，左右上角各一个红色闪光——“保护动物”的标志。",
    why="盾牌外形、狼（头、身体、腿）、两个闪光；每个形状独立一笔。",
    subjects=[("wolf", A), ("shield", O)],
    parts=wolf_parts("protect", 300, stand(390, 0.38, leg=45), 0.38) + [P("shield", "shield", "shield", ["盾牌外形一笔", "两个闪光"], FULL)],
    reqs=[R("protect", "狼是我国的保护动物", "盾牌里护着一只狼")],
    exception="先画盾牌里的狼，再画盾牌外形和闪光"),
 "safe": dict(
    composition="左边远处一只狼，右边一个小朋友站着，脚下一支红色箭头指向右边——慢慢退开。",
    why="狼（头、身体、腿）、小朋友六部分、箭头和地面；每个形状独立一笔。",
    subjects=[("wolf", A), ("kid", H), ("ground", E)],
    parts=wolf_parts("safe", 240, stand(525, 0.42, leg=45), 0.42, prefix="wolf_") + kid_parts("safe", 900, 300, 0.62) + [ground_part("ground", "地面外框一笔；红色箭头")],
    reqs=[R("away", "慢慢退开", "小朋友远离狼，脚下有向远处的箭头")],
    exception="先画左边的狼，再画小朋友（头→下半身），地面和箭头最后"),
 "wolf_tree": dict(
    composition="一只灰黄色的狼站在一棵大树旁边，树上停着一只小鸟，地上有几丛草。（封面主图、结尾）",
    why="狼（头、身体、腿）、树（树干、树冠）、小鸟、草和地面；每个形状独立一笔。",
    subjects=[("wolf", A), ("tree", E)],
    parts=wolf_parts("wolf_tree", 245, stand(475, 0.62, leg=45), 0.62) + [P("tree", "tree", "tree_bird_ground", ["树干一笔", "树冠一笔", "小鸟", "草丛", "地面一笔"], FULL)],
    reqs=[R("place", "大自然里的每一种动物，都有自己的位置", "狼和树、小鸟同在一个画面里")],
    exception="先画狼，再画树、小鸟和地面"),
 "fox_hare": dict(
    composition="左边一只橙色的狐狸，蓬松的大尾巴；右边一只坐着的野兔。",
    why="狐狸（头、身体含大尾巴、腿）、野兔（耳朵和头、身体）、地面；每个形状独立一笔。",
    subjects=[("fox", A), ("hare", A), ("ground", E)],
    parts=quadruped_parts("fox_hare", 330, stand(385, 0.42, leg=20), 0.42, leg=20, tail="bushy", subject="fox", prefix="fox_")
          + [P("hare_head", "hare", "ears_head", ["两只长耳朵", "头部一圈", "眼睛鼻子"], box("fox_hare", 660, 180, 760, 330)),
             P("hare_body", "hare", "body", ["身体一笔", "短尾巴一圈", "后脚一圈"], box("fox_hare", 620, 300, 760, 400)), ground_part()],
    reqs=[R("q", "没了狐狸，野兔会变多还是变少", "一只狐狸和一只野兔")],
    reqs_short=[R("q", "没了狐狸，野兔会变多还是变少", "一只狐狸和一只野兔")],
    exception="先画左边的狐狸，再画右边的野兔，地面最后"),
 "sanlian": dict(
    composition="一排三个小图标：粉色爱心（点赞）、金色硬币（投币）、金色五角星（收藏）。（结尾“一键三连”）",
    why="三个独立的简单形状，各一笔外框；硬币内圈一笔。",
    subjects=[("icons", O)],
    parts=[P("heart", "icons", "like_heart", ["爱心外形一笔"], rect(0, 0, 0.33, 1)),
           P("coin", "icons", "coin", ["硬币外圈一笔", "内圈一笔"], rect(0.33, 0, 0.66, 1)),
           P("star", "icons", "favourite_star", ["五角星外形一笔"], FULL)],
    reqs=[R("sanlian", "记得一键三连哦", "爱心、硬币、星星三个图标排成一排")],
    exception="从左到右：爱心、硬币、星星"),
}
