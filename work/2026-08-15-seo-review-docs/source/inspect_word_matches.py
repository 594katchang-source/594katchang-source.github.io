import sys
from pathlib import Path

from docx import Document
from docx.table import Table
from docx.text.paragraph import Paragraph

sys.stdout.reconfigure(encoding='utf-8')
ROOT = Path(__file__).resolve().parents[3]
OUTPUT = ROOT / 'work' / '2026-08-15-seo-review-docs' / 'output'
TARGETS = {
    'chapter-02-nutrition-tools-seo-review.docx': ['植化素', '食物基質', '同一條思考路線'],
    'chapter-06-proteins-amino-acids-seo-review.docx': ['蛋白質與胺基酸', 'Controversy 6', '書籍重點', '這張表讓我重新理解', '書中以蛋白質合成說明', '固定答案'],
    'chapter-07-vitamins-seo-review.docx': ['維生素怎麼吃才安心', '閱讀本章時', '食物是日常底盤', '本章從維生素', '接著整理脂溶性', '分辨方式', '先看身體如何處理', '安全保證', '長期堆高', '可提供較容易', '國健署第八版', '抗老膠囊', '蔬果是日常', '烹調水', '清楚分流', '遮住B12', '吃肉就一定夠', '書中把補充品', '自動變成', '直接等同效果好', '一個可執行', '缺口是什麼', '回頭評估', '判讀順序', '瓶身正面', '入口', '日常底盤', '不等於提神', '不等於感冒藥', '單一答案'],
}

for filename, needles in TARGETS.items():
    doc = Document(OUTPUT / filename)
    print(f'\nFILE {filename}')
    body = False
    index = 0
    for child in doc.element.body.iterchildren():
        if child.tag.endswith('}p'):
            p = Paragraph(child, doc)
            text = p.text
            if text.strip() == '正文':
                body = True
                continue
            if body and text.strip() == 'SEO 描述':
                break
            if body:
                hits = [needle for needle in needles if needle in text]
                if hits:
                    print(f'P {index:03d} style={p.style.name!r} hits={hits}')
                    print(f'  {text}')
                index += 1
        elif child.tag.endswith('}tbl') and body:
            table = Table(child, doc)
            for row in table.rows:
                for cell in row.cells:
                    text = cell.text
                    hits = [needle for needle in needles if needle in text]
                    if hits:
                        print(f'T {index:03d} hits={hits}')
                        print(f'  {text}')
                index += 1
