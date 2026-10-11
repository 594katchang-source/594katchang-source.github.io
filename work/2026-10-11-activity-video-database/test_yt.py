# -*- coding: utf-8 -*-
import sys, urllib.request, urllib.parse, re, json
sys.stdout.reconfigure(encoding='utf-8')

def search_yt_video(query):
    url = 'https://www.youtube.com/results?search_query=' + urllib.parse.quote(query)
    req = urllib.request.Request(url, headers={
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
        'Accept-Language': 'zh-TW,zh;q=0.9,en;q=0.8'
    })
    html = urllib.request.urlopen(req, timeout=10).read().decode('utf-8', errors='ignore')
    vids = re.findall(r'"videoId":"([a-zA-Z0-9_-]{11})"', html)
    seen = []
    for v in vids:
        if v not in seen:
            seen.append(v)
    return seen[:5]

def get_channel_videos(ch_url):
    target = ch_url.rstrip('/') + '/videos'
    req = urllib.request.Request(target, headers={
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
        'Accept-Language': 'zh-TW,zh;q=0.9,en;q=0.8'
    })
    html = urllib.request.urlopen(req, timeout=10).read().decode('utf-8', errors='ignore')
    vids = re.findall(r'"videoId":"([a-zA-Z0-9_-]{11})"', html)
    seen = []
    for v in vids:
        if v not in seen:
            seen.append(v)
    return seen[:5]

def verify_oembed(vid):
    url = f'https://www.youtube.com/oembed?url=https://www.youtube.com/watch?v={vid}&format=json'
    req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    with urllib.request.urlopen(req, timeout=8) as r:
        data = json.loads(r.read().decode('utf-8'))
        return data.get('title'), data.get('author_name')

vids = search_yt_video('紙鶴 摺法 教學')
print('Search vids:', vids)
if vids:
    print('oEmbed:', verify_oembed(vids[0]))

ch_vids = get_channel_videos('https://www.youtube.com/@ylhuang2555')
print('Channel vids:', ch_vids)
if ch_vids:
    print('Channel oEmbed:', verify_oembed(ch_vids[0]))
