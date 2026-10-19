"""Single source of truth for each illustration: plan text, semantic parts (with polygons), narrative requirements.
Polygons are normalized to the figure canvas; bear parts are authored in the bear's local (side view, facing right)
frame and transformed with the same pose used in draw_figures, so the regions follow the actual anatomy."""
import math

SIZES = {"kid": (520, 720), "jacket": (380, 400), "bear_side": (900, 560), "fur_layers": (900, 520), "sun_hair": (900, 560),
         "fat_layers": (720, 560), "bear_head": (520, 460), "paw": (560, 540), "bear_swim": (900, 480), "bear_hunt": (1000, 580),
         "bear_snow": (900, 600), "ice_melt": (900, 560)}


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


PIVOT = (175, -70)
COOL = [[180, 215, 0.02, 0.85]]   # ice / water / snow hue band; bear cream (~43°) and ink are never excluded


def rot_about(pts, a):
    ca, sa = math.cos(a), math.sin(a)
    return [(PIVOT[0] + (x - PIVOT[0]) * ca - (y - PIVOT[1]) * sa, PIVOT[1] + (x - PIVOT[0]) * sa + (y - PIVOT[1]) * ca) for x, y in pts]


def bear_parts(name, cx, cy, s=1.0, head_rot=0.0, crouch=0.0, legs=True, body_bottom=78):
    g = lambda pts: pose(name, pts, cx, cy, s, 0)
    ly = 165 - 45 * crouch
    out = [P("head", "bear", "head", ["小耳朵一笔", "长长的头部外形一笔", "眼睛", "黑鼻子", "嘴线"], g(rot_about(rect(150, -140, 400, -5), head_rot)), exclude_hsv=COOL),
           P("body", "bear", "torso", ["短尾巴一圈", "身体外形一笔"], g(rect(-285, -150, 215, body_bottom)), exclude_hsv=COOL)]
    if legs:
        out.append(P("legs", "bear", "legs", ["远侧前后腿各一笔", "近侧前后腿各一笔", "四只脚掌各一圈"], g(rect(-240, -10, 240, ly + 35)), exclude_hsv=COOL))
    return out


def R(i, q, o): return {"id": i, "narration_quote": q, "observable": o}


H, A, O, E = "human", "animal", "object", "environment"
BEAR_EXC = "北极熊按解剖顺序 头→身体→腿 绘制（头在画面右侧），作为背景的冰/雪/水最后补上"
SPECS = {
 "kid": dict(
    composition="正面站立的小朋友：红色毛线帽带绒球、圆脸红脸蛋、冻得嘴巴圆圆的；黄色围巾一端垂下；橙色鼓鼓的羽绒服，两只红手套；灰裤子和棕色靴子。",
    why="人物拆为头（含帽子）、颈部（被围巾遮住）、躯干（羽绒服）、画面左臂、右臂、下半身六部分，各部分外形独立一笔。",
    subjects=[("kid", H)],
    parts=[P("head", "kid", "head", ["脸部圆形一笔", "两只眼睛", "两团脸蛋", "嘴巴一圈", "帽子外形一笔", "绒球一圈"], norm("kid", rect(140, 40, 380, 282))),
           P("neck", "kid", "neck", ["围巾外形一笔（颈部被围巾遮住）", "垂下的围巾端一笔"],
             norm("kid", [(150, 280), (370, 280), (370, 345), (342, 345), (342, 450), (288, 450), (288, 345), (150, 345)])),
           P("torso", "kid", "torso", ["羽绒服外形一笔", "两道绗线", "拉链线"], norm("kid", [(150, 318), (370, 318), (392, 562), (128, 562)])),
           P("left_arm", "kid", "left_arm", ["画面左侧袖子一笔", "左手套一圈"], norm("kid", rect(0, 300, 178, 600))),
           P("right_arm", "kid", "right_arm", ["画面右侧袖子一笔", "右手套一圈"], norm("kid", rect(342, 300, 520, 600))),
           P("lower_body", "kid", "lower_body", ["两条裤腿各一笔", "两只靴子各一圈"], FULL)],
    reqs=[R("coat", "小朋友们都穿上了厚厚的棉衣和羽绒服", "小朋友穿着鼓鼓的羽绒服，戴帽子、围巾和手套"),
          R("cold", "寒冷的冬天到了", "帽子、围巾、手套齐全，一副怕冷的样子")]),
 "bear_side": dict(
    composition="侧面站在浮冰上的北极熊，头朝右：小耳朵、长脖子、长头、黑鼻子，四条粗壮的腿，短尾巴；脚下一块淡蓝色浮冰。",
    why="北极熊拆为头、身体（含尾巴）、腿三部分，浮冰一部分；各形状外形独立一笔。",
    subjects=[("bear", A), ("ice", E)],
    parts=bear_parts("bear_side", 430, 300) + [P("ice", "ice", "ice_floe", ["浮冰外形一笔"], FULL)],
    reqs=[R("bear", "北极熊是熊家族里个子最大的一种", "一只完整、体型硕大的北极熊"),
          R("ice", "家就在北冰洋的海岸和海冰上", "北极熊脚下是一块浮冰")],
    exception=BEAR_EXC),
 "jacket": dict(
    composition="一件橙色鼓鼓的羽绒服，有绗线分格和拉链线。",
    why="左袖、右袖、衣身三部分，每件外形一笔，绗线各一笔。",
    subjects=[("jacket", O)],
    parts=[P("left_sleeve", "jacket", "left_sleeve", ["左袖外形一笔"], rect(0, 0, 0.27, 1)),
           P("right_sleeve", "jacket", "right_sleeve", ["右袖外形一笔"], rect(0.73, 0, 1, 1)),
           P("coat_body", "jacket", "coat_body", ["衣身外形一笔", "三道绗线", "拉链线"], FULL)],
    reqs=[R("jacket", "就像穿了一件羽绒服", "画面是一件可辨认的羽绒服")],
    exception="先画两只袖子，再画压在袖子上的衣身"),
 "fur_layers": dict(
    composition="皮毛横切面：最下面一条黑色皮肤；紧贴皮肤一层卷卷的奶白绒毛；上面竖着一根根长长的针毛，针毛之间飘着小空气泡。",
    why="针毛（含空气泡）、绒毛、皮肤三层，从上到下；每根针毛一笔、每个卷一笔、每个气泡一圈。",
    subjects=[("fur", A)],
    parts=[P("guard_hairs", "fur", "guard_hairs", ["15根长针毛各一笔", "10个空气泡各一圈"], rect(0, 0, 1, 0.635)),
           P("underfur", "fur", "underfur", ["绒毛层上缘波浪一笔", "一个个小卷各一笔"], rect(0, 0, 1, 0.78)),
           P("skin", "fur", "skin", ["皮肤外框一笔"], FULL)],
    reqs=[R("two", "贴着皮肤的是一层软软的绒毛，外面再盖一层长长的针毛", "紧贴皮肤一层短而卷的绒毛，上面是一根根长针毛"),
          R("air", "毛里藏着空气", "针毛之间有一个个小空气泡")]),
 "sun_hair": dict(
    composition="左上角黄色太阳，橙色光线射向一根放大的透明空心毛（浅色管子，中间一条更细的空芯）和下方的黑色皮肤；皮肤上方三个红色波浪箭头向下表示热量被吸进去。",
    why="太阳、毛、光线与热量箭头、皮肤四部分；每个形状独立一笔。",
    subjects=[("sun", E), ("hair", O), ("rays", O), ("skin", O)],
    parts=[P("sun", "sun", "sun", ["太阳圆圈一笔", "八道短光芒"], rect(0, 0, 0.27, 0.42)),
           P("hair", "hair", "hair", ["毛外形一笔", "空芯一笔"], rect(0.3, 0.28, 1, 0.56)),
           P("rays", "rays", "light_and_heat", ["三道光线与箭头", "三个红色热量箭头"], rect(0, 0, 1, 0.76)),
           P("skin", "skin", "skin", ["黑皮肤外框一笔"], FULL)],
    reqs=[R("clear", "北极熊的毛其实是透明的", "放大的毛是浅淡透明的管子，中间有空芯"),
          R("black", "毛底下的皮肤却是黑色的，能把太阳的热量吸进来", "下方是黑色皮肤，有光线照到并有指向皮肤的红色热量箭头")]),
 "fat_layers": dict(
    composition="身体横切面，从上到下：奶白毛层、黑色皮肤、厚厚的黄色脂肪层（右侧一个量尺括号标出厚度）、粉色身体；身体里三支红色热量箭头向上碰到脂肪又折回身体。",
    why="毛、皮肤、脂肪（含量尺）、身体（含热量箭头）四层，从上到下各一笔外框。",
    subjects=[("section", A)],
    parts=[P("fur", "section", "fur_layer", ["毛层外框", "一根根短毛"], rect(0, 0, 1, 0.243)),
           P("skin", "section", "skin_layer", ["黑皮肤外框"], rect(0, 0.243, 1, 0.302)),
           P("fat", "section", "fat_layer", ["脂肪层外框", "脂肪小格", "量尺括号三笔"], rect(0, 0.302, 1, 0.646)),
           P("body", "section", "body_layer", ["身体外框", "三支折回的热量箭头"], FULL)],
    reqs=[R("fat", "皮肤下面一层厚厚的脂肪", "皮肤下面有一层明显很厚的黄色脂肪"),
          R("lock", "把热量锁在身体里", "红色热量箭头碰到脂肪后折回身体")]),
 "bear_head": dict(
    composition="北极熊头部正面：两只小小的圆耳朵、宽圆的头、一对小黑眼睛、浅色口鼻部上一个大黑鼻子和嘴线。",
    why="左耳、右耳、头三部分；耳朵各一圈，头外形一笔，五官各自一笔。",
    subjects=[("bear", A)],
    parts=[P("left_ear", "bear", "left_ear", ["左耳外圈"], circle("bear_head", 150, 112, 58)),
           P("right_ear", "bear", "right_ear", ["右耳外圈"], circle("bear_head", 370, 112, 58)),
           P("head", "bear", "head", ["头外形一笔", "两只眼睛", "口鼻部一圈", "黑鼻子", "嘴线三笔"], FULL)],
    reqs=[R("ears", "耳朵又短又小", "耳朵相对于头很小")]),
 "paw": dict(
    composition="北极熊脚掌底面：奶白色毛茸茸的脚掌上，五个小黑趾垫排成弧形，中间一个大黑掌垫，周围有一簇簇短毛。",
    why="脚趾区（趾垫）与脚掌（掌垫和短毛）两部分；每个垫一圈，每簇毛两笔。",
    subjects=[("paw", A)],
    parts=[P("toes", "paw", "toe_pads", ["脚掌上缘", "五个趾垫各一圈"], rect(0, 0, 1, 0.5)),
           P("sole", "paw", "sole", ["脚掌外形其余部分", "大掌垫一笔", "短毛各两笔"], FULL)],
    reqs=[R("hairy", "它的脚掌上也长着毛", "脚掌大部分是毛，黑色的垫子很小")]),
 "bear_swim": dict(
    composition="北极熊在海里游泳：只露出头和背，头朝右微微抬起；下方是淡蓝色海水和几道小波浪。",
    why="头、露出水面的背、海水三部分；各形状独立一笔，波浪各一笔。",
    subjects=[("bear", A), ("sea", E)],
    parts=bear_parts("bear_swim", 380, 300, head_rot=-0.14, crouch=1.0, legs=False, body_bottom=4) + [P("water", "sea", "sea", ["海面波浪线一笔", "五道小波浪"], FULL)],
    reqs=[R("swim", "还能在冰冷的海水里游泳", "北极熊身体浸在海水中，只露出头和背")],
    exception=BEAR_EXC),
 "bear_hunt": dict(
    composition="冰面上，北极熊蹲在左侧，低着头盯着右侧的冰窟窿；冰窟窿里一只灰色海豹探出脑袋。",
    why="北极熊头、身体、腿，海豹，冰面与冰窟窿五部分；各形状独立一笔。",
    subjects=[("bear", A), ("seal", A), ("ice", E)],
    parts=bear_parts("bear_hunt", 330, 243, head_rot=0.35, crouch=1.0)
          + [P("seal_left", "seal", "head_left", ["海豹头左半外形", "左眼", "左侧三根胡须"], norm("bear_hunt", [(730, 446), (728, 375), (755, 333), (790, 324), (790, 446)])),
             P("seal_right", "seal", "head_right", ["海豹头右半外形", "右眼", "鼻子", "右侧三根胡须"], norm("bear_hunt", [(790, 324), (825, 333), (852, 375), (850, 446), (790, 446)]))]
          + [P("ice", "ice", "ice_and_hole", ["冰面外框", "冰窟窿一圈"], FULL)],
    reqs=[R("hole", "海豹要从冰窟窿里探出头来换气", "冰面上有一个冰窟窿，海豹从里面探出头"),
          R("wait", "北极熊就蹲在旁边耐心地等", "北极熊在冰窟窿旁低头守着")],
    exception="北极熊按头→身体→腿绘制，再画右侧冰窟窿里的海豹，冰面最后"),
 "bear_snow": dict(
    composition="雪花飘落，北极熊独自站在雪地上，头朝右；身后雪地上留着几个小脚印。",
    why="雪花、北极熊头、身体、腿、雪地五部分；每片雪花三笔。",
    subjects=[("snow", E), ("bear", A), ("ground", E)],
    parts=[P("flakes", "snow", "snowflakes", ["八片雪花，每片三笔"], rect(0, 0, 1, 0.235))] + bear_parts("bear_snow", 430, 300)
          + [P("ground", "ground", "snow_ground", ["雪地外框", "三个脚印"], FULL)],
    reqs=[R("alone", "喜欢独来独往", "画面里只有一只北极熊"),
          R("winter", "照样在冰天雪地里找吃的", "北极熊站在雪地里，天上飘着雪花")],
    exception="先画天上的雪花，再按头→身体→腿画北极熊，雪地最后"),
 "ice_melt": dict(
    composition="右上角太阳；一大片海水里只剩一块小小的浮冰，一只小小的北极熊站在上面；旁边漂着两块碎冰。",
    why="太阳、北极熊头、北极熊身体、海水与浮冰四部分。",
    subjects=[("sun", E), ("bear", A), ("sea", E)],
    parts=[P("sun", "sun", "sun", ["太阳圆圈", "八道光芒"], rect(0.7, 0, 1, 0.42))]
          + [P("bear_head", "bear", "head", ["头、耳朵、眼睛、鼻子"], pose("ice_melt", rot_about(rect(150, -140, 400, -5), 0), 452, 270, 0.36, 0), exclude_hsv=COOL),
             P("bear_body", "bear", "body_and_legs", ["身体、尾巴、四条腿"], pose("ice_melt", rect(-290, -160, 240, 200), 452, 270, 0.36, 0), exclude_hsv=COOL)]
          + [P("sea", "sea", "sea_and_ice", ["海面波浪线", "小浮冰", "两块碎冰", "三道波浪"], FULL)],
    reqs=[R("melt", "海冰越来越少，它们的家正在变小", "北极熊站在一块很小的浮冰上，四周都是海水")],
    exception="先画太阳，再画北极熊，海水与浮冰最后"),
}
