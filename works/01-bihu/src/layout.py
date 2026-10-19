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
 ([0, 1], [G(0, 0, [text("小壁虎在等什么？", 150, 70, 84), ill("gecko_wait", 170, 200, 600, 735)]),
           G(1, 1, [ill("mosquito", 1100, 250, 440, 417), text("嗡嗡嗡～", 1320, 720, 76, RED, center=True)])]),
 ([2, 3], [G(2, 2, [ill("gecko_catch", 90, 150, 1060, 742)]),
           G(3, 3, [text("壁虎", 1220, 330, 150), text("= 墙壁上的", 1230, 520, 72), under(1222, 710, 330), text("小老虎", 1230, 630, 104, RED)])]),
 ([4, 5], [G(4, 4, [text("为什么掉不下来？", 150, 60, 84), ill("suction", 170, 250, 380, 380), text("是吸盘吗？", 360, 660, 68, center=True)]),
           G(5, 5, [text("不是吸盘！", 360, 760, 68, RED, center=True), ill("foot", 700, 290, 520, 482), text("脚趾上的褶皱", 960, 800, 54, center=True),
                    ill("setae", 1310, 300, 470, 470), text("褶皱上的刚毛", 1545, 800, 54, center=True)])]),
 ([6, 7], [G(6, 6, [text("一根刚毛，一分再分", 150, 60, 80), ill("spatula", 170, 190, 540, 540), text("成百上千个小分叉", 440, 760, 54, center=True)]),
           G(7, 7, [text("贴得极近 → 分子间的吸引力", 820, 340, 60, RED), ill("force", 800, 450, 1000, 440)])]),
 ([8], [G(8, 8, [text("一点点力，积少成多", 150, 60, 84), ill("ceiling", 380, 330, 1100, 640)])]),
 ([9], [G(9, 9, [text("抬脚：从脚尖往回卷", 150, 60, 84), ill("peel", 240, 230, 1440, 720)])]),
 ([10], [G(10, 10, [text("向壁虎学习", 150, 60, 84), ill("tape", 200, 290, 600, 493), text("壁虎胶带", 500, 800, 64, center=True),
                    ill("robot", 1100, 300, 500, 500), text("爬墙机器人", 1350, 820, 64, center=True)])]),
 ([11], [G(11, 11, [ill("gecko_wait", 140, 130, 560, 686, weight=2), text("壁虎不掉下来的秘密", 780, 230, 76),
                    text("不是吸盘，", 780, 390, 80), under(772, 600, 820), text("而是脚底数不清的细毛", 780, 520, 80, RED),
                    text("十万个为什么", 790, 720, 60, GREY)], hold=.6)]),
]
pages = []
for pb, groups in pages_spec:
    off = pb[0]
    for g in groups: g["start_beat"] -= off; g["end_beat"] -= off
    pages.append({"beats": [{"id": beats[i]["id"], "text": beats[i]["text"], "actions": []} for i in pb], "visual_groups": groups})

STHEITI = "/System/Library/Fonts/STHeiti Medium.ttc"
job = {"version": 1, "title": "十万个为什么：为什么壁虎能在墙上爬却不掉下来", "design_file": "design.json",
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
