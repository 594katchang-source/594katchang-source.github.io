from __future__ import annotations

import os
import sys
from pathlib import Path

from docx import Document

sys.stdout.reconfigure(encoding="utf-8")

ROOT = Path(__file__).resolve().parents[3]
DOCX = ROOT / "work/2026-08-15-seo-review-docs/output/chapter-08-water-minerals-seo-review.docx"
TEMP = DOCX.with_suffix(".tmp.docx")
OLD = "正文實際字數：8,110 字元，含正文內標點、表格、英文與文內連結，去除空白後 7,538 字元。"
NEW = "正文實際字數：8,156 字元，含正文內標點、表格、英文與文內連結，去除空白後 7,584 字元。"


def main() -> None:
    document = Document(DOCX)
    hits = 0
    for paragraph in document.paragraphs:
        for node in paragraph._p.xpath(".//w:t"):
            value = node.text or ""
            if OLD in value:
                node.text = value.replace(OLD, NEW)
                hits += 1
    if hits != 1:
        raise RuntimeError(f"expected one Word count replacement, found {hits}")
    document.save(TEMP)
    os.replace(TEMP, DOCX)
    print(f"updated={DOCX}")


if __name__ == "__main__":
    main()
