import json
import sys
from pathlib import Path

from compare_blog_word_semantic import blog_body_blocks, word_body_blocks, MAPPING, POSTS, OUTPUT

sys.stdout.reconfigure(encoding='utf-8')
posts = json.loads(POSTS.read_text(encoding='utf-8'))['posts']
for post_id in ('2026-08-22-proteins-amino-acids-book-notes', '2026-08-25-vitamins-book-notes'):
    post = next(x for x in posts if x['id'] == post_id)
    blog = blog_body_blocks(post['body'])
    word = word_body_blocks(OUTPUT / MAPPING[post_id])
    print(f'\nID {post_id}')
    print('BLOG first')
    for i, (kind, value) in enumerate(blog[:8]):
        print(i, kind, value)
    print('BLOG last')
    for i, (kind, value) in enumerate(blog[-12:], start=len(blog)-12):
        print(i, kind, value)
    print('WORD first')
    for i, (kind, value) in enumerate(word[:8]):
        print(i, kind, value)
    print('WORD last')
    for i, (kind, value) in enumerate(word[-12:], start=len(word)-12):
        print(i, kind, value)
