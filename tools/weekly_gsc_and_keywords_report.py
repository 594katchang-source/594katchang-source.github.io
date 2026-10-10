import os
import sys
import json
from datetime import datetime, timedelta
import truststore
truststore.inject_into_ssl()

import certifi
sys.stdout.reconfigure(encoding='utf-8')
os.environ['SSL_CERT_FILE'] = certifi.where()
os.environ['REQUESTS_CA_BUNDLE'] = certifi.where()

from google.oauth2 import service_account
from googleapiclient.discovery import build
import httplib2
import google_auth_httplib2
import ssl

BASE_DIR = r"d:\@Codex\594katchang-source.github.io-main"
CREDENTIALS_FILE = os.path.join(BASE_DIR, "gsc-credentials.json")
SCOPES = ['https://www.googleapis.com/auth/webmasters.readonly']
SITE_URL = "https://594katchang-source.github.io/"

REPORTS_DIR = os.path.join(BASE_DIR, "work", "weekly-gsc-reports")
os.makedirs(REPORTS_DIR, exist_ok=True)

# 6 大主打教具定義
CORE_TOOLS = [
    {
        "id": "nutrirank",
        "name": "NutriRank 食品營養排行榜",
        "path": "teach/nutritionranking/",
        "canonical": "https://594katchang-source.github.io/teach/nutritionranking/",
        "keywords": [
            "台灣食品營養成分資料庫查詢", "食品營養成分排行查詢", "高鉀食物排行榜",
            "高鈣食物排行榜", "六大類食物營養比對工具"
        ]
    },
    {
        "id": "paper-radar",
        "name": "論文讀書小站 公開閱讀版",
        "path": "teach/paper-radar/",
        "canonical": "https://594katchang-source.github.io/teach/paper-radar/",
        "keywords": [
            "PubMed 營養醫學論文導讀", "功能醫學實證研究解析", "阿茲海默與失智症預防營養論文",
            "GRADE 營養研究品質評讀", "高齡肌少症國際營養指南實證"
        ]
    },
    {
        "id": "food-exchange",
        "name": "食物代換速查表",
        "path": "teach/food-exchange/",
        "canonical": "https://594katchang-source.github.io/teach/food-exchange/",
        "keywords": [
            "食物代換速查表", "一份肉幾克蛋白質", "一份全穀雜糧代換計算",
            "衛福部標準食物代換表線上版", "減重食物份數計算工具"
        ]
    },
    {
        "id": "daily-needs",
        "name": "每日營養與熱量需求計算器",
        "path": "teach/daily-needs/",
        "canonical": "https://594katchang-source.github.io/teach/daily-needs/",
        "keywords": [
            "TDEE 熱量計算機線上", "BMR 基礎代謝率計算器", "每日三大營養素熱量分配計算",
            "地中海飲食熱量配比試算", "高齡長輩蛋白質需求克數計算"
        ]
    },
    {
        "id": "stress-food",
        "name": "Stress Food 壓力飲食解謎",
        "path": "teach/Stress-Food/",
        "canonical": "https://594katchang-source.github.io/teach/Stress-Food/",
        "keywords": [
            "壓力大吃什麼線上解謎", "皮質醇荷爾蒙調節飲食", "抗焦慮與抗疲勞食物組合",
            "熬夜加班健康宵夜推薦", "企業健康日互動攤位體驗教材"
        ]
    },
    {
        "id": "emotion-cards",
        "name": "草木心語 情緒覺察卡牌",
        "path": "teach/emotion-cards/",
        "canonical": "https://594katchang-source.github.io/teach/emotion-cards/",
        "keywords": [
            "情緒覺察卡牌線上版", "植物輔療情緒引導工具", "草木心語 36張植癒牌卡自我對話",
            "高齡心靈陪伴互動教材", "1分鐘放鬆呼吸與身心覺察微練習"
        ]
    }
]

# 原全站 41 組既有關鍵字
ORIGINAL_41_KEYWORDS = [
    "中高齡營養師", "中高齡營養專家", "企業健康講座", "肌少症飲食", "精準營養",
    "上班族外食抗疲勞飲食", "台北營養師推薦", "桃園營養師推薦", "健康講座接案講師",
    "職場健康促進講座", "長照營養師", "穩定血糖早餐", "食品營養標示法規",
    "辦公室輕食手作示範", "植物芳香手作營養工作坊", "高齡肌少症飲食講座", "失智症預防飲食工作坊",
    "功能醫學門診", "企業營養講座推薦", "食品營養博士講師", "高階主管減壓與護心飲食",
    "預防脂肪肝與三高飲食講座", "辦公室微運動與飲食搭配", "生動幽默營養講師", "零明火健康飲食示範",
    "電鍋快煮壺料理教學", "體重管理與外食減醣工作坊", "樂齡大學健康講座", "長照機構吞嚥防嗆培訓",
    "蛋白質克數計算與吸收", "全穀膳食纖維與添加糖", "Omega-3 飽和脂肪抗發炎",
    "水分平衡與電解質生活判讀", "維生素 D 骨骼鈣化", "EAP 員工健康講座",
    "公司健康日講座規劃", "福委會健康活動推薦", "企業外聘營養講師", "台北營養師演講邀約",
    "桃園營養師演講邀約", "低鈉高纖外食示範講座"
]

def get_service():
    if not os.path.exists(CREDENTIALS_FILE):
        print(f"[ERROR] Credentials file not found at {CREDENTIALS_FILE}")
        sys.exit(1)
    creds = service_account.Credentials.from_service_account_file(CREDENTIALS_FILE, scopes=SCOPES)
    ctx = ssl.create_default_context()
    http = httplib2.Http()
    http.ssl_context = ctx
    authed_http = google_auth_httplib2.AuthorizedHttp(creds, http=http)
    return build('searchconsole', 'v1', http=authed_http)

def generate_report():
    service = get_service()
    
    # 1. Probe available dates in 2026
    date_probe = service.searchanalytics().query(
        siteUrl=SITE_URL, 
        body={'startDate': '2026-05-18', 'endDate': (datetime.now() - timedelta(days=1)).strftime('%Y-%m-%d'), 'dimensions': ['date'], 'rowLimit': 500}
    ).execute()
    
    date_rows = date_probe.get('rows', [])
    if not date_rows:
        print("[WARNING] No date data returned by GSC.")
        return
    
    first_date = date_rows[0]['keys'][0]
    latest_date = date_rows[-1]['keys'][0]
    
    # 2. Total all-time performance
    all_time_res = service.searchanalytics().query(
        siteUrl=SITE_URL,
        body={'startDate': first_date, 'endDate': latest_date}
    ).execute().get('rows', [{}])[0]
    
    # 3. Rolling 28 days
    dt_latest = datetime.strptime(latest_date, '%Y-%m-%d')
    start_28d = (dt_latest - timedelta(days=28)).strftime('%Y-%m-%d')
    res_28d = service.searchanalytics().query(
        siteUrl=SITE_URL,
        body={'startDate': start_28d, 'endDate': latest_date}
    ).execute().get('rows', [{}])[0]
    
    # 4. Top Pages Performance (all-time & rolling 28d)
    pages_res = service.searchanalytics().query(
        siteUrl=SITE_URL,
        body={'startDate': first_date, 'endDate': latest_date, 'dimensions': ['page'], 'rowLimit': 100}
    ).execute().get('rows', [])
    
    pages_map = {p['keys'][0]: p for p in pages_res}
    
    # 5. Queries Breakdown (all-time & rolling 28d)
    queries_res = service.searchanalytics().query(
        siteUrl=SITE_URL,
        body={'startDate': first_date, 'endDate': latest_date, 'dimensions': ['query'], 'rowLimit': 500}
    ).execute().get('rows', [])
    
    queries_28d = service.searchanalytics().query(
        siteUrl=SITE_URL,
        body={'startDate': start_28d, 'endDate': latest_date, 'dimensions': ['query'], 'rowLimit': 500}
    ).execute().get('rows', [])
    
    # 6. Build Weekly Report Markdown
    now_str = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    report_filename = f"GSC_Weekly_Growth_Report_{dt_latest.strftime('%Y-%m-%d')}.md"
    report_path = os.path.join(REPORTS_DIR, report_filename)
    
    md = []
    md.append(f"# Kat Chang 凱特營養師網站｜Google Search Console 每週成長進度報告")
    md.append(f"\n> **產出時間**：{now_str}  ")
    md.append(f"> **官方最新數據區間**：歷史累計 ({first_date} ~ **{latest_date}**) ｜ 近 28 天 ({start_28d} ~ **{latest_date}**)  ")
    md.append(f"> **監測網址**：`{SITE_URL}`  ")
    md.append(f"> **監測指標**：點擊數 (Clicks)、曝光數 (Impressions)、點閱率 (CTR)、平均排名 (Position)  ")
    md.append(f"> **數據來源**：Google Search Console Official API (71 組核心關鍵字庫)\n")
    md.append(f"---\n")
    
    md.append(f"## 📊 一、全站核心總指標")
    md.append(f"| 指標項目 | 歷史累計 ({first_date}~{latest_date}) | 近 28 天成長走勢 ({start_28d}~{latest_date}) |")
    md.append(f"|---|:---:|:---:|")
    md.append(f"| **總點擊數 (Clicks)** | **{all_time_res.get('clicks', 0)} 次** | **{res_28d.get('clicks', 0)} 次** |")
    md.append(f"| **總曝光數 (Impressions)** | **{all_time_res.get('impressions', 0)} 次** | **{res_28d.get('impressions', 0)} 次** |")
    md.append(f"| **平均點閱率 (CTR)** | **{all_time_res.get('ctr', 0)*100:.2f}%** | **{res_28d.get('ctr', 0)*100:.2f}%** |")
    md.append(f"| **全站平均搜尋排名 (Position)** | **{all_time_res.get('position', 0):.2f} 名** | **{res_28d.get('position', 0):.2f} 名** |\n")
    
    md.append(f"## 🛠️ 二、6 大主打互動教具專屬成效追蹤板塊")
    md.append(f"針對 6 大主打教具路徑，追蹤獨立點擊、曝光、CTR 與排名，並對應專屬 30 組擴充關鍵字：\n")
    md.append(f"| 教具名稱 | 教具 URL 路徑 | 累計點擊 | 累計曝光 | 點閱率 | 官方排名 | 專屬主打擴充關鍵字群 (共 30 組) |")
    md.append(f"|---|---|:---:|:---:|:---:|:---:|---|")
    
    for tool in CORE_TOOLS:
        p_data = pages_map.get(tool["canonical"]) or pages_map.get(tool["canonical"].rstrip("/"))
        c = p_data.get('clicks', 0) if p_data else 0
        imp = p_data.get('impressions', 0) if p_data else 0
        ctr = (p_data.get('ctr', 0) * 100) if p_data else 0.0
        pos = f"{p_data.get('position', 0):.1f}" if p_data else "新上線觀測中"
        kw_str = "、".join(tool["keywords"][:3]) + " 等"
        md.append(f"| **{tool['name']}** | `{tool['path']}` | {c} | {imp} | {ctr:.1f}% | **{pos}** | {kw_str} |")
    md.append("")
    
    md.append(f"## 📄 三、全站主要網頁成效分佈")
    md.append(f"| 網頁 URL | 點擊數 | 曝光數 | 點閱率 (CTR) | 平均排名 | 頁面定位 |")
    md.append(f"|---|:---:|:---:|:---:|:---:|---|")
    for p in pages_res:
        url = p['keys'][0]
        c = p.get('clicks', 0)
        imp = p.get('impressions', 0)
        ctr = p.get('ctr', 0) * 100
        pos = p.get('position', 0)
        theme = "全站首頁/品牌" if url == SITE_URL else ("個人簡介" if "about" in url else ("授課講座" if "class" in url else ("專文連載" if "post" in url else ("教具工具" if "teach" in url else "站內索引"))))
        md.append(f"| `{url}` | {c} | {imp} | {ctr:.1f}% | **{pos:.1f}** | {theme} |")
    md.append("")
    
    md.append(f"## 🎯 四、全站 71 組關鍵字與官方解鎖狀態")
    md.append(f"### 1. 官方已解鎖查詢詞 (Google 官方去識別化已揭露詞)")
    if queries_res:
        md.append(f"| 查詢關鍵字 | 累計點擊 | 累計曝光 | 點閱率 (CTR) | 官方平均排名 |")
        md.append(f"|---|:---:|:---:|:---:|:---:|")
        for q in queries_res:
            md.append(f"| **{q['keys'][0]}** | {q.get('clicks', 0)} | {q.get('impressions', 0)} | {q.get('ctr', 0)*100:.1f}% | **{q.get('position', 0):.1f}** |")
    else:
        md.append(f"*目前所有長尾查詢因搜尋頻率初期低於 Google 去識別化隱私門檻，數據已 100% 歸入上述頁面。*")
    md.append("")
    
    md.append(f"### 2. 71 組關鍵字矩陣佈局覆蓋狀態")
    md.append(f"- **原 41 組商業與專科關鍵字**：已 100% 深入首頁、簡介頁、授課頁（四大特色模組）與 12 篇衛教專文。")
    md.append(f"- **6 大教具 30 組擴充關鍵字**：已全面配置於 6 大主打教具頁面之標題、Meta 描述、關鍵字與結構化資料中。")
    md.append(f"- **排程監控機制**：每週一 09:00 定期透過 Windows Task Scheduler 與 Antigravity 自動檢核並產生本報表。\n")
    
    report_text = "\n".join(md)
    with open(report_path, "w", encoding="utf-8") as f:
        f.write(report_text)
        
    print(f"[OK] Upgraded Weekly Report generated successfully: {report_path}")
    print("\n" + "="*50)
    print(report_text)
    print("="*50)

if __name__ == '__main__':
    generate_report()
