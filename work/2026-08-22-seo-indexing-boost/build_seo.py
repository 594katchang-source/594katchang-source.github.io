# -*- coding: utf-8 -*-
from pathlib import Path
import json
import os
import sys
import urllib.parse

sys.stdout.reconfigure(encoding='utf-8')

ROOT_DIR = Path(r"d:\@Codex\594katchang-source.github.io-main")
OUTPUT_DIR = ROOT_DIR / "work" / "2026-08-22-seo-indexing-boost" / "output"
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
BASE_URL = "https://594katchang-source.github.io"
TODAY = "2026-08-22"

print(f"[*] Boosting SEO & Indexing for {BASE_URL}...")

posts_file = ROOT_DIR / "blog" / "posts.json"
posts = json.loads(posts_file.read_text(encoding="utf-8")).get("posts", [])
print(f"[*] Found {len(posts)} articles in posts.json")

sections = [
    {
        "category": "核心主要頁面 (Core Pages)",
        "items": [
            {"title": "首頁 ｜ Kat Chang 凱特營養師", "url": f"{BASE_URL}/", "desc": "中高齡營養專家、課程講座、衛教教具與健康管理服務。", "priority": "1.0", "changefreq": "weekly"},
            {"title": "簡介 ｜ 專業資歷與服務理念", "url": f"{BASE_URL}/about.html", "desc": "國家高考合格營養師、長照與功能醫學專長、產官學合作經驗。", "priority": "0.9", "changefreq": "monthly"},
            {"title": "授課 ｜ 課程講座與工作坊", "url": f"{BASE_URL}/class.html", "desc": "銀髮共餐營養、肌少症預防、慢性病飲食、實務培訓與衛教演講。", "priority": "0.9", "changefreq": "monthly"},
            {"title": "文章 ｜ 衛教專欄與書籍導讀", "url": f"{BASE_URL}/blog/", "desc": "精選營養學概念、食物選擇、疾病飲食與實證衛教知識庫。", "priority": "0.9", "changefreq": "weekly"},
            {"title": "教具 ｜ 衛教工具與教學遊戲", "url": f"{BASE_URL}/teach/", "desc": "專為樂齡與衛教教學設計的互動式數位教具與字卡工具。", "priority": "0.8", "changefreq": "monthly"},
        ]
    },
    {
        "category": "互動教具與模組 (Interactive Teaching Tools)",
        "items": [
            {"title": "教具：營養排行榜 (Nutrition Ranking)", "url": f"{BASE_URL}/teach/nutritionranking/", "desc": "六大類食材營養密度與微量元素即時排序與比較工具。", "priority": "0.8", "changefreq": "weekly"},
            {"title": "教具：論文讀書小站 (Paper Radar)", "url": f"{BASE_URL}/teach/paper-radar/", "desc": "國際權威醫學期刊與營養實證研究導讀雷達站。", "priority": "0.8", "changefreq": "weekly"},
            {"title": "教具：壓力與食物關係 (Stress Food)", "url": f"{BASE_URL}/teach/Stress-Food/", "desc": "壓力荷爾蒙、皮質醇與情緒性進食的生理機轉與飲食對策。", "priority": "0.7", "changefreq": "monthly"},
            {"title": "教具：情緒營養字卡 (Emotion Cards)", "url": f"{BASE_URL}/teach/emotion-cards/", "desc": "高齡長輩情緒引導與身心健康互動式翻牌教具。", "priority": "0.7", "changefreq": "monthly"},
            {"title": "教具：營養大作戰 (Nutrition Battle)", "url": f"{BASE_URL}/teach/nutrition-battle/", "desc": "樂齡課堂實體與線上互動營養問答對戰遊戲。", "priority": "0.7", "changefreq": "monthly"},
        ]
    },
    {
        "category": "衛教專欄與書籍導讀文章 (Articles & Guides)",
        "items": [
            {
                "title": f"衛教：{p['title']}",
                "url": f"{BASE_URL}/blog/post.html?id={urllib.parse.quote(p['id'])}",
                "desc": f"【{p.get('date', TODAY)}】{p.get('excerpt', '')[:85]}...",
                "priority": "0.8",
                "changefreq": "monthly"
            }
            for p in posts
        ]
    }
]

# 1. Update sitemap.xml
xml_lines = ['<?xml version="1.0" encoding="UTF-8"?>', '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">']
for sec in sections:
    for item in sec["items"]:
        xml_lines.append(f'  <url><loc>{item["url"]}</loc><lastmod>{TODAY}</lastmod><changefreq>{item["changefreq"]}</changefreq><priority>{item["priority"]}</priority></url>')
xml_lines.append('</urlset>\n')
xml_content = "\n".join(xml_lines)

(ROOT_DIR / "sitemap.xml").write_text(xml_content, encoding="utf-8")
(OUTPUT_DIR / "sitemap.xml").write_text(xml_content, encoding="utf-8")
print(f"[✓] Generated sitemap.xml with {len(xml_lines)-3} URLs.")

# 2. Generate sitemap.html
html_content = f"""<!doctype html>
<html lang="zh-Hant">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>網站地圖 (Sitemap) | Kat Chang 凱特營養師</title>
  <meta name="description" content="Kat Chang 凱特營養師全站地圖，收錄所有核心頁面、衛教文章、互動教具與課程講座快速導覽。">
  <meta name="robots" content="index, follow, max-image-preview:large, max-snippet:-1">
  <link rel="canonical" href="{BASE_URL}/sitemap.html">
  <link rel="stylesheet" href="styles.css?v={TODAY}">
  <style>
    .sitemap-container {{ max-width: 920px; margin: 40px auto 80px; padding: 0 20px; }}
    .sitemap-section {{ margin-bottom: 36px; background: var(--surface); border: 1px solid var(--line); border-radius: 24px; padding: 28px; box-shadow: 0 10px 30px rgba(24,33,43,.05); }}
    .sitemap-section h2 {{ font-size: 1.4rem; color: var(--green-dark); margin-bottom: 18px; border-bottom: 2px solid var(--sage); padding-bottom: 10px; }}
    .sitemap-list {{ list-style: none; padding: 0; margin: 0; display: grid; gap: 14px; }}
    .sitemap-item {{ padding: 14px 16px; background: rgba(244,247,242,.6); border-radius: 14px; border: 1px solid rgba(223,230,223,.7); }}
    .sitemap-item a {{ font-weight: 800; font-size: 1.08rem; color: var(--green-dark); text-decoration: none; display: inline-block; margin-bottom: 4px; }}
    .sitemap-item a:hover {{ color: var(--green); text-decoration: underline; }}
    .sitemap-desc {{ color: var(--muted); font-size: 0.92rem; margin: 0; }}
  </style>
</head>
<body class="sitemap-page">
  <header class="site-header">
    <a class="brand" href="./"><img src="assets/profile/kat-avatar.jpg" alt="Kat Chang 凱特營養師"><span>Kat Chang</span></a>
    <nav>
      <a href="index.html">首頁</a>
      <a href="about.html">簡介</a>
      <a href="class.html">授課</a>
      <a href="index.html#services">服務</a>
      <a href="teach/">教具</a>
      <a href="blog/">文章</a>
      <a href="https://zcal.co/katchang" target="_blank" rel="noopener">聯絡</a>
    </nav>
  </header>
  <main class="sitemap-container">
    <div class="section-title">
      <p class="eyebrow">Sitemap</p>
      <h1>網站地圖與文章導覽</h1>
      <p class="lead">收錄 Kat Chang 凱特營養師全站公開頁面、衛教專欄與互動教具，提供訪客與搜尋引擎最佳檢索結構。</p>
    </div>
"""

for sec in sections:
    html_content += f"""    <section class="sitemap-section">
      <h2>{sec["category"]}</h2>
      <ul class="sitemap-list">
"""
    for it in sec["items"]:
        html_content += f"""        <li class="sitemap-item"><a href="{it["url"]}">{it["title"]}</a><p class="sitemap-desc">{it["desc"]}</p></li>\n"""
    html_content += """      </ul>
    </section>
"""

html_content += f"""  </main>
  <footer>
    <p>@2026 Kat Chang 凱特營養師｜中高齡營養專家 ｜ <a href="sitemap.html" style="color:inherit;font-weight:bold;">網站地圖 (Sitemap)</a> ｜ <a href="sitemap.xml" target="_blank" style="color:inherit;">XML Sitemap</a></p>
  </footer>
</body>
</html>
"""

(ROOT_DIR / "sitemap.html").write_text(html_content, encoding="utf-8")
(OUTPUT_DIR / "sitemap.html").write_text(html_content, encoding="utf-8")
print("[✓] Generated sitemap.html successfully.")

# 3. Update robots.txt
r_file = ROOT_DIR / "robots.txt"
r_txt = r_file.read_text(encoding="utf-8")
if "sitemap.html" not in r_txt:
    r_txt = r_txt.replace("Sitemap: https://594katchang-source.github.io/sitemap.xml", "Sitemap: https://594katchang-source.github.io/sitemap.xml\nSitemap: https://594katchang-source.github.io/sitemap.html")
    r_file.write_text(r_txt, encoding="utf-8")
    print("[✓] Updated robots.txt with sitemap.html")

# 4. Footer link across pages
for p in ["index.html", "about.html", "class.html", "blog/index.html", "blog/post.html", "teach/index.html"]:
    fp = ROOT_DIR / p
    if fp.exists():
        c = fp.read_text(encoding="utf-8")
        if "sitemap.html" not in c and "<footer>" in c:
            c = c.replace("<footer>@2026 Kat Chang 凱特營養師｜中高齡營養專家</footer>", '<footer>@2026 Kat Chang 凱特營養師｜中高齡營養專家 ｜ <a href="https://594katchang-source.github.io/sitemap.html" style="color:inherit;font-weight:700;">網站地圖</a></footer>')
            fp.write_text(c, encoding="utf-8")
            print(f"[✓] Footer link injected into {p}")

# 5. Static articles fallback in blog/index.html
bp = ROOT_DIR / "blog" / "index.html"
bc = bp.read_text(encoding="utf-8")
if "seo-fallback-articles" not in bc:
    fallback = '\n      <!-- SEO Pre-rendered Crawler Article Index -->\n      <noscript>\n        <div class="seo-fallback-articles" style="margin-top:20px;padding:20px;background:#fff;border-radius:16px;">\n          <h3>文章索引清單</h3>\n          <ul>\n'
    for p in posts:
        fallback += f'            <li><a href="{BASE_URL}/blog/post.html?id={urllib.parse.quote(p["id"])}">{p["title"]}</a></li>\n'
    fallback += '          </ul>\n        </div>\n      </noscript>\n'
    bc = bc.replace('<div id="posts" class="post-list"></div>', f'<div id="posts" class="post-list"></div>{fallback}')
    bp.write_text(bc, encoding="utf-8")
    print("[✓] Static SEO fallback links injected into blog/index.html")

print("\n[🎉] ALL SEO BOOST TASKS COMPLETED!")
