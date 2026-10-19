"""为什么说猩猩最聪明 — what each figure shows, its parts, and the narration it must make visible."""
from partkit import *
from character_parts import *   # 系列素材库 kit/：ape_parts……


SPECS = {
 "kin": dict(
    composition="草地上并排站着一个小朋友（左）和一只挥手的猩猩（右）。",
    why="小朋友用 kid() 六部分；猩猩为头、躯干（含双臂）、腿三部分；草地兜底。各形状独立一笔。",
    subjects=[("kid", H), ("ape", A), ("ground", E)],
    parts=kid_parts("kin", 320, 280, 0.85, prefix="kid_")
          + ape_parts("kin", 690, 276, 0.85, subject="ape", prefix="ape_")
          + [P("ground", "ground", "ground", ["草地外框一笔", "几丛草"], FULL)],
    reqs=[R("kin", "猩猩和我们人类有着共同的祖先，样子也长得很像", "猩猩和小朋友并排站在草地上，猩猩举起一只手挥手")]),

 "brain_cells": dict(
    composition="左边一个带沟回的大脑，中间一支箭头，右边放大镜里有许多彩色圆点（神经细胞）。",
    why="大脑外形一笔、三条沟回线、放大镜圈与镜柄各一笔；圆点为填色圆点，箭头为彩色线，都并入放大镜兜底部位。",
    subjects=[("brain", O), ("lens", O)],
    parts=[P("brain", "brain", "brain", ["大脑外形一笔", "三条沟回线", "脑桥一笔", "小脑一圈"], box("brain_cells", 100, 100, 505, 545)),
           P("lens", "lens", "lens", ["放大镜圈一圈", "镜柄一笔", "镜内连线", "箭头（彩色线）"], FULL)],
    reqs=[R("cells", "放大看一看，大脑里住着好多好多神经细胞", "放大镜里有十多个彩色小圆点，左边是一个大脑")],
    reqs_short=[R("cells", "神经细胞比狗多十多倍", "放大镜里有十多个彩色小圆点，左边是一个大脑")],
    exception="大脑先画、镜内玻璃再画、放大镜圈最后；剩余像素（含箭头）归放大镜兜底。"),

 "ant_fish": dict(
    composition="侧面蹲姿的猩猩（左）把一根细树枝伸进右边蚁巢顶部的洞口，树枝和洞口有蚂蚁。",
    why="猩猩分头、身体（含手臂和腿）两部分；蚁巢一笔、树枝为木色细线、蚂蚁为小圆点；草地兜底。",
    subjects=[("ape", A), ("mound", O), ("ground", E)],
    parts=[P("ape_head", "ape", "head", ["耳朵一圈", "头部外形一笔", "眼眶一圈", "吻部一圈", "眼睛", "眉毛", "鼻头", "嘴线", "头顶毛发两笔"], box("ant_fish", 310, 10, 495, 155)),
           P("ape_body", "ape", "torso", ["远侧手臂一笔（手扶地）", "身体外形一笔", "颈肩一笔", "背部鬃毛两笔", "折叠的膝盖一笔", "脚一圈", "近侧手臂一笔", "拿树枝的手一圈"], box("ant_fish", 170, 128, 512, 340)),
           P("mound", "mound", "mound", ["蚁巢外形一笔", "洞口线", "树枝一笔", "蚂蚁"], box("ant_fish", 470, 270, 645, 340)),
           P("ground", "ground", "ground", ["草地外框一笔", "几丛草"], FULL)],
    reqs=[R("stick_in_hole", "会折断树枝和草茎，插进蚂蚁洞里", "一根细树枝从猩猩手里伸进蚁巢顶部的洞口"),
          R("ants", "等蚂蚁爬上小棍", "树枝上和蚁巢边上看得见小蚂蚁")],
    reqs_short=[R("stick_in_hole", "插进蚂蚁洞里，钓蚂蚁吃", "一根细树枝从猩猩手里伸进蚁巢顶部的洞口"),
                R("ants", "钓蚂蚁吃", "树枝上和蚁巢边上看得见小蚂蚁")],
    exception="猩猩先画（头在身体之前声明），蚁巢和树枝后画盖在地面之上。"),

 "faces": dict(
    composition="三张圆脸从左到右：微笑、瞪眉撇嘴、垂眉瘪嘴。",
    why="每张脸为脸圈、嘴圈、眼睛、眉线、嘴线几笔，三张互不重叠。",
    subjects=[("happy", O), ("angry", O), ("sad", O)],
    parts=[P("happy", "happy", "face", ["脸圈一圈", "嘴圈一圈", "两只眼睛", "两道眉", "微笑线"], box("faces", 0, 0, 334, 360)),
           P("angry", "angry", "face", ["脸圈一圈", "嘴圈一圈", "两只眼睛", "两道斜眉", "撇嘴线"], box("faces", 334, 0, 667, 360)),
           P("sad", "sad", "face", ["脸圈一圈", "嘴圈一圈", "两只眼睛", "两道垂眉", "瘪嘴线"], box("faces", 667, 0, 1000, 360))],
    reqs=[R("expressions", "高兴、生气、难过，全写在脸上", "三张圆脸从左到右是微笑、瞪眉撇嘴、垂眉瘪嘴")]),

 "console": dict(
    composition="左边一只生气的猩猩（头顶冒热气），右边一只难过表情的猩猩把手臂搭到它的肩上。",
    why="两只猩猩各分头、躯干（含双臂）、腿三部分；热气为彩色波浪线并入左头部部位；草地兜底。",
    subjects=[("angry_ape", A), ("friend_ape", A), ("ground", E)],
    parts=ape_parts("console", 400, 306, 0.8, subject="angry_ape", prefix="angry_")
          + ape_parts("console", 690, 306, 0.8, subject="friend_ape", prefix="friend_")
          + [P("ground", "ground", "ground", ["草地外框一笔"], FULL)],
    reqs=[R("hand_on_shoulder", "同伴就把手搭在它的肩上", "右边猩猩的手臂伸到左边猩猩的肩上，左边猩猩头上有生气的热气")],
    reqs_short=[R("hand_on_shoulder", "会安慰发脾气的朋友", "右边猩猩的手臂伸到左边猩猩的肩上，左边猩猩头上有生气的热气")],
    exception="先生气猩猩、后搭肩猩猩（其手臂盖在对方肩上）；头部先声明以拥有热气区域。"),

 "learn_eat": dict(
    composition="猩猩坐在桌子后面举着勺子，桌上有一碗饭和一个勺子。",
    why="猩猩三部分；勺子为金属色线和椭圆；桌面直边矩形；碗一圈加饭粒圆点。",
    subjects=[("ape", A), ("spoon", O), ("table", O), ("bowl", O)],
    parts=[P("ape_head", "ape", "head", ["耳朵一圈", "头部一圈", "脸庞一圈", "眼睛", "嘴巴"], box("learn_eat", 240, 20, 400, 172)),
           P("ape_torso", "ape", "torso", ["两只手臂各一笔", "身体外形一笔", "肚皮一圈"], box("learn_eat", 220, 148, 448, 362)),
           P("ape_legs", "ape", "legs", ["两条腿各一笔", "两只脚各一圈"], box("learn_eat", 270, 320, 390, 480)),
           P("spoon", "spoon", "spoon", ["勺柄一笔", "勺头一圈"], box("learn_eat", 400, 100, 452, 172)),
           P("table", "table", "table", ["桌面矩形一笔"], box("learn_eat", 150, 378, 850, 550)),
           P("bowl", "bowl", "bowl", ["碗一圈", "饭粒", "桌上勺子一笔"], FULL)],
    reqs=[R("spoon_eat", "用餐具吃饭", "猩猩手里举着金属勺子，桌上有盛着饭的碗")],
    exception="猩猩先画、勺子随后、桌面盖住猩猩下半身、碗最后。"),

 "four_apes": dict(
    composition="四只高矮毛色不同的类人猿并排站在草地上（黄猩猩、黑猩猩、侏黑猩猩、大猩猩）。",
    why="每只猩猩为头、躯干、腿三部分，用不同毛色参数复用同一函数；草地兜底。",
    subjects=[("orang", A), ("chimp", A), ("bonobo", A), ("gorilla", A), ("ground", E)],
    parts=ape_parts("four_apes", 200, 580 - 334 * 0.78, 0.78, subject="orang", prefix="orang_")
          + ape_parts("four_apes", 500, 580 - 334 * 0.74, 0.74, subject="chimp", prefix="chimp_")
          + ape_parts("four_apes", 780, 580 - 334 * 0.70, 0.70, subject="bonobo", prefix="bonobo_")
          + ape_parts("four_apes", 1060, 580 - 334 * 0.90, 0.90, subject="gorilla", prefix="gorilla_")
          + [P("ground", "ground", "ground", ["草地外框一笔", "几丛草"], FULL)],
    reqs=[R("four", "世界上一共有四种类人猿", "四只高矮毛色不同的类人猿并排站在草地上")]),

 "fossil": dict(
    composition="山坡剖面（土层）上有个山洞口，洞口旁嵌着头骨和牙齿化石；右边一把铁锹、左边一把刷子。",
    why="土层直边矩形、洞口一笔、头骨两笔加牙齿短线、铲子和刷子各两笔；顶部草地兜底。",
    subjects=[("hill", E), ("skull", O), ("tools", O)],
    parts=[P("skull", "skull", "skull", ["头骨一圈", "下颌一笔", "眼窝一圈", "牙齿短线"], box("fossil", 468, 418, 582, 538)),
           P("hill", "hill", "hill", ["土层矩形一笔", "洞口一笔", "几丛草"], box("fossil", 40, 268, 960, 562)),
           P("tools", "tools", "tools", ["铲柄一笔", "铲头一笔", "刷柄一笔", "刷毛一笔", "闪光"], FULL)],
    reqs=[R("bones", "还挖到过它们的化石呢", "山坡剖面上有头骨和牙齿化石，旁边有铲子和刷子")],
    exception="化石嵌在土层里，头骨部位先声明以拥有洞口内的像素；土层和工具后画。"),

 "friend": dict(
    composition="猩猩站在草地上挥手，头旁一颗爱心，左边有闪光。",
    why="猩猩三部分；爱心一笔、闪光两笔；草地兜底。",
    subjects=[("ape", A), ("heart", O), ("ground", E)],
    parts=ape_parts("friend", 430, 560 - 334 * 0.85, 0.85, subject="ape")
          + [P("heart", "heart", "heart", ["爱心一笔", "闪光两笔"], box("friend", 190, 60, 750, 262)),
             P("ground", "ground", "ground", ["草地外框一笔"], FULL)],
    reqs=[R("friend", "大多成了珍稀的保护动物", "猩猩挥着手，头旁有一颗爱心")],
    exception="猩猩先画、爱心后画（不重叠）。"),

 "sanlian": dict(
    composition="爱心、硬币、星星三个小图标一排。",
    why="三个图标各一笔（轮廓），互不重叠。",
    subjects=[("icons", O)],
    parts=[P("icons", "icons", "icons", ["爱心一圈", "硬币两圈", "星星一笔"], FULL)],
    reqs=[R("sanlian", "想看更多这样的视频，记得一键三连哦", "爱心、硬币、星星三个图标并排")],
    reqs_short=[R("sanlian", "想看更多，记得一键三连哦", "爱心、硬币、星星三个图标并排")]),
}
