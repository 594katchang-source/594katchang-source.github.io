import json
import re
import sys
from pathlib import Path

from docx import Document

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


def get_value(values, label, prefix=False):
    for i, value in enumerate(values):
        if value.strip() == label and i + 1 < len(values):
            next_value = values[i + 1]
            if prefix and next_value.startswith(prefix):
                return next_value[len(prefix):].strip()
            return next_value.strip()
    return ''


posts = json.loads(POSTS.read_text(encoding='utf-8'))['posts']
for post_id, filename in MAPPING.items():
    post = next(x for x in posts if x['id'] == post_id)
    values = [p.text.strip() for p in Document(OUTPUT / filename).paragraphs]
    title = get_value(values, 'SEO 標題')
    excerpt = get_value(values, '文章摘要與適合搜尋結果顯示的開場', '文章摘要：')
    keywords = get_value(values, '目標搜尋字詞、相關搜尋字詞與搜尋意圖', '目標搜尋字詞：')
    category = next((v[len('分類：'):].strip() for v in values if v.startswith('分類：')), '')
    date = next((v[len('建議更新日期：'):].strip() for v in values if v.startswith('建議更新日期：')), '')
    print(f'\n{post_id}')
    for label, remote, local in [
        ('title', post.get('title', ''), title),
        ('excerpt', post.get('excerpt', ''), excerpt),
        ('keywords', '、'.join(post.get('keywords', [])), keywords),
        ('category', post.get('category', ''), category),
        ('date', post.get('date', ''), date),
    ]:
        print(f'  {label}: same={remote == local}')
        if remote != local:
            print(f'    remote={remote}')
            print(f'    local ={local}')
