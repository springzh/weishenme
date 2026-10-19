"""Covers = paper background + cleaned bear figure + editable text layers (Hannotate).
inputs/cover.png is the 16:9 opening frame of the film; inputs/cover_4x3.png is the 1440x1080 upload cover."""
import glob, json
from PIL import Image, ImageDraw, ImageFont
HAN = glob.glob('/System/Library/AssetsV2/com_apple_MobileAsset_Font8/*/AssetData/Hannotate.ttc')[0]
PAPER = (251, 247, 238)


def make(W, H, fig_xy, fig_scale, badge_xy, layers, out):
    im = Image.new("RGB", (W, H), PAPER)
    fig = Image.open("inputs/figures/bear_side.png").convert("RGB")
    fig = fig.resize((int(fig.width * fig_scale), int(fig.height * fig_scale)), Image.Resampling.LANCZOS)
    mask = fig.convert("L").point(lambda v: 255 if v < 250 else 0)
    im.paste(fig, fig_xy, mask)
    d = ImageDraw.Draw(im)
    bf = ImageFont.truetype(HAN, 84, index=2); bb = d.textbbox(badge_xy, "十万个为什么", font=bf)
    d.rounded_rectangle([bb[0] - 30, bb[1] - 22, bb[2] + 30, bb[3] + 22], radius=22, fill="#E06A4E")
    layers = [{"text": "十万个为什么", "xy": list(badge_xy), "size": 84, "color": "#FFFFFF", "index": 2}] + layers
    for L in layers:
        d.text(tuple(L["xy"]), L["text"], font=ImageFont.truetype(HAN, L["size"], index=L["index"]), fill=L["color"])
    im.save(out)
    return {"canvas": [W, H], "base": f"paper #FBF7EE + red rounded badge sized to the 十万个为什么 text bbox +30/+22px + inputs/figures/bear_side.png at {fig_xy} x{fig_scale}", "layers": layers}


wide = make(1920, 1080, (980, 330), 1.0, (168, 160),
            [{"text": "为什么北极熊", "xy": [150, 380], "size": 120, "color": "#2A2622", "index": 2},
             {"text": "不怕冷？", "xy": [150, 550], "size": 120, "color": "#2A2622", "index": 2},
             {"text": "30秒看懂：秘密藏在毛和脂肪里", "xy": [156, 760], "size": 54, "color": "#8A7A52", "index": 2}], "inputs/cover.png")
tall = make(1440, 1080, (600, 570), 0.9, (128, 110),
            [{"text": "为什么北极熊", "xy": [110, 280], "size": 128, "color": "#2A2622", "index": 2},
             {"text": "不怕冷？", "xy": [110, 450], "size": 128, "color": "#2A2622", "index": 2},
             {"text": "30秒看懂：秘密藏在毛和脂肪里", "xy": [116, 630], "size": 48, "color": "#8A7A52", "index": 2}], "inputs/cover_4x3.png")
json.dump({"font": HAN, "cover_16x9": wide, "cover_4x3": tall}, open("design/cover-layers.json", "w"), ensure_ascii=False, indent=1)
