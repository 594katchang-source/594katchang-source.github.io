# -*- coding: utf-8 -*-
"""
專文靜態化 (SSG) 自動化生成腳本
==================================
為 blog/posts.json 中所有 12 篇衛教專文生成 100% 獨立實體靜態 HTML 檔案，
徹底解決 SPA 帶參數網址 (?id=...) 導致 Google 爬蟲僅收錄 1 次曝光、無法索引長尾內容的致命弱點。
每個靜態 HTML 檔案內建：
1. 專屬 Title, Description, Keywords, Canonical URL
2. 專屬 Open Graph / Twitter Card 與封面圖
3. 專屬 Schema.org BlogPosting 與 BreadcrumbList JSON-LD
4. 預渲染全文 HTML 與「🎤 企業健康講座與授課邀約」高對比導流卡
5. 延伸閱讀 3 篇相關文章靜態鏈結
"""

import os
import sys
import json
import re
import html
import urllib.parse
from pathlib import Path

sys.stdout.reconfigure(encoding='utf-8')

ROOT_DIR = Path(r"d:\@Codex\594katchang-source.github.io-main")
BLOG_DIR = ROOT_DIR / "blog"
POSTS_FILE = BLOG_DIR / "posts.json"
BASE_URL = "https://594katchang-source.github.io"

def escape(s):
    return html.escape(str(s or ''))

def clean_summary(post, max_len=150):
    text = post.get('excerpt', '')
    if not text:
        body = post.get('body', '')
        text = re.sub(r'<[^>]+>', ' ', body)
    text = re.sub(r'\s+', ' ', text).strip()
    if len(text) > max_len:
        return text[:max_len-1] + "…"
    return text

def get_image_url(post):
    raw = str(post.get('image', '')).strip()
    if not raw:
        return f"{BASE_URL}/assets/og/og-blog.png"
    if raw.startswith("http://") or raw.startswith("https://"):
        return raw
    if raw.startswith("blog/images/"):
        return f"{BASE_URL}/{raw}"
    if raw.startswith("images/"):
        return f"{BASE_URL}/blog/{raw}"
    return f"{BASE_URL}/blog/images/{raw}"

def get_image_rel(post):
    raw = str(post.get('image', '')).strip()
    if not raw:
        return "../assets/og/og-blog.png"
    if raw.startswith("http://") or raw.startswith("https://"):
        return raw
    if raw.startswith("blog/images/"):
        return raw.replace("blog/", "")
    if raw.startswith("images/"):
        return raw
    return f"images/{raw}"

def build_related_posts_html(current_post, all_posts):
    other_posts = [p for p in all_posts if p.get('id') != current_post.get('id')]
    matched = [p for p in other_posts if p.get('category') == current_post.get('category')]
    candidates = (matched if len(matched) >= 2 else other_posts)[:3]
    
    cards_html = []
    for p in candidates:
        pid = p.get('id', '')
        title = escape(p.get('title', ''))
        date_str = escape(p.get('date', ''))
        desc = escape(clean_summary(p, 90))
        target_url = f"{pid}.html"
        cards_html.append(f"""
          <a class="service-card" href="{target_url}" style="display:block;text-decoration:none;padding:18px;border-radius:18px;background:#fff;border:1px solid var(--line);box-shadow:0 6px 18px rgba(0,0,0,0.04);">
            <div style="font-size:0.92rem;color:var(--muted);margin-bottom:6px;">{date_str}</div>
            <h3 style="font-size:1.15rem;line-height:1.4;margin-bottom:8px;color:var(--ink);font-weight:800;">{title}</h3>
            <p style="font-size:0.95rem;color:var(--muted);margin:0;line-height:1.6;">{desc}</p>
          </a>
        """)

    return f"""
    <section class="related-posts-section" style="margin-top:48px;padding-top:32px;border-top:1px solid var(--line);">
      <h2 style="font-size:1.4rem;color:var(--green-dark);margin-bottom:20px;font-weight:900;">💡 延伸閱讀・精選衛教文章</h2>
      <div style="display:grid;grid-template-columns:repeat(auto-fit,minmax(260px,1fr));gap:16px;">
        {''.join(cards_html)}
      </div>
    </section>
    """

def generate_static_post(post, all_posts):
    post_id = post.get('id', '')
    title = post.get('title', '')
    date_str = post.get('date', '2026-08-25')
    category = post.get('category', '營養衛教')
    excerpt = clean_summary(post)
    kws = post.get('keywords', [])
    if not kws:
        kws = ["實證營養", "衛教專欄", "長照營養", "肌少症", "Kat Chang", "凱特營養師"]
    kws_str = ", ".join(kws)
    
    canonical_url = f"{BASE_URL}/blog/{post_id}.html"
    image_abs = get_image_url(post)
    image_rel = get_image_rel(post)
    body_html = post.get('body', '')

    keywords_spans = "".join([f"<span>{escape(k)}</span>" for k in kws[:6]])

    # JSON-LD
    schema_data = {
        "@context": "https://schema.org",
        "@graph": [
            {
                "@type": "BlogPosting",
                "headline": title,
                "description": excerpt,
                "image": [image_abs],
                "datePublished": date_str,
                "dateModified": date_str,
                "articleSection": category,
                "keywords": kws_str,
                "mainEntityOfPage": canonical_url,
                "author": {
                    "@type": "Person",
                    "name": "張雁雲營養師",
                    "alternateName": "Kat Chang 凱特營養師",
                    "url": f"{BASE_URL}/about.html"
                },
                "publisher": {
                    "@type": "Person",
                    "name": "張雁雲營養師",
                    "url": f"{BASE_URL}/"
                }
            },
            {
                "@type": "BreadcrumbList",
                "itemListElement": [
                    {
                        "@type": "ListItem",
                        "position": 1,
                        "name": "首頁",
                        "item": f"{BASE_URL}/"
                    },
                    {
                        "@type": "ListItem",
                        "position": 2,
                        "name": "衛教專欄",
                        "item": f"{BASE_URL}/blog/"
                    },
                    {
                        "@type": "ListItem",
                        "position": 3,
                        "name": title,
                        "item": canonical_url
                    }
                ]
            }
        ]
    }
    schema_json = json.dumps(schema_data, ensure_ascii=False, indent=2)

    related_html = build_related_posts_html(post, all_posts)

    html_content = f"""<!doctype html>
<html lang="zh-Hant">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>{escape(title)} ｜ Kat Chang 凱特營養師</title>
  <meta name="description" content="{escape(excerpt)}">
  <meta name="keywords" content="{escape(kws_str)}">
  <meta name="robots" content="index, follow, max-image-preview:large, max-snippet:-1">
  <link rel="canonical" href="{canonical_url}">
  
  <!-- Open Graph -->
  <meta property="og:type" content="article">
  <meta property="og:title" content="{escape(title)} ｜ Kat Chang 凱特營養師">
  <meta property="og:description" content="{escape(excerpt)}">
  <meta property="og:url" content="{canonical_url}">
  <meta property="og:image" content="{image_abs}">
  <meta property="og:image:width" content="1200">
  <meta property="og:image:height" content="630">
  <meta property="og:site_name" content="Kat Chang 凱特營養師">
  <meta property="og:locale" content="zh_TW">
  <meta property="article:published_time" content="{date_str}">
  
  <!-- Twitter Card -->
  <meta name="twitter:card" content="summary_large_image">
  <meta name="twitter:title" content="{escape(title)} ｜ Kat Chang 凱特營養師">
  <meta name="twitter:description" content="{escape(excerpt)}">
  <meta name="twitter:image" content="{image_abs}">

  <link rel="stylesheet" href="../styles.css?v=20260822-cover-fix">

  <script type="application/ld+json">
{schema_json}
  </script>
</head>
<body class="blog-directory">
  <header class="site-header">
    <a class="brand" href="../">
      <img src="../assets/profile/kat-avatar.jpg" alt="Kat Chang 凱特營養師">
      <span>Kat Chang</span>
    </a>
    <nav>
      <a href="../index.html">首頁</a>
      <a href="../about.html">簡介</a>
      <a href="../class.html">授課</a>
      <a href="../index.html#services">服務</a>
      <a href="../teach/">教具</a>
      <a href="./">文章</a>
      <a href="https://zcal.co/katchang" target="_blank" rel="noopener">聯絡</a>
    </nav>
  </header>

  <main>
    <article class="article" style="max-width:860px; margin:0 auto; padding: 24px 20px;">
      <div class="nav-breadcrumbs" style="margin-bottom:16px; font-size:0.95rem; color:var(--muted);">
        <a href="../" style="color:inherit; text-decoration:none;">首頁</a> &gt; 
        <a href="./" style="color:inherit; text-decoration:none;">衛教文章</a> &gt; 
        <span>{escape(title[:25])}…</span>
      </div>

      <a class="back-link" href="./">← 返回文章列表</a>
      
      <div class="post-meta" style="margin: 14px 0; color: var(--muted); font-size: 0.98rem;">
        {escape(date_str)}｜分類：<span class="category-tag" style="background:#eef6f2; color:var(--green-dark); padding:2px 10px; border-radius:999px; font-weight:700;">{escape(category)}</span>｜作者：<a href="../about.html" style="color:var(--green-dark); font-weight:700;">張雁雲營養師</a>
      </div>

      <h1 style="font-size: clamp(1.6rem, 3.2vw, 2.3rem); line-height: 1.35; margin-bottom: 18px; color: var(--ink); font-weight: 900;">{escape(title)}</h1>

      <div class="keywords" style="display:flex; flex-wrap:wrap; gap:8px; margin-bottom:24px;">
        {keywords_spans}
      </div>

      <img class="article-cover" src="{image_rel}" alt="{escape(title)}" style="width:100%; border-radius:18px; margin-bottom:28px; box-shadow:0 8px 24px rgba(0,0,0,0.06);">

      <div class="article-body" style="font-size:1.12rem; line-height:1.85; color:var(--ink);">
        {body_html}
      </div>

      {related_html}
    </article>

    <section class="contact-band directory-contact" style="margin-top:48px;">
      <div>
        <p class="eyebrow">Contact &amp; Lecture</p>
        <h2>企業健康講座與授課邀約</h2>
        <p>提供客製化職場活力抗疲勞飲食、樂齡肌少症防護與 100% 零明火手作烹飪示範。</p>
      </div>
      <div class="actions">
        <a class="btn primary" href="../class.html">檢視授課大綱與實績</a>
        <a class="btn" href="https://lin.ee/uGHIQcH" target="_blank" rel="noopener">官方 Line 洽詢</a>
      </div>
    </section>
  </main>

  <footer>
    @2026 Kat Chang 凱特營養師｜中高齡營養專家 ｜ <a href="https://594katchang-source.github.io/sitemap.html" style="color:inherit;font-weight:700;">網站地圖</a>
  </footer>
</body>
</html>
"""
    return html_content

def main():
    if not POSTS_FILE.exists():
        print(f"[ERROR] posts.json not found at {POSTS_FILE}")
        sys.exit(1)
        
    data = json.loads(POSTS_FILE.read_text(encoding="utf-8"))
    posts = data.get("posts", [])
    print(f"[*] 準備為 {len(posts)} 篇專文生成靜態 HTML...")

    generated_files = []
    for post in posts:
        pid = post.get('id')
        out_path = BLOG_DIR / f"{pid}.html"
        content = generate_static_post(post, posts)
        out_path.write_text(content, encoding="utf-8")
        generated_files.append(out_path.name)
        print(f"  [✓] 生成靜態頁：blog/{out_path.name}")

    print(f"\n[OK] 成功生成 {len(generated_files)} 篇實體靜態文章頁面！")
    return generated_files

if __name__ == '__main__':
    main()
