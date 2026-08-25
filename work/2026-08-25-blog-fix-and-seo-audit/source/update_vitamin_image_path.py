# -*- coding: utf-8 -*-
import json
from pathlib import Path
import sys

sys.stdout.reconfigure(encoding='utf-8')

ROOT_DIR = Path(r"d:\@Codex\594katchang-source.github.io-main")
POSTS_FILE = ROOT_DIR / "blog" / "posts.json"

data = json.loads(POSTS_FILE.read_text(encoding="utf-8"))
posts = data.get("posts", [])

for p in posts:
    if "vitamin" in p["id"]:
        p["image"] = "images/2026-08-25-vitamins-book-notes.png"

POSTS_FILE.write_text(json.dumps({"posts": posts}, ensure_ascii=False, indent=2), encoding="utf-8")
print("[✓] posts.json 已將維生素篇封面圖路徑更新為 images/2026-08-25-vitamins-book-notes.png！")
