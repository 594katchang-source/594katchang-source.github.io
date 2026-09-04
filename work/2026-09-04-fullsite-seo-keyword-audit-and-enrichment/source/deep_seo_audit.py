# -*- coding: utf-8 -*-
import sys
sys.stdout.reconfigure(encoding='utf-8')
import json
from pathlib import Path
from bs4 import BeautifulSoup

ROOT = Path(r"d:\@Codex\594katchang-source.github.io-main")

KEYWORDS = {
    "A-01 企業健康講座": "企業健康講座",
    "A-02 EAP 員工健康講座": "EAP 員工健康講座",
    "A-03 職場健康促進講座": "職場健康促進講座",
    "A-04 企業營養講座推薦": "企業營養講座推薦",
    "A-05 公司健康日講座規劃": "公司健康日講座規劃",
    "A-06 福委會健康活動推薦": "福委會健康活動推薦",
    "B-01 健康講座接案講師": "健康講座接案講師",
    "B-02 企業外聘營養講師": "企業外聘營養講師",
    "B-03 台北營養師演講邀約": "台北營養師演講邀約",
    "B-03b 桃園營養師演講邀約": "桃園營養師演講邀約",
    "B-04 生動幽默營養講師": "生動幽默營養講師",
    "B-05 食品營養博士講師": "食品營養博士講師",
    "C-01 零明火健康飲食示範": "零明火健康飲食示範",
    "C-02 辦公室輕食手作示範": "辦公室輕食手作示範",
    "C-03 電鍋快煮壺料理教學": "電鍋快煮壺料理教學",
    "C-04 低鈉高纖外食示範講座": "低鈉高纖外食示範講座",
    "C-05 植物芳香手作營養工作坊": "植物芳香手作營養工作坊",
    "D-01 上班族外食抗疲勞飲食": "上班族外食抗疲勞飲食",
    "D-02 高階主管減壓與護心飲食": "高階主管減壓與護心飲食",
    "D-03 體重管理與外食減醣工作坊": "體重管理與外食減醣工作坊",
    "D-04 預防脂肪肝與三高飲食講座": "預防脂肪肝與三高飲食講座",
    "D-05 辦公室微運動與飲食搭配": "辦公室微運動與飲食搭配",
    "E-01 樂齡大學健康講座": "樂齡大學健康講座",
    "E-02 長照機構吞嚥防嗆培訓": "長照機構吞嚥防嗆培訓",
    "E-03 高齡肌少症飲食講座": "高齡肌少症飲食講座",
    "E-04 失智症預防飲食工作坊": "失智症預防飲食工作坊",
    "BRAND-01 中高齡營養師": "中高齡營養師",
    "BRAND-02 中高齡營養專家": "中高齡營養專家",
    "BRAND-03 台北營養師推薦": "台北營養師推薦",
    "BRAND-04 桃園營養師推薦": "桃園營養師推薦",
    "BRAND-05 長照營養師": "長照營養師",
    "BRAND-06 功能醫學門診": "功能醫學門診",
    "BRAND-07 精準營養": "精準營養",
    "BRAND-08 肌少症飲食": "肌少症飲食",
    "BRAND-09 蛋白質克數計算與吸收": "蛋白質克數計算與吸收",
    "BRAND-10 穩定血糖早餐": "穩定血糖早餐",
    "BRAND-11 全穀膳食纖維與添加糖": "全穀膳食纖維與添加糖",
    "BRAND-12 Omega-3 飽和脂肪抗發炎": "Omega-3 飽和脂肪抗發炎",
    "BRAND-13 水分平衡與電解質生活判讀": "水分平衡與電解質生活判讀",
    "BRAND-14 維生素 D 骨骼鈣化": "維生素 D 骨骼鈣化",
    "BRAND-15 食品營養標示法規": "食品營養標示法規"
}

SHORT_TOKENS = [
    "中高齡營養師", "中高齡營養", "肌少症飲食", "肌少症", "企業健康講座",
    "健康講座", "營養講座", "外聘營養師", "外聘講師", "EAP",
    "台北營養師", "桃園營養師", "台北營養師推薦", "桃園營養師推薦",
    "抗疲勞", "零明火", "料理示範", "植物輔療", "芳香調理", "吞嚥防嗆"
]

def analyze_site():
    results = {
        "pages": {},
        "articles": {},
        "keyword_occurrences": {k: 0 for k in KEYWORDS},
        "short_token_occurrences": {t: 0 for t in SHORT_TOKENS}
    }

    html_files = [
        ROOT / "index.html",
        ROOT / "about.html",
        ROOT / "class.html",
        ROOT / "blog" / "index.html",
        ROOT / "blog" / "post.html",
        ROOT / "teach" / "index.html",
        ROOT / "teach" / "nutritionranking" / "index.html",
        ROOT / "teach" / "Stress-Food" / "index.html",
        ROOT / "teach" / "nutrition-battle" / "index.html",
        ROOT / "teach" / "emotion-cards" / "index.html",
        ROOT / "teach" / "paper-radar" / "index.html"
    ]

    for hf in html_files:
        rel = str(hf.relative_to(ROOT)).replace("\\", "/")
        if not hf.exists():
            continue
        text = hf.read_text(encoding="utf-8")
        soup = BeautifulSoup(text, "html.parser")
        
        title = soup.title.string.strip() if soup.title and soup.title.string else ""
        meta_desc = ""
        meta_kw = ""
        m_desc = soup.find("meta", attrs={"name": "description"})
        if m_desc:
            meta_desc = m_desc.get("content", "")
        m_kw = soup.find("meta", attrs={"name": "keywords"})
        if m_kw:
            meta_kw = m_kw.get("content", "")
            
        h1s = [h.get_text(strip=True) for h in soup.find_all("h1")]
        h2s = [h.get_text(strip=True) for h in soup.find_all("h2")]
        
        schemas = []
        for s in soup.find_all("script", attrs={"type": "application/ld+json"}):
            try:
                schemas.append(json.loads(s.string))
            except Exception:
                pass

        page_kw_hits = {}
        for code, kw in KEYWORDS.items():
            cnt = text.count(kw)
            if cnt > 0:
                page_kw_hits[code] = cnt
                results["keyword_occurrences"][code] += cnt

        page_token_hits = {}
        for token in SHORT_TOKENS:
            cnt = text.count(token)
            if cnt > 0:
                page_token_hits[token] = cnt
                results["short_token_occurrences"][token] += cnt

        results["pages"][rel] = {
            "title": title,
            "meta_desc": meta_desc,
            "meta_keywords": meta_kw,
            "h1": h1s,
            "h2_sample": h2s[:5],
            "schemas_found": len(schemas),
            "schema_types": [s.get("@type", "graph" if "@graph" in s else "unknown") for s in schemas],
            "kw_hits": page_kw_hits,
            "token_hits": page_token_hits
        }

    posts_path = ROOT / "blog" / "posts.json"
    posts_data = json.loads(posts_path.read_text(encoding="utf-8"))
    
    for p in posts_data["posts"]:
        pid = p["id"]
        title = p["title"]
        category = p.get("category", "")
        excerpt = p.get("excerpt", "")
        body = p.get("body", "")
        full_text = f"{title}\n{category}\n{excerpt}\n{body}\n{' '.join(p.get('keywords', []))}"
        
        post_kw_hits = {}
        for code, kw in KEYWORDS.items():
            cnt = full_text.count(kw)
            if cnt > 0:
                post_kw_hits[code] = cnt
                results["keyword_occurrences"][code] += cnt

        post_token_hits = {}
        for token in SHORT_TOKENS:
            cnt = full_text.count(token)
            if cnt > 0:
                post_token_hits[token] = cnt
                results["short_token_occurrences"][token] += cnt

        results["articles"][pid] = {
            "title": title,
            "category": category,
            "date": p["date"],
            "keywords": p.get("keywords", []),
            "has_faq": "faq" in p,
            "faq_count": len(p.get("faq", [])),
            "body_length": len(body),
            "kw_hits": post_kw_hits,
            "token_hits": post_token_hits
        }

    out_file = ROOT / "work" / "2026-09-04-fullsite-seo-keyword-audit-and-enrichment" / "output" / "site_deep_audit_data.json"
    out_file.write_text(json.dumps(results, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"[OK] Audit completed! Output saved to {out_file}")

if __name__ == "__main__":
    analyze_site()
