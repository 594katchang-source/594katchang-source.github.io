import json
from pathlib import Path


BASE = Path(__file__).resolve().parents[3]
REVIEW = BASE / "work" / "2026-08-15-seo-review-docs" / "source" / "chapter-04-review.json"
POSTS = BASE / "blog" / "posts.json"


def main():
    review = json.loads(REVIEW.read_text(encoding="utf-8"))
    data = json.loads(POSTS.read_text(encoding="utf-8"))
    posts = data["posts"]
    article_id = review["slug"]
    if any(post.get("id") == article_id for post in posts):
        raise SystemExit(f"target article already exists locally: {article_id}")
    posts.append(
        {
            "id": article_id,
            "title": review["seoTitle"],
            "date": review["reviewDate"],
            "excerpt": review["seoDescription"],
            "keywords": review["targetTerms"][:5],
            "showOnHome": False,
            "body": review["bodyHtml"],
            "category": review["category"],
            "faq": review["faqEntities"],
        }
    )
    POSTS.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({"path": str(POSTS), "articleId": article_id, "postCount": len(posts), "showOnHome": False}, ensure_ascii=False))


if __name__ == "__main__":
    main()
