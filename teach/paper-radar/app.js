(function () {
  "use strict";

  const PAGE_SIZE = 50;
  const state = { items: [], query: "", kind: "all", page: 1 };
  const elements = {
    query: document.querySelector("#query"),
    status: document.querySelector("#status"),
    list: document.querySelector("#paper-list"),
    pagination: document.querySelector("#pagination"),
    updatedAt: document.querySelector("#updated-at"),
    totalCount: document.querySelector("#total-count"),
    reviewCount: document.querySelector("#review-count"),
    digestCount: document.querySelector("#digest-count"),
  };

  const SEARCH_GROUPS = [
    ["肥胖", "obesity", "obesity management", "obesity metabolism"],
    ["老化", "衰老", "高齡", "older adults", "aging", "healthy aging"],
    ["衰弱", "frailty"],
    ["肌少症", "sarcopenia", "muscle loss"],
    ["營養", "營養學", "nutrition", "nutritional"],
    ["飲食型態", "飲食模式", "dietary pattern", "diet pattern"],
    ["蛋白質", "protein"],
    ["微量營養素", "micronutrients", "vitamins", "minerals"],
    ["精準營養", "precision nutrition"],
    ["代謝體學", "metabolomics", "metabolome"],
    ["生物標記", "biomarkers", "biomarker"],
    ["草藥", "草本", "herbal medicine", "herbal"],
    ["植物化學物", "植物化合物", "phytochemicals", "phytochemical"],
    ["膳食補充品", "營養補充品", "dietary supplements", "supplements"],
    ["慢性腎病", "慢性腎臟病", "chronic kidney disease", "CKD"],
    ["糖尿病", "diabetes", "type 2 diabetes", "T2DM"],
    ["心血管疾病", "cardiovascular disease", "cardiovascular"],
    ["癌症", "cancer", "oncology"],
  ];

  const JOURNAL_LABELS = {
    "Frontiers in Nutrition (PubMed)": "營養學前沿（PubMed）",
    "Aging, frailty and sarcopenia (PubMed)": "老化、衰弱與肌少症（PubMed）",
    "Precision nutrition and biomarkers (PubMed)": "精準營養與生物標記（PubMed）",
    "Obesity and metabolism (PubMed)": "肥胖與代謝（PubMed）",
    "Herbs, phytochemicals and supplement safety (PubMed)": "草藥、植物化學物與補充品安全（PubMed）",
    "Nutrients (PubMed)": "營養素（PubMed）",
    "Nutrition open-access records (PubMed / PMC route)": "營養學開放取用文獻（PubMed／PMC）",
    "Nutrition guidelines and consensus (PubMed)": "營養指引與共識（PubMed）",
    "Other nutrition journals (PubMed)": "其他營養期刊（PubMed）",
    "Clinical Nutrition (PubMed)": "臨床營養學（PubMed）",
    "Scientific Reports (PubMed)": "科學報告（PubMed）",
  };

  const TITLE_LABELS = {
    "A path to sustainable and healthy diets: modeling ovo-lacto-vegetarian food-based dietary guidelines.": "永續且健康飲食的實踐路徑：以蛋奶素食物為基礎的飲食指引建模",
    "Dietary and nutritional supplementation strategies for table tennis athletes: a mini-review.": "桌球運動員的飲食與營養補充策略：迷你回顧",
    "Effects of Curcumin Supplementation on Exercise Recovery, Oxidative Stress, Inflammation, Muscle Damage, and Performance in Exercise and Sport Contexts: A Systematic Review.": "薑黃素補充對運動恢復、氧化壓力、發炎、肌肉損傷與運動表現的影響：系統性回顧",
    "Association of Dietary Animal and Plant Protein Composition with All-Cause Mortality: 24-Year Population-Based Cohort Study.": "膳食中動物性與植物性蛋白質比例和全因死亡率的關聯：24 年人口世代研究",
    "Cardiometabolic Biomarkers for Disease Severity Prediction in Metabolic Dysfunction-Associated Steatotic Liver Disease.": "代謝功能障礙相關脂肪肝疾病嚴重度預測的心臟代謝生物標記",
    "[Recommendations of the German Society for Rheumatology committee for complementary treatment and nutrition on phytotherapy : Supplement on the use of selected phytotherapeutic agents and herbal preparations in rheumatology: extension to include 13 medicinal plants].": "德國風濕病學會補充治療與營養委員會對植物療法的建議：納入 13 種藥用植物的選定植物療法與草藥製劑使用補充",
    "Vitamin D in the UK: an urgent call to redefine the threshold for deficiency.": "英國維生素 D：重新界定缺乏門檻的緊急呼籲",
    "Trimester-specific gestational weight gain and adverse outcomes in GDM women: a retrospective cohort study.": "妊娠期糖尿病女性依孕期分期的體重增加與不良結果：回溯性世代研究",
    "Pratenol B, Eriodictyol, Losbanine, and Isookanin, as potential EGFR and HRAS inhibitors in oral squamous cell carcinoma.": "Pratenol B、Eriodictyol、Losbanine 與 Isookanin 作為口腔鱗狀細胞癌 EGFR 與 HRAS 抑制劑的潛力",
    "Frailty may confound the association between MASLD and cardiovascular mortality in people with cardiometabolic risk factors.": "衰弱可能混淆代謝功能障礙相關脂肪肝與心血管死亡的關聯",
    "Frailty burden and symptomatic BPH/LUTS in aging men: evidence from two nationally representative population-based studies.": "老化男性衰弱負荷與有症狀良性前列腺增生／下泌尿道症狀的關聯：兩項全國代表性人口研究的證據",
    "CYP450 Network Shifts in MASLD/MASH: From Pathogenesis to Nutrition-Informed Modulation.": "MASLD／MASH 的 CYP450 網絡變化：從發病機制到營養導向的調節",
    "Revolutionizing Nutrition: AI-Driven Health Solutions and Personalized Diets.": "營養學的革新：AI 驅動的健康解決方案與個人化飲食",
    "Trace element dynamics following low-calorie formula diet and their association with glycaemic traits.": "低熱量配方飲食後微量元素的變化及其與血糖特徵的關聯",
    "Prognostic Value of the Geriatric Nutritional Risk Index for Long-Term All-Cause Mortality in Older Patients with Non-ST-Segment Elevation Myocardial Infarction.": "老年營養風險指數對非 ST 節段上升型心肌梗塞高齡患者長期全因死亡率的預後價值",
    "Functional fermented foods in public health nutrition: key biomolecular mechanisms, gut microbiota interactions, and implications for metabolic disease prevention.": "公共衛生營養中的功能性發酵食品：關鍵生物分子機制、腸道菌相交互作用與代謝疾病預防意涵",
    "Dietary intake adequacy among Iranian older adults: evidence from national household survey data and two population-based cohorts.": "伊朗高齡者的膳食攝取充足性：全國家戶調查資料與兩項人口世代研究的證據",
    "Sarcopenia and Frailty in COPD: Mechanisms, Relationship with Malnutrition and Potential Therapeutic Interventions.": "COPD 的肌少症與衰弱：機制、與營養不良的關係及潛在治療介入",
    "Efficacy and tolerability of nutraceuticals and phytotherapics for antipsychotic-induced weight gain in schizophrenia spectrum disorders: Systematic review and meta-analysis.": "精神分裂症類群疾病抗精神病藥物引起體重增加的營養保健品與植物療法療效及耐受性：系統性回顧與統合分析",
    "Orexin, Sleep, and Cognition in Alzheimer Disease: Non-REM Oscillatory Activity and Neural Resilience.": "食慾素、睡眠與阿茲海默症認知：非快速眼動睡眠振盪活動與神經韌性",
    "Dietary exposure to food additives in ultra-processed foods: implications for gut microbiome, metabolic health, and risk assessment.": "超加工食品中的食品添加物膳食暴露：對腸道菌相、代謝健康與風險評估的影響",
    "Nutritional Status and Cardiovascular Disease in Older Adults: Clinical Perspectives from Mechanisms to Management.": "高齡者營養狀態與心血管疾病：從機制到管理的臨床觀點",
    "The effects of resistance exercise with blood flow restriction on muscle performance, muscle mass, and function in older adults: a systematic review.": "血流限制阻力運動對高齡者肌肉表現、肌肉量與功能的影響：系統性回顧",
    "Associations between dietary food categories, epigenetic age acceleration and low-grade inflammation in the Lifelines-DEEP cohort.": "Lifelines-DEEP 世代中膳食食物類別、表觀遺傳年齡加速與低度發炎的關聯",
    "Severe Malnutrition in a Young Adult: Diagnostic Challenges in a Multifactorial Case With Helicobacter pylori Infection.": "年輕成人嚴重營養不良：合併幽門螺旋桿菌感染的多因素病例診斷挑戰",
    "Age-related plasma N-glycosylation changes across humans, rats, and mice identify candidate glycan biomarkers for translational aging studies.": "人類、大鼠與小鼠的年齡相關血漿 N-醣基化變化：找出轉譯老化研究的候選醣鏈生物標記",
    "The Development and Validation of the Vegan/Vegetarian Athlete's Plate®.": "純素／素食運動員餐盤的開發與驗證",
    "U-shaped association between non-protein calorie-to-nitrogen ratio and mortality in adults with overweight and obesity: a population-based cohort study.": "非蛋白質熱量與氮比和過重及肥胖成人死亡率的 U 型關聯：人口世代研究",
    "Metabolomic signature of ultra-processed foods and cardiovascular morbidity and mortality.": "超加工食品的代謝體特徵與心血管疾病發生率及死亡率",
    "The health benefits of alkaline water: is it a fact or marketing myth?": "鹼性水的健康效益：事實或行銷迷思",
    "Non-advanced age-related macular degeneration: current concepts and future perspectives.": "非進展性年齡相關黃斑部病變：目前概念與未來觀點",
    "Association between diabetes and elevated circulating advanced oxidation protein products: a comprehensive systematic review and meta-analysis.": "糖尿病與循環中進階氧化蛋白產物升高的關聯：綜合性系統性回顧與統合分析",
    "Sarcopenia and body composition abnormalities in chronic pancreatitis: Pathophysiology, assessment, and clinical impact.": "慢性胰臟炎的肌少症與身體組成異常：病理生理、評估與臨床影響",
  };

  function escapeHtml(value) {
    return String(value == null ? "" : value)
      .replaceAll("&", "&amp;")
      .replaceAll("<", "&lt;")
      .replaceAll(">", "&gt;")
      .replaceAll('"', "&quot;")
      .replaceAll("'", "&#39;");
  }

  function expandSearchTerms(value) {
    const normalized = String(value || "").trim().toLocaleLowerCase("zh-Hant");
    if (!normalized) return [];

    const terms = new Set([normalized]);
    for (const group of SEARCH_GROUPS) {
      const normalizedGroup = group.map((term) => term.toLocaleLowerCase("zh-Hant"));
      if (normalizedGroup.some((term) => normalized.includes(term))) {
        normalizedGroup.forEach((term) => terms.add(term));
      }
    }
    return [...terms];
  }

  function safeUrl(value) {
    try {
      const url = new URL(String(value || ""), window.location.href);
      return url.protocol === "https:" ? url.toString() : "";
    } catch {
      return "";
    }
  }

  function formatDate(value) {
    if (!value) return "尚未標記日期";
    const date = new Date(value);
    if (Number.isNaN(date.getTime())) return "日期未提供";
    return new Intl.DateTimeFormat("zh-Hant-TW", { dateStyle: "medium" }).format(date);
  }

  function kindLabel(kind) {
    return kind === "digest" ? "全文評讀" : "品質評讀";
  }

  function scopeLabel(scope) {
    return scope === "full_text" ? "全文評讀" : "摘要層級評讀，受全文限制";
  }

  function articleKey(item) {
    const doi = String(item.doi || "").trim().toLocaleLowerCase("en-US");
    if (doi) return `doi:${doi}`;
    const title = String(item.title || "").trim().replace(/\s+/g, " ").toLocaleLowerCase("en-US");
    return `title:${title}`;
  }

  function groupItems(items) {
    const groups = new Map();
    for (const item of items) {
      const key = articleKey(item);
      const group = groups.get(key);
      if (group) {
        group.results.push(item);
      } else {
        groups.set(key, { ...item, results: [item] });
      }
    }
    return [...groups.values()];
  }

  function resultItems(item) {
    return Array.isArray(item.results) ? item.results : [item];
  }

  function groupScopeLabel(item) {
    const results = resultItems(item);
    const hasFullText = results.some((result) => result.evidenceScope === "full_text");
    const hasAbstractLevel = results.some((result) => result.evidenceScope !== "full_text");
    if (hasFullText && hasAbstractLevel) return "含全文與摘要評讀";
    return hasFullText ? "全文評讀" : "摘要層級評讀，受全文限制";
  }

  function itemTags(item) {
    return [...new Set(resultItems(item).flatMap((result) => Array.isArray(result.tags) ? result.tags : []))];
  }

  function journalLabel(item) {
    return item.journal || "Journal not provided";
  }

  function sourceTitle(item) {
    return item.title || "Untitled article";
  }

  function hasChinese(value) {
    return [...String(value || "")].some((character) => {
      const codePoint = character.codePointAt(0) || 0;
      return codePoint >= 0x3400 && codePoint <= 0x9fff;
    });
  }

  function normalizeTitle(value) {
    return String(value || "").trim().toLocaleLowerCase("en-US").replace(/\s+/g, " ");
  }

  const topicTitleOverrides = [
    ["Discrepancies between validated", "FFQ 驗證範圍與實際飲食暴露分析"],
    ["The \"Hidden Hunger\" Paradox", "高能量飲食中的隱性飢餓與營養素攝取不足"],
    ["Dietary pattern modifies associations", "飲食型態與飲食因子對表觀遺傳老化速度關聯的修飾"],
    ["Predicting Oral Food Challenge Outcomes", "牛奶過敏兒童口服食物激發試驗結果的預測"],
    ["Expert Consensus on Optimizing the Strategy", "中亞維生素 D 缺乏預防策略的專家共識"],
    ["Effects of inspiratory muscle training", "COPD 吸氣肌訓練對呼吸肌力與運動耐受度的效果"],
    ["Lipid metabolic reprogramming in osteoarthritis", "骨關節炎脂質代謝重編程與軟骨、全關節交互作用"],
    ["Dietary Collagen Supplementation as a Strategy", "膠原蛋白補充對皮膚、頭髮、指甲與傷口癒合的臨床效果"],
    ["Dietary Mineral Intake and Vascular Health", "Long COVID 患者膳食礦物質攝取與血管健康"],
    ["Relationships Between High Dietary Inflammatory Index", "高膳食發炎指數與腸道、血腦屏障完整性的關係"],
    ["Joint assessment of white blood cell-to-HDL", "WHH 與 WHR 聯合指標對心代謝共病風險的評估"],
    ["Cellulite as a Possible Biomarker", "橘皮組織作為代謝功能障礙生物標記的假說"],
    ["Late eating is associated", "非傳染性疾病患者晚餐進食時間與能量攝取、食物群適足性"],
    ["Evaluating online nutrition information", "年輕成人對線上營養資訊可信度的判斷"],
    ["Threshold effect of the METS-VF", "METS-VF 與高血壓成人高尿酸血症的閾值關係"],
    ["Best Evidence Summary on Nutritional Risk", "成人重症患者營養風險篩檢與營養評估的最佳證據"],
    ["Identifying Gastrostomy Care", "ALS 患者與家庭照顧者的胃造口照護與居家管灌教育內容"],
    ["A multidisciplinary virtual", "大腸直腸癌手術的多專業虛擬復健照護模式"],
    ["Integrative Management of Premenstrual", "經前不悅症的整合管理與傳統中醫角色"],
    ["Clinical efficacy of Jianqiao ancient moxibustion", "肩橋古法艾灸治療慢性疲勞症候群的臨床試驗計畫"],
    ["Shiyiwei Shenqi Pian-derived quercetin", "沈氏參芪片來源槲皮素對透明細胞腎癌凋亡的作用"],
    ["Male fertility as an integral reflection", "男性生育力與代謝、內分泌及肌肉骨骼健康的關聯"],
    ["Association between dietary inflammatory index", "日本第二型糖尿病成人膳食發炎指數、肥胖與飲食攝取"],
    ["Integrating executive function training", "幼兒肥胖預防的執行功能訓練與健康行為介入整合"],
    ["Effect of Carbohydrate-Restricted Dietary Patterns", "過重與肥胖成人碳水化合物限制飲食型態的系統性回顧"],
    ["Anthocyanins and Aging Intervention", "花青素介入與老化的機轉及發展方向"],
    ["Systems approach to integrative oncology", "乳癌整合腫瘤照護的系統設計、服務提供與患者經驗"],
    ["Metabolic syndrome is associated", "代謝症候群與腦部加速老化的關聯"],
    ["Metabolomic Profiles Associated With Sugary", "青少年含糖飲料攝取相關的代謝體特徵"],
    ["Impact of Obesity on the Association", "肥胖對鹽分攝取與高血壓男性血壓關聯的影響"],
    ["Defining a ketone threshold", "減重用酮體閾值與生酮飲食者 14 天 β-羥基丁酸監測"],
    ["Food-Based Antioxidant Nutrition", "食物型抗氧化營養對運動恢復與訓練適應的策略"],
    ["Dietary and nutritional supplementation strategies for table tennis", "桌球運動員飲食與營養補充策略"],
    ["Clinical evidence for fat-binding-mediated", "RODLTM 植物複方促進限制飲食下糞便脂肪排出的臨床證據"],
    ["German and Roman Chamomile", "德國洋甘菊與羅馬洋甘菊的植化素及機能性食品應用"],
    ["A path to sustainable and healthy diets", "卵奶素食物型飲食指引與永續健康飲食模型"],
    ["Age-related plasma N-glycosylation", "人類、大鼠與小鼠的年齡相關血漿 N-醣基化變化與老化生物標記"],
    ["The Development and Validation of the Vegan", "素食運動員餐盤的建立與驗證"],
    ["U-shaped association between non-protein", "過重與肥胖成人非蛋白熱量氮比與死亡風險的 U 型關聯"],
    ["Metabolomic signature of ultra-processed", "超加工食品的代謝體特徵與心血管發病、死亡"],
    ["The health benefits of alkaline water", "鹼性水的健康效益：事實或行銷迷思"],
    ["Non-advanced age-related macular degeneration", "非進展型年齡相關黃斑部病變的現代理解與展望"],
    ["Association between diabetes and elevated", "糖尿病與循環高濃度高級氧化蛋白產物的關聯"],
    ["Sarcopenia and body composition abnormalities", "慢性胰臟炎的肌少症與身體組成異常"],
  ];

  function topicTitleForSource(sourceTitle) {
    const normalized = normalizeTitle(sourceTitle);
    return topicTitleOverrides.find(([pattern]) => normalized.includes(normalizeTitle(pattern)))?.[1] || "";
  }

  function topicTitleFromContent(value) {
    const lines = stripFrontMatter(value).split(/\r?\n/).map((line) => line.trim());
    for (const line of lines) {
      if (!hasChinese(line) || /^(#|[-*>]|\|)/.test(line) || line.length < 8) continue;
      const sentence = line.split(/[。！？]/)[0].trim();
      if (sentence.length >= 8) return sentence.slice(0, 36);
    }
    return "";
  }

  function stripFrontMatter(value) {
    const text = String(value || "").trim();
    return text.startsWith("---")
      ? text.replace(/^---\s*\r?\n[\s\S]*?\r?\n---\s*\r?\n?/, "").trim()
      : text;
  }

  function noteHeading(item, sourceTitle) {
    const noteTitle = String(item.noteTitle || "").trim();
    const kindNoteLabel = item.kind === "digest" ? "內容整理" : "品質評讀";
    const genericLabels = new Set([
      "品質評讀",
      "內容整理",
      "全文評讀",
      "摘要層級評讀",
      "品質評讀筆記",
      "內容整理筆記",
      "全文評讀筆記",
    ]);
    if (noteTitle && !genericLabels.has(noteTitle)) {
      const directLabelMatch = noteTitle.match(/^(品質評讀|內容整理|全文評讀)\s*[:：]\s*(.+)$/);
      const directSuffix = directLabelMatch?.[2]?.trim() || "";
      if (directLabelMatch) {
        if (hasChinese(directSuffix) && normalizeTitle(sourceTitle) !== normalizeTitle(directSuffix)) {
          if (/(品質評讀|全文評讀|內容整理|全文內容整理)(筆記)?$/.test(directSuffix)) return directSuffix;
          return `${directSuffix}的${kindNoteLabel}`;
        }
      } else if (hasChinese(noteTitle)) {
        return noteTitle;
      }
    }
    const mappedTopic = topicTitleForSource(sourceTitle);
    if (mappedTopic) return `${mappedTopic}的${kindNoteLabel}`;
    const candidates = [
      ...(stripFrontMatter(item.content).match(/^#\s+(.+)$/gm) || []).map((heading) => heading.replace(/^#\s+/, "").trim()),
    ];
    for (const candidate of candidates) {
      const labelMatch = candidate.match(/^(品質評讀|內容整理|全文評讀)\s*[:：]\s*(.+)$/);
      if (labelMatch) {
        const suffix = labelMatch[2].trim();
        if (!hasChinese(suffix) || normalizeTitle(sourceTitle) === normalizeTitle(suffix)) {
          continue;
        }
        if (/(品質評讀|全文評讀|內容整理|全文內容整理)(筆記)?$/.test(suffix)) return suffix;
        return `${suffix}的${kindNoteLabel}`;
      }
      if (hasChinese(candidate)) return candidate;
    }
    const contentTopic = topicTitleFromContent(item.content);
    if (contentTopic) return `${contentTopic}的${kindNoteLabel}`;
    return `${kindNoteLabel}筆記`;
  }

  function readingSummaryLabel(item, sourceTitle) {
    return `繁體中文筆記：${noteHeading(item, sourceTitle)}`;
  }

  function itemText(item) {
    const results = resultItems(item);
    return [
      item.title,
      sourceTitle(item),
      item.authors,
      item.journal,
      journalLabel(item),
      item.year,
      item.doi,
      item.abstract,
      item.category,
      itemTags(item).join(" "),
      results.flatMap((result) => [
        result.kind,
        result.noteTitle,
        noteHeading(result, item.title),
        stripFrontMatter(result.content),
        Array.isArray(result.cards) ? result.cards.flatMap((card) => [card.title, card.question, card.answer]) : [],
      ]),
    ].join(" ").toLocaleLowerCase("zh-Hant");
  }

  function filteredItems() {
    const terms = expandSearchTerms(state.query);
    return state.items.filter((item) => {
      if (state.kind !== "all" && !resultItems(item).some((result) => result.kind === state.kind)) return false;
      const searchable = itemText(item);
      return !terms.length || terms.some((term) => searchable.includes(term));
    });
  }

  function link(label, url) {
    const safe = safeUrl(url);
    return safe ? `<a class="paper-link" href="${escapeHtml(safe)}" target="_blank" rel="noopener noreferrer">${label}</a>` : "";
  }

  function renderTags(tags) {
    if (!Array.isArray(tags) || !tags.length) return "";
    return `<div class="paper-tags">${tags.map((tag) => `<span>${escapeHtml(tag)}</span>`).join("")}</div>`;
  }

  function renderCards(cards) {
    if (!Array.isArray(cards) || !cards.length) return "";
    const cardsHtml = cards.map((card, index) => `
      <article class="quiz-card">
        <span class="quiz-number">${index + 1}</span>
        <div>
          <h4>${escapeHtml(card.title || `理解卡 ${index + 1}`)}</h4>
          <p><strong>問題</strong>${escapeHtml(card.question)}</p>
          <details><summary>查看答案</summary><p>${escapeHtml(card.answer)}</p></details>
        </div>
      </article>`).join("");
    return `<details class="paper-section"><summary>自我測驗（${cards.length} 張）</summary><div class="quiz-list">${cardsHtml}</div></details>`;
  }

  function renderResult(result, sourceTitle) {
    const noteBody = stripFrontMatter(result.content);
    return `
        <details class="paper-section paper-note-section">
          <summary><span class="paper-note-summary-title">${escapeHtml(readingSummaryLabel(result, sourceTitle))}</span><span>${escapeHtml(formatDate(result.completedAt))}</span></summary>
          <div class="paper-note">${escapeHtml(noteBody || "目前沒有可顯示的中文筆記內容。")}</div>
          ${renderCards(result.cards)}
        </details>`;
  }

  function renderItem(item) {
    const results = resultItems(item).slice().sort((left, right) => {
      const order = { review: 0, digest: 1 };
      return (order[left.kind] ?? 9) - (order[right.kind] ?? 9);
    });
    const kindBadges = [...new Set(results.map((result) => kindLabel(result.kind)))].map((label) => `<span>${escapeHtml(label)}</span>`).join("");
    const displayTitle = sourceTitle(item);
    const displayJournal = journalLabel(item);
    const tags = renderTags(itemTags(item));
    const fullTextLink = link("合法全文", item.legalFullTextUrl);
    const sourceLink = link("來源頁面", item.sourceUrl);
    const doiLink = item.doi ? `<a class="paper-link" href="https://doi.org/${encodeURIComponent(item.doi)}" target="_blank" rel="noopener noreferrer">DOI</a>` : "";
    const resultSections = results.map((result) => renderResult(result, displayTitle)).join("");
    return `
      <article class="paper-card">
        <header class="paper-card-head">
          <div>
            <div class="paper-kicker">${kindBadges}<span>${escapeHtml(item.category || "未分類")}</span></div>
            <div class="paper-source-label">原文（English）</div>
            <h2>${escapeHtml(displayTitle)}</h2>
          </div>
          <span class="paper-scope">${escapeHtml(groupScopeLabel(item))}</span>
        </header>
        <p class="paper-authors">${escapeHtml(item.authors || "作者資料未提供")}</p>
        <div class="paper-meta"><span>${escapeHtml(displayJournal)}</span><span>${escapeHtml(item.year || "年份未提供")}</span><span>${escapeHtml(item.doi || "DOI 未提供")}</span></div>
        ${item.abstract ? `<details class="paper-section paper-abstract-section"><summary><span class="paper-note-summary-title">查看摘要</span><span>Abstract</span></summary><p class="paper-abstract"><span class="paper-language-label">Abstract</span>${escapeHtml(item.abstract)}</p></details>` : ""}
        ${tags}
        <div class="paper-links">${fullTextLink}${sourceLink}${doiLink}</div>
        ${resultSections}
      </article>`;
  }

  function renderPagination(totalPages, currentPage, total) {
    if (!total) {
      elements.pagination.innerHTML = "";
      return;
    }
    const firstItem = (currentPage - 1) * PAGE_SIZE + 1;
    const lastItem = Math.min(currentPage * PAGE_SIZE, total);
    const pageButtons = totalPages > 1 ? `
      <div class="page-buttons">
        <button type="button" data-page="${currentPage - 1}" ${currentPage === 1 ? "disabled" : ""}>上一頁</button>
        ${Array.from({ length: totalPages }, (_, index) => index + 1).map((page) => `<button type="button" class="${page === currentPage ? "active" : ""}" data-page="${page}" aria-label="第 ${page} 頁" ${page === currentPage ? 'aria-current="page"' : ""}>${page}</button>`).join("")}
        <button type="button" data-page="${currentPage + 1}" ${currentPage === totalPages ? "disabled" : ""}>下一頁</button>
      </div>` : "";
    elements.pagination.innerHTML = `<div class="page-summary">顯示第 ${firstItem} 至 ${lastItem} 筆，共 ${total} 筆</div>${pageButtons}`;
    elements.pagination.querySelectorAll("button[data-page]").forEach((button) => {
      button.addEventListener("click", () => {
        if (button.disabled) return;
        state.page = Number(button.dataset.page) || 1;
        render();
        window.scrollTo({ top: elements.list.offsetTop - 24, behavior: "smooth" });
      });
    });
  }

  function render() {
    const visible = filteredItems();
    const totalPages = Math.max(1, Math.ceil(visible.length / PAGE_SIZE));
    state.page = Math.min(state.page, totalPages);
    const start = (state.page - 1) * PAGE_SIZE;
    const current = visible.slice(start, start + PAGE_SIZE);
    elements.list.innerHTML = current.length
      ? current.map(renderItem).join("")
      : `<div class="paper-empty"><strong>目前沒有符合條件的公開論文</strong><span>可換一組搜尋詞，或切換成果類型。</span></div>`;
    elements.status.textContent = visible.length ? `顯示第 ${start + 1} 至 ${Math.min(start + PAGE_SIZE, visible.length)} 筆，共 ${visible.length} 篇公開論文` : "目前沒有符合條件的公開論文";
    renderPagination(totalPages, state.page, visible.length);
  }

  function updateStats() {
    elements.totalCount.textContent = String(state.items.length);
    elements.reviewCount.textContent = String(state.items.filter((item) => resultItems(item).some((result) => result.kind === "review")).length);
    elements.digestCount.textContent = String(state.items.filter((item) => resultItems(item).some((result) => result.kind === "digest")).length);
  }

  async function load() {
    try {
      const response = await fetch("./data/papers-public.json", { cache: "no-store" });
      if (!response.ok) throw new Error("data unavailable");
      const data = await response.json();
      if (!data || data.schemaVersion !== 1 || !Array.isArray(data.papers)) throw new Error("invalid data");
      state.items = groupItems(data.papers.filter((item) => item && ["review", "digest"].includes(item.kind)));
      elements.updatedAt.textContent = data.generatedAt ? `更新於 ${formatDate(data.generatedAt)}` : "已載入公開資料";
      updateStats();
      render();
    } catch {
      elements.status.textContent = "公開資料暫時無法讀取，請稍後再試。";
      elements.list.innerHTML = `<div class="paper-empty"><strong>資料載入失敗</strong><span>頁面本身仍可開啟，請稍後重新整理。</span></div>`;
    }
  }

  elements.query.addEventListener("input", (event) => {
    state.query = event.target.value;
    state.page = 1;
    render();
  });

  document.querySelectorAll("[data-kind]").forEach((button) => {
    button.addEventListener("click", () => {
      state.kind = button.dataset.kind;
      state.page = 1;
      document.querySelectorAll("[data-kind]").forEach((item) => item.classList.toggle("active", item === button));
      render();
    });
  });

  load();
}());
