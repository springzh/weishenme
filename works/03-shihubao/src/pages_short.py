"""为什么狮、虎、豹在白天老睡觉 — 30-second pages (beat ids from beats.short.json)."""
from layoutkit import *

HOOK1 = "天哪！狮子一天能睡"
HOOK2 = "二十个小时！"
PUN_A, PUN_B = "这哪是百兽之王，", "分明是睡觉大王！"
PUN_X = 960 - (text_width(PUN_A, 80) + text_width(PUN_B, 80)) / 2

HOOK_PAGE = page(G("hook", [text(HOOK1, 960, 170, 110, center=True)] + ring_word(HOOK2, 960 - text_width(HOOK2, 150) / 2, 330, 150, ACCENT), lead=.15),
                 G("hook2", [text(PUN_A, PUN_X, 650, 80), text(PUN_B, PUN_X + text_width(PUN_A, 80), 650, 80, ACCENT)]))

PAGES = [
 HOOK_PAGE,
 page(G("night", [text("白天休息", 90, 220, 64), ill("day_rest", 60, 330, 840, 560, weight=2),
                  text("夜里捕猎", 1000, 220, 64, ACCENT), ill("night_hunt", 1000, 330, 840, 560, weight=2)])),
 page(G("eye", [title("眼睛里的“小镜子”"), ill("eye_mirror", 120, 200, 1080, 672)] + ring_word("黑夜也看得清", 1270, 480, 64, ACCENT))),
 page(G("hunt", [ill("pounce", 60, 260, 900, 504, weight=2), text("猛地一扑", 330, 790, 64),
                 ill("charge", 1000, 300, 860, 497, weight=2), text("多睡觉攒劲", 1280, 820, 64, ACCENT)])),
 page(G("cta", [ill("walk_lion", 80, 260, 960, 597, weight=2), text("想看它们精神的样子？", 1080, 380, 64)]
               + boxed("早上或傍晚去！", 1100, 540, 80, ACCENT)),
      G("outro", [ill("sanlian", 1100, 700, 380, 121)], hold=.8)),
]
