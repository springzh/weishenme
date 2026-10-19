# 制作日志

`story.py` 每条命令自动记一条（时间、耗时、结果、关键输出）；人工判断和返工用 `story.py note "…"` 补记。做完回看这份日志，把反复出现的问题沉淀进技能。

## 10-19 19:09:54  story.py init 05-xingxing --slug xingxing --title 为什么说猩猩最聪明 --story stories/为什么说猩猩最聪明.txt  — ok · 0s

## 10-19 19:20:22  story.py beats full  — ok · 0s

## 10-19 19:20:22  story.py beats short  — ok · 0s

## 10-19 19:21:53  story.py tts full  — ok · 54s
    synthesized 113.5s (513 chars)
    master 112.01s; suffix cut at 111.847s in a 0.52s pause (-66 dBFS)

## 10-19 19:22:20  story.py tts short  — ok · 19s
    synthesized 36.6s (150 chars)
    master 35.12s; suffix cut at 34.961s in a 0.53s pause (-68 dBFS)

## 10-19 21:38:04  story.py figures  — exit 1 · 0s
    spec.py problems:
  kin: subject 'ape' has no part
  kin: subject 'ground' has no part
  kin: parts name subjects ['animal', 'environment'] that are not listed in subjects
  brain_cells: subject 'brain' has no part
  brain_cells: subject 'lens' has no part
  brain_cells: parts name subjects ['enviro

## 10-19 21:39:34  story.py figures  — ok · 1s
    WARNING ant_fish: content touches the canvas edge (28% of border pixels): enlarge the canvas or move it in
    contact sheet → /Users/spring/Dev/ai_coding/weishenme/works/05-xingxing/figures/sheet.png

## 10-19 21:42:51  story.py figures  — ok · 1s
    contact sheet → /Users/spring/Dev/ai_coding/weishenme/works/05-xingxing/figures/sheet.png

## 10-19 21:45:29  story.py figures  — ok · 1s
    contact sheet → /Users/spring/Dev/ai_coding/weishenme/works/05-xingxing/figures/sheet.png

## 10-19 21:47:22  story.py figures ant_fish  — ok · 0s
    contact sheet → /Users/spring/Dev/ai_coding/weishenme/works/05-xingxing/figures/sheet.png

## 10-19 21:48:51  story.py figures ant_fish  — ok · 0s
    contact sheet → /Users/spring/Dev/ai_coding/weishenme/works/05-xingxing/figures/sheet.png

## 10-19 21:55:46  story.py prepare full  — exit 2 · 71s
    LINT page 8 four_apes overlaps 黄猩猩
    LINT page 8 four_apes overlaps 黑猩猩
    LINT page 8 four_apes overlaps 侏黑猩猩
    LINT page 8 four_apes overlaps 大猩猩
    LINT page 11 一键三连: outside the safe area (captions start ≈ y 975) (1680, 858, 1904, 910)
    EVIDENCE MISSING — look at these images, then write what you saw:
    - cover-review.json["full:cover"]  (full/inputs/cover.png)
    - cover-review.json["full:cover_4x3"]  (full/inputs/cover_4x3.png)

## 10-19 21:57:38  story.py prepare full  — ok · 1s
    full: job ready at /Users/spring/Dev/ai_coding/weishenme/works/05-xingxing/full (11 pages, 10 figures)

## 10-19 21:58:16  story.py render full --preview 40  — exit 1 · 5s
    ERROR: Empty semantic part: env
    failed: /usr/local/bin/python3 /Users/spring/.claude/skills/sweety-handdraw-video/scripts/handdraw_video.py build /Users/spring/Dev/ai_coding/weishenme/works/05-xingxing/full

## 10-19 21:58:16  story.py sheet full --preview  — exit 1 · 0s
    /Users/spring/Dev/ai_coding/weishenme/works/05-xingxing/full/work/review/preview.mp4 missing

## 10-19 21:59:19  story.py prepare full  — ok · 1s
    full: job ready at /Users/spring/Dev/ai_coding/weishenme/works/05-xingxing/full (11 pages, 10 figures)

## 10-19 21:59:46  story.py render full --preview 40  — exit 1 · 8s
    ERROR: Empty semantic part: spoon
    failed: /usr/local/bin/python3 /Users/spring/.claude/skills/sweety-handdraw-video/scripts/handdraw_video.py build /Users/spring/Dev/ai_coding/weishenme/works/05-xingxing/full

## 10-19 21:59:46  story.py sheet full --preview  — exit 1 · 0s
    /Users/spring/Dev/ai_coding/weishenme/works/05-xingxing/full/work/review/preview.mp4 missing

## 10-19 22:01:25  story.py figures learn_eat  — ok · 0s
    contact sheet → /Users/spring/Dev/ai_coding/weishenme/works/05-xingxing/figures/sheet.png

## 10-19 22:01:31  story.py prepare full  — ok · 6s
    full: job ready at /Users/spring/Dev/ai_coding/weishenme/works/05-xingxing/full (11 pages, 10 figures)

## 10-19 22:02:02  story.py render full --preview 40  — exit 1 · 12s
    ERROR: Empty semantic part: skull
    failed: /usr/local/bin/python3 /Users/spring/.claude/skills/sweety-handdraw-video/scripts/handdraw_video.py build /Users/spring/Dev/ai_coding/weishenme/works/05-xingxing/full

## 10-19 22:02:02  story.py sheet full --preview  — exit 1 · 0s
    /Users/spring/Dev/ai_coding/weishenme/works/05-xingxing/full/work/review/preview.mp4 missing

## 10-19 22:03:03  story.py prepare full  — ok · 1s
    full: job ready at /Users/spring/Dev/ai_coding/weishenme/works/05-xingxing/full (11 pages, 10 figures)

## 10-19 22:03:35  story.py render full --preview 40  — ok · 33s

## 10-19 22:03:59  story.py sheet full --preview  — ok · 1s
    → /Users/spring/Dev/ai_coding/weishenme/works/05-xingxing/full/work/review/sheet_preview.png (look at it: every page complete at its end, nothing under the watermark or captions, hook readable at ~3 s)

## 10-19 22:05:32  story.py prepare short  — exit 2 · 35s
    LINT page 4 group feel..feel: 3 items in 2.6s of drawing time (< 0.8 s each): drop a label, move it to a later beat, or split the beat (story.py split)
    LINT page 5 group outro..outro: 3 items in 1.8s of drawing time (< 0.8 s each): drop a label, move it to a later beat, or split the beat (story.py split)
    EVIDENCE MISSING — look at these images, then write what you saw:
    - cover-review.json["short:cover"]  (short/inputs/cover.png)
    - cover-review.json["short:cover_4x3"]  (short/inputs/cover_4x3.png)

## 10-19 22:05:50  story.py render full  — ok · 57s

## 10-19 22:11:25  story.py sheet full  — ok · 2s
    → /Users/spring/Dev/ai_coding/weishenme/works/05-xingxing/full/work/review/sheet_film.png (look at it: every page complete at its end, nothing under the watermark or captions, hook readable at ~3 s)

## 10-19 22:13:39  story.py asr full  — ok · 28s
    "similarity": 0.966,
    "tail_mean_db": -60.1,
    "last_words": "看更多这样的视频记得一键三连哦"

## 10-19 22:16:16  story.py asr full  — ok · 29s
    "similarity": 0.966,
    "tail_mean_db": -60.1,
    "last_words": "看更多这样的视频记得一键三连哦"

## 10-19 22:18:39  story.py finalize full  — ok · 9s

## 10-19 22:19:05  story.py prepare short  — ok · 1s
    short: job ready at /Users/spring/Dev/ai_coding/weishenme/works/05-xingxing/short (5 pages, 4 figures)

## 10-19 22:19:17  story.py render short --preview 15  — ok · 12s

## 10-19 22:19:47  story.py sheet short --preview  — ok · 0s
    → /Users/spring/Dev/ai_coding/weishenme/works/05-xingxing/short/work/review/sheet_preview.png (look at it: every page complete at its end, nothing under the watermark or captions, hook readable at ~3 s)

## 10-19 22:21:38  story.py render short  — ok · 17s

## 10-19 22:21:39  story.py sheet short  — ok · 1s
    → /Users/spring/Dev/ai_coding/weishenme/works/05-xingxing/short/work/review/sheet_film.png (look at it: every page complete at its end, nothing under the watermark or captions, hook readable at ~3 s)

## 10-19 22:23:11  story.py asr short  — ok · 10s
    "similarity": 0.969,
    "tail_mean_db": -63.1,
    "last_words": "区告诉我想看更多记得一键三连哦"

## 10-19 22:25:18  story.py finalize short  — ok · 3s

## 10-19 22:25:46  story.py deliver  — ok · 0s
    → /Users/spring/Dev/ai_coding/weishenme/exports/05-为什么说猩猩最聪明.mp4
    → /Users/spring/Dev/ai_coding/weishenme/exports/05-为什么说猩猩最聪明_封面_4x3.png
    → /Users/spring/Dev/ai_coding/weishenme/exports/05-为什么说猩猩最聪明_封面.png
    → /Users/spring/Dev/ai_coding/weishenme/exports/05-为什么说猩猩最聪明_30秒版.mp4
    → /Users/spring/Dev/ai_coding/weishenme/exports/05-为什么说猩猩最聪明_30秒版_封面_4x3.png
    → /Users/spring/Dev/ai_coding/weishenme/exports/05-为什么说猩猩最聪明_30秒版_封面.png

## 10-19 22:26:17  NOTE
    自定义猩猩角色（ape/ape_side）为本期新增，其他期可复用；踩坑：spec 部位的 subject 要写主体名不是类型字母；FULL 兜底部位若只剩白底会报 Empty semantic part（faces/learn_eat/fossil 改为区域含墨线或前移声明）；木色树枝画在土色蚁巢上看不见，改用墨线

## 10-19 22:36:04  story.py figures ant_fish  — ok · 0s
    contact sheet → /Users/spring/Dev/ai_coding/weishenme/works/05-xingxing/figures/sheet.png

## 10-19 22:39:55  story.py figures ant_fish  — ok · 0s
    contact sheet → /Users/spring/Dev/ai_coding/weishenme/works/05-xingxing/figures/sheet.png

## 10-19 22:42:01  story.py figures ant_fish  — ok · 0s
    contact sheet → /Users/spring/Dev/ai_coding/weishenme/works/05-xingxing/figures/sheet.png

## 10-19 22:43:53  story.py prepare full  — ok · 18s
    full: job ready at /Users/spring/Dev/ai_coding/weishenme/works/05-xingxing/full (11 pages, 10 figures)

## 10-19 22:45:19  story.py render full  — ok · 55s

## 10-19 22:45:21  story.py sheet full  — ok · 1s
    → /Users/spring/Dev/ai_coding/weishenme/works/05-xingxing/full/work/review/sheet_film.png (look at it: every page complete at its end, nothing under the watermark or captions, hook readable at ~3 s)

## 10-19 22:46:53  NOTE
    用户反馈侧面猩猩不像猩猩 → 重画 ape_side：凸吻、大圆耳、眉弓、驼背、颈肩衔接、去腿部杂线；prepare→render→sheet 已重看

## 10-19 22:47:50  story.py finalize full  — ok · 9s

## 10-19 22:48:43  story.py prepare short  — ok · 18s
    short: job ready at /Users/spring/Dev/ai_coding/weishenme/works/05-xingxing/short (5 pages, 4 figures)

## 10-19 22:49:00  story.py render short  — ok · 17s

## 10-19 22:49:01  story.py sheet short  — ok · 1s
    → /Users/spring/Dev/ai_coding/weishenme/works/05-xingxing/short/work/review/sheet_film.png (look at it: every page complete at its end, nothing under the watermark or captions, hook readable at ~3 s)

## 10-19 22:50:19  story.py finalize short  — ok · 3s

## 10-19 22:50:19  story.py deliver  — ok · 0s
    → /Users/spring/Dev/ai_coding/weishenme/exports/05-为什么说猩猩最聪明.mp4
    → /Users/spring/Dev/ai_coding/weishenme/exports/05-为什么说猩猩最聪明_封面_4x3.png
    → /Users/spring/Dev/ai_coding/weishenme/exports/05-为什么说猩猩最聪明_封面.png
    → /Users/spring/Dev/ai_coding/weishenme/exports/05-为什么说猩猩最聪明_30秒版.mp4
    → /Users/spring/Dev/ai_coding/weishenme/exports/05-为什么说猩猩最聪明_30秒版_封面_4x3.png
    → /Users/spring/Dev/ai_coding/weishenme/exports/05-为什么说猩猩最聪明_30秒版_封面.png

## 10-19 23:19:50  story.py harvest  — ok · 0s
    HARVEST note 10-19 22:26:17: 自定义猩猩角色（ape/ape_side）为本期新增，其他期可复用；踩坑：spec 部位的 subject 要写主体名不是类型字母；FULL 兜底部位若只剩白底会报 Empty semantic part（faces/learn_eat/fossil 改为区域含墨线或前移声明）；木色树枝画在土色蚁巢上看不见，改用墨线
    HARVEST note 10-19 22:46:53: 用户反馈侧面猩猩不像猩猩 → 重画 ape_side：凸吻、大圆耳、眉弓、驼背、颈肩衔接、去腿部杂线；prepare→render→sheet 已重看
    HARVEST settle each note: a lesson about drawing this series → kit/LESSONS.md; an unclear error / missing check / wrong default → the skill (script check first, docs second)
    HARVEST kit/LESSONS.md is missing: start it with this episode's lessons

## 10-19 23:24:07  NOTE
    已沉淀：ape / ape_side / ant 和毛色常量 → kit/characters.py，ape_parts → kit/character_parts.py，本期改为 import（重画 10 张图与迁移前逐像素一致）；三个部位坑 → 技能在 figures/prepare 阶段模拟渲染器归属规则提前报 PARTS（写明图名、部位、被谁占了），subject 写成类型时给提示；侧面猩猩特征、木色树枝看不见 → kit/LESSONS.md
