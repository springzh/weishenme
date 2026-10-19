import json, sys
sys.path.insert(0, "src"); from spec import SPECS
plans = []
for iid, s in SPECS.items():
    parts = [{"id": p["id"], "subject": p["subject"], "role": p["role"], "stroke_groups": p["stroke_groups"]} for p in s["parts"]]
    d = {"id": iid, "composition": s["composition"], "drawability_reason": s["why"], "outline_strategy": "visible_source_ink",
         "subjects": [{"id": a, "kind": k} for a, k in s["subjects"]], "parts": parts,
         "outline_order": [p["id"] for p in parts], "fill_order": [p["id"] for p in parts],
         "spatial_order": "top_to_bottom_left_to_right", "narrative_requirements": s["reqs"]}
    if s.get("exception"): d["spatial_order"] = "custom"; d["order_exception"] = s["exception"]
    plans.append(d)
json.dump({"illustrations": plans}, open("design/drawing-plan.json", "w"), ensure_ascii=False, indent=1)
