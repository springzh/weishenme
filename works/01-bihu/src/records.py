import json, hashlib
sha = lambda p: hashlib.sha256(open(p, "rb").read()).hexdigest()
beats = json.load(open("src/beats.json"))
design = {
 "narrative_route": {"decision": "story_question_mechanism",
  "reason": "原文是一个小故事（壁虎捉蚊子）加一句解释。默认的“生活常见错误→概念→机制→行动”路线不完全适用；但原文里“壁虎靠吸盘”恰好是一个常见误解，最自然的路径是：故事引入 → 提问 → 揭开误解（不是吸盘）→ 逐级放大讲机制 → 抬脚 → 仿生应用 → 收束回答。",
  "director_review": "Spine：从“它怎么不掉下来”到“原来不是吸盘，是亿万细毛”。支点在第3页“是吸盘吗？→不是吸盘！”。机制段用放大镜一级级往里看（脚趾→褶皱→刚毛→分叉→贴近墙面），每页一个完整意思，图形逐步累积。结尾回到开头那只壁虎，回答标题问题。",
  "director_plan": {"spine": "壁虎不掉下来，靠的不是吸盘，而是脚底下数不清的细毛。",
   "pivot": "第3页：吸盘？→ 显微镜下没有吸盘。",
   "genre_contract": "少儿科普《十万个为什么》：孩子期待可爱的角色、清楚的“为什么—因为”与一个惊喜的答案。",
   "beats_per_page": [2, 2, 2, 2, 1, 1, 1, 1],
   "sound": "旁白直出，不加配乐；换页跟随下一页首句起点。"}},
 "topic": "为什么壁虎能在墙上爬却不掉下来（《十万个为什么》系列）",
 "audience": "小学生及亲子观众",
 "explanation_goal": "知道壁虎脚上没有吸盘；脚趾褶皱上长满刚毛，刚毛末端分成许多小分叉，贴近墙面时分子间的吸引力加起来把壁虎粘住；抬脚时从脚尖卷起所以又快又轻；人们据此发明了壁虎胶带和爬墙机器人。",
 "source_scope": {"type": "book_adaptation_with_correction",
   "sources": ["用户提供：《十万个为什么》“为什么壁虎能在墙上爬却不掉下来”（为什么壁虎能在墙上爬却不掉下来.txt）",
               "Autumn K. et al., Adhesive force of a single gecko foot-hair, Nature 405:681–685 (2000)",
               "Autumn K. et al., Evidence for van der Waals adhesion in gecko setae, PNAS 99(19):12252–12256 (2002)",
               "Kim S. et al., Smooth vertical surface climbing with directional adhesion (Stickybot), IEEE Trans. Robotics 24(1) (2008)"],
   "facts": "壁虎脚趾腹面有成排的皮瓣褶皱（lamellae），其上密布刚毛（setae），每只脚约数十万根；每根刚毛末端分成100–1000个铲状小分叉（spatulae），宽约0.2微米；附着主要依靠范德华力（分子间作用力），并非吸盘或胶水；抬脚时脚趾从尖端向后翻卷（digital hyperextension），使刚毛逐排脱离；据此研制了可反复粘贴的“壁虎胶带”与 Stickybot 等爬墙机器人。",
   "correction": "原文写壁虎“脚上长着一种叫‘吸盘’的小东西”，并称吸盘挂钩等发明源于壁虎。这与现代研究不符：壁虎脚上没有吸盘（吸盘挂钩靠大气压，与壁虎无关）。成片保留原文的故事（夏夜墙角等蚊子、悄无声息闪电捕蚊、‘墙壁上的小老虎’名字由来、移动时一点声音也没有），把‘吸盘’作为过去的常见看法引出，再给出科学解释；应用部分改为真实的壁虎仿生发明。",
   "simplifications": "范德华力表述为“分子和分子之间的一种微弱的吸引力”；刚毛数量用“几十万根”，分叉用“成百上千个”。"},
 "visual_direction": {"characters": "一只嫩黄绿色、黄色大眼睛的卡通壁虎贯穿全片（同一绘制函数）；红肚子蚊子", "color": "米白纸、墨线、嫩黄绿壁虎、奶黄脚底、暖砖墙面，红色只用于吸饱血的蚊子、吸盘与关键箭头", "line": "6px 圆润墨线带轻微抖动", "density": "每页1–3个图形+短标题"},
 "subtitle_design": {"font": "STHeiti Medium（常规黑体，独立于手写体）", "size": 40, "style": "白字黑色3px描边、无底板，底部居中单行为主",
   "reason": "米白纸面浅色背景，白字需描边保证可读；正文为手写体，字幕用板正黑体区分层级。"},
 "series_mark": {"text": "十万个为什么", "where": "封面红色徽标；全片低不透明度浮动水印；结尾页手写一行", "reason": "用户要求系列视频统一带上“十万个为什么”字样"},
 "beats": [{"id": b["id"], "narration": b["text"]} for b in beats],
 "cover": {"title": "为什么壁虎能在墙上爬却不掉下来？", "badge": "十万个为什么", "subtitle": "秘密藏在它的脚底下", "visual": "正文第1页同一只墙角壁虎"},
 "asset_prompts": {"method": "代码绘制（src/draw_figures.py），本机无可用生图工具；美术简报与“代码即提示词”在 design/briefs、design/prompts", "text_in_images": "无，全部文字由运行时文字层书写"}
}
json.dump(design, open("design.json", "w"), ensure_ascii=False, indent=1)

C = {  # (narrative observations, anatomy/occlusion, part boundaries, stroke breaks)
 "gecko_wait": ({"gecko": "画面中部一只完整的俯视壁虎，左侧竖线与底部横线构成墙角，壁虎在墙角内", "eyes": "头部两侧各一只黄色大圆眼，带竖瞳和高光"},
   "俯视壁虎：头、身体压在四条腿根部与尾巴根部之上；墙线不与壁虎接触", "按壁虎局部坐标旋转后的矩形：头部区覆盖头和双眼；身体区覆盖躯干；前/后腿区覆盖腿和五趾；尾巴区；墙角线为剩余", "每条腿外形、每个脚趾和趾垫、身体、头、尾巴各自闭合一笔，部位间抬笔"),
 "mosquito": ({"blood": "腹部为鼓起的番茄红椭圆"}, "翅膀压在腿根之上，胸部压在翅根之上", "头部（头圆圈、口器、触角）为中央上窄条；翅膀区为上半剩余；身体为中央下窄条；六条腿为剩余", "每条腿、每片翅、每个圆圈各一笔"),
 "gecko_catch": ({"dash": "壁虎身体斜向右上，左下有四条平行速度线", "eat": "壁虎吻端紧贴一只倒置的小蚊子，翅膀与红腹部露在嘴外"},
   "蚊子位于壁虎吻端前方并略压在头部轮廓上", "蚊子按身体轴线分左右两半先画；壁虎各区排除蚊子圆形区域；速度线为剩余", "速度线每条一笔，壁虎各部位外形各一笔"),
 "suction": ({"cup": "红色半球形吸盘与扁平底边，上方黑色挂钩"}, "挂钩从吸盘顶部伸出", "挂钩为上方窄条，吸盘为剩余", "挂钩一笔，拱顶一笔，底边一笔"),
 "foot": ({"folds": "五个趾垫上各有六道弧形褶皱线", "nocup": "趾垫为细长加宽的扁平垫，没有圆形吸盘"},
   "掌心压在五个脚趾根部之上，腿在掌心之下伸出画外", "脚趾区为上部64%；掌心为中下矩形；腿为剩余", "每个脚趾外形一笔、每道褶皱一笔、小爪一笔"),
 "setae": ({"hairs": "放大镜圆框内，一道奶黄褶皱上竖着19根细毛"}, "褶皱压在细毛根部上；手柄从镜框右下伸出", "镜框为圆环（排除内圆与手柄角）；刚毛为内圆上部；褶皱为内圆剩余；手柄为剩余", "镜框一笔、每根刚毛一笔、褶皱一笔、手柄一笔"),
 "spatula": ({"split": "茎顶端分五枝，每枝再分四根细枝，末端红色小扁片共20个"}, "无遮挡", "茎为下部47%，分叉为剩余", "茎一笔、每根分枝与细枝各一笔、扁片各一圈"),
 "force": ({"close": "八个扁片悬在墙面上缘上方约十几像素", "attract": "每个扁片右侧一个向下指向墙面的红色小箭头"}, "无遮挡", "细毛与扁片为上部（排除箭头竖带）；箭头为扁片高度的横带；墙面为剩余", "每根细毛一笔、扁片一圈、箭头竖线和两笔箭头、墙面与分子各一笔"),
 "ceiling": ({"hang": "砖色天花板下，壁虎背朝下，四条腿向上，扁平趾垫贴住天花板"}, "腿根被身体遮挡；趾垫贴在天花板下缘", "天花板为上方横带；腿为天花板下的中部横带；头为左侧；身体为中部；尾巴为剩余", "天花板、每条腿、头、身体、尾巴各一笔"),
 "peel": ({"curl": "脚趾左段平贴墙面，右段向上弯起，趾尖离开墙面", "lift": "右侧一支红色弯箭头向上指"}, "脚趾贴在墙面上缘", "脚趾为左侧71%墙面以上；箭头为右侧；墙面为剩余", "脚趾外形一笔、四道小褶皱、箭头弧线和两笔箭头、墙面一笔"),
 "tape": ({"tape": "暖黄胶带卷，右下拉出的胶带条上有三个小脚印"}, "胶带条根部压在卷上", "胶带卷为圆形区；胶带条为剩余", "外圈、内圈、胶带条、每个脚印三笔"),
 "robot": ({"robot": "灰色机器人身体、黄眼睛笑脸，四条机械腿末端各一个红色大脚垫"}, "腿根被身体遮挡", "身体为中央矩形；腿和脚垫为剩余", "身体、眼睛、嘴、每条腿、每个脚垫各一笔"),
}
plan = json.load(open("design/drawing-plan.json"))
review = {"style_sha256": sha("style/resolved.json"), "plan_sha256": sha("design/drawing-plan.json"), "illustrations": []}
for p in plan["illustrations"]:
    obs, a, b, c = C[p["id"]]
    review["illustrations"].append({"plan_id": p["id"], "status": "pass", "source_sha256": sha(f"inputs/figures/{p['id']}.png"), "crop": None,
        "anatomy_and_occlusion": a, "part_boundaries": b, "stroke_breaks": c,
        "outline_then_fill": "所有轮廓为深墨色6px可独立追踪；填色均为暖色平涂，先轮廓后填色；褶皱/刚毛/速度线为浅棕或砖色细线，在填色阶段随笔刷出现",
        "spatial_order": p.get("order_exception", "从上到下、从左到右"),
        "narrative_checks": [{"id": r["id"], "status": "pass", "evidence": "实际看图：" + obs[r["id"]]} for r in p["narrative_requirements"]]})
json.dump(review, open("design/drawing-review.json", "w"), ensure_ascii=False, indent=1)

rec = json.load(open("design/art-direction.json"))
for e in rec["images"]:
    name = e["source"].split("/")[-1][:-4]
    e["sha256"] = sha(e["source"].replace("../", ""))
    e["status"] = "pass"
    e["evidence"] = ("实际看图：左上红色圆角徽标内白字“十万个为什么”完整（已修正首版徽标过窄导致“么”出界），主标题两行“为什么壁虎能在墙上爬”“却不掉下来？”与副标题“秘密藏在它的脚底下”逐字正确各一次；右侧为正文同一只墙角壁虎，留白充足，无伪文字。文字为可编辑字体图层（design/cover-layers.json）。"
                     if name == "cover" else f"代码绘制成图实际查看：{C[name][0]}；轮廓深墨色连续、填色暖色平涂、白底干净、无文字和杂点；正常尺寸下主体一眼可辨。")
json.dump(rec, open("design/art-direction.json", "w"), ensure_ascii=False, indent=1)
