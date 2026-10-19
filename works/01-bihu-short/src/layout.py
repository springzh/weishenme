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
 ([0], [G(0, 0, [text("小壁虎捉蚊子", 150, 60, 84), ill("gecko_catch", 200, 210, 1060, 742, weight=2)])]),
 ([1, 2], [G(1, 1, [text("为什么掉不下来？", 150, 60, 84), ill("suction", 170, 270, 340, 340), text("不是吸盘！", 340, 660, 68, RED, center=True)]),
           G(2, 2, [ill("setae", 640, 280, 460, 460), text("几十万根刚毛", 870, 790, 54, center=True),
                    ill("spatula", 1180, 300, 440, 440), text("一分再分", 1400, 790, 54, center=True)])]),
 ([3], [G(3, 3, [text("分子间的吸引力，积少成多", 150, 60, 80), ill("force", 120, 300, 800, 352), ill("ceiling", 980, 330, 820, 478)])]),
 ([4], [G(4, 4, [text("秘密在脚底：", 960, 260, 96, center=True), under(560, 530, 800),
                 text("数不清的细毛", 960, 420, 120, RED, center=True), text("十万个为什么", 960, 660, 64, GREY, center=True)], lead=.2, hold=.6)]),
]
pages = []
for pb, groups in pages_spec:
    off = pb[0]
    for g in groups: g["start_beat"] -= off; g["end_beat"] -= off
    pages.append({"beats": [{"id": beats[i]["id"], "text": beats[i]["text"], "actions": []} for i in pb], "visual_groups": groups})

STHEITI = "/System/Library/Fonts/STHeiti Medium.ttc"
job = {"version": 1, "title": "十万个为什么：为什么壁虎能在墙上爬却不掉下来（30秒精简版）", "design_file": "design.json",
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
