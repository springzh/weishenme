"""本系列角色的语义部位：各期 src/spec.py 里 `from character_parts import *` 就能用。

每个函数和 characters.py 里同名角色（去掉 _parts）一一对应，局部坐标必须一致：改了角色的造型，同步改这里的框。
"""
from partkit import *


def ape_parts(name, cx, cy, s=1.0, subject="ape", prefix=""):
    """head / torso(含双臂) / legs boxes matching characters.ape(f, cx, cy, s) (any mood / arm)."""
    g = lambda x0, y0, x1, y1: pose(name, rect(x0, y0, x1, y1), cx, cy, s)
    return [
        P(prefix + "head", subject, "head",
          ["两只耳朵各一圈", "头部一圈", "脸庞一圈", "两只眼睛", "眉毛", "嘴巴"],
          g(-140, -320, 140, -100)),
        P(prefix + "torso", subject, "torso",
          ["两只手臂各一笔", "身体外形一笔", "肚皮一圈"],
          g(-200, -140, 200, 220)),
        P(prefix + "legs", subject, "legs",
          ["两条腿各一笔", "两只脚各一圈"],
          g(-140, 120, 140, 345)),
    ]


def wolf_parts(name, cx, cy, s, head_rot=0.0, prefix="", subject="wolf"):
    """head / body / legs matching characters.wolf(f, cx, cy, s, head_rot)."""
    return quadruped_parts(name, cx, cy, s, head_rot=head_rot, leg=45, tail="down", subject=subject, prefix=prefix)


def deer_parts(name, cx, cy, s, head_rot=0.0, prefix="", subject="deer"):
    """head (with antlers) / body / legs matching characters.deer(f, cx, cy, s, head_rot)."""
    return quadruped_parts(name, cx, cy, s, head_rot=head_rot, leg=60, antlers=True, subject=subject, prefix=prefix)


def ground_part(name="ground", what="地面外框一笔"):
    """The FULL catch-all for a scene's ground. List it LAST, and only when ground / grass ink is left for it to own."""
    return P(name, "ground", "ground", [what], FULL)
