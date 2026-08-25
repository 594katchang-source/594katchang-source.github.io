import json
import sys
import zipfile
import xml.etree.ElementTree as ET
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8")
docx_path = Path(__file__).resolve().parent.parent / "output" / "chapter-04-carbohydrates-seo-review.docx"
ns = {"w": "http://schemas.openxmlformats.org/wordprocessingml/2006/main"}

with zipfile.ZipFile(docx_path) as archive:
    root = ET.fromstring(archive.read("word/document.xml"))

rows = []
for index, table in enumerate(root.findall(".//w:tbl", ns), 1):
    props = table.find("./w:tblPr", ns)
    def prop_value(path):
        node = props.find(path, ns) if props is not None else None
        return node.get("{%s}w" % ns["w"]) if node is not None else None
    layout = props.find("./w:tblLayout", ns) if props is not None else None
    tr_nodes = table.findall("./w:tr", ns)
    rows.append({
        "table": index,
        "width": prop_value("./w:tblW"),
        "indent": prop_value("./w:tblInd"),
        "layout": layout.get("{%s}type" % ns["w"]) if layout is not None else None,
        "header": tr_nodes[0].find("./w:trPr/w:tblHeader", ns) is not None if tr_nodes else False,
        "cantSplitAll": all(row.find("./w:trPr/w:cantSplit", ns) is not None for row in tr_nodes),
        "rows": len(tr_nodes),
    })
print(json.dumps(rows, ensure_ascii=False, indent=2))
