"""为什么狮、虎、豹在白天老睡觉 — what each figure shows, its parts, and the narration it must make visible.

reqs quote the full narration; reqs_short quotes the 30-second narration where it uses the figure."""
from partkit import *

CAT_ORDER = "猫科动物按 头→身体→腿 绘制（头在画面右侧），作为背景的地面/夜空最后补上"

SPECS = {
 "kid": dict(
    composition="正面站立的小朋友：棕色短发、好奇地扬起眉毛、嘴巴圆圆的；黄色外套，手套，裤子和靴子。",
    why="人物拆为头（含头发）、颈、躯干、画面左臂、右臂、下半身六部分，各部分外形独立一笔。",
    subjects=[("kid", H)],
    parts=kid_parts("kid", 260, 360),
    reqs=[R("kid", "动物园是小朋友最喜欢去的地方", "一个好奇张望的小朋友")]),
 "zoo_sleep": dict(
    composition="动物园围栏前的沙地上，从左到右趴着一只狮子（深棕鬃毛）、一只老虎（黑条纹）、一只豹子（深色斑点），三只都闭着眼睛把头搁在前爪上睡觉。",
    why="围栏一部分；三只猫各分头、身体两部分；沙地最后。每个形状独立一笔，条纹、斑点各一笔。",
    subjects=[("fence", E), ("lion", A), ("tiger", A), ("leopard", A), ("ground", E)],
    parts=[P("fence", "fence", "zoo_fence", ["两道横杆", "一根根竖栏杆"], rect(0, 0, 1, 0.568))]
          + lying_parts("zoo_sleep", 225, 486, 0.82, subject="lion", prefix="lion_")
          + lying_parts("zoo_sleep", 650, 486, 0.82, subject="tiger", prefix="tiger_")
          + lying_parts("zoo_sleep", 1070, 486, 0.82, subject="leopard", prefix="leopard_")
          + [P("ground", "ground", "sand_ground", ["沙地外框一笔"], FULL)],
    reqs=[R("three", "大家都想看狮子、老虎、豹子威风凛凛的样子", "狮子、老虎、豹子三只都在画面里，一眼能分清"),
          R("sleep", "可它们偏偏总在抱头睡大觉", "三只都闭着眼、把头搁在前爪上睡觉")],
    reqs_short=[R("zoo", "动物园里的它们，也还保留着这个老习惯", "动物园围栏里，狮子、老虎、豹子都在睡觉")],
    exception="先画背景围栏，再从左到右画三只猫（各自头→身体），沙地最后"),
 "day_rest": dict(
    composition="白天：左边一棵大树，树荫下趴着一只闭眼睡觉的老虎；右上角火辣的太阳，下面三支红色波浪热量箭头。",
    why="大树、太阳与热量箭头、老虎头、老虎身体、地面五部分；每个形状独立一笔。",
    subjects=[("tree", E), ("sun", E), ("tiger", A), ("ground", E)],
    parts=[P("tree", "tree", "tree", ["树冠一笔", "树干一笔"], rect(0, 0, 0.55, 0.655)),
           P("sun", "sun", "sun_and_heat", ["太阳一圈", "八道光芒", "三支波浪热量箭头"], rect(0.62, 0, 1, 0.56))]
          + lying_parts("day_rest", 320, 488, 0.74, subject="tiger")
          + [P("ground", "ground", "ground_and_shade", ["地面外框", "树荫"], FULL)],
    reqs=[R("shade", "它们大多躲在树荫、草丛或者山洞里休息", "老虎趴在树荫下闭眼睡觉"),
          R("hot", "白天太阳火辣辣的", "画面里有火辣的太阳和向下的热量箭头")],
    reqs_short=[R("shade", "白天躲在阴凉处休息", "老虎趴在树荫下闭眼睡觉")],
    exception="先画背景大树和太阳，再画树荫下的老虎（头→身体），地面最后"),
 "night_hunt": dict(
    composition="暮紫色夜空和深一些的地面，左上一弯金色月亮，几颗星星；一只狮子睁着发亮的金色眼睛在夜里走动。",
    why="月亮、狮子头、身体、腿，夜空与星星五部分；夜空是一整块暮紫色面。",
    subjects=[("moon", E), ("lion", A), ("night", E)],
    parts=[P("moon", "moon", "moon", ["月亮一圈"], circle("night_hunt", 120, 110, 66))]
          + quadruped_parts("night_hunt", 420, 290, 0.95, subject="lion", exclude=COOL + NIGHT)
          + [P("night", "night", "night_sky_and_ground", ["夜空外框一笔", "六颗星星各两笔"], FULL)],
    reqs=[R("night", "到了夜里才出来捕猎", "夜空（月亮和星星）下，狮子醒着在走动"),
          R("glow", "所以在昏暗的夜里，也能看得清清楚楚", "狮子的眼睛在黑夜里发亮")],
    reqs_short=[R("night", "夜里才出来捕猎", "夜空（月亮和星星）下，狮子醒着在走动")],
    exception="先画月亮，再画狮子（头→身体→腿），夜空最后作为背景铺满"),
 "eye_mirror": dict(
    composition="眼睛剖面示意：左上一弯月亮（夜里光很弱）；一个大眼球，前面是透明的晶状体，后面内壁有一层金色弧形“小镜子”；一支黄色光线从左边射进眼睛碰到小镜子，另一支红色光线从小镜子反射回来射出眼睛，反射处有一个小闪光。",
    why="月亮、眼球（含晶状体、金色反光层和穿过它的彩色光线——光线没有墨线，归到有墨线的眼球部位）两部分；每个形状独立一笔。",
    subjects=[("moon", E), ("eye", O)],
    parts=[P("moon", "moon", "moon", ["月亮一圈"], rect(0, 0, 0.19, 0.3)),
           P("eye", "eye", "eyeball", ["眼球一圈", "金色反光层一笔", "晶状体一圈", "射入的光线", "反射出的光线和箭头", "闪光两笔"], FULL)],
    reqs=[R("mirror", "有一层像小镜子一样的膜", "眼睛后部内壁有一层金色的反光层"),
          R("bounce", "能把微弱的光再反射一遍", "一支光线射进眼睛碰到反光层，另一支从反光层反射回来")],
    reqs_short=[R("mirror", "它们眼睛后面有一层像小镜子的膜", "眼睛后部内壁有一层金色的反光层"),
                R("bounce", "黑夜里也看得清", "光线射进眼睛碰到反光层又反射回来")]),
 "heat": dict(
    composition="火辣辣的大太阳，下面三支红色波浪热量箭头射向沙地；右边一支温度计，红色液柱几乎升到顶。",
    why="太阳、热量箭头、温度计、沙地四部分；每个形状独立一笔。",
    subjects=[("sun", E), ("heat", O), ("thermometer", O), ("ground", E)],
    parts=[P("sun", "sun", "sun", ["太阳一圈", "八道光芒"], rect(0, 0, 0.62, 0.56)),
           P("heat", "heat", "heat_arrows", ["三支波浪热量箭头"], rect(0, 0, 0.62, 0.79)),
           P("thermometer", "thermometer", "thermometer", ["温度计外形", "液泡一圈", "六道刻度"], rect(0.68, 0, 1, 0.88)),
           P("ground", "ground", "sand_ground", ["沙地外框一笔"], FULL)],
    reqs=[R("hot", "跑一跑就浑身发热", "太阳、热量箭头和升到顶的温度计表示很热")]),
 "ambush": dict(
    composition="一只豹子压低身体趴伏着，身体大半藏在一排绿色草丛后面，只露出背和头，盯着前方。",
    why="豹子头、身体、腿，草丛与地面四部分；每根草一笔、斑点各一圈。",
    subjects=[("leopard", A), ("grass", E)],
    parts=quadruped_parts("ambush", 330, 230, 0.8, crouch=1.2, head_rot=0.12, subject="leopard", exclude=COOL + GRASS)
          + [P("grass", "grass", "grass_and_ground", ["一簇簇草各三笔", "地面外框"], FULL)],
    reqs=[R("hide", "先悄悄埋伏", "豹子压低身体藏在草丛后")],
    exception=CAT_ORDER),
 "pounce": dict(
    composition="一只豹子腾空扑出：身体前倾离开地面，前腿伸向前方、后腿蹬向后方，身后有四条速度线；下面一条沙地。",
    why="豹子头、身体、腿，速度线与地面四部分；每条速度线一笔。",
    subjects=[("leopard", A), ("speed", E)],
    parts=quadruped_parts("pounce", 520, 235, 0.88, rot=-0.18, stride=1.0, subject="leopard")
          + [P("speed", "speed", "speed_lines_and_ground", ["四条速度线各一笔", "地面外框"], FULL)],
    reqs=[R("leap", "再猛地冲上去", "豹子腾空前扑，四条腿离地张开，身后有速度线")],
    reqs_short=[R("leap", "捕猎要猛地一扑", "豹子腾空前扑，四条腿离地张开，身后有速度线")],
    exception=CAT_ORDER),
 "charge": dict(
    composition="一只豹子闭着眼趴在沙地上睡觉；右上方一节电池，里面四格绿色电量已经充满。",
    why="电池、豹子头、豹子身体、地面四部分；电池外壳和每格电量各一笔。",
    subjects=[("battery", O), ("leopard", A), ("ground", E)],
    parts=[P("battery", "battery", "battery", ["电池外壳一笔", "正极一笔", "四格电量各一笔"], rect(0.6, 0, 1, 0.36))]
          + lying_parts("charge", 400, 455, 0.95, subject="leopard")
          + [P("ground", "ground", "sand_ground", ["沙地外框一笔"], FULL)],
    reqs=[R("rest", "所以平时得好好休息，攒足力气", "睡觉的豹子上方，电池电量是满的")],
    reqs_short=[R("rest", "所以平时得多睡觉攒劲", "睡觉的豹子上方，电池电量是满的")],
    exception="先画右上角的电池，再画睡觉的豹子（头→身体），地面最后"),
 "walk_lion": dict(
    composition="动物园围栏前的沙地上，一只狮子睁着眼睛站起来，向右走动。",
    why="狮子头、身体、腿，围栏，沙地五部分；栏杆每根一笔。",
    subjects=[("lion", A), ("fence", E), ("ground", E)],
    parts=quadruped_parts("walk_lion", 420, 330, 0.95, subject="lion")
          + [P("fence", "fence", "zoo_fence", ["两道横杆", "一根根竖栏杆"], rect(0, 0, 1, 0.54)),
             P("ground", "ground", "sand_ground", ["沙地外框一笔"], FULL)],
    reqs=[R("walk", "它们常常会起来走来走去", "动物园围栏前，狮子睁着眼站起来走动")],
    reqs_short=[R("walk", "早上或傍晚去动物园试试吧", "动物园围栏前，狮子睁着眼站起来走动")],
    exception="先画前景的狮子（头→身体→腿），背景围栏和地面后画；被狮子挡住的那几段栏杆随狮子一起出现"),
 "cat": dict(
    composition="一只橘色条纹小猫蜷在粉色圆垫子上，闭着眼睛，把头搁在前爪上睡觉。",
    why="小猫头、小猫身体、垫子三部分；每个形状独立一笔。",
    subjects=[("cat", A), ("cushion", O)],
    parts=lying_parts("cat", 250, 300, 0.9, subject="cat") + [P("cushion", "cushion", "cushion", ["垫子一圈"], FULL)],
    reqs=[R("cat", "家里的小猫", "一只在垫子上睡觉的小猫")],
    exception="先画小猫（头→身体），垫子最后"),
 "lion_sleep": dict(
    composition="一只大大的狮子（深棕鬃毛）闭着眼睛，把头搁在前爪上趴在沙地上睡觉。（封面主图）",
    why="狮子头、身体、沙地三部分；每个形状独立一笔。",
    subjects=[("lion", A), ("ground", E)],
    parts=lying_parts("lion_sleep", 360, 352, 1.25, subject="lion") + [P("ground", "ground", "sand_ground", ["沙地外框一笔"], FULL)],
    reqs=[R("sleep", "可它们偏偏总在抱头睡大觉", "一只狮子闭眼趴着睡大觉")],
    exception="先画狮子（头→身体），沙地最后"),
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
