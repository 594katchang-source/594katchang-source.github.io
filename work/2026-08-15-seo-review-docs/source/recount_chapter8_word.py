import re
import sys
from pathlib import Path

from docx import Document
from docx.oxml.ns import qn
from docx.table import Table
from docx.text.paragraph import Paragraph


sys.stdout.reconfigure(encoding="utf-8")

DOCX = Path(__file__).resolve().parents[1] / "output" / "chapter-08-water-minerals-seo-review.docx"


def body_text(document):
    blocks = []
    started = False
    for child in document.element.body.iterchildren():
        if child.tag == qn("w:p"):
            paragraph = Paragraph(child, document)
            text = paragraph.text.strip()
            if text.startswith("開場："):
                started = True
            if paragraph.style.name == "Heading 1" and text == "SEO 描述":
                break
            if started and text:
                blocks.append(text)
        elif child.tag == qn("w:tbl") and started:
            for row in Table(child, document).rows:
                for cell in row.cells:
                    if cell.text.strip():
                        blocks.append(cell.text)
    return "\n".join(blocks)


def main():
    document = Document(DOCX)
    text = body_text(document)
    characters = len(text)
    without_whitespace = len(re.sub(r"\s+", "", text))
    matches = [p for p in document.paragraphs if p.text.startswith("正文實際字數：")]
    if len(matches) != 1:
        raise RuntimeError(f"Expected one count paragraph, found {len(matches)}")
    paragraph = matches[0]
    for run in paragraph.runs:
        if re.fullmatch(r"[0-9,]+ ", run.text):
            run.text = f"{characters:,} "
        elif re.fullmatch(r" [0-9,]+ ", run.text):
            run.text = f" {without_whitespace:,} "
    document.save(DOCX)
    print(f"正文實際字數：{characters:,} 字元；去除空白後：{without_whitespace:,} 字元")


if __name__ == "__main__":
    main()
