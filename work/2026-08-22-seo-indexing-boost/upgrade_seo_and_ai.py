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

print(f"[*] Starting Comprehensive SEO & AI Optimization for {BASE_URL}...")

posts_file = ROOT_DIR / "blog" / "posts.json"
posts = json.loads(posts_file.read_text(encoding="utf-8")).get("posts", [])
print(f"[*] Found {len(posts)} articles in posts.json")

# ==========================================
# 1. Generate Comprehensive llms-full.txt & Update llms.txt
# ==========================================
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
(OUTPUT_DIR / "llms.txt").write_text(llms_txt_content.strip() + "\n", encoding="utf-8")
print("[✓] llms.txt updated.")

# Generate llms-full.txt with in-depth summaries for AI Search Engines
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
(OUTPUT_DIR / "llms-full.txt").write_text(llms_full_content.strip() + "\n", encoding="utf-8")
print("[✓] llms-full.txt created successfully.")

# ==========================================
# 2. Upgrade robots.txt for all modern AI & Search Crawlers
# ==========================================
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
(OUTPUT_DIR / "robots.txt").write_text(robots_content.strip() + "\n", encoding="utf-8")
print("[✓] robots.txt upgraded with comprehensive AI & Search agents.")

# ==========================================
# 3. Enhance blog.js with Related Articles & Cross-Links
# ==========================================
blog_js_path = ROOT_DIR / "blog" / "blog.js"
blog_js = blog_js_path.read_text(encoding="utf-8")

# Let's add related posts generator logic into blog.js
related_posts_script = """
function renderRelatedPosts(currentPost, allPosts) {
  const otherPosts = allPosts.filter(p => p.id !== currentPost.id);
  if (!otherPosts.length) return '';
  const matched = otherPosts.filter(p => p.category === currentPost.category);
  const candidates = (matched.length >= 2 ? matched : otherPosts).slice(0, 3);
  return `
    <section class="related-posts-section" style="margin-top:48px;padding-top:32px;border-top:1px solid var(--line);">
      <h2 style="font-size:1.4rem;color:var(--green-dark);margin-bottom:20px;">💡 延伸閱讀・精選衛教文章</h2>
      <div style="display:grid;grid-template-columns:repeat(auto-fit,minmax(260px,1fr));gap:16px;">
        ${candidates.map(p => `
          <a class="service-card" href="post.html?id=${encodeURIComponent(p.id)}" style="display:block;text-decoration:none;padding:18px;border-radius:18px;">
            <div style="font-size:0.85rem;color:var(--muted);margin-bottom:6px;">${escapeHtml(p.date || '')}</div>
            <h3 style="font-size:1.05rem;line-height:1.4;margin-bottom:8px;color:var(--ink);">${escapeHtml(p.title || '')}</h3>
            <p style="font-size:0.9rem;color:var(--muted);margin:0;">${escapeHtml(summary(p))}</p>
          </a>
        `).join('')}
      </div>
    </section>
  `;
}
"""

if "renderRelatedPosts" not in blog_js:
    # Insert renderRelatedPosts before main()
    blog_js = blog_js.replace(
        "async function main(){",
        related_posts_script + "\nasync function main(){"
    )
    # Append related posts HTML to article
    blog_js = blog_js.replace(
        '<div class="article-body">${sanitizeHtml(post.body||\'\')}</div>`',
        '<div class="article-body">${sanitizeHtml(post.body||\'\')}</div>${renderRelatedPosts(post, posts)}`'
    )
    blog_js_path.write_text(blog_js, encoding="utf-8")
    print("[✓] blog.js upgraded with Related Articles cross-linking!")

# ==========================================
# 4. Enhance sitemap.html with Schema.org Breadcrumb & CollectionPage
# ==========================================
sitemap_html_path = ROOT_DIR / "sitemap.html"
sitemap_html = sitemap_html_path.read_text(encoding="utf-8")
schema_json = f"""
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
"""

if "application/ld+json" not in sitemap_html:
    sitemap_html = sitemap_html.replace("</head>", f"{schema_json}\n</head>")
    sitemap_html_path.write_text(sitemap_html, encoding="utf-8")
    (OUTPUT_DIR / "sitemap.html").write_text(sitemap_html, encoding="utf-8")
    print("[✓] Added Schema.org Breadcrumb & CollectionPage to sitemap.html")

# ==========================================
# 5. Enhance teach/index.html with cross-links to Blog Articles
# ==========================================
teach_index_path = ROOT_DIR / "teach" / "index.html"
if teach_index_path.exists():
    teach_html = teach_index_path.read_text(encoding="utf-8")
    teach_crosslink = f"""
    <section class="section" style="padding-top:20px;border-top:1px solid var(--line);margin-top:40px;">
      <div class="section-title split">
        <div>
          <p class="eyebrow">Related Knowledge</p>
          <h2>搭配衛教專欄文章</h2>
          <p class="lead">運用數位教具互動之餘，歡迎搭配營養師專欄文章進行深度實證研讀。</p>
        </div>
        <a class="btn" href="../blog/">瀏覽全部文章</a>
      </div>
      <div class="card-grid" style="grid-template-columns:repeat(auto-fit,minmax(280px,1fr));gap:16px;">
        <a class="service-card" href="../blog/post.html?id=2026-08-15-nutrition-tools-standards-guidelines">
          <h3>DRI 與營養標示怎麼看？</h3>
          <p>用六大類食物讀懂營養數字、每日參考值與超級食物迷思。</p>
        </a>
        <a class="service-card" href="../blog/post.html?id=2026-08-14-food-choices-human-health-guide">
          <h3>食物選擇怎麼影響健康？</h3>
          <p>適足、均衡、適量、多樣四大原則，輕鬆落實日常餐盤搭配。</p>
        </a>
        <a class="service-card" href="../blog/post.html?id=2026-08-16-remarkable-body-nutrition-guide">
          <h3>人體消化與吸收機轉</h3>
          <p>從消化道生理、酵素作用到營養訊號傳遞，讀懂身體代謝運作。</p>
        </a>
      </div>
    </section>
    """
    if "搭配衛教專欄文章" not in teach_html:
        teach_html = teach_html.replace(
            '<section class="contact-band directory-contact">',
            f"{teach_crosslink}\n    <section class=\"contact-band directory-contact\">"
        )
        teach_index_path.write_text(teach_html, encoding="utf-8")
        print("[✓] Added cross-links to blog articles in teach/index.html")

print("\n[🎉] ALL SEO & AI UPGRADES COMPLETED!")
