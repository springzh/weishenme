# 制作日志

`story.py` 每条命令自动记一条（时间、耗时、结果、关键输出）；人工判断和返工用 `story.py note "…"` 补记。做完回看这份日志，把反复出现的问题沉淀进技能。

## 10-19 23:57:44  story.py init 06-daishu --slug daishu --title 袋鼠为什么有袋 --story stories/袋鼠为什么有袋.txt  — ok · 0s

## 10-20 00:03:39  story.py beats full  — ok · 0s

## 10-20 00:03:39  story.py beats short  — exit 1 · 0s
    PROBLEM the series ends every video with an outro beat ("role": "outro"), e.g. '想看更多这样的视频，记得一键三连哦！'

## 10-20 00:04:14  story.py beats short  — ok · 0s

## 10-20 00:05:15  story.py tts full  — ok · 52s
    synthesized 117.5s (553 chars)
    master 115.98s; suffix cut at 115.823s in a 0.50s pause (-63 dBFS)

## 10-20 00:05:58  story.py tts short  — ok · 35s
    synthesized 32.4s (145 chars)
    master 30.82s; suffix cut at 30.662s in a 0.59s pause (-68 dBFS)

## 10-20 01:17:00  story.py figures  — exit 1 · 0s
    spec.py problems:
  bean_scale: animal 'bean' has 1 part — the renderer needs ≥ 2 (head / body), or call it an environment subject if it is only a few strokes
  climb: animal 'joey' has 1 part — the renderer needs ≥ 2 (head / body), or call it an environment subject if it is only a few strokes
  pou

## 10-20 01:18:57  story.py figures  — ok · 2s
    contact sheet → /Users/spring/Dev/ai_coding/weishenme/works/06-daishu/figures/sheet.png

## 10-20 01:20:14  story.py figures  — ok · 2s
    contact sheet → /Users/spring/Dev/ai_coding/weishenme/works/06-daishu/figures/sheet.png

## 10-20 01:21:04  story.py figures  — ok · 1s
    contact sheet → /Users/spring/Dev/ai_coding/weishenme/works/06-daishu/figures/sheet.png

## 10-20 01:22:12  story.py figures  — ok · 1s
    contact sheet → /Users/spring/Dev/ai_coding/weishenme/works/06-daishu/figures/sheet.png

## 10-20 01:24:28  story.py figures  — ok · 1s
    contact sheet → /Users/spring/Dev/ai_coding/weishenme/works/06-daishu/figures/sheet.png

## 10-20 01:25:27  story.py figures  — ok · 1s
    contact sheet → /Users/spring/Dev/ai_coding/weishenme/works/06-daishu/figures/sheet.png

## 10-20 01:26:58  story.py figures  — ok · 1s
    contact sheet → /Users/spring/Dev/ai_coding/weishenme/works/06-daishu/figures/sheet.png

## 10-20 01:32:55  story.py prepare full  — exit 1 · 0s
    figures not drawn yet: ['kangaroo_bean'] (story.py figures)

## 10-20 01:36:40  story.py figures  — ok · 2s
    contact sheet → /Users/spring/Dev/ai_coding/weishenme/works/06-daishu/figures/sheet.png

## 10-20 01:40:09  story.py figures  — ok · 2s
    contact sheet → /Users/spring/Dev/ai_coding/weishenme/works/06-daishu/figures/sheet.png

## 10-20 01:43:34  story.py prepare full  — exit 2 · 53s
    EVIDENCE MISSING — look at these images, then write what you saw:
    - cover-review.json["full:cover"]  (full/inputs/cover.png)
    - cover-review.json["full:cover_4x3"]  (full/inputs/cover_4x3.png)

## 10-20 01:45:26  story.py prepare full  — ok · 1s
    full: job ready at /Users/spring/Dev/ai_coding/weishenme/works/06-daishu/full (14 pages, 12 figures)

## 10-20 01:46:13  story.py prepare short  — exit 2 · 35s
    LINT page 5 group outro..outro: 3 items in 1.9s of drawing time (< 0.8 s each): drop a label, move it to a later beat, or split the beat (story.py split)
    EVIDENCE MISSING — look at these images, then write what you saw:
    - cover-review.json["short:cover"]  (short/inputs/cover.png)
    - cover-review.json["short:cover_4x3"]  (short/inputs/cover_4x3.png)

## 10-20 01:48:19  story.py prepare short  — ok · 1s
    LINT page 5 group outro..outro: 3 items in 1.9s of drawing time (< 0.8 s each): drop a label, move it to a later beat, or split the beat (story.py split)
    short: job ready at /Users/spring/Dev/ai_coding/weishenme/works/06-daishu/short (5 pages, 4 figures)

## 10-20 01:50:28  story.py render full --preview 40  — exit 1 · 0s
    ERROR: Image has no completed art-direction review: /Users/spring/Dev/ai_coding/weishenme/works/06-daishu/full/inputs/cover.png
    failed: /usr/local/bin/python3 /Users/spring/.claude/skills/sweety-handdraw-video/scripts/handdraw_video.py build /Users/spring/Dev/ai_coding/weishenme/works/06-daishu/full

## 10-20 01:57:18  story.py prepare full  — ok · 1s
    full: job ready at /Users/spring/Dev/ai_coding/weishenme/works/06-daishu/full (14 pages, 12 figures)

## 10-20 01:57:19  story.py prepare short  — ok · 1s
    LINT page 5 group outro..outro: 3 items in 1.9s of drawing time (< 0.8 s each): drop a label, move it to a later beat, or split the beat (story.py split)
    short: job ready at /Users/spring/Dev/ai_coding/weishenme/works/06-daishu/short (5 pages, 4 figures)

## 10-20 01:58:24  story.py render full --preview 40  — ok · 46s

## 10-20 01:58:38  story.py sheet full --preview  — ok · 1s
    → /Users/spring/Dev/ai_coding/weishenme/works/06-daishu/full/work/review/sheet_preview.png (look at it: every page complete at its end, nothing under the watermark or captions, hook readable at ~3 s)

## 10-20 01:59:37  story.py render short --preview 15  — ok · 14s

## 10-20 01:59:37  story.py sheet short --preview  — ok · 0s
    → /Users/spring/Dev/ai_coding/weishenme/works/06-daishu/short/work/review/sheet_preview.png (look at it: every page complete at its end, nothing under the watermark or captions, hook readable at ~3 s)

## 10-20 02:00:26  story.py render full  — ok · 77s

## 10-20 02:00:28  story.py render short  — ok · 20s

## 10-20 02:00:43  story.py sheet full  — ok · 1s
    → /Users/spring/Dev/ai_coding/weishenme/works/06-daishu/full/work/review/sheet_film.png (look at it: every page complete at its end, nothing under the watermark or captions, hook readable at ~3 s)

## 10-20 02:03:45  story.py prepare full  — ok · 1s
    full: job ready at /Users/spring/Dev/ai_coding/weishenme/works/06-daishu/full (14 pages, 12 figures)

## 10-20 02:03:46  story.py prepare short  — ok · 0s
    LINT page 5 group outro..outro: 3 items in 1.9s of drawing time (< 0.8 s each): drop a label, move it to a later beat, or split the beat (story.py split)
    short: job ready at /Users/spring/Dev/ai_coding/weishenme/works/06-daishu/short (5 pages, 4 figures)

## 10-20 02:05:10  story.py render full  — ok · 66s

## 10-20 02:05:48  story.py render short  — ok · 16s

## 10-20 02:05:50  story.py sheet full  — ok · 1s
    → /Users/spring/Dev/ai_coding/weishenme/works/06-daishu/full/work/review/sheet_film.png (look at it: every page complete at its end, nothing under the watermark or captions, hook readable at ~3 s)

## 10-20 02:05:50  story.py sheet short  — ok · 1s
    → /Users/spring/Dev/ai_coding/weishenme/works/06-daishu/short/work/review/sheet_film.png (look at it: every page complete at its end, nothing under the watermark or captions, hook readable at ~3 s)

## 10-20 02:07:21  story.py asr full  — ok · 24s
    "similarity": 0.951,
    "tail_mean_db": -59.0,
    "last_words": "看更多这样的视频记得一键三零哦"

## 10-20 02:08:21  story.py asr full  — ok · 23s
    "similarity": 0.951,
    "tail_mean_db": -59.0,
    "last_words": "看更多这样的视频记得一键三零哦"

## 10-20 02:08:56  story.py asr short  — ok · 7s
    "similarity": 0.953,
    "tail_mean_db": -91.0,
    "last_words": "区告诉我想看更多记得一键三连哦"

## 10-20 02:12:25  story.py finalize full  — ok · 10s

## 10-20 02:12:28  story.py finalize short  — ok · 3s

## 10-20 02:12:49  story.py deliver  — ok · 0s
    → /Users/spring/Dev/ai_coding/weishenme/exports/06-袋鼠为什么有袋.mp4
    → /Users/spring/Dev/ai_coding/weishenme/exports/06-袋鼠为什么有袋_封面_4x3.png
    → /Users/spring/Dev/ai_coding/weishenme/exports/06-袋鼠为什么有袋_封面.png
    → /Users/spring/Dev/ai_coding/weishenme/exports/06-袋鼠为什么有袋_30秒版.mp4
    → /Users/spring/Dev/ai_coding/weishenme/exports/06-袋鼠为什么有袋_30秒版_封面_4x3.png
    → /Users/spring/Dev/ai_coding/weishenme/exports/06-袋鼠为什么有袋_30秒版_封面.png

## 10-20 02:13:12  story.py harvest  — ok · 0s
    HARVEST candidate src/figures.py:135 _finger(): would another episode draw this? → kit/characters.py (+ @sample)
    HARVEST candidate src/figures.py:150 _pouch() (uses MILK, POUCH_IN, TEAT): would another episode draw this? → kit/characters.py (+ @sample)
    HARVEST candidate src/spec.py:8 joey_parts(): would another episode draw this? → kit/character_parts.py
    HARVEST kit/catalog.* is stale: run story.py catalog

## 10-20 02:24:31  story.py figures  — ok · 2s
    contact sheet → /Users/spring/Dev/ai_coding/weishenme/works/06-daishu/figures/sheet.png

## 10-20 02:26:03  NOTE
    已沉淀：joey_parts 移入 kit/character_parts.py（joey_bean 的头/身体部位拆分）；_finger 改造为 kit/characters.py 的 finger 角色（锚点=指尖，固定肤色 FINGER_SKIN 与 NAIL），本期改 import 后 13 张插图+sheet 像素级一致。_pouch（袋切面+乳头+奶滴）是本期专用示意图，未沉淀。修复：Edit 误加重复 @sample(zoo) 行，已删。
