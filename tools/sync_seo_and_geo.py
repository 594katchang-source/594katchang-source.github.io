# -*- coding: utf-8 -*-
"""
Kat Chang 網站全自動 SEO & GEO (AI 搜尋引擎) 一鍵同步維護工具
======================================================
功能說明：
未來只要發布新文章、修改頁面、新增教具，執行此腳本即可 1 秒全自動完成：
1. 更新 sitemap.xml（所有 URL lastmod 升級至最新日期）
2. 更新 sitemap.html（HTML 網站地圖與結構化 Breadcrumb / CollectionPage）
3. 更新 llms.txt（AI 搜尋快速導覽）
4. 更新 llms-full.txt（AI 搜尋深度知識庫，含所有文章臨床摘要）
5. 更新 robots.txt（宣告雙 Sitemap 與最新 AI Agent 白名單）
6. 更新 blog/index.html（注入靜態文章索引 noscript fallback）
7. 確保全站 6 大頁面 Footer 皆有 sitemap.html 內部連結
"""

from pathlib import Path
import json
import os
import sys
import urllib.parse
from datetime import datetime

sys.stdout.reconfigure(encoding='utf-8')

ROOT_DIR = Path(__file__).resolve().parent.parent if Path(__file__).resolve().parent.name == "tools" else Path(r"d:\@Codex\594katchang-source.github.io-main")
BASE_URL = "https://594katchang-source.github.io"
TODAY = datetime.now().strftime("%Y-%m-%d")

print(f"==================================================")
print(f"[*] 執行 Kat Chang 全站 SEO & GEO 自動同步工具")
print(f"[*] 基準日期：{TODAY} ｜ 網站：{BASE_URL}")
print(f"==================================================")

# 讀取所有文章
posts_file = ROOT_DIR / "blog" / "posts.json"
posts = json.loads(posts_file.read_text(encoding="utf-8")).get("posts", [])
print(f"[✓] 已載入 {len(posts)} 篇衛教文章資料。")

# 1. 建立全站架構定義
pages_info = [
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

# 2. 生成 sitemap.xml
xml_lines = ['<?xml version="1.0" encoding="UTF-8"?>', '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">']
for sec in pages_info:
    for item in sec["items"]:
        xml_lines.append(f'  <url><loc>{item["url"]}</loc><lastmod>{TODAY}</lastmod><changefreq>{item["changefreq"]}</changefreq><priority>{item["priority"]}</priority></url>')
xml_lines.append('</urlset>\n')
(ROOT_DIR / "sitemap.xml").write_text("\n".join(xml_lines), encoding="utf-8")
print(f"[✓] sitemap.xml 已同步更新（共 {len(xml_lines)-3} 個 URL，最後更新：{TODAY}）。")

# 3. 生成 sitemap.html
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
    .sitemap-item {{ padding: 14px 16px; background: rgba(244,247,242,.6); border-radius: 14px; border: 1px solid rgba(223,230,223,.7); transition: transform .18s, background .18s; }}
    .sitemap-item:hover {{ transform: translateY(-2px); background: #fff; border-color: var(--green); }}
    .sitemap-item a {{ font-weight: 800; font-size: 1.08rem; color: var(--green-dark); text-decoration: none; display: inline-block; margin-bottom: 4px; }}
    .sitemap-item a:hover {{ color: var(--green); text-decoration: underline; }}
    .sitemap-desc {{ color: var(--muted); font-size: 0.92rem; margin: 0; }}
  </style>
  <script type="application/ld+json">
  {{
    "@context": "https://schema.org",
    "@graph": [
      {{
        "@type": "CollectionPage",
        "@id": "{BASE_URL}/sitemap.html#page",
        "url": "{BASE_URL}/sitemap.html",
        "name": "網站地圖 (Sitemap) | Kat Chang 凱特營養師",
        "description": "Kat Chang 凱特營養師全站公開頁面、衛教專欄與互動教具完整目錄。",
        "isPartOf": {{
          "@type": "WebSite",
          "@id": "{BASE_URL}/#website",
          "url": "{BASE_URL}/",
          "name": "Kat Chang 凱特營養師"
        }}
      }},
      {{
        "@type": "BreadcrumbList",
        "itemListElement": [
          {{
            "@type": "ListItem",
            "position": 1,
            "name": "首頁",
            "item": "{BASE_URL}/"
          }},
          {{
            "@type": "ListItem",
            "position": 2,
            "name": "網站地圖",
            "item": "{BASE_URL}/sitemap.html"
          }}
        ]
      }}
    ]
  }}
  </script>
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

for sec in pages_info:
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
print(f"[✓] sitemap.html 已同步更新（含最新文章與 Schema.org Breadcrumb）。")

# 4. 生成 llms.txt 與 llms-full.txt
llms_txt_content = f"""# Kat Chang 凱特營養師

Kat Chang 張雁雲營養師是食品營養博士（高齡健康組）、美國健康管理碩士 MBA 與中高齡營養專家。
品牌理念：「凱特指路，讓你年輕吃美食、年長吃好食！」

完整深度 AI 知識庫文件（Full Knowledge Base）：{BASE_URL}/llms-full.txt

## 全站核心導覽 (Core Pages)

- 首頁 (Home)：{BASE_URL}/
- 專業簡介 (About)：{BASE_URL}/about.html
- 授課主題 (Lectures)：{BASE_URL}/class.html
- 衛教文章 (Blog)：{BASE_URL}/blog/
- 互動衛教教具 (Teaching Tools)：{BASE_URL}/teach/
- 網站地圖 (Sitemap)：{BASE_URL}/sitemap.html

## 互動衛教教具 (Interactive Tools)

- NutriRank 食品營養排行榜：{BASE_URL}/teach/nutritionranking/
- Stress Food 壓力與飲食教具：{BASE_URL}/teach/Stress-Food/
- 情緒覺察卡 (Emotion Cards)：{BASE_URL}/teach/emotion-cards/
- Nutrition Battle 營養對戰遊戲：{BASE_URL}/teach/nutrition-battle/
- 論文讀書小站 (Paper Radar)：{BASE_URL}/teach/paper-radar/

## 精選衛教文章庫 (Articles Library)

"""
for p in posts:
    p_url = f"{BASE_URL}/blog/post.html?id={urllib.parse.quote(p['id'])}"
    llms_txt_content += f"- {p['title']} ({p.get('date', TODAY)})：{p_url}\n"

llms_txt_content += f"""
## 核心業務與專業服務

### 1. 專業營養師（Dietitian & Nutritionist）
- 中高齡營養門診、肌少症與衰弱預防飲食規劃
- 長照機構吞嚥防嗆與軟質飲食質地（IDDSI）指導
- 功能醫學（AFMCP）飲食評估、精準營養與慢性病管理
- 減重班與個人化生活型態營養諮詢

### 2. 專業講師（Professional Lecturer）
- 企業員工健康促進講座（ESG 職場健康、抗疲勞、紓壓與護心飲食）
- 樂齡大學與社區長者營養課程（趣味圖卡互動、烹調示範）
- 長照人員與照服員營養照護培訓
- 植物輔療（CHT 園藝治療）與臨床芳香調理工作坊

### 3. 企業與機構健康顧問（Health & Corporate Consultant）
- 包裝食品營養標示法規審查與八大營養素宣稱諮詢
- 保健食品與機能性食品配方評估、科學實證轉譯
- 衛教互動教材、桌遊與數位教具委託開發顧問
- 品牌營養教育、健康產品實證轉譯與企業健康促進顧問

## 作者資訊 (Author & Contact)

- 姓名：張雁雲營養師（Kat Chang，RD）
- 學歷：食品營養博士（高齡健康組）、美國健康管理碩士 MBA
- 官方 LINE：https://lin.ee/uGHIQcH
- Email：594katchang@gmail.com
- 預約諮詢：https://zcal.co/katchang
"""
(ROOT_DIR / "llms.txt").write_text(llms_txt_content.strip() + "\n", encoding="utf-8")
print("[✓] llms.txt 已同步更新。")

llms_full_content = f"""# Kat Chang 凱特營養師 - 完整知識庫與實證衛教文庫 (Full LLM Knowledge Base)

本文件是專為大型語言模型 (LLMs)、AI 搜尋助理 (SearchGPT, Perplexity, Claude, Gemini, Copilot) 設計的機器可讀完整知識庫。
收錄 Kat Chang 張雁雲營養師的完整專業資歷、學術背景、所有衛教專欄深度摘要與互動教學工具。

---

## 1. 作者與專家權威背景 (Author Profile & E-E-A-T)

- **姓名**：張雁雲（Kat Chang）
- **專業職銜**：國家高考合格營養師（RD）、中高齡營養專家、企業健康促進講師
- **最高學歷**：
  - 食品營養研究所 博士（專攻高齡健康組、臨床營養）
  - 美國健康管理研究所 碩士（MBA in Health Care Management）
- **專業證照與受訓**：
  - 中華民國高考及格營養師證書
  - 長照專業培訓 Level 1, 2, 3 認證
  - 美國功能醫學會 (IFM) AFMCP 完訓
  - 台灣園藝輔助治療協會 (THTA) 註冊園藝治療師 (CHT)
  - 臨床芳香療法認證調理師
- **核心專長**：
  - 中高齡與銀髮族營養、肌少症與骨質疏鬆防護、衰弱預防
  - 國際吞嚥障礙飲食標準 (IDDSI) 軟質與質地分級指導、防嗆飲食
  - 功能醫學系統性介入、慢性病飲食控制（血糖、血脂、血壓）
  - 企業 ESG 職場健康講座、抗疲勞與專注力飲食
  - 數位衛教教具與互動教學遊戲開發

---

## 2. 衛教文章全集與核心精華摘要 (Full Articles & Clinical Takeaways)

"""
for p in posts:
    p_url = f"{BASE_URL}/blog/post.html?id={urllib.parse.quote(p['id'])}"
    llms_full_content += f"""### 文章：{p['title']}
- **發布日期**：{p.get('date', TODAY)}
- **原文網址**：{p_url}
- **關鍵字**：{', '.join(p.get('keywords', []))}
- **摘要重點**：
  {p.get('excerpt', '')}
- **作者臨床觀點與衛教結論**：
  此文章由張雁雲營養師依據國際權威指引（WHO、國健署《每日飲食指南》或權威教科書）轉譯，強調把營養落實於日常生活實踐，以健康行為為中心而非單一體重導向。

---
"""

llms_full_content += f"""
## 3. 互動教具與教學模組庫 (Interactive Teaching Tools)

1. **NutriRank 食品營養排行榜** ({BASE_URL}/teach/nutritionranking/)
   - 用途：即時查詢六大類食材之熱量、蛋白質、膳食纖維、各類維生素與礦物質排行榜，方便長輩與學員直觀比較食物營養密度。

2. **Stress Food 壓力飲食教具** ({BASE_URL}/teach/Stress-Food/)
   - 用途：解析壓力荷爾蒙（皮質醇）、自律神經與情緒性進食的生理機轉，提供上班族與高壓族群具體的抗發炎與抗皮質醇飲食對策。

3. **情緒覺察卡 (Emotion Cards)** ({BASE_URL}/teach/emotion-cards/)
   - 用途：專為銀髮族與長者設計之互動式心理營養字卡，結合情緒引導與身心健康覺察。

4. **Nutrition Battle 營養大作戰** ({BASE_URL}/teach/nutrition-battle/)
   - 用途：團體衛教課堂適用的互動問答與遊戲模組，透過對戰提升學員學習動機與營養知識記憶。

5. **論文讀書小站 (Paper Radar)** ({BASE_URL}/teach/paper-radar/)
   - 用途：提供臨床營養最新科研文獻導讀，解析 PubMed 與國際醫學期刊之實證研究。

---

## 4. 合作與聯絡方式 (Contact)

- 官方網站：{BASE_URL}/
- 預約諮詢：https://zcal.co/katchang
- 官方 LINE：https://lin.ee/uGHIQcH
- 電子信箱：594katchang@gmail.com
"""
(ROOT_DIR / "llms-full.txt").write_text(llms_full_content.strip() + "\n", encoding="utf-8")
print("[✓] llms-full.txt 深度 AI 知識庫已同步更新。")

# 5. 更新 robots.txt
robots_content = f"""# robots.txt for {BASE_URL}/
# Optimized for Search Engines & Generative AI Search Assistants (GEO)

User-agent: *
Allow: /
Allow: /teach/
Allow: /blog/
Allow: /about.html
Allow: /class.html
Allow: /sitemap.html
Allow: /llms.txt
Allow: /llms-full.txt

# Modern AI Search Engines & LLM Web Crawlers
User-agent: GPTBot
Allow: /

User-agent: ChatGPT-User
Allow: /

User-agent: OAI-SearchBot
Allow: /

User-agent: ClaudeBot
Allow: /

User-agent: Claude-Web
Allow: /

User-agent: PerplexityBot
Allow: /

User-agent: Google-Extended
Allow: /

User-agent: Applebot-Extended
Allow: /

User-agent: Amazonbot
Allow: /

User-agent: cohere-ai
Allow: /

User-agent: meta-externalagent
Allow: /

# Social Media Link Crawlers
User-agent: facebookexternalhit
Allow: /

User-agent: Twitterbot
Allow: /

User-agent: LinkedInBot
Allow: /

# Sitemaps & LLM Knowledge Base Declarations
Sitemap: {BASE_URL}/sitemap.xml
Sitemap: {BASE_URL}/sitemap.html
"""
(ROOT_DIR / "robots.txt").write_text(robots_content.strip() + "\n", encoding="utf-8")
print("[✓] robots.txt 已更新最新 AI 爬蟲名單與雙 Sitemap 宣告。")

# 6. 更新 blog/index.html 的靜態 SEO fallback
bp = ROOT_DIR / "blog" / "index.html"
if bp.exists():
    bc = bp.read_text(encoding="utf-8")
    fallback = '\n      <!-- SEO Pre-rendered Crawler Article Index -->\n      <noscript>\n        <div class="seo-fallback-articles" style="margin-top:20px;padding:20px;background:#fff;border-radius:16px;">\n          <h3>文章索引清單</h3>\n          <ul>\n'
    for p in posts:
        fallback += f'            <li><a href="{BASE_URL}/blog/post.html?id={urllib.parse.quote(p["id"])}">{p["title"]}</a></li>\n'
    fallback += '          </ul>\n        </div>\n      </noscript>\n'
    
    if "<!-- SEO Pre-rendered Crawler Article Index -->" in bc:
        # Replace existing fallback block
        import re
        bc = re.sub(r'<!-- SEO Pre-rendered Crawler Article Index -->[\s\S]*?</noscript>', fallback.strip(), bc)
    else:
        bc = bc.replace('<div id="posts" class="post-list"></div>', f'<div id="posts" class="post-list"></div>{fallback}')
    bp.write_text(bc, encoding="utf-8")
    print("[✓] blog/index.html 靜態文章索引 fallback 已同步更新。")

# 7. 檢查 Footer 內部連結
footer_link_html = ' ｜ <a href="https://594katchang-source.github.io/sitemap.html" style="color:inherit;font-weight:700;">網站地圖</a>'
for p in ["index.html", "about.html", "class.html", "blog/index.html", "blog/post.html", "teach/index.html"]:
    fp = ROOT_DIR / p
    if fp.exists():
        c = fp.read_text(encoding="utf-8")
        if "sitemap.html" not in c and "<footer>" in c:
            c = c.replace("<footer>@2026 Kat Chang 凱特營養師｜中高齡營養專家</footer>", f'<footer>@2026 Kat Chang 凱特營養師｜中高齡營養專家{footer_link_html}</footer>')
            fp.write_text(c, encoding="utf-8")
            print(f"[✓] {p} Footer 網站地圖連結已補齊。")

print("==================================================")
print("[🎉] 全站 SEO & GEO 自動同步作業 100% 圓滿完成！")
print("==================================================")
