"""为什么不把狼都消灭光 — 30-second pages (beat ids from beats.short.json)."""
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
 page(G("gone", GONE("狼被打光", "小树被啃光"))),
 page(G("back", BACK("狼回来了", "小树又长起来"))),
 page(G("chain", CHAIN[:1] + [text("不能把狼都消灭光！", 960, 800, 72, ACCENT, center=True)])),
 page(G("cta", ASK + boxed("野兔会变多还是变少？", 1050, 380, 56, ACCENT)),
      G("outro", [ill("sanlian", 1100, 580, 380, 121)], hold=.8)),
]
