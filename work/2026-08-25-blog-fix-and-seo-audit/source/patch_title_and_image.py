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
        p["id"] = "2026-08-25-vitamins-book-notes"
        p["title"] = "維生素怎麼吃？從脂溶性、水溶性到補充品風險"
        p["date"] = "2026-08-25"
        p["image"] = "images/2026-08-23-vitamins-book-notes.png"
        p["category"] = "書籍連載與營養知識"
        p["keywords"] = ["維生素怎麼吃", "脂溶性與水溶性維生素", "維生素D日曬補充", "維生素B群提神迷思", "葉酸孕婦劑量", "維生素C感冒", "維生素K抗凝血藥"]
    elif "protein" in p["id"]:
        p["image"] = "images/2026-08-22-proteins-amino-acids-book-notes.jpg"
        p["category"] = "書籍連載與營養知識"

# 依日期降序排列
posts.sort(key=lambda x: x.get("date", ""), reverse=True)

POSTS_FILE.write_text(json.dumps({"posts": posts}, ensure_ascii=False, indent=2), encoding="utf-8")
print("[✓] posts.json 已成功修正維生素篇標題與封面圖路徑！")
