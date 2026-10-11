# -*- coding: utf-8 -*-
import sys
import json
import re
from pathlib import Path

sys.stdout.reconfigure(encoding='utf-8')

root = Path(r"d:\@Codex\594katchang-source.github.io-main")
data = json.loads((root / "teach/activity-database/activities_full.json").read_text(encoding="utf-8"))
items = data["activities"]
html = (root / "teach/activity-database/index.html").read_text(encoding="utf-8")

print(f"Total items: {len(items)}")
for label, idx in [("首項 (First)", 0), ("中項 (Middle)", len(items)//2), ("末項 (Last)", -1)]:
    it = items[idx]
    print(f"[{label}] UID={it['uid']} | YT_ID={it['id']} | Source={it['source_db']} | Title={it['title']} | Cat={it['cat']} | Subcats={it['subcats']} | AnalysisKeys={len(it['analysis'])}")

for attr, field, is_list in [
    ("data-cat", "cat", False),
    ("data-subcat", "subcats", True),
    ("data-ab", "abilities", True),
    ("data-aud", "audiences", True),
    ("data-mat", "mat_groups", True),
    ("data-lv", "level", False),
    ("data-dur", "dur_bucket", False),
    ("data-reg", "region", True),
]:
    vals = re.findall(rf'{attr}="([^"]+)"', html)
    zero = []
    for v in vals:
        if v == "ALL":
            continue
        if is_list:
            cnt = sum(1 for x in items if v in x.get(field, []))
        else:
            cnt = sum(1 for x in items if x.get(field) == v)
        if cnt == 0:
            zero.append(v)
    print(f"Filter {attr}: {len(vals)} chips | Zero-match chips: {zero}")
