# -*- coding: utf-8 -*-
import sys, os, re, json, urllib.request, urllib.parse
from concurrent.futures import ThreadPoolExecutor, as_completed

sys.stdout.reconfigure(encoding='utf-8')

BASE_DIR = r"d:\@Codex\594katchang-source.github.io-main\work\2026-10-11-activity-video-database"
SRC_DIR = os.path.join(BASE_DIR, "source")

HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36',
    'Accept-Language': 'zh-TW,zh;q=0.9,en-US;q=0.8,en;q=0.7'
}

def verify_oembed(vid):
    if not vid:
        return None
    url = f'https://www.youtube.com/oembed?url=https://www.youtube.com/watch?v={vid}&format=json'
    try:
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        with urllib.request.urlopen(req, timeout=8) as r:
            data = json.loads(r.read().decode('utf-8'))
            return {
                'vid': vid,
                'yt_title': data.get('title', ''),
                'yt_author': data.get('author_name', ''),
                'yt_author_url': data.get('author_url', '')
            }
    except Exception:
        return None

def search_yt_candidates(query):
    url = 'https://www.youtube.com/results?search_query=' + urllib.parse.quote(query)
    try:
        req = urllib.request.Request(url, headers=HEADERS)
        html = urllib.request.urlopen(req, timeout=10).read().decode('utf-8', errors='ignore')
        vids = re.findall(r'"videoId":"([a-zA-Z0-9_-]{11})"', html)
        seen = []
        for v in vids:
            if v not in seen:
                seen.append(v)
        return seen[:8]
    except Exception:
        return []

def get_channel_candidates(ch_url, fallback_query):
    for suffix in ['/videos', '/shorts', '']:
        target = ch_url.rstrip('/') + suffix
        try:
            req = urllib.request.Request(target, headers=HEADERS)
            html = urllib.request.urlopen(req, timeout=10).read().decode('utf-8', errors='ignore')
            vids = re.findall(r'"videoId":"([a-zA-Z0-9_-]{11})"', html)
            seen = []
            for v in vids:
                if v not in seen:
                    seen.append(v)
            if seen:
                return seen[:8]
        except Exception:
            pass
    return search_yt_candidates(fallback_query)

# 1. Parse seniorart.html (40 items)
with open(os.path.join(SRC_DIR, "seniorart.html"), "r", encoding="utf-8") as f:
    t_seniorart = f.read()

seniorart_items = []
m_lessons = re.search(r"const lessons = \[(.*?)\];\s*const state", t_seniorart, re.S)
for line in m_lessons.group(1).splitlines():
    line = line.strip().rstrip(',')
    if not line.startswith('{id:'):
        continue
    # Convert JS object literal to JSON
    j_str = re.sub(r'(\b(?:id|title|region|medium|abilities|level|time|views|url|description|materials|tips)\b):', r'"\1":', line)
    obj = json.loads(j_str)
    m_v = re.search(r'(?:v=|shorts/)([\w-]{11})', obj['url'])
    obj['orig_vid'] = m_v.group(1) if m_v else ''
    seniorart_items.append(obj)

print(f"Parsed seniorart: {len(seniorart_items)} items")

# 2. Parse art-senior-database.html (124 items)
with open(os.path.join(SRC_DIR, "art-senior-database.html"), "r", encoding="utf-8") as f:
    t_crafts = f.read()

craft_items = []
m_crafts = re.search(r"const CRAFTS = \[(.*?)\];\s*const CAT_ORDER", t_crafts, re.S)
for line in m_crafts.group(1).splitlines():
    line = line.strip().rstrip(',')
    if not line.startswith('{id:'):
        continue
    j_str = re.sub(r'(\b(?:id|n|c|e|t|l|m|g|mat|s|goal|ad|yt)\b):', r'"\1":', line)
    obj = json.loads(j_str)
    craft_items.append(obj)

print(f"Parsed art-senior-database: {len(craft_items)} items")

# 3. Parse party-games.html (45 items)
with open(os.path.join(SRC_DIR, "party-games.html"), "r", encoding="utf-8") as f:
    t_party = f.read()

party_items = []
m_games = re.search(r"const games=\[(.*?)\]\.map", t_party, re.S)
for idx, line in enumerate(m_games.group(1).splitlines(), 1):
    line = line.strip().rstrip(',')
    if not line.startswith('['):
        continue
    arr = eval(line)
    party_items.append({
        'id': idx,
        'title': arr[0],
        'category': arr[1],
        'audience': arr[2],
        'material': arr[3],
        'players': arr[4],
        'time': arr[5],
        'note': arr[6],
        'steps': arr[7].split('|'),
        'tip': arr[8]
    })

print(f"Parsed party-games: {len(party_items)} items")

# 4. Parse daycare-activity-library.html (30 items)
with open(os.path.join(SRC_DIR, "daycare-activity-library.html"), "r", encoding="utf-8") as f:
    t_daycare = f.read()

daycare_items = []
m_seed = re.search(r"const seed = \[(.*?)\];\s*const KEY", t_daycare, re.S)
for line in m_seed.group(1).splitlines():
    line = line.strip().rstrip(',')
    if not line.startswith('{id:'):
        continue
    j_str = re.sub(r'(\b(?:id|region|country|name|url|language|directness|popularity|categories|description|note)\b):', r'"\1":', line)
    obj = json.loads(j_str)
    daycare_items.append(obj)

print(f"Parsed daycare-activity-library: {len(daycare_items)} items")

# Resolve & verify oEmbed for all items concurrently
tasks = []
for it in seniorart_items:
    tasks.append(('seniorart', it['id'], it['orig_vid'], f"{it['title']} 手作 藝術 教學", None))

for it in craft_items:
    tasks.append(('craft', it['id'], None, f"{it['yt']} DIY 教學", None))

for it in party_items:
    tasks.append(('party', it['id'], None, f"{it['title']} 團康 遊戲 玩法 party game", None))

for it in daycare_items:
    tasks.append(('daycare', it['id'], None, f"{it['name']} 樂齡 日照 活動", it['url']))

def worker(task):
    src, item_id, orig_vid, query, ch_url = task
    if orig_vid:
        res = verify_oembed(orig_vid)
        if res:
            return (src, item_id, res, [orig_vid])
    if ch_url:
        cands = get_channel_candidates(ch_url, query)
    else:
        cands = search_yt_candidates(query)
    for vid in cands:
        res = verify_oembed(vid)
        if res:
            return (src, item_id, res, cands)
    # Fallback broader query
    cands2 = search_yt_candidates(query.split()[0] + " 教學")
    for vid in cands2:
        res = verify_oembed(vid)
        if res:
            return (src, item_id, res, cands2)
    return (src, item_id, None, [])

results_map = {}
with ThreadPoolExecutor(max_workers=14) as ex:
    futs = [ex.submit(worker, t) for t in tasks]
    done_cnt = 0
    for fut in as_completed(futs):
        src, item_id, res, cands = fut.result()
        results_map[f"{src}_{item_id}"] = {'verified': res, 'candidates': cands}
        done_cnt += 1
        if done_cnt % 25 == 0 or done_cnt == len(tasks):
            print(f"Progress: {done_cnt}/{len(tasks)} verified")

# Ensure uniqueness of videoId across all 239 items if possible
used_vids = set()
# First lock in seniorart original vids
for it in seniorart_items:
    k = f"seniorart_{it['id']}"
    v = results_map[k]['verified']
    if v:
        used_vids.add(v['vid'])

for src, items_list in [('craft', craft_items), ('party', party_items), ('daycare', daycare_items)]:
    for it in items_list:
        k = f"{src}_{it['id']}"
        info = results_map[k]
        v = info['verified']
        if v and v['vid'] not in used_vids:
            used_vids.add(v['vid'])
        else:
            # Try next candidate in info['candidates']
            found_alt = None
            for cand_vid in info['candidates']:
                if cand_vid not in used_vids:
                    alt_res = verify_oembed(cand_vid)
                    if alt_res:
                        found_alt = alt_res
                        used_vids.add(cand_vid)
                        break
            if found_alt:
                results_map[k]['verified'] = found_alt
            elif v:
                used_vids.add(v['vid'])

missing = [k for k, v in results_map.items() if not v['verified']]
print("Missing oEmbed count:", len(missing))

out_data = {
    'seniorart': seniorart_items,
    'craft': craft_items,
    'party': party_items,
    'daycare': daycare_items,
    'yt_map': results_map
}
with open(os.path.join(BASE_DIR, "verified_raw_239.json"), "w", encoding="utf-8") as f:
    json.dump(out_data, f, ensure_ascii=False, indent=2)
print("Saved verified_raw_239.json successfully!")
