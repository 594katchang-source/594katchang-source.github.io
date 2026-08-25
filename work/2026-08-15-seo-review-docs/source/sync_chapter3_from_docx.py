import html
import json
import re
from pathlib import Path

from docx.document import Document as DocumentObject
from docx.table import Table, _Cell
from docx.text.paragraph import Paragraph
from docx.oxml.table import CT_Tbl
from docx.oxml.text.paragraph import CT_P
from docx.oxml.ns import qn
from docx import Document


BASE = Path(__file__).resolve().parent.parent
SOURCE_DIR = BASE / "source"
OUTPUT_DIR = BASE / "output"
DOCX_PATH = OUTPUT_DIR / "chapter-03-remarkable-body-seo-review.docx"
JSON_PATH = SOURCE_DIR / "chapter-03-review.json"
HTML_PATH = SOURCE_DIR / "chapter-03-review.html"


def iter_block_items(parent):
    if isinstance(parent, DocumentObject):
        parent_elm = parent.element.body
    elif isinstance(parent, _Cell):
        parent_elm = parent._tc
    else:
        raise ValueError("unsupported parent")
    for child in parent_elm.iterchildren():
        if isinstance(child, CT_P):
            yield Paragraph(child, parent)
        elif isinstance(child, CT_Tbl):
            yield Table(child, parent)


def paragraph_text(paragraph):
    return paragraph.text.replace("\r", "").strip()


def inline_html(element, part):
    chunks = []
    for node in element.iter():
        if node.tag == qn("w:t"):
            chunks.append(html.escape(node.text or ""))
        elif node.tag == qn("w:br"):
            chunks.append("<br>")
    if element.tag == qn("w:hyperlink"):
        rid = element.get(qn("r:id"))
        relationship = part.rels.get(rid) if rid else None
        if relationship and relationship.target_ref:
            return f'<a href="{html.escape(relationship.target_ref, quote=True)}">{"".join(chunks)}</a>'
    return "".join(chunks)


def paragraph_inner_html(paragraph):
    chunks = []
    for child in paragraph._p.iterchildren():
        if child.tag in (qn("w:r"), qn("w:hyperlink")):
            chunks.append(inline_html(child, paragraph.part))
    markup = "".join(chunks) or html.escape(paragraph.text).replace("\n", "<br>")
    # Some Word revisions keep a visible URL in [URL] notation while the
    # review section stores the same destinations as real hyperlinks. Keep
    # the visible text and make those body links usable on the published page.
    return re.sub(
        r"\[(https?://[^\]]+)\]",
        lambda match: f'<a href="{html.escape(match.group(1), quote=True)}">{html.escape(match.group(1))}</a>',
        markup,
    )


def table_html(table):
    rows = [[html.escape(cell.text.strip()) for cell in row.cells] for row in table.rows]
    if not rows:
        return ""
    head = "<thead><tr>" + "".join(f"<th>{cell}</th>" for cell in rows[0]) + "</tr></thead>"
    body = "".join("<tr>" + "".join(f"<td>{cell}</td>" for cell in row) + "</tr>" for row in rows[1:])
    return f"<table>{head}<tbody>{body}</tbody></table>"


def append_list(events, list_tag, text):
    if events and events[-1][0] == "list" and events[-1][1] == list_tag:
        events[-1][2].append(text)
    else:
        events.append(["list", list_tag, [text]])


def close_lists(events):
    return events


def body_from_docx(document):
    blocks = list(iter_block_items(document))
    in_body = False
    article_title = None
    events = []
    for block in blocks:
        if isinstance(block, Paragraph):
            text = paragraph_text(block)
            style_name = block.style.name if block.style else ""
            if not in_body:
                if text == "正文":
                    in_body = True
                continue
            if text == "SEO 描述":
                break
            if article_title is None:
                if text and style_name.startswith("Heading 2"):
                    article_title = text
                continue
            if not text:
                continue
            if style_name.startswith("Heading 2"):
                events.append(["heading", 2, text])
            elif style_name.startswith("Heading 3"):
                events.append(["heading", 3, text])
            elif style_name.startswith("List Number"):
                append_list(events, "ol", paragraph_inner_html(block))
            elif style_name.startswith("List Bullet"):
                append_list(events, "ul", paragraph_inner_html(block))
            else:
                events.append(["paragraph_html", paragraph_inner_html(block)])
        elif isinstance(block, Table) and in_body and article_title is not None:
            events.append(["table", table_html(block)])

    if article_title is None:
        raise RuntimeError("Word body article title not found")
    chunks = []
    for event in events:
        kind = event[0]
        if kind == "heading":
            chunks.append(f"<h{event[1]}>{html.escape(event[2])}</h{event[1]}>")
        elif kind == "paragraph_html":
            chunks.append(f"<p>{event[1]}</p>")
        elif kind == "table":
            chunks.append(event[1])
        elif kind == "list":
            items = "".join(f"<li>{item}</li>" for item in event[2])
            chunks.append(f"<{event[1]}>{items}</{event[1]}>")
    return article_title, "\n".join(chunks)


def visible_text(markup):
    text = re.sub(r"<script[\s\S]*?</script>", " ", markup, flags=re.I)
    text = re.sub(r"<style[\s\S]*?</style>", " ", text, flags=re.I)
    text = re.sub(r"<[^>]+>", " ", text)
    return re.sub(r"\s+", " ", html.unescape(text)).strip()


def faq_from_body(body_html):
    faq_section = body_html.split("<h2>FAQ：", 1)[-1]
    faq_section = faq_section.split("</h2>", 1)[-1]
    pattern = re.compile(r"<h3>(.*?)</h3>\s*<p>(.*?)</p>", re.S)
    faq_entities = []
    for question, answer in pattern.findall(faq_section):
        clean_question = visible_text(question)
        clean_answer = visible_text(answer)
        if clean_question and clean_answer:
            faq_entities.append({"question": clean_question, "answer": clean_answer})
    return faq_entities


def render_review_html(data):
    def esc(value):
        return html.escape(str(value))

    links = "".join(f'<li><a href="{esc(url)}">{esc(label)}</a></li>' for label, url in data["internalLinks"])
    faq = "".join(f"<li>{esc(item)}</li>" for item in data["faq"])
    source_rows = "".join(
        f'<tr><td>{esc(label)}</td><td><a href="{esc(url)}">{esc(url)}</a></td><td>{esc(scope)}</td></tr>'
        for label, url, scope in data["sources"]
    )
    claims = "".join(f"<li>{esc(item)}</li>" for item in data["originalClaims"])
    pending = "".join(f"<li>{esc(item)}</li>" for item in data["pending"])
    return f'''<!doctype html>
<html lang="zh-Hant"><head><meta charset="utf-8"><title>{esc(data["reviewTitle"])}</title><link rel="canonical" href="{esc(data["canonical"])}"></head><body>
<h1>{esc(data["reviewTitle"])}</h1>
<h2>SEO 標題</h2><p>{esc(data["seoTitle"])}</p>
<h2>目標搜尋字詞、相關搜尋字詞與搜尋意圖</h2><p><strong>目標：</strong>{"、".join(data["targetTerms"])}</p><p><strong>相關：</strong>{"、".join(data["relatedTerms"])}</p><p><strong>搜尋意圖：</strong>{esc(data["searchIntent"])}</p>
<h2>文章摘要與適合搜尋結果顯示的開場</h2><p>{esc(data["summary"])}</p><p>{esc(data["opening"])}</p>
<h2>正文</h2><h3>{esc(data["articleTitle"])}</h3>{data["bodyHtml"]}
<h2>SEO 描述</h2><p>{esc(data["seoDescription"])}</p>
<h2>文章分類、標籤與網址 slug</h2><p><strong>分類：</strong>{esc(data["category"])}</p><p><strong>標籤：</strong>{"、".join(data["tags"])}</p><p><strong>slug：</strong>{esc(data["slug"])}</p><p><strong>canonical：</strong>{esc(data["canonical"])}</p>
<h2>站內連結建議</h2><ul>{links}</ul>
<h2>FAQ 題目與結構化資料建議</h2><ul>{faq}</ul><p>{esc(data["faqSchema"])}</p>
<h2>文章結構化資料、作者、更新日期與 canonical 建議</h2><p>{"、".join(data["articleSchema"])}</p><p>{esc(data["author"])}</p>
<h2>來源連結與各來源支持的段落或主張</h2><table><thead><tr><th>來源</th><th>連結或檔案</th><th>支持內容</th></tr></thead><tbody>{source_rows}</tbody></table>
<h2>文章字數、原創差異化主張與待確認事項</h2><p>正文可見字數：{data["wordCount"]["characters"]} 字，空白分隔詞數 {data["wordCount"]["words"]}。</p><h3>原創差異化主張</h3><ul>{claims}</ul><h3>待確認事項</h3><ul>{pending}</ul>
</body></html>'''


def main():
    data = json.loads(JSON_PATH.read_text(encoding="utf-8"))
    document = Document(DOCX_PATH)
    article_title, body_html = body_from_docx(document)
    data["articleTitle"] = article_title
    data["bodyHtml"] = body_html
    faq_entities = faq_from_body(body_html)
    if faq_entities:
        data["faqEntities"] = faq_entities
        data["faq"] = [item["question"] for item in faq_entities]
    data["wordCount"] = {"characters": len(visible_text(body_html)), "words": len(visible_text(body_html).split())}
    data["sources"] = [
        [label, url, scope.replace("Controversy 3", "爭議 3")]
        for label, url, scope in data["sources"]
    ]
    data["sourcePageAudit"] = [item.replace("Controversy 3 Alcohol", "爭議 3 Alcohol") for item in data["sourcePageAudit"]]
    data["pending"] = [item.replace("Controversy", "爭議") for item in data["pending"]]
    JSON_PATH.write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8")
    HTML_PATH.write_text(render_review_html(data), encoding="utf-8")
    print(json.dumps({"articleTitle": article_title, "wordCount": data["wordCount"], "faq": len(data["faq"]), "bodyTables": body_html.count("<table>")}, ensure_ascii=False))


if __name__ == "__main__":
    main()
