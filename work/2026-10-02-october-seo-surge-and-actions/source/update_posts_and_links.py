# -*- coding: utf-8 -*-
import json
import sys
import re

sys.stdout.reconfigure(encoding='utf-8')

posts_json_path = 'blog/posts.json'
with open(posts_json_path, 'r', encoding='utf-8') as f:
    data = json.load(f)

# 1. 微調 Ch 1 專文 Title 與 Excerpt
ch1_id = '2026-08-14-food-choices-human-health-guide'
new_ch1_title = '你每天吃對了嗎？食物選擇怎麼影響健康？營養師揭密「適足、均衡、適量、多樣」落實解方'
new_ch1_excerpt = '你每天吃對了嗎？食物選擇怎麼影響健康？凱特營養師以《Nutrition: Concepts & Controversies》第17版 第一章 為基礎，破解飲食盲點，用適足、均衡、適量、多樣四原則，帶你做出每天吃得到的高健康選擇。'

ch1_updated = False
for p in data['posts']:
    if p.get('id') == ch1_id:
        old_title = p.get('title')
        p['title'] = new_ch1_title
        p['excerpt'] = new_ch1_excerpt
        # 同時如果正文第一行是舊標題 h2，也同步替換
        p['body'] = re.sub(r'<h2>食物選擇怎麼影響健康？.*?</h2>', f'<h2>{new_ch1_title}</h2>', p.get('body', ''))
        ch1_updated = True
        print(f"Ch1 Title updated from:\n  '{old_title}'\nto:\n  '{new_ch1_title}'")
        break

if not ch1_updated:
    print("Warning: Ch1 post not found!")

# 2. 為全站 12 篇專文注入指向 class.html 的強效商業錨點卡片
class_card_html = (
    '<blockquote style="border-left:4px solid #0284c7;background:rgba(2,132,199,0.08);padding:14px 18px;margin:24px 0;border-radius:8px;">'
    '<p style="margin:0 0 6px 0;font-weight:700;color:#0369a1;">🎤 企業健康講座與專業培訓邀約</p>'
    '<p style="margin:0;">尋找生動幽默、兼具醫學實證與互動教具的專業講師？歡迎瀏覽：'
    '<a href="https://594katchang-source.github.io/class.html" style="font-weight:700;text-decoration:underline;">'
    '邀約企業健康講座 ｜ 檢視營養師授課實績與 12 大主題課程</a>，'
    '提供外商科技業、長照機構、公部門與福委會客製化 EAP 職場減壓、慢病預防與互動工作坊方案！</p>'
    '</blockquote>'
)

cards_injected = 0
for p in data['posts']:
    body = p.get('body', '')
    if 'class.html' not in body:
        p['body'] = body + '\n' + class_card_html
        cards_injected += 1
        print(f"Injected class.html link card into: {p.get('id')}")
    else:
        print(f"class.html already in: {p.get('id')}")

print(f"\nTotal posts updated with class.html card: {cards_injected}")

with open(posts_json_path, 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print("posts.json successfully saved.")
