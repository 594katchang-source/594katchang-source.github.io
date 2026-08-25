# -*- coding: utf-8 -*-
"""
更新與同步 blog/posts.json
"""
import json
from pathlib import Path
import sys

sys.stdout.reconfigure(encoding='utf-8')

ROOT_DIR = Path(r"d:\@Codex\594katchang-source.github.io-main")
POSTS_FILE = ROOT_DIR / "blog" / "posts.json"
REMOTE_CANDIDATE = ROOT_DIR / "work" / "2026-08-15-seo-review-docs" / "source" / "remote-posts-candidate.json"
CH7_FILE = ROOT_DIR / "work" / "2026-08-15-seo-review-docs" / "source" / "chapter-07-publish.json"

from seo_ai_keywords_auditor import OPTIMIZED_DATA

# 讀取現有 posts.json
current_data = json.loads(POSTS_FILE.read_text(encoding="utf-8"))
posts_map = {p["id"]: p for p in current_data.get("posts", [])}

# 讀取 candidate
if REMOTE_CANDIDATE.exists():
    cand_data = json.loads(REMOTE_CANDIDATE.read_text(encoding="utf-8"))
    for p in cand_data.get("posts", []):
        if p["id"] not in posts_map:
            posts_map[p["id"]] = p

# 讀取 chapter 7 (維生素)
if CH7_FILE.exists():
    ch7 = json.loads(CH7_FILE.read_text(encoding="utf-8"))
    ch7_id = "2026-08-25-vitamins-book-notes"
    ch7["id"] = ch7_id
    ch7["date"] = "2026-08-25"
    ch7["category"] = "書籍連載與營養知識"
    posts_map[ch7_id] = ch7
    if "2026-08-23-vitamins-book-notes" in posts_map:
        del posts_map["2026-08-23-vitamins-book-notes"]

# 將優化後的 category, keywords, date 套用至每篇文章
final_posts = list(posts_map.values())

for p in final_posts:
    pid = p["id"]
    if pid in OPTIMIZED_DATA:
        opt = OPTIMIZED_DATA[pid]
        p["category"] = opt["category"]
        p["keywords"] = opt["keywords"]
        if "date" in opt:
            p["date"] = opt["date"]
    elif pid == "2026-08-23-vitamins-book-notes" or pid == "2026-08-25-vitamins-book-notes":
        opt = OPTIMIZED_DATA["2026-08-25-vitamins-book-notes"]
        p["id"] = "2026-08-25-vitamins-book-notes"
        p["category"] = opt["category"]
        p["keywords"] = opt["keywords"]
        p["date"] = opt["date"]

# 依日期由新到舊排序
final_posts.sort(key=lambda x: x.get("date", ""), reverse=True)

output_json = {"posts": final_posts}
POSTS_FILE.write_text(json.dumps(output_json, ensure_ascii=False, indent=2), encoding="utf-8")
print(f"[✓] 成功更新 blog/posts.json，共 {len(final_posts)} 篇文章。")
for idx, p in enumerate(final_posts):
    print(f"  {idx+1:02d}. [{p.get('date')}] [{p.get('category')}] {p.get('title')[:32]}... ({len(p.get('keywords', []))} keywords)")
