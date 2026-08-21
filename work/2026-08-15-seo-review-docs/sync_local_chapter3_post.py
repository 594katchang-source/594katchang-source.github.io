from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(r"D:\@Codex\594katchang-source.github.io-main")
SOURCE = ROOT / "work" / "2026-08-15-seo-review-docs" / "source" / "chapter-03-review.json"
POSTS = ROOT / "blog" / "posts.json"


def read_json(path: Path):
    return json.loads(path.read_text(encoding="utf-8-sig"))


source = read_json(SOURCE)
payload = read_json(POSTS)
target_id = source["slug"]
matches = [index for index, post in enumerate(payload["posts"]) if post.get("id") == target_id]
if len(matches) != 1:
    raise SystemExit(f"expected exactly one local Chapter 3 target, found {len(matches)}")

index = matches[0]
old_target = payload["posts"][index]
new_target = {
    "id": target_id,
    "slug": target_id,
    "title": source["seoTitle"],
    "date": "2026-08-16",
    "category": source["category"],
    "tags": source["tags"],
    "excerpt": source["seoDescription"],
    "keywords": source["targetTerms"][:5],
    "showOnHome": False,
    "faq": source["faqEntities"],
    "body": source["bodyHtml"],
}

if old_target.get("showOnHome") is True:
    raise SystemExit("refusing to change a manually selected homepage post")

payload["posts"][index] = new_target
POSTS.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
print(json.dumps({
    "target": target_id,
    "oldBodyCharacters": len(old_target.get("body", "")),
    "newBodyCharacters": len(new_target["body"]),
    "newInternalLinks": new_target["body"].count("<a "),
    "showOnHome": new_target["showOnHome"],
    "nonTargetCount": len(payload["posts"]) - 1,
}, ensure_ascii=False))
