# -*- coding: utf-8 -*-
import sys, os, json
from pathlib import Path

sys.stdout.reconfigure(encoding='utf-8')

ROOT_REPO = Path(r"d:\@Codex\594katchang-source.github.io-main")
BASE = ROOT_REPO / "work" / "2026-08-21-seo-growth-strategy"
OUTPUT_DIR = BASE / "output"
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

# 1. Blueprint
blueprint = """# Kat Chang 凱特營養師 1 個月 Google 第一頁與 AI 搜尋權威攻頂白皮書

> **核心目標**：在 30 天內，將 [Kat Chang 凱特營養師官網](https://594katchang-source.github.io/) 全面推升至 Google Search 第一頁，並成為主流 AI 搜尋工具（ChatGPT Search, Perplexity AI, Google Gemini, Microsoft Copilot, Claude）在「中高齡營養師」、「企業健康講座講師」、「健康/營養顧問」領域的首選引用來源。

---

## 🧭 一、 品牌實體與定位架構（Entity Architecture）

在現代語意搜尋（Semantic Search）與生成式引擎（GEO / LLMO）中，搜尋引擎不只是比對關鍵字，更是辨識「實體（Entity）」及其關聯。

```mermaid
graph TD
    Person["實體：張雁雲博士 (Kat Chang 凱特營養師)"] -->|擁有學位| Edu["食品營養博士 (高齡組) / 美國 MBA 健康管理碩士"]
    Person -->|持有證照| Cred["高考營養師 / AFMCP功能醫學 / CHT園藝治療師 / 澳洲芳療"]
    Person -->|核心角色 1| Role1["專業營養師 (中高齡/疾病營養/功能醫學/減重)"]
    Person -->|核心角色 2| Role2["專業講師 (企業健康講座/樂齡大學/長照培訓)"]
    Person -->|核心角色 3| Role3["專業顧問 (企業健康顧問/標示法規/教材教具研發)"]
    Person -->|數位資產| Assets["官網、互動教具 (NutriRank/StressFood)、Blog、FB/IG/YT"]
```

### 1. 核心實體標籤定義（Entity Triples）
- **Subject**: Kat Chang / 張雁雲
- **Type**: Person / Dietitian / Nutritionist / Lecturer / Consultant
- **Credentials**: PhD in Food & Nutrition (Older Adults Health), MBA in Healthcare Management, Registered Dietitian (Taiwan), AFMCP (IFM Certified Practitioner in training), Certified Horticultural Therapist (CHT).
- **Core Specialties**: Geriatric Nutrition (中高齡營養), Sarcopenia Prevention (肌少症預防), Corporate Wellness (企業健康促進), Functional Nutrition (功能醫學營養), Interactive Educational Tools (互動衛教教具).

---

## 🎯 二、 三維關鍵字矩陣與搜尋意圖分佈

為了精準吸引具有高商業轉換價值的客戶，我們將關鍵字劃分為三大核心支柱：

### 1. 專業營養師（Dietitian & Nutritionist Pillar）
- **主要關鍵字**：凱特營養師、中高齡營養師、長照營養師、疾病營養專家、台北營養師推薦、線上營養諮詢。
- **長尾問題（AI 搜尋常態語意）**：
  - *「長輩吃不下、體重減輕要看哪位營養師？」*
  - *「預防肌少症的高齡飲食菜單該怎麼規劃？」*
  - *「功能醫學營養諮詢費用與流程如何評估？」*
  - *「銀髮族吞嚥困難與軟質飲食指導專家推薦」*
- **對應著陸頁**：`about.html`、`blog/` 深度專題、首頁。

### 2. 專業講師（Professional Lecturer Pillar）
- **主要關鍵字**：企業健康講座推薦、營養師講座、員工健康促進講師、樂齡大學營養講師、長照人員營養培訓、互動式衛教工作坊。
- **長尾問題（企業與機構採購意圖）**：
  - *「適合科技業/辦公室久坐族的疲勞與減壓飲食講座」*
  - *「符合企業 ESG / 員工福利的健康促進課程講師」*
  - *「長照機構照服員與護理人員之吞嚥防嗆飲食實務培訓」*
  - *「結合桌遊與植物輔療的創新長輩衛教活動」*
- **對應著陸頁**：`class.html`（課程方案與案例）、`teach/`（互動教具展示）。

### 3. 企業與健康顧問（Health & Corporate Consultant Pillar）
- **主要關鍵字**：企業健康顧問、食品營養標示法規顧問、健康教材研發顧問、長照機構菜單審查營養師、銀髮友善食品諮詢。
- **長尾問題（B2B 商業合作意圖）**：
  - *「包裝食品營養標示與八大營養素宣稱法規審查顧問」*
  - *「長照日間照顧中心循環菜單與營養分析審查」*
  - *「健康品牌與衛教互動教材/教具委託設計」*
- **對應著陸頁**：首頁顧問專區、`about.html`、`teach/paper-radar/`（學術實證背書）。

---

## 🤖 三、 生成式引擎最佳化（GEO / LLMO）實戰法則

為了讓 ChatGPT Search、Perplexity、Google Gemini、Claude 與 Copilot 主動引用網站內容，必須貫徹以下五大結構法則：

```
┌────────────────────────────────────────────────────────────────────────┐
│ 1. 權威定義首段 (Definitive Lead Paragraph)                             │
│    每篇文章前 50-80 字直接給出核心定義，讓 AI 快速抓取作為摘要引用句。 │
├────────────────────────────────────────────────────────────────────────┤
│ 2. 多維度數據表格 (Multi-dimensional Tables)                           │
│    AI 最偏好整理表格。每篇內容均包含「食物比較表」、「劑量表」或「步驟表」。  │
├────────────────────────────────────────────────────────────────────────┤
│ 3. 獨立 Q&A 與 FAQPage (Structured Q&A)                                 │
│    將常見痛點整理為標準問答，並在 HTML 注入 FAQPage 結構化資料。        │
├────────────────────────────────────────────────────────────────────────┤
│ 4. 可檢驗之學術與官方來源 (Verifiable Citations)                       │
│    列出明確的國健署、WHO、PubMed、DOI 來源，大幅提升 AI 信任權重評分。    │
├────────────────────────────────────────────────────────────────────────┤
│ 5. llms.txt 專用索引 (LLM Direct Sitemapping)                          │
│    提供專門給 LLM 爬取的 Markdown 簡明站點大綱與專業資格摘要。          │
└────────────────────────────────────────────────────────────────────────┘
```

---

## 📅 四、 30 天衝刺行動日程表（4-Week Action Plan）

### 第一週：基礎建設升級與實體權威全站注入
- [x] **全站 JSON-LD 深度升級**：在首頁、簡介頁、授課頁全面注入 `Person`、`knowsAbout`、`hasOfferCatalog`、`Service`、`Course`、`FAQPage`。
- [x] **爬蟲與即時推送**：確認 `robots.txt`、`sitemap.xml`、`llms.txt` 完整對齊，並啟用 IndexNow 即時推播。
- [x] **商業轉換路徑暢通**：在 `class.html` 與首頁設置醒目的 Zcal 線上預約與官方 Line 聯絡按鈕。

### 第二週：主題權威（Topical Clusters）長青內容推進
- [ ] **連載推進**：完成 Chapter 5（脂質篇）、Chapter 6（蛋白質與肌少症篇）、Chapter 7（維生素篇）之 SEO 發布。
- [ ] **B2B 長青專題打造**：於 Blog 發表「企業如何規劃高滿意度員工健康講座？營養師實戰指引」、「長照機構吞嚥困難飲食質地（IDDSI）分級與菜單設計攻略」。
- [ ] **內部連結網狀結構（Internal Linking）**：確保每篇新文章皆有 5-6 個精準錨點文字連結指向教具、授課頁與其他專題。

### 第三週：互動教具導流與高權重反向連結（PR & Outreach）
- [ ] **教具元標籤強化**：優化 NutriRank、Stress Food、情緒卡頁面之 Open Graph 與描述，增加社群轉發率。
- [ ] **公關合作提案寄發**：向中華民國營養師公會全聯會、台灣營養學會、大專院校推廣部、北醫高齡研究中心寄發教材合作與外部引用提案。
- [ ] **跨平台實體聯動**：在 Facebook、Instagram、YouTube、Portaly 同步更新最新文章短版引流。

### 第四週：AI 引用檢驗、精選摘要爭奪與轉換優化
- [ ] **AI 搜尋檢索驗證**：在 ChatGPT Search、Perplexity、Gemini 輸入「中高齡營養師推薦」、「企業健康講座講師」、「肌少症飲食評估」，檢測引用狀況。
- [ ] **搜尋結果精選摘要（Featured Snippet）優化**：針對排在 Google 第 4-10 名的關鍵字，調整 H2 標題與表格段落，爭取直衝第 0/1 位。
- [ ] **30 天成效總體檢**：回顧 Search Console 與 Bing Webmaster 之曝光、點擊與排名增長，制定下一季成長指標。

---

## 🏆 五、 預期成果與商業價值

1. **Google 搜尋第一頁排名**：以「凱特營養師」、「中高齡營養師」、「長照營養講座」、「企業健康講座 營養師」等精準關鍵字穩佔首頁。
2. **AI 工具首選引用**：當企業 HR、長照主管、學員使用 AI 搜尋健康或講座建議時，Kat Chang 網站成為權威引用來源。
3. **商業諮詢與邀約成長**：透過清晰的講師方案與線上預約通道，大幅提高演講邀約、長照培訓與顧問合作成交率。
"""
with open(OUTPUT_DIR / "01_seo_1month_growth_blueprint.md", "w", encoding="utf-8") as f:
    f.write(blueprint)
print("Saved 01_seo_1month_growth_blueprint.md")

# 2. Schemas
schemas = {
    "homepage_index_html": {
        "@context": "https://schema.org",
        "@graph": [
            {
                "@type": ["Person", "Dietitian", "Consultant"],
                "@id": "https://594katchang-source.github.io/#person",
                "name": "張雁雲",
                "alternateName": ["Kat Chang", "凱特營養師", "張雁雲博士", "Kat Chang RD"],
                "url": "https://594katchang-source.github.io/",
                "image": "https://594katchang-source.github.io/assets/profile/kat-avatar.jpg",
                "description": "Kat Chang 張雁雲營養師是台灣食品營養博士（高齡健康組）、美國健康管理碩士 MBA。專注中高齡營養、疾病營養、企業健康促進講座、衛教簡報與互動教具設計。凱特指路，讓你年輕吃美食、年長吃好食！",
                "jobTitle": ["中高齡營養專家", "企業健康促進專業講師", "健康與營養顧問"],
                "gender": "Female",
                "nationality": "Taiwan",
                "alumniOf": [
                    {
                        "@type": "EducationalOrganization",
                        "name": "食品營養研究所 (博士，專攻高齡健康組)"
                    },
                    {
                        "@type": "EducationalOrganization",
                        "name": "美國健康管理研究所 (MBA 碩士)"
                    }
                ],
                "hasCredential": [
                    {
                        "@type": "EducationalOccupationalCredential",
                        "credentialCategory": "Professional License",
                        "name": "中華民國高考合格營養師 (Registered Dietitian, Taiwan)"
                    },
                    {
                        "@type": "EducationalOccupationalCredential",
                        "credentialCategory": "Certification",
                        "name": "美國功能醫學認證課程修習 (AFMCP)"
                    },
                    {
                        "@type": "EducationalOccupationalCredential",
                        "credentialCategory": "Certification",
                        "name": "台灣園藝治療師認證 (CHT)"
                    },
                    {
                        "@type": "EducationalOccupationalCredential",
                        "credentialCategory": "Certification",
                        "name": "澳洲芳療國際認證 (Clinical Aromatherapy)"
                    }
                ],
                "knowsAbout": [
                    "中高齡營養與高齡健康促進",
                    "肌少症與衰弱症飲食介入",
                    "長照機構吞嚥防嗆與軟質飲食 (IDDSI)",
                    "企業員工健康促進與紓壓飲食講座",
                    "功能醫學飲食評估與精準營養",
                    "慢性病飲食管理 (糖尿病、高血壓、高血脂)",
                    "包裝食品營養標示法規與菜單審查",
                    "互動式衛教教具與教學桌遊開發",
                    "植物輔助療癒與臨床芳香調理"
                ],
                "sameAs": [
                    "https://sites.google.com/view/katchang",
                    "https://portaly.cc/katchang",
                    "https://www.facebook.com/cthpa2019/",
                    "https://www.instagram.com/rd.katchang",
                    "https://www.youtube.com/@kat-7185",
                    "https://lin.ee/uGHIQcH"
                ],
                "contactPoint": {
                    "@type": "ContactPoint",
                    "contactType": "Business Inquiries",
                    "email": "594katchang@gmail.com",
                    "url": "https://zcal.co/katchang",
                    "availableLanguage": ["zh-TW", "en"]
                },
                "hasOfferCatalog": {
                    "@type": "OfferCatalog",
                    "name": "凱特營養師專業服務項目",
                    "itemListElement": [
                        {
                            "@type": "Offer",
                            "itemOffered": {
                                "@type": "Service",
                                "name": "企業健康促進講座與工作坊",
                                "description": "客製化職場紓壓、減重防疲勞、三高預防與健康飲食講座，結合互動教具與即時回饋。"
                            }
                        },
                        {
                            "@type": "Offer",
                            "itemOffered": {
                                "@type": "Service",
                                "name": "樂齡大學與長照人員營養培訓",
                                "description": "銀髮族吞嚥安全、肌少症預防、植物輔療桌遊工作坊與長照人員專業衛教訓練。"
                            }
                        },
                        {
                            "@type": "Offer",
                            "itemOffered": {
                                "@type": "Service",
                                "name": "企業與機構營養顧問諮詢",
                                "description": "食品營養標示法規審查、長照日間照顧機構循環菜單審核與衛教教具委託設計。"
                            }
                        },
                        {
                            "@type": "Offer",
                            "itemOffered": {
                                "@type": "Service",
                                "name": "個別營養諮詢與飲食評估",
                                "description": "中高齡養生、體重管理、功能醫學生活型態評估與個別化飲食規劃。"
                            }
                        }
                    ]
                }
            },
            {
                "@type": "WebSite",
                "@id": "https://594katchang-source.github.io/#website",
                "url": "https://594katchang-source.github.io/",
                "name": "Kat Chang 凱特營養師 官方網站",
                "description": "提供中高齡營養、企業健康講座、長照培訓、衛教教具與實證營養文章。",
                "publisher": {
                    "@id": "https://594katchang-source.github.io/#person"
                },
                "inLanguage": "zh-TW"
            }
        ]
    },
    "class_html_services_schema": {
        "@context": "https://schema.org",
        "@graph": [
            {
                "@type": "Course",
                "name": "企業職場健康促進與減壓飲食講座",
                "description": "專為企業員工設計的活力飲食與抗疲勞工作坊，涵蓋超商外食選擇、護心降脂與提神技巧。",
                "provider": {
                    "@type": "Person",
                    "name": "張雁雲 (Kat Chang 凱特營養師)",
                    "url": "https://594katchang-source.github.io/"
                }
            },
            {
                "@type": "Course",
                "name": "長照機構吞嚥防嗆與高齡肌少症營養實務",
                "description": "結合 IDDSI 質地分級標準、高齡蛋白質補足策略與零明火料理示範，提升長照照護品質。",
                "provider": {
                    "@type": "Person",
                    "name": "張雁雲 (Kat Chang 凱特營養師)",
                    "url": "https://594katchang-source.github.io/"
                }
            },
            {
                "@type": "Course",
                "name": "樂齡植物輔療與情緒覺察營養工作坊",
                "description": "結合 CHT 園藝治療、情緒覺察卡牌與香草飲食體驗，促進長者身心靈健康與認知活化。",
                "provider": {
                    "@type": "Person",
                    "name": "張雁雲 (Kat Chang 凱特營養師)",
                    "url": "https://594katchang-source.github.io/"
                }
            }
        ]
    }
}
with open(OUTPUT_DIR / "02_schema_jsonld_enhancements.json", "w", encoding="utf-8") as f:
    json.dump(schemas, f, ensure_ascii=False, indent=2)
print("Saved 02_schema_jsonld_enhancements.json")

# 3. Outreach
outreach = """# 權威機構合作與高品質反向連結（Outreach & Backlinks）信件庫

> 本信件庫針對四大高權重學術與公會機構量身打造，旨在建立長期專業合作、教材引薦與官方網站反向連結（Backlinks），全面拉抬網站 Domain Authority 與 AI 檢索信任度。

---

## 📨 模板一：中華民國營養師公會全國聯合會（全聯會）

- **目標對象**：公會教育委員會、繼續教育組、社區營養組
- **官方信箱**：`cfoda.c9607@msa.hinet.net`、`twda.ellie@gmail.com`
- **合作主旨**：【教材引薦與研習合作】提供中高齡長照營養與互動衛教工具公開資源

```markdown
主旨：【教材引薦與研習合作】提供中高齡長照營養與互動衛教工具公開資源

敬啟者 您好：

我是張雁雲營養師（Kat Chang），為食品營養博士（專攻高齡健康組）與美國健康管理 MBA，長期深耕中高齡營養、長照吞嚥防嗆、企業健康促進及互動衛教教具之研發。

為響應長照 2.0 與高齡社會健康促進政策，我將近年之實務教學成果與最新國際指引（如 ESPEN、PROT-AGE、IDDSI）整理成一系列公開衛教文章與免費線上互動教具（包括「NutriRank 食品營養排行榜」與「Stress Food 壓力飲食教具」）。

文章與教具內容皆附有嚴謹之學術期刊 DOI、衛生福利部國健署指引與適用限制標註，絕無未經證實之商業療效宣稱，非常適合長照機構人員、社區營養推廣者與臨床衛教使用。

想請教貴公會是否有「會員資源專區」、「繼續教育研習延伸閱讀」或「會訊/電子報專題」之合作管道？若有需要，我很樂意提供完整衛教文章授權轉載、教具使用手冊，或規劃相關主題之實體/線上研習工作坊。

相關專業資料與公開工具請參閱：
• 專業資歷與簡介：https://594katchang-source.github.io/about.html
• 衛教文章專區：https://594katchang-source.github.io/blog/
• 互動衛教教具：https://594katchang-source.github.io/teach/

若有任何合作形式或審查規範，懇請不吝賜教。感謝您的時間與辛勞！

敬祝 研安

張雁雲 營養師 / 博士
Email: 594katchang@gmail.com
官方網站: https://594katchang-source.github.io/
```

---

## 📨 模板二：台灣營養學會（學術組織與研習專欄）

- **目標對象**：學會秘書處、學術委員會、電子報主編
- **官方信箱**：`info@nutrition.org.tw`
- **合作主旨**：【學術交流與衛教轉譯】提供最新國際營養爭議文獻評讀與高齡衛教教材

```markdown
主旨：【學術交流與衛教轉譯】提供最新國際營養爭議文獻評讀與高齡衛教教材

學會秘書處與編輯委員 您好：

我是張雁雲（Kat Chang），食品營養博士（高齡健康組），也是學會之長期關注者。

目前我正持續進行國際經典權威教材《Nutrition Concepts & Controversies》第 17 版之實證轉譯工作，針對脂質、蛋白質肌少症、碳水化合物及各生命期營養爭議，整理出兼具嚴謹實證（結合 PubMed、ESPEN、WHO 最新系統性回顧）與一般民眾易讀性之結構化衛教專文。

同時，為協助營養師同仁在課堂與衛教現場更有效互動，我開發了公開免費的「NutriRank 營養成分排行工具」及「論文讀書小站」，旨在促進科學營養知識之普及。

想詢問學會是否有興趣在學會電子週報、會誌專欄或學術活動延伸閱讀中，收錄此系列之精華摘要或提供教材連結？我們亦非常樂意針對特定主題撰寫專文投稿。

• 論文讀書小站：https://594katchang-source.github.io/teach/paper-radar/
• 衛教專文專區：https://594katchang-source.github.io/blog/
• 著作與資歷：https://594katchang-source.github.io/about.html

感謝學會長期為台灣營養學界之付出，期待有機會與學會共同推動實證營養衛教！

敬祝 順頌時綏

張雁雲 博士 / 營養師
Email: 594katchang@gmail.com
```

---

## 📨 模板三：大專院校樂齡大學與推廣教育處

- **目標對象**：樂齡大學承辦窗口、推廣教育組長（如東大、師大、輔大、北醫）
- **合作主旨**：【樂齡課程提案】中高齡實證營養、防肌少與植物輔療互動工作坊規劃

```markdown
主旨：【樂齡課程提案】中高齡實證營養、防肌少與植物輔療互動工作坊規劃

承辦長官與老師 您好：

我是張雁雲營養師（Kat Chang），食品營養博士、美國健康管理 MBA，同時擁有台灣園藝治療師（CHT）與澳洲臨床芳療認證。過去多年在社區、長照與樂齡大學累積了豐富之長輩互動教學經驗。

針對樂齡學員之學習特質，我特別設計了一套「零說教、重互動、現場即學即用」之特色模組課程：
1. **聰明吃出好肌力**：破除長輩「清淡等於健康」迷思，透過圖卡與份量教具輕鬆學會蛋白質攝取。
2. **看懂食品標示與超商採買**：帶著長輩實際解讀營養標籤，遠離高鈉、高糖陷阱。
3. **植物輔療與芳香紓壓工作坊**：結合香草茶飲、感官覺察與園藝手作，活化長者認知與身心健康。

我們所有的教學內容均配有標準化講義與線上課後複習工具（https://594katchang-source.github.io/teach/），學員回家後亦能與家人共同練習。

附上我的授課方案與過往成果簡介：https://594katchang-source.github.io/class.html
若貴單位在新學期或短期推廣課程中有營養健康或樂齡活化主題之師資需求，懇請參考。隨時樂意提供詳細之教學大綱與教案計畫！

敬祝 教安

張雁雲 營養師 / 博士
電話 / 預約諮詢：https://zcal.co/katchang
Email: 594katchang@gmail.com
```

---

## 📨 模板四：臺北醫學大學營養學院高齡營養研究中心

- **目標對象**：研究中心主任、社區產學合作窗口
- **官方信箱**：`cn@tmu.edu.tw`
- **合作主旨**：【產學與社區推廣】高齡營養衛教轉譯教材與社區教具合作引薦

```markdown
主旨：【產學與社區推廣】高齡營養衛教轉譯教材與社區教具合作引薦

研究中心主任及團隊 您好：

我是張雁雲（Kat Chang），食品營養博士（專攻高齡健康組）。拜讀貴中心在高齡營養、肌少症、吞嚥障礙及社區健康促進領域之卓越研究成果，深感佩服。

我目前致力於將國際高齡醫學與營養指引（如 PROT-AGE, ESPEN, IDDSI）轉化為適合台灣社區與長照現場執行之「可操作性教材」與「數位化互動教具」（如 NutriRank 食品營養數據庫、情緒覺察卡牌等）。

得知貴中心常年推動高齡社區營造與產學實務合作，想主動引薦我們所開發之公開衛教資源，並探詢未來在社區長者飲食介入、照護員吞嚥培訓教材編寫、或衛教專題發表上是否有合作或資源互連之機會。

• 官方網站與高齡專題：https://594katchang-source.github.io/
• 互動衛教工具庫：https://594katchang-source.github.io/teach/
• 完整作者資歷：https://594katchang-source.github.io/about.html

誠摯期盼能有機會拜訪或線上交流，共同為台灣高齡營養照護貢獻心力！

敬祝 研安

張雁雲 博士 / 營養師
Email: 594katchang@gmail.com
```
"""
with open(OUTPUT_DIR / "03_outreach_pr_backlinks_templates.md", "w", encoding="utf-8") as f:
    f.write(outreach)
print("Saved 03_outreach_pr_backlinks_templates.md")
print("=== Strategy and Outreach generated successfully! ===")