"""袋鼠为什么有袋 — what each figure shows, its parts, and the narration it must make visible.

reqs quote the full narration; reqs_short quotes the 30-second narration where the wording differs."""
from partkit import *
from character_parts import *   # 系列素材库 kit/：kangaroo_parts、joey_parts……


SPECS = {
 "australia": dict(
    composition="澳大利亚草原：右上角太阳，后面一道低矮的沙丘，草地上两只袋鼠（右边一大只带着袋里的宝宝，左边一小只）。",
    why="两只袋鼠各为尾巴、头、身体（含育儿袋和前爪）、后腿四部分；太阳一块；草地与沙丘兜底。",
    subjects=[("sun", E), ("big", A), ("small", A), ("ground", E)],
    parts=[P("sun", "sun", "sun", ["太阳圆圈一笔", "八道光芒"], box("australia", 800, 20, 970, 170))]
          + kangaroo_parts("australia", 660, 522, 0.72, subject="big", prefix="big_")
          + kangaroo_parts("australia", 250, 522, 0.45, subject="small", prefix="small_")
          + [P("ground", "ground", "grass", ["草地外框一笔", "沙丘轮廓一笔", "几丛草"], FULL)],
    reqs=[R("grass", "在澳大利亚的草原上，住着一群跳跃高手", "草地上站着两只袋鼠，天上有太阳"),
          R("legs", "它们后腿特别有力，一蹦一跳，就是好几米远", "袋鼠的后腿又粗又长，长尾巴撑在地上")],
    exception="太阳先画，再由小到大画两只袋鼠，草地在最后；沙丘只作背景。"),

 "emblem": dict(
    composition="一个盾形国徽，中间一只侧面站立的袋鼠，盾牌上方一颗五角星，下方一道横线分开。",
    why="盾牌一笔、星星一笔、横线一笔；袋鼠为尾巴、头、身体、后腿四部分。",
    subjects=[("shield", O), ("kangaroo", A)],
    parts=kangaroo_parts("emblem", 350, 620, 0.55, subject="kangaroo")
          + [P("shield", "shield", "shield", ["盾牌外形一笔", "五角星一笔", "横线一笔"], FULL)],
    reqs=[R("emblem", "人们把它画进了国家的国徽里", "一个盾形徽章，中间是袋鼠，上方一颗星")],
    exception="盾牌是底，先画袋鼠再画盾牌的星和线以拥有袋鼠之外的像素。"),

 "kangaroo_full": dict(
    composition="草地上正面偏侧的一只袋鼠妈妈：长耳朵、长吻、粗后腿、撑地的长尾巴，肚子前面一个明显的育儿袋。",
    why="袋鼠为尾巴、头、身体（含育儿袋）、后腿四部分；草地兜底。",
    subjects=[("kangaroo", A), ("ground", E)],
    parts=kangaroo_parts("kangaroo_full", 450, 690, 0.95, subject="kangaroo")
          + [P("ground", "ground", "grass", ["草地外框一笔", "两丛草"], FULL)],
    reqs=[R("pouch", "袋鼠妈妈的肚子上，都有一个毛茸茸的口袋", "袋鼠肚子前面有明显的口袋和一道袋口线")],
    exception="草地画在最后；袋鼠按尾巴→头→身体→后腿的顺序声明。"),

 "belly_cutaway": dict(
    composition="草地上的袋鼠妈妈，腹部旁一条短线连到一个圆形放大框，框里是一颗豆子大的粉色小宝宝。",
    why="袋鼠四部分；放大框圆圈一笔、指向腹部的小线、豆子宝宝一笔。",
    subjects=[("kangaroo", A), ("inset", O), ("ground", E)],
    parts=kangaroo_parts("belly_cutaway", 400, 690, 0.88, subject="kangaroo")
          + [P("inset", "inset", "inset", ["圆形放大框一圈", "指向腹部的小线", "豆子宝宝外形一笔", "闭着的眼睛", "两只小爪"],
               circle("belly_cutaway", 758, 232, 112))]
          + [P("ground", "ground", "grass", ["草地外框一笔"], FULL)],
    reqs=[R("early", "它在妈妈肚子里，只住一个多月", "妈妈腹部旁有一个圆形放大框，框里是一颗小小的豆子宝宝")],
    exception="先画袋鼠，再画指向腹部的小线和放大框。"),

 "bean_scale": dict(
    composition="左边一根朝下指的手指，手指右边一颗真实大小的粉色豆子宝宝，右边放大镜里是放大的宝宝（闭着眼、两只小爪）。",
    why="手指外形与指甲、指节线；豆子宝宝一笔；放大镜镜圈与镜柄各一笔。",
    subjects=[("finger", O), ("bean", A), ("lens", O)],
    parts=[P("finger", "finger", "finger", ["手掌矩形一笔", "手指外形一笔", "指甲一圈", "指节线一笔", "手背折线两笔"],
             box("bean_scale", 60, 40, 400, 590)),
           P("bean_head", "bean", "head", ["头端一圈", "闭着的眼睛", "小鼻子"], box("bean_scale", 488, 372, 556, 456)),
           P("bean_body", "bean", "torso", ["豆子身体一笔", "两只小爪", "卷尾巴"], box("bean_scale", 360, 372, 500, 502)),
           P("lens", "lens", "lens", ["放大镜圈一圈", "镜柄一笔", "镜里的宝宝外形一笔", "闭着的眼睛", "两只小爪"], FULL)],
    reqs=[R("size", "只有两厘米多长，还没有一根手指长", "一根手指竖在旁边，豆子宝宝比手指短得多，放大镜里能看清闭着的眼睛"),
          R("bean", "像一颗红色的豆子，眼睛也没睁开", "宝宝是一颗粉红色的豆子形状，眼睛是一条闭着的线")],
    reqs_short=[R("size", "才两厘米多长", "一根手指竖在旁边，豆子宝宝比手指短得多，放大镜里能看清闭着的眼睛")],
    exception="先手指、再真实大小的宝宝、最后放大的宝宝与镜圈。"),

 "climb": dict(
    composition="草地上袋鼠妈妈侧身站立，身前一条由短横线组成的湿路从地面一直通到袋口，豆子大的小宝宝在小路上往上爬。",
    why="袋鼠四部分；小宝宝一笔加爪子；湿路为短横线，画在身体之上。",
    subjects=[("kangaroo", A), ("joey", A), ("ground", E)],
    parts=joey_parts("climb", 712, 566, 0.42, subject="joey")
          + [P("path_dots", "joey", "path", ["湿路上的短横线"], box("climb", 664, 380, 768, 700))]
          + kangaroo_parts("climb", 560, 690, 0.9, subject="kangaroo", prefix="mom_")
          + [P("ground", "ground", "grass", ["草地外框一笔", "湿路上的短横线"], FULL)],
    reqs=[R("path", "舔出一条通往口袋的小路", "袋鼠妈妈身前有一条虚线小点组成的小路，从地上一直通到袋口"),
          R("crawl", "一点一点爬进育儿袋", "豆子大的小宝宝贴在妈妈肚子的小路上，用小爪往上爬")],
    exception="湿路画在身体上，但小宝宝部位先声明以拥有自己的像素。"),

 "pouch_milk": dict(
    composition="育儿袋的横切面：外壁是毛，里面是浅色袋腔，袋腔右侧连着一只乳头，宝宝在袋里用嘴含住乳头。",
    why="袋腔一笔、袋壁一笔加几根绒毛、乳头两笔、宝宝一笔加爪子。",
    subjects=[("pouch", O), ("teat", O), ("joey", A)],
    parts=[P("teat", "teat", "teat", ["乳头管一笔", "乳头头一圈"], box("pouch_milk", 480, 300, 680, 362))]
           + joey_parts("pouch_milk", 404, 356, 1.45, subject="joey")
           + [P("cavity", "pouch", "pouch_inside", ["袋腔内壁一笔", "几根绒毛"], box("pouch_milk", 128, 164, 672, 494)),
              P("wall", "pouch", "pouch_wall", ["袋壁外沿一笔"], FULL)],
    reqs=[R("teat", "口袋里藏着乳头", "袋腔里一侧伸出一只乳头，宝宝的脸凑在乳头边"),
          R("hold", "一口咬住，就再也不肯松开了", "宝宝的嘴紧紧含住乳头")],
    reqs_short=[R("teat", "宝宝爬进去咬住乳头", "袋腔里一侧伸出一只乳头，宝宝的嘴含住它")],
    exception="乳头和宝宝画在袋腔里面，先于袋腔声明。"),

 "milk_spray": dict(
    composition="同一幅育儿袋横切面，乳头旁一串白色奶滴喷向宝宝的嘴，嘴下几道短短的红色奶流。",
    why="袋腔、袋壁、乳头、宝宝同 pouch_milk；奶滴为白色小圈，奶流为红色短线。",
    subjects=[("pouch", O), ("teat", O), ("joey", A), ("milk", O)],
    parts=[P("milk", "milk", "milk", ["四滴奶各一圈", "三道奶流短线"], box("milk_spray", 448, 336, 520, 404)),
           P("teat", "teat", "teat", ["乳头管一笔", "乳头头一圈"], box("milk_spray", 480, 300, 680, 362))]
           + joey_parts("milk_spray", 404, 356, 1.45, subject="joey")
           + [P("cavity", "pouch", "pouch_inside", ["袋腔内壁一笔", "几根绒毛"], box("milk_spray", 128, 164, 672, 494)),
              P("wall", "pouch", "pouch_wall", ["袋壁外沿一笔"], FULL)],
    reqs=[R("spray", "妈妈的乳汁会自己喷出来", "乳头旁边有一串白色奶滴，射向宝宝的嘴"),
          R("sleep", "一边睡觉，一边就能喝到奶", "宝宝闭着眼睛含住乳头")],
    exception="奶滴画在宝宝前面，先声明；其余同 pouch_milk。"),

 "grow": dict(
    composition="草地上袋鼠妈妈站着，袋口探出一只长大不少的小袋鼠脑袋（两只耳朵、眼睛睁着），旁边两个小闪光。",
    why="袋鼠四部分（头和袋里的宝宝都在头的框外，宝宝属于身体部位）；闪光两笔；草地兜底。",
    subjects=[("kangaroo", A), ("ground", E)],
    parts=kangaroo_parts("grow", 460, 636, 0.9, subject="kangaroo")
          + [P("ground", "ground", "grass", ["草地外框一笔", "两个闪光"], FULL)],
    reqs=[R("grow", "宝宝在口袋里住了大半年", "袋口探出一个长了绒毛的小袋鼠脑袋"),
          R("peek", "还常常探出头来东张西望", "小袋鼠的头和耳朵露在口袋外面，眼睛睁着")]),

 "leap": dict(
    composition="袋鼠妈妈贴着地面全速腾空：身体前伸、后腿向后拖、长尾巴向后伸直，袋口露出宝宝的头；身后几道速度线，脚下有几个土块。",
    why="袋鼠为尾巴、头、身体（含袋里宝宝）、后腿四部分；速度线与土块并入草地兜底。",
    subjects=[("kangaroo", A), ("ground", E)],
    parts=kangaroo_parts("leap", 700, 520, 0.78, pose="leap", subject="kangaroo")
          + [P("ground", "ground", "speed", ["速度线四笔", "三个土块", "草地外框一笔"], FULL)],
    reqs=[R("run", "小袋鼠一头钻进袋子，妈妈撒腿就跑", "袋鼠妈妈腾空跳跃，后腿和尾巴向后伸，袋口露出宝宝的头"),
          R("speed", "跑得再快，也不会掉出来", "妈妈身后有几道速度线，宝宝稳稳在袋里")],
    reqs_short=[R("run", "宝宝钻进口袋，妈妈一跳五米多", "袋鼠妈妈腾空跳跃，后腿和尾巴向后伸，袋口露出宝宝的头")],
    exception="袋鼠在速度线之后画；尾巴先于身体声明。"),

 "leap_far": dict(
    composition="草地上两根标柱相隔很远，中间一条虚线弧线表示跳跃轨迹；袋鼠妈妈在弧线中间腾空，袋里带着宝宝。",
    why="袋鼠四部分；标柱各一笔、虚线弧九段；草地兜底。",
    subjects=[("kangaroo", A), ("marks", O), ("ground", E)],
    parts=kangaroo_parts("leap_far", 700, 470, 0.62, pose="leap", subject="kangaroo")
          + [P("marks", "marks", "distance_marks", ["两根标柱各一笔", "九段虚线弧"], box("leap_far", 60, 160, 1040, 560))]
          + [P("ground", "ground", "grass", ["草地外框一笔"], FULL)],
    reqs=[R("five", "就能跳出五米多远", "地上两根标柱隔得很远，中间一条虚线弧线，袋鼠在弧线中腾空")],
    exception="标柱和弧线画在袋鼠之前，但袋鼠部位先声明以拥有自己的像素。"),

 "kangaroo_bean": dict(
    composition="封面主图：浅沙色圆底上放大的粉色豆子宝宝，闭着眼睛、两只小爪，周围三个小闪光。",
    why="圆底一笔；宝宝拆头/身体两块；闪光三笔。",
    subjects=[("bean", A), ("backdrop", E)],
    parts=joey_parts("kangaroo_bean", 320, 322, 2.9, subject="bean")
          + [P("backdrop", "backdrop", "backdrop", ["圆底一圈", "三个闪光"], FULL)],
    reqs=[R("bean", "袋鼠宝宝只有豆子大", "一颗放大的粉色豆子宝宝，闭着眼睛、两只小爪")],
    exception="圆底先画，宝宝后画；两个部位的框落在圆底之内。"),

 "sanlian": dict(
    composition="爱心、硬币、星星三个小图标一排。",
    why="三个图标各一笔（轮廓），互不重叠。",
    subjects=[("icons", O)],
    parts=[P("icons", "icons", "icons", ["爱心一圈", "硬币两圈", "星星一笔"], FULL)],
    reqs=[R("sanlian", "记得一键三连哦", "爱心、硬币、星星三个图标并排")],
    reqs_short=[R("sanlian", "记得一键三连哦", "爱心、硬币、星星三个图标并排")]),
}
