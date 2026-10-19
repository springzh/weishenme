# 素材目录

由 `story.py catalog` 生成，不要手改：改了 `kit/` 或技能的 figkit 之后重新生成。看图：`catalog.png`，格子左上角的编号就是下面的 #。新画角色之前先在这里找；本系列的经验和坑见 `LESSONS.md`。

<!-- catalog-of: c28426b8e9a4593a -->

## 本系列素材库（kit/）

### `ape(f, cx, cy, s=1.0, mood='happy', arm='down', fur=None)` · kit/characters.py:20

样例：#1 happy · #2 angry · #3 sad_shoulder · #4 waving · #5 spoon · #6 orangutan · #7 gorilla  （`angry`: `{'mood': 'angry'}`；`sad_shoulder`: `{'mood': 'sad', 'arm': 'shoulder'}`；`waving`: `{'arm': 'up'}`；`spoon`: `{'arm': 'spoon'}`；`orangutan`: `{'fur': (200, 146, 88)}`；`gorilla`: `{'fur': (146, 130, 122)}`）

部位：`ape_parts(name, cx, cy, s=1.0, subject='ape', prefix='')` · kit/character_parts.py:8

> Front-view cartoon ape; local frame ~640×620: head top ≈ cy-280s, feet ≈ cy+334s.
> mood: happy (smile) / angry (slanted brows + frown) / sad (droopy brows + downturned mouth).
> arm: down (both hang) / up (canvas-right arm raised, waving) /
>      spoon (canvas-right arm bent up, hand by the mouth — caller draws the spoon) /
>      shoulder (canvas-left arm reaches sideways onto a neighbour drawn earlier).

### `ape_side(f, cx, cy, s=1.0, fur=None)` · kit/characters.py:77

样例：#8 knuckle_sitting

> Side view chimp sitting knuckle-handed, facing right; (cx, cy) = ground under the hips.
> Chimp signatures: protruding muzzle past the head edge, big round ear at the back-top,
> brow over the eye, hunched rounded back, long front arm (far hand knuckles on the ground).
> Local frame (s=1): head top ≈ -296 (tuft to -314), reaching hand ≈ (190, -30) holds the stick.

### `ant(f, x, y, s=1.0)` · kit/characters.py:109

样例：#9 default  （`default`: `{'s': 4.0}`）

> A tiny ant: two body blobs + two legs, warm accent colour.

### `wolf(f, cx, cy, s=1.0, head_rot=0.0, fur=(196, 178, 150), crouch=0.0)` · kit/characters.py:124

样例：#10 standing · #11 howling · #12 pup  （`howling`: `{'head_rot': -0.6}`；`pup`: `{'s': 0.5, 'fur': (218, 204, 180)}`）

部位：`wolf_parts(name, cx, cy, s, head_rot=0.0, prefix='', subject='wolf')` · kit/character_parts.py:24

> The episode's wolf: lean body, long legs, pointed ears, bushy tail hanging down.

### `deer(f, cx, cy, s=1.0, head_rot=0.0)` · kit/characters.py:130

样例：#13 standing · #14 grazing  （`grazing`: `{'head_rot': 1.05}`）

部位：`deer_parts(name, cx, cy, s, head_rot=0.0, prefix='', subject='deer')` · kit/character_parts.py:29

> The deer (elk): slim body, long legs, branched antlers. head_rot ≈ 1.05 lowers the head to graze.

### `fence(f, x0, x1, y0, y1, step=60)` · kit/characters.py:137

样例：#15 zoo  （`zoo`: 自定义调用）

> Zoo enclosure: two rails and vertical bars (all ink strokes).


## kit/ 里没有样例图的函数

- `ground_part(name='ground', what='地面外框一笔')` · kit/character_parts.py:34 — The FULL catch-all for a scene's ground. List it LAST, and only when ground / grass ink is left for it to own.

## 技能自带（figkit / partkit）

### `sanlian(f, cx, cy, gap=130, r=44)` · figkit.py:239

样例：#16 default

> 一键三连 row: heart (like), coin, star (favourite), left → right.

### `sun(f, cx, cy, r=60, rays=8, fill=None)` · figkit.py:253

样例：#17 default

### `cloud(f, cx, cy, s=1.0, fill=None)` · figkit.py:261

样例：#18 default

### `tree(f, x, y_ground, h=300, crown=None, trunk=None)` · figkit.py:302

样例：#19 default

### `magnifier(f, cx, cy, r, handle=True)` · figkit.py:309

样例：#20 default  （`default`: `{'r': 110}`）

> Lens rim (ink ring) + handle. Draw the magnified content first, inside radius r-10.

### `kid(f, cx, cy, s=1.0, mood='cold', hat=True, scarf=True, coat=None)` · figkit.py:353

样例：#21 cold · #22 happy · #23 curious  （`happy`: `{'mood': 'happy', 'hat': False, 'scarf': False}`；`curious`: `{'mood': 'curious', 'hat': False, 'scarf': False}`）

部位：`kid_parts(name, cx, cy, s=1.0, subject='kid', prefix='')` · partkit.py:70

> Front-view child, ~ 330×650 local units centred on (cx, cy) (head top ≈ cy-310s, boots ≈ cy+330s).
> 
> mood: "cold" (round shivering mouth), "happy" (smile), "curious" (small o + raised brows).
> Pairs with partkit.kid_parts(name, cx, cy, s) for the six human parts.

### `quadruped(f, cx, cy, s=1.0, head_rot=0.0, crouch=0.0, lw=6, fur=None, fur2=None, ear='round', tail='stub', snout=1.0, rot=0.0, mane=None, pattern=None, pattern_color=None, eye_glow=None, head='long', stride=0.0, body='stocky', leg=0, antlers=None)` · figkit.py:395

样例：#24 bear · #25 wolf_like · #26 big_cat · #27 deer_like  （`wolf_like`: `{'ear': 'pointed', 'tail': 'down', 'snout': 1.08, 'body': 'slim', 'leg': 45}`；`big_cat`: `{'head': 'round', 'tail': 'long', 'pattern': 'stripes'}`；`deer_like`: `{'ear': 'pointed', 'body': 'slim', 'leg': 60, 'snout': 0.92, 'antlers': (228, 208, 172)}`）

部位：`quadruped_parts(name, cx, cy, s=1.0, head_rot=0.0, crouch=0.0, legs=True, body_bottom=78, subject='animal', exclude=[[180, 215, 0.02, 0.85]], rot=0.0, stride=0.0, leg=0, tail='stub', antlers=False, prefix='')` · partkit.py:84

> Side-view four-legged animal facing right (bear-like by default). Local frame: body ≈ x -255..205,
> y -140..72; feet at y = leg_len(crouch)+17; nose ≈ x 384·snout. head_rot > 0 lowers the head;
> rot tilts the whole animal (negative = nose up: leaping, climbing). mane: colour of a lion's mane;
> pattern: "stripes" (tiger) or "spots" (leopard); eye_glow: colour of eyes shining in the dark.
> head: "long" (bear, dog) or "round" (cats: lion, tiger, leopard, house cat). stride 0..1 swings the front legs
> forward and the hind legs back (running, leaping: lift the animal so the feet leave the ground).
> fur2 (far legs) defaults to fur darkened by 8%.
> Beyond bears and cats (wolf / dog / fox / deer):
>   body="slim" + leg=45 — a lean body on longer legs (wolf, dog, deer); leg adds to the leg length
>   tail="down" (wolf: bushy, hanging), "curl" (dog: curled up over the back), "bushy" (fox: long, level)
>   ear="pointed" | "round" | "floppy" (dog: hangs beside the head) ; antlers=<colour> (deer: branched antlers)
> 
> Order matters: far legs → near legs → tail → body (covers leg tops) → ear → head. Pairs with
> partkit.quadruped_parts(name, cx, cy, s, head_rot, crouch).

### `lying(f, cx, cy, s=1.0, fur=None, mane=None, pattern=None, pattern_color=None, ear='round', asleep=True, tail_tip=None)` · figkit.py:508

样例：#28 asleep · #29 lion  （`lion`: `{'mane': (196, 122, 66)}`）

部位：`lying_parts(name, cx, cy, s=1.0, subject='animal', prefix='', exclude=None)` · partkit.py:103

> Animal lying on the ground, facing right, head resting above its front paws (sleeping big cat, cat, dog).
> Local frame: ground at y=0, body x -160..130, head centre (150, -70), paws to x ≈ 225. Pairs with
> partkit.lying_parts(name, cx, cy, s). Draw order: tail → haunch → body → pattern → mane → ears → head → paws.

### `sheep(f, cx, cy, s=1.0, wool=(240, 236, 226), face=(150, 132, 118))` · figkit.py:551

样例：#30 default

> A sheep: woolly scalloped body over a quadruped frame with a darker face (a plain pale quadruped reads as a bear).

### `hare(f, cx, cy, s=1.0, fur=None)` · figkit.py:559

样例：#31 default

> Side-view wild hare sitting, facing right; (cx, cy) = ground under its body.

### `mouse(f, cx, cy, s=1.0, fur=None)` · figkit.py:573

样例：#32 default

> Small field mouse / vole, facing right; (cx, cy) = ground.

### `beaver(f, cx, cy, s=1.0, fur=None)` · figkit.py:584

样例：#33 default

> Beaver sitting by the water, facing right, with its flat tail; (cx, cy) = ground.

### `bird(f, cx, cy, s=1.0, color=None, flying=False)` · figkit.py:596

样例：#34 perched · #35 flying  （`flying`: `{'flying': True}`）

> A small bird: perched (round body, facing right) or flying (two wing strokes).

### `sapling(f, x, y_ground, h=110, leaf=None)` · figkit.py:608

样例：#36 default

> A young tree: thin stem with three small leaves.

### `stump(f, x, y_ground, w=26, h=30)` · figkit.py:616

样例：#37 default

> A chewed-off sapling / stump: short stem with a jagged top.

