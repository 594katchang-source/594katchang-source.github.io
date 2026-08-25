# 🔐 Google Search Console 授權與自動化登錄指南

為了讓 AI / 程式端能代表您**自動化提交網址、即時檢查 Google 索引狀態、抓取排名數據**，Google 官方提供最安全且不需洩漏個人 Google 帳號密碼的「**服務帳號（Service Account）API 串接機制**」。

---

## 🛠️ 三步完成 Google Search Console API 自動化授權

### 第一步：在 Google Cloud Console 建立免費服務帳號
1. 前往 [Google Cloud Console](https://console.cloud.google.com/)。
2. 建立新專案（例如 `katchang-seo-indexer`）。
3. 進入 **API 和服務 > 程式庫**，搜尋並啟用 **「Web Search Console API」** 與 **「Indexing API」**。
4. 前往 **憑證 (Credentials) > 建立憑證 > 服務帳號 (Service Account)**：
   - 服務帳號名稱：`seo-bot`
   - 系統會產生一組 Email（例如：`seo-bot@katchang-seo-indexer.iam.gserviceaccount.com`）。
5. 點擊該服務帳號進入 **金鑰 (Keys) > 新增金鑰 > 建立新金鑰 (JSON)**，下載金鑰檔案。

---

### 第二步：在 Google Search Console 後台新增授權
1. 開啟 [Google Search Console](https://search.google.com/search-console)。
2. 選擇資源 `https://594katchang-source.github.io/`。
3. 點選左側選單最下方的 **「設定 (Settings)」 > 「使用者與權限 (Users and permissions)」**。
4. 點擊右上角 **「新增使用者 (Add user)」**：
   - **電子郵件**：貼上剛才的服務帳號 Email（例如 `seo-bot@...iam.gserviceaccount.com`）。
   - **權限**：選擇 **「擁有者 (Owner)」** 或 **「完整 (Full)」**。
5. 點擊「新增」完成授權。

---

### 第三步：將金鑰檔案放入專案
將下載的 JSON 金鑰檔案重新命名為 `service_account.json`，放置於：
`d:\@Codex\594katchang-source.github.io-main\work\2026-08-21-seo-growth-strategy\service_account.json`
（本機 `.gitignore` 已保護此類機敏金鑰，不會被推送到公開 GitHub）。

一旦放置完成，每次有新文章或頁面發布，執行 `python gsc_indexer.py` 即可在 **1 秒內全自動通知 Google 建立即時索引**！

---

## ⚡ 若目前尚未設定 API 金鑰：最快速手動提交法（只需 30 秒）
1. 登入 [Google Search Console](https://search.google.com/search-console)。
2. 在上方搜尋欄輸入 `https://594katchang-source.github.io/` 按 Enter。
3. 點擊 **「要求建立索引 (Request Indexing)」**。
4. 依序對 `https://594katchang-source.github.io/about.html` 與 `https://594katchang-source.github.io/class.html` 重複此動作即可！
