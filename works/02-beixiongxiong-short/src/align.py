"""Map mlx_whisper word timestamps onto the locked script -> inputs/narration/alignment.json."""
import json, hashlib, difflib, re, subprocess, numpy as np, wave, sys
beats = json.load(open("src/beats.json"))
asr = json.load(open("work/asr/doubao_raw.json"))
PUNCT = re.compile(r"[\s，。：？！、,.:?!；;“”\"']")
# per-character times from ASR words
achars, atimes = [], []
for seg in asr["segments"]:
    for w in seg["words"]:
        t = PUNCT.sub("", w["word"])
        n = len(t)
        for i, c in enumerate(t):
            a = w["start"] + (w["end"] - w["start"]) * i / max(n, 1)
            b = w["start"] + (w["end"] - w["start"]) * (i + 1) / max(n, 1)
            achars.append(c); atimes.append((a, b))
# script chars (non-punct) with index map
schars, sidx = [], []
full = "".join(b["text"] for b in beats)
for i, c in enumerate(full):
    if not PUNCT.match(c): schars.append(c); sidx.append(i)
sm = difflib.SequenceMatcher(None, schars, achars, autojunk=False)
stime = [None] * len(schars)
for op, i1, i2, j1, j2 in sm.get_opcodes():
    if op == "equal" or (op == "replace" and i2 - i1 == j2 - j1):
        for k in range(i2 - i1): stime[i1 + k] = atimes[j1 + k]
    elif op == "replace":
        a, b = atimes[j1][0], atimes[j2 - 1][1]
        for k in range(i2 - i1): stime[i1 + k] = (a + (b - a) * k / (i2 - i1), a + (b - a) * (k + 1) / (i2 - i1))
missing = [schars[i] for i, t in enumerate(stime) if t is None]
print("unmatched script chars:", "".join(missing), file=sys.stderr)
# interpolate any gaps
for i in range(len(stime)):
    if stime[i] is None:
        prev = next((stime[j] for j in range(i - 1, -1, -1) if stime[j]), (0, 0))
        stime[i] = (prev[1], prev[1])
pos2t = {sidx[k]: stime[k] for k in range(len(sidx))}
def span(a, b):
    ts = [pos2t[p] for p in range(a, b) if p in pos2t]
    return ts[0][0], ts[-1][1]
src = open("inputs/narration/master.wav", "rb").read()
dur = float(subprocess.check_output(["ffprobe","-v","error","-show_entries","format=duration","-of","csv=p=0","inputs/narration/master.wav"]))
out, off, prev_end = [], 0, 0.0
for bi, b in enumerate(beats):
    t = b["text"]; s, e = span(off, off + len(t))
    s = max(s - 0.08, prev_end + 0.01); e = min(e + 0.12, dur)
    # caption cues: split at sentence/comma, merge pieces to <=20 chars
    parts = re.findall(r"[^，。：？！]*[，。：？！]?", t); parts = [p for p in parts if p]
    cues, cur = [], ""
    for p in parts:
        if cur and (len(cur) + len(p) > 20 or (cur[-1] in "。？！" and len(cur) >= 6)): cues.append(cur); cur = p
        else: cur += p
    if cur: cues.append(cur)
    cue_objs, co = [], off
    for ci, c in enumerate(cues):
        cs, ce = span(co, co + len(c)); co += len(c)
        cue_objs.append({"text": c, "start": round(max(cs - s, 0), 3), "end": round(min(ce - s + 0.1, e - s), 3)})
    for ci in range(len(cue_objs) - 1):  # no overlap; keep text until next starts
        cue_objs[ci]["end"] = round(min(cue_objs[ci]["end"], cue_objs[ci + 1]["start"]), 3)
    cue_objs[0]["start"] = 0
    cue_objs[-1]["end"] = round(e - s, 3)
    out.append({"id": b["id"], "text": t, "start": round(s, 3), "end": round(e, 3), "caption_cues": cue_objs})
    prev_end = e; off += len(t)
json.dump({"version": 1, "source_sha256": hashlib.sha256(src).hexdigest(),
           "script_sha256": hashlib.sha256(full.encode()).hexdigest(), "beats": out},
          open("inputs/narration/alignment.json", "w"), ensure_ascii=False, indent=1)
for b in out: print(b["id"], b["start"], b["end"], [c["text"] for c in b["caption_cues"]])
