"""袋鼠为什么有袋 — short version pages (beat ids from beats.short.json)."""
from layoutkit import *

HOOK1 = "天哪！袋鼠宝宝"
HOOK2 = "只有豆子大！"

PAGES = [
 page(G("hook", [text(HOOK1, 960, 200, 120, center=True)] + ring_word(HOOK2, 960 - text_width(HOOK2, 130) / 2, 380, 130, ACCENT), lead=.15)),

 page(G("why_a", [title("刚出生：两厘米多长"), ill("bean_scale", 40, 260, 1100, 682),
                  text("还没一根手指长", 1180, 400, 60, ACCENT), text("眼睛也没睁开", 1180, 540, 56)])),

 page(G("why_b", [title("口袋就是育儿房"), ill("pouch_milk", 60, 240, 900, 698),
                  text("含着乳头", 1040, 380, 64), text("边睡边喝奶", 1040, 520, 64, ACCENT)])),

 page(G("safety", [title("遇险就钻进袋子"), ill("leap", 40, 300, 1150, 627),
                   text("妈妈一跳五米多", 1220, 400, 60, ACCENT), text("宝宝稳稳在袋里", 1220, 540, 56)])),

 page(G("cta", [text("小袋鼠要在口袋里", 960, 280, 72, center=True),
                boxed("住多久才出来？", 960 - text_width("住多久才出来？", 84) / 2, 430, 84, ACCENT),
                text("评论区告诉我！", 960, 640, 60, GREY, center=True)]),
      G("outro", [text("一键三连", 1060, 828, 54, ACCENT), ill("sanlian", 1300, 800, 300, 119)], hold=.8)),
]
