from __future__ import annotations

import os
import sys
import zipfile
from pathlib import Path

from lxml import etree

sys.stdout.reconfigure(encoding="utf-8")

PROJECT = Path(__file__).resolve().parents[3]
DOCX = PROJECT / "work" / "2026-08-15-seo-review-docs" / "output" / "chapter-08-water-minerals-seo-review.docx"
TEMP = DOCX.with_suffix(".tmp.docx")
W_NS = "http://schemas.openxmlformats.org/wordprocessingml/2006/main"
NS = {"w": W_NS}


def paragraph_text(element: etree._Element) -> str:
    return "".join(element.xpath(".//w:t/text()", namespaces=NS)).strip()


def main() -> None:
    with zipfile.ZipFile(DOCX, "r") as source_zip:
        entries = source_zip.infolist()
        payloads = {info.filename: source_zip.read(info.filename) for info in entries}

    root = etree.fromstring(payloads["word/document.xml"])
    body = root.find("w:body", namespaces=NS)
    if body is None:
        raise RuntimeError("word/document.xml has no w:body")

    children = list(body)
    quick_versions = [child for child in children if child.tag == f"{{{W_NS}}}p" and paragraph_text(child) == "省時版本："]
    questions = [
        child
        for child in children
        if child.tag == f"{{{W_NS}}}p" and paragraph_text(child).startswith("本章的四個生活問題很適合拿來自我檢查：")
    ]
    if len(quick_versions) != 1:
        raise RuntimeError(f"expected one quick-version heading, found {len(quick_versions)}")
    if len(questions) != 2:
        raise RuntimeError(f"expected two question paragraphs, found {len(questions)}")

    quick = quick_versions[0]
    question = questions[-1]
    quick_index = list(body).index(quick)
    following = list(body)[quick_index + 1]
    if following.tag != f"{{{W_NS}}}tbl":
        raise RuntimeError("the quick-version heading is not followed by its table")

    body.remove(quick)
    body.remove(following)
    target_index = list(body).index(question)
    body.insert(target_index, quick)
    body.insert(target_index + 1, following)
    payloads["word/document.xml"] = etree.tostring(root, xml_declaration=True, encoding="UTF-8", standalone=True)

    with zipfile.ZipFile(TEMP, "w") as target_zip:
        for info in entries:
            target_zip.writestr(info, payloads[info.filename])
    os.replace(TEMP, DOCX)
    print(f"updated={DOCX}")


if __name__ == "__main__":
    main()
