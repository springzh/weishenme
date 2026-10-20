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


def kangaroo_parts(name, cx, cy, s=1.0, pose="stand", subject="kangaroo", prefix=""):
    """tail / head / body (含育儿袋、前爪) / legs boxes matching characters.kangaroo(f, cx, cy, s, pose).
    pose="leap" is the airborne pose. List them in this order: the tail and head are declared before the body,
    the body before the legs, so each keeps the pixels it draws."""
    g = lambda x0, y0, x1, y1: pose_rect(name, rect(x0, y0, x1, y1), cx, cy, s)
    if pose == "leap":
        return [
            P(prefix + "tail", subject, "tail", ["尾巴外框一笔"], g(-390, -345, -110, -275)),
            P(prefix + "head", subject, "head", ["两只耳朵各一笔", "头部外形一笔", "吻部一圈", "眼睛", "鼻子"],
              g(110, -520, 330, -355)),
            P(prefix + "body", subject, "torso", ["身体外形一笔", "肚皮", "两只前爪各一笔", "腹部圆圈"],
              g(-160, -430, 185, -255)),
            P(prefix + "legs", subject, "legs", ["远侧后腿一笔", "远侧脚一圈", "近侧后腿一笔", "近侧脚一圈"],
              g(-310, -350, -130, -185)),
        ]
    return [
        P(prefix + "tail", subject, "tail", ["尾巴外框一笔"], g(-380, -330, -40, -8)),
        P(prefix + "head", subject, "head", ["远耳一笔", "头形一笔", "近耳一笔", "吻部一圈", "眼睛", "鼻子", "嘴线", "眉毛"],
          g(80, -670, 295, -430)),
        P(prefix + "body", subject, "torso", ["身体外形一笔", "育儿袋一圈", "袋口一笔", "近侧前臂一笔", "前爪一圈"],
          g(-82, -510, 182, -180)),
        P(prefix + "legs", subject, "legs", ["远侧后腿一笔", "远侧脚一圈", "近侧大腿一笔", "近侧小腿一笔", "近侧脚一圈", "脚趾线"],
          g(-30, -350, 215, 6)),
    ]


def joey_parts(name, cx, cy, s=1.0, subject="joey", prefix=""):
    """head (head end, closed eye, nose) / body (bean body, claws, tail) matching characters.joey_bean."""
    g = lambda x0, y0, x1, y1: pose_rect(name, rect(x0, y0, x1, y1), cx, cy, s)
    return [
        P(prefix + "head", subject, "head", ["头端一圈", "闭着的眼睛", "小鼻子"], g(8, -52, 62, 12)),
        P(prefix + "body", subject, "torso", ["豆子身体一笔", "两只小爪", "卷尾巴"], g(-82, -52, 18, 46)),
    ]


def pose_rect(name, local, cx, cy, s=1.0):
    """`pose()` without shadowing the kangaroo's own pose argument."""
    return pose(name, local, cx, cy, s)


def ground_part(name="ground", what="地面外框一笔"):
    """The FULL catch-all for a scene's ground. List it LAST, and only when ground / grass ink is left for it to own."""
    return P(name, "ground", "ground", [what], FULL)
