# -*- coding: utf-8 -*-
"""
Milestone 4 Audit Script: 全站內鏈網與長尾排名追蹤分析工具
"""
import os
import sys
import json
import re
from pathlib import Path
from bs4 import BeautifulSoup
from urllib.parse import urlparse

sys.stdout.reconfigure(encoding='utf-8')

ROOT_DIR = Path(r"d:\@Codex\594katchang-source.github.io-main")
BASE_HOST = "594katchang-source.github.io"

CORE_PAGES = [
    ("index.html", "首頁", "https://594katchang-source.github.io/"),
    ("about.html", "個人簡介", "https://594katchang-source.github.io/about.html"),
    ("class.html", "授課講座", "https://594katchang-source.github.io/class.html"),
    ("blog/index.html", "衛教專欄首頁", "https://594katchang-source.github.io/blog/"),
    ("teach/index.html", "教學工具首頁", "https://594katchang-source.github.io/teach/"),
    ("teach/nutritionranking/index.html", "教具：營養排行榜", "https://594katchang-source.github.io/teach/nutritionranking/"),
    ("teach/paper-radar/index.html", "教具：論文讀書小站", "https://594katchang-source.github.io/teach/paper-radar/"),
    ("teach/Stress-Food/index.html", "教具：壓力與食物關係", "https://594katchang-source.github.io/teach/Stress-Food/"),
    ("teach/emotion-cards/index.html", "教具：情緒營養字卡", "https://594katchang-source.github.io/teach/emotion-cards/"),
    ("teach/nutrition-battle/index.html", "教具：營養大作戰", "https://594katchang-source.github.io/teach/nutrition-battle/"),
    ("sitemap.html", "網站地圖 (HTML)", "https://594katchang-source.github.io/sitemap.html"),
]

page_html_map = {}
for rel_path, name, url in CORE_PAGES:
    file_path = ROOT_DIR / rel_path
    if file_path.exists():
        page_html_map[url] = {
            "name": name,
            "type": "Core/Tool",
            "html": file_path.read_text(encoding="utf-8", errors="ignore"),
            "file": str(file_path)
        }

posts_file = ROOT_DIR / "blog" / "posts.json"
posts = []
if posts_file.exists():
    posts_data = json.loads(posts_file.read_text(encoding="utf-8"))
    posts = posts_data.get("posts", [])

for p in posts:
    pid = p.get("id")
    title = p.get("title")
    post_url = f"https://594katchang-source.github.io/blog/post.html?id={pid}"
    body_html = p.get("body", "")
    page_html_map[post_url] = {
        "name": f"文章：{title}",
        "type": "Article",
        "html": body_html,
        "raw_post": p
    }

print(f"[*] 總共納入盤點節點數：{len(page_html_map)} 個 (11 個核心/教具分頁 + {len(posts)} 篇專文)")

def normalize_internal_url(href):
    if not href or href.startswith("#") or href.startswith("javascript:") or href.startswith("mailto:") or href.startswith("tel:"):
        return None
    if href.startswith("http://") or href.startswith("https://"):
        parsed = urlparse(href)
        if parsed.netloc == BASE_HOST or "594katchang-source.github.io" in parsed.netloc:
            path = parsed.path
            query = f"?{parsed.query}" if parsed.query else ""
            if path == "" or path == "/":
                return "https://594katchang-source.github.io/"
            return f"https://594katchang-source.github.io{path}{query}"
        return None
    if href.startswith("/"):
        return f"https://594katchang-source.github.io{href}"
    elif href.startswith("../"):
        return f"https://594katchang-source.github.io/{href.replace('../', '')}"
    else:
        return f"https://594katchang-source.github.io/{href}"

internal_links = []
node_outgoing = {url: [] for url in page_html_map}
node_incoming = {url: [] for url in page_html_map}

for src_url, info in page_html_map.items():
    soup = BeautifulSoup(info["html"], "html.parser")
    for a in soup.find_all("a", href=True):
        raw_href = a["href"].strip()
        norm_target = normalize_internal_url(raw_href)
        if norm_target:
            anchor_text = a.get_text(strip=True)
            if not anchor_text:
                img = a.find("img")
                if img and img.get("alt"):
                    anchor_text = f"[圖片Alt: {img['alt']}]"
                else:
                    anchor_text = "[無文字連結]"
            clean_target = norm_target.rstrip("/") if not norm_target.endswith(".html") and not "?" in norm_target else norm_target
            if clean_target == "https://594katchang-source.github.io":
                clean_target = "https://594katchang-source.github.io/"
            item = {
                "source_url": src_url,
                "source_name": info["name"],
                "source_type": info["type"],
                "target_url": clean_target,
                "anchor_text": anchor_text,
                "raw_href": raw_href
            }
            internal_links.append(item)
            node_outgoing[src_url].append(item)
            if clean_target in node_incoming:
                node_incoming[clean_target].append(item)

pair_connections = {}
for link in internal_links:
    s = link["source_url"]
    t = link["target_url"]
    if (s, t) not in pair_connections:
        pair_connections[(s, t)] = []
    pair_connections[(s, t)].append(link["anchor_text"])

bidirectional_pairs = []
for (s, t), s_anchors in pair_connections.items():
    if (t, s) in pair_connections and s < t:
        t_anchors = pair_connections[(t, s)]
        s_name = page_html_map.get(s, {}).get("name", s)
        t_name = page_html_map.get(t, {}).get("name", t)
        bidirectional_pairs.append({
            "node_a": s,
            "node_a_name": s_name,
            "node_b": t,
            "node_b_name": t_name,
            "a_to_b_anchors": s_anchors,
            "b_to_a_anchors": t_anchors
        })

KEYWORDS_TARGET = ["中高齡營養師", "肌少症飲食", "企業健康講座"]
keyword_coverage = {kw: [] for kw in KEYWORDS_TARGET}

for url, info in page_html_map.items():
    soup = BeautifulSoup(info["html"], "html.parser")
    plain_text = soup.get_text(separator=" ", strip=True)
    title_text = ""
    if info["type"] == "Core/Tool":
        title_tag = soup.find("title")
        if title_tag:
            title_text = title_tag.get_text(strip=True)
    else:
        title_text = info["raw_post"].get("title", "")
    headings = [h.get_text(strip=True) for h in soup.find_all(["h1", "h2", "h3"])]
    for kw in KEYWORDS_TARGET:
        kw_in_title = kw in title_text
        kw_in_headings = any(kw in h for h in headings)
        count_in_body = plain_text.count(kw)
        sub_terms = []
        if kw == "中高齡營養師":
            sub_terms = ["中高齡", "長照", "高齡營養", "長輩"]
        elif kw == "肌少症飲食":
            sub_terms = ["肌少症", "蛋白質", "阻力運動", "肌少"]
        elif kw == "企業健康講座":
            sub_terms = ["企業講座", "健康講座", "員工健康", "EAP"]
        sub_counts = {st: plain_text.count(st) for st in sub_terms if plain_text.count(st) > 0}
        if kw_in_title or kw_in_headings or count_in_body > 0 or sub_counts:
            keyword_coverage[kw].append({
                "page_name": info["name"],
                "url": url,
                "in_title": kw_in_title,
                "in_headings": kw_in_headings,
                "exact_count": count_in_body,
                "related_terms": sub_counts
            })

output_data = {
    "total_nodes": len(page_html_map),
    "total_internal_links": len(internal_links),
    "bidirectional_pairs_count": len(bidirectional_pairs),
    "bidirectional_pairs": bidirectional_pairs,
    "keyword_coverage": keyword_coverage,
    "node_stats": [
        {
            "name": info["name"],
            "url": url,
            "type": info["type"],
            "outgoing_count": len(node_outgoing[url]),
            "incoming_count": len(node_incoming[url]),
            "outgoing_samples": [l["anchor_text"] for l in node_outgoing[url][:5]],
            "incoming_samples": [l["anchor_text"] for l in node_incoming[url][:5]],
        }
        for url, info in page_html_map.items()
    ]
}

OUTPUT_FILE = ROOT_DIR / "work" / "2026-09-04-milestone-4-internal-links-ranking-audit" / "output" / "internal_links_and_keywords_data.json"
OUTPUT_FILE.write_text(json.dumps(output_data, ensure_ascii=False, indent=2), encoding="utf-8")
print(f"[✓] 數據萃取完成，已寫入 {OUTPUT_FILE}")
print(f"[*] 總內部連結數：{len(internal_links)}，雙向互連組數：{len(bidirectional_pairs)}")
