import html
import json
import re
import sys
from difflib import SequenceMatcher
from html.parser import HTMLParser
from pathlib import Path

from docx import Document
from docx.table import Table
from docx.text.paragraph import Paragraph

sys.stdout.reconfigure(encoding='utf-8')

ROOT = Path(__file__).resolve().parents[3]
POSTS = ROOT / 'blog' / 'posts.json'
OUTPUT = ROOT / 'work' / '2026-08-15-seo-review-docs' / 'output'
MAPPING = {
    '2026-08-14-food-choices-human-health-guide': 'chapter-01-food-choices-seo-review.docx',
    '2026-08-15-nutrition-tools-standards-guidelines': 'chapter-02-nutrition-tools-seo-review.docx',
    '2026-08-16-remarkable-body-nutrition-guide': 'chapter-03-remarkable-body-seo-review.docx',
    '2026-08-17-carbohydrates-food-guide': 'chapter-04-carbohydrates-seo-review.docx',
    '2026-08-20-lipids-fatty-acids-guide': 'chapter-05-lipids-seo-review.docx',
    '2026-08-22-proteins-amino-acids-book-notes': 'chapter-06-proteins-amino-acids-seo-review.docx',
    '2026-08-25-vitamins-book-notes': 'chapter-07-vitamins-seo-review.docx',
}


def norm(value):
    value = html.unescape(value or '')
    value = value.replace('\u00a0', ' ')
    return re.sub(r'\s+', '', value)


class HTMLBlocks(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.blocks = []
        self.current = []
        self.block_tag = None
        self.table = None
        self.row = None
        self.cell = None

    def target(self):
        return self.cell if self.cell is not None else self.current

    def flush(self):
        if self.block_tag and self.current:
            value = norm(''.join(self.current))
            if value:
                self.blocks.append((self.block_tag, value))
        self.current = []
        self.block_tag = None

    def handle_starttag(self, tag, attrs):
        if tag in ('p', 'h2', 'h3'):
            self.flush()
            self.block_tag = tag
        elif tag == 'table':
            self.flush()
            self.table = []
        elif tag == 'tr':
            self.row = []
        elif tag in ('th', 'td'):
            self.cell = []
        elif tag == 'br':
            self.target().append(' ')

    def handle_data(self, data):
        self.target().append(data)

    def handle_endtag(self, tag):
        if tag in ('th', 'td'):
            if self.row is not None and self.cell is not None:
                self.row.append(norm(''.join(self.cell)))
            self.cell = None
        elif tag == 'tr':
            if self.table is not None and self.row:
                self.table.append(tuple(self.row))
            self.row = None
        elif tag == 'table':
            self.flush()
            for row in self.table or []:
                self.blocks.append(('tr', '|'.join(row)))
            self.table = None
        elif tag in ('p', 'h2', 'h3'):
            self.flush()


def html_blocks(value):
    parser = HTMLBlocks()
    parser.feed(value)
    return parser.blocks


def docx_blocks(path):
    doc = Document(path)
    blocks = []
    for child in doc.element.body.iterchildren():
        if child.tag.endswith('}p'):
            text = norm(Paragraph(child, doc).text)
            if text:
                blocks.append(('p', text))
        elif child.tag.endswith('}tbl'):
            table = Table(child, doc)
            for row in table.rows:
                text = '|'.join(norm(cell.text) for cell in row.cells)
                if text:
                    blocks.append(('tr', text))
    return blocks


def short(value, limit=280):
    return value if len(value) <= limit else value[:limit] + '...'


posts = json.loads(POSTS.read_text(encoding='utf-8'))['posts']
print('blog_word_sequence_diff')
for post_id, docx_name in MAPPING.items():
    post = next(item for item in posts if item['id'] == post_id)
    blog = html_blocks(post.get('body', ''))
    word = docx_blocks(OUTPUT / docx_name)
    matcher = SequenceMatcher(a=[value for _, value in blog], b=[value for _, value in word], autojunk=False)
    print(f'\nID: {post_id}')
    print(f'  blog_blocks={len(blog)} word_blocks={len(word)}')
    printed = 0
    for tag, i1, i2, j1, j2 in matcher.get_opcodes():
        if tag == 'equal':
            continue
        print(f'  {tag} blog[{i1}:{i2}] word[{j1}:{j2}]')
        if i1 != i2:
            for index in range(i1, min(i2, i1 + 3)):
                print(f'    BLOG {index:03d} {blog[index][0]} {short(blog[index][1])}')
        if j1 != j2:
            for index in range(j1, min(j2, j1 + 3)):
                print(f'    WORD {index:03d} {word[index][0]} {short(word[index][1])}')
        printed += 1
        if printed >= 12:
            print('  ... more differences omitted')
            break
