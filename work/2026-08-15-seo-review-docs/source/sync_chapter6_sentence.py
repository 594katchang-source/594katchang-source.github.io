from __future__ import annotations

import json
import sys
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8")

SOURCE = Path(__file__).with_name("chapter-06-publish.json")
OLD = "蛋白質不能夠只強調在健身上，太過簡化了。"
NEW = "談蛋白質的功能，不能只聚焦在健身用途上，這樣的理解太過簡化了。"

raw = SOURCE.read_text(encoding="utf-8")
count = raw.count(OLD)
if count != 1:
    raise SystemExit(f"expected exactly one old sentence, found {count}")

updated = raw.replace(OLD, NEW)
json.loads(updated)
SOURCE.write_text(updated, encoding="utf-8", newline="")
print(f"updated={SOURCE}")
print(f"replacements={count}")
