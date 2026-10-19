"""为什么说猩猩最聪明 — short version pages (beat ids from beats.short.json)."""
from layoutkit import *

HOOK1 = "天哪！猩猩"
HOOK2 = "居然会劝架！"
PUN_A, PUN_B = "它还会自己做工具，", "钓蚂蚁吃！"
PUN_X = 960 - (text_width(PUN_A, 76) + text_width(PUN_B, 76)) / 2

HOOK_PAGE = page(G("hook", [text(HOOK1, 960, 180, 120, center=True)] + ring_word(HOOK2, 960 - text_width(HOOK2, 130) / 2, 350, 130, ACCENT), lead=.15),
                 G("hook2", [text(PUN_A, PUN_X, 660, 76), text(PUN_B, PUN_X + text_width(PUN_A, 76), 660, 76, ACCENT)]))

PAGES = [
 HOOK_PAGE,
 page(G("brain", [title("我们的近亲"), ill("brain_cells", 90, 290, 1050, 590),
                  text("神经细胞", 1200, 410, 60), text("比狗多十多倍", 1200, 540, 64, ACCENT)])),
 page(G("tool", [title("会做工具"), ill("ant_fish", 150, 330, 1250, 540, weight=2),
                 text("插进蚂蚁洞", 1450, 430, 60), text("钓蚂蚁吃！", 1450, 560, 64, ACCENT)])),
 page(G("feel", [ill("console", 250, 280, 1300, 570, weight=2),
                 text("会安慰朋友", 300, 850, 64, ACCENT)])),
 page(G("ending", [text("会想办法、会做工具", 960, 320, 72, center=True), text("还有感情", 960, 450, 64, center=True),
                   text("所以说猩猩最聪明！", 960, 570, 84, ACCENT, center=True)]),
      G("cta", boxed("还有哪些动物特别聪明？", 652, 700, 56, ACCENT)),
      G("outro", [ill("sanlian", 1280, 800, 380, 150)], hold=.8)),
]
