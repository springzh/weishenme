"""Cover = paper background + cleaned gecko figure + editable text layers (Hannotate)."""
import glob, json
from PIL import Image, ImageDraw, ImageFont
HAN = glob.glob('/System/Library/AssetsV2/com_apple_MobileAsset_Font8/*/AssetData/Hannotate.ttc')[0]
W, H, PAPER = 1920, 1080, (251, 247, 238)
im = Image.new("RGB", (W, H), PAPER)
fig = Image.open("inputs/figures/gecko_wait.png").convert("RGB")
fig = fig.resize((int(fig.width * 0.98), int(fig.height * 0.98)), Image.Resampling.LANCZOS)
mask = fig.convert("L").point(lambda v: 255 if v < 250 else 0)
im.paste(fig, (1120, 70), mask)
d = ImageDraw.Draw(im)
layers = [{"text": "十万个为什么", "xy": [168, 178], "size": 84, "color": "#FFFFFF", "index": 2},
          {"text": "为什么壁虎能在墙上爬", "xy": [150, 410], "size": 100, "color": "#2A2622", "index": 2},
          {"text": "却不掉下来？", "xy": [150, 560], "size": 100, "color": "#2A2622", "index": 2},
          {"text": "秘密藏在它的脚底下", "xy": [156, 760], "size": 60, "color": "#8A7A52", "index": 2}]
bf = ImageFont.truetype(HAN, 84, index=2); bb = d.textbbox((168, 178), "十万个为什么", font=bf)
d.rounded_rectangle([bb[0] - 30, bb[1] - 22, bb[2] + 30, bb[3] + 22], radius=22, fill="#E06A4E")
for L in layers:
    d.text(tuple(L["xy"]), L["text"], font=ImageFont.truetype(HAN, L["size"], index=L["index"]), fill=L["color"])
im.save("inputs/cover.png")
json.dump({"base": "paper #FBF7EE + red rounded badge sized to the 十万个为什么 text bbox +30/+22px + inputs/figures/gecko_wait.png at (1120,70) x0.98", "font": HAN, "layers": layers},
          open("design/cover-layers.json", "w"), ensure_ascii=False, indent=1)
