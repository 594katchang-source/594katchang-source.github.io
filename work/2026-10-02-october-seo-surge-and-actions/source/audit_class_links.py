import json
import sys

sys.stdout.reconfigure(encoding='utf-8')

with open('blog/posts.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

print(f"Total posts: {len(data['posts'])}")
for p in data['posts']:
    body = p.get('body', '')
    has_class_link = 'class.html' in body
    print(f"- {p['id']}: has_class={has_class_link}, title={p['title'][:30]}...")
