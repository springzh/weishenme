#!/bin/zsh
# bind evidence -> draw -> clean -> cover -> clean -> records (order required by the art-direction gate)
set -e
S=~/.claude/skills/sweety-handdraw-video/scripts
python3 src/plan.py && python3 $S/drawing_contract.py . design/drawing-plan.json >/dev/null
python3 src/briefs.py && python3 $S/art_direction.py bind-evidence design/art-direction.json
python3 src/draw_figures.py >/dev/null
for f in inputs/figures/*.png; do python3 $S/clean_image.py $f --audit ${f%.png}.privacy.json >/dev/null; done
python3 src/cover.py && python3 $S/clean_image.py inputs/cover.png --audit inputs/cover.privacy.json >/dev/null
python3 src/records.py && python3 src/layout.py
