"""为什么不把狼都消灭光 — full version pages (beat ids from beats.full.json)."""
from layoutkit import *

HOOK1 = "天哪！狼没了"
HOOK2 = "小树竟然遭殃了！"
PUN_A, PUN_B = "狼和小树，", "到底有什么关系？"
PUN_X = 960 - (text_width(PUN_A, 80) + text_width(PUN_B, 80)) / 2

# hook: the surprising consequence + the riddle, big words only, no picture
HOOK_PAGE = page(G("hook", [text(HOOK1, 960, 170, 120, center=True)] + ring_word(HOOK2, 960 - text_width(HOOK2, 130) / 2, 340, 130, ACCENT), lead=.15),
                 G("hook2", [text(PUN_A, PUN_X, 650, 80), text(PUN_B, PUN_X + text_width(PUN_A, 80), 650, 80, ACCENT)]))

GONE = lambda a, b: [ill("gone", 60, 250, 1300, 600), text(a, 1420, 360, 64), text(b, 1420, 480, 64, ACCENT)]
BACK = lambda a, b: [ill("back", 60, 250, 1300, 600), text(a, 1420, 360, 64), text(b, 1420, 480, 64, ACCENT)]
CHAIN = [ill("chain", 160, 300, 1300, 440), text("吃", 585, 470, 64, ACCENT), text("吃", 1035, 470, 64, ACCENT)]
ASK = [ill("fox_hare", 80, 300, 900, 440)]

PAGES = [
 HOOK_PAGE,
 page(G("story_a", [ill("storybook", 60, 220, 900, 600), text("故事里：大灰狼是坏蛋", 1020, 330, 56)]),
      G("story_b", [ill("kid", 1580, 470, 300, 415), text("真消灭光，会怎样？", 1020, 460, 56, ACCENT)])),
 page(G("wolf_a", [title("狼长得像大狗"), ill("wolf_dog", 220, 260, 1300, 560), text("耳朵竖着", 560, 330, 56), text("尾巴下垂", 60, 600, 56)]),
      G("wolf_b", [text("狗：尾巴向上卷", 920, 330, 56, ACCENT)])),
 page(G("pack_a", [title("狼是一家子"), ill("pack", 60, 300, 1340, 520), text("几只到十几只", 1430, 600, 56, ACCENT)])),
 page(G("pack_b", [ill("howl", 80, 200, 820, 600), text("嗷呜——", 1000, 300, 90), text("呼唤家人", 1000, 470, 64), text("这是我家地盘！", 1000, 590, 64, ACCENT)])),
 page(G("eat", [title("狼吃什么？"), ill("eat", 300, 280, 1300, 480), text("有时偷吃羊", 1250, 800, 56, ACCENT)])),
 page(G("gone_a", [title("黄石公园：狼被打光了")]),
      G("gone_b", GONE("鹿变多", "小树被啃光")),
      G("gone_c", [text("鸟和河狸不见了", 1420, 600, 56, ACCENT)])),
 page(G("back_a", [title("把狼请回来！")]),
      G("back_b", BACK("小树长起来", "鸟和河狸回来了"))),
 page(G("chain", [title("狼吃鹿，鹿吃树")] + CHAIN + [text("大自然的管理员", 960, 800, 72, ACCENT, center=True)])),
 page(G("protect", [ill("protect", 160, 260, 620, 620), text("国家二级保护动物", 900, 420, 72), text("不能随便捕杀", 900, 560, 64, ACCENT)])),
 page(G("safe", [title("野外看见狼？"), ill("safe", 60, 300, 1240, 600), text("不靠近", 1360, 330, 60), text("不转身跑", 1360, 440, 60),
                 text("大声喊", 1360, 550, 60), text("慢慢退开", 1360, 660, 60), text("找大人！", 1360, 770, 60, ACCENT)])),
 page(G("ending", [ill("wolf_tree", 100, 260, 760, 560), text("每一种动物", 960, 380, 72), text("都有自己的位置", 960, 500, 72, ACCENT)])),
 # the question back to the viewer, then the series outro
 page(G("cta", ASK + boxed("野兔会变多还是变少？", 1050, 380, 56, ACCENT)),
      G("outro", [ill("sanlian", 1100, 580, 380, 121), text("一键三连", 1520, 600, 60, ACCENT)], hold=.8)),
]
