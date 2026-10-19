import json, hashlib, inspect, sys
sys.path.insert(0, "src"); import draw_figures as D
plan = json.load(open("design/drawing-plan.json"))["illustrations"]
style = json.load(open("style/resolved.json"))
src_sha = hashlib.sha256(open("src/draw_figures.py", "rb").read()).hexdigest()
helpers = "".join(inspect.getsource(f) for f in (D.bear, D.rot_about, D.leg_len, D.flake))
images = []
for p in plan:
    i = p["id"]
    brief = f"""交付：生成图片（代码绘制的卡通线稿，非 AI 生图模型；本机无可用生图工具，用户要求全自动推进，由模型用代码绘制）。
用途与观看尺寸：1920×1080 少儿科普手绘讲解视频《十万个为什么·为什么北极熊不怕冷》的插图，正常播放尺寸观看，占画面约 1/4–1/2。
主体与场景：{p['composition']}
接触与受力：北极熊四只脚掌踩实冰面/雪地，无悬空；游泳图水面盖住身体下半；海豹从冰窟窿里探头。
媒介与画风：{style['style_name']}。线条：{style['style_spec']['line']}。色彩：{style['style_spec']['palette']}。明暗：{style['style_spec']['shading']}。
参考图及用途：无。同片北极熊统一由 bear() 绘制，保证造型、配色、比例一致。
准确文案：无（图中不含任何文字；标签由视频运行时的可控文字层书写）。
必须保留：科学结构正确——两层毛（贴皮肤的短绒毛+外层长针毛）；毛透明、皮肤黑色；皮下厚脂肪；耳朵小、尾巴短；脚掌多毛、垫子小。
观看主次：先看主体整体轮廓，其次是红色强调（热量箭头、帽子手套）；无装饰、无漂浮元素、无纸纹。
可绘制性：{p['drawability_reason']}
对应讲解：{'；'.join(r['narration_quote'] for r in p['narrative_requirements'])}
"""
    fn = D.ALL[i]
    prompt = f"""# 本图实际生成指令（代码即提示词）
# 生成器：src/draw_figures.py  sha256={src_sha}
# 共用规则：Catmull-Rom 样条 + wobble() 低频抖动 amp≈1.8px、墨线 6px、2x 超采样后 LANCZOS 缩小、白底、随机种子 2026
# 调色：INK=#2A2622 BEAR=#F6EEDA BEAR2=#E6DCC4 SKINK=#403A38 ICE=#E2EEF2 WATER=#DCEAF2 FAT=#F8DE8C MEAT=#EEAC98 RED=#E06A4E（冷色红分量≥218，不会被当作墨线）

{inspect.getsource(fn)}
# 共用角色绘制函数
{helpers}"""
    open(f"design/briefs/{i}.md", "w").write(brief); open(f"design/prompts/{i}.txt", "w").write(prompt)
    images.append({"source": f"../inputs/figures/{i}.png", "method": "generated_under_guidance",
                   "brief_file": f"briefs/{i}.md", "prompt_file": f"prompts/{i}.txt", "status": "pending", "evidence": ""})
# covers (composed from the cleaned bear figure + editable text layers)
open("design/briefs/cover.md", "w").write("""交付：视频封面两版——片头 1920×1080（inputs/cover.png）与发布用 4:3 1440×1080（inputs/cover_4x3.png），《十万个为什么》系列。
主体：正文同一只浮冰上的北极熊（inputs/figures/bear_side.png），16:9 版在右侧，4:3 版在右下。
准确文案（可编辑文字图层，Hannotate 手写体）：顶部红色徽标“十万个为什么”出现一次；主标题“为什么北极熊”“不怕冷？”两行各一次；副标题“30秒看懂：秘密藏在毛和脂肪里”一次。
观看主次：先看主标题，再看北极熊，再看系列徽标。米白纸底，留白充足，无伪文字。
""")
open("design/prompts/cover.txt", "w").write("# 封面合成指令：见 src/cover.py（米白纸底 + 已清理的 bear_side.png + 文字图层，图层参数写入 design/cover-layers.json）\n" + open("src/cover.py").read())
for c in ("cover", "cover_4x3"):
    images.append({"source": f"../inputs/{c}.png", "method": "composed_with_verified_layers", "brief_file": "briefs/cover.md",
                   "prompt_file": "prompts/cover.txt", "status": "pending", "evidence": "", "layers": "cover-layers.json"})
rec = {"dependency_sha256": hashlib.sha256(open("/Users/spring-kite/.claude/skills/sweety-handdraw-video/dependencies/sweety-image-art-direction/GUIDE.md", "rb").read()).hexdigest(),
       "style_sha256": hashlib.sha256(open("style/resolved.json", "rb").read()).hexdigest(), "images": images}
json.dump(rec, open("design/art-direction.json", "w"), ensure_ascii=False, indent=1)
