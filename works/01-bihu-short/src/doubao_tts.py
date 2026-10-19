"""Synthesize the full narration in one Doubao (Volcengine seed-tts-2.0) request -> inputs/narration/master.wav.
Key loaded at runtime from the promo-video .env (never printed)."""
import base64, json, os, pathlib, subprocess, sys, hashlib
sys.path.insert(0, "/Users/spring-kite/Dev/ai/ai_coding/promo-video/skills/promo-video/scripts")
os.chdir("/Users/spring-kite/Dev/ai/ai_coding/promo-video")
from env import load_env
load_env()
os.chdir(pathlib.Path(__file__).resolve().parents[1])
import requests
VOICE = sys.argv[1] if len(sys.argv) > 1 else "zh_male_m191_uranus_bigtts"
RATE = int(sys.argv[2]) if len(sys.argv) > 2 else 0
beats = json.load(open("src/beats.json"))
SUFFIX = "我们下期再见。"  # protection suffix, removed at a natural pause after the real last word
text = "".join(b["text"] for b in beats) + SUFFIX
r = requests.post("https://openspeech.bytedance.com/api/v3/tts/unidirectional", stream=True, timeout=300,
    headers={"X-Api-Key": os.environ["VOLC_TTS_KEY"], "X-Api-Resource-Id": os.environ.get("VOLC_TTS_RESOURCE", "seed-tts-2.0")},
    json={"user": {"uid": "bihu-short-handdraw"}, "req_params": {"text": text, "speaker": VOICE,
          "audio_params": {"format": "pcm", "sample_rate": 24000, "speech_rate": RATE}}})
if not r.ok: sys.exit(f"HTTP {r.status_code}: {r.text[:300]}")
pcm = b""
for ln in r.iter_lines():
    if not ln: continue
    m = json.loads(ln)
    if m.get("data"): pcm += base64.b64decode(m["data"])
    code = m.get("code", m.get("header", {}).get("code"))
    if code not in (0, 20000000, None): sys.exit(f"TTS error: {m}")
out = pathlib.Path("inputs/narration"); out.mkdir(parents=True, exist_ok=True)
(out / "raw.pcm").write_bytes(pcm)
subprocess.run(["ffmpeg", "-y", "-loglevel", "error", "-f", "s16le", "-ar", "24000", "-ac", "1", "-i", str(out / "raw.pcm"),
                "-ar", "48000", str(out / "doubao_raw.wav")], check=True)
(out / "raw.pcm").unlink()
json.dump({"engine": "volcengine seed-tts-2.0 unidirectional", "speaker": VOICE, "speech_rate": RATE,
           "text_sha256": hashlib.sha256(text.encode()).hexdigest(), "requests": 1, "protection_suffix": SUFFIX, "delivered_text_excludes_suffix": True}, open(out / "generation.json", "w"), ensure_ascii=False, indent=1)
print("seconds", len(pcm) / 48000)
