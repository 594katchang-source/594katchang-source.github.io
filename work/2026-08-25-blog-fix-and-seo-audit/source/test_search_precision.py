# -*- coding: utf-8 -*-
import json
import re
from pathlib import Path
import sys

sys.stdout.reconfigure(encoding='utf-8')

ROOT_DIR = Path(r"d:\@Codex\594katchang-source.github.io-main")
posts = json.loads((ROOT_DIR / "blog" / "posts.json").read_text(encoding="utf-8"))["posts"]

print("=== 1. 檢查文章清單、日期與分類 ===")
for p in posts:
    print(f"[{p.get('date')}] [{p.get('category')}] {p.get('title')[:30]}... (關鍵字數: {len(p.get('keywords', []))})")

print("\n=== 2. 測試站內關鍵字搜尋精準度 ===")
test_queries = [
    "維生素D", "B群", "葉酸", "蛋白質", "必需胺基酸", 
    "超商早餐", "食物過敏", "阿茲海默", "Omega-3", "膳食纖維", "DRI", "營養標示"
]

def strip_html(s=""):
    return re.sub(r"\s+", " ", re.sub(r"<[^>]*>", " ", str(s))).strip()

def search_val(post):
    vals = [
        post.get("title", ""),
        post.get("excerpt", ""),
        post.get("body", ""),
        post.get("category", "")
    ] + post.get("keywords", [])
    return " ".join([strip_html(v) for v in vals]).lower()

for q in test_queries:
    matched = [p for p in posts if q.lower() in search_val(p)]
    titles = " | ".join([m["title"][:16] for m in matched])
    print(f"🔍 查詢【{q}】-> 命中 {len(matched)} 篇：{titles}")
