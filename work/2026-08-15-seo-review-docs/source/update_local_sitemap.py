from pathlib import Path


BASE = Path(__file__).resolve().parents[3]
SITEMAP = BASE / "sitemap.xml"
LOC = "https://594katchang-source.github.io/blog/post.html?id=2026-08-17-carbohydrates-food-guide"
ENTRY = f"  <url><loc>{LOC}</loc><lastmod>2026-08-19</lastmod><changefreq>monthly</changefreq><priority>0.8</priority></url>"


def main():
    content = SITEMAP.read_text(encoding="utf-8")
    if LOC in content:
        raise SystemExit("target sitemap entry already exists locally")
    if "</urlset>" not in content:
        raise SystemExit("unexpected local sitemap shape")
    SITEMAP.write_text(content.replace("</urlset>", ENTRY + "\n</urlset>"), encoding="utf-8")
    print(f"updated {SITEMAP}")


if __name__ == "__main__":
    main()
