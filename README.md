# 十万个为什么 · 手绘科普视频系列

把《十万个为什么》里的一个个小故事做成少儿手绘讲解视频：中文配音，儿童彩铅手一笔一笔画出卡通插图和关键词，烧录字幕和“十万个为什么”系列水印。每期产出：

- 完整版（约 1.5–2 分钟）和 30 秒精简版，1920×1080；
- 每版两张封面：16:9 片头封面（也是成片第 0 帧）和 4:3 发布封面。

每期都有三秒钩子开头（反常识的事实加一句抖包袱，语气夸张），中间按“生活场景 → 原理逐层讲 → 收束回答”展开，结尾抛出一个观众能在评论区回答的问题，再请观众一键三连。原书里过时或不准确的科学说法，查证一手资料后更正，依据写在每期的 `design.json`。

本仓库只放**内容和制作记录**；制作工具是两个 Claude Code 技能，见下文“依赖”。

## 已完成

| 期 | 故事 | 完整版 | 精简版 | 目录 | 说明 |
|---|---|---|---|---|---|
| 01 | 为什么壁虎能在墙上爬却不掉下来 | 91 秒 | 27 秒 | `works/01-bihu/`、`works/01-bihu-short/` | 技能出现前的手工流水线；没有 4:3 封面 |
| 02 | 为什么北极熊不怕冷 | 109 秒 | 32 秒 | `works/02-beixiongxiong/`、`works/02-beixiongxiong-short/` | 手工流水线 |
| 03 | 为什么狮、虎、豹在白天老睡觉 | 110 秒 | 33 秒 | `works/03-shihubao/` | science-story-video；按反馈加强了钩子，加了一键三连 |
| 04 | 为什么不把狼都消灭光 | 125 秒 | 30 秒 | `works/04-lang/` | science-story-video；以黄石公园营养级联为主线，更正原文 6 处 |

## 目录

```
series.json            系列设置：系列名、徽标与水印、手、音色与语气指令、结语、目录约定（每期 init 时复制进 episode.json）
stories/               输入：故事原文，文件名就是标题，如 为什么不把狼都消灭光.txt
works/                 各期工作目录，一期一个，NN- 编号开头
  01-bihu/ 01-bihu-short/ 02-…/   01、02 两期（旧的手工流水线，见下）
  04-lang/             03 起的结构：
    episode.json         本期设置：配色、封面文案、交付文件名……
    design.json          精读与核对：资料来源、更正、叙事路线、钩子与互动的理由
    beats.full.json      完整版口播稿（role: hook / cta / outro 标出钩子、互动、结语）
    beats.short.json     精简版口播稿
    src/figures.py       插图（代码绘制，figkit）
    src/spec.py          每张图的构图、语义部位、必须看得见的叙事要求
    src/pages_*.py       两版的分页与版式
    figures/             画好的插图（看图记录 figure-review.json 针对的就是这些图）
    figure-review.json   看图记录   cover-review.json  看封面记录
    production-log.md    制作日志：每条命令自动记录，加上人工补记的判断与返工
    source/              本期用到的原文副本
    full/ short/         渲染任务目录（只入库 review.json 和 TTS 原始结果，其余可重建）
exports/               输出：NN-<标题>.mp4、NN-<标题>_封面.png、NN-<标题>_封面_4x3.png、
                       NN-<标题>_30秒版.mp4……（不入库，见“版本管理”）
```

01、02 两期是做技能之前手工搭的流水线：完整版和精简版各一个目录，脚本都在 `src/` 下，由 `src/regen.sh` 驱动。它们保留作档案，不再按这套结构维护。

## 依赖

| 依赖 | 用途 | 说明 |
|---|---|---|
| Claude Code | 驱动整个流程 | 精读核对、写稿、画图代码、看帧验收都由模型完成 |
| `science-story-video` 技能 | 本系列的制作流程（`story.py` 等脚本、figkit 画图库、配色主题、钩子与互动规则） | 在 promo-video 仓库的 `skills/science-story-video/`，软链到 `~/.claude/skills/science-story-video` |
| `sweety-handdraw-video` 技能 | 手绘渲染器：笔画动画、手臂、字幕、水印、隐私清理、验收 | 软链到 `~/.claude/skills/sweety-handdraw-video`，或设置环境变量 `SWEETY_HANDDRAW` |
| Python 3 + numpy、pillow、scipy、requests | 脚本运行环境 | |
| ffmpeg / ffprobe | 音视频处理 | |
| 豆包语音合成 2.0（火山引擎） | 整篇配音，带字级时间戳 | 在 `.env` 里设置 `VOLC_TTS_KEY`，可选 `VOLC_TTS_RESOURCE`；会读取当前目录及所有上级目录里的 `.env`。**不要提交 `.env`** |
| mlx_whisper（Apple 芯片）或 faster-whisper | 成片听写检查 | 可选，但验收需要 |
| 手写字体 Hannotate（macOS 自带） | 画面手写字和封面字 | |

检查环境：在任意一期目录里运行

```bash
SK=~/.claude/skills/science-story-video/scripts
python3 $SK/story.py doctor
```

## 做新的一期

最简单的方式：把故事放进 `stories/`，在本目录启动 Claude Code，然后说：

> 用 science-story-video 做 stories/为什么企鹅不怕冷.txt 的视频

系列约定是全自动推进、中途不提问（`series.json` 的 `confirmation`）。完成后成片和封面在 `exports/`，制作过程在该期的 `production-log.md`。

手动跑的主要步骤如下（细节见技能的 SKILL.md）：

```bash
SK=~/.claude/skills/science-story-video/scripts
python3 $SK/story.py init 05-qie --slug qie --title 为什么企鹅不怕冷 --story stories/为什么企鹅不怕冷.txt   # 建在 works/05-qie/
cd works/05-qie
# 写 design.json、beats.full.json、beats.short.json
python3 $SK/story.py beats full && python3 $SK/story.py beats short   # 字数、估计时长、钩子/互动检查
python3 $SK/story.py tts full && python3 $SK/story.py tts short       # 整篇一次合成
# 写 src/spec.py、src/figures.py
python3 $SK/story.py figures                                          # 画图，然后看 figures/sheet.png，写 figure-review.json
# 写 src/pages_full.py、src/pages_short.py
python3 $SK/story.py prepare full                                     # 第一次会要求看封面并写 cover-review.json
python3 $SK/story.py render full --preview 40 && python3 $SK/story.py sheet full --preview
python3 $SK/story.py render full && python3 $SK/story.py sheet full
python3 $SK/story.py asr full                                         # 听写对比
# 写 full/review.json
python3 $SK/story.py finalize full
# 精简版同样走 prepare → render → sheet → asr → review.json → finalize
python3 $SK/story.py deliver                                          # → exports/05-为什么企鹅不怕冷*.mp4 / *.png
```

命名规则：工作目录用 `NN-<拼音短名>`，编号顺延，统一放在 `works/` 下（`series.json` 的 `works_dir`；`init` 只给名字时自动放进去）；`--title` 用 `stories/` 里的文件名（不带 .txt）。交付文件名是“编号-标题”，例如 `05-为什么企鹅不怕冷.mp4`，不加系列名前缀，因为系列名已经在封面徽标和水印里。

## 修改已有的一期

在该期目录里改对应文件，再重跑后面的步骤：

| 改什么 | 改哪里 | 再运行 |
|---|---|---|
| 台词、钩子、互动句 | `beats.*.json`（同步 `src/spec.py` 里引用的原句） | `tts` → `prepare` → `render` → `sheet` → `asr` → `review.json` → `finalize` → `deliver` |
| 某张插图 | `src/figures.py`、`src/spec.py` | `figures <id>` → 看图，更新 `figure-review.json` → `prepare` → `render` …… |
| 版式 | `src/pages_*.py` | `prepare` → `render` …… |
| 封面文案 | `episode.json` 的 `cover` | `prepare`（重看封面，更新 `cover-review.json`）→ `render` …… |
| 配色 | `episode.json` 的 `palette` | `figures` → `prepare` → `render` …… |

`finalize` 只接受和当前成片哈希一致的 `review.json`，所以重新渲染之后，要重新看帧并重写验收记录。

## 从仓库重建

clone 下来的仓库没有渲染产物。重建一期（需要上面的依赖）：

```bash
cd works/03-shihubao
SK=~/.claude/skills/science-story-video/scripts
python3 $SK/story.py tts full      # 发现已入库的 raw.mp3 和 words.json 与稿子一致，复用它们，不重新付费合成
python3 $SK/story.py figures       # 由代码重画插图（与入库的 figures/ 对比，有变化就重看）
python3 $SK/story.py prepare full && python3 $SK/story.py render full
```

重渲后成片哈希会变，入库的 `review.json` 随即失效，需要重新看帧、听写并重写，才能 `finalize` 和 `deliver`。

## 维护

- **系列设置统一放在 `series.json`**。音色、语气指令、结语、水印、手都在这里改；新的一期 `init` 时自动带上。已有各期的 `episode.json` 不会跟着变。
- **每期做完回看 `production-log.md`**。同一类返工出现两次以上，或者某个报错要靠猜才能定位，就去改 science-story-video 技能（脚本自查、文档、默认值），并在日志末尾补记一条“已沉淀进技能”。第 04 期就这样改进了配色推荐、时长估算、spec 自查、动物站位、标签定位，并把重复的隐私清理加了缓存。
- **科学更正必须有出处**，写进 `design.json` 的 `source_scope.sources` 和 `correction`。
- **听感由人验收**。脚本和模型只能检查文字、时长、静音电平，语气、停顿和多音字需要人听。
- **默认不加背景音乐**，需要的话在剪辑软件或发布平台里配。
- **技能本身在 promo-video 仓库维护**，改了技能在那边跑测试、提交；本仓库只放内容。

## 版本管理

`.gitignore` 的原则：只收“源头”和“花了钱、花了人工、没法免费重建”的东西。

| 入库 | 不入库 |
|---|---|
| `series.json`、`stories/`、README | `exports/`：成片和封面，`deliver` 可重建，体积大，发布或备份走网盘或平台 |
| 各期的稿子、设计、`src/`、`figures/`、看图与验收记录、制作日志 | `full/`、`short/` 渲染任务目录里的其他内容：`prepare`/`render` 生成，每期约 200MB |
| `full/`、`short/` 下 `inputs/narration/` 里的 `raw.mp3`、`words.json`、`generation.json`（付费 TTS 的原始结果） | `master.wav`、`alignment.json`：由 raw.mp3 重建 |
| 01、02：`src/`、`design.json`、`review.json`、配音参数与对齐 | 01、02：渲染工作区、成片、wav 母带、插图与封面（由 `src/regen.sh` 生成） |
| | `.env`（密钥）、`.DS_Store`、`__pycache__/` |

如果确实要把成片放进仓库，用 Git LFS 跟踪 `exports/*.mp4`，不要直接提交。

提交需要手动完成，并使用 GPG 签名。远程仓库叫 `upstream`：`git@github.com:springzh/weishenme.git`。
