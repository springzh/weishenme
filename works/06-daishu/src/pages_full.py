"""袋鼠为什么有袋 — full version pages (beat ids from beats.full.json)."""
from layoutkit import *

HOOK1 = "天哪！袋鼠宝宝"
HOOK2 = "只有豆子大！"
REACT = "这么小的宝宝，到底怎么活下来的？"

PAGES = [
 # hook: the surprise, written big, picture-free
 page(G("hook", [text(HOOK1, 960, 170, 120, center=True)] + ring_word(HOOK2, 960 - text_width(HOOK2, 130) / 2, 340, 130, ACCENT), lead=.15),
      G("hook2", [text(REACT, 960, 650, 72, center=True)])),

 page(G("hero", [title("澳大利亚的跳跃高手"), ill("australia", 60, 240, 1093, 700),
                  text("草原上的袋鼠", 1200, 360, 60), text("后腿特别有力", 1200, 500, 64),
                  text("一跳就是好几米", 1200, 620, 56, ACCENT)])),

 page(G("emblem", [title("国徽上的袋鼠"), ill("emblem", 120, 220, 640, 695),
                   text("画进了国徽", 900, 400, 76), text("澳大利亚的象征", 900, 560, 58)])),

 page(G("question", [title("肚子上的口袋"), ill("kangaroo_full", 60, 210, 860, 726),
                     text("名字叫育儿袋", 1000, 380, 72), text("它干什么用呢？", 1000, 660, 64, ACCENT)])),

 page(G("tiny_a", [title("宝宝出生得特别早"), ill("belly_cutaway", 50, 200, 880, 743),
                   text("只在肚里住", 1000, 380, 68), text("一个多月", 1000, 500, 68, ACCENT)])),

 page(G("tiny_b", [title("小得像一颗豆子"), ill("bean_scale", 40, 250, 1097, 680),
                   text("两厘米多长", 1180, 400, 76, ACCENT), text("还没一根手指长", 1180, 540, 56)])),

 page(G("climb", [title("妈妈舔出一条小路"), ill("climb", 40, 190, 1000, 760),
                  text("宝宝用小爪", 1230, 380, 60), text("一点一点爬进袋", 1230, 520, 56, ACCENT)])),

 page(G("milk_a", [title("袋里藏着乳头"), ill("pouch_milk", 60, 240, 903, 700),
                   text("宝宝找到了", 1080, 380, 64), text("一口咬住", 1080, 520, 68, ACCENT)])),

 page(G("milk_b", [title("奶会自己喷出来"), ill("milk_spray", 60, 240, 903, 700),
                   text("含着乳头", 1080, 380, 64), text("边睡边喝", 1080, 520, 68, ACCENT)])),

 page(G("grow", [title("在袋里住大半年"), ill("grow", 80, 230, 850, 661),
                 text("长出了绒毛", 1000, 380, 68), text("还探头看世界", 1000, 520, 64, ACCENT)])),

 page(G("danger_a", [title("危险来了！"), ill("leap", 40, 290, 1173, 640),
                     text("钻进袋子", 1280, 380, 64), text("妈妈就跑", 1280, 520, 64, ACCENT)])),

 page(G("danger_b", [title("一跳就是五米多"), ill("leap_far", 40, 290, 1173, 640),
                     text("一次跳出五米多", 1280, 380, 60, ACCENT), text("宝宝不会掉出来", 1280, 520, 56)])),

 page(G("answer", [ill("australia", 60, 300, 1000, 640), text("是宝宝的小床", 1120, 380, 64),
                   text("也是安全座", 1120, 500, 68), text("没有它，活不下来", 1120, 680, 60, ACCENT)])),

 page(G("cta", [text("小袋鼠要在口袋里住多久", 960, 300, 72, center=True),
                boxed("才第一次跳出来呢？", 960 - text_width("才第一次跳出来呢？", 80) / 2, 450, 80, ACCENT),
                text("把你的答案发在评论区", 960, 700, 56, GREY, center=True)]),
      G("outro", [text("一键三连", 1020, 828, 54, ACCENT), ill("sanlian", 1260, 800, 320, 127)], hold=.8)),
]
