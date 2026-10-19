"""Single source of truth for each illustration: plan text, semantic parts (with polygons), narrative requirements.
Polygons are normalized to the figure canvas; gecko parts are authored in the gecko's local (facing-up) frame
and transformed with the same pose used in draw_figures, so the regions follow the actual anatomy."""
import math

SIZES = {"gecko_wait": (800, 980), "mosquito": (380, 360), "gecko_catch": (1000, 700), "suction": (420, 420),
         "foot": (820, 760), "setae": (620, 620), "spatula": (640, 640), "force": (1000, 440), "ceiling": (960, 560),
         "peel": (1000, 500), "tape": (560, 460), "robot": (600, 600)}


def clip(v): return float(min(1, max(0, v)))


def norm(name, pts):
    w, h = SIZES[name]
    return [[clip(x / (w - 1)), clip(y / (h - 1))] for x, y in pts]


def rect(x0, y0, x1, y1): return [[x0, y0], [x1, y0], [x1, y1], [x0, y1]]


FULL = rect(0, 0, 1, 1)


def pose(name, local, cx, cy, s, rot):
    ca, sa = math.cos(rot), math.sin(rot)
    return norm(name, [(cx + s * (x * ca - y * sa), cy + s * (x * sa + y * ca)) for x, y in local])


def circle(name, cx, cy, r, n=24):
    return norm(name, [(cx + r * math.cos(t), cy + r * math.sin(t)) for t in [2 * math.pi * i / n for i in range(n)]])


def P(pid, subj, role, strokes, polygon, **extra):
    d = {"id": pid, "subject": subj, "role": role, "stroke_groups": strokes, "polygon": polygon}
    d.update(extra)
    return d


def gecko_parts(name, cx, cy, s, rot, prefix=""):
    g = lambda pts: pose(name, pts, cx, cy, s, rot)
    return [
        P(prefix + "head", "gecko", "head", ["头部外形一笔", "左眼圆圈", "右眼圆圈", "嘴线"], g(rect(-100, -320, 100, -140))),
        P(prefix + "body", "gecko", "torso", ["身体外形一笔"], g(rect(-62, -140, 62, 112))),
        P(prefix + "front_legs", "gecko", "front_legs", ["左前腿外形", "左前脚五个脚趾与趾垫", "右前腿外形", "右前脚五个脚趾与趾垫"],
          g(rect(-240, -280, 240, -40))),
        P(prefix + "back_legs", "gecko", "back_legs", ["左后腿外形", "左后脚五个脚趾与趾垫", "右后腿外形", "右后脚五个脚趾与趾垫"],
          g(rect(-240, -40, 240, 215)), exclude_polygons=[g(rect(-52, 92, 52, 215))]),
        P(prefix + "tail", "gecko", "tail", ["尾巴外形一笔，从身体后端到卷起的尾尖"], g(rect(-160, 92, 160, 440))),
    ]


def R(i, q, o): return {"id": i, "narration_quote": q, "observable": o}


A, O, E = "animal", "object", "environment"
SPECS = {
 "gecko_wait": dict(
    composition="墙角（左侧与底部两条浅砖色墙线）里一只俯视的小壁虎，头朝右上，圆圆的黄眼睛，四条腿张开、脚趾末端有圆趾垫，尾巴卷曲；四周留白。",
    why="壁虎拆为头、身体、前腿、后腿、尾巴五部分，每部分外形独立一笔；墙线两笔。线条量适合约10秒口播。",
    subjects=[("gecko", A), ("wall", E)],
    parts=gecko_parts("gecko_wait", 420, 450, 1.05, 0.3) + [P("wall", "wall", "wall_corner", ["左侧竖墙线", "底部横墙线"], FULL)],
    reqs=[R("gecko", "一只小壁虎静静地趴在墙角", "画面里有一只完整的壁虎，位于两条墙线围成的墙角内"),
          R("eyes", "瞪着圆圆的眼睛", "壁虎有两只明显的圆形黄色大眼睛")],
    exception="壁虎按头→身体→前腿→后腿→尾巴的解剖顺序绘制；作为背景的墙角线最后补上"),
 "mosquito": dict(
    composition="俯视的一只蚊子：细长口器、两片浅灰翅膀、六条细腿，腹部是吸饱血的红色。",
    why="头部（头、触角、口器）、翅膀、身体、腿四部分；腿每条一笔，翅膀各一笔。",
    subjects=[("mosquito", A)],
    parts=[P("head", "mosquito", "head", ["头部圆圈", "口器一笔", "两根触角"], rect(0.42, 0, 0.58, 0.43)),
           P("wings", "mosquito", "wings", ["左翅外形", "右翅外形"], rect(0, 0, 1, 0.49), exclude_polygons=[rect(0.43, 0.43, 0.57, 0.49)]),
           P("body", "mosquito", "torso", ["胸部圆圈", "红色腹部外形"], rect(0.40, 0.43, 0.60, 1)),
           P("legs", "mosquito", "legs", ["左侧三条腿", "右侧三条腿"], FULL)],
    reqs=[R("blood", "一只吸饱了血的蚊子", "蚊子腹部为醒目的红色、鼓起")]),
 "gecko_catch": dict(
    composition="壁虎斜向右上猛冲，身后左下有四条速度线；嘴边叼着一只倒过来的小蚊子（翅膀和红肚子露在嘴外）。",
    why="蚊子单独一部分，壁虎五部分，速度线最后；各部分外形独立一笔。",
    subjects=[("gecko", A), ("prey", A), ("speed", E)],
    parts=[P("prey_left", "prey", "left_wing_side", ["左翅", "左侧细腿", "半边腹部"], pose("gecko_catch", [(-90, -90), (0, -90), (0, 90), (-90, 90)], 812, 222, 1, 0.95)),
           P("prey_right", "prey", "right_wing_side", ["右翅", "右侧细腿", "另半边腹部与口器"], circle("gecko_catch", 812, 222, 80))]
          + [dict(p, exclude_polygons=p.get("exclude_polygons", []) + [circle("gecko_catch", 812, 222, 80)]) for p in gecko_parts("gecko_catch", 520, 380, 1.0, 0.95)]
          + [P("speed_lines", "speed", "motion_lines", ["四条速度线，每条一笔"], FULL)],
    reqs=[R("dash", "像闪电一样一冲", "壁虎身体斜向前冲，身后有速度线"),
          R("eat", "就把蚊子吞进了肚子", "蚊子就在壁虎嘴边、被叼住")],
    exception="先画被叼住的蚊子（视觉焦点在右上），再按壁虎解剖顺序，最后画背景速度线"),
 "suction": dict(
    composition="一个红色吸盘挂钩：上方黑色挂钩，下方半球形吸盘与扁平边缘。",
    why="挂钩一笔，吸盘拱顶和底边各一笔。",
    subjects=[("hook", O)],
    parts=[P("hook", "hook", "hook", ["挂钩弯线一笔"], rect(0.42, 0, 0.7, 0.37)),
           P("cup", "hook", "suction_cup", ["拱形吸盘外形", "底部边缘"], FULL)],
    reqs=[R("cup", "壁虎的脚上长着吸盘", "画面是一个可辨认的吸盘")]),
 "foot": dict(
    composition="壁虎一只脚的底面特写：五个脚趾从掌心向上张开，脚趾末端变宽成趾垫，趾垫上一道道弧形褶皱，趾尖有小爪；下方绿色腿伸出画外。",
    why="脚趾（含褶皱、小爪）、掌心、腿三部分；每个脚趾外形一笔，每道褶皱一笔。",
    subjects=[("foot", A)],
    parts=[P("toes", "foot", "toes", ["五个脚趾外形各一笔", "趾尖小爪各一笔", "每个趾垫上六道褶皱各一笔"], rect(0, 0, 1, 0.64)),
           P("palm", "foot", "palm", ["掌心外形一笔"], rect(0.25, 0.6, 0.75, 0.87)),
           P("leg", "foot", "leg", ["腿的两条边线"], FULL)],
    reqs=[R("folds", "而是一道道褶皱", "脚趾趾垫上有成排的弧形褶皱线"),
          R("nocup", "壁虎的脚趾上并没有吸盘", "脚趾上没有圆形吸盘结构")]),
 "setae": dict(
    composition="放大镜圆框里：下方一道奶黄色褶皱，上面竖着密密的一排细毛（刚毛）；右下是放大镜手柄。",
    why="镜框一笔，手柄一笔，褶皱一笔，19根细毛各一笔。",
    subjects=[("lens", O), ("ridge", A)],
    parts=[P("rim", "lens", "magnifier_rim", ["镜框圆圈一笔"], FULL, exclude_polygons=[circle("setae", 310, 300, 240), rect(0.74, 0.74, 1, 1)]),
           P("hairs", "ridge", "setae", ["19根刚毛，每根一笔"], circle("setae", 310, 300, 240), exclude_polygons=[norm("setae", [(90, 410), (530, 410), (530, 560), (90, 560)])]),
           P("ridge", "ridge", "ridge", ["褶皱外形一笔"], circle("setae", 310, 300, 240)),
           P("handle", "lens", "handle", ["手柄外形一笔"], FULL)],
    reqs=[R("hairs", "上面长满了几十万根细细的刚毛", "放大镜里一道褶皱上竖着许多细毛")],
    exception="先画放大镜框，再画框内的刚毛与褶皱，手柄最后"),
 "spatula": dict(
    composition="一根刚毛：下方一根竖直的茎，顶端分成五枝，每枝再分成四根更细的小枝，末端是红色的小扁片。",
    why="茎一笔、五根分枝各一笔、二十根小枝各一笔、红色小扁片各一圈。",
    subjects=[("seta", A)],
    parts=[P("stalk", "seta", "stalk", ["茎的外形一笔"], rect(0, 0.53, 1, 1)),
           P("branches", "seta", "branches", ["五根主分枝", "二十根细小分叉", "末端小扁片"], FULL)],
    reqs=[R("split", "又分出成百上千个更细的小分叉", "一根刚毛末端一分再分，形成许多细小分叉")],
    exception="从茎向上生长到分叉，与“末端又分出”的讲解顺序一致"),
 "force": dict(
    composition="下方一段砖色墙面，墙里有一排小圆圈表示分子；上方八根细毛末端的扁片几乎贴着墙面，每个扁片旁一个指向墙面的红色小箭头。",
    why="细毛与扁片、红箭头、墙面三部分；每根细毛一笔、每个扁片一圈、每个箭头三笔、墙面与每个分子各一笔。",
    subjects=[("tips", O), ("arrows", O), ("wall", E)],
    parts=[P("tips", "tips", "spatula_tips", ["八根细毛各一笔", "八个扁片各一圈"], rect(0, 0, 1, 0.74),
             exclude_polygons=[rect((x + 34) / 999, 0.66, (x + 60) / 999, 0.74) for x in range(110, 960, 110)]),
           P("arrows", "arrows", "attraction_arrows", ["八个红色小箭头，竖线与两笔箭头"], rect(0, 0, 1, 0.745)),
           P("wall", "wall", "wall_surface", ["墙面上缘与外框", "墙内分子小圆圈各一笔"], FULL)],
    reqs=[R("close", "这些小分叉能紧紧贴近墙面", "扁片与墙面之间只有极窄的缝隙"),
          R("attract", "会产生一种微弱的吸引力", "扁片与墙之间有指向墙面的红色小箭头")]),
 "ceiling": dict(
    composition="侧视：上方一条砖色天花板，壁虎背朝下倒挂在天花板下，四只脚的扁平趾垫贴住天花板；头在左、尾巴在右向下卷。",
    why="天花板、四条腿、头、身体、尾巴五部分，各自外形一笔。",
    subjects=[("ceiling", E), ("gecko", A)],
    parts=[P("ceiling", "ceiling", "ceiling", ["天花板外框"], rect(0, 0, 1, 0.168)),
           P("legs", "gecko", "legs", ["四条腿与贴住天花板的趾垫，各一笔"], rect(0.28, 0.16, 0.7, 0.305)),
           P("head", "gecko", "head", ["头部外形", "眼睛", "嘴线"], rect(0, 0.16, 0.325, 1)),
           P("body", "gecko", "torso", ["身体外形一笔"], rect(0.325, 0.16, 0.68, 1)),
           P("tail", "gecko", "tail", ["向下卷的尾巴一笔"], FULL)],
    reqs=[R("hang", "甚至倒挂在天花板上", "壁虎在天花板下方倒挂，脚掌贴住天花板")]),
 "peel": dict(
    composition="侧视：下方砖色墙面，一根脚趾的左半段平贴墙面，右半段从趾尖向上卷起离开墙面；右侧一支红色弯箭头表示向上卷。",
    why="脚趾一笔外形加四道小褶皱，箭头三笔，墙面一笔。",
    subjects=[("toe", O), ("arrow", O), ("wall", E)],
    parts=[P("toe", "toe", "toe", ["脚趾外形一笔", "贴墙处四道小褶皱"], rect(0, 0, 0.71, 0.755)),
           P("arrow", "arrow", "curl_arrow", ["弯箭头弧线", "箭头两笔"], rect(0.71, 0, 1, 0.75)),
           P("wall", "wall", "wall_surface", ["墙面外框"], FULL)],
    reqs=[R("curl", "壁虎把脚趾从尖端往回一卷", "脚趾尖端向上卷离墙面，根部仍贴着墙"),
          R("lift", "轻轻松松就抬起了脚", "有表示向上卷起的箭头")]),
 "tape": dict(
    composition="一卷暖黄色胶带，右下拉出一段胶带条，条上印着小小的壁虎脚印纹样。",
    why="胶带卷外圈与内圈各一笔，胶带条一笔，三个脚印各三笔。",
    subjects=[("tape", O)],
    parts=[P("roll", "tape", "roll", ["外圈", "内圈"], circle("tape", 200, 210, 160)),
           P("strip", "tape", "strip", ["胶带条外形", "三个小脚印"], FULL)],
    reqs=[R("tape", "不留痕迹的壁虎胶带", "画面是一卷胶带，拉出的胶带条上有壁虎脚印纹样")]),
 "robot": dict(
    composition="正面的爬墙机器人：灰色身体、两只黄眼睛和笑脸，四条机械腿伸向四角，末端是红色的大脚垫。",
    why="身体（含眼睛和嘴）与四条腿（含脚垫）两部分；每个形状一笔。",
    subjects=[("robot", O)],
    parts=[P("robot_body", "robot", "body", ["身体外形", "两只眼睛", "嘴线"], rect(0.33, 0.27, 0.67, 0.78)),
           P("robot_legs", "robot", "legs_and_pads", ["四条机械腿各一笔", "四个红色脚垫各一圈"], FULL)],
    reqs=[R("robot", "还造出了会爬墙的机器人", "一个有四条腿和大脚垫的机器人")],
    exception="先画机器人身体再画伸向四角的腿和脚垫"),
}
