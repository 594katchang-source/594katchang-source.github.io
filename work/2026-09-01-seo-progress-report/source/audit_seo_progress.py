import os
import sys
import json
import re
import xml.etree.ElementTree as ET

sys.stdout.reconfigure(encoding='utf-8')

ROOT_DIR = rd:\@Codex\594katchang-source.github.io-main
POSTS_FILE = os.path.join(ROOT_DIR, blog, posts.json)
SITEMAP_XML = os.path.join(ROOT_DIR, sitemap.xml)
SITEMAP_HTML = os.path.join(ROOT_DIR, sitemap.html)
LLMS_TXT = os.path.join(ROOT_DIR, llms.txt)
LLMS_FULL_TXT = os.path.join(ROOT_DIR, llms-full.txt)
ROBOTS_TXT = os.path.join(ROOT_DIR, robots.txt)

REVIEW_DOCS_DIR = os.path.join(ROOT_DIR, work, 2026-08-15-seo-review-docs, output)
BOOK_SOURCE_DIR = rD:\@Codex\書籍\2026-07-29-Nutrition-Concepts-Controversies-17e\output

def audit_posts():
    with open(POSTS_FILE, r, encoding=utf-8) as f:
        posts = json.load(f)
    print(f=== Blog Posts Audit (Total: {len(posts)}) ===)
    book_series_count = 0
    home_count = 0
    for idx, p in enumerate(posts, 1):
        pid = p.get(id)
        title = p.get(title)
        date = p.get(date)
        cat = p.get(category, 未分類)
        home = p.get(showOnHome, False)
        keywords = p.get(keywords, [])
        content = p.get(content, ")
 # rough word count without html
 clean_text = re.sub(r'<[^>]+>', '', content).strip()
 word_count = len(clean_text)
 if home:
 home_count += 1
 if cat == 書籍連載與營養知識 or 連載 in cat:
 book_series_count += 1
 print(f[{idx}] ID: {pid} | 日期: {date} | 分類: {cat} | 首頁: {home} | 字數: {word_count} | 關鍵字數: {len(keywords)})
 print(f    標題: {title})
 print(f\n摘要統計: 總文章數={len(posts)}, 書籍連載篇數={book_series_count}, 首頁精選篇數={home_count})
 return posts

def audit_sitemaps():
 print(f\n=== Sitemaps & AI Index Files Audit ===)
 # XML
 if os.path.exists(SITEMAP_XML):
 tree = ET.parse(SITEMAP_XML)
 root = tree.getroot()
 urls = [elem.text for elem in root.findall(.//{http://www.sitemaps.org/schemas/sitemap/0.9}loc)]
 print(fsitemap.xml: 包含 {len(urls)} 個 URL)
 for u in urls:
 print(f  - {u})
 else:
 print(sitemap.xml 不存在！)

 # LLMS.TXT
 if os.path.exists(LLMS_TXT):
 with open(LLMS_TXT, r, encoding=utf-8) as f:
 llms_content = f.read()
 llms_lines = [l for l in llms_content.splitlines() if l.strip()]
 print(fllms.txt: {len(llms_lines)} 行)
 
 # ROBOTS.TXT
 if os.path.exists(ROBOTS_TXT):
 with open(ROBOTS_TXT, r, encoding=utf-8) as f:
 robots_content = f.read()
 print(frobots.txt: 長度 {len(robots_content)} bytes)

def audit_review_queue():
 print(f\n=== Review Docs & Drafts Audit in work/2026-08-15-seo-review-docs/output/ ===)
 if os.path.exists(REVIEW_DOCS_DIR):
 files = os.listdir(REVIEW_DOCS_DIR)
 for f in sorted(files):
 fpath = os.path.join(REVIEW_DOCS_DIR, f)
 size = os.path.getsize(fpath)
 print(f - {f} ({size:,} bytes))
 else:
 print(REVIEW_DOCS_DIR 不存在)

if __name__ == __main__:
 audit_posts()
 audit_sitemaps()
 audit_review_queue()
