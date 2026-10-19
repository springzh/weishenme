"""为什么狮、虎、豹在白天老睡觉 — full version pages (beat ids from beats.full.json)."""
from layoutkit import *

HOOK1 = "天哪！狮子一天能睡"
HOOK2 = "二十个小时！"
PUN_A, PUN_B = "这哪是百兽之王，", "分明是睡觉大王！"
PUN_X = 960 - (text_width(PUN_A, 80) + text_width(PUN_B, 80)) / 2

HOOK_PAGE = page(G("hook", [text(HOOK1, 960, 170, 110, center=True)] + ring_word(HOOK2, 960 - text_width(HOOK2, 150) / 2, 330, 150, ACCENT), lead=.15),
                 G("hook2", [text(PUN_A, PUN_X, 650, 80), text(PUN_B, PUN_X + text_width(PUN_A, 80), 650, 80, ACCENT)]))

PAGES = [
 # hook: exaggerated fact + a punchline, big words only, no picture
 HOOK_PAGE,
 page(G("zoo_a", [ill("kid", 200, 140, 540, 748), text("去动物园，最想看：", 860, 340, 72), text("狮子 · 老虎 · 豹子", 860, 480, 96, ACCENT)])),
 page(G("zoo_b", [title("它们怎么老睡觉？"), ill("zoo_sleep", 180, 250, 1560, 672)])),
 # day vs night, side by side
 page(G("night_a", [text("白天：躲起来休息", 90, 220, 64), ill("day_rest", 60, 330, 840, 560)]),
      G("night_b", [text("夜里：出来捕猎", 1000, 220, 64, ACCENT), ill("night_hunt", 1000, 330, 840, 560)])),
 page(G("eye_a", [title("眼睛里的“小镜子”"), ill("eye_mirror", 120, 200, 1080, 672)]),
      G("eye_b", [text("微光再反射一遍", 1260, 400, 60)] + ring_word("黑夜也看得清", 1270, 560, 64, ACCENT))),
 page(G("hot", [title("白天太热，躲进阴凉"), ill("heat", 150, 200, 984, 672), text("省力气", 1260, 420, 72), text("不热坏", 1260, 560, 72, ACCENT)])),
 page(G("hunt_a", [title("捕猎：突然一扑"), ill("ambush", 60, 330, 760, 420), text("先埋伏", 330, 780, 64),
                   ill("pounce", 880, 330, 900, 504), text("再猛扑！", 1230, 850, 64, ACCENT)])),
 page(G("hunt_b", [title("好好睡觉，攒足力气"), ill("charge", 160, 220, 1170, 676), text("吃饱一顿", 1400, 520, 64), text("睡大半天", 1400, 640, 64, ACCENT)])),
 page(G("zoo_habit", [title("住进动物园，老习惯没变"), ill("zoo_sleep", 100, 300, 1100, 474), text("白天休息多", 1260, 380, 72), text("晚上活动多", 1260, 520, 72, ACCENT)])),
 page(G("tip_a", [title("什么时候去看？"), ill("walk_lion", 100, 220, 1080, 672), text("早上一开园", 1240, 360, 68)]),
      G("tip_b", [text("喂食之前", 1240, 500, 68), text("傍晚", 1240, 640, 68, ACCENT)])),
 # answer, then the question back to the viewer
 page(G("ending", [ill("night_hunt", 80, 230, 780, 520, weight=2), text("黑夜里的猎手", 940, 250, 84, ACCENT)]),
      G("cta", [ill("cat", 940, 400, 500, 339, weight=2)] + boxed("小猫也白天睡、晚上闹吗？", 950, 770, 56, ACCENT)),
      G("outro", [ill("sanlian", 1480, 430, 380, 121), text("一键三连", 1560, 590, 60, ACCENT)], hold=.8)),
]
