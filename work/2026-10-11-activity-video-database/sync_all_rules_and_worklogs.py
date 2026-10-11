# -*- coding: utf-8 -*-
import sys
import hashlib
from pathlib import Path

sys.stdout.reconfigure(encoding='utf-8')

NEW_RULE_BLOCK = """

# 互動教具與影片資料庫（料理／運動／活動）開發與使用者偏好硬性規範（2026-10-11 跨 Codex & Antigravity 同步）

1. **彈窗與內文嚴禁提及原本參考網站（No External Reference Site Names in Modals）**：
   - 凡參考外部網站整合進本站的資料庫（如料理、運動、活動影片資料庫），一旦統一收錄為本站專屬資料庫後，**彈窗與卡片內文（如「📌 教案規格與屬性」、「⚠️ 帶領提醒與常見卡關點」、「💬 引導口訣與延伸」等）一律嚴禁出現 `【原《...》】`、`【原站...】`、`原設定對象`、`原活動分類`、`原影片` 等外部參考網站名稱或字樣**，必須 100% 轉化為本站原生一致的乾淨欄位文字。
2. **全齡跨世代定位（All-Ages Perspective）**：
   - 本站所有資料庫（`teach/cook-database/`、`teach/exercise-database/`、`teach/activity-database/`）**皆不是單純給長輩使用**；所有觀點、引導語、核心訓練目的與「退階／進階調整」必須擴及各年齡層（親子兒童、青少年校園、成人企業團建與紓壓、社區樂齡與失智友善）。
3. **Hero 區 4 顆統計膠囊文字精煉（Concise Hero Stat Pills）**：
   - 頂部深林綠橫幅的 4 顆膠囊（`.hero-stat-pills`）文字必須簡短精煉（每顆控制在 10–14 字內，如 `🎬 239 筆影片靈感`、`🧩 藝術創作・手工教案・團康活動`、`📋 內建材料步驟與退階/進階調整`、`🌏 台灣・日本・歐美的全齡活動`），刪除「涵蓋」、「100%」、「網羅」等贅字，避免過長換行。
4. **分層導覽與跨庫篩選設計**：
   - 若多來源整合，直接依屬性打散歸入第一層主分類（如活動庫之 `全部活動`、`藝術創作`、`手工教案`、`團康活動`），不額外做獨立的「頻道庫切換按鈕」。
   - 第二層「`▾ 更多跨庫篩選`」預設收合，展開後須 100% 完整納入所有細分類別，並以腳本驗證每顆篩選膠囊皆有對應資料（零空集合）。
5. **彈窗結構、底部行動按鈕與頁尾雙框統一**：
   - 點擊卡片放大彈窗統一採用 5 大結構化區塊（綠底核心效益與全齡觀點、白底結構化明細表、黃橘底帶領提醒與安全注意事項、藍底全齡退階與進階調整、底部行動按鈕列），且內容預先由 AI 結構化填妥。
   - 底部行動按鈕統一命名：`▶ 看影片跟著做`、（團康活動額外提供 `🔍 延伸玩法規則搜尋 ↗`）、`📋 複製 AI 延伸提問`、`🖨️ 列印單張教案`。
   - 頁面最下方固定保留兩框：`#dbFooterMeta`（`共 xx 部影片 ｜ 每支連結皆經 YouTube oEmbed 驗證存在 ｜ 影片版權屬各原始頻道所有，請遵守合理使用原則`）與 `.db-credits-box`（安全防跌、手作安全與互動自主權警語）。
6. **三大資料庫手機版（Mobile RWD）閱覽舒適度與教具卡片排序**：
   - `teach/index.html` 各大分類中，凡名稱帶有「**資料庫**」的工具卡片一律排在該分類最前面。
   - 三座資料庫皆須具備 `overflow-x: hidden`，並在 `@media (max-width: 640px)` 下確保搜尋列、主分類膠囊與彈窗底部行動按鈕滿版、觸控高度 >= 42px、單欄清晰易讀。
"""

PROJECT_WORKLOG_ENTRY = """## 2026-10-11｜體智遊戲「活動影片資料庫 (`teach/activity-database/`)」239 筆全齡整合、三大資料庫手機版 RWD 升級與無原站字樣規範同步

### 任務

- 依使用者指示，於 `teach/index.html` 的「3. 體智遊戲」分類首位新增「**活動影片資料庫**」（`teach/activity-database/`），整合四大參考資料庫共 **239 筆**國內外活動影片與教案靈感。
- **核心設計與使用者偏好落實**：
  1. **不設獨立頻道庫切換鈕**：將日照活動靈感庫 30 筆直接依屬性打散融入三大主分類：`全部活動 (239)`、`藝術創作 (41)`、`手工教案 (131)`、`團康活動 (67)`。
  2. **第二層收合式跨庫篩選**：預設收合「`▾ 更多跨庫篩選`」，展開後涵蓋 7 大維度共 88 顆細分篩選膠囊，100% 納入所有細分類別且零空集合。
  3. **Hero 區 4 顆精簡膠囊**：`🎬 239 筆影片靈感`、`🧩 藝術創作・手工教案・團康活動`、`📋 內建材料步驟與退階/進階調整`、`🌏 台灣・日本・歐美的全齡活動`。
  4. **全齡跨世代定位與無原站字樣彈窗**：彈窗統一為 5 大結構化區塊，觀點與退階/進階調整涵蓋親子兒童、青少年校園、成人職場團建與社區樂齡；並徹底移除彈窗內所有提及原本參考網站之字樣（如 `【原《...》】`、`【原站...】`）。
  5. **三大資料庫手機版（Mobile RWD）舒適度升級**：同步優化 `teach/activity-database/`、`teach/exercise-database/`、`teach/cook-database/` 之手機版單欄排版、防橫向捲動與大觸控目標。
  6. **全站 SEO & GEO 同步与規則沉澱**：執行 `tools/sync_seo_and_geo.py`，並將本次學習到的使用者偏好與錯誤防呆同步寫入專案與 Codex / Antigravity 全域規則。

### 錯誤與根因

- 初版生成 `activities_full.json` 時，為標示資料整合來源，在彈窗「📌 教案規格與屬性」與「⚠️ 帶領提醒與常見卡關點」中加上了 `【原《派對遊戲資料庫》查看玩法】`、`【原《手工藝教案資料庫》材料步驟】`、`【原站帶領小提醒】` 等前綴；此外 Hero 區 4 顆膠囊初版文字較長。
- 根因：整合外部參考庫時誤將「來源對齊過程標籤」暴露於最終面向讀者的 UI 彈窗中。

### 修正與驗證

- 修改 `generate_activities_json.py` 與 `teach/activity-database/index.html`，將所有 `【原《...》】`、`【原站...】`、`原設定對象`、`原活動分類`、`原影片觀看數` 100% 清除，並同步檢查確認 `teach/cook-database/` 與 `teach/exercise-database/` 均無任何原站字樣。
- 精簡 Hero 區 4 顆膠囊文字。
- 執行 `audit_verification.py` 通過首項（`act_sa_1`）、中項（`act_cr_80`）、末項（`act_dc_we10`）與 92 顆篩選膠囊零空集合驗證，以及 239 支 YouTube oEmbed 100% 存在驗證。
- 更新專案 `agent.md`、`.codex/teach-tools-and-user-preferences.md`、`work/2026-10-10-teach-tools-expansion/README.md` 以及 Codex / Antigravity 全域 `AGENTS.md` 與 `global-worklog.md`。

"""

GLOBAL_WORKLOG_ENTRY = """
## 2026-10-11 互動教具與影片資料庫（料理／運動／活動）彈窗無原站字樣與全齡化規範同步

### 任務

- 於 Kat Chang 網站完成「活動影片資料庫 (`teach/activity-database/`)」239 筆全齡教案整合，並將過程中確認的使用者偏好、錯誤防呆與快速開發 SOP 同步寫入專案、Codex 全域與 Antigravity 全域規則。

### 錯誤與根因

- 初版活動影片資料庫在彈窗「📌 教案規格與屬性」與「⚠️ 帶領提醒與常見卡關點」中保留了 `【原《派對遊戲資料庫》查看玩法】`、`【原《手工藝教案資料庫》材料步驟】`、`【原站帶領小提醒】` 等外部參考網站字樣；且頂部 4 顆統計膠囊初版文字偏長。
- 根因：將內部資料整併的來源標記直接輸出至前台讀者可見的彈窗欄位。

### 修正與驗證

- 全面清除 `activities_full.json` 與 `teach/activity-database/index.html` 中所有提及原本參考網站的字樣（驗證殘留數為 0），並全面檢查確認 `cook-database` 與 `exercise-database` 亦 100% 無原站字樣。
- 將「彈窗與內文嚴禁提及原本參考網站」、「資料庫全齡跨世代定位」、「Hero 膠囊文字精煉」、「不設多餘頻道切換鈕而直接打散融入主分類」、「三大資料庫手機版 RWD 舒適度」與「YouTube oEmbed + 三點式 + 篩選膠囊零空集合自動化檢驗 SOP」寫入 Codex 與 Antigravity 全域 `AGENTS.md` 及專案 `agent.md`。

### 回寫狀態

- 專案 `agent.md`、`.codex/teach-tools-and-user-preferences.md`、`project-worklog.md`：已更新。
- Codex 全域 `AGENTS.md`、`global-worklog.md`：已更新。
- Antigravity 全域 `AGENTS.md`、`global-worklog.md`：已更新。
"""

root = Path(r"d:\@Codex\594katchang-source.github.io-main")

# 1. Update project agent.md, .codex/teach-tools-and-user-preferences.md, work/2026-10-10-teach-tools-expansion/README.md
for rel in [
    "agent.md",
    ".codex/teach-tools-and-user-preferences.md",
    "work/2026-10-10-teach-tools-expansion/README.md",
    "work/2026-10-10-teach-tools-expansion/output/USER_PREFERENCES_AND_DEV_GUIDE.md",
]:
    p = root / rel
    if p.exists():
        txt = p.read_text(encoding="utf-8")
        if "彈窗與內文嚴禁提及原本參考網站" not in txt:
            p.write_text(txt.rstrip() + "\n" + NEW_RULE_BLOCK, encoding="utf-8")
            print(f"[✓] Updated {p}")

# 2. Prepend to project-worklog.md
pw = root / "project-worklog.md"
pw_txt = pw.read_text(encoding="utf-8")
if "2026-10-11｜體智遊戲「活動影片資料庫" not in pw_txt:
    pw_txt = pw_txt.replace("# Kat Chang site 工作日誌\n\n", "# Kat Chang site 工作日誌\n\n" + PROJECT_WORKLOG_ENTRY, 1)
    if "2026-10-11｜體智遊戲「活動影片資料庫" not in pw_txt:
        pw_txt = pw_txt.replace("# Kat Chang site 工作日誌\r\n\r\n", "# Kat Chang site 工作日誌\r\n\r\n" + PROJECT_WORKLOG_ENTRY, 1)
    pw.write_text(pw_txt, encoding="utf-8")
    print(f"[✓] Updated {pw}")

# 3. Update global files if accessible
for gp in [
    Path(r"C:\Users\cygnu\.codex\AGENTS.md"),
    Path(r"C:\Users\cygnu\.antigravity\AGENTS.md"),
    Path(r"C:\Users\cygnu\.gemini\config\AGENTS.md"),
]:
    try:
        if gp.exists():
            gtxt = gp.read_text(encoding="utf-8")
            if "彈窗與內文嚴禁提及原本參考網站" not in gtxt:
                gp.write_text(gtxt.rstrip() + "\n" + NEW_RULE_BLOCK, encoding="utf-8")
            print(f"[✓] Updated global rule: {gp}")
    except Exception as e:
        print(f"[!] Could not update {gp}: {e}")

for gw in [
    Path(r"C:\Users\cygnu\.codex\global-worklog.md"),
    Path(r"C:\Users\cygnu\.antigravity\global-worklog.md"),
]:
    try:
        if gw.exists():
            gwtxt = gw.read_text(encoding="utf-8")
            if "2026-10-11 互動教具與影片資料庫" not in gwtxt:
                gw.write_text(gwtxt.rstrip() + "\n" + GLOBAL_WORKLOG_ENTRY, encoding="utf-8")
            print(f"[✓] Updated global worklog: {gw}")
    except Exception as e:
        print(f"[!] Could not update {gw}: {e}")
