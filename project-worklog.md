# Kat Chang site 工作日誌

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
