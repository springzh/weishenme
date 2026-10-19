"""为什么说猩猩最聪明 — full version pages (beat ids from beats.full.json)."""
from layoutkit import *

HOOK1 = "天哪！猩猩"
HOOK2 = "居然会劝架！"
PUN_A, PUN_B = "它还会自己做工具，", "钓蚂蚁吃！"
PUN_X = 960 - (text_width(PUN_A, 76) + text_width(PUN_B, 76)) / 2

# hook: the surprising fact + the second beat, big words only, no picture
HOOK_PAGE = page(G("hook", [text(HOOK1, 960, 180, 120, center=True)] + ring_word(HOOK2, 960 - text_width(HOOK2, 130) / 2, 350, 130, ACCENT), lead=.15),
                 G("hook2", [text(PUN_A, PUN_X, 660, 76), text(PUN_B, PUN_X + text_width(PUN_A, 76), 660, 76, ACCENT)]))

KIN = [title("猩猩为什么聪明？"), ill("kin", 90, 250, 900, 640)]
BRAIN = [title("秘密一：大脑特别发达"), ill("brain_cells", 90, 270, 1080, 610)]
TOOL = [title("秘密二：会做工具"), ill("ant_fish", 90, 330, 1300, 560)]
APES = [title("四种类人猿"), ill("four_apes", 60, 280, 1560, 560),
        text("黄猩猩在印尼 · 其余在非洲", 150, 170, 46, ACCENT)]

PAGES = [
 HOOK_PAGE,
 page(G("like_us_a", KIN + [text("出了名的聪明", 1030, 360, 60), text("为什么说它最聪明？", 1030, 480, 56, ACCENT)]),
      G("like_us_b", [text("和人类有", 1030, 620, 60), text("共同的祖先", 1030, 730, 64, ACCENT)])),
 page(G("brain_a", BRAIN + [text("神经细胞特别多", 1230, 380, 60)], ),
      G("brain_b", [text("比狗多十多倍", 1230, 510, 66, ACCENT), text("遇到问题就靠它们想办法", 1230, 650, 50)])),
 page(G("tool_a", TOOL + [text("折下树枝", 1450, 390, 60), text("插进蚂蚁洞", 1450, 510, 60, ACCENT)]),
      G("tool_b", [text("蚂蚁爬上来", 1450, 640, 60), text("美餐一顿！", 1450, 760, 64, ACCENT)])),
 page(G("feel_a", [title("秘密三：感情丰富"), ill("faces", 150, 350, 1620, 583),
                   text("见面大声问好", 960, 260, 56, ACCENT),
                   text("高兴", 425, 810, 64, center=True), text("生气", 960, 810, 64, center=True), text("难过", 1495, 810, 64, center=True)])),
 page(G("feel_b", [title("还会安慰朋友"), ill("console", 90, 290, 1300, 600),
                   text("手搭在肩上", 1450, 420, 60), text("别生气，别发火", 1450, 550, 56, ACCENT)])),
 page(G("learn", [title("还能学会新本领"), ill("learn_eat", 120, 310, 1150, 560),
                  text("用餐具吃饭", 1350, 400, 60), text("用铲子挖土", 1350, 530, 56), text("骑三轮车", 1350, 650, 60, ACCENT)])),
 page(G("family_a", APES + [text("黄猩猩", 239, 845, 56, center=True), text("黑猩猩", 508, 845, 56, center=True),
                            text("侏黑猩猩", 759, 845, 56, center=True), text("大猩猩", 1057, 845, 56, center=True)])),
 page(G("family_b", [title("我国南方也发现过化石"), ill("fossil", 120, 310, 1150, 590),
                     text("山洞里的化石", 1350, 400, 56), text("猩猩家族曾经很大", 1350, 530, 56, ACCENT)])),
 page(G("protect", [title("要好好保护它们"), ill("friend", 150, 290, 700, 620),
                    text("越来越少了", 950, 410, 64), text("珍稀的保护动物", 950, 550, 68, ACCENT)])),
 page(G("ending", [ill("friend", 100, 300, 700, 560), text("会想办法", 880, 370, 64), text("会做工具", 880, 490, 64),
                   text("还有真感情", 880, 610, 64, ACCENT)]),
      G("cta", boxed("你还知道哪些聪明的动物？", 880, 740, 56, ACCENT)),
      G("outro", [ill("sanlian", 1260, 810, 320, 127), text("一键三连", 1620, 838, 54, ACCENT)], hold=.8)),
]
