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
 ([0], [G(0, 0, [ill("kid", 250, 140, 540, 748, weight=2), text("北极熊为什么", 880, 430, 110, RED), text("不怕冷？", 880, 590, 110, RED)], lead=.2)]),
 ([1], [G(1, 1, [text("秘密一：两层毛", 150, 60, 84), ill("fur_layers", 130, 200, 990, 572), text("长长的针毛", 1170, 330, 60), text("软软的绒毛", 1170, 560, 60),
                 ill("jacket", 1560, 470, 266, 280), text("像羽绒服", 1693, 780, 56, RED, center=True)])]),
 ([2], [G(2, 2, [text("秘密二：黑皮肤 + 厚脂肪", 150, 60, 80), ill("fat_layers", 200, 190, 936, 728), text("黑皮肤：吸热", 1180, 360, 64),
                 text("厚脂肪：锁住热量", 1180, 520, 64, RED)])]),
 ([3], [G(3, 3, [text("热量跑不掉", 150, 60, 84), ill("bear_head", 170, 220, 520, 460, weight=2), text("小耳朵 · 短尾巴", 430, 720, 64, center=True),
                 ill("paw", 1000, 200, 560, 540, weight=2), text("毛脚掌", 1280, 790, 64, center=True)])]),
 ([4], [G(4, 4, [text("不怕冷，还会游泳！", 150, 60, 84), ill("bear_swim", 360, 230, 1200, 640), text("十万个为什么", 156, 170, 56, GREY)], hold=.6)]),
]
pages = []
for pb, groups in pages_spec:
    off = pb[0]
    for g in groups: g["start_beat"] -= off; g["end_beat"] -= off
    pages.append({"beats": [{"id": beats[i]["id"], "text": beats[i]["text"], "actions": []} for i in pb], "visual_groups": groups})

STHEITI = "/System/Library/Fonts/STHeiti Medium.ttc"
job = {"version": 1, "title": "十万个为什么：为什么北极熊不怕冷（30秒精简版）", "design_file": "design.json",
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
