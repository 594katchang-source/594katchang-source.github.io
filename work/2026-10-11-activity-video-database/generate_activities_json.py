# -*- coding: utf-8 -*-
import sys, os, re, json, urllib.parse
from datetime import datetime

sys.stdout.reconfigure(encoding='utf-8')

BASE_DIR = r"d:\@Codex\594katchang-source.github.io-main\work\2026-10-11-activity-video-database"
TEACH_ACT_DIR = r"d:\@Codex\594katchang-source.github.io-main\teach\activity-database"
os.makedirs(TEACH_ACT_DIR, exist_ok=True)
os.makedirs(os.path.join(BASE_DIR, "output"), exist_ok=True)

with open(os.path.join(BASE_DIR, "verified_raw_239.json"), "r", encoding="utf-8") as f:
    raw = json.load(f)

seniorart_items = raw['seniorart']
craft_items = raw['craft']
party_items = raw['party']
daycare_items = raw['daycare']
yt_map = raw['yt_map']

def classify_material_group(mat_text, is_game=False):
    groups = []
    t = mat_text
    if '免道具' in t or '不用任何工具' in t:
        groups.append('免道具')
    if any(k in t for k in ['紙', '色紙', '卡紙', '宣紙', '畫紙', '剪貼簿', '信封', '紅包袋', '紙盤', '紙杯', '紙藤', '紙繩', '紙板']):
        groups.append('紙材／色紙／卡紙')
    if any(k in t for k in ['顏料', '水彩', '畫筆', '彩色筆', '蠟筆', '代針筆', '粉彩', '墨汁', '毛筆', '手指膏', '亮光漆', '調色盤']):
        groups.append('畫具／顏料／彩筆')
    if any(k in t for k in ['布', '毛線', '針線', '棉線', '麻繩', '繡線', '襪子', '方巾', '毛巾', '圍裙', '鬆緊帶', '緞帶', '中國結', '皮繩', '釣魚線']):
        groups.append('布料／毛線／針線')
    if any(k in t for k in ['黏土', '陶土', '石膏', '麵粉', '麵團', '皂基', '蜂蠟', '大豆蠟', '填縫劑']):
        groups.append('黏土／陶土／石膏')
    if any(k in t for k in ['葉', '花', '松果', '種子', '豆', '苔', '竹', '稻草', '樹枝', '貝殼', '果核', '石頭', '鵝卵石', '柚子', '艾草', '薰衣草', '香料']):
        groups.append('花草／種子／自然物')
    if any(k in t for k in ['捲筒', '雜誌', '舊衣', '空玻璃', '寶特瓶', '瓶蓋', '報紙', '光碟', '牛奶盒', '罐頭', '蛋盒', '衣架', '鞋盒', '面紙盒']):
        groups.append('回收物（瓶罐／紙盒／報紙）')
    if any(k in t for k in ['珠', '拼豆', '毛根', '亮粉', '亮片', '活動眼睛', '鈕扣', '鑰匙圈', '磁鐵', 'LED', '鈴鐺']):
        groups.append('珠飾／毛根／配件')
    if any(k in t for k in ['題目卡', '便利貼', '任務單', '紙筆', '賓果卡', '情緒卡', '圖卡']):
        groups.append('紙筆／題目卡／便利貼')
    if any(k in t for k in ['氣球', '乒乓球', '球', '水桶', '塑膠杯', '杯子']):
        groups.append('氣球／球類／杯盤')
    if any(k in t for k in ['播放設備', '音樂', '手機']):
        groups.append('播放設備／音樂')
    if any(k in t for k in ['筷子', '湯匙', '吸管', '冰棒棍', '竹籤', '牙籤', '棉花棒', '海綿', '夾子', '晒衣夾', '叉子', '餅乾', '義大利麵', '骰子', '桌子', '椅子', '地墊', '包裹']):
        groups.append('日常小物（筷子／湯匙／面紙等）')
    if not groups:
        groups.append('日常小物（筷子／湯匙／面紙等）' if not is_game else '簡單道具')
    return list(dict.fromkeys(groups))

def parse_minutes(time_str):
    nums = [int(x) for x in re.findall(r'\d+', str(time_str))]
    if not nums:
        return 35
    if '兩次' in str(time_str):
        return 60
    return int(sum(nums) / len(nums))

def get_dur_bucket(mins):
    if mins <= 15:
        return '15分鐘以內'
    elif mins <= 30:
        return '16–30分鐘'
    elif mins <= 45:
        return '31–45分鐘'
    else:
        return '46分鐘以上'

all_activities = []

# ==============================================================================
# 1. 處理《教案靈感庫》(seniorart.html) - 40 筆 -> 歸入「藝術創作」
# ==============================================================================
for it in seniorart_items:
    k = f"seniorart_{it['id']}"
    yt_info = yt_map.get(k, {}).get('verified') or {}
    vid = yt_info.get('vid') or it['orig_vid']
    ch_name = yt_info.get('yt_author') or f"{it['region']}藝術教案頻道"

    mins = parse_minutes(it['time'])
    dur_bucket = get_dur_bucket(mins)

    lv_map = {'簡易': '★ 入門／簡易', '中等': '★★ 中等', '進階': '★★★ 挑戰／進階'}
    lv_label = lv_map.get(it['level'], '★ 入門／簡易')
    lv_num = 1 if it['level'] == '簡易' else (2 if it['level'] == '中等' else 3)

    subcats = [it['medium'], '美術']
    if it['medium'] == '繪畫':
        subcats.append('繪畫著色')
    if it['medium'] == '黏土':
        subcats.append('黏土陶藝')

    abilities = list(it['abilities'])
    norm_abilities = []
    for ab in abilities:
        norm_abilities.append(ab)
        if ab == '情緒紓壓':
            norm_abilities.append('情緒放鬆')
        if ab == '團體合作':
            norm_abilities.append('社交互動')
    if '創造表達' not in norm_abilities:
        norm_abilities.append('創造表達')
    if '認知刺激' not in norm_abilities:
        norm_abilities.append('認知刺激')
    norm_abilities = list(dict.fromkeys(norm_abilities))

    audiences = ['全年齡', '親子／兒童', '成人／職場團建', '樂齡／長輩', '坐姿完成']
    if '失智友善' in abilities:
        audiences.append('失智友善')
    if '團體合作' in abilities:
        audiences.append('小組／團體')
        group_mode = '個人／小組合作'
    else:
        audiences.append('個人完成')
        group_mode = '個人創作／團體皆可'
    if any(w in it['title'] + it['description'] for w in ['春', '夏', '秋', '冬', '聖誕', '節分', '七夕', '節慶']):
        audiences.append('節慶／季節活動')
    audiences = list(dict.fromkeys(audiences))

    mat_groups = classify_material_group(it['materials'])
    views_str = f"{it['views']/10000:.1f} 萬" if it['views'] >= 10000 else f"{it['views']:,}"

    # 根據原教案資訊建立完整 4 步帶領步驟與全齡擴充觀點
    steps_list = [
        f"1. 【暖身引導與感官觀察】先向學員展示「{it['title']}」完成範例或播放教學影片前段，帶領大家觸摸感受準備材料（{it['materials']}），並聊聊季節經驗或日常印象作為破冰。",
        f"2. 【分步示範與材料發放】{it['tips']} 帶領者將操作拆解為單一明確動作，示範一步、確認大家跟上後再進入下一步。",
        f"3. 【核心創作與自由配色】{it['description']} 鼓勵不同年齡層參與者自由挑選喜愛的色彩與排列位置，強調藝術創作沒有標準答案與對錯。",
        f"4. 【作品命名與正向欣賞】完成後邀請自願者為作品取名或拼成團體展示牆，彼此給予具體稱讚（如色彩搭配、線條活力），並拍照留念或帶回布置。"
    ]

    analysis = {
        "教案規格與屬性": f"地區：{it['region']} ｜ 媒材：{it['medium']} ｜ 難度：{it['level']} ｜ 建議時間：{it['time']} ｜ 影片觀看數：約 {views_str} 次",
        "核心訓練目的": f"{it['description']}\n💡 【全齡跨世代活動觀點】此藝術活動不僅適合社區樂齡與失智友善據點進行「{ '、'.join(it['abilities']) }」訓練，亦非常適合親子兒童美感教育（強化小肌肉控制與視覺空間）、青少年創意手作，以及成人／企業職場的正念藝術減壓工作坊，透過專注創作進入心流（Flow）狀態。",
        "主要訓練能力": "、".join(it['abilities'][:2]) if len(it['abilities']) >= 2 else (it['abilities'][0] if it['abilities'] else "手眼協調、創造表達"),
        "次要促進效益": "、".join(it['abilities'][2:] + ["美感創造表達", "跨世代成就感賦能"]),
        "活動類型与媒材": f"藝術創作・{it['medium']}（適合{group_mode}，建議時長 {it['time']}）",
        "準備材料與道具": f"{it['materials']}（建議桌面鋪設好清理之桌墊，並依參與者人數預先分盤）",
        "帶領步驟": "\n".join(steps_list),
        "引導口訣與延伸": f"💬 帶領者引導語：「創作沒有對錯，每一個線條和顏色都是獨一無二的風景！」\n📌 現場帶領核心提醒：{it['tips']}",
        "常見錯誤": f"{it['tips']} 避免一次將所有複雜工具堆滿桌面造成選擇焦慮，或過度要求作品「畫得像／剪得對齊」而削弱創作樂趣。",
        "安全注意事項": "請依個人能力調整手作材料與步驟；使用剪刀、竹籤或黏膠時請選用安全圓頭工具與無毒水洗顏料。全程採穩固坐姿進行，尊重每個人選擇跳過或降低難度的權利。",
        "初學者退階": f"【幼兒／失智／手部功能受限退階】{it['tips']} 可由帶領者預先完成裁切或底圖輪廓、改用大尺寸紙材與粗握柄工具，讓參與者專注於最療癒的貼合、點畫或配色步驟。",
        "進階變化": "【青少年／成人／高階能力進階變化】可挑戰自由構圖、結合異材質複合媒材拼貼，或轉化為小組限時共創大型主題壁畫，結合故事接龍分享創作理念。",
        "適合對象与權利": "適合全年齡（親子兒童美勞、青少年校園、成人正念紓壓、樂齡據點與失智友善）；每個人有選擇跳過、改用坐姿或降低難度的權利。"
    }

    all_activities.append({
        "uid": f"act_sa_{it['id']}",
        "id": vid,
        "source_db": "活動影片資料庫",
        "cat": "藝術創作",
        "subcats": list(dict.fromkeys(subcats)),
        "title": it['title'],
        "emoji": "🎨",
        "ch": ch_name,
        "url": it['url'],
        "yt_search_url": f"https://www.youtube.com/results?search_query={urllib.parse.quote(it['title'] + ' 手作 藝術 教學')}",
        "extra_search_url": "",
        "duration": it['time'],
        "duration_min": mins,
        "dur_bucket": dur_bucket,
        "level": lv_label,
        "level_num": lv_num,
        "group_mode": group_mode,
        "materials_short": it['materials'],
        "mat_groups": mat_groups,
        "abilities": norm_abilities,
        "audiences": audiences,
        "region": [it['region']],
        "lang": ["繁中" if it['region'] == "台灣" else ("日文" if it['region'] == "日本" else "英文")],
        "note": it['description'],
        "analysis": analysis
    })

# ==============================================================================
# 2. 處理手工教案 - 124 筆 -> 歸入「手工教案」
# ==============================================================================
LV_MAP_CRAFT = {1: '★ 入門／簡易', 2: '★★ 中等', 3: '★★★ 挑戰／進階'}
LV_WORD_CRAFT = {1: '★ 入門', 2: '★★ 中等', 3: '★★★ 挑戰'}

for it in craft_items:
    k = f"craft_{it['id']}"
    yt_info = yt_map.get(k, {}).get('verified') or {}
    vid = yt_info.get('vid') or 'VZmaJUH9sXA'
    ch_name = yt_info.get('yt_author') or '精選手工藝教學示範'

    mins = int(it['m'])
    dur_bucket = get_dur_bucket(mins)
    lv_label = LV_MAP_CRAFT.get(it['l'], '★★ 中等')
    lv_orig = LV_WORD_CRAFT.get(it['l'], '★★ 中等')

    subcats = [it['c'], '手作']
    tags = list(it['t'])
    abilities = []
    for tg in tags:
        abilities.append(tg)
        if tg == '情緒放鬆':
            abilities.append('情緒紓壓')
        if tg == '社交互動':
            abilities.append('團體合作')
    if '手眼協調' not in abilities and '精細動作' in abilities:
        abilities.append('手眼協調')
    abilities = list(dict.fromkeys(abilities))

    audiences = ['全年齡', '親子／兒童', '青少年／校園', '成人／職場團建', '樂齡／長輩']
    if '失智友善' in tags:
        audiences.append('失智友善')
    if '坐姿完成' in tags or True:
        audiences.append('坐姿完成')
    if '個人' in it['g']:
        audiences.append('個人完成')
    if '小組' in it['g']:
        audiences.append('小組／團體')
    if '可送禮' in tags:
        audiences.append('可送禮')
    if '節慶' in tags or it['c'] == '節慶民俗':
        audiences.append('節慶／季節活動')
    if '家庭互動' in tags:
        audiences.append('親子／兒童')
    audiences = list(dict.fromkeys(audiences))

    mat_str = "、".join(it['mat'])
    mat_groups = classify_material_group(mat_str + " " + it['c'])
    yt_search_url = f"https://www.youtube.com/results?search_query={urllib.parse.quote(it['yt'])}"
    watch_url = f"https://www.youtube.com/watch?v={vid}"

    steps_formatted = "\n".join([f"{idx}. {st}" for idx, st in enumerate(it['s'], 1)])

    analysis = {
        "教案規格與屬性": f"分類：{it['c']} ｜ 難度：{lv_orig} ｜ 建議時間：約 {mins} 分鐘 ｜ 進行形式：{it['g']} ｜ 標籤：{'、'.join(tags)}",
        "核心訓練目的": f"【職能治療與全齡觀點】{it['goal']}\n💡 【跨年齡層應用價值】除了支援銀髮據點與居家健康促進外，本教案亦適合「兒童親子手作（訓練精細抓握、順序計畫與專注力）」、「青少年社團／工藝課」與「成人手作療癒工作坊」，讓不同年齡層都能在動手做中獲得具體成品與成就感。",
        "主要訓練能力": "、".join(tags[:2]) if len(tags) >= 2 else (tags[0] if tags else "精細動作、創造表達"),
        "次要促進效益": "、".join(tags[2:]) if len(tags) > 2 else "雙手協調、專注力與作品成就感",
        "活動類型与媒材": f"手工教案・{it['c']}（{lv_orig}，形式：{it['g']}，約 {mins} 分鐘）",
        "準備材料與道具": "\n".join([f"• {m}" for m in it['mat']]),
        "帶領步驟": steps_formatted,
        "引導口訣與延伸": f"💬 跨世代暖身引導：開場可先展示完成品，邀請兒童／成人／長輩分享與「{it['n']}」相關的生活經驗或喜好配色。\n🔍 影片搜尋關鍵字：「{it['yt']}」（可點擊下方按鈕直接觀看代表教學影片，或搜尋更多慢速步驟示範）。",
        "常見錯誤": "步驟推進過快、材料未事先分裝導致現場混亂，或參與者因手部精細度差異產生挫折感。建議每步等全員完成再前進，並強調手作重在過程體驗。",
        "安全注意事項": "請依個人能力調整手作材料與步驟。若涉及剪刀、珠針、鐵絲或加熱工具（如熱熔膠、熨斗、隔水加熱），務必由帶領者或成人協助操作，並確保桌面穩固、光線充足。",
        "初學者退階": f"【調整與簡化（幼兒／失能／失智／手部功能較弱）】{it['ad']}",
        "進階變化": "【中高階／青少年／成人巧手進階變化】可讓參與者自行設計紙型與配色結構、增加複合媒材裝飾細節，或結合「一人負責一道工序」的團隊流水線合作與禮品包裝設計。",
        "適合對象与權利": f"適合全年齡（親子共學、校園社團、成人手作紓壓、社區樂齡與失智據點；建議形式：{it['g']}）。互動時避免強迫分享，每個人有選擇跳過、改用坐姿或降低難度的權利。"
    }

    all_activities.append({
        "uid": f"act_cr_{it['id']}",
        "id": vid,
        "source_db": "活動影片資料庫",
        "cat": "手工教案",
        "subcats": list(dict.fromkeys(subcats)),
        "title": f"{it['e']} {it['n']}",
        "emoji": it['e'],
        "ch": ch_name,
        "url": watch_url,
        "yt_search_url": yt_search_url,
        "extra_search_url": "",
        "duration": f"約 {mins} 分鐘",
        "duration_min": mins,
        "dur_bucket": dur_bucket,
        "level": lv_label,
        "level_num": int(it['l']),
        "group_mode": it['g'],
        "materials_short": mat_str,
        "mat_groups": mat_groups,
        "abilities": abilities,
        "audiences": audiences,
        "region": ["台灣", "跨文化通用"],
        "lang": ["繁中"],
        "note": it['goal'],
        "analysis": analysis
    })

# ==============================================================================
# 3. 處理《派對遊戲資料庫》(party-games.html) - 45 款 -> 歸入「團康活動」
# ==============================================================================
PARTY_EMOJI_MAP = {
    '破冰認識': '🤝',
    '猜題表演': '🎭',
    '反應挑戰': '⚡',
    '音樂舞動': '🎵',
    '合作挑戰': '🧩',
    '戶外任務': '🏃',
    '一分鐘挑戰': '⏱️'
}

PARTY_ABILITIES_MAP = {
    '破冰認識': ['社交互動', '團體合作', '情緒放鬆', '創造表達'],
    '猜題表演': ['認知刺激', '創造表達', '社交互動', '專注力'],
    '反應挑戰': ['反應訓練', '專注力', '手眼協調', '認知刺激'],
    '音樂舞動': ['感官刺激', '情緒放鬆', '社交互動', '反應訓練'],
    '合作挑戰': ['團體合作', '社交互動', '手眼協調', '認知刺激'],
    '戶外任務': ['團體合作', '肌力', '平衡', '社交互動'],
    '一分鐘挑戰': ['精細動作', '手眼協調', '反應訓練', '專注力']
}

for it in party_items:
    k = f"party_{it['id']}"
    yt_info = yt_map.get(k, {}).get('verified') or {}
    vid = yt_info.get('vid') or 's3R_0C9wvMw'
    ch_name = yt_info.get('yt_author') or '團康派對遊戲示範'

    mins = parse_minutes(it['time'])
    dur_bucket = get_dur_bucket(mins)

    # 依遊戲特性設定難度
    lv_num = 1 if it['category'] in ['破冰認識', '音樂舞動'] or '免道具' in it['material'] else 2
    lv_label = LV_MAP_CRAFT[lv_num]
    em = PARTY_EMOJI_MAP.get(it['category'], '🎲')

    subcats = [it['category'], '團康遊戲', '互動遊戲']
    if it['category'] == '破冰認識':
        subcats.append('破冰遊戲')
    elif it['category'] == '猜題表演':
        subcats.append('懷舊問答')
    elif it['category'] == '反應挑戰':
        subcats.append('反應遊戲')
    elif it['category'] == '音樂舞動':
        subcats.extend(['音樂律動', '歌唱'])
    elif it['category'] == '合作挑戰':
        subcats.append('團體活動')
    elif it['category'] == '一分鐘挑戰':
        subcats.append('器材遊戲')

    abilities = list(PARTY_ABILITIES_MAP.get(it['category'], ['社交互動', '認知刺激', '反應訓練']))
    audiences = ['全年齡', '小組／團體']
    orig_aud = it['audience']
    if '親子' in orig_aud or '全年齡' in orig_aud:
        audiences.append('親子／兒童')
    if '青少年' in orig_aud or '全年齡' in orig_aud:
        audiences.append('青少年／校園')
    if '成人' in orig_aud or '全年齡' in orig_aud:
        audiences.append('成人／職場團建')
    if '樂齡' in orig_aud or '全年齡' in orig_aud:
        audiences.append('樂齡／長輩')
    if it['category'] != '戶外任務':
        audiences.append('坐姿完成')
    audiences = list(dict.fromkeys(audiences))

    mat_groups = classify_material_group(it['material'], is_game=True)
    yt_search_url = f"https://www.youtube.com/results?search_query={urllib.parse.quote(it['title'] + ' party game how to play 遊戲 玩法')}"
    google_search_url = f"https://www.google.com/search?q={urllib.parse.quote(it['title'] + ' 遊戲 玩法 規則')}"
    watch_url = f"https://www.youtube.com/watch?v={vid}"

    steps_formatted = "\n".join([f"{idx}. {st}" for idx, st in enumerate(it['steps'], 1)])

    analysis = {
        "教案規格與屬性": f"類型：{it['category']} ｜ 👥 建議人數：{it['players']} ｜ ⏱ 時間：{it['time']} ｜ 🎒 道具：{it['material']} ｜ 🎯 適合對象：{it['audience']}",
        "核心訓練目的": f"【玩法核心說明】{it['note']}\n💡 【全齡跨世代團康觀點】本活動兼具破冰暖場、注意力集中、即時反應與團隊正向溝通效益。無論是「校園班級經營／迎新營隊」、「企業 Team Building／會議提神」、「家庭派對聚會」或「社區樂齡據點腦力團康」，皆可透過節奏與題目微調讓全場快速融入！",
        "主要訓練能力": "、".join(abilities[:2]),
        "次要促進效益": "、".join(abilities[2:] + ["破冰暖場", "正向社交連結"]),
        "活動類型与媒材": f"團康活動・{it['category']}（👥 {it['players']}，⏱ {it['time']}，對象：{it['audience']}）",
        "準備材料與道具": f"🎒 所需道具：{it['material']}（建議事先確認活動空間動線順暢、座椅穩固無尖角）",
        "帶領步驟": steps_formatted,
        "引導口訣與延伸": f"💬 帶領者開場口訣：「我們今天重在合作與歡笑，不採殘酷淘汰制，隨時可以互相提示支援！」\n🔍 點擊下方按鈕可觀看示範影片，或點選「延伸玩法規則搜尋」查看更多題庫與變化版。",
        "常見錯誤": f"{it['tip']} 帶領時避免規則講解過長，建議直接由帶領者示範一回合最快進入狀況。",
        "安全注意事項": "請依個人身體狀況及跌倒風險調整體能活動。互動時避免強迫分享、淘汰羞辱或危險肢體接觸，每個人有選擇跳過、改用坐姿或降低難度的權利。",
        "初學者退階": "【幼兒／長輩／行動不便或慢熟族群退階】可改為「全坐姿圍圈／桌面版」進行、放慢口令節奏、改用舉牌／手勢代替奔跑移動，並採「雙人組隊互相提示、零淘汰制」降低心理壓力。",
        "進階變化": "【青少年／企業成人／高階反應進階變化】可加入計時挑戰、增加「雙重任務（如邊做動作邊反向喊口令／雙倍道具）」或分組積分賽，激發團隊策略討論與高能量互動。",
        "適合對象与權利": f"適合：{it['audience']}（跨世代通用：親子聚會、校園青少年、企業團建、社區樂齡；建議人數：{it['players']}）。每個人皆有選擇跳過、改用坐姿或降低難度的權利。"
    }

    all_activities.append({
        "uid": f"act_pg_{it['id']}",
        "id": vid,
        "source_db": "活動影片資料庫",
        "cat": "團康活動",
        "subcats": list(dict.fromkeys(subcats)),
        "title": f"{em} {it['title']}",
        "emoji": em,
        "ch": ch_name,
        "url": watch_url,
        "yt_search_url": yt_search_url,
        "extra_search_url": google_search_url,
        "duration": it['time'],
        "duration_min": mins,
        "dur_bucket": dur_bucket,
        "level": lv_label,
        "level_num": lv_num,
        "group_mode": f"團體 ({it['players']})",
        "materials_short": it['material'],
        "mat_groups": mat_groups,
        "abilities": abilities,
        "audiences": audiences,
        "region": ["台灣", "跨文化通用"],
        "lang": ["繁中"],
        "note": it['note'],
        "analysis": analysis
    })

# ==============================================================================
# 4. 處理精選活動頻道 - 30 筆 -> 打散至三大分類
# ==============================================================================
# 分類映射：
# - we01 (Art for Alzheimers Care) -> 藝術創作 (1筆)
# - tw01, tw09, jp05, we02, we03, we09, we10 -> 手工教案 (7筆)
# - 其餘 22 筆 -> 團康活動 (22筆)
DAYCARE_HANDCRAFT_IDS = {'tw01', 'tw09', 'jp05', 'we02', 'we03', 'we09', 'we10'}

for it in daycare_items:
    k = f"daycare_{it['id']}"
    yt_info = yt_map.get(k, {}).get('verified') or {}
    vid = yt_info.get('vid') or 's3R_0C9wvMw'
    sample_yt_title = yt_info.get('yt_title') or f"{it['name']} 精選活動示範"

    if it['id'] == 'we01':
        main_cat = '藝術創作'
        em = '🎨'
    elif it['id'] in DAYCARE_HANDCRAFT_IDS:
        main_cat = '手工教案'
        em = '🧶'
    else:
        main_cat = '團康活動'
        em = '🎬'

    orig_cats = list(it['categories'])
    subcats = list(orig_cats) + ['日照實務']
    if main_cat == '藝術創作' and '繪畫著色' not in subcats:
        subcats.append('繪畫著色')
    if main_cat == '手工教案' and '綜合媒材' not in subcats:
        subcats.append('綜合媒材')

    abilities = []
    for c_tag in orig_cats:
        if c_tag in ['認知訓練', '腦力體操', '腦力訓練', '腦力遊戲', '懷舊問答']:
            abilities.append('認知刺激')
        if c_tag in ['手作', '美術', '手指操', '節慶手作']:
            abilities.extend(['精細動作', '手眼協調'])
        if c_tag in ['團康遊戲', '互動遊戲', '破冰遊戲', '團體運動', '團體活動']:
            abilities.extend(['社交互動', '團體合作'])
        if c_tag in ['感官刺激', '音樂律動', '歌唱', '歌唱體操']:
            abilities.extend(['感官刺激', '情緒放鬆'])
        if c_tag in ['反應訓練', '反應遊戲', '器材遊戲', '棒球活動']:
            abilities.extend(['反應訓練', '手眼協調'])
        if c_tag in ['肌力', '樂齡運動', '體操', '椅子體操', '椅子運動', '復健體操', '低衝擊運動', '有氧', '瑜伽', '步行']:
            abilities.append('肌力')
        if c_tag in ['平衡', '協調']:
            abilities.append('平衡')
        if c_tag in ['失智預防', '失智活動', '介護預防']:
            abilities.append('失智預防')
        if c_tag in ['口腔運動']:
            abilities.append('呼吸訓練')
    if not abilities:
        abilities = ['認知刺激', '社交互動', '手眼協調']
    abilities = list(dict.fromkeys(abilities))

    audiences = ['全年齡', '樂齡／長輩', '失智友善', '坐姿完成', '小組／團體']
    if main_cat in ['藝術創作', '手工教案']:
        audiences.extend(['個人完成', '親子／兒童', '成人／職場團建'])
    else:
        audiences.extend(['親子／兒童', '青少年／校園', '成人／職場團建'])
    if any(w in orig_cats for w in ['節慶活動', '季節活動', '節慶手作']):
        audiences.append('節慶／季節活動')
    audiences = list(dict.fromkeys(audiences))

    mat_groups = ['紙筆／題目卡／便利貼', '氣球／球類／杯盤', '日常小物（筷子／湯匙／面紙等）']
    if main_cat in ['藝術創作', '手工教案']:
        mat_groups = ['紙材／色紙／卡紙', '畫具／顏料／彩筆', '回收物（瓶罐／紙盒／報紙）']
    if any(w in orig_cats for w in ['椅子體操', '椅子運動', '手指操', '腦力體操', '歌唱']):
        mat_groups.insert(0, '免道具')

    watch_url = f"https://www.youtube.com/watch?v={vid}"

    steps_daycare = [
        f"1. 【課前選片與教材準備】開啟「{it['name']}」代表示範影片或推薦清單（{it['note']}），觀察影片中的座位配置、低成本教具與帶領節奏。",
        f"2. 【暖身破冰與規則示範】先以 3–5 分鐘手指操、節奏拍手或主題問答吸引注意力；將活動規則簡化為 1–2 個直覺動作，由帶領者親自示範一次。",
        f"3. 【主活動帶領與雙向互動】{it['description']} 帶領過程中搭配正向鼓勵，依現場反應自由調整速度、回合數或改編為分組合作挑戰。",
        f"4. 【緩和收操與經驗分享】活動尾聲進行深呼吸放鬆或作品成果展示，邀請參與者分享今天最有成就感或最好玩的瞬間。"
    ]

    analysis = {
        "教案規格與屬性": f"國家／地區：{it['region']}・{it['country']} ｜ 語言：{it['language']} ｜ 熱門度：{it['popularity']} ｜ 活動分類：{'、'.join(orig_cats)}",
        "核心訓練目的": f"【頻道核心特色】{it['description']}\n💡 【全齡跨世代改編觀點】本資源收錄高密度實務示範影片（代表影片：{sample_yt_title}），不僅是日照中心與社區據點的備課寶庫，其中的反應遊戲、桌面破冰、節奏體操與創意手作，亦可直接改編用於「親子家庭日」、「學校班級團康」與「職場久坐醒腦健康操」。",
        "主要訓練能力": "、".join(orig_cats[:2]),
        "次要促進效益": "、".join(orig_cats[2:] + abilities[:2]),
        "活動類型与媒材": f"{main_cat}・{'／'.join(orig_cats)}（語言：{it['language']}，地區：{it['country']}）",
        "準備材料與道具": "依示範影片選用日常低成本素材（如紙杯、乒乓球、色紙、毛巾、穩固無輪座椅或徒手免道具即可進行）",
        "帶領步驟": "\n".join(steps_daycare),
        "引導口訣與延伸": f"📌 【活動帶領備註與推薦清單】{it['note']}\n🌐 頻道完整首頁：{it['url']}（日本與歐美外語影片可開啟 YouTube 自動字幕與中文翻譯輔助備課）。",
        "常見錯誤": "直接照搬高難度動作而未先暖身，或外語影片直接播放未加上中文口令引導。建議帶領者先看懂玩法結構，再用現場熟悉的語言與音樂帶動。",
        "安全注意事項": "請依個人身體狀況及跌倒風險調整體能活動。請依個人能力調整手作材料與步驟。互動時避免強迫分享、淘汰羞辱或危險肢體接觸，每個人有選擇跳過、改用坐姿或降低難度的權利。",
        "初學者退階": "【初學者／失智／體能受限退階】全程採穩固坐姿操作、將播放速度調慢至 0.75 倍或由帶領者慢速分解口令，減少干擾物，只保留最核心的單一動作或手作步驟。",
        "進階變化": "【青少年／成人／高階能力進階變化】加快節奏、結合雙重任務（邊做動作邊算數／猜謎／唱副歌），或將個人練習改編為分組接力賽與創意規則改造。",
        "適合對象与權利": "適合全年齡活動帶領者、社區據點、日照中心、親子與學校團體（每個人有選擇跳過、改用坐姿或降低難度的權利）。"
    }

    all_activities.append({
        "uid": f"act_dc_{it['id']}",
        "id": vid,
        "source_db": "活動影片資料庫",
        "cat": main_cat,
        "subcats": list(dict.fromkeys(subcats)),
        "title": f"{em} {it['name']}（{'・'.join(orig_cats[:2])}）",
        "emoji": em,
        "ch": f"{it['name']} ({it['country']})",
        "url": watch_url,
        "yt_search_url": it['url'],
        "extra_search_url": it['url'],
        "duration": "15–30 分鐘",
        "duration_min": 25,
        "dur_bucket": "16–30分鐘",
        "level": "★ 入門／簡易",
        "level_num": 1,
        "group_mode": "個人／團體皆可",
        "materials_short": "日常簡易教具／免道具",
        "mat_groups": mat_groups,
        "abilities": abilities,
        "audiences": audiences,
        "region": [it['region']],
        "lang": [it['language']],
        "note": f"{it['description']}（{it['note']}）",
        "analysis": analysis
    })

# Verify category counts
from collections import Counter
cat_counts = Counter(x['cat'] for x in all_activities)
print("Total activities:", len(all_activities))
print("Category breakdown:", dict(cat_counts))

output_payload = {
    "updatedAt": datetime.now().strftime("%Y-%m-%d"),
    "totalActivities": len(all_activities),
    "categoryCounts": dict(cat_counts),
    "activities": all_activities
}

with open(os.path.join(TEACH_ACT_DIR, "activities_full.json"), "w", encoding="utf-8") as f:
    json.dump(output_payload, f, ensure_ascii=False, indent=2)

with open(os.path.join(BASE_DIR, "output", "activities_full.json"), "w", encoding="utf-8") as f:
    json.dump(output_payload, f, ensure_ascii=False, indent=2)

print("Saved activities_full.json successfully!")
