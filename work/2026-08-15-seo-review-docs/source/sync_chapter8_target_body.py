import json
import sys
from pathlib import Path


sys.stdout.reconfigure(encoding="utf-8")

ROOT = Path(__file__).resolve().parents[3]
WORK = ROOT / "work" / "2026-08-15-seo-review-docs"
TARGET_PATH = WORK / "source" / "chapter-08-publish.json"
POSTS_PATH = ROOT / "blog" / "posts.json"
TARGET_ID = "2026-09-01-how-much-water-electrolytes-calcium-iron-bone-health"


def main():
    target = json.loads(TARGET_PATH.read_text(encoding="utf-8"))
    if target.get("id") != TARGET_ID:
        raise RuntimeError("Publish source target ID is not Chapter 8")

    posts_doc = json.loads(POSTS_PATH.read_text(encoding="utf-8"))
    matches = [index for index, post in enumerate(posts_doc.get("posts", [])) if post.get("id") == TARGET_ID]
    if len(matches) != 1:
        raise RuntimeError(f"Expected exactly one local Chapter 8 target, found {len(matches)}")

    index = matches[0]
    before = posts_doc["posts"][index].get("body", "")
    posts_doc["posts"][index]["body"] = target["body"]
    POSTS_PATH.write_text(json.dumps(posts_doc, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({
        "target_id": TARGET_ID,
        "body_changed": before != target["body"],
        "old_link_count": before.count("<a href="),
        "new_link_count": target["body"].count("<a href="),
        "requested_url_present": "https://www.hpa.gov.tw/Pages/Detail.aspx?nodeid=4306&amp;pid=14493" in target["body"],
    }, ensure_ascii=False))


if __name__ == "__main__":
    main()
