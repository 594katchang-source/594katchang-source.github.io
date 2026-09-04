import html
import re
from pathlib import Path

from docx import Document
from docx.oxml.ns import qn
from docx.table import Table
from docx.text.paragraph import Paragraph


ROOT = Path(__file__).resolve().parents[3]
WORK = ROOT / "work" / "2026-08-15-seo-review-docs"
DOCX = WORK / "output" / "chapter-08-water-minerals-seo-review.docx"
MARKDOWN = WORK / "output" / "chapter-08-water-minerals-seo-review.md"


def inline_text(paragraph):
    parts = []
    children = list(paragraph._p)
    index = 0
    while index < len(children):
        child = children[index]
        if child.tag == qn("w:hyperlink"):
            rid = child.get(qn("r:id"))
            url = paragraph.part.rels[rid].target_ref if rid in paragraph.part.rels else ""
            text = "".join((node.text or "") for node in child.findall(".//" + qn("w:t")))
            if url and url.startswith("http"):
                parts.append(f"[{text}]({url})")
            else:
                parts.append(text)
            index += 1
            continue
        if child.tag != qn("w:r"):
            index += 1
            continue
        is_field_begin = any(
            node.tag == qn("w:fldChar") and node.get(qn("w:fldCharType")) == "begin"
            for node in child
        )
        if is_field_begin:
            instruction = []
            display = []
            separated = False
            end_index = index
            for field_index in range(index, len(children)):
                field_run = children[field_index]
                if field_run.tag != qn("w:r"):
                    continue
                field_ended = False
                for node in field_run:
                    if node.tag == qn("w:instrText"):
                        instruction.append(node.text or "")
                    elif node.tag == qn("w:fldChar"):
                        field_type = node.get(qn("w:fldCharType"))
                        if field_type == "separate":
                            separated = True
                        elif field_type == "end":
                            field_ended = True
                    elif separated and node.tag == qn("w:t"):
                        display.append(node.text or "")
                    elif separated and node.tag == qn("w:tab"):
                        display.append(" ")
                    elif separated and node.tag == qn("w:br"):
                        display.append("\n")
                if field_ended:
                    end_index = field_index
                    break
            instruction_text = "".join(instruction)
            display_text = "".join(display)
            match = re.search(r'HYPERLINK\s+"([^"]+)"', instruction_text, flags=re.IGNORECASE)
            if match and display_text:
                parts.append(f"[{display_text}]({match.group(1)})")
            else:
                parts.append(display_text)
            index = end_index + 1
            continue
        for node in child:
            if node.tag == qn("w:t"):
                parts.append(node.text or "")
            elif node.tag == qn("w:tab"):
                parts.append(" ")
            elif node.tag == qn("w:br"):
                parts.append("\n")
        index += 1
    return "".join(parts).strip()


def table_markdown(table):
    rows = []
    for row in table.rows:
        cells = [inline_text(paragraph) for cell in row.cells for paragraph in []]
        cells = []
        for cell in row.cells:
            value = "<br>".join(inline_text(p) for p in cell.paragraphs).strip()
            cells.append(value.replace("|", "\\|").replace("\n", "<br>"))
        rows.append(cells)
    if not rows:
        return ""
    width = max(len(row) for row in rows)
    rows = [row + [""] * (width - len(row)) for row in rows]
    lines = ["| " + " | ".join(rows[0]) + " |", "| " + " | ".join(["---"] * width) + " |"]
    lines.extend("| " + " | ".join(row) + " |" for row in rows[1:])
    return "\n".join(lines)


def main():
    document = Document(DOCX)
    lines = []
    list_state = None

    def flush_list():
        nonlocal list_state
        if list_state:
            lines.extend(list_state)
            lines.append("")
            list_state = None

    for child in document.element.body.iterchildren():
        if child.tag == qn("w:p"):
            paragraph = Paragraph(child, document)
            text = inline_text(paragraph)
            if not text:
                flush_list()
                continue
            style = paragraph.style.name if paragraph.style else ""
            if style == "List Bullet":
                if list_state is None or not list_state or not list_state[0].startswith("-"):
                    flush_list()
                    list_state = []
                list_state.append(f"- {text}")
            elif style == "List Number":
                if list_state is None or not list_state or not list_state[0].startswith("1."):
                    flush_list()
                    list_state = []
                list_state.append(f"1. {text}")
            else:
                flush_list()
                if style == "Heading 1":
                    lines.extend([f"# {text}", ""])
                elif style == "Heading 2":
                    lines.extend([f"## {text}", ""])
                elif style == "Heading 3":
                    lines.extend([f"### {text}", ""])
                else:
                    lines.extend([text, ""])
        elif child.tag == qn("w:tbl"):
            flush_list()
            value = table_markdown(Table(child, document))
            if value:
                lines.extend([value, ""])
    flush_list()
    MARKDOWN.write_text("\n".join(lines).rstrip() + "\n", encoding="utf-8")
    print(f"Synced Markdown from Word: {MARKDOWN}")


if __name__ == "__main__":
    main()
