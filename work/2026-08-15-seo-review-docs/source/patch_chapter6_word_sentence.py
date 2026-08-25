from __future__ import annotations

import sys
import tempfile
import zipfile
import xml.etree.ElementTree as ET
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8")

INPUT = Path(__file__).resolve().parent.parent / "output" / "chapter-06-proteins-amino-acids-seo-review.docx"
OLD = "蛋白質不能夠只強調在健身上，太過簡化了。"
NEW = "談蛋白質的功能，不能只聚焦在健身用途上，這樣的理解太過簡化了。"
W_NS = "http://schemas.openxmlformats.org/wordprocessingml/2006/main"
W_T = f"{{{W_NS}}}t"
W_P = f"{{{W_NS}}}p"


def replace_in_paragraph(paragraph: ET.Element) -> int:
    text_nodes = paragraph.findall(".//w:t", {"w": W_NS})
    full_text = "".join(node.text or "" for node in text_nodes)
    start = full_text.find(OLD)
    if start < 0:
        return 0
    if full_text.count(OLD) != 1:
        raise RuntimeError("target phrase occurs more than once in one paragraph")

    end = start + len(OLD)
    offsets = []
    cursor = 0
    for node in text_nodes:
        value = node.text or ""
        offsets.append((node, cursor, cursor + len(value)))
        cursor += len(value)

    overlapping = [(node, a, b) for node, a, b in offsets if a < end and b > start]
    first_node, _, _ = overlapping[0]
    for node, a, b in overlapping:
        left = max(start - a, 0)
        right = min(end - a, b - a)
        value = node.text or ""
        prefix = value[:left]
        suffix = value[right:]
        if node is first_node:
            node.text = prefix + NEW + suffix
        else:
            node.text = suffix
    return 1


def main() -> None:
    with zipfile.ZipFile(INPUT, "r") as source_zip:
        members = {info.filename: source_zip.read(info.filename) for info in source_zip.infolist()}

    document = ET.fromstring(members["word/document.xml"])
    paragraphs = document.findall(f".//{W_P}")
    replacements = sum(replace_in_paragraph(paragraph) for paragraph in paragraphs)
    if replacements != 1:
        raise RuntimeError(f"expected one replacement, got {replacements}")

    members["word/document.xml"] = ET.tostring(document, encoding="UTF-8", xml_declaration=True)
    with tempfile.NamedTemporaryFile(prefix="chapter6-", suffix=".docx", dir=INPUT.parent, delete=False) as handle:
        temp_path = Path(handle.name)
    try:
        with zipfile.ZipFile(temp_path, "w", compression=zipfile.ZIP_DEFLATED) as output_zip:
            for name, data in members.items():
                output_zip.writestr(name, data)
        temp_path.replace(INPUT)
    finally:
        if temp_path.exists():
            temp_path.unlink()
    print(f"updated={INPUT}")
    print(f"replacements={replacements}")


if __name__ == "__main__":
    main()
