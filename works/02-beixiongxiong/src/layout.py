import json, glob, sys
from PIL import ImageFont
sys.path.insert(0, "src"); from spec import SPECS
HAN = glob.glob('/System/Library/AssetsV2/com_apple_MobileAsset_Font8/*/AssetData/Hannotate.ttc')[0]
INK, RED, GREY, GREEN = "#2A2622", "#D2563C", "#6E6656", "#6F8A2E"

def ill(name, x, y, w, h, weight=3):
    parts = [{k: v for k, v in p.items() if k in ("id", "polygon", "exclude_polygons")} for p in SPECS[name]["parts"]]
    return {"type": "illustration", "source": f"inputs/figures/{name}.png", "x": x, "y": y, "width": w, "height": h,
            "weight": weight, "drawing_plan_id": name, "parts": parts}
def tw(t, size):
    f = ImageFont.truetype(HAN, size, index=2); b = f.getbbox(t); return b[2] - b[0]
def text(t, x, y, size, color=INK, center=False, weight=1):
    if center: x = int(x - tw(t, size) / 2)
    return {"type": "text", "text": t, "x": int(x), "y": int(y), "size": size, "color": color, "weight": weight}
def under(x, y, w, color="#F3D36A"): return {"type": "marker", "style": "highlight", "x": x, "y": y, "width": w, "height": 26, "color": color, "z": -1}
def G(a, b, actions, lead=.3, hold=.6): return {"start_beat": a, "end_beat": b, "lead": lead, "hold": hold, "actions": actions}

beats = json.load(open("src/beats.json"))
pages_spec = [
 ([0, 1], [G(0, 0, [ill("kid", 250, 140, 540, 748), text("冬天到了，好冷呀！", 880, 330, 84)]),
           G(1, 1, [text("小民问：", 880, 480, 72), text("北极熊为什么", 880, 590, 104, RED), text("不怕冷？", 880, 740, 104, RED)])]),
 ([2, 3], [G(2, 2, [text("熊家族里的大个子", 150, 60, 84), ill("bear_side", 200, 230, 1100, 684),
                    under(1352, 500, 300), text("两米多长", 1360, 420, 72), under(1352, 640, 300), text("一千多斤", 1360, 560, 72)]),
           G(3, 3, [text("家在北冰洋的海冰上", 1360, 720, 54, GREY)])]),
 ([4, 5], [G(4, 4, [text("秘密一：两层毛", 150, 60, 84), ill("fur_layers", 130, 200, 990, 572),
                    text("长长的针毛", 1170, 330, 60), text("软软的绒毛", 1170, 560, 60)]),
           G(5, 5, [text("毛里藏着空气", 1170, 440, 54, GREY), ill("jacket", 1560, 470, 266, 280), text("像羽绒服", 1693, 780, 56, RED, center=True)])]),
 ([6, 7], [G(6, 6, [text("毛是透明的，皮肤是黑的", 150, 60, 80), ill("sun_hair", 200, 200, 1170, 728), text("透明的毛", 1420, 460, 64)]),
           G(7, 7, [text("黑皮肤：吸热", 1420, 800, 64, RED)])]),
 ([8, 9], [G(8, 8, [text("秘密二：厚厚的脂肪", 150, 60, 84), ill("fat_layers", 200, 190, 936, 728), text("约10厘米", 1180, 470, 72, RED)]),
           G(9, 9, [text("像一床棉被", 1180, 620, 60), text("把热量锁住", 1180, 740, 60)])]),
 ([10, 11], [G(10, 10, [text("露在外面的少，热量跑不掉", 150, 60, 76), ill("bear_head", 170, 210, 520, 460), text("耳朵小 · 尾巴短", 430, 710, 64, center=True)]),
             G(11, 11, [ill("paw", 1000, 190, 560, 540), text("脚掌长毛：保暖又防滑", 1280, 780, 60, center=True)])]),
 ([12], [G(12, 12, [text("不怕冷，还会游泳潜水", 150, 60, 84), ill("bear_swim", 360, 260, 1200, 640)])]),
 ([13, 14], [G(13, 13, [text("守在冰窟窿旁等海豹", 150, 60, 84), ill("bear_hunt", 260, 220, 1200, 696)]),
             G(14, 14, [text("一露头，就扑上去！", 1000, 75, 64, RED)])]),
 ([15, 16], [G(15, 15, [ill("bear_snow", 130, 240, 1000, 667), text("独来独往", 1250, 380, 96)]),
             G(16, 16, [text("冬天不冬眠", 1250, 560, 96, RED)])]),
 ([17], [G(17, 17, [text("海冰越来越少", 150, 60, 84), ill("ice_melt", 200, 200, 1080, 672), text("一起保护北极熊", 1320, 560, 72, RED)])]),
 ([18], [G(18, 18, [ill("bear_side", 100, 330, 760, 473, weight=2), text("北极熊不怕冷的秘密", 900, 330, 76),
                    text("厚厚的毛", 900, 470, 80), text("厚厚的脂肪", 900, 590, 80), under(892, 790, 740),
                    text("不让热量跑掉的好身材", 900, 710, 72, RED), text("十万个为什么", 910, 840, 60, GREY)], hold=.6)]),
]
pages = []
for pb, groups in pages_spec:
    off = pb[0]
    for g in groups: g["start_beat"] -= off; g["end_beat"] -= off
    pages.append({"beats": [{"id": beats[i]["id"], "text": beats[i]["text"], "actions": []} for i in pb], "visual_groups": groups})

STHEITI = "/System/Library/Fonts/STHeiti Medium.ttc"
job = {"version": 1, "title": "十万个为什么：为什么北极熊不怕冷", "design_file": "design.json",
       "art_direction": {"record": "design/art-direction.json"},
       "drawing_plan": "design/drawing-plan.json", "drawing_review": "design/drawing-review.json",
       "canvas": {"width": 1920, "height": 1080, "fps": 30}, "paper": "#FBF7EE",
       "cover": {"source": "inputs/cover.png", "seconds": 1.0},
       "font": {"path": HAN, "index": 2},
       "hand": {"preset": "child-pencil", "pen_text": ""},
       "voice_studio": {"voice": "sweet-student"},
       "narration": {"source": "inputs/narration/master.wav", "alignment": "inputs/narration/alignment.json"},
       "audio": {"end_hold_seconds": 0.45},
       "watermark": {"text": "十万个为什么", "opacity": 0.28, "font_size": 36},
       "captions": {"font": {"path": STHEITI, "index": 0}, "font_size": 40, "color": "#FFFFFF", "stroke_width": 3,
                    "stroke_color": "#1E1C1A", "background": None, "bottom_margin": 46, "max_width_ratio": 0.82, "max_lines": 2},
       "timeline": {"captions": {"presentation": "burned", "owner": "caption_events"}},
       "pages": pages}
json.dump(job, open("job.json", "w"), ensure_ascii=False, indent=1)
