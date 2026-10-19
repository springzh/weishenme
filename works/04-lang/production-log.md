# 制作日志

`story.py` 每条命令自动记一条（时间、耗时、结果、关键输出）；人工判断和返工用 `story.py note "…"` 补记。做完回看这份日志，把反复出现的问题沉淀进技能。

## 10-19 17:39:37  story.py init 04-lang --slug lang --title 为什么不把狼都消灭光 --story stories/为什么不把狼都消灭光.txt  — ok · 0s

## 10-19 17:39:37  NOTE
    开工：用户要求“继续使用当前 skill 制作 stories/为什么不把狼都消灭光.txt 的视频，记录关键日志，生成完毕后检查日志、必要时完善 skill”。按系列惯例全自动：完整版+30秒版+4:3封面。

## 10-19 17:39:37  story.py doctor  — ok · 0s

## 10-19 17:39:46  NOTE
    配色：palette.py suggest 给 warm-paper(16) > forest(4)。warm-paper 靠“动物/为什么/小朋友/吃”这类泛词得分，几乎每篇都会赢；第 03 期同样问题（手选 sun-desert）。本期题材是森林/河边/鹿/狼，手选 forest。→ 待改：泛词不该给通用主题加分。

## 10-19 17:42:36  story.py beats full  — ok · 0s

## 10-19 17:42:36  story.py beats short  — ok · 0s

## 10-19 17:42:43  NOTE
    精读核对：原文 6 处过时/不准（上百只狼群、嚎叫召集四面八方、拟人“知道招人恨”、叼走小孩/见人就攻、皮毛肉油可利用、狗耳下垂），已在 design.json 逐条更正；骨架改用黄石公园营养级联的真实故事。

## 10-19 17:43:30  story.py tts full  — ok · 47s
    synthesized 124.7s (550 chars)
    master 123.27s; suffix cut at 123.106s in a 0.52s pause (-68 dBFS)

## 10-19 17:43:43  story.py figures  — exit 1 · 0s
    spec.py has no entry for ['storybook', 'wolf_dog', 'pack', 'howl', 'eat', 'gone', 'back', 'chain', 'protect', 'safe', 'wolf_tree', 'fox_hare', 'sanlian']: write composition/parts/reqs before drawing

## 10-19 17:43:51  story.py tts short  — ok · 22s
    synthesized 36.7s (152 chars)
    master 35.38s; suffix cut at 35.218s in a 0.50s pause (-62 dBFS)

## 10-19 17:44:41  story.py figures  — ok · 1s
    contact sheet → /Users/spring-kite/Dev/ai/ai_coding/gen-video/weishenme/04-lang/figures/sheet.png

## 10-19 17:44:58  NOTE
    配音时长偏差：完整版估 112s 实测 123.3s（550字，4.46字/秒），精简版估 31s 实测 35.4s（4.30字/秒）。原因：加了 voice.context 夸张语气后语速比 4.9字/秒 慢约 10%。精简版超出“约30秒”，删稿到 ~125 字重合成。→ 待改：beats 的估算应跟随实际语速（有语气指令时用 ~4.4，或从本系列已合成的 words.json 学）。

## 10-19 17:45:12  story.py tts short  — ok · 14s
    synthesized 30.6s (125 chars)
    master 28.68s; suffix cut at 28.517s in a 0.53s pause (-63 dBFS)

## 10-19 17:45:56  NOTE
    看图第1轮（figures/sheet.png）问题：①悬空——eat 的鹿和羊、chain 的狼和鹿、pack 的大狼、safe/wolf_tree/fox_hare 的狼和狐狸，脚都离地 30–90px（cy 靠手算，算错了）；②gone 的鹿 head_rot=.55 还不够低，看不出在啃树苗，树桩画在水边、离嘴很远；③howl 的声音弧线压在月亮上；④鹿角太细像乱线；⑤狼的垂尾太短像个钩；⑥羊和白熊一样（敦实白身体）；⑦wolf_tree 狼鼻子顶到树干。→ 待改：figkit 给“脚踩地面”的定位函数，不再手算 cy。

## 10-19 17:46:35  story.py figures  — ok · 1s
    contact sheet → /Users/spring-kite/Dev/ai/ai_coding/gen-video/weishenme/04-lang/figures/sheet.png

## 10-19 17:46:58  story.py figures pack wolf_tree  — ok · 0s
    contact sheet → /Users/spring-kite/Dev/ai/ai_coding/gen-video/weishenme/04-lang/figures/sheet.png

## 10-19 17:47:35  NOTE
    看图第2轮：用新加的 figkit.stand() 重放所有动物后脚全部落地；gone 鹿头 head_rot 1.05、树桩移到鹿嘴边；howl 月亮移到左上；鹿角加粗；狼尾加长；羊改用新 sheep()（卷毛身体）；pack 两只大狼缩小拉开不再重叠；wolf_tree 树冠移回画内。figure-review.json 按看到的写完。另：figure-review 的 observed 键是“叙事要求 id”，不是主体名——第 03 期 sanlian 就因此报过 EVIDENCE MISSING，文档没写清。

## 10-19 17:48:37  story.py prepare full  — exit 1 · 0s
    Traceback (most recent call last):
    failed: /usr/local/bin/python3 /Users/spring-kite/.claude/skills/sweety-handdraw-video/scripts/drawing_contract.py /Users/spring-kite/Dev/ai/ai_coding/gen-video/weishenme/04-lang/full /Users/spring-kite/Dev/ai/ai_coding/gen-video/weishenme/04-lang/full/design/drawing-plan.json

## 10-19 17:48:37  story.py prepare short  — exit 1 · 0s
    Traceback (most recent call last):
    failed: /usr/local/bin/python3 /Users/spring-kite/.claude/skills/sweety-handdraw-video/scripts/drawing_contract.py /Users/spring-kite/Dev/ai/ai_coding/gen-video/weishenme/04-lang/short /Users/spring-kite/Dev/ai/ai_coding/gen-video/weishenme/04-lang/short/design/drawing-plan.json

## 10-19 17:48:52  NOTE
    prepare 失败：ValueError 'Animals also need separate anatomical parts'——没说是哪张图、哪个主体（查了半天才定位到 back 里只有一个部位的河狸）。河狸拆头/身体，飞鸟两笔 V 线改为环境主体。→ 待改：figures/prepare 阶段先自查“每个 A 主体 ≥2 个部位”，报出图名和主体名。

## 10-19 17:48:53  story.py prepare full  — exit 1 · 0s
    Traceback (most recent call last):
    failed: /usr/local/bin/python3 /Users/spring-kite/.claude/skills/sweety-handdraw-video/scripts/drawing_contract.py /Users/spring-kite/Dev/ai/ai_coding/gen-video/weishenme/04-lang/full /Users/spring-kite/Dev/ai/ai_coding/gen-video/weishenme/04-lang/full/design/drawing-plan.json

## 10-19 17:49:34  story.py prepare short  — exit 2 · 41s
    LINT page 4 group chain..chain: 5 items in 3.7s of drawing time (< 0.8 s each): drop a label, move it to a later beat, or split the beat (story.py split)
    LINT page 4 chain overlaps 吃
    LINT page 4 chain overlaps 吃
    EVIDENCE MISSING — look at these images, then write what you saw:

## 10-19 17:49:48  NOTE
    prepare 失败：'A drawing plan needs unique semantic parts'——同一张图里狼和小朋友都叫 head。同样没报图名。→ 待改：spec 自查重复 part id 并报图名；quadruped_parts/kid_parts 混用时建议 prefix。

## 10-19 17:51:22  story.py prepare full  — exit 2 · 93s
    LINT page 9 chain overlaps 吃
    LINT page 9 chain overlaps 吃
    EVIDENCE MISSING — look at these images, then write what you saw:

## 10-19 17:52:02  story.py prepare short  — exit 2 · 41s
    EVIDENCE MISSING — look at these images, then write what you saw:

## 10-19 17:54:20  story.py prepare full  — exit 2 · 93s
    LINT page 9 chain overlaps 吃
    LINT page 9 chain overlaps 吃
    EVIDENCE MISSING — look at these images, then write what you saw:

## 10-19 17:55:01  story.py prepare short  — exit 2 · 41s
    EVIDENCE MISSING — look at these images, then write what you saw:

## 10-19 17:55:17  NOTE
    封面第1版：16:9 正常；4:3 两张主图被挤到底部约 290px 一条（两行标题字多、第二行放大 1.1），小得看不清。改 story.py make_cover：4:3 时若主图可用高度 < 38% 画面，就逐步缩小标题字号重排。重出后主图约 540px 宽。

## 10-19 17:56:50  story.py prepare full  — ok · 93s
    LINT page 9 chain overlaps 吃
    LINT page 9 chain overlaps 吃
    full: job ready at /Users/spring-kite/Dev/ai/ai_coding/gen-video/weishenme/04-lang/full (13 pages, 14 figures)

## 10-19 17:57:31  story.py prepare short  — ok · 41s
    short: job ready at /Users/spring-kite/Dev/ai/ai_coding/gen-video/weishenme/04-lang/short (5 pages, 5 figures)

## 10-19 17:58:01  story.py render full --preview 40  — ok · 29s

## 10-19 17:58:01  story.py sheet full --preview  — ok · 1s
    → /Users/spring-kite/Dev/ai/ai_coding/gen-video/weishenme/04-lang/full/work/review/sheet_preview.png (look at it: every page complete at its end, nothing under the watermark or captions, hook readable at ~3 s)

## 10-19 17:58:36  NOTE
    预览第1轮（前40秒抽帧）：钩子页 3 秒内大字完整；狼狗对比页“尾巴下垂”标签落在地面下方、离尾巴很远——wolf_dog 画布上半是空白，按画布坐标估的位置偏了。图右移 160、标签放到尾巴左侧。→ 待改：给 layoutkit 一个“插图内某点 → 页面坐标”的换算（anchor），标签按图内坐标放。

## 10-19 18:00:10  story.py prepare full  — ok · 94s
    LINT page 3 wolf_dog overlaps 尾巴下垂
    LINT page 9 chain overlaps 吃
    LINT page 9 chain overlaps 吃
    full: job ready at /Users/spring-kite/Dev/ai/ai_coding/gen-video/weishenme/04-lang/full (13 pages, 14 figures)

## 10-19 18:00:54  story.py render full  — ok · 44s

## 10-19 18:00:55  story.py sheet full  — ok · 1s
    → /Users/spring-kite/Dev/ai/ai_coding/gen-video/weishenme/04-lang/full/work/review/sheet_film.png (look at it: every page complete at its end, nothing under the watermark or captions, hook readable at ~3 s)

## 10-19 18:01:10  story.py render short  — ok · 15s

## 10-19 18:01:11  story.py sheet short  — ok · 1s
    → /Users/spring-kite/Dev/ai/ai_coding/gen-video/weishenme/04-lang/short/work/review/sheet_film.png (look at it: every page complete at its end, nothing under the watermark or captions, hook readable at ~3 s)

## 10-19 18:01:47  story.py asr full  — ok · 7s
    "similarity": 0.994,
    "tail_mean_db": -60.4,
    "last_words": "看更多这样的视频记得一键三连哦"

## 10-19 18:01:51  story.py asr short  — ok · 3s
    "similarity": 0.991,
    "tail_mean_db": -91.0,
    "last_words": "还是变少想看更多记得一键三连哦"
    note: text transcribed after the narration ended is whisper hallucination on silence when tail_mean_db is below ≈ -45 dB

## 10-19 18:02:17  NOTE
    抽帧终检：完整版 13 页 + 精简版 5 页每页结束完整，单层字幕，无压水印/字幕。ASR：完整版 0.994（狸→里 同音）、精简版 0.991（哪→呐）；精简版尾部 -91dB 纯静音里 whisper 幻听出 14 段“小树”，已被 after_narration_segments 识别剔除——脚本处理正确，但报告里一长串重复词读起来像出错，可在 asr 输出里折叠成“静音段幻听 N 段（已忽略）”。

## 10-19 18:02:26  story.py finalize full  — ok · 9s

## 10-19 18:02:29  story.py finalize short  — ok · 3s

## 10-19 18:02:29  story.py deliver  — ok · 0s
    → /Users/spring-kite/Dev/ai/ai_coding/gen-video/weishenme/exports/04-为什么不把狼都消灭光.mp4
    → /Users/spring-kite/Dev/ai/ai_coding/gen-video/weishenme/exports/04-为什么不把狼都消灭光_封面_4x3.png
    → /Users/spring-kite/Dev/ai/ai_coding/gen-video/weishenme/exports/04-为什么不把狼都消灭光_封面.png
    → /Users/spring-kite/Dev/ai/ai_coding/gen-video/weishenme/exports/04-为什么不把狼都消灭光_30秒版.mp4
    → /Users/spring-kite/Dev/ai/ai_coding/gen-video/weishenme/exports/04-为什么不把狼都消灭光_30秒版_封面_4x3.png
    → /Users/spring-kite/Dev/ai/ai_coding/gen-video/weishenme/exports/04-为什么不把狼都消灭光_30秒版_封面.png

## 10-19 18:08:19  story.py prepare full  — ok · 93s
    LINT page 3 wolf_dog overlaps 尾巴下垂
    LINT page 9 chain overlaps 吃
    LINT page 9 chain overlaps 吃
    full: job ready at /Users/spring-kite/Dev/ai/ai_coding/gen-video/weishenme/04-lang/full (13 pages, 14 figures)

## 10-19 18:08:19  story.py prepare full  — ok · 0s
    LINT page 3 wolf_dog overlaps 尾巴下垂
    LINT page 9 chain overlaps 吃
    LINT page 9 chain overlaps 吃
    full: job ready at /Users/spring-kite/Dev/ai/ai_coding/gen-video/weishenme/04-lang/full (13 pages, 14 figures)

## 10-19 18:12:43  story.py beats full  — ok · 0s

## 10-19 18:12:43  story.py beats short  — ok · 0s

## 10-19 18:14:08  story.py figures sanlian  — ok · 0s
    contact sheet → /Users/spring-kite/Dev/ai/ai_coding/gen-video/weishenme/04-lang/figures/sheet.png

## 10-19 18:15:17  story.py asr short  — ok · 3s
    "similarity": 0.991,
    "tail_mean_db": -91.0,
    "last_words": "还是变少想看更多记得一键三连哦"

## 10-19 18:17:06  story.py lint full  — ok · 0s

## 10-19 18:25:02  NOTE
    交付后回看日志，已沉淀进技能（未提交）：①配色推荐默认主题只兜底+not_words，四篇回归全对；②beats 估时长改用本系列实测语速（4.54字/秒，估 121s/28s vs 实际 123s/28.7s）；③figures/prepare 先自查 spec（重复 part id、单部位动物、人缺部位），报图名；④figkit.stand() 脚踩地面、狼狗鹿狐狸变体、羊/兔/鼠/河狸/鸟/树苗/树桩；⑤layoutkit.at() 按图内坐标放标签，lint 重叠改按实际笔迹算（误报清零）；⑥4:3 封面主图过小时自动缩标题；⑦prepare 隐私清理按内容缓存（93s→0.5s，6 次 prepare 原本浪费约 7 分钟）；⑧日志本身：补抓 xxxError: 行和缺证据清单；⑨asr 幻听折叠计数、尾部不静音时提示去听。测试 188 passed，隐私扫描无发现。

## 10-19 18:43:38  story.py deliver  — ok · 0s
    → /Users/spring-kite/Dev/ai/ai_coding/gen-video/weishenme/exports/04-为什么不把狼都消灭光.mp4
    → /Users/spring-kite/Dev/ai/ai_coding/gen-video/weishenme/exports/04-为什么不把狼都消灭光_封面_4x3.png
    → /Users/spring-kite/Dev/ai/ai_coding/gen-video/weishenme/exports/04-为什么不把狼都消灭光_封面.png
    → /Users/spring-kite/Dev/ai/ai_coding/gen-video/weishenme/exports/04-为什么不把狼都消灭光_30秒版.mp4
    → /Users/spring-kite/Dev/ai/ai_coding/gen-video/weishenme/exports/04-为什么不把狼都消灭光_30秒版_封面_4x3.png
    → /Users/spring-kite/Dev/ai/ai_coding/gen-video/weishenme/exports/04-为什么不把狼都消灭光_30秒版_封面.png

## 10-19 18:43:38  story.py beats short  — ok · 0s
