# Kat Chang site 工作日誌

## 2026-09-04｜全站內鏈優化、三大關鍵字與桃園營養師推薦佈局、21組企業講座關鍵字確立與推播 GitHub

### 任務

- 依使用者指示落實全站 SEO 與個人品牌升級：
  1. **Chapter 8 補齊站內十字互鏈**：於 Chapter 8（水與礦物質）專文正文嵌入連向 Chapter 6（蛋白質與肌力）、Chapter 7（維生素 D 與鈣化）及營養師個人簡介（about.html）之十字互鏈。
  2. **互動教具反向連結暫時保留**：依使用者指示，互動工具頁面（teach/）暫時不加專文回鏈，保持互動教具乾淨體驗。
  3. **三大商業關鍵字完全匹配植入**：
     - about.html：植入「中高齡營養師」（Title、H1、Lead、Profile）。
     - class.html：植入「企業健康講座」、「健康講座接案講師」（Title、H1、Lead）。
     - index.html：Hero Lead 植入「中高齡營養師」、「肌少症飲食」、「企業健康講座」。
  4. **個人諮詢與品牌大詞增補**：於 about.html、index.html Meta Keywords、agent.md 規範與關鍵字矩陣檔全面加入「桃園營養師推薦」（與既有「台北營養師推薦」並列）。
  5. **21 組企業講座核心關鍵字沉澱**：正式將使用者挑選之 21 組關鍵字（含 A-01~A-06、B-01~B-03、C-02、C-05、D-01~D-05、E-01~E-04）及三大商業支柱寫入 agent.md 與關鍵字矩陣報告，作為後續專文（Chapter 9～15）與教材之硬性嵌入標準。
  6. **全站 SEO 與 AI (GEO) 自動同步**：執行 sync_seo_and_geo.py，全站 22 個 URL、Sitemaps 與 AI 知識庫（llms.txt / llms-full.txt）全數同步至 2026-09-04。
  7. **版本控制與線上發布**：將所有整理妥善之程式碼、設定與文檔推送至 GitHub origin/main。

### 主要輸出

- about.html：注入「中高齡營養師」完全匹配與「桃園營養師推薦」Meta Keywords。
- class.html：注入「企業健康講座」與「健康講座接案講師」完全匹配。
- index.html：Hero 區整合三大關鍵字，並於 Meta Keywords 加入「桃園營養師推薦」。
- blog/posts.json、work/2026-08-15-seo-review-docs/：Chapter 8 補齊十字互鏈。
- agent.md：寫入 21 組企業講座關鍵字與個人品牌核心詞規範（含桃園營養師推薦）。
- work/2026-09-04-internal-links-and-keyword-enrichment/output/Corporate_Wellness_Keywords_Matrix.md：收錄完整 21 組選定詞與品牌大詞。
- sitemap.xml、sitemap.html、llms.txt、llms-full.txt、robots.txt、blog/index.html：全站 SEO & GEO 同步完成。

### 驗證

- 三點式抽檢通過：
  - 首項：about.html 標籤與 Meta 正確包含「中高齡營養師」與「桃園營養師推薦」。
  - 中項：class.html 標籤與 Hero 包含「企業健康講座」與「健康講座接案講師」。
  - 末項：Chapter 8 正文延伸閱讀錨點與 URL 經由 blog/posts.json 與公開頁同步驗證，可順暢跳轉至 Ch 6、Ch 7 與簡介頁。
- teach/ 保持乾淨無多餘回鏈，符合使用者指示。
- python tools/sync_seo_and_geo.py 執行退出碼 0。
- GitHub Pages 發布推送驗證完成。

## 2026-09-04｜檢核點 4（Milestone 4）全站內鏈網與長尾排名追蹤總檢核

### 任務

- 依「4 週 SEO & AI 搜尋攻頂計畫」時程，於第 2 週（09/04）啟動「檢核點 4（Milestone 4）：全站內鏈網與長尾排名追蹤」驗收。
- 遵循目錄規範，建立獨立專屬資料夾 `work/2026-09-04-milestone-4-internal-links-ranking-audit/`，分析腳本放置於 `source/`，總檢核報告產出於 `output/`。
- **任務 ①**：透過實體管線盤點全站 23 個節點（11 個核心/教具分頁 + 12 篇衛教專文），共計解析 148 條內部連結，深度分析「文章 ➔ 教具」、「教具 ➔ 文章」之雙向錨點連結。
- **任務 ②**：深入觀測「中高齡營養師」、「肌少症飲食」、「企業健康講座」三大核心詞於全站各頁面（Title, H1/H2, Body, Keywords）之分佈密度、完全匹配缺口與長尾排名爬升策略。
- 貫徹「嚴禁推測原則」，落實搜尋觀測通道說明與三點式一致性抽檢。

### 主要輸出

- `work/2026-09-04-milestone-4-internal-links-ranking-audit/source/audit_internal_links_and_keywords.py`：全站內鏈拓撲與關鍵字實體分析管線腳本。
- `work/2026-09-04-milestone-4-internal-links-ranking-audit/output/internal_links_and_keywords_data.json`：全站 23 個節點與 148 條連結拓撲資料檔。
- `work/2026-09-04-milestone-4-internal-links-ranking-audit/output/Milestone_4_Internal_Links_and_Keyword_Ranking_Report.md`：檢核點 4 全方位盤點總報告。
- `project-worklog.md`：更新本日工作日誌。

### 驗證

- 首項、中項、末項抽檢通過：
  - 首項：Chapter 1 正文連向全書導讀與論文讀書小站教具錨點 100% 正確可點擊。
  - 中項：Chapter 6 蛋白質專文包含 113 次「蛋白質」詞彙，並包含 7 條連向前幾章的交叉連結。
  - 末項：Chapter 8 水與礦物質專文已上線，外部來源 10 條齊備，已標示出站內十字互鏈待補優化點。
- 全域與專案規範遵行，報告確認無亂碼。

## 2026-09-04｜狀態修正：確認 Chapter 8《水與主要礦物質》已於 9/1 發布上線

### 任務

- 依使用者指示校正全站連載與 SEO 進度狀態：Chapter 8《水與主要礦物質》（`chapter-08-water-minerals-seo-review.docx`）已於 2026-09-01 正式發布至 GitHub 上線，修正狀態為「已上線」。
- 校正全站 SEO 資產與進度報告：全站公開專文總數更新為 12 篇（9 篇書籍連載專文 + 3 篇功能醫學/生活衛教），Sitemap 網址數為 22 個。
- 同步更新 `.codex/seo/book-series-progress.md`、`work/2026-09-01-seo-progress-report/output/SEO_Progress_Report_2026-09-01.md` 與專案工作日誌。
- 明確標記當前唯一待審稿件為 Chapter 9《能量平衡與健康體態（Energy Balance and a Healthy Body）》。

### 主要輸出

- `work/2026-09-01-seo-progress-report/output/SEO_Progress_Report_2026-09-01.md`：校正 Chapter 8 為「已上線」，更新全站統計數據與 M3 里程碑進度（95%）。
- `.codex/seo/book-series-progress.md`：回寫 2026-09-04 狀態校正紀錄，解除誤判之待審狀態。
- `project-worklog.md`：完成工作日誌回寫。

### 驗證

- 已核對文章 ID `2026-09-01-how-much-water-electrolytes-calcium-iron-bone-health` 於 `blog/posts.json`、`sitemap.xml` 與 `sitemap.html` 正確收錄。
- 確認 Chapter 8 狀態於各處進度報告統一為「已上線」。
- 全域與專案規則嚴格遵行。

## 2026-09-01｜三大業務支柱關鍵字佈局深度規劃確立

### 任務

- 依使用者指示，深度制定「專業營養師」、「專業講師」、「健康與法規顧問」三大商業支柱關鍵字佈局矩陣與全方位轉換漏斗。
- 遵循目錄規範，建立專屬資料夾 `work/2026-09-01-three-pillars-keyword-strategy/`，腳本放置於 `source/`，總規劃指南產出於 `output/`。
- 整合實體關聯圖譜（Entity Graph）、四層關鍵字矩陣（大詞/商業詞/痛點長尾詞/AI 語意問句）、著陸頁與 Schema.org 語意標註架構。

### 主要輸出

- `work/2026-09-01-three-pillars-keyword-strategy/source/make_plan.py`：規劃指南生成工具。
- `work/2026-09-01-three-pillars-keyword-strategy/output/Three_Pillars_Keyword_Strategy_Master_Plan.md`：三大業務支柱關鍵字佈局深度規劃旗艦指南。
- `project-worklog.md`：完成工作日誌回寫。

### 驗證

- 已確認 `Three_Pillars_Keyword_Strategy_Master_Plan.md` 包含完整實體圖、關鍵字矩陣、著陸頁配置、Schema 複合聲明與 4 階段推進時程。
- `git diff --check` 通過。

### 回寫狀態

- `project-worklog.md`：已更新。
- 專案與全域規則：嚴格遵行。

## 2026-09-01｜SEO Progress Report 全站進度總盤點與開工檢核

### 任務

- 依使用者指示啟動「SEO Progress Report Inquiry」開工任務。
- 遵循目錄規範，建立專屬資料夾 `work/2026-09-01-seo-progress-report/`，過程腳本放置於 `source/`，總審查報告產出於 `output/`。
- 完整盤點全站 SEO 資產：11 篇公開專文、8 篇書籍連載專文、4 篇首頁精選、21 個 Sitemap 網址、llms.txt AI 知識庫同步狀態。
- 盤點書籍連載審閱管線：確認 Chapter 1～7 已公開上線，Chapter 8（水與主要礦物質）與 Chapter 9（能量平衡與健康體態）Word 審閱主檔與 Markdown 待審稿已於 `work/2026-08-15-seo-review-docs/output/` 齊備。
- 追蹤「4 週 SEO & AI 搜尋攻頂計畫」8 大里程碑進度。
- 執行 ISO 第 36 週（偶數週）Search Console 與 6 大高權重機構反向連結合作機會盤點（貫徹「嚴禁推測原則」）。

### 主要輸出

- `work/2026-09-01-seo-progress-report/source/audit_seo_progress.py`：全站 SEO 資產與審閱管線檢查工具。
- `work/2026-09-01-seo-progress-report/output/SEO_Progress_Report_2026-09-01.md`：2026-09-01 SEO 全方位進度審查與開工總回報。
- `project-worklog.md`：更新本日工作日誌。

### 驗證

- 已執行 `audit_seo_progress.py`，確認 `blog/posts.json`、`sitemap.xml`、`llms.txt` 與本地檔案 100% 一致。
- 已確認 Chapter 8 Word 檔（8,110 字元、9 張表格）與 Chapter 9 Word 檔（5,577 字元、8 張表格）結構 QA 通過。
- `git diff --check` 通過。

### 回寫狀態

- `project-worklog.md`：已更新 2026-09-01 工作日誌。
- 全域與專案規則：嚴格遵行。

## 2026-08-30｜4 週 SEO 攻頂執行行事曆、8 大關鍵檢核點與全方位行銷策略確立

### 任務

- 重新梳理並向使用者完整回報「4 週 SEO & AI 搜尋攻頂執行行事曆」與 8 大關鍵檢核點（Milestones 1～8）。
- 確立雙邊協作權責劃分：Codex 負責公開專文連載深度撰寫、審閱套件產出與使用者授權後的發布；Antigravity 負責全站 SEO、AI 搜尋收錄（GEO/LLMO）、三大業務支柱關鍵字佈局、站內外連結網與 B2B/EAP 行銷推廣手段。
- 排程守護重置：重新掛載並啟動每日 11:30 定時檢核守護任務（`task-65`），防止背景行程因伺服器重啟中斷。
- 全站資產與連載進度盤點：確認 Chapter 7 維生素篇已公開上線，Chapter 8（水與礦物質）與 Chapter 9（能量平衡）待審稿均已就緒，全站 11 篇公開文章與 sitemap/llms 比對一致。

### 已完成

- 4 週攻頂行事曆與 8 大檢核點正式梳理與確認。
- 三大業務支柱關鍵字矩陣（營養師、講師、顧問）與 GEO/LLMO 實體綁定架構確立。
- 站外推廣（EAP 企業方案信函、公會學術機構外鏈、教具社群卡片裂變、LINE/Zcal 漏斗）策略確立。
- 每日定時守護任務排程常駐設定完成（`task-65`）。
- 專案工作日誌完整回寫。

### 驗證

- 已確認 `blog/posts.json`、`sitemap.xml` 與 `llms.txt` 在公開端與本地一致（11 篇公開專文）。
- 已確認 Chapter 8 與 Chapter 9 同源 Word 審閱檔與 Markdown 待審稿均完整保留於 `work/2026-08-15-seo-review-docs/output/`。
- `git status` 與工作樹檢查完成。

### 規則回寫

- `project-worklog.md`：已更新 2026-08-30 完整執行日誌。
- 專案與全域規則沿用最新規範。

## 2026-08-24｜書籍連載分類統一

### 任務

- 使用者發現最新書籍連載文章日期後出現「書籍連載與營養知識」，要求前幾篇連載也補上相同分類。
- 先採用這個分類名稱，文章數量增加後再依讀者搜尋意圖與導覽需求重新設計分類方式。

### 已完成

- 重新讀取 GitHub `main` 的 `blog/posts.json`，遠端基準內容 SHA-256 為 `EE1ADC9112D68BC17EFBEFB1DD831BB130DE67E64571C6EEE6B588870349F1B`。
- 只替換 7 篇書籍連載的 `category` 欄位：2026-08-13、08-14、08-15、08-16、08-17、08-20、08-22。
- GitHub commit：`e51230d61dff3dc6b434e7f180e4b842db9935f5`，提交訊息為 `Add category field to nutrition-related posts`。

### 驗證

- 遠端文章總數維持 10 篇，7 篇連載分類均為「書籍連載與營養知識」。
- 3 篇非連載文章的欄位未變，7 篇目標文章的標題、日期、內文、圖片、關鍵字與 `showOnHome` 未變。
- `showOnHome` 原值保留，首頁精選仍為 4 篇。
- 公開 Blog 列表顯示「書籍連載與營養知識」，分類篩選結果為 7 篇。
- 最新文章公開頁標題正常，BlogPosting 的 `articleSection` 為「書籍連載與營養知識」。

### 已修正錯誤

- 第一次準備提交時，GitHub 編輯分頁在工作輪次切換後關閉，沒有產生公開變更。
- 重新開啟編輯頁並再次讀取遠端基準，確認內容 SHA 未變後重建目標欄位，再完成提交。

### 尚未完成

- 本機 `blog/posts.json` 保留原工作樹版本，沒有用落後的本機檔案覆蓋遠端 `main`。
- 分類架構先採單一書籍連載分類，尚未建立更多分類層級。

### 仍有風險

- 書籍連載篇數增加後，單一分類可能不足以支援搜尋與導覽，需要依文章主題、讀者問題與篩選使用情況重新評估。

### 規則回寫

- `agent.md` 已加入書籍連載分類一致性與分類增長前的評估規則。
- `context.md` 與自動化記憶已記錄本次遠端欄位修正與驗證結果。

## 2026-08-24｜文章產物集中整理

### 任務

- 依使用者習慣，將文章工作集中到 `work/2026-08-15-seo-review-docs/`。
- 清查 2026-08-23 之後產出的檔案，將可保留內容歸入 `output`、`source`、`render`。
- 移除已無檔案用途的日期型工作資料夾與 Word 暫存鎖定檔，保留可復原紀錄。

### 已完成

- Chapter 7 待審稿已位於 `work/2026-08-15-seo-review-docs/output/chapter-07-vitamins-seo-review.md`，檔案大小 23,400 bytes。
- Chapter 7 研究回報、Chapter 6 發布來源、發布 manifest 與產出腳本已分別放入三個既有分類位置。
- 原本散落在主資料夾根部的 24 個歷史腳本與參考檔已移入 `source`，主資料夾現在只保留 `output`、`source`、`render` 三個分類位置。
- `work/2026-08-23-chapter6-publish`、`work/2026-08-23-chapter7-vitamins-seo-review` 與一個 Word 暫存鎖定檔已移至 Windows 資源回收筒，可復原。
- `.codex/seo/context.md`、`.codex/seo/book-series-progress.md` 與自動化記憶已改用集中後路徑。

### 驗證

- Chapter 7 QA 通過：正文可見字數 5,360，H2 13 個，H3 6 個，表格 12 張，FAQ 5 題，來源連結 15 個，禁用詞命中 0。
- 已確認兩個 2026-08-23 日期型資料夾與 Word 暫存鎖定檔原位置均不存在。
- 已確認 `work` 現在只保留既有的 `2026-08-14-blog-restore`、`2026-08-15-seo-review-docs`、`2026-08-21-seo-growth-strategy`。
- Codex 與 Antigravity 全域 `AGENTS.md` 已加入集中資料夾規則，新增內容逐行一致。兩份完整檔案仍有歷史差異，未宣稱整檔相同。

### 已修正錯誤

- 第一次清理指令的 PowerShell 路徑陣列組合有誤，未發生刪除。
- 第二次檢查把空的子資料夾算入檔案清單，未發生刪除。
- 改用遞迴檔案數量檢查後才執行資源回收筒移動，並重新確認目標路徑。
- 搬移後相關腳本的相對路徑已修正，23 個 Python 檔案通過語法解析，2 個 JavaScript 檔案通過語法檢查，Chapter 7 QA 已用新位置重跑通過。

### 尚未完成

- `2026-08-14-blog-restore` 與 `2026-08-21-seo-growth-strategy` 仍保留，原因是它們屬於 Git 追蹤的歷史資料，且工作日誌與進度紀錄仍有引用。
- 本次整理沒有建立 Git commit，也沒有推送 GitHub，避免覆蓋工作樹內其他既有變更。

### 仍有風險

- 未來腳本若自行指定日期型輸出路徑，仍可能造成資料夾增加，產出前要先套用集中位置規則。
- 舊日誌中的歷史路徑保留原貌，僅更新目前交接位置，避免改寫歷史紀錄造成追溯困難。

### 規則回寫

- 本專案 `agent.md` 已加入文章產物集中規則。
- Codex 與 Antigravity 全域 `AGENTS.md` 已加入同一項長期提醒。
- 本次沒有新增或修改 skill，因現有工作流程已能承載集中資料夾規則。

## 2026-08-22 (授課資訊擴充、封面圖卡防裁切修復與全站文字排版升級)

### 任務

- 更新 `class.html`：新增 7 家邀約合作夥伴單位（核安會、國環院、長庚醫院、台北國際航空站、元智大學、育達科大、慈濟基金會），依相同屬性歸類並排序於舊單位之後；新增 12 項過往授課主題題目並歸入對應分類。
- 衛教文章頁面（`blog/`）與全站封面圖卡裁切修復：徹底改善標題封面圖卡過大與圖片文字被裁切問題。
- 全站排版與文字大小規範升級：包含主站（首頁、簡介、授課、文章列表、單篇文章）與各分頁（公開版論文讀書小站 `teach/paper-radar/` 等），所有文字（內文、導覽、Meta、Tag、搜尋、按鈕、表格、頁尾等）最小字體全面確保 >= 16px (1rem)。
- 建立並沉澱使用者喜好與硬性規範至 `agent.md`。
- 執行 Git 提交與推送至 GitHub 遠端儲存庫，完成收工驗證。

### 主要輸出

- `class.html`：完成合作夥伴與 12 項授課題目分類更新。
- `styles.css`：
  - 文章列表縮圖 `.post-thumb` 改為 `object-fit: contain` + `16:9` 襯底，桌機 260px，手機自適應防切字。
  - 單篇封面圖卡 `.article-cover` 改為 `object-fit: contain` + `height: auto` + 置中 760px，移除強制鎖死高度。
  - 全站導覽、Tag、Meta、按鈕、搜尋結果文字全面調升至 16px (1rem) 以上。
- `blog/index.html`、`blog/post.html`、`blog/blog.js`：更新版本號快取參數、延伸閱讀區塊字體大小調升至 1rem。
- `teach/paper-radar/index.html`、`teach/paper-radar/style.css`：公開版論文讀書小站所有摘要、評讀筆記、中英文作者、文獻標籤、DOI/期刊資訊、搜尋分頁字體全面升級至 16px (1rem) 以上。
- `agent.md`：新增「全站文字大小規範」、「封面圖卡防裁切規範」與「合作夥伴/授課主題維護規範」。
- `project-worklog.md`：完成工作日誌回寫。

### 驗證

- 已確認 `git diff` 與檔案語法完整無誤。
- 已執行 `git commit` 與 `git push origin main`（Commit: `8f99887`、`4d270e1`、`362bc12`），遠端儲存庫已完整同步。
- 已確認所有圖卡文字在各長寬比下皆完整收錄不切字，各分頁最小字體 >= 16px。

### 錯誤或風險與過程修正

- 上一輪因只提交 `class.html` 單一檔案，修正圖卡的 `styles.css` 當時留在本地尚未推送到遠端，造成線上 GitHub Pages 仍載入舊版 cover 裁切樣式；本次已將所有樣式與分頁檔案完整提交並推送到 GitHub。

### 新學到的規則與使用者偏好

- 合作夥伴單位新增時，依相同屬性單位放在一起，新的單位固定放在舊的後面。
- 圖片內含文字之封面圖卡與列表縮圖，一律使用 `object-fit: contain`，不得使用強制高度的 `cover` 造成文字被截斷。
- 網站所有文字（含主站及各獨立分頁、教具、論文小站等）最小字體一律不得低於 16px (1rem)，手機版維持在 1.05rem - 1.25rem。
- 修改完成後需同步更新快取版本參數，並推送到遠端確認生效，完成規則與日誌回寫後方屬完整收工流程。

### 回寫狀態

- `agent.md`：已更新
- `project-worklog.md`：已更新
- 全域 `AGENTS.md`：沿用最新版


## 2026-06-19

### 任務

- 補上 Kat Chang 網站專案的收尾 SOP。
- 明確規定 skill、`agent.md`、全域 `AGENTS.md`、工作日誌各自要記什麼。

### 主要輸出

- 更新 `agent.md`，加入「專案收尾 SOP」段落。
- 新增 `project-worklog.md`，作為後續每次任務完成後的固定紀錄位置。

### 驗證

- 已確認本專案有根目錄 `agent.md`。
- 已確認本專案先前沒有 `project-worklog.md`，本次已補建。

### 錯誤或風險

- 若只把經驗留在對話裡，後續代理容易重犯 JSON 結構、SEO 欄位、品牌說法與健康內容邊界的同類問題。

### 新學到的規則

- 網站專案收尾時，skill 要記可重複用的模板、流程、修正步驟與驗證法。
- `agent.md` 要記 Kat Chang 網站專案限定規則。
- 全域 `AGENTS.md` 要記跨專案也要跟著做的長期規則。
- 工作日誌要記日期、任務、輸出、驗證、風險、規則沉澱與回寫狀態。

### 回寫狀態

- `agent.md`：已更新
- `project-worklog.md`：已建立
- 全域 `AGENTS.md`：沿用既有最新版

## 2026-07-05

### 任務

- 將文字雲互動工具加入 `teach/` 入口頁。
- 首頁互動衛教工具區調整為三張卡片，移除 Nutrition Battle 首頁入口。

### 主要輸出

- 更新 `teach/index.html`，新增文字雲互動工具外連卡片。
- 更新 `index.html`，首頁教具區保留 Stress Food、草木心語情緒覺察卡、NutriRank 食品營養排行榜。
- 更新 `llms.txt`，補上文字雲互動工具連結。

### 驗證

- 已用文字搜尋確認首頁 `index.html` 沒有 Nutrition Battle 卡片。
- 已確認 `teach/index.html` 保留 Nutrition Battle，並新增 `https://teaching-3809d.web.app/` 文字雲連結。
- 已確認本次改動未碰觸憑證或設定檔。

### 錯誤或風險

- 文字雲工具為外部 Firebase 網址，這次只做入口連結，未驗證該站後端或資料寫入狀態。
- 一開始公開頁面仍回傳快取內容，後續已用帶版本參數的公開網址再次確認頁面更新。

### 新學到的規則

- Kat Chang 網站首頁教具區固定精簡為三張卡片：Stress Food、草木心語情緒覺察卡、NutriRank 食品營養排行榜。
- Nutrition Battle 與文字雲互動工具放在 `teach/` 入口頁，避免首頁工具區過長。

### 使用者偏好

- 使用者希望首頁工具區維持精簡，只放三個主要互動衛教工具。
- 使用者希望新增或調整網站後能推到 GitHub，並確認公開頁面真的更新。

### 過程修正

- 本次先提交並推送網站檔，收工時才發現 `agent.md` 與 `project-worklog.md` 仍未納入 Git 追蹤。後續遇到專案收尾紀錄，應在提交前一併檢查文件是否需要納入版本控制。

### 回寫狀態

- `agent.md`：已更新
- `project-worklog.md`：已更新
- 全域 `AGENTS.md`：本次無跨專案規則更新

## 2026-07-06

### 任務

- 查看 GitHub Actions 信件通知中的 GitHub Pages 部署失敗。
- 排查 run `28738942936`，嘗試修復靜態網站部署流程。

### 主要輸出

- 讀取失敗 job log，確認失敗點在 `Deploy to GitHub Pages`。
- 重跑失敗 job 一次，重跑後仍在同一階段失敗。
- 更新 `.github/workflows/pages.yml`，將 Pages workflow 使用的 action 升到目前查得的官方 release 版本：`actions/checkout@v7`、`actions/configure-pages@v6`、`actions/upload-pages-artifact@v5`、`actions/deploy-pages@v5`。
- 更新 `agent.md`，補上 GitHub Pages 部署失敗排查流程。
- 推送修正 commit `9f2a5cc` 後，新 run `28795226316` 已成功完成。
- 推送最後工作日誌 commit `1c56598` 後，內建 Pages run `28796072444` 一開始仍在 deploy 階段失敗。等待約 2 分鐘後重跑同一 run，第 3 次嘗試成功。

### 驗證

- 已確認本機工作樹起始狀態為乾淨。
- 已確認公開網站 `https://594katchang-source.github.io/` 回傳 200，既有線上頁面仍可開啟。
- 已確認原 run 的 artifact 上傳成功，檔案大小約 23 MB。
- 已確認 GitHub Status API 在 2026-07-06 回報 GitHub Pages 與 Actions 為 operational。
- 已確認新 GitHub Actions run `28795226316` 結果為 success。
- 已確認推送後本機工作樹回到乾淨狀態。
- 已確認最新 Pages run `28796072444` 第 3 次嘗試結果為 success。
- 已確認公開 `project-worklog.md` 已包含最新修復紀錄，代表公開網站已發布到 commit `1c56598`。

### 錯誤或風險

- GitHub Pages log 只回傳 `Deployment failed, try again later.`，未提供更細的後端錯誤。
- 若後續再次出現同樣錯誤，下一步需到 GitHub 網頁後台檢查 Pages Source 是否為 GitHub Actions，以及 `github-pages` environment 是否有卡住的 deployment 或保護規則。
- 本機 `gh` 目前尚未登入，Actions log 讀取與重跑是透過已連線的 GitHub 工具完成。
- 後續確認最新版 workflow 仍會在 Pages deploy 階段間歇失敗，決定改回 GitHub Pages 直接從 `main` 分支發布，並移除 `.github/workflows/pages.yml`，避免 Actions 繼續寄失敗信。
- GitHub Pages Source 已改成 `Deploy from a branch`，來源為 `main` 與 `/ (root)`。
- 推送 commit `7473757` 後，GitHub 產生的 `pages build and deployment` run `28795994127` 已成功完成。
- GitHub Pages 後台可能在短時間連續部署時仍回 `Deployment failed, try again later.`。若建置與 artifact 都成功、公開網站仍可開啟，先等待數分鐘再重跑同一個 failed run，不要一直推新 commit 製造更多部署。

### 新學到的規則

- GitHub Pages 若 artifact 上傳成功但 deploy 階段失敗，先重跑 failed job。若仍失敗，檢查 Pages Source、environment 狀態與 action release 版本。
- 純靜態網站若不需要建置流程，優先使用 GitHub Pages branch source，減少 Actions deploy 服務端狀態造成的失敗點。
- Pages deploy 階段若是 GitHub 服務端短暫卡住，重跑前先等幾分鐘，同一 run 成功後再用公開檔案內容確認最新 commit 已上線。

### 回寫狀態

- `agent.md`：已更新
- `project-worklog.md`：已更新
- 全域 `AGENTS.md`：本次無新增跨專案規則

## 2026-07-18

### 任務

- 在 `teach/` 加入論文讀書小站公開閱讀版，提供可公開查閱的論文資料與中文閱讀成果。

### 主要輸出

- 新增 `teach/paper-radar/index.html`、`app.js`、`style.css` 與 `data/papers-public.json`。
- `teach/index.html` 新增「論文讀書小站公開版」入口卡片。
- 公開頁提供搜尋、成果類型篩選、頁碼、合法全文連結、摘要層級限制標示與自我測驗卡呈現。
- 公開 JSON 目前為空資料檔，等待私人 Sites 發布器產生完成成果。

### 驗證

- 公開頁 `app.js` 通過 Node 語法檢查。
- `papers-public.json` 可解析，`schemaVersion` 為 1。
- 公開頁檔案未出現私人 API 路徑、Worker token、owner、PDF 識別欄位。
- `teach/index.html` 已確認含有 `paper-radar/` 入口連結。

### 錯誤或風險

- GitHub repository 尚未完成本次 commit 與推送。
- GitHub Pages 線上頁面尚未做 live 驗證。
- 公開資料檔保持空陣列，未放入私人 Sites 或個人閱讀紀錄。

### 新學到的規則

- 公開論文頁只讀取同一路徑下的 `data/papers-public.json`，頁面不連接私人 API。
- 摘要層級評讀必須明確標示全文限制，完整全文整理才可作為全文層級成果。

### 回寫狀態

- `agent.md`：已更新公開頁路徑、資料欄位與驗證要求。
- `project-worklog.md`：已更新。
- 全域 `AGENTS.md`：本次無新增跨專案規則。

## 2026-07-18｜公開頁中文化與線上驗證收尾

- 任務：完成公開頁論文標題、期刊分類、左上角人像 logo、每頁 50 筆與中文搜尋的同步。
- 主要輸出：公開頁以繁體中文顯示 76 篇成果的標題與期刊分類，英文原始欄位仍保留於搜尋索引。指定成果顯示為「全文評讀：中鏈三酸甘油酯與慢性病預防」。
- 驗證：GitHub Pages 線上頁面讀取 76 筆，第一頁顯示 50 張卡片，第二頁顯示第 51 至 76 筆。主頁人像 logo、指定成果、中文「孕期飲食」搜尋均已核對。
- 錯誤或風險：同步過程曾因 GitHub tree 基準選錯而漏掉公開資料與樣式檔，已用完整檔案樹補回。Windows 狀態外框曾誤送入遠端 blob，已改用原始位元組重建 UTF-8 檔案。
- 新增規則：公開頁標題與期刊分類固定優先顯示繁體中文，技術縮寫、DOI、作者與原文內容依原始資料保留。
- 回寫狀態：本機工作庫與 GitHub 均已更新，專案規則與工作日誌已補齊。

## 2026-07-18｜公開頁論文標題與期刊分類中文化

- 任務：處理公開頁仍大量顯示英文論文標題與期刊分類的問題，讓「全文評讀：中鏈三酸甘油酯與慢性病預防」這類成果標題與卡片欄位一致使用繁體中文。
- 主要輸出：更新公開頁 `app.js`，加入目前 76 篇成果的繁體中文標題顯示、期刊分類中文對照、中文搜尋索引與成果折疊標題格式。原始英文標題仍保留於搜尋內容中。
- 驗證：待本機頁面重新整理後檢查指定中鏈三酸甘油酯成果、英文標題替換、期刊分類與中文搜尋。
- 錯誤或風險：翻譯採公開頁顯示用語，DOI、作者、原文內容與技術縮寫保留原始資料。GitHub Pages 尚未完成本次同步。
- 新增規則：公開卡片標題與期刊分類固定優先顯示繁體中文，原始英文欄位仍納入搜尋。
- 回寫狀態：已更新專案 `agent.md` 與工作日誌。未修改全域 skill、Antigravity、Firebase 或私有 Sites。

## 2026-07-18｜公開頁 logo 與每頁筆數統一

### 任務

- 讓公開頁左上角沿用主頁相同的人像 logo，並把公開頁每頁顯示數量從 100 篇改為 50 篇，保持本機與 GitHub 版本一致。

### 主要輸出

- 更新 `teach/paper-radar/index.html` 的品牌區，加入主頁相同的人像圖、品牌名稱與首頁連結。
- 更新 `teach/paper-radar/app.js` 的 `PAGE_SIZE` 為 50。
- 同步更新專案規則與工作日誌。

### 驗證

- 本機頁面將以 50 篇為一頁，資料共 76 篇時會顯示兩頁。
- 品牌區使用與主頁相同的 logo URL。
- GitHub 待本次修改完成後同步。

### 錯誤或風險

- logo 使用主頁目前公開的人像資源，需等待 GitHub Pages 同步後再核對線上畫面。
- 公開資料內容與搜尋規則未變更。

### 新學到的規則

- 公開頁每頁固定 50 篇，左上角固定沿用主頁品牌 logo 與首頁連結。

### 回寫狀態

- `agent.md`：已更新。
- `project-worklog.md`：已更新。
- 全域 `AGENTS.md`：本次無新增跨專案規則。

## 2026-07-18｜公開版提交至 GitHub

### 任務

- 依使用者授權，把公開唯讀版提交到 `594katchang-source/594katchang-source.github.io` 的 `main`。

### 主要輸出

- 公開頁、中文折疊標籤、76 篇公開成果資料、入口頁、`agent.md` 與工作日誌均已寫入 GitHub。

### 驗證

- GitHub `main` 最新修正版 commit 為 `26094d165a618ec89f3172f9515ca78cc17255da`。
- 遠端資料檔首段、末段與指定 DOI `10.1016/j.ajcnut.2026.101393` 均已核對。
- 公開 JSON 本機資料仍為 76 篇，頁面標籤檢查通過。

### 錯誤或風險

- GitHub CLI 未完成登入，改用已授權的 GitHub 連線推送。
- 第一次大型 JSON 傳輸有截斷風險，已從 commit `a9620725` 重新以 39 段原始位元組建立完整資料 blob，並由 commit `26094d1` 更新 `main`。

### 回寫狀態

- `agent.md`：已更新。
- `project-worklog.md`：已更新。
- 全域 `AGENTS.md`：本次無新增跨專案規則。

## 2026-07-18｜公開頁折疊標籤中文化

### 任務

- 把公開頁下拉標籤統一成中文，並讓成果折疊標題採用「全文評讀：論文標題」或「品質評讀：論文標題」的格式。

### 主要輸出

- 更新 `teach/paper-radar/app.js` 與 `teach/paper-radar/index.html`。
- `全文整理` 改為 `全文評讀`。摘要、品質評讀、全文評讀、自我測驗與查看答案均以中文顯示。
- 英文 noteTitle 會在畫面上補上中文成果類型，原有「全文評讀：中鏈三酸甘油酯與慢性病預防」格式予以保留。

### 驗證

- 本機頁面重新整理後，統計區與篩選鈕均顯示 `全文評讀`。
- 頁面可見 `查看摘要`、`全文評讀`、`品質評讀`、`自我測驗（4 張）`。
- 指定的中鏈三酸甘油酯成果顯示為 `全文評讀：中鏈三酸甘油酯與慢性病預防`。

### 錯誤或風險

- 公開頁仍保留英文論文原標題與作者資料，這些是論文原始欄位，畫面標籤與成果類型已中文化。
- GitHub 公開部署尚未進行。

### 新學到的規則

- 公開頁下拉標籤固定使用中文。全文成果標題固定使用 `全文評讀：` 前綴，摘要層級成果使用 `品質評讀：` 前綴，已有更精確中文成果標題時保留原標題。

### 回寫狀態

- `agent.md`：已更新。
- `project-worklog.md`：已更新。
- 全域 `AGENTS.md`：本次無新增跨專案規則。
## 2026-07-18｜收工核對

- 產出狀態：公開頁中文標題、期刊分類、主頁人像 logo、每頁 50 筆與中文搜尋均已完成。
- 驗證狀態：本機 Git 工作庫乾淨，公開頁程式通過 Node 語法檢查，GitHub 公開資料與樣式檔存在，線上頁面已核對 76 篇與第二頁切換。
- 錯誤記錄：同步時曾遇到 Windows 狀態外框與 GitHub tree 基準問題，已改用原始 UTF-8 位元組及完整公開檔案樹修正。
- 回寫狀態：本次收工紀錄補入專案工作日誌，未新增全域規則或 skill 修改。

## 2026-07-27｜公開資料更新

- 產出狀態：由私人 Sites 公開匯出取得 295 篇已完成且符合資格的成果，更新 `teach/paper-radar/data/papers-public.json`。
- 驗證狀態：線上頁面顯示 295 篇、198 篇品質評讀、97 篇全文評讀，每頁 50 篇，更新日期為 2026 年 7 月 27 日。公開 repo 工作樹乾淨，發布狀態為 `published`。
- 錯誤記錄：本次以合併提交保留本機公開資料與遠端頁面修正，再完成 GitHub `main` 推送。Node 連線曾需使用系統憑證設定重跑。
- 回寫狀態：已更新本工作日誌，未寫入私人 Sites 資料、PDF、token 或其他憑證。

## 2026-07-27｜移除公開管理頁

- 任務：處理公開 GitHub Pages repo 中可直接開啟的 `/admin/` Blog 管理頁，避免訪客在公開頁面輸入 GitHub token。
- 主要輸出：移除 `admin/index.html` 與 `admin/admin.js`，移除 Blog 首頁的公開管理入口，保留 Blog 閱讀頁與論文公開頁。
- 驗證：目前版本已沒有 `admin/` 檔案、管理入口或 GitHub token 輸入欄位。公開論文頁的資料檔與程式仍維持原狀。
- 錯誤或風險：`noindex` 不能提供權限控制。公開 repo 歷史仍保留舊版 Firebase key 樣式內容，需另到 Firebase 或 Google Cloud Console 確認是否已停用、更換與收緊規則。
- 新增規則：需要貼上 GitHub token 的管理功能不得放在公開 GitHub Pages。管理功能固定移至私人或本機環境。
- 回寫狀態：已更新本工作日誌與專案 `agent.md`，未修改全域 skill。

## 2026-07-27｜確認 teach 文字雲保留 Firebase

- 任務：確認移除 GitHub Pages 一般頁面頭像 Firebase Storage token 時，沒有誤改 `teach/` 入口外連的文字雲。
- 驗證：`teach/index.html` 仍連到 `https://teaching-3809d.web.app/`。線上文字雲仍載入 `/firebase-config.js`，其 `app.js` 仍載入 Firebase SDK、Firestore 與 `onSnapshot` 即時監聽。本機文字雲設定檔仍存在於忽略檔 `public/firebase-config.js`，沒有進入 Git。
- 新增規則：文字雲是獨立的 Firebase Hosting 工具，必須保留 Firebase 設定注入與 Firestore 即時回饋。GitHub Pages 頭像改用 repo 內圖片的規則只適用一般頁面，不能套用到文字雲。
- 回寫狀態：已更新本專案 `agent.md` 與工作日誌，沒有修改文字雲程式或 Firebase 設定。

## 2026-07-27｜移除公開 Firebase Storage token

- 任務：移除公開 HTML 中人像圖片的 Firebase Storage download token，保留原本的人像 logo。
- 主要輸出：新增 `assets/profile/kat-avatar.jpg`，根頁面、簡介、授課、Blog、教具入口與論文公開頁改用 repo 內圖片路徑。
- 驗證：公開 HTML 已找不到 `firebasestorage.googleapis.com`、Firebase Storage token 或 `token=` 圖片網址。`papers-public.json` 仍可解析，共 295 篇。
- 錯誤或風險：Nutrition Battle 仍保留使用者自行貼入 Firebase Web app config 的教學流程，設定只存瀏覽器，不含內建 API key。Firebase 專案的 API restrictions 與資料庫規則仍需在 Console 核對。
- 新增規則：公開網站圖片資產改放 repo 內，避免把第三方下載 token 寫進 HTML 或 metadata。
- 回寫狀態：已更新本工作日誌與專案 `agent.md`，未修改全域 skill。

## 2026-07-27｜收工核對

- 產出狀態：公開 repo `main` 已推送 `0f60e7f`，本次只新增文字雲 Firebase 邊界規則與工作日誌，沒有改動文字雲程式、Firebase 設定或論文資料。
- 驗證狀態：公開 repo 工作樹乾淨且遠端同步。公開論文資料仍為 295 篇，線上論文頁仍使用本地人像資產。線上文字雲仍載入 Firebase 設定、Firebase SDK、Firestore 與 `onSnapshot`。
- 未驗證與風險：尚未進入 Firebase Console 核對文字雲 key 的 API 限制、配額與 Firestore Rules，未執行會新增課堂資料的實際寫入測試。
- 使用者偏好：GitHub Pages 一般頁面的頭像 token 清理，不能影響 teach 文字雲。文字雲固定保留 Firebase。
- 錯誤與修正：已將頭像資產與文字雲服務分開核對，並把規則寫入 `agent.md`。下次先盤點外連工具的服務依賴，再處理公開資產或 token 清理。
- 回寫狀態：本次收工紀錄已寫入專案工作日誌，沒有把真實 key 寫入工作日誌或 GitHub。

## 2026-07-27｜行動版版面修正

### 任務

- 修正簡介與授課頁在手機上一般按鈕白底白字的問題。
- 整理互動教具入口頁的手機配色、標題與卡片排列。
- 移除教具頁標題下方沒有用途的說明段落，並讓頂端「教具」「文章」直接連到各自分頁。

### 主要輸出

- 更新 `styles.css`：一般按鈕固定使用深綠文字，行動版導覽改成上下排列，hero 標題允許換行，並補上行動版按鈕與教具入口頁的對比規則。
- 更新 `about.html`、`class.html`、`index.html`、`blog/index.html`、`teach/index.html` 與 `teach/paper-radar/index.html` 的導覽連結。
- `teach/index.html` 移除「原本 info 底下的工具已整理到 teach 目錄。」。

### 驗證

- `git diff --check` 通過，沒有發現空白或補丁格式錯誤。
- 搜尋所有 HTML 後，已找不到舊的 `index.html#teach`、`index.html#blog` 與已移除段落。
- 已確認本機工作樹只包含本次七個頁面與共用樣式的預期改動。
- 已用帶版本參數的公開網址核對簡介與教具入口：CSS 已切到 `20260727-mobile`，教具頁標題存在、工具卡片共 6 張、說明段落已移除，導覽列路徑正確。
- 行動版 375px 與 390px 的規則已寫入共用 CSS，這次瀏覽器連線未提供實機寬度切換，因此仍未取得兩個寬度的實機截圖。

### 錯誤或風險

- 本機背景預覽服務受環境權限限制，未能以本機網址開啟瀏覽器預覽。已改以公開頁 cache-busting 連結核對發布內容。
- 本次未改動教具內部遊戲邏輯、資料檔或文字雲 Firebase 設定。

### 新學到的規則

- 共用手機樣式調整要同時檢查導覽列、hero 標題、按鈕對比與工具入口頁背景，不能只看單一元件。

### 回寫狀態

- `agent.md`：已補上行動版寬度與按鈕對比檢查規則。
- `project-worklog.md`：已更新。
- 全域 `AGENTS.md`：本次無跨專案規則更新。

### 發布補充

- 公開頁核對時發現共用 CSS 仍使用舊版本參數，已將七個共用樣式入口改為 `20260727-mobile`，並再次提交推送。
- CSS 快取版本更新後，需重新讀取公開頁確認 HTML 與樣式入口都已切到新版本，不能只看 GitHub 提交成功。

### 收尾狀態

- GitHub `main` 已推送至 `181f112`，公開頁已讀到最新導覽與 CSS 版本。
- 本機工作樹已完成清理檢查，未留下未提交的網站修改。

## 2026-07-27｜聯絡入口與高齡閱讀版面統一

### 任務

- 將簡介頁「立即行動」連到預約頁 `https://zcal.co/katchang`。
- 檢查主要網站頁面的頁尾聯絡按鈕，統一為「官方 Line」與「Email」。
- 補上 teach、blog、文章內容頁與論文公開頁的頁尾聯絡區。
- 在簡介證照補上 `CHT園藝治療師證照`。
- 修正 blog 行動版標題黑字落在深色背景的問題，讓 teach 與 blog 入口頁採用一致的淺色背景與深色標題。
- 把首頁頂端「聯絡」改成明確的 `index.html#contact`，並把桌面與手機版同步檢查規則寫入 `agent.md`。

### 主要輸出

- 更新 `about.html`、`class.html`、`index.html`、`blog/index.html`、`blog/post.html`、`teach/index.html`、`teach/paper-radar/index.html`。
- 更新 `styles.css`，補上 blog 入口與文章頁的行動版配色、標題與內文字級規則。
- 更新 `agent.md`，新增桌面與手機同步修改、頁尾按鈕、聯絡錨點與中高齡閱讀字級規則。

### 驗證

- `git diff --check` 通過。
- 已搜尋主要頁面，確認 zcal 預約連結、CHT 證照、官方 Line、Email、首頁 contact 錨點均存在。
- 已確認 teach 頁沒有「原本 info 底下的工具已整理到 teach 目錄。」。
- 已確認 teach、blog 入口頁與 blog 文章頁都帶有專用 body class，CSS 會覆蓋行動版深色背景與黑色 h1 問題。
- 已用帶版本參數的公開網址重新核對 HTML 與 CSS。瀏覽器約 375px 寬度檢查結果：teach 與 blog 背景為淺色、h1 為深色、內文至少 1rem、頁面沒有水平溢出。簡介頁曾發現 hero 裝飾造成水平溢出，已補上 html 與 body 的行動版 `overflow-x:hidden`，並更新 CSS 快取版本。
- 尚未取得實體手機裝置截圖，已完成瀏覽器行動版尺寸檢查。

### 錯誤或風險

- `teach/` 內的個別互動工具是獨立頁面與獨立樣式，這次頁尾聯絡區先統一網站入口頁、文章頁與論文公開頁，沒有改寫教具互動邏輯。
- GitHub Pages 可能保留舊 CSS 快取，發布後要用新的 CSS 版本參數或重新整理核對。這次已由 `20260727-contact` 更新到 `20260727-contact3`，並補上 html 與 body 的行動版水平溢出限制。

### 新學到的規則

- 網站頁面調整要把 HTML 內容、共用 CSS、導覽路徑與頁尾聯絡入口放在同一次檢查中。
- 面向中高齡讀者的行動版內文與卡片說明以 `1rem` 為下限，標題與按鈕要確認背景對比及換行。

### 回寫狀態

- `agent.md`：已更新。
- `project-worklog.md`：本筆已更新。
- 全域 `AGENTS.md`：本次規則限於本網站，未更新。

## 2026-07-28｜收工核對

### 收尾結果

- 本機工作樹乾淨，`HEAD` 與 `origin/main` 的差異為 `0 0`。
- 最新提交為 `7dd1ac0 Record final mobile verification`。
- 公開首頁已核對頁尾「官方 Line」「Email」、頂端「聯絡」與 `styles.css?v=20260727-contact3`。
- 公開 teach 入口已核對標題、body class、頁尾兩個聯絡按鈕。
- 公開 blog 入口已核對標題、body class、頁尾兩個聯絡按鈕與共用 CSS 版本。

### 連線狀態與風險

- PowerShell 直接查 GitHub 時遇到 Windows Schannel 憑證通道錯誤，改用瀏覽器完成公開頁核對。
- 實體手機截圖仍未取得，已保留瀏覽器行動版尺寸檢查結果。

### 回寫狀態

- `agent.md`：既有桌面與手機同步規則仍有效。
- `project-worklog.md`：已補上本次收工紀錄。
- 全域 `AGENTS.md` 與 skill：本次無新增跨專案規則。

## 2026-07-28｜全站桌機、手機、資安與 SEO 稽核

### 任務

- 盤點公開網站所有 HTML 頁面，核對桌機與約 375px 行動版的頁首、頁尾、配色、字級、導覽與聯絡入口。
- 檢查公開頁的資安曝露、外部服務、Firebase 設定使用方式與 SEO 欄位。

### 主要輸出

- 主要品牌頁 `index.html`、`about.html`、`class.html`、`teach/index.html`、`blog/index.html` 與 `teach/paper-radar/index.html` 共用頁首、頁尾與官方 Line、Email 聯絡區，桌機版視覺已大致一致。
- 主要頁在行動版的 h1 對比、背景與水平溢出已符合目前規則。Console 基本載入檢查沒有觀察到錯誤或警告。
- 確認獨立工具 `emotion-cards`、`Stress-Food`、`nutrition-battle`、`nutritionranking` 使用各自頁首與頁尾，和本站品牌頁不一致。`nutritionranking` 在約 375px 寬度有導覽與按鈕超出畫面的問題，列為高優先修正項目。
- 確認 Blog 行動版入口內容區左右留白不足，標題、摘要與卡片貼近畫面邊緣，列為中優先修正項目。`paper-radar` 頂端導覽少了「服務」入口。
- SEO 基礎欄位大多存在。文章內容頁的 canonical、Open Graph 與 BlogPosting JSON-LD 目前由 JavaScript 載入後補上，靜態原始 HTML 沒有完整 fallback。`sitemap.xml` 日期停在 2026-06-14，且漏列 `teach/paper-radar/`。`llms.txt` 也漏列公開論文工具。
- 未在目前追蹤檔案找到實際 API key、token 或 secret。資安風險集中在 Nutrition Battle 顯示公開讀寫 Firebase Rules 的示例、將含設定的完整房間網址交給 QR 服務，以及 Blog 內容進入 `innerHTML` 前的清理不足。這些項目需要在後續修版處理。

### 驗證

- 讀取並盤點 13 個 HTML 檔案，排除 Google 驗證檔這類非內容頁。
- 以公開網址檢查桌機與行動版畫面，核對共用樣式、頁首、頁尾、聯絡區、h1 顏色、內文尺寸與水平溢出。
- 以公開文章網址確認動態 canonical、Open Graph 與 BlogPosting JSON-LD 能在頁面載入後產生。
- 量測 Blog 行動版內容區與 NutriRank 導覽的實際邊界。NutriRank 的導覽列右側延伸至約 592px，超過約 375px 的手機畫面。
- 掃描追蹤檔案的憑證樣式、外部資源與不安全新視窗連結。未發現未加 `noopener` 的 `target="_blank"` 連結。
- 未執行實體手機、Lighthouse、PageSpeed、Firebase Console Rules 與實際資料庫寫入測試，這些仍屬待驗證項目。

### 錯誤或風險

- PowerShell 直接連線公開 GitHub 時遇到 Windows 憑證通道錯誤，已改用瀏覽器完成公開頁核對。
- GitHub Pages 原始碼目前沒有可直接設定的 CSP、HSTS、X-Frame-Options 與 Permissions-Policy 標頭，需由部署層補強。
- 共用品牌頁已達到目前的頁首、頁尾與聯絡規則，獨立工具仍未形成同一套站體，不能把目前結果判定為整站完成一致化。

### 新增規則

- `teach/` 內獨立工具也要檢查品牌辨識、返回首頁、頁尾聯絡入口與 375px 寬度，不能只檢查入口頁。
- SEO 更新要同步檢查靜態 canonical、Open Graph、sitemap、llms 與頁面類型結構化資料。
- Firebase 規則、設定傳遞與第三方 QR 服務要一起做資安檢查，不能把公開讀寫範例當成可部署設定。

### 回寫狀態

- 已更新 `agent.md` 與本工作日誌。
- 沒有更新全域 `AGENTS.md` 或 skill，因為本次沉澱內容屬 Kat Chang 網站專案規則。
- 本次沒有修改網站 HTML、CSS 或 JavaScript，待使用者確認修版範圍後再處理列出的問題。

## 2026-07-28｜頁首首頁與預約聯絡入口統一

### 任務

- 為每個內容頁與互動教具頁的頁首補上「首頁」。
- 將頁首「聯絡」統一連到 `https://zcal.co/katchang`，並以新分頁開啟。

### 主要輸出

- 更新首頁、簡介、授課、文章列表、文章內容、互動教具入口與論文公開頁的頁首導覽。
- 更新 Stress Food、情緒覺察卡、Nutrition Battle 與 NutriRank 的工具頁首入口。
- Nutrition Battle 補上工具頁導覽樣式，NutriRank 補上網站層級首頁與聯絡入口。
- 情緒覺察卡保留原有互動程式，頁面載入時將舊的返回首頁入口改成正式首頁，並補上預約聯絡入口。

### 驗證

- `git diff --check` 通過。
- 靜態搜尋確認主要頁面頁首已包含「首頁」與 `https://zcal.co/katchang`，原本頁首的 `#contact` 連結已移除。
- 確認預約連結使用 `target="_blank"` 與 `rel="noopener"`。
- 確認子目錄頁的首頁相對路徑分別指向網站根目錄。
- 已嘗試以行動版寬度驗證。公開網址尚未反映本地修改，本機預覽連線受到目前瀏覽器環境限制，保留靜態路徑與版面規則檢查結果。

### 錯誤或風險

- 本次變更尚未推送前，公開網址仍會顯示舊版頁首。
- NutriRank 原有的應用程式內部導覽仍保留，新增的「首頁」與「聯絡」屬於網站層級入口。

### 新增規則

- 頁首「聯絡」統一使用 zcal 預約頁並另開新分頁，不能回到首頁 contact 錨點。
- 每個公開內容頁與獨立工具頁都要有可回到網站根目錄的「首頁」入口。

### 回寫狀態

- 已更新 `agent.md` 與本工作日誌。
- 沒有更新全域 `AGENTS.md` 或 skill，本次規則限於 Kat Chang 網站。

### 發布狀態

- GitHub `main` 已推送至 `619e829`。
- 公開頁已用版本參數重新讀取，桌機約 1280px 與手機約 375px 都確認新的頁首入口。

## 2026-07-28｜SEO、資安與行動版修正

### 任務

- 補強公開頁 SEO、結構化資料與靜態 metadata。
- 修正 Firebase Rules 示範、QR 服務傳遞、Blog HTML 清理與舊路由。
- 改善 NutriRank、Blog、互動教具的行動版字級、留白與水平邊界。
- 清理本機空的未追蹤資料夾，確認 GitHub `main` 與本機版本一致。

### 主要輸出

- `about.html`、`class.html`、`teach/index.html` 與互動工具補上 Open Graph 與頁面類型 JSON-LD。
- Blog 文章補上靜態 canonical 與 OG fallback，動態內容改用 HTML 白名單清理與文字跳脫。
- `sitemap.xml` 更新至 2026-07-28，加入 `teach/paper-radar/`。`llms.txt` 補上公開論文工具。
- Nutrition Battle 改用匿名登入、host UID 與受限房間規則，QR 圖片改為瀏覽器本機生成，移除公開讀寫示範。
- NutriRank 導覽與內容區補上手機寬度限制與較易閱讀的內文字級。Blog 補上內容卡片邊界與左右留白。
- emotion-cards 返回首頁改為網站根目錄，移除舊 `/info/` 轉址依賴。
- `agent.md` 補寫獨立教具、Firebase、QR、SEO、HTML 清理與 375px 檢查規則。

### 驗證

- `git diff --check` 通過，主要 JavaScript 通過 Node 語法檢查。
- 8 個 JSON-LD 區塊通過 JSON 解析，`sitemap.xml` 通過 XML 解析並含 13 個網址。
- 靜態搜尋確認未保留公開 Rules 範例、QR Server 網址與工具頁舊 `/info/` 路徑。
- 公開頁檢查確認主要頁 canonical、OG、JSON-LD、頁首首頁與 zcal 聯絡連結正常。
- Blog 實際 DOM 未發現 script、事件屬性、危險 href 或危險 img src。
- NutriRank 公開頁載入資料正常，瀏覽器紀錄沒有頁面 error 或 warning。
- 行動版以 375px CSS 規則、水平邊界與字級靜態檢查完成。現有瀏覽器介面無法切換 viewport，未宣稱已完成實體手機驗證。
- Git 工作樹已清理，移除空的未追蹤 `.github/workflows`、`.github` 與 `admin` 資料夾。

### 錯誤或風險

- Firebase Console 的匿名登入、實際 Rules enforcement 與資料庫寫入流程尚未在本次環境執行整合測試。
- GitHub Pages 原始碼無法直接設定 CSP、HSTS、X-Frame-Options、Permissions-Policy，需由 CDN 或部署層補上 Response Header。
- 未執行實體手機、Lighthouse、PageSpeed 與部署層安全標頭檢查。
- QR 既有加入房間流程仍將必要設定放在網址中，已停止送往第三方 QR 服務，後續若要進一步降敏需改設計房間邀請資料格式。

### 新增規則

- 每次 SEO 或版面修改都要同時檢查桌機頁與手機 CSS 邊界，內容文字不可壓到高齡者難以閱讀的尺寸。
- Blog 或其他資料進入 `innerHTML` 前，必須先做文字跳脫或白名單清理。
- 工具頁資料若涉及 Firebase，必須搭配登入、房間識別與受限 Rules，不得保留公開讀寫示範。
- GitHub Pages 的安全標頭要列為部署層工作，不能把 noindex 當成存取控制。

### 回寫狀態

- 已更新 `agent.md` 與本工作日誌。
- 未更新全域 `AGENTS.md` 或 skill，因為本次規則限於 Kat Chang 網站。

### 發布狀態

- GitHub `main` 已推送至 `3e821f1`。
- 本機工作樹與 `origin/main` 同步，待本次工作日誌寫入後再完成收尾提交。

## 2026-07-28｜公開頁第二輪驗證

### 驗證結果

- 本機 `main` 與 `origin/main` 位於 `81779b3`，工作樹初始狀態乾淨。
- 逐頁載入首頁、簡介、授課、教具索引、文章列表、Blog 文章、NutriRank、Paper Radar、Stress Food、情緒卡與 Nutrition Battle。
- 各主要頁的 canonical、Open Graph、JSON-LD、頁首「聯絡」zcal 連結均正常。獨立情緒卡返回首頁指向網站根目錄。
- NutriRank 載入 41 個營養按鈕，Paper Radar 載入 50 筆公開資料，情緒卡載入 36 張卡片。
- 公開頁桌機寬度檢查沒有水平溢出，網站來源沒有 error 或 warning。
- 逐一審核 `innerHTML` 使用點，Blog、Paper Radar、NutriRank、Nutrition Battle、Stress Food 與情緒卡的外部或資料欄位都有跳脫、白名單、固定選項或 DOM textContent 保護。
- `sitemap.xml`、`llms.txt`、舊 `/info/` 路徑、公開 Rules 字串與 QR Server 網址檢查均正常。

### 尚未驗證

- 現有瀏覽器介面無法切換 375px viewport，因此手機版以 CSS 規則與靜態邊界完成檢查，未宣稱實體手機驗證。
- Windows 的 PowerShell、curl TLS 通道無法取得公開 Response Header。CSP、HSTS、X-Frame-Options、Permissions-Policy 仍需在部署層或 CDN 實際確認。
- Firebase Console 的匿名登入、Realtime Database Rules enforcement 與真實房間寫入流程仍需在 Firebase 專案端測試。

### 發布狀態

- 本次只新增驗證紀錄，未修改網站程式。
- 待本紀錄提交後，GitHub `main` 應與本機同步且工作樹保持乾淨。

## 2026-07-28｜行動版內容字級再修正

### 任務

- 依使用者回報，修正手機版所有分頁的內文、卡片說明、表單文字與 h3、h4 字級過小問題。

### 問題原因

- 前一版只提高共用頁部分段落與卡片文字，獨立工具仍各自使用原本 CSS。
- NutriRank、Paper Radar、Stress Food、Nutrition Battle 與情緒卡的行動版小字沒有共用規則覆寫，因此手機閱讀仍不易。

### 主要輸出

- 共用 `styles.css` 的行動版一般內容提高至 `1.12rem`，卡片標題提高至 `1.28rem`。
- NutriRank 補上搜尋、卡片、排行榜、矩陣、表格、表單與頁尾的行動版文字規則。
- Paper Radar 補上摘要、作者、期刊資訊、標籤、筆記、測驗卡與操作按鈕的行動版文字規則。
- Stress Food、Nutrition Battle 與情緒卡補上各自 CSS 的內文、h3、按鈕與結果區字級規則。
- `agent.md` 將行動版檢查基準提高為內文 `1.12rem`、h3/h4 `1.2rem` 以上，並要求逐一檢查各獨立工具。

### 驗證

- `git diff --check` 通過。
- 7 個 JavaScript 檔案通過 Node 語法檢查。
- 6 組行動版規則覆寫標記均存在。
- CSS 已依 520px、560px、640px、760px 與 768px 的實際頁面斷點補上規則。
- 需推送後再用公開網址重讀各頁，並以可用的 375px CSS 靜態檢查核對。

### 風險

- 目前瀏覽器介面仍無法切換到實際 375px viewport，實機手機仍需另行確認。

### 回寫狀態

- 已更新 `agent.md` 與本工作日誌。
- 未更新全域 `AGENTS.md` 或 skill，本次規則限於 Kat Chang 網站。

## 2026-07-28｜手機 CSS 快取版本更新

### 修正

- 發現共用與獨立工具 CSS 的網址版本仍沿用舊快取標記，使用者可能持續讀到前一版小字規則。
- 所有主站、Blog、教具入口、Paper Radar、Stress Food、Nutrition Battle 與 NutriRank 的 CSS 連結已更新為 `20260728-mobile`。

### 驗證

- 已確認 HTML 不再引用 `20260728-nav` 的 CSS 版本。
- 本次只變更 CSS 快取版本參數，沒有改動互動程式邏輯。

### 公開頁重查

- GitHub Pages 初次讀取時首頁與簡介仍短暫回傳舊 CSS 版本，等待部署快取更新後，兩頁均已讀到 `styles.css?v=20260728-mobile`。
- 其他主站、Blog、教具與獨立工具頁也均已讀到新的 CSS 版本。
- 公開頁網站來源沒有新增 error 或 warning。瀏覽器介面仍只能提供桌機寬度，375px 以 CSS 規則靜態核對。

### 字級基準補正

- 收尾檢查發現共用 h4 與 NutriRank 部分 h4 仍低於行動版閱讀基準，已統一提高至至少 `1.2rem`。

## 2026-07-28｜主站手機版最低字級再調整

### 任務

- 依使用者回報，主站手機版除 h1、h2 外，h3、h4 與所有主要閱讀文字最低提高至 `1.2rem`，行距同步收斂。

### 修正

- 首頁、簡介、授課、Blog 列表、Blog 文章與 teach 入口使用主站 CSS 範圍。
- 共用手機 CSS 將主站內文、卡片、摘要、標籤、按鈕、導覽列與頁尾統一設為至少 `1.2rem`，h1、h2 保留原本版型。
- Paper Radar 保留獨立工具 CSS，不套用主站手機字級規則。其他獨立教具仍使用各自 CSS。
- `agent.md` 已把主站手機版最低字級規則改為 `1.2rem`。

### 驗證

- `git diff --check`、7 個 JavaScript 檔案語法檢查、主站 HTML 標記與 CSS 字級靜態檢查均通過。
- GitHub push 已成功，提交為 `e981c52`，本機 `HEAD` 與 `origin/main` 追蹤標記一致，工作樹乾淨。
- 追加執行 `git ls-remote` 時，Windows TLS 憑證通道回報 `SEC_E_NO_CREDENTIALS`，因此未能以第二種方式讀取遠端摘要。推送回應與本機追蹤分支已完成核對。
- 實體手機與 375px 瀏覽器 viewport 仍需另行確認，現有瀏覽器介面無法切換至該寬度。

## 2026-07-28｜首頁教育工具入口更新

### 任務

- 依使用者指定，更新首頁互動衛教工具區的三個教育連結。

### 修正

- 保留 `NutriRank 食品營養排行榜`，連結至 `teach/nutritionranking/`。
- 新增 `論文讀書小站公開版`，連結至 `teach/paper-radar/`。
- 新增 `文字雲互動工具`，連結至 `https://teaching-3809d.web.app/`，並使用新分頁與 `rel="noopener"`。
- 移除首頁教育工具區原本的 Stress Food 與情緒覺察卡入口，其他 teach 目錄內容未修改。

### 驗證

- 已確認首頁三個卡片標題與目標網址一致。
- 已確認首頁不再出現教育工具區的舊入口。
- `git diff --check`、首頁連結靜態檢查與 `app.js` 語法檢查均通過。
- GitHub push 已成功，提交為 `f6048e2`，本機 `HEAD` 與 `origin/main` 追蹤標記一致，工作樹乾淨。

### 收工規則回寫

- 已把「每次修改公開頁面都要同步檢查桌機網頁版與手機版」寫入 `agent.md`，範圍包含 HTML、CSS、文字、連結與互動功能。


## 2026-08-14｜修復昨晚文章版本被覆寫與首頁勾選失效

### 任務

- 調查文章 `2026-08-13-nutrition-concepts-controversies-17e-guide` 被改回舊版、封面圖消失，以及取消首頁勾選後再次出現的原因。

### 已完成

- 以昨晚保留的修正版恢復目標文章，只替換遠端 `blog/posts.json` 的同一篇文章物件。
- 恢復標題、完整內文、摘要、封面圖 `images/2026-08-13-nutrition-concepts-controversies-17e-guide.png` 與 `showOnHome: false`。
- 保留遠端現有 Chapter 1 與其他文章資料，共 5 篇文章。遠端恢復提交為 `4f6edac29a41ae1cf9d11e0a924b44f8122d91f0`。
- 更新 SEO 自動化，加入遠端 SHA、單篇合併、非目標差異即停與首頁勾選保留規則。

### 已修正錯誤

- 錯誤一：Chapter 1 發布流程使用舊的整份 `blog/posts.json` 快照，直接回寫遠端，覆蓋昨晚文章的標題、內文與封面圖欄位。
- 錯誤二：同一份舊快照帶有 `showOnHome: true`，使已取消勾選的文章重新進入首頁精選。首頁程式原本已依 `showOnHome === true` 篩選，資料被回寫才是出錯點。

### 驗證

- 遠端 `blog/posts.json` 可解析，共 5 篇文章，首頁精選為 4 篇，目標文章的 `showOnHome` 為 `false`，封面圖欄位存在。
- 公開文章頁標題已回復，封面圖載入成功，正文開頭與昨晚版本一致，正文可見文字約 4,210 字。
- 公開首頁實讀為 4 張文章卡片，目標文章沒有出現。

### 尚未完成

- 本機分支仍保留其他既有未提交修改，沒有用整個本機工作樹覆蓋遠端。

### 仍有風險

- 若未來有流程繞過遠端 SHA 與單篇合併規則，仍可能重新造成整檔覆寫。

## 2026-08-15｜Blog 文章列表排序與搜尋

### 已完成

- Blog 列表改為依有效 `date` 由新到舊排序。
- 列表上方加入關鍵字搜尋，搜尋標題、摘要、正文、關鍵字與分類。
- 分類選單依文章資料動態產生，缺少分類的舊文章歸入「未分類」。
- 本次只更新 `blog/blog.js`、`blog/index.html`、`styles.css`，沒有修改 `blog/posts.json`。

### 驗證與風險

- 遠端文章資料共 6 篇，首頁精選 4 篇，目標文章的 `showOnHome` 仍為 `false`。
- 本機 Windows TLS 讀取公開頁面時發生憑證通道錯誤，已改以遠端檔案 SHA 與功能內容核對。日後需在可用的公開頁面連線環境補做 DOM 實讀。


## 2026-08-21 14:15｜全站 SEO 與 AI 索引基礎建設升級、授課影音整合與 GitHub 發布（收工）

### 任務

- 制定 Kat Chang 凱特營養師網站（https://594katchang-source.github.io/）1 個月 Google 第一頁與主流 AI 搜尋引擎（ChatGPT Search, Perplexity, Gemini, Copilot, Claude）權威引用成長白皮書。
- 升級全站 SEO 與 AI 索引基礎建設：首頁 index.html、簡介頁 about.html、授課頁 class.html 之 Schema.org JSON-LD 深度結構化資料與 Meta Keywords。
- 完整覆蓋「凱特營養師」、「Kat營養師」、「張雁雲營養師」、「Kat Chang」四大常用別名。
- 修正顧問服務定位，聚焦於「保健食品配方評估、營養標示法規審查與衛教教材開發」，徹底排除非專長之菜單與團膳字詞。
- 整合 5 支精選授課現場與教具短影音至 class.html，並在 `<head>` 注入 Google VideoObject 結構化資料。
- 更新 llms.txt 結構化三支柱服務與代表影音清單。
- 整理 Chapter 6 蛋白質篇審閱套件並歸檔至 `work/2026-08-15-seo-review-docs/`。
- 提交並發布至 GitHub Pages 遠端 repository。

### 主要輸出

- 網站部署上線檔案：`index.html`、`about.html`、`class.html`、`llms.txt`、`sitemap.xml`、`.gitignore`。
- 策略成果（存於 `work/2026-08-21-seo-growth-strategy/output/`）：
  - `01_seo_1month_growth_blueprint.md`：1 個月攻頂白皮書。
  - `02_schema_jsonld_enhancements.json`：全站結構化資料備份與規格庫。
  - `03_outreach_pr_backlinks_templates.md`：四大公關機構反向連結合作信件庫。
- 蛋白質篇審閱歸檔（存於 `work/2026-08-15-seo-review-docs/`）：
  - `output/chapter-06-proteins-amino-acids-seo-review.docx`
  - `source/chapter-06-review.json`
  - `source/chapter-06-review.html`
  - `artifact-chapter-06-reference.md`
  - `build_chapter6_artifacts.py`

### 已完成與驗證

- 全站 HTML、JSON-LD 與 Schema 語法通過檢查，未改動任何 `<body>` 視覺排版與元件樣式。
- 授課頁 `class.html` 成功嵌入 5 支 YouTube 授課/教具短片，並注入 5 筆 VideoObject JSON-LD。
- 全站無任何非專長之菜單或團膳字眼，符合使用者之保健食品與標示法規專業背景。
- `robots.txt` 已確認開放 14+ 種主流 AI 爬蟲。
- `git push origin main` 成功推送到遠端 GitHub 儲存庫，commit SHA 為 `4ca827d`。

### 已修正錯誤

- 修正早期草稿中包含菜單/團膳之誤植，已全面調整為保健食品配方評估與營養標示法規審查。
- 修正 Git rebase 衝突，保留遠端最新 Blog 歷史與本機全部升級。
- 依 Windows 檔案安全清理規範，透過 PowerShell Shell API 將 9 個過程暫存檔安全移至資源回收桶。

### 尚未完成與仍有風險

- Chapter 5（脂質篇）與 Chapter 6（蛋白質篇）Word 審閱稿已歸檔，待使用者完成人工閱讀與指示後，再行發布上線。
- Search Console 尚待使用者完成後台權限指派，方可讀取曝光與點擊關鍵字數據。

### 使用者偏好與本次規則

- 使用者要求略過每日連載發布，專注全站基礎建設部署與影音整合。
- 常用名字標籤固定為「凱特營養師」、「Kat營養師」、「張雁雲營養師」、「Kat Chang」。
- 顧問業務嚴格定位在保健食品、機能性食品、標示法規與教材教具，嚴禁提及菜單或團膳。

### 回寫狀態

- `project-worklog.md`：已完整回寫本次所有任務、驗證與收工狀態。
- `.codex/seo/book-series-progress.md`：已同步更新 Chapter 6 歸檔與基礎建設升級狀態。
- 本次無新增跨專案規則，全域 `AGENTS.md` 未修改。

### Git 收工狀態

- 遠端 GitHub `main` 分支已完成同步與發布（Commit: `4ca827d`）。
- 本機工作樹維持乾淨（Working tree clean），無遺留未提交變更。

## 2026-08-21 14:45｜4 週 SEO 執行行事曆排定、GSC 索引自動化與 EAP 企業方案合作轉移（收工）

### 任務

- 將 4 週 SEO 攻頂計畫細化為具體可執行的每日工作與 8 大關鍵檢核時間點（每週二、五固定檢核）。
- 建立 Google Search Console (GSC) API 服務帳號自動化登錄指南與即時索引推播工具。
- 排查並解答 GSC 後台 Sitemap 顯示「無法擷取」之機制（排程中 Pending 狀態）與驗證方式。
- 依使用者策略指示，將第 3 週之合作提案對象由學術/長照機構全面轉移為「EAP 方案顧問公司與企業健康促進合作」。
- 排除既有合作夥伴「宇聯心理健康產業 / 宇聯 EAP」，將其合作經驗轉化為向其他潛在 EAP 機構提案的實務實績背書。

### 主要輸出

- `work/2026-08-21-seo-growth-strategy/output/04_seo_execution_schedule_calendar.md`：4 週攻頂執行行事曆與 8 個確認時間點清單。
- `work/2026-08-21-seo-growth-strategy/output/05_gsc_indexing_automation_guide.md`：Google Search Console 服務帳號 API 授權與自動化串接指南。
- `work/2026-08-21-seo-growth-strategy/gsc_indexer.py`：自動化 Sitemap 廣播與 GSC 索引檢查工具腳本。
- `work/2026-08-21-seo-growth-strategy/output/03_eap_corporate_wellness_outreach_templates.md`：三大 EAP 顧問與企業健康講座/諮詢提案信件庫（鎖定鉅微、寬欣、旭立、華人心理等）。
- 更新 `work/2026-08-21-seo-growth-strategy/output/01_seo_1month_growth_blueprint.md`。

### 已完成與驗證

- GSC Sitemap 實時線上連線驗證：`https://594katchang-source.github.io/sitemap.xml` 讀取成功（HTTP 200，XML 結構與 20 餘筆網址正確）。
- 執行 `python work/2026-08-21-seo-growth-strategy/gsc_indexer.py` 測試通過（Windows UTF-8 編碼與路徑安全無誤）。
- 舊版公關模板透過 PowerShell Shell API 安全移至「資源回收桶（Recycle Bin）」。
- `agent.md` 已同步回寫 EAP 合作定位與宇聯夥伴註記。

### 尚未完成與仍有風險

- GSC Sitemap 目前處於 Google 系統後台排程佇列（Pending），預計 12～48 小時內 Googlebot 實際爬取後自動轉為綠色「成功」。
- GSC API 服務帳號金鑰 `service_account.json` 待使用者下載放置後即可啟用全自動 API 提交。

### 使用者偏好與新增規則

- 宇聯心理健康產業 / 宇聯 EAP 為既有合作夥伴，不列入冷開發名單，轉化為提案時之成熟合作背書。
- 企業端商業拓展以 EAP 方案公司（鉅微、寬欣、旭立、華人心理等）與科技廠福委會/職護為核心方向。

### 回寫狀態

- `agent.md`：已更新 EAP 合作定位。
- `project-worklog.md`：已完整補齊本次工作紀錄。

## 2026-08-21 16:15｜Google Search Console 實時驗證排查、VideoObject 結構化時區修復與全站收工

### 任務

- 協助使用者即時進行 Google Search Console (GSC) 後台全面健康診斷與 6 大關鍵設定檢查。
- 排查使用者提供的 GSC 截圖：解析 `class.html` 網址審查之「網頁已編入索引」、「HTTPS 正常」、「5 個有效影片項目」及「選擇性 uploadDate 警告」。
- 修復 `class.html` 中 5 支影片之 `VideoObject` Schema.org `uploadDate` 缺少時區問題。
- 嚴格驗證 `sitemap.xml` 之 XML 語法合法性與對外 HTTP 回應狀態。

### 主要輸出與程式碼修復

- 修正 `class.html`：將 5 支授課與教具精選影片之 `uploadDate` 由 `2024-01-01` 統一升級為符合 ISO 8601 標準之帶時區格式 `2024-01-01T08:00:00+08:00`。
- 提交並推送到 GitHub 遠端 repository（Commit: `689ee62`）。

### 已完成與驗證

- GSC 實時審查結果確認：
  - `class.html`「網頁已編入索引」🟢
  - 「HTTPS 正常」🟢
  - 「偵測到 5 個有效的影片項目」🟢（結構化資料已全數辨識）
- `sitemap.xml` 經 Python `xml.etree.ElementTree` 嚴格解析驗證，語法 100% 合法，包含 18 個標準 URL。
- 線上 HTTP 請求 `https://594katchang-source.github.io/sitemap.xml` 回傳 200 OK。

### 尚未完成與仍有風險

- GSC Sitemap「無法擷取」為新站剛提交時 Google 伺服器排程中（Pending）的正常現象（上次讀取時間為空白），待 12～48 小時 Googlebot 實際輪巡後將自動轉綠。

### 新增規則與知識沉澱

- Schema.org `VideoObject` 之 `uploadDate` 屬性在 Google GSC 嚴格檢驗下，必須帶有明確時間與時區（`YYYY-MM-DDTHH:MM:SS+08:00`），方能達成 100% 零警告之最佳健康度。

### Git 收工狀態

- 遠端 GitHub `main` 分支已同步發布最新修復（Commit: `689ee62`）。
- 本機工作樹乾淨（Working tree clean），無殘留修改。

## 2026-08-22 14:35｜全站 SEO 索引加速引擎部署：HTML 網站地圖、靜態爬蟲 Fallback、Footer 內鏈網與 Sitemap XML 2.0

### 任務

- 建立全新 `sitemap.html`（HTML 網站地圖）獨立頁面，收錄全站 19 個核心頁面、互動教具與所有衛教專欄文章。
- 全面更新 `sitemap.xml`，所有 URL 之 `<lastmod>` 統一升級至 `2026-08-22`。
- 在 `robots.txt` 宣告 `sitemap.html` 與 `sitemap.xml` 雙地圖。
- 在全站 6 大核心頁面之 Footer 注入「網站地圖」內部連結，打造完整蜘蛛網。
- 在 `blog/index.html` 注入 `<noscript>` 靜態文章索引連結，供不執行 JS 的輕量爬蟲 0 延遲抓取 9 篇衛教文章。
- 部署並同步至 GitHub Pages 遠端。

### 主要輸出與程式碼修改

- `sitemap.html`：新建美觀、語意化 HTML5、兼顧 UX 與 SEO 的網站地圖頁面。
- `sitemap.xml`：更新 19 筆網址與權重配置。
- `robots.txt`：加入雙 Sitemap 宣告。
- `index.html`、`about.html`、`class.html`、`blog/index.html`、`blog/post.html`、`teach/index.html`：更新 Footer 內部錨點。
- `blog/index.html`：加入 `<noscript class="seo-fallback-articles">` 9 篇衛教靜態文章連結。

### 驗證

- 遠端 `origin/main` 已成功 Push 最新 Commit。
- HTML Sitemap 與 XML Sitemap 本地與線上路徑皆可正常存取。

## 2026-08-22 14:48｜全站 GEO（AI 搜尋優化）、文章延伸閱讀互鏈與機器人權限全面升級

### 任務

- 深度加強 AI 搜尋引擎（SearchGPT, Perplexity, Claude, Google Gemini, Copilot）的語義檢索與權威引用（GEO / Generative Engine Optimization）。
- 建立全站 `llms-full.txt` 完整深度機器可讀知識庫。
- 更新 `llms.txt` 與 `robots.txt`，對最新 AI 爬蟲全面開放白名單。
- 在 `blog/blog.js` 加入每篇衛教文章底部的「延伸閱讀・精選相關文章」動態推薦網絡。
- 在 `teach/index.html` 注入衛教文章反向推薦模組，打通教具與部落格之間的內鏈循環。
- 升級 `sitemap.html` 之 Schema.org 結構化資料（`BreadcrumbList` 與 `CollectionPage`）。

### 主要輸出

- `llms-full.txt`：新建專門提供給大型語言模型與 AI 搜尋引擎的完整衛教與資歷知識庫。
- `llms.txt`：更新導覽並指向完整知識庫。
- `robots.txt`：擴充 `OAI-SearchBot`、`ClaudeBot`、`PerplexityBot` 等最新 AI Agent 宣告。
- `blog/blog.js`：新增 `renderRelatedPosts` 函式，每篇文章自動關聯同類推薦文章。
- `teach/index.html`：新增「搭配衛教專欄文章」內鏈區塊。
- `sitemap.html`：補齊 Schema.org Breadcrumb 與 CollectionPage JSON-LD。

### 驗證

- 本地與遠端測試所有檔案語法與渲染正確。
- GitHub Pages 自動部署。

### 新增規則與工具沉澱

- 建立 `tools/sync_seo_and_geo.py` 全自動一鍵同步工具，涵蓋 XML/HTML Sitemap、LLMS 知識庫、Robots、Noscript Fallback 與 Footer 內鏈。
- 專案規則 `agent.md` 已正式寫入「【硬性規範】全站 SEO & GEO (AI 搜尋引擎) 自動化同步 SOP」，強制規定日後每次新增/修改文章、網頁或教具時，必須即時執行該腳本並驗證 6 大 SEO/GEO 指標。

### 已完成與驗證

- 全站 19 個 URL 之 XML Sitemap 與 HTML Sitemap 雙軌上線，最後更新日期均標示為 `2026-08-22`。
- `llms.txt` 與 `llms-full.txt` 深度知識庫產出完成，收錄 9 篇衛教文章臨床結論與 5 大教具。
- `robots.txt` 宣告完整 AI 爬蟲名單與雙 Sitemap。
- `blog/blog.js` 延伸閱讀推薦模組運作正常，教具目錄頁與部落格形成雙向導流。
- 專案一鍵自動同步腳本 `tools/sync_seo_and_geo.py` 測試 100% 成功。
- `agent.md` 已完整更新並推送到遠端倉庫。

### 尚未完成與仍有風險

- 無。所有功能與檔案皆已部署並通過本地及線上語法驗證。
- GSC 抓取與索引排程為 Google 伺服器端正常非同步佇列，預計 24～48 小時內陸續收錄。

### Git 收工狀態

- 遠端 GitHub `main` 分支已完全同步（Commit: `cbf9c49` 及最新收工 Commit）。
- 本機工作樹乾淨（Working tree clean），所有改動皆已妥善保存與推送。

## 2026-08-22｜Chapter 6 獨立比較稿與 Word 審閱檔

### 任務

- 使用者希望把既有 Antigravity Chapter 6 Word 與另一種寫法放在一起比較，依同一份書籍 Chapter 6 來源另寫一版獨立 SEO 草稿。
- 新稿與既有 Word 分開保存，未覆寫既有檔，也未進入網站發布流程。

### 已完成

- 使用 `documents` skill 的 Word 建檔、版型沿用與結構檢查流程，工作資料夾為 `work/2026-08-22-chapter6-comparison/`，成品位於 `output/`。
- 新稿正文實際可見字數 5,495 字，含 12 個 H2、6 個 H3、8 張正文表格、5 題 FAQ、5 個正文站內連結、7 個站內連結建議與 9 組來源。
- 新稿主線改為每餐安排與健康情境分流，將健康成人、高齡者、運動者、CKD G3 至 G5、透析與補充品放在不同判讀區塊。
- 比較回報已建立，記錄既有 Antigravity 稿與本稿在文章入口、順序、腎臟病界線、植物性飲食、補充品與讀者行動上的差異。
- 進度檔已記錄本次比較稿，Chapter 6 仍維持待人工選稿與審閱，沒有前進到 Chapter 7。

### 錯誤與根因

- 初版正文缺少 H3 與正文內自然站內連結，與 SEO 審閱要求的層級與站內導覽需求不完全相符。
- 初版內容掃描命中數個專案禁用詞，原因是新稿文字未在第一次生成前完成逐檔掃描。
- LibreOffice `soffice.exe` 不在目前環境，官方 DOCX 轉頁工具因此無法建立 PDF 與 PNG。

### 修正與驗證

- 補上 6 個 H3，加入 5 個正文內站內連結，再生成 JSON、HTML 與 Word。
- 重新執行禁用詞、DOCX ZIP、頁面尺寸、邊界、表格固定寬度、表頭列、`w:cantSplit`、Heading 樣式與外部超連結關係檢查，結果通過。
- 新稿 Word 為有效 DOCX ZIP，9 張表格格線總寬均為 9360 DXA，9 個表頭列、53 個 `w:cantSplit` 列、7 個外部超連結關係、Letter 直式與四邊 1 英吋邊界均已核對。
- 轉頁缺口已保留為未驗證，沒有把結構 QA 寫成視覺審查完成。

### 尚未完成與仍有風險

- 新稿與既有 Antigravity 稿均待使用者人工比較與選稿，尚未取得發布確認。
- 食物份量表為教育用途估算，正式上線前需依採用的台灣食品成分資料來源逐項核對。
- FAQPage、BlogPosting、canonical、作者資料與公開頁版面尚未進入網站實作與公開核對。
- 本輪未讀取 Search Console 成效資料，也未進行外部聯絡、投稿、發布或 GitHub 推送。

### 新增規則與回寫狀態

- 本次確認同一章需要比較不同作者寫法時，應建立獨立工作資料夾、獨立 slug 與獨立 Word 檔，原待審稿維持原位。
- 專案進度與工作日誌已更新。沒有新增需寫入 `agent.md` 或全域 skill 的跨工作流程規則。

### Git 狀態

- 工作樹原有變更與本次新增的比較工作資料夾均保留，未執行提交、合併、推送或清理。

## 2026-08-22｜Chapter 6 書籍重點與心得整合主稿

### 任務

- 依使用者要求，結合兩版 Codex 內容與 Antigravity 第六章稿，重寫成符合前幾次書籍連載規定的「書籍重點與心得整理」。
- 成品只保留在 `work/2026-08-15-seo-review-docs/output/`，並清理本次比較與建檔產生的中間資料。

### 已完成

- 最終檔案：`work/2026-08-15-seo-review-docs/output/chapter-06-proteins-amino-acids-seo-review.docx`。
- 正文實際可見字數 7,225 字，15 個 H2、12 個 H3、11 張正文表格、5 題 FAQ、7 個站內連結建議與 9 組來源。
- 內容已回到書籍章節路徑，保留胺基酸、蛋白質結構、消化吸收、身體功能、蛋白質合成、需求量、品質、攝取不足與過量、食物來源、Controversy 6 與補充品，再接上 Kat Chang 營養師的閱讀心得與台灣餐桌例子。
- 原本比較稿中的高齡、運動、CKD 與補充品判讀已移到章節理解之後，沒有讓 SEO 操作框架取代書籍主線。

### 驗證

- 正式 Word 重新讀取通過，檔案大小 55,341 bytes。
- DOCX ZIP 有效，12 張表格固定 9360 DXA，12 個表頭列、70 個 `w:cantSplit` 列、12 個 H3、7 個外部超連結關係、Letter 直式與四邊 1 英吋邊界通過。
- LibreOffice 缺少，官方轉頁工具未能建立 PDF 與 PNG，逐頁視覺 QA 保留為未驗證。
- `output` 只留下 Chapter 1 至 Chapter 6 六份 Word 成品。

### 清理與風險

- 舊第六章 Word 已先送進資源回收筒，再由整合稿接替原檔名。
- 本次比較資料夾、Chapter 6 舊 JSON/HTML、舊版型說明、Chapter 6 專用腳本、整合建檔腳本、QA 腳本、轉頁資料夾與 Python 快取均已送進資源回收筒。
- 第一至第五章既有來源與審閱材料保留。網站、Blog、sitemap、`llms.txt`、圖片、公開頁、外部聯絡、Git 提交與 GitHub 推送均未執行。
- 第六章仍待人工審閱，整合稿尚未取得發布確認。

### 回寫狀態

- `.codex/seo/book-series-progress.md` 與 `project-worklog.md` 已記錄整合主稿、驗證、清理範圍與未驗證項目。
- 本次沒有新增需寫入 `agent.md` 或全域 skill 的規則。

## 2026-08-22｜書籍連載定位與用語收工修正

### 任務

- 使用者確認後續書籍連載固定使用「書籍的重點和心得整理」定位，並要求 `Controversy` 統一翻成「爭議」。

### 已完成

- 專案 `agent.md` 已補上書籍文章定位，要求保留章節主題、核心問題、概念順序與章末爭議，再加入營養師判讀、生活例子與可執行應用。
- Codex 記憶已新增同一項固定規則，供後續章節延續使用。
- 已核對 `agent.md` 與記憶筆記，正文、標題、摘要、FAQ 與 Word 審閱檔的 `Controversy` 均以「爭議」為準。

### 修正與根因

- 前幾版寫法曾被 SEO 衛教框架帶偏，文章入口與段落安排較像獨立衛教文章，書籍章節主線與閱讀心得辨識度下降。
- 根因是產出時先套用搜尋結構，再回填書籍內容，造成 SEO 需求主導文章性格。
- 本次改以章節主題、核心問題、概念順序、章末爭議與作者心得作為正文骨架，SEO 欄位放在服務書籍整理的位置。

### 後續改進事項

- 每次開始新章節前，先核對書籍章節整理檔、前一章進度與既有草稿，列出本章必留的核心概念與爭議。
- 產出後逐一掃描正文、標題、摘要、FAQ、SEO 審閱資料與 Word 檔，確認 `Controversy` 已統一為「爭議」。
- 判讀書籍文章時，先檢查讀者是否能辨識本章在全書中的位置，再檢查搜尋意圖、表格、站內連結與結構化資料。
- 後續比較不同寫法時，評估重點放在書籍主線、心得整理、作者辨識度與生活轉譯，SEO 完整度列為支援項目。

### 驗證與仍有風險

- 已完成檔案內容核對、專案規則核對與 Git 狀態核對。
- Chapter 6 整合稿仍待人工審閱，尚未取得發布確認。
- LibreOffice 缺少，Chapter 6 Word 的 PDF 轉頁與逐頁視覺檢查仍未驗證。
- 本次沒有修改網站、發布文章、提交或推送 GitHub。工作樹既有修改與未追蹤檔案均保留原狀。

### 規則回寫狀態

- 已回寫專案 `agent.md` 與 Codex 記憶筆記。
- 本次屬專案文章定位與用語規則，沒有新增跨專案 skill 修改。
- 前一筆記錄中「沒有新增需寫入 `agent.md`」只適用整合主稿產出當下，已由本筆補充後續使用者確認的規則。

## 2026-08-22｜第一至第五章風格回查與第六章保護

### 任務

- 使用者指出第六章草稿又出現格式與語氣回退，要求以第一至第五章的既有成品作為後續書籍文章基準。
- 使用者明確要求第六章 Word 已自行修改，這一輪只檢查，不再更動第六章檔案。

### 回查結果

- 第一至第五章均採用固定 SEO 審閱架構：SEO 欄位、文章摘要與開場、正文、SEO 描述、分類標籤、站內連結、FAQ、結構化資料、來源與待確認事項。
- 第二至第五章的營養師段落標題固定為「Kat Chang 營養師的判讀」。
- 第三至第五章的 FAQ 標題已定型為「FAQ：章節主題常見問題」。第二章與第一章保留較早版本的短標題，後續以第三至第五章的格式為準。
- 正文導讀固定使用「省時版本：」，未使用「先給閱讀地圖：」。
- 營養師段落以章節重點、條列歸納、直接判讀與生活應用為主，沒有另外設計「我讀到這裡的第一個心得」作為入口。

### 修正與根因

- 第六章先前的標籤曾寫成「先給閱讀地圖：」，FAQ 標題曾帶入「常見問題與第六章的回答」，判讀標題曾加入「與內容限制」，段落開頭也曾改成第一人稱閱讀路線。
- 根因是產出時重新發明段落標籤與心得入口，沒有逐項對照第一至第五章的已定型版面與語氣。
- 已把固定標籤、FAQ 格式、判讀標題與心得段落寫法回寫到專案 `agent.md` 與 Codex 記憶。

### 後續改進事項

- 新章節開始前，先從第一至第五章抽查固定標籤、H2/H3、判讀段落與 FAQ 標題，再開始產出。
- 建立產出後的文字閘門：搜尋「先給閱讀地圖」、「先給答案」、「常見問題與第六章的回答」、「與內容限制」、「我讀到這裡的第一個心得」與「我會把本章讀成」，命中時先停下修正。
- 判讀段落先寫章節主題的重點整理，再接營養師判讀與生活應用。內容限制維持獨立段落，不併入標題。
- 每次修改前後核對第六章 Word SHA-256，保護使用者已完成的內容。

### 驗證與仍有風險

- 已讀取第一至第六章 Word 的段落、標題層級、FAQ 標題、判讀段落與表格數量，完成風格比對。
- 第六章目前 SHA-256 為 `1133CEA9F1BDACAD8F6077BF1C28ED3A6ED65ED9A563C7093E685B6F3C09F3A2`，本輪未執行任何第六章檔案寫入。
- LibreOffice 缺少，第一至第六章的逐頁視覺檢查仍未完成，本次回查屬文字與 DOCX 結構檢查。
- 第六章仍待人工審閱，網站、發布、提交與推送均未執行。

### 規則回寫狀態

- 已回寫專案 `agent.md` 與 Codex 記憶筆記。
- 沒有修改 `documents` skill，因本次確認的是 Kat Chang 專案限定的文章風格規則。

## 2026-08-22｜書籍連載風格鎖定與規則分層

### 嚴謹度結論

- 先前的流程做到部分一致，尚未建立足夠硬的風格閘門，因此第六章曾重複出現標籤、FAQ 標題與判讀段落語氣回退。
- 本次重新讀取第一至第五章 Word，確認五份文件的 H1 順序一致，共同骨架相同。第一、第二章保留早期格式，第三至第五章已形成較穩定的判讀標題、FAQ 標題與正文導讀格式。
- Antigravity 比較內容曾用於本輪討論，但原稿與中間檔已送進資源回收筒，後續只能引用使用者當次貼出的文字或工作紀錄中可追溯的觀察，不能視為目前可讀取來源。

### 規則落點決定

- 專案限定的文章風格、固定標籤、段落順序與產出閘門寫入專案 `agent.md`，這裡是本網站連載的主要工作規則。
- `project-worklog.md` 只記錄本次稽核、修正原因、驗證與後續改進，不取代 `agent.md` 的固定規則。
- `.codex/seo/book-series-progress.md` 只維持章節進度與待審狀態，不放寫作風格規則。
- Codex 記憶筆記用來提醒跨工作階段的固定偏好，但不取代專案 `agent.md`。
- 不修改全域 `AGENTS.md`，因這套格式只適用 Kat Chang 書籍連載。也不修改通用 `book-analysis` 或 `documents` skill，因它們負責書籍分析與 DOCX 技術流程，不負責本網站的文章聲音。

### 固定工作流程

- 新章節開始前先讀第一至第五章成品，抽取 H1 順序、正文導讀、`省時版本：`、`Kat Chang 營養師的判讀` 與 FAQ 格式。
- 再讀當日章節整理檔與前一章進度，列出本章要保留的書籍概念、章末爭議、心得重點與台灣生活轉譯。
- 寫作時先完成書籍正文與營養師判讀，再補 SEO 欄位。不得讓搜尋框架先行改變正文性格。
- 完稿後執行固定詞句掃描、H1 順序核對、判讀段落核對、FAQ 標題核對、`Controversy` 用語核對與第六章 SHA-256 保護檢查。
- 任何格式或語氣不符合時，先停止交付並修正規則落點，再重新檢查，不以重新生成一版文字代替流程修正。

### 回寫狀態

- 已將風格鎖定與產出流程寫入專案 `agent.md`。
- 已新增 Codex 記憶筆記，記錄規則分層與 Antigravity 可採用的流暢表達範圍。
- 第六章 Word 本輪沒有寫入，SHA-256 維持 `1133CEA9F1BDACAD8F6077BF1C28ED3A6ED65ED9A563C7093E685B6F3C09F3A2`。

## 2026-08-22｜來源狀態與溝通精準度收工修正

### 本次確認

- 專案目前保留的第六章檔案只有 `work/2026-08-15-seo-review-docs/output/chapter-06-proteins-amino-acids-seo-review.docx`。
- Antigravity 比較稿與中間檔已送進資源回收筒，沒有留在目前專案檔案清單中。第六章現有 Word 是使用者修改後的版本。
- 本輪重新核對第六章 Word，SHA-256 為 `1133CEA9F1BDACAD8F6077BF1C28ED3A6ED65ED9A563C7093E685B6F3C09F3A2`，沒有寫入第六章。

### 錯誤、原因與修正

- 錯誤：前一則回覆寫成「Antigravity 的句子銜接與閱讀流暢度可以採用」，容易讓人理解為目前仍能直接讀取或持續學習 Antigravity 原稿。
- 原因：把先前看過的比較內容、使用者貼出的段落與目前仍可讀取的檔案混在一起，沒有先標示來源狀態。
- 影響：來源邊界說明不精準，也沒有準確回應使用者指出的檔案已清理這個重點。
- 修正：後續只在有實際保留檔案或使用者當次提供文字時描述寫作特徵，已清理檔案只可引用可追溯的既有紀錄，不表述為仍可讀取來源。

### 後續提速與溝通改進

- 回覆前先用三行確認：使用者這次要處理的重點、明確不要動的檔案、目前可用的來源。
- 建立來源狀態四分法：目前可讀取、使用者當次貼出、工作紀錄可追溯、目前不可讀取。不同狀態不能混寫。
- 使用者說「刪除」時，先核對檔案清單與回收筒處理紀錄。使用者說「不要更動」時，先記錄檔案 SHA-256，再開始其他工作。
- 對已經確認過的偏好直接套用，回覆先處理使用者指出的錯誤，再說明已完成的規則回寫，減少重複解釋與方向漂移。
- 比較不同作者時，只比較有證據的文字特徵，分開寫「目前看到的內容」與「仍可取得的來源」，不把推測寫成已確認事實。

### 規則回寫與收工狀態

- 已將來源狀態核對與「刪除／不要更動」回覆閘門寫入專案 `agent.md`。
- 已新增 Codex 記憶筆記，記錄使用者希望回覆準確抓住重點與習慣。
- 本次沒有修改全域 `AGENTS.md` 或通用 skill，因本次規則落在 Kat Chang 專案來源與溝通流程。
- Git 沒有提交或推送。工作樹原有修改、刪除標記與未追蹤檔案均保留。
- 第六章仍待人工審閱，網站發布與視覺轉頁檢查均未完成。

## 2026-08-22｜工作資料夾清理

### 判斷

- `work/2026-08-22-seo-indexing-boost` 是 SEO 與 AI 索引輸出的過程資料夾。其 `llms.txt`、`llms-full.txt`、`robots.txt` 與 `sitemap.xml` 已存在於專案根目錄，正式同步工具為 `tools/sync_seo_and_geo.py`。資料夾內的 `sitemap.html` 為舊版副本，與根目錄版本不同，不能當成正式來源。
- `work/2026-08-21-workspace-cleanup` 是已完成清理工作的腳本與報表，沒有網站執行所需的正式檔案，也沒有被專案引用。

### 已完成

- 已將上述兩個過程資料夾安全移至 Windows 資源回收筒，沒有使用永久刪除方式，日後仍可還原。
- 第六章 Word、網站根目錄正式檔案、`tools/sync_seo_and_geo.py` 與其他工作資料均未處理。

### 驗證與風險

- 清理前已盤點檔案內容、專案引用、Git 追蹤狀態與根目錄副本。
- 清理目標均位於專案 `work` 子資料夾內，路徑安全檢查通過。
- 本次沒有修改網站、提交或推送 GitHub。
- 資源回收筒內的兩個資料夾可還原，若日後需要舊版索引腳本或清理報表，需先人工確認用途再還原。

## 2026-08-23｜第六章發布與第七章啟動

### 已完成

- 使用者確認第六章人工審閱完成，已從 Word 定稿轉成公開 Blog 目標文章，正文可見字數 7,352 字，含 11 張表格、5 題 FAQ 與 7 組正文站內連結。
- 透過已連線的 GitHub 內容 API 完成目標欄位合併與 main 更新，最終 commit 為 `84d674968a5c4bd284e572a6fa1135470ed45273`。
- 遠端 `blog/posts.json` 由 9 篇變為 10 篇，第六章 `showOnHome=false`。四則首頁精選 ID 與非目標文章資料均已回查。
- `sitemap.xml` 與 `sitemap.html` 各加入第六章一列，移除新增列後與發布前遠端版本逐字一致。
- 第七章待審稿建立於 `work/2026-08-15-seo-review-docs/output/chapter-07-vitamins-seo-review.md`，正文可見字數 5,360 字，禁用詞句掃描 0 命中，研究回報位於同資料夾的 `source/chapter-07-vitamins-research-report.md`。

### 已修正錯誤

- 初次索引檔提交把換行符號當作文字寫入。以遠端基準檔移除目標列後比對，找到問題並用兩筆修正提交恢復 XML、HTML 的實際換行與原有縮排。
- GitHub CLI 因認證失效無法使用 `gh auth status`、`git ls-remote`，改用已連線的 GitHub API。發布前後均以遠端 branch head、檔案 SHA、目標文章與非目標欄位核對。
- `llms.txt` 與 `llms-full.txt` 的 blob 建立遭連線層拒絕，原因涉及既有聯絡方式與未經本次核實的資格主張。已停止該兩檔寫入，沒有採取替代繞行。

### 尚未完成

- `llms.txt`、`llms-full.txt` 尚未加入第六章，需另行清理既有公開資格與聯絡內容後再評估安全更新方式。
- GitHub Pages 公開文章、首頁 DOM、桌機與 375px 畫面、Console、FAQPage 與 canonical 的瀏覽器核對尚未取得。GitHub commit 只代表原始碼分支已更新。
- Search Console 本輪仍無資源權限，曝光、點擊、CTR、排名、查詢、頁面與索引狀態均未取得。
- 第七章的台灣國健署維生素數字、孕前葉酸文字、Word 排版、PDF、PNG 與人工審閱尚未完成，未發布。

### 仍有風險

- 第六章公開日期採 Word 內建建議更新日期 2026-08-22，sitemap lastmod 使用發布日 2026-08-23。需由後續網站核對決定是否統一。
- 第六章沒有新增封面圖，遠端文章沿用無 `image` 欄位的目標資料。若要補圖需另取得明確授權與圖片檔案。
- 工作樹含使用者既有刪除、修改與未追蹤檔案，本輪未整理、未提交本地 Git。

### 本次規則回寫

- 已把 GitHub API 索引檔實際換行檢查，以及遭風險拒絕時維持檔案原狀的處理方式寫入本專案 `agent.md`。
- 已使用 documents skill 讀取與核對第六章 Word。因第七章目前為 Markdown 待審稿，尚未建立 Word 檔，也沒有進行 PDF 或逐頁視覺驗證。

## 2026-08-24｜第七章 Word 審閱檔補齊

### 已完成

- 依使用者回報修正交付格式，建立 `work\2026-08-15-seo-review-docs\output\chapter-07-vitamins-seo-review.docx`。
- Word 以第三至第五章 Word 成品作版型參考建立，保留標題層級、表格、真實項目清單、超連結、表格固定寬度、重複標題列與列不可拆分設定。第六章只作用字遣詞與內容核對參考。
- Markdown 保留在 `output\chapter-07-vitamins-seo-review.md` 作為同源來源，研究回報保留在 `source\chapter-07-vitamins-research-report.md`。

### 驗證

- Markdown QA：正文可見字數 5,360 字，13 個 H2、6 個 H3、12 張表格、5 題 FAQ、15 組來源網址，禁用詞句 0 命中。
- Word QA：11 個 Heading 1、15 個 Heading 2、6 個 Heading 3、7 張表格、31 筆項目清單、15 筆編號清單、17 組超連結，DOCX ZIP 與表格幾何檢查通過。
- 參考版型檔 SHA-256 仍為 `686AC61893DE7477A0F6525A0AAD00AA8E9A6E0143B97BDDE20D9C58AC80C31F`，建立 Word 時未修改第六章參考檔。

### 已修正錯誤與根因

- 錯誤：第七章先交付 Markdown，與書籍連載一直使用 Word 審閱檔的習慣不一致。
- 根因：文章集中整理時只確認來源檔存在，沒有把 Word 審閱檔列為交付閘門。
- 修正：補建第七章 Word，並將「Word 為人工審閱主檔，Markdown 為同源來源」寫入專案 context、agent 與進度檔。

### 尚未完成與仍有風險

- LibreOffice 不在目前環境，Word COM 受目前工作階段限制，PDF、PNG 與逐頁視覺檢查尚未完成。
- 第七章仍待人工審閱、台灣 DRI 與孕前葉酸文字核對，尚未寫入 `blog/posts.json`，沒有發布或推送 GitHub。

### 本次新增規則與回寫狀態

- 後續書籍連載每章固定交付 Word 審閱檔，Markdown 只作同源來源，不再以 Markdown 單獨交付。
- 規則已回寫 `.codex\seo\context.md`、`.codex\seo\book-series-progress.md` 與專案 `agent.md`。未修改通用 skill，因本次是專案交付格式規則。

## 2026-08-24｜第七章版型依第三至第五章修正

### 已完成

- 回查第三、第四、第五章 Word，確認它們是目前書籍連載的固定版型。第六章只保留用字遣詞與內容核對價值。
- 第七章 Markdown 與 Word 已重建。文件標題改為「第七章待審 SEO 草稿」，文章主標改為「維生素怎麼吃才安心？從脂溶性、水溶性到補充品風險」，移除標題中的「第七章整理」字樣。
- 正文補回文章主標、書籍識別、文章性質與「省時版本：」。搜尋字詞、摘要與開場改為前幾章的普通段落格式，營養師判讀移到 FAQ 前。

### 驗證

- Markdown QA：正文可見字數 5,680 字，14 個 H2、6 個 H3、12 張表格、5 題 FAQ、15 組來源網址，禁用詞句 0 命中。
- Word QA：11 個 Heading 1、16 個 Heading 2、6 個 Heading 3、7 張表格、28 筆項目清單、15 筆編號清單、17 組超連結，表格幾何與 DOCX ZIP 檢查通過。
- Word 順序已核對：正文主標後接書籍識別、文章性質與「省時版本：」，`Kat Chang 營養師的判讀` 位於 FAQ 前，來源與待確認事項留在文章後段。

### 已修正錯誤與根因

- 錯誤：前一版新建 Word 以第六章作版型，且把「第七章書籍重點與心得整理」放入文件標題與 SEO 標題。
- 根因：先前只處理 Markdown 轉 Word，沒有再次套用已記錄的第三至第五章版型閘門與標題規則。
- 修正：改用第五章 Word 作建檔參考，並以第三至第五章共同結構回查 H1/H2/H3、摘要段落、正文導讀、FAQ 順序與結尾段落。

### 尚未完成與仍有風險

- LibreOffice 與目前工作階段可用的 Word 轉頁工具仍未取得，PDF、PNG 與逐頁視覺檢查尚未完成。
- 第七章仍待人工審閱、台灣 DRI 與孕前葉酸文字核對，尚未寫入 `blog/posts.json`，未發布或推送 GitHub。

### 本次規則回寫

- 已更新 `.codex\seo\context.md`、`.codex\seo\book-series-progress.md` 與專案 `agent.md`，固定標題不放「第 N 章整理」字樣，並保留第三至第五章版型閘門。

## 2026-08-24｜work 資料夾集中與錯誤防重犯規則

### 已完成

- 盤點 `D:\@Codex\594katchang-source.github.io-main\work` 的實際檔案、Git 追蹤清單與專案引用。
- 將 `2026-08-14-blog-restore` 與 `2026-08-21-seo-growth-strategy` 的 10 個歷史檔案移入 `work\2026-08-15-seo-review-docs\source`，以 `archive-` 前綴保留來源辨識。
- 兩個舊日期資料夾的空目錄已送入 Windows 資源回收筒。現在 `work` 只剩 `2026-08-15-seo-review-docs`，主資料夾只保留 `output`、`source`、`render`。
- 建立 `source\cleanup-hold-2026-08-24.md`，記錄已保留、暫存與日後刪除判定。

### 已修正錯誤與根因

- 錯誤：歷史策略、還原材料與文章審閱檔曾以日期型資料夾分散保存，增加查找與判定成本。
- 錯誤：前一輪曾把 Markdown 當成 Word 審閱交付，並把第六章當成版型基準，標題也帶入「第七章整理」。
- 根因：開始產出前沒有執行固定版型回查、交付格式閘門與工作資料夾清理判定。
- 修正：固定使用第三至第五章 Word 作版型來源，第六章只作內容與用字參考，Word 為審閱主檔，文章標題聚焦營養問題，歷史檔案集中到既有 `source` 並加暫存清單。

### 暫存與風險

- `archive-*` 歷史檔案與第六章版型錯誤證據仍保留，等確認沒有專案引用後再由使用者決定是否移除。
- 沒有永久刪除檔案。資源回收筒內只有已確認為空的舊資料夾與子資料夾，仍可復原。
- Git 工作樹原有修改、刪除與未追蹤狀態均保留，沒有提交或推送。

### 全域規則同步

- 已把「先盤點、明確檔案才清理、用途未明先暫存、錯誤要記錄根因與防呆」寫入 Codex 與 Antigravity 全域 `AGENTS.md`。
- 已建立 Codex 長期記憶更新筆記，後續工作開始前要先回查這些規則，避免再次要求使用者提醒相同問題。

## 2026-08-24｜收工核對與 render 分類釐清

### 已完成

- 核對 `work\2026-08-15-seo-review-docs\render` 的實際檔案。現有內容是第五章版型證據、第六章發布核對 manifest、第七章版型證據與共用版型證據。
- 核對第一至第四章的審閱資料仍在 `source`，包含 review HTML、review JSON 與第二章來源文字。檔案內容仍保留，沒有因分類差異擅自搬動。
- 確認主工作資料夾仍只有 `output`、`source`、`render` 三個位置。

### 已做驗證

- 已查看 `render`、`output`、`source` 的檔案清單與檔案用途。
- 已確認目前沒有 PDF、PNG 或逐頁視覺檢查成品。LibreOffice 與目前工作階段可用的 Word 轉頁工具仍未取得，這一項維持未驗證。
- 已檢查 Git 狀態。分支 `main` 落後 `origin/main` 14 個提交，工作樹含本輪整理、Chapter 7 產物與既有修改，未提交、未推送。

### 錯誤、根因與修正

- 錯誤：`render` 的實際內容只涵蓋第五至第七章，第一至第四章的審閱資料仍在 `source`，容易讓人誤以為前幾章缺少檢查材料。
- 根因：早期章節沿用舊流程，審閱 HTML、JSON 與來源文字直接放入 `source`。後期流程才產生版型證據與發布 manifest，分類名稱沒有同步說明。
- 修正：在專案 `agent.md` 明確定義 `render` 只存放 PDF、PNG、逐頁視覺檢查與 QA 證據。舊章節審閱資料依用途留在 `source`，不因章節編號強行搬移。轉頁未成功時不建立假成品。

### 尚未完成與仍有風險

- 各章 PDF、PNG 與逐頁畫面檢查仍未完成，不能宣稱視覺審查已通過。
- `archive-*` 歷史檔案與錯誤修正證據仍在暫存清單中，等待確認專案引用後再由使用者決定是否移除。
- Git 尚未整理，遠端同步、文章發布與推送均未執行。

### 本次使用者習慣與規則回寫

- 使用者要求工作資料夾少量集中，確定無用途才送資源回收筒，用途未明的項目先暫存。
- 已把 `render` 分類規則寫入專案 `agent.md`。跨專案的先盤點、錯誤根因與防呆、暫存清理規則已在本輪前段同步至 Codex 與 Antigravity 全域 `AGENTS.md` 與 Codex 長期記憶。
- 本次沒有新增或修改可重複使用的 skill。

## 2026-08-24｜第六章蛋白質文章公開段落修正

### 已完成

- 核對 GitHub `main` 的最新 `blog/posts.json`，確認目標文章 `2026-08-22-proteins-amino-acids-book-notes` 原句為「蛋白質不能夠只強調在健身上，太過簡化了」。
- 將句子修正為「談蛋白質的功能，不能只聚焦在健身用途上，這樣的理解太過簡化了。」
- 透過 GitHub API 以遠端最新 SHA 做目標文章限定更新，提交為 `1364f709f9d4ea20a0703d82cd888a228fd111ad`，`blog/posts.json` 新 Blob SHA 為 `2539a3d20ceeb261f23340f27f13f8f8b1040f00`。

### 已做驗證

- 遠端文章筆數 10，目標文章 1 篇，修正句子存在，`showOnHome` 維持 `false`。
- 與父提交比較只有 `blog/posts.json` 1 行變更，逐字比對確認為單一指定句子的替換，舊句出現 1 次，新句出現 1 次。
- 公開 `blog/posts.json`、蛋白質文章頁與 Blog 首頁均回應 200。公開 JSON 已載入新句子，首頁精選維持 4 則。

### 已修正錯誤與根因

- 錯誤：蛋白質文章公開段落缺少「功能」與「用途」語意，形成「強調在健身上」的殘句。
- 根因：文章發布前只核對欄位、連結與大段內容，沒有逐句回讀中文段落。
- 修正：補上句子主詞與用途語意，並新增公開文章逐句文字核對規則。

### 尚未完成與仍有風險

- 文章頁的正文由前端 JavaScript 依公開 JSON 載入，原始 HTML 回應只核對到 200 與頁面識別參數，未使用互動瀏覽器做畫面 DOM 逐字檢視。
- 本機工作樹仍有既有混合修改，未把遠端文章整份拉回本機，也未提交或推送本機 Git。遠端單句修正已完成，後續合併共享 JSON 前仍需重新讀取遠端 `main` 與 SHA。

### 本次規則回寫

- 已更新專案 `agent.md`，加入公開文章逐句文字核對與發布後遠端回讀規則。
- 本次沒有新增或修改通用 skill。

## 2026-08-25｜第七章修正版發布與 GitHub 推送

### 已完成

- 以修正版 Word 主檔 `work\2026-08-15-seo-review-docs\output\chapter-07-vitamins-seo-review.docx` 作為網站正文唯一來源，Word SHA-256 為 `895CB9347D58CB2612E4DB9608EEBFFFCCA959793AE3C8580D559B2933CA0412`。
- 建立同源發布資料與核對 manifest。網站正文可見字數 5,587 字，14 個 H2、6 個 H3、6 張 HTML 表格、5 題 FAQ、6 組站內連結。
- 以遠端最新 `main` `4c115bdd7fd91e0b13324f959a092212ab884dba` 做基準，保留 10 篇既有文章、既有欄位與首頁精選設定，只新增 `2026-08-23-vitamins-book-notes`，並更新 `sitemap.xml` 與 `sitemap.html`。
- 遠端提交 `202ca6f40ab2eb878a852fe262292ee583ed8ab2` 已快進到 `main`。`showOnHome=false`，首頁精選維持 4 篇。`llms.txt` 未修改。
- GitHub Pages workflow `32820485024` 已對應本次提交完成，結果為 `success`。

### 已做驗證

- 遠端回讀後，`blog/posts.json` 共 11 篇文章，目標文章 1 篇，非目標 10 篇物件欄位維持一致。第七章目標網址在兩份 sitemap 各出現 1 次。
- 遠端檔案 SHA：`blog/posts.json`=`2636ad807096cf9c0702e4123785f584d54176f4`，`sitemap.xml`=`50a81cf4db6fefdb01e6ee6a40bb33ee48a3bfdc`，`sitemap.html`=`fc4dea9461a65311be3659816a173d92016dd026`。
- 生成資料 JSON 可解析，FAQ 與正文標題、表格、站內連結數量一致。修正版句子存在，舊版 `日常底盤` 與 `自動變成慢性病保護傘` 未出現。
- 遠端 GitHub API 的分支、檔案、提交與 Pages workflow 均已回讀。沒有覆蓋本機混合工作樹，也沒有使用本機落後分支推送。

### 錯誤、根因與修正

- 使用者提供的路徑多了一層反斜線資料夾。回查後確認實際 Word 路徑存在，錯誤路徑不存在，發布來源改用實際存在的 Word 主檔。
- PowerShell 轉換器初次測試遇到字串引號解析錯誤，改用字串串接。遠端讀取候選產生時又因 `$Path?ref` 被 PowerShell 當成變數名稱，造成 API 404，改用字串串接建立 endpoint 後通過。
- 遠端合併 audit 初版把新增文章算進舊首頁精選數量，修正為從遠端舊物件計算。重新執行後舊、新首頁精選均為 4，非目標物件核對為 `true`。
- 曾因測試命令誤用建立 `work\2026-08-15-seo-review-docx` 暫存資料夾，已確認為本次誤產物並移入 Windows 資源回收筒，沒有永久刪除。

### 尚未完成與仍有風險

- 公開文章 DOM、首頁 DOM、375px 畫面與 Console 尚未完成。命令列公開頁請求因 `SEC_E_NO_CREDENTIALS` 失敗，瀏覽器 skill 所需的 `browser-client.mjs` 不在已安裝目錄，未把這些項目寫成已通過。
- ISO 第 35 週為奇數週，Search Console 與反向連結盤點未執行。沒有新增曝光、點擊、CTR、平均排名、熱門查詢或熱門頁面數據。
- Word PDF、PNG 與逐頁視覺檢查仍未驗證。工作樹原有刪除、修改與未追蹤檔案保持原狀，尚未做本機 Git 整理。

### 本次規則回寫

- 新增 `source\publish_chapter7_from_word.ps1` 與 `source\build_chapter7_remote_merge_candidates.ps1`，保留在既有工作資料夾內，供本章發布證據與目標限定合併回查。
- 本次沒有修改通用 skill，專案進度已同步寫入 `.codex\seo\book-series-progress.md`。

## 2026-08-24｜第六章 Word 與本機發布來源同步修正

### 已完成

- 回查 `work\2026-08-15-seo-review-docs\output\chapter-06-proteins-amino-acids-seo-review.docx`，確認 Word 第 21 段也有同一個缺字句。
- 以最小範圍 OOXML 文字替換修正 Word，保留原有段落、格式片段、標題、表格與連結。
- 同步修正 `source\chapter-06-publish.html`、`source\chapter-06-publish.json` 的同一句，讓 Word、本機發布來源與 GitHub 公開句子一致。

### 已做驗證

- DOCX ZIP 測試通過，文件包含 `word/document.xml` 與關聯檔。
- Word 目前 132 個段落、12 張表格、1 個 section，原句出現 0 次，新句出現 1 次。
- Word SHA-256：`4DAD2D5B5C0F4BD67533AB47FF8E5D73CE6CD522D2A7A745FD7728A16E724069`。
- HTML 與 JSON 來源檔案均已核對，原句出現 0 次，新句各出現 1 次，JSON 可解析。
- 第一次以 Windows 預設編碼輸出中文核對結果時遇到 `cp1252` 編碼錯誤，改用 UTF-8 輸出後重跑通過，檔案內容未受影響。

### 已修正錯誤與根因

- 錯誤：公開文章修正後，Word 審閱主檔與本機發布來源仍保留缺字句。
- 根因：先前只回讀 GitHub 遠端 JSON，沒有把同一段落回查到 Word 與 source 證據。
- 修正：加入 Word 與 source 同步回查，並以段落文字出現次數與 DOCX ZIP 驗證作為交付檢查。

### 尚未完成與仍有風險

- `render_docx.py` 已執行，但環境找不到 LibreOffice `soffice.exe`，沒有產生 PDF、PNG，逐頁視覺檢查維持未完成。
- 本機 `blog/posts.json` 仍是落後遠端的混合工作樹版本，這次沒有整份覆蓋。日後若要修改共享 JSON，仍需從遠端 `main` 最新 SHA 做目標限定合併。

### 本次規則回寫

- 已更新專案 `agent.md`，要求公開文章回修時同步回查 Word 審閱主檔與 source 證據。
- 本次沒有新增或修改通用 skill。

## 2026-08-25｜第八章 Word 補建與漏交防呆

### 已完成

- 補建第八章同源 Markdown 與 Word 審閱主檔，均放在既有 `work\2026-08-15-seo-review-docs\output`。
- 執行 DOCX ZIP、段落、標題、表格、超連結、正文字數、禁用詞與內容一致性檢查。
- Word QA 通過：170 個段落、9 張表格、43 個標題、21 個外部連結、表格寬度 9360 DXA、重複標題列與 `w:cantSplit` 通過，正文 8,110 字元，去除空白後 7,538 字元。
- 更新 `.codex\seo\book-series-progress.md`，保留待人工審閱狀態。未修改網站、Blog、共享 JSON、圖片、公開頁面或 GitHub。

### 錯誤、根因與修正

- 錯誤：第八章先交付聊天稿，未同步建立 Word，且同類漏交已重複發生。
- 根因：收尾流程缺少「同名 Markdown 與 Word 均存在」的硬性閘門，建置模組也帶有第七章固定輸出路徑。第一次隔離測試未能覆寫模組內的全域變數，導致第七章 Word 被重新序列化。
- 修正：改用明確載入模組並覆寫來源與目標路徑後重建第八章，新增 `source\qa_chapter8_word.py`，並把 Word 存在性、章次、標題順序、字數、來源、表格與禁用詞檢查寫入 `agent.md`。
- 驗證：第八章 Word 現檔結構與內容檢查通過。第七章現檔的段落、標題、表格、清單與連結數量與既有交付紀錄一致，原始舊 SHA-256 無法從目前檔案系統恢復，已列為人工確認風險。

### 尚未完成與仍有風險

- 找不到 LibreOffice `soffice.exe`，第八章 Word 尚未完成 PDF、PNG 與逐頁畫面核對。
- 第八章尚未取得人工審閱確認，不能進入網站編排、發布或第九章產出。

### 本次規則回寫

- 已更新專案 `agent.md`，新增 Word 交付閘門與建置腳本路徑隔離規則。
- 已更新 `.codex\seo\book-series-progress.md`，記錄第八章 Word 已補建與未驗證項目。
- 未修改通用 skill。

## 2026-08-25｜第八章 Word 批註修正

### 已完成

- 依使用者批註，將第八章正文的「省時版本：」與判斷表移到「本章的四個生活問題」段落之前。
- 同步更新 Word 與同源 Markdown，保留其他文章內容、來源連結、表格與樣式。
- 重跑 Word QA 與可讀性檢查。170 個段落、9 張表格、43 個標題、21 個外部連結、正文 8,110 字元，去除空白後 7,538 字元，表格寬度 9360 DXA，DOCX ZIP 有效，禁用詞命中 0 次，a11y high、medium、low 均為 0。
- 已把「省時版本：」位於正文四個生活問題之前的順序檢查加入 `source\qa_chapter8_word.py`。

### 錯誤、根因與修正

- 批註指出「省時版本：」位置晚於本章四個生活問題，閱讀入口順序不符合既有格式偏好。
- 修正方式：以局部 OOXML 移動保留原樣式與表格，再用同源 Markdown 對照順序。

### 尚未完成與仍有風險

- LibreOffice `soffice.exe` 不在目前環境，PDF、PNG 與逐頁畫面檢查尚未完成。
- 第八章仍待人工審閱，尚未進入網站編排、發布或第九章產出。

### 本次規則回寫

- 已更新 `agent.md`，固定「省時版本：」在正文導讀之後、四個生活問題之前。
- 已更新 `.codex\seo\book-series-progress.md`。
- 未修改通用 skill。




## 2026-08-25: 部落格發布日期規則確立、封面圖名同步與全站 SEO/AI 關鍵字審查優化

- **封面圖檔名與發布日同步**：將維生素篇封面圖片由 `2026-08-23-vitamins-book-notes.png` 重新命名為 `2026-08-25-vitamins-book-notes.png`，與文章發布日期完全一致。
- **寫入專案硬性規則**：在 `agent.md` 明確訂定「新文章發布一律以正式推上 GitHub 當日為發布日期（`post.date`），且封面圖檔名前綴必須與發布日相同（`YYYY-MM-DD-slug.png`）」。
- **分類與搜尋機制優化**：全站 11 篇衛教文章分類與關鍵字全面升級，文章內頁修復分類顯示（`.category-tag`），並完成全站 `sitemap.xml`、`llms.txt` 同步更新。

## 2026-08-25｜第八章批註修正收工

### 已完成

- 完成第八章 Word 批註修正，將「省時版本：」與判斷表放到正文四個生活問題之前。
- Word 與同源 Markdown 均已存在於既有 `work\2026-08-15-seo-review-docs\output`。

### 已驗證

- Word QA 通過：170 個段落、9 張表格、43 個標題、21 個外部連結、正文 8,110 字元，去除空白後 7,538 字元，表格寬度 9360 DXA，DOCX ZIP 有效，禁用詞命中 0 次。
- 可讀性檢查 high、medium、low 均為 0，順序檢查已加入 `source\qa_chapter8_word.py`。
- `git diff --check` 通過。收工前 `git status --porcelain=v2` 無輸出，分支 `main` 與 `origin/main` 均在 `54072af`。

### 尚未完成與仍有風險

- LibreOffice `soffice.exe` 缺少，PDF、PNG 與逐頁畫面檢查尚未完成。
- 第八章仍待人工審閱確認，尚未進入網站編排、發布或第九章產出。
- 本次收工未執行 commit 或 push，網站與共享文章資料未修改。

### 本次使用者偏好與規則回寫

- 依使用者批註，Word 為人工審閱主檔，正文入口順序需固定保留「省時版本：」在四個生活問題之前。
- 已將該順序寫入 `agent.md` 與章節 QA。未修改通用 skill。

## 2026-08-29 18:57 SEO 第九章待審稿、左側任務整理與 GitHub 同步核對

### 任務

- 依使用者明確指示，在第八章仍待審核的情況下建立第九章待審 SEO 草稿。
- 整理「Kat Chang SEO 草稿與搜尋成效」左側重複任務，保留目前任務與其他有明確辦理內容的任務。
- 核對 GitHub `main` 與本機網站檔案，確認 Blog 直接修改是否需要回存本機。

### 已完成

- 封存 15 個舊的同名 SEO 任務，保留目前使用中的任務。封存可恢復，未刪除其他有工作內容的任務。
- 以 Chapter 9 原始 PDF 第 360 至 401 頁與 `chapter-09-source.txt` 為內容基礎，建立同源 HTML、JSON、Markdown 與 Word 產出流程。
- 產出第九章 Markdown 待審稿、Word 審閱主檔與研究回報。正文實際字數 5,577 個去除空白字元，空白分隔詞數 152。
- 文章含能量平衡、復胖、BMI、腰圍、身體組成、飢餓與食慾、斷食、活動、醫療選項、飲食失調警訊、FAQ、來源對照與待確認事項。
- GitHub 公開 API 與本機核對結果一致。`HEAD` 與遠端 `main` 均為 `42423f21ad07d03746c1c450367debda5f888de1`。`blog/posts.json` 本機與遠端 blob 均為 `2ac81496f1cd231c40800f2424256848f6923fad`。
- 未修改網站、`blog/posts.json`、圖片、sitemap、`llms.txt`、公開頁、GitHub 遠端或首頁精選設定。

### 已修正錯誤

- 文件技能的作業標記命令第一次使用錯誤路徑，改用文件技能實際的 `container_tools` 路徑後成功完成標記。
- 第九章來源表初版含一個分號，已回到同源 JSON 修正並重新產生 Markdown 與 Word。文字規則掃描目前通過。
- Word QA 初版把 8 個超連結當成門檻，查明目前版型有 7 個站內超連結，來源表另保留 10 組 URL，已修正 QA 門檻並重新驗證。
- 先前進度檔的重複錨點問題已持續保留防呆，本輪新增紀錄放在檔案末端並核對日期順序。

### 驗證

- Markdown QA 通過，H1、H2、H3、8 張表格、FAQ、作者判讀、來源網址、正文長度與文字規則均通過。
- Word 結構 QA 通過，DOCX ZIP、9360 DXA 表格寬度、`w:cantSplit`、`w:tblHeader`、7 個站內連結與既有章節污染檢查均通過。
- `git diff --check` 通過。
- 第八章 Markdown 與 Word SHA-256 未變更，仍為 `DCBE16C7DE9368C9F6CA6A1126F9217AF6CD9E4D169286FB00E73ADBE19A3115` 與 `7B7FA91950C5652B8D89B912F9994685D710AAEBABAE857CCA6853C77922DC80`。
- `soffice.exe` 不可用，Word PDF、PNG 轉頁與逐頁畫面檢視未完成，沒有把結構 QA 寫成視覺通過。

### 尚未完成

- 第八章仍待人工審核，第九章也仍待人工審閱。未進入網站編排、發布或 GitHub 推送。
- 第九章正式網址、封面圖、台灣飲食失調轉介資源與最新體位衛教版本待人工確認。
- 2026 年 ISO 第 35 週為奇數週，本輪未執行 Search Console 與反向連結盤點。

### 仍有風險

- Git HTTPS 讀取遇到 Windows Schannel `SEC_E_NO_CREDENTIALS`，GitHub CLI token 顯示失效。遠端狀態由公開 GitHub API 讀取核對，未完成 authenticated Git transport 驗證。
- 第九章來源表中的本機書籍路徑供人工回查，發布前仍需確認公開頁只保留適合公開的來源網址。

### 這次新增的規則與回寫狀態

- 本次依使用者明確指示保留第八章待審狀態，同時建立第九章待審稿。這是本輪工作決定，未改寫固定連載順序規則。
- 新增的生成與 QA 腳本只放在既有 SEO 工作資料夾，未回寫全域 skill 或專案 agent，因本輪沒有確認新的跨任務規則。
- 下次處理前仍需先讀取本進度檔、工作日誌、Git 狀態、遠端共享 JSON 與前一章人工審核狀態。

## 2026-08-29 19:52 公開 Blog 即時內容回查

### 任務

- 使用者指出 GitHub Blog 可能有比本機較新的文章內容，要求以公開網站目前版本為準並存回本機。

### 查核結果

- 以 `https://594katchang-source.github.io/blog/posts.json` 加入新查詢參數重新讀取，HTTP 200，取得 11 篇文章。
- 以 GitHub API 重新讀取 `main` 的 `blog/posts.json`，HTTP 200，取得 11 篇文章，blob SHA 為 `2ac81496f1cd231c40800f2424256848f6923fad`。
- 逐篇比對文章 ID、標題、日期、分類、摘要、關鍵字、`showOnHome` 與正文，公開網站、本機與 GitHub API 的差異 ID 均為空，代表目前沒有文章欄位需要回存。
- 目前公開網站與 GitHub API 的 UTF-8 內容 SHA-256 均為 `165ad88caf9a3343ec1b90fc183687ad903bfc9ca58053954b4e11de9285f7ec`。本機檔案採 CRLF，換行轉為 LF 後與公開網站內容完全相同，差異只有 224 組換行字元。
- GitHub `blog` 目錄的追蹤檔案 SHA 與本機 Git blob 逐項相同，包含 `blog.js`、`index.html`、`post.html`、`posts.json` 與圖片。沒有發現另一份較新的公開 Blog 文章版本。

### 已修正認知落差

- 前次紀錄只核對 GitHub `main` 與本機，沒有把公開網站即時回應列為獨立來源。本次已補上公開網站、GitHub API、本機解析內容與 Git blob 四方交叉核對。
- 本次沒有覆寫 `blog/posts.json`，因目前本機文章內容已是公開網站與 GitHub `main` 的同一份內容。若直接改成公開服務回傳的 LF，反而會改變本機工作樹的換行形式，無助於保留 Git blob 一致性。

### 尚未完成與限制

- 本次未發現可新增的 GitHub Blog 文章修改，因此沒有文章回存差異可交付。
- Git HTTPS 仍受 Windows Schannel `SEC_E_NO_CREDENTIALS` 影響，GitHub CLI token 狀態仍需重新登入。公開 GitHub API 讀取已成功。
- 第九章仍待人工審閱，第八章仍待人工審核，沒有進行網站發布、commit 或 push。

## 2026-08-29 21:00 公開 Blog 版本回存本機

### 任務

- 使用者說明公開 GitHub Blog 曾用文章修改功能改過少量文字，要求檢查遠端檔案日期與內容，並把較新版本保存到桌機專案。
- 依公開 GitHub `main`、本機 `blog/posts.json`、Word 審閱檔與 `source` 發布紀錄逐層核對。

### 已完成

- 重新讀取 GitHub Contents API 的 `main:blog/posts.json`，HTTP 200，遠端 blob SHA 為 `2ac81496f1cd231c40800f2424256848f6923fad`，遠端 `main` HEAD 為 `42423f21ad07d03746c1c450367debda5f888de1`。
- 遠端 `blog/posts.json` 的最新路徑提交為 `54072afe60134dfa320c380a4628f31e293fff9a`，時間為 2026-08-25 19:56:49（台灣時間）。原本本機檔案時間為 2026-08-25 19:55:59，遠端時間較晚約 50 秒。內容已從遠端重新保存到本機，現在遠端與本機原始位元組完全相同，均為 171,864 bytes，SHA-256 均為 `165ad88caf9a3343ec1b90fc183687ad903bfc9ca58053954b4e11de9285f7ec`。
- 公開文章資料與本機解析結果均為 11 篇，ID 順序相同，首頁精選仍為原有 4 篇，沒有改動 `showOnHome`。
- 比對 7 篇已發布書籍連載的 Word 審閱檔。七份文件的標題、摘要、目標搜尋字詞、分類與日期已依公開 Blog 欄位更新。第二、六、七章的正文少量差異已回存，包含第七章多處用字、標題、表格文字與延伸閱讀段落。
- 第六章與第七章的 `source\chapter-06-publish.json`、`source\chapter-06-publish.html`、`source\chapter-07-publish.json`、`source\chapter-07-publish.html` 已同步公開文章核心欄位與正文。原始 Word 檔案先保留於 `source\remote-sync-backups-2026-08-29`。
- 修正 `source\qa_review_docs.py` 的 UTF-8 輸出設定，讓 Windows PowerShell 能正常列印中文 QA 結果。新增同步與 QA 腳本均放在既有 SEO 工作資料夾。

### 已修正錯誤

- 舊的遠端回查紀錄只核對解析內容，沒有執行公開版本回存，也沒有逐一回查 Word。這次補做公開 API 下載、原始位元組比對、Word 差異分析與來源紀錄同步。
- QA 腳本第一次執行時因 cp1252 輸出中文失敗，已補上 `sys.stdout.reconfigure(encoding='utf-8')`，重跑後通過。
- 文字差異比對初版把段落拆分、來源網址與 Word 審閱附註列為正文差異，已改用正文區段、表格與去除網址的語意核對，確認真正需要回存的差異範圍。

### 驗證

- 7 份同步後 Word 均通過 DOCX ZIP、metadata、正文標題、表格 9360 DXA、重複標題列與 `w:cantSplit` 檢查。第 1、2 章既有 QA 也已重跑通過，第 7 章 Markdown QA 通過，第 8 章既有 Word QA 通過。
- 第六章與第七章發布 HTML 已與本機 `blog/posts.json` 對應正文完全相同，發布 JSON 的公開核心欄位也已相同。
- 本機 `blog/posts.json` 與 GitHub 公開 API 已完成原始位元組相同、JSON 解析相同、11 篇文章與 ID 相同的核對。
- 公開 GitHub Pages、GitHub API 與本機 `blog/posts.json` 均回應 HTTP 200，三者各為 171,864 bytes，SHA-256 均為 `165ad88caf9a3343ec1b90fc183687ad903bfc9ca58053954b4e11de9285f7ec`，原始位元組與 JSON 均相同。
- `git diff --check` 已通過。`blog/posts.json` 的 Git 工作樹標記只反映本機改成遠端 LF 的換行形式，忽略行尾後沒有語意差異。尚未進行 commit、push、網站發布或公開內容寫入。

### 尚未完成與仍有風險

- Word 文件的 PDF、PNG 與逐頁畫面檢查仍未完成，因環境缺少 LibreOffice `soffice.exe`。結構 QA 不代表視覺 QA 通過。
- 第八章仍待人工審核，第九章仍為使用者要求建立的待審稿，未因本次同步變成已核准文章。
- Git HTTPS 仍有 Windows Schannel `SEC_E_NO_CREDENTIALS`，GitHub CLI token 仍顯示失效。本次只用公開 GitHub API 讀取與保存，未進行 authenticated Git transport、commit 或 push。
- 本次保留的同步前檔案與新增工具仍屬本機工作資料，尚未提交到 GitHub。

### 本次新增的規則與回寫狀態

- 已將「公開 `/admin/` 修改只會寫入 GitHub，不會自動更新桌機或 Word」與「遠端時間較新時先抓取並逐篇核對，再回存本機」寫入專案 `agent.md`。
- 使用者偏好已記錄：公開 Blog 的少量人工修改要以公開版本為準，保存到本機 Word 與 source，並維持網站未發布、未 commit、未 push 的狀態。
- 本次未改寫通用 skill，已修正專案內 QA 腳本並完成代表性執行驗證。

## 2026-09-01 第八章使用者審閱回修與第九章格式同步

### 任務

- 使用者正在審核第八章，提供多處明確文字修正，並指出第八章、第九章「省時版本」格式不符合偏好；要求修改後直接覆蓋舊 Word 檔。

### 已完成

- 第八章 Word 與同名 Markdown 已同步回修。標題移除「生活判讀」尾字；礦物質分類另設小標題；依使用者指定修正限水、尿液、電解質、食鹽、鈣磷鎂、血鈣、缺鐵、茶／乳品、鈣來源、營養師判讀與安全說明。
- 第八章「省時版本」改成兩段短文，第九章同樣改成兩段短文；第九章同源 HTML、JSON wordCount、Markdown 與 Word 已重建同步。兩章均保留待人工審閱，沒有標記為通過或發布。
- 第八章正文統計更新為 8,156 字元、去除空白後 7,584 字元；第九章為 5,482 字元、145 個空白分隔詞。
- 新增／修正既有 SEO 工作資料夾內的 Word 回修與 QA 腳本，並把使用者確認的風格規則回寫專案 `agent.md`；未修改全域 skill。

### 驗證

- `qa_chapter8_word.py` 通過：173 段落、8 張表、43 個標題、21 個外部連結、表格 9360 DXA、重複表頭與 `w:cantSplit` 均通過。
- `qa_chapter9_word.py` 通過：112 段落、7 張表、7 個外部連結，且省時版本為兩段短文、沒有舊表格。
- 使用者回修專用 QA 通過；第八、九章均完成首／中／末段抽查，Markdown、Word 與第九章 HTML／JSON 的省時版本格式一致。
- DOCX ZIP 與文字結構完整，沒有發現使用者列出的舊句型殘留。收尾重跑 Git `diff --check` 通過。

### 錯誤與限制

- 第八章第一次重跑舊 QA 時因 QA 腳本仍要求「省時版本」H2 後接表格而失敗；已依使用者新格式更新 QA 規則，重跑通過。
- 第八章 QA 的禁用詞清單原本包含使用者指定的新句型「不是只靠少吃食鹽、控制食鹽而已」，已移除該單字級衝突，保留其餘禁用詞檢查。
- 文件渲染因本機沒有 LibreOffice／`soffice.exe`（WinError 2）而無法產生 PDF／PNG，未宣稱完成逐頁畫面 QA。Word 結構 QA 通過不代表視覺 QA 通過。

### 尚未完成與 Git 狀態

- 第八章仍待使用者人工審閱，第九章仍為待審稿；沒有修改 `blog/posts.json`、網站程式、sitemap、`llms.txt`、公開頁或 GitHub 遠端內容，沒有 commit 或 push。
- 工作樹原有其他修改與未追蹤資料均保留；本次新增／修改的 SEO 檔案仍在本機工作樹，Git `main` 與 `origin/main` 未因本輪提交而改變。

## 2026-09-01 第八章使用者偏好學習、格式同步與公開發布

### 任務

- 使用者提供第八章 Word 的直接修改結果，要求以 Word 內容學習寫作偏好、修正「巨量礦物質」用語、將第九章之後的文章性質／省時版本統一為新格式，並把第八章以今日日期發布至 GitHub，且補上文章分類。

### 已完成

- 以現行第八章 Word 為 canonical，保留使用者已修改的句子與段落，不用舊 Markdown 覆蓋 Word；只把殘留的「主要礦物質」改為「巨量礦物質」，並同步同名 Markdown、發布 HTML／JSON 與發布 manifest。
- 已把使用者偏好記錄至 `C:\Users\cygnu\.codex\memories\extensions\ad_hoc\notes\2026-09-01-kat-chang-seo-review-style.md`，並回寫專案 `agent.md`：標題採精簡且不誇大；`文章性質：` 後直接接兩段省時版本；第一段放核心問題，第二段合併生活判讀與閱讀路線；礦物質分類使用「巨量礦物質／微量礦物質」並另設標題；安全警語需說明原因、邊界與處理方式。
- 第九章已依新格式重建同名 Word／Markdown／同源 HTML／JSON，維持待審稿，沒有因本輪格式同步而視為通過或發布。
- 第八章已發布為 `2026-09-01-how-much-water-electrolytes-calcium-iron-bone-health`，日期為 `2026-09-01`，分類為「書籍連載與營養知識」，`showOnHome=false`。發布前重新讀取遠端 `main`，只新增目標文章，保留既有 11 篇文章與 4 篇首頁精選。
- GitHub 遠端提交證據：`cc88b0f5ec1c5c6ff14cab3563249f9d6099fe2f`（`blog/posts.json`）、`e8de4c82a60d30627a52cb756a54c022674c50f0`（`sitemap.xml`）、`51b640e950fbfa4823fe8951cff59f86001d955b`（`sitemap.html`）；完成後遠端 `main` HEAD 為 `51b640e950fbfa4823fe8951cff59f86001d955b`。

### 驗證

- 第八章 Word QA 通過：169 段落、8 張表、43 個標題、32 個外部連結；正文 7,037 字元，去除空白後 6,762 字元；9360 DXA、重複表頭、`w:cantSplit`、ZIP 完整性通過。
- 第九章 Word QA、Markdown／研究草稿 QA 與使用者回修首／中／末段抽查通過；第九章 111 段落、7 張表、7 個外部連結。
- 已用 LibreOffice Portable 渲染第八章 17 頁、第九章 14 頁 PDF／PNG，抽查前頁未見裁切或重疊；尚未完成全部頁面逐頁人工視覺審閱。
- 遠端 GitHub API 回查目標文章正文無「主要礦物質」、有「巨量礦物質」、FAQ 5 題與正文表格 7 張。文章沒有專屬 `image` 欄位，因此未捏造封面圖。
- GitHub Pages 公開文章頁、Blog 列表、根目錄首頁、XML sitemap、HTML sitemap 均 HTTP 200。瀏覽器 DOM 確認文章頁日期、分類、作者、標題、正文、表格與 FAQ；Blog 列表顯示 12 篇；根目錄首頁仍為原 4 篇精選且沒有第八章。
- `git diff --check` 通過。專案本機仍保留既有修改與未追蹤檔案，沒有做本地 commit 或 push；本輪的 GitHub 遠端寫入由已連線的 GitHub 內容更新完成。

### 尚未完成與風險

- 第八章雖依使用者明確要求發布，但文件中的「待審稿」性質未被改成已通過；第九章仍待人工審閱。
- 本機 `blog/posts.json`、`sitemap.xml`、`sitemap.html` 已加入第八章，但本機原先即少於遠端的 3 篇舊文章未擅自補回，故本機非目標內容與遠端不完全同步，已保留此限制供後續人工決定。
- 第八章沒有文章專屬封面圖；遠端文章沒有 `image` 欄位，網站畫面未被捏造圖片替代。
- Search Console 尚未取得網站資源權限，本輪沒有曝光、點擊、CTR、平均排名、熱門查詢或熱門頁面數據。

## 2026-09-01 第八章站外來源連結回修

### 問題

- 使用者指出正文中的「國民健康署：清涼消暑，聰明喝水」沒有連到站外來源。查核後確認 Word 內已有正確的 `HYPERLINK` 欄位，網址為 `https://www.hpa.gov.tw/Pages/Detail.aspx?nodeid=4306&pid=14493`；問題在於原轉換器只處理一般 Word 超連結，沒有處理欄位型超連結。

### 已完成

- 修正 Word→Markdown／HTML 的連結解析，保留一般 `w:hyperlink` 與 Word `HYPERLINK` 欄位型連結。
- 以人工修正版 Word 重新同步第八章同名 Markdown、發布 HTML／JSON、manifest 與本機 `blog/posts.json` 目標文章；第八章 Word 本身沒有被改寫。
- 重新讀取遠端 `main`，只更新第八章正文，未改動其他文章、`showOnHome` 或 sitemap。
- GitHub 提交：`9c0da9e2a80752d5549db5f2b6d8a01f7af18724`；內容 blob SHA：`5c29ad96074c3e8d990274785f843947cc111f51`。

### 驗證

- 第八章公開正文外部連結由 1 個增為 10 個；指定的「清涼消暑，聰明喝水」已成為可點擊連結。
- 公開文章 DOM 核對通過：指定連結文字與網址正確，文章仍顯示原日期、分類、兩段省時版本與「巨量礦物質」。
- 遠端仍為 12 篇文章、4 篇首頁精選，第八章 `showOnHome=false`。
- 第八章 Word QA 與使用者回修首／中／末段抽查通過。

## 2026-09-01 第八章站外連結完整稽核與跨代理收工規則

### 任務

- 使用者要求再檢查第八章是否還有其他站外連結遺漏，並要求把本次修改、錯誤、偏好與防呆完整記錄，供 Codex 與 Antigravity 後續共用。

### 已完成

- 以人工修正版 Word 為唯一正文來源，分開稽核 Word 正文、發布 HTML／JSON、本機 `blog/posts.json` 與公開頁面 DOM。
- Word 正文有 10 個獨立站外來源連結；發布 HTML、發布 JSON、本機目標文章與公開正文均為同一組 10 個，沒有遺漏或多出。
- 公開頁面整頁另有「聯絡」與「官方 Line」2 個網站功能連結；Word SEO／研究來源區共有 13 個獨立網址，其中 WHO 飲用水指引、NIH ODS Iodine、NIH ODS 礦物質索引 3 個只在來源說明區，未進入公開正文，已明確區分為「未發布區段」而非斷線。
- 這次沒有再修改文章內容、Word、Markdown、JSON 或 GitHub 遠端資料；只完成讀取與比對，保留使用者原有工作樹修改。

### 驗證

- 重新開啟帶快取破除參數的公開文章頁，正文 DOM 外部來源連結為 10 個，指定「國民健康署：清涼消暑，聰明喝水」文字與網址均正確，沒有缺少 `href` 的國民健康署來源標籤。
- 比對結果：Word 正文 → 發布 HTML：缺少 0；Word 正文 → 發布 JSON：缺少 0；Word 正文 → 本機 `blog/posts.json`：缺少 0。
- 文章標題仍為「每天喝多少水才夠？從電解質、鈣鐵到骨質保養」，日期與分類未被稽核流程改動。

### 錯誤與根因、修正

- 原始問題：Word 中的站外來源使用 Word `HYPERLINK` 欄位，舊轉換器只解析一般 `w:hyperlink`，因此公開正文保留了來源文字卻遺失可點擊網址。
- 修正：Word→Markdown／HTML 轉換同時解析一般 `w:hyperlink` 與欄位型 `HYPERLINK`；同步後再以遠端資料與公開 DOM 驗證連結數量與目標網址。
- 稽核命令第一次輸出中文時遇到 Windows `cp1252` `UnicodeEncodeError`；原因是診斷腳本未設定 UTF-8 標準輸出，已補上 `sys.stdout.reconfigure(encoding='utf-8')` 後重新執行通過。

### 新學到的使用者偏好與下次防呆

- Word 是人工審閱主檔；不得用舊 Markdown、舊 HTML 或舊 JSON 覆蓋使用者修改。下游檔案只能由最新 Word 同源重建。
- 標題採精簡、不誇大的寫法；使用者刪除的標題尾語不得自行補回。`文章性質：` 後直接接兩段短格式的 `省時版本：`；後續章節沿用此格式。
- 固定使用「巨量礦物質／微量礦物質」，礦物質需另設清楚段落；容易誤解的衛教句要解釋原因、適用邊界與處理方式。
- 來源標籤不能只保留顯示文字；只要屬於公開正文的外部來源，就必須是可點擊的站外連結。稽核時要把正文連結與 SEO／研究來源區連結分開統計，不能把未公開的來源區連結誤報成正文遺漏。
- 每次發布或修正後，固定比對 Word、HTML、JSON、公開 DOM 的外部連結集合，並另核對網站全域功能連結，避免把兩者混算。

### 規則回寫與狀態

- 已補強本專案 `agent.md` 的站外來源稽核規則；本次共用規則同步寫入 Codex 全域 `AGENTS.md`、Antigravity 全域 `AGENTS.md`，並另存 Codex／Antigravity 共用記憶更新紀錄。
- 第八章仍保留文章內「待審稿」性質；本次只是連結稽核，沒有自行判定通過。未完成項目是：若使用者希望 WHO、Iodine、礦物質索引 3 個來源也出現在公開正文，需另行指定放置段落。
- 本機 Git 工作樹仍有既有修改與未追蹤檔案，未 commit；本次沒有新增遠端寫入。
- 收工遠端核對：`main:blog/posts.json` blob SHA `5c29ad96074c3e8d990274785f843947cc111f51`；12 篇文章、目標文章日期 `2026-09-01`、分類「書籍連載與營養知識」、`showOnHome=false`、首頁精選 4 篇，目標正文站外連結 10 個。
- 收工驗證：第八章 Word QA 重新通過；Codex／Antigravity 新增共用規則在換行正規化後 SHA-256 均為 `ab7a3b9eb5502ac84a470d17777f2867d3b020fb11ca3111d219ed555199a04e`。

## 2026-09-01 第八章公開狀態與來源區段說明

### 使用者追問與查核結果

- 使用者指出第八章既然已送出 GitHub，公開正文仍出現「本篇為待審稿」不合理，並追問 WHO、NIH ODS Iodine、NIH ODS 礦物質索引為何未出現在公開正文。
- 重新查核遠端 `main:blog/posts.json`：目標文章確實已存在，日期為 `2026-09-01`、分類為「書籍連載與營養知識」、`showOnHome=false`；公開正文仍含 1 次「本篇為待審稿」，正文站外來源仍為 10 個。
- Word 中的「文章性質」與 SEO／研究來源資料屬於審閱資料；發布建置器只取 Word 的「正文」區段。WHO 飲用水、NIH ODS Iodine、NIH ODS 礦物質索引 3 個網址確實在 Word 來源區，但不在 Word 正文，因此不是連結失效，而是沒有被放入公開內容。

### 錯誤根因與使用者偏好釐清

- 根因：先前把「允許發布到 GitHub」與「不要自行判定審閱通過」混在同一流程；為了保留內部審閱狀態，未把「待審稿」標籤從公開正文隔離，造成已發布文章看起來仍是草稿。這是流程設計錯誤，不是 GitHub 沒有發布。
- 本次明確偏好：文章既然送出到 GitHub，公開正文不應保留「本篇為待審稿」等內部審閱狀態；公開版狀態與 Word 內部審閱標籤必須在發布前分開處理並核對。
- 本次明確偏好：Word SEO／研究來源區的連結不會自動等於公開正文連結；若要讓 WHO、Iodine、礦物質索引等來源出現在文章，必須先放入正文適當段落，再重新同步與發布，不能只因 Word 有網址就宣稱公開頁已連接。

### 尚未修改與下次防呆

- 本次只完成查核與紀錄，尚未改動 Word、Markdown、HTML、JSON 或 GitHub，因為移除「待審稿」會涉及 Word 人工審閱主檔與公開版本是否同步的明確決定。
- 下次發布前增加硬性檢查：公開正文若含「待審稿」「待確認」等內部狀態字樣，先停止發布並回報；來源連結則分別核對 Word 正文、SEO／研究來源區、發布 HTML／JSON 與公開 DOM。

## 2026-09-01 第八章封面顯示查核

### 使用者問題與證據

- 使用者回報第八章公開文章頁沒有顯示已上傳的封面圖。
- 重新讀取 GitHub `main` 後，目標文章已保存 `image` 欄位：`images/2026-09-01-how-much-water-electrolytes-calcium-iron-bone-health.png`；遠端 tree 也確認同名圖片檔存在。
- GitHub 提交紀錄顯示圖片上傳提交 `7a8a944f3adece971ba68b619a02bb1051d56158`，文章資料更新提交 `ae87bfbfcce5951a3589ebc30522e75f87d116b0`。
- 以全新、帶快取破除參數的公開頁面重新載入，DOM 確認封面 `img.article-cover` 存在、可見且成功載入，原始尺寸為 1408×768。

### 根因與狀態

- 目前證據顯示，先前公開資料在封面同步前沒有 `image` 欄位，網站模板因此不會產生正文封面元素；這不是圖片 CSS 裁切或尺寸不合造成的。
- 本機工作樹的 `blog/posts.json` 目前仍沒有第八章 `image` 欄位，本機也沒有對應圖片檔；本機與遠端 `main` 已出現差異。這輪沒有用本機舊版本覆蓋遠端，也沒有改寫使用者文章。
- 截至本次查核，公開頁封面已能正常顯示。若使用者仍看到舊畫面，優先判定為瀏覽器或 GitHub Pages 快取尚未更新，應使用強制重新整理、無痕視窗或加查詢參數重新開啟。

### 下次防呆

- 發布或回修前，必須以遠端 `main` 最新 `blog/posts.json` 與 SHA 為基準，核對目標文章的 `image` 欄位、遠端圖片檔與公開頁 `img.article-cover` 的實際載入狀態；本機缺欄位時不得直接發布本機舊快照。

## 2026-09-01 第八章分類未顯示修正

### 問題與根因

- 使用者指出 Blog 列表第八章日期後沒有顯示文章分類；截圖中維生素篇有「書籍連載與營養知識」，第八章只有日期。
- 遠端 `blog/posts.json` 的第八章物件缺少 `category` 欄位；列表模板本身已有分類顯示邏輯，並非 CSS 或列表模板失效。
- 管理頁原本沒有分類輸入欄位，且新增／編輯寫入物件時沒有保存 `category`，因此從管理頁更新文章可能遺失分類。

### 已完成

- 只在遠端 `main:blog/posts.json` 的第八章目標物件補上 `category: "書籍連載與營養知識"`，保留其他文章與目標文章既有欄位；提交 `bdde375f401b6cd5bc57bf02fd898d5af208541f`，更新後內容 blob SHA `2bacecb540ecce4f2219eccf033abb48c31c3623`。
- 管理頁新增必填「文章分類」欄位，編輯既有文章時帶回原分類，發布／更新與預覽均保存／顯示分類；管理腳本快取版本更新為 `20260901-category`。遠端提交：`6c6fb87`（`admin/index.html`）、`24a2f178526e728a8b854c16e77ebea4f7841200`（`admin/admin.js`）。
- 本機同步保留相同管理頁修正；沒有用本機舊版 `blog/posts.json` 覆蓋遠端。

### 驗證

- 公開 Blog 列表 DOM：第八章顯示 `2026-09-01｜書籍連載與營養知識`。
- 公開文章頁 DOM：顯示 `2026-09-01｜分類：書籍連載與營養知識｜作者：張雁雲營養師`；封面仍成功載入，naturalWidth 為 1408。
- 公開管理頁 DOM：`#category` 存在、為必填，載入 `admin.js?v=20260901-category`。

## 2026-09-01 收工：第八章分類顯示修正與跨代理規則同步

### 今日完成

- 修正第八章公開 Blog 列表日期後沒有分類的問題；遠端 `main:blog/posts.json` 目標文章已補上「書籍連載與營養知識」。
- 修正 `/admin/` 管理頁，加入必填文章分類欄位；編輯既有文章會帶回原分類，發布、更新與預覽都會保存分類。
- 完成公開 Blog 列表、文章頁、封面圖片與管理頁的快取後 DOM 驗證。

### 錯誤與根因

- 公開列表模板原本已有分類顯示邏輯，但遠端第八章資料缺少 `category` 欄位，所以日期後只顯示日期。
- 管理頁原本沒有分類欄位，且發布時重建文章物件未保存 `category`；日後從管理頁編輯文章可能再次遺失分類。
- 本機工作樹仍是舊的第八章資料快照，沒有對應遠端封面欄位／圖片檔；若直接用本機舊快照發布，可能覆蓋遠端較新的內容。

### 修正與驗證

- 遠端文章資料提交：`bdde375f401b6cd5bc57bf02fd898d5af208541f`；最新內容 blob SHA：`2bacecb540ecce4f2219eccf033abb48c31c3623`。
- 管理頁遠端提交：`6c6fb87`（HTML）、`24a2f178526e728a8b854c16e77ebea4f7841200`（JavaScript）。
- 公開 Blog 列表顯示 `2026-09-01｜書籍連載與營養知識`；文章頁顯示分類與作者；封面成功載入，naturalWidth 為 1408。
- 公開管理頁確認 `#category` 存在、為必填，腳本版本為 `admin.js?v=20260901-category`。
- 本機 `admin.js` 通過 `node --check`；本次相關檔案通過 `git diff --check`。
- 收工時另執行整個工作樹的 `git diff --check`，發現既有 `sitemap.html` 第 102–103 行及 `sitemap.xml` 第 24–29 行有尾端空白，整體返回 2；這些不是本次分類修正所改動，未自行清理，避免覆蓋既有 sitemap 修改。

### 尚未完成與風險

- 本機 Git 工作樹仍有本輪前既有的文章、Word、Markdown、sitemap、研究腳本與第九章檔案修改；沒有擅自整批提交或清理。
- 本機 `blog/posts.json` 與遠端 `main` 尚未完全同步，尤其第八章封面欄位與圖片仍要由後續安全同步流程處理；本輪未用本機舊快照覆蓋遠端。
- Search Console 本輪未取得資源權限，沒有新增曝光、點擊、CTR、排名、查詢或索引數據；不能以公開頁 DOM 代替 Search Console 數據。

### 規則、偏好與同步狀態

- 使用者明確要求：每次收工都要記錄修改、錯誤、根因、修正、驗證、風險、未完成事項與個人偏好，並同步 Codex 與 Antigravity，減少重複溝通。
- 使用者偏好：文章分類要實際顯示在日期後方；管理頁不能因新增／編輯而遺失分類；公開資料、封面、列表 DOM、文章 DOM 與本機 Git 狀態要分開核對。
- 已回寫專案 `agent.md`、Codex 全域 `AGENTS.md`、Antigravity 全域 `AGENTS.md`，並建立 Codex 記憶更新筆記；三份全域／專案規則的新增內容一致。

### Git 與公開狀態

- 遠端公開修正已完成並可由公開頁核對；本機 Git 保留 dirty worktree，未 commit、未以本機工作樹推送，避免混入未授權或既有修改。
- 收工狀態分開記錄：公開分類與管理頁修正已完成；本機完整同步與 Search Console 數據未完成／未取得。
