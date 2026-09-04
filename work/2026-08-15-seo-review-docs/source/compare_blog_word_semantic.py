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


def clean(value):
    value = value or ''
    value = re.sub(r'https?://[^\s\]\)》」]+', '', value)
    value = value.replace('[', '').replace(']', '')
    return value


def tokens(value):
    value = clean(value)
    return re.findall(r'[\u4e00-\u9fff]+|[A-Za-z]+|\d+(?:\.\d+)?|[^\w\s]', value)


class HTMLBlocks(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.blocks = []
        self.current = []
        self.tag = None
        self.table = None
        self.row = None
        self.cell = None

    def target(self):
        if self.cell is not None:
            return self.cell
        return self.current

    def flush(self):
        if self.tag and ''.join(self.current).strip():
            self.blocks.append((self.tag, ''.join(self.current)))
        self.current = []
        self.tag = None

    def handle_starttag(self, tag, attrs):
        if tag in ('p', 'h2', 'h3', 'li'):
            self.flush()
            self.tag = tag
        elif tag == 'table':
            self.flush()
            self.table = []
        elif tag == 'tr':
            self.row = []
        elif tag in ('th', 'td'):
            self.cell = []
        elif tag == 'br':
            self.target().append('\n')

    def handle_data(self, data):
        self.target().append(data)

    def handle_endtag(self, tag):
        if tag in ('th', 'td'):
            if self.row is not None and self.cell is not None:
                self.row.append(''.join(self.cell))
            self.cell = None
        elif tag == 'tr':
            if self.table is not None and self.row:
                self.table.append(self.row)
            self.row = None
        elif tag == 'table':
            self.flush()
            for row in self.table or []:
                self.blocks.append(('tr', '|'.join(row)))
            self.table = None
        elif tag in ('p', 'h2', 'h3', 'li'):
            self.flush()


def blog_body_blocks(value):
    parser = HTMLBlocks()
    parser.feed(value)
    return parser.blocks


def word_body_blocks(path):
    doc = Document(path)
    blocks = []
    active = False
    for child in doc.element.body.iterchildren():
        if child.tag.endswith('}p'):
            paragraph = Paragraph(child, doc)
            text = paragraph.text.strip()
            style = paragraph.style.name.lower() if paragraph.style else ''
            if text == '正文':
                active = True
                continue
            if active and text == 'SEO 描述':
                break
            if active and text:
                kind = 'h2' if style == 'heading 2' else 'h3' if style == 'heading 3' else 'p'
                blocks.append((kind, text))
        elif child.tag.endswith('}tbl') and active:
            table = Table(child, doc)
            for row in table.rows:
                blocks.append(('tr', '|'.join(cell.text for cell in row.cells)))
    return blocks


def show_tokens(items, limit=55):
    text = ' '.join(items[:limit])
    return text + (' ...' if len(items) > limit else '')


posts = json.loads(POSTS.read_text(encoding='utf-8'))['posts']
only_id = sys.argv[1] if len(sys.argv) > 1 else None
print('blog_word_semantic_comparison')
for post_id, docx_name in MAPPING.items():
    if only_id and post_id != only_id:
        continue
    post = next(item for item in posts if item['id'] == post_id)
    blog_blocks = blog_body_blocks(post.get('body', ''))
    word_blocks = word_body_blocks(OUTPUT / docx_name)
    blog_tokens = tokens('\n'.join(value for _, value in blog_blocks))
    word_tokens = tokens('\n'.join(value for _, value in word_blocks))
    matcher = SequenceMatcher(a=blog_tokens, b=word_tokens, autojunk=False)
    diffs = []
    for tag, i1, i2, j1, j2 in matcher.get_opcodes():
        if tag != 'equal':
            diffs.append((tag, i1, i2, j1, j2))
    print(f'\nID: {post_id}')
    print(f'  blog_blocks={len(blog_blocks)} word_body_blocks={len(word_blocks)} blog_tokens={len(blog_tokens)} word_tokens={len(word_tokens)} differences={len(diffs)}')
    for tag, i1, i2, j1, j2 in diffs:
        print(f'  {tag} blog[{i1}:{i2}] word[{j1}:{j2}]')
        if i1 != i2:
            print('    BLOG', show_tokens(blog_tokens[i1:i2]))
        if j1 != j2:
            print('    WORD', show_tokens(word_tokens[j1:j2]))
