import sys
import zipfile
import xml.etree.ElementTree as ET
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8")

docx_path = Path(__file__).parent / "output" / "chapter-04-carbohydrates-seo-review.docx"
ns = {
    "w": "http://schemas.openxmlformats.org/wordprocessingml/2006/main",
    "r": "http://schemas.openxmlformats.org/officeDocument/2006/relationships",
}

with zipfile.ZipFile(docx_path) as archive:
    root = ET.fromstring(archive.read("word/document.xml"))
    rel_root = ET.fromstring(archive.read("word/_rels/document.xml.rels"))

rel_map = {item.attrib.get("Id"): item.attrib.get("Target") for item in rel_root}
paragraphs = root.findall(".//w:body/w:p", ns)

for index, paragraph in enumerate(paragraphs[58:90], 58):
    text = "".join(node.text or "" for node in paragraph.findall(".//w:t", ns)).strip()
    links = []
    for hyperlink in paragraph.findall(".//w:hyperlink", ns):
        rid = hyperlink.attrib.get("{%s}id" % ns["r"])
        links.append(rel_map.get(rid))
    print(index, "HYPERLINKS=" + str(links), repr(text[:240]))
