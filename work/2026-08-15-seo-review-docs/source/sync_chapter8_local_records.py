import html
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
WORK = ROOT / "work" / "2026-08-15-seo-review-docs"
TARGET = json.loads((WORK / "source" / "chapter-08-publish.json").read_text(encoding="utf-8"))
POSTS = ROOT / "blog" / "posts.json"
SITEMAP = ROOT / "sitemap.xml"
SITEMAP_HTML = ROOT / "sitemap.html"


def main():
    posts_doc = json.loads(POSTS.read_text(encoding="utf-8"))
    if not any(item.get("id") == TARGET["id"] for item in posts_doc["posts"]):
        posts_doc["posts"].append(TARGET)
        POSTS.write_text(json.dumps(posts_doc, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
        posts_action = "appended"
    else:
        posts_action = "already-present"

    article_url = f"https://594katchang-source.github.io/blog/post.html?id={TARGET['id']}"
    sitemap_text = SITEMAP.read_text(encoding="utf-8")
    if article_url not in sitemap_text:
        entry = (
            "  <url>\n"
            f"    <loc>{article_url}</loc>\n"
            "    <lastmod>2026-09-01</lastmod>\n"
            "    <changefreq>monthly</changefreq>\n"
            "    <priority>0.8</priority>\n"
            "  </url>\n"
        )
        sitemap_text = sitemap_text.replace("</urlset>", entry + "</urlset>")
        SITEMAP.write_text(sitemap_text, encoding="utf-8")
        sitemap_action = "appended"
    else:
        sitemap_action = "already-present"

    html_text = SITEMAP_HTML.read_text(encoding="utf-8")
    if TARGET["id"] not in html_text:
        marker = "<li class=\"sitemap-item\"><a href=\"https://594katchang-source.github.io/blog/post.html?id=2026-08-25-vitamins-book-notes\">"
        index = html_text.find(marker)
        if index < 0:
            raise RuntimeError("Could not find Chapter 7 sitemap insertion point")
        eol = "\r\n" if "\r\n" in html_text else "\n"
        title = html.escape(TARGET["title"], quote=True)
        excerpt = html.escape(TARGET["excerpt"], quote=True)
        entry = f"        <li class=\"sitemap-item\"><a href=\"{article_url}\">衛教：{title}</a><p class=\"sitemap-desc\">【2026-09-01】{excerpt}</p></li>"
        html_text = html_text[:index] + entry + eol + html_text[index:]
        SITEMAP_HTML.write_text(html_text, encoding="utf-8")
        html_action = "appended"
    else:
        html_action = "already-present"

    print(json.dumps({"posts": posts_action, "sitemap_xml": sitemap_action, "sitemap_html": html_action}, ensure_ascii=False))


if __name__ == "__main__":
    main()
