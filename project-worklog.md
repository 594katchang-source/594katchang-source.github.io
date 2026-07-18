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
