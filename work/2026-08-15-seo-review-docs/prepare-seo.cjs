const fs = require('fs');
const path = require('path');

const root = path.resolve(__dirname, '..', '..');
const outputDir = path.join(__dirname, 'source');
const attachmentPath = 'C:/Users/cygnu/.codex/attachments/b36265b7-7140-4a93-8e87-17f2708b4066/pasted-text.txt';

function readUtf8(filePath) {
  return fs.readFileSync(filePath, 'utf8');
}

function writeUtf8(filePath, value) {
  fs.writeFileSync(filePath, value, 'utf8');
}

function escapeHtml(value) {
  return String(value)
    .replace(/&/g, '&amp;')
    .replace(/</g, '&lt;')
    .replace(/>/g, '&gt;')
    .replace(/"/g, '&quot;')
    .replace(/'/g, '&#039;');
}

function chapterLabel(value) {
  const chinese = ['零', '一', '二', '三', '四', '五', '六', '七', '八', '九', '十', '十一', '十二', '十三', '十四', '十五'];
  return String(value).replace(/\bChapter\s+(\d{1,2})\b/g, (match, number) => `第${chinese[Number(number)] || number}章`);
}

function editorialRules(value) {
  return chapterLabel(String(value))
    .replace(/\bControversy\b/g, '爭議')
    .replace(/先(?:說|給)答案：/g, '**省時版本：**')
    .replace(/(第[一二三四五六七八九十百]+章) 的/g, '$1的');
}

function editorialHtmlRules(value) {
  return chapterLabel(String(value))
    .replace(/\bControversy\b/g, '爭議')
    .replace(/先(?:說|給)答案：/g, '<strong>省時版本：</strong>')
    .replace(/(第[一二三四五六七八九十百]+章) 的/g, '$1的');
}

function markdownInline(value) {
  let text = escapeHtml(value);
  text = text.replace(/\[([^\]]+)\]\((https?:\/\/[^)]+)\)/g, (_match, label, url) => {
    const external = !url.startsWith('https://594katchang-source.github.io/');
    const attrs = external ? ' target="_blank" rel="noopener"' : '';
    return `<a href="${url}"${attrs}>${label}</a>`;
  });
  text = text.replace(/\*\*([^*]+)\*\*/g, '<strong>$1</strong>');
  text = text.replace(/__([^_]+)__/g, '<strong>$1</strong>');
  return text;
}

function parseTable(lines, start) {
  const rows = [];
  let cursor = start;
  while (cursor < lines.length && lines[cursor].includes('\t')) {
    rows.push(lines[cursor].split('\t').map(cell => cell.trim()));
    cursor += 1;
  }
  if (rows.length < 2) return null;
  const header = rows[0];
  const body = rows.slice(1);
  const headHtml = `<thead><tr>${header.map(cell => `<th>${markdownInline(cell)}</th>`).join('')}</tr></thead>`;
  const bodyHtml = `<tbody>${body.map(row => `<tr>${header.map((_cell, index) => `<td>${markdownInline(row[index] || '')}</td>`).join('')}</tr>`).join('')}</tbody>`;
  return { html: `<table>${headHtml}${bodyHtml}</table>`, next: cursor };
}

const chapter2Headings = new Set([
  '先分清楚：DRI 每個縮寫在處理什麼問題？',
  '從數字走到餐桌：台灣讀者先看六大類食物',
  '一餐怎麼判斷？',
  '營養密度怎麼用？同時看營養、熱量與份量',
  '食品標籤怎麼看？四步驟先抓到真正吃進去的量',
  '標示上的「健康」兩個字要怎麼拆？',
  '「超級食物」真的比較強嗎？先看食物型態，再看單一成分',
  '一週實作：用五個小任務練習讀懂自己的飲食',
  '常見錯誤與修正',
  '哪些情況需要營養師或醫師評估？',
  'Kat Chang 營養師的判讀',
  '結語'
]);

function buildChapter2Body(draft) {
  const start = draft.indexOf('正文');
  const end = draft.indexOf('SEO 描述');
  const bodyText = draft.slice(start + '正文'.length, end).trim();
  const lines = editorialRules(bodyText).split(/\r?\n/);
  const blocks = [];
  let cursor = 0;
  let skippedTitle = false;

  while (cursor < lines.length) {
    const raw = lines[cursor].trim();
    if (!raw) {
      cursor += 1;
      continue;
    }
    if (!skippedTitle) {
      skippedTitle = true;
      cursor += 1;
      continue;
    }
    const table = parseTable(lines, cursor);
    if (table) {
      blocks.push(table.html);
      cursor = table.next;
      continue;
    }
    if (chapter2Headings.has(raw)) {
      blocks.push(`<h2>${markdownInline(raw)}</h2>`);
      cursor += 1;
      continue;
    }
    if (/^[-*]\s+/.test(raw)) {
      const items = [];
      while (cursor < lines.length && /^[-*]\s+/.test(lines[cursor].trim())) {
        items.push(`<li>${markdownInline(lines[cursor].trim().replace(/^[-*]\s+/, ''))}</li>`);
        cursor += 1;
      }
      blocks.push(`<ul>${items.join('')}</ul>`);
      continue;
    }
    if (/^\d+[.)]\s+/.test(raw)) {
      const items = [];
      while (cursor < lines.length && /^\d+[.)]\s+/.test(lines[cursor].trim())) {
        items.push(`<li>${markdownInline(lines[cursor].trim().replace(/^\d+[.)]\s+/, ''))}</li>`);
        cursor += 1;
      }
      blocks.push(`<ol>${items.join('')}</ol>`);
      continue;
    }
    const paragraph = [raw];
    cursor += 1;
    while (cursor < lines.length) {
      const next = lines[cursor].trim();
      if (!next || chapter2Headings.has(next) || next.includes('\t') || /^[-*]\s+/.test(next) || /^\d+[.)]\s+/.test(next)) break;
      paragraph.push(next);
      cursor += 1;
    }
    blocks.push(`<p>${paragraph.map(markdownInline).join('<br>')}</p>`);
  }

  const internalLinks = '<p>延伸閱讀：<a href="https://594katchang-source.github.io/blog/post.html?id=2026-08-13-nutrition-concepts-controversies-17e-guide">全書導讀</a>、<a href="https://594katchang-source.github.io/blog/post.html?id=2026-08-14-food-choices-human-health-guide">第一章食物選擇</a>、<a href="https://594katchang-source.github.io/blog/">Blog 文章列表</a>、<a href="https://594katchang-source.github.io/about.html">作者簡介</a>、<a href="https://594katchang-source.github.io/teach/paper-radar/">論文讀書小站</a>。</p>';
  const insertBefore = '<h2>Kat Chang 營養師的判讀</h2>';
  const html = blocks.join('\n');
  return html.includes(insertBefore) ? html.replace(insertBefore, `${internalLinks}\n${insertBefore}`) : `${html}\n${internalLinks}`;
}

function visibleText(html) {
  return String(html)
    .replace(/<script[\s\S]*?<\/script>/gi, ' ')
    .replace(/<style[\s\S]*?<\/style>/gi, ' ')
    .replace(/<[^>]+>/g, ' ')
    .replace(/&amp;/g, '&')
    .replace(/&lt;/g, '<')
    .replace(/&gt;/g, '>')
    .replace(/&quot;/g, '"')
    .replace(/&#039;/g, "'")
    .replace(/\s+/g, ' ')
    .trim();
}

function countText(html) {
  const text = visibleText(html);
  return { characters: text.length, words: text.split(/\s+/).filter(Boolean).length };
}

const postsPath = path.join(root, 'blog', 'posts.json');
const postsData = JSON.parse(readUtf8(postsPath));
const draft = readUtf8(attachmentPath);
const chapter2Body = buildChapter2Body(draft);

for (const post of postsData.posts) {
  post.title = editorialRules(post.title);
  post.excerpt = editorialRules(post.excerpt);
  post.body = editorialHtmlRules(post.body);
}

const chapter1 = postsData.posts.find(post => post.id === '2026-08-14-food-choices-human-health-guide');
if (!chapter1) throw new Error('Chapter 1 post not found');
chapter1.slug = chapter1.slug || chapter1.id;
chapter1.category = chapter1.category || '營養學概念與爭論';
chapter1.tags = chapter1.tags || chapter1.keywords;
chapter1.faq = chapter1.faq || [];

const chapter2Id = '2026-08-15-nutrition-tools-standards-guidelines';
const chapter2 = {
  id: chapter2Id,
  slug: chapter2Id,
  title: '第二章：DRI、營養標示怎麼看？用六大類食物讀懂營養數字與超級食物迷思',
  date: '2026-08-15',
  category: '營養學概念與爭論',
  tags: ['DRI', '營養標示', '六大類食物', '營養密度', '超級食物', '植化素', '健康飲食'],
  excerpt: 'DRI、RDA、AI、UL、每日參考值怎麼看？凱特營養師以《Nutrition Concepts & Controversies》第 17 版第二章為基礎，整理台灣六大類食物、食品標籤與超級食物判讀方法。',
  keywords: ['DRI', '營養標示', '每日參考值', '營養密度', '超級食物', '六大類食物'],
  showOnHome: false,
  body: chapter2Body
};
const existingChapter2 = postsData.posts.findIndex(post => post.id === chapter2Id);
if (existingChapter2 >= 0) postsData.posts[existingChapter2] = chapter2;
else postsData.posts.splice(2, 0, chapter2);
writeUtf8(postsPath, `${JSON.stringify(postsData, null, 2)}\n`);

const sitemapPath = path.join(root, 'sitemap.xml');
let sitemap = readUtf8(sitemapPath);
const chapter1Sitemap = '<url><loc>https://594katchang-source.github.io/blog/post.html?id=2026-08-14-food-choices-human-health-guide</loc><lastmod>2026-08-14</lastmod><changefreq>monthly</changefreq><priority>0.8</priority></url>';
const chapter1SitemapUpdated = chapter1Sitemap.replace('2026-08-14</lastmod>', '2026-08-15</lastmod>');
sitemap = sitemap.replace(chapter1Sitemap, chapter1SitemapUpdated);
const chapter2Sitemap = '<url><loc>https://594katchang-source.github.io/blog/post.html?id=2026-08-15-nutrition-tools-standards-guidelines</loc><lastmod>2026-08-15</lastmod><changefreq>monthly</changefreq><priority>0.8</priority></url>';
if (!sitemap.includes('id=2026-08-15-nutrition-tools-standards-guidelines')) sitemap = sitemap.replace('</urlset>', `  ${chapter2Sitemap}\n</urlset>`);
writeUtf8(sitemapPath, sitemap);

const llmsPath = path.join(root, 'llms.txt');
let llms = readUtf8(llmsPath);
llms = editorialRules(llms);
const chapter2Llms = '- 第二章：DRI、營養標示怎麼看？用六大類食物讀懂營養數字與超級食物迷思：https://594katchang-source.github.io/blog/post.html?id=2026-08-15-nutrition-tools-standards-guidelines';
if (!llms.includes('id=2026-08-15-nutrition-tools-standards-guidelines')) llms = llms.replace(/(## 最新文章\r?\n\r?\n)/, `$1${chapter2Llms}\n`);
writeUtf8(llmsPath, llms);

const chapter1Review = {
  reviewTitle: '第一章待審 SEO 草稿',
  seoTitle: chapter1.title,
  targetTerms: ['食物選擇', '健康飲食', '營養密度', '飲食行為', '營養資訊判讀'],
  relatedTerms: ['適足', '均衡', '適量', '多樣', '六大類食物', '保健食品', '行為改變', '營養資訊查核'],
  searchIntent: '讀者想知道食物選擇如何影響健康，並需要一套能放進外食、家庭飲食與營養資訊查核的判斷方法。',
  summary: chapter1.excerpt,
  opening: '每天都要吃飯，卻很少有人能靠一張固定菜單處理所有生活情境。第一章的核心答案是：食物選擇會在一段時間內累積影響健康，判斷飲食品質時，要看整體型態、營養是否足夠、食物搭配、份量與頻率，也要把活動、睡眠、壓力、基因、收入與食物取得放進來。',
  articleTitle: chapter1.title,
  bodyHtml: chapter1.body,
  seoDescription: chapter1.excerpt,
  category: chapter1.category,
  tags: chapter1.tags,
  slug: chapter1.slug,
  canonical: `https://594katchang-source.github.io/blog/post.html?id=${chapter1.slug}`,
  internalLinks: [
    ['全書導讀', 'https://594katchang-source.github.io/blog/post.html?id=2026-08-13-nutrition-concepts-controversies-17e-guide'],
    ['超商早餐怎麼搭才更穩定', 'https://594katchang-source.github.io/blog/post.html?id=sample-balanced-breakfast'],
    ['作者簡介', 'https://594katchang-source.github.io/about.html'],
    ['Blog 文章列表', 'https://594katchang-source.github.io/blog/'],
    ['論文讀書小站', 'https://594katchang-source.github.io/teach/paper-radar/']
  ],
  faq: (chapter1.faq || []).map(item => item.question),
  faqSchema: '使用 FAQPage 結構化資料，公開正文需完整呈現每題與答案。',
  articleSchema: ['BlogPosting', 'headline', 'description', 'author', 'datePublished: 2026-08-14', 'dateModified: 2026-08-15', 'mainEntityOfPage', 'image', 'articleSection', 'keywords'],
  author: '張雁雲營養師，Kat Chang 凱特營養師，專長為高齡營養、疾病營養、精準營養與健康促進。',
  sources: [
    ['第一章整理 DOCX', 'D:/@Codex/書籍/2026-07-29-Nutrition-Concepts-Controversies-17e/output/chapter-01-food-choices-human-health.docx', '第一章核心概念、食物選擇、營養密度與行為改變'],
    ['第一章全文擷取檔', 'D:/@Codex/書籍/2026-07-29-Nutrition-Concepts-Controversies-17e/process/chapter-01-source.txt', '原章節逐頁內容與頁碼核對'],
    ['WHO Healthy diet', 'https://www.who.int/en/news-room/fact-sheets/detail/healthy-diet', '健康飲食原則與飲食型態限制'],
    ['WHO Physical activity', 'https://www.who.int/news-room/fact-sheets/detail/physical-activity?c=MY2024', '身體活動量的衛教背景'],
    ['NIH ODS Dietary Supplements', 'https://ods.od.nih.gov/factsheets/dietarysupplements-Consumer/', '補充品用途、限制與安全判讀'],
    ['營養資訊品質回顧', 'https://pubmed.ncbi.nlm.nih.gov/37138366/', '線上營養資訊品質與查核必要性'],
    ['營養錯誤資訊回顧', 'https://pubmed.ncbi.nlm.nih.gov/40008658/', '奇蹟飲食與快速健康宣稱的資訊風險'],
    ['全國法規資料庫《營養師法》', 'https://law.moj.gov.tw/LawClass/LawAll.aspx?pcode=L0040006', '營養師名稱與執業規範'],
    ['NHS Food Allergy', 'https://www.nhs.uk/conditions/food-allergy/', '嚴重過敏症狀與就醫提醒']
  ],
  originalClaims: [
    '把第一章的食物選擇與健康行為概念轉成台灣外食、家庭飲食與預算情境。',
    '以適足、均衡、適量、多樣四個檢查詞，建立一餐到一週的自我檢查流程。',
    '把營養密度、行為目標、資訊查核與補充品安全放在同一套生活判讀路線。',
    '清楚區分一般營養教育與疾病、用藥、吞嚥、過敏等需要專業評估的情況。'
  ],
  pending: ['正式發布後仍需重新核對公開頁面的 FAQPage、canonical、封面圖與手機寬度。', '本文不取代診斷、檢驗或治療。'],
  wordCount: countText(chapter1.body)
};

const chapter2Review = {
  reviewTitle: '第二章待審 SEO 草稿',
  seoTitle: 'DRI、營養標示怎麼看？用六大類食物讀懂營養數字與超級食物迷思',
  targetTerms: ['DRI 是什麼', '營養標示怎麼看', '每日參考值', '營養密度', '超級食物', '六大類食物'],
  relatedTerms: ['RDA', 'AI', 'EAR', 'UL', 'AMDR', 'CDRR', 'Daily Values', '5/20 Rule', '食品標籤', '植化素補充品', '台灣每日飲食指南'],
  searchIntent: '讀者想知道營養標準的差異、包裝食品標籤的閱讀順序，以及超級食物與補充品宣稱該如何判斷。',
  summary: chapter2.excerpt,
  opening: '省時版本：營養標準是拿來協助判斷的工具，不要求每個人每天精準達成固定分數。DRI 裡的 RDA、AI、EAR、UL、AMDR、CDRR，各有不同用途。食品包裝上的每日參考值百分比，適合做快速比較，不能直接當成個人需求。',
  articleTitle: 'DRI、營養標示怎麼看？用六大類食物讀懂營養數字與「超級食物」迷思',
  bodyHtml: chapter2Body,
  seoDescription: 'DRI、RDA、AI、UL、每日參考值怎麼看？凱特營養師以《Nutrition Concepts & Controversies》第 17 版第二章為基礎，整理台灣六大類食物、食品標籤與超級食物判讀方法。',
  category: '營養學概念與爭論',
  tags: ['DRI', '營養標示', '六大類食物', '營養密度', '超級食物', '植化素', '健康飲食'],
  slug: chapter2Id,
  canonical: `https://594katchang-source.github.io/blog/post.html?id=${chapter2Id}`,
  internalLinks: [
    ['全書導讀', 'https://594katchang-source.github.io/blog/post.html?id=2026-08-13-nutrition-concepts-controversies-17e-guide'],
    ['第一章食物選擇', 'https://594katchang-source.github.io/blog/post.html?id=2026-08-14-food-choices-human-health-guide'],
    ['Blog 文章列表', 'https://594katchang-source.github.io/blog/'],
    ['作者簡介', 'https://594katchang-source.github.io/about.html'],
    ['論文讀書小站', 'https://594katchang-source.github.io/teach/paper-radar/']
  ],
  faq: ['DRI、RDA、AI、EAR、UL 有什麼差別？', '5/20 Rule 可以直接用在台灣食品標籤嗎？', '2,000 kcal 飲食型態適合每個人嗎？', '超級食物真的比一般食物更有用嗎？', '哪些人使用營養補充品前應先諮詢專業人員？'],
  faqSchema: '建議使用 FAQPage 結構化資料，前提是問題與答案完整出現在公開正文。',
  articleSchema: ['BlogPosting', 'headline', 'description', 'author', 'datePublished: 2026-08-15', 'dateModified: 2026-08-15', 'mainEntityOfPage', 'image', 'articleSection', 'keywords'],
  author: '張雁雲營養師，Kat Chang 凱特營養師，專長為高齡營養、疾病營養、精準營養、健康促進。',
  sources: [
    ['第二章整理 DOCX', 'D:/@Codex/書籍/2026-07-29-Nutrition-Concepts-Controversies-17e/output/chapter-02-nutrition-tools-standards-and-guidelines.docx', 'DRI、Daily Values、USDA Dietary Patterns、營養密度、標籤、植化素與爭議 2'],
    ['第二章全文擷取檔', 'D:/@Codex/書籍/2026-07-29-Nutrition-Concepts-Controversies-17e/process/chapter-02-source.txt', 'PDF 第 58 至 93 頁的逐頁原文'],
    ['國健署第八版 DRIs', 'https://www.hpa.gov.tw/Pages/Detail.aspx?kv=default&lottery=NnNicDZvK2lCZFF6cW5SSXYzY3dsUT09&nodeid=4248&pid=12285', '台灣營養素參考攝取量與特殊需求提醒'],
    ['國健署每日飲食指南', 'https://www.hpa.gov.tw/pages/ebook.aspx?nodeid=1208', '六大類食物、熱量需求與台灣飲食轉譯'],
    ['國健署六大類食物', 'https://www.hpa.gov.tw/Pages/List.aspx?nodeid=4086', '台灣常見食物、份量與選擇方向'],
    ['食藥署包裝食品營養標示規定', 'https://www.fda.gov.tw/TC/newsContent.aspx?cid=3&id=28026', '每份量、包裝份數、營養素含量與每日參考值百分比'],
    ['食藥署健康食品概說', 'https://www.fda.gov.tw/tc/siteContent.aspx?sid=1776', '健康食品法律定義與宣稱限制'],
    ['NIH ODS DRI 說明', 'https://ods.od.nih.gov/HealthInformation/nutrientrecommendations/', 'RDA、AI、EAR、UL 與 Daily Values 定義'],
    ['WHO Healthy Diet', 'https://www.who.int/news-room/fact-sheets/detail/healthy-diet', '適足、均衡、節制、多樣與食品安全原則'],
    ['PubMed 飲食型態系統性回顧', 'https://pubmed.ncbi.nlm.nih.gov/35258870/', '高營養密度飲食型態與健康結果的研究整理，並標示觀察性研究限制'],
    ['NCCIH 綠茶安全資料', 'https://www.nccih.nih.gov/health/green-tea', '綠茶萃取補充品與肝損傷風險'],
    ['NCCIH 益生菌安全資料', 'https://www.nccih.nih.gov/health/probiotics-usefulness-and-safety', '益生菌在免疫功能低下或虛弱族群的安全限制']
  ],
  originalClaims: [
    '把美國教材中的營養標準改寫成台灣讀者能使用的判讀流程。',
    '明確區分美國 5/20 Rule 與台灣食品標示制度。',
    '用六大類食物、標籤四步驟與 7 日練習，讓文章能直接轉成生活行動。',
    '將超級食物放回食物型態、劑量、產品形式與安全風險判斷。',
    '把高齡、慢性病、用藥、吞嚥與補充品安全納入文章限制。'
  ],
  pending: ['FAQPage 建議要等公開正文補上完整問答後再啟用。', '正式發布後仍需重新核對公開頁面的 canonical、文章結構化資料、站內連結與手機寬度。', '本文不取代診斷、檢驗或治療。'],
  wordCount: countText(chapter2Body)
};

writeUtf8(path.join(outputDir, 'chapter-1-review.json'), `${JSON.stringify(chapter1Review, null, 2)}\n`);
writeUtf8(path.join(outputDir, 'chapter-2-review.json'), `${JSON.stringify(chapter2Review, null, 2)}\n`);
writeUtf8(path.join(outputDir, 'chapter-2-review-source.txt'), editorialRules(draft));

console.log(JSON.stringify({
  posts: postsData.posts.map(post => ({ id: post.id, title: post.title, showOnHome: post.showOnHome, bodyCharacters: countText(post.body).characters })),
  chapter1: chapter1Review.wordCount,
  chapter2: chapter2Review.wordCount,
  internalLinks: chapter2Review.internalLinks
}, null, 2));
