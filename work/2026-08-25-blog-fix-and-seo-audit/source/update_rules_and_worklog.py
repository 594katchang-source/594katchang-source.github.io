# -*- coding: utf-8 -*-
from pathlib import Path
import sys

sys.stdout.reconfigure(encoding='utf-8')

ROOT_DIR = Path(r"d:\@Codex\594katchang-source.github.io-main")
agent_file = ROOT_DIR / "agent.md"
worklog_file = ROOT_DIR / "project-worklog.md"

agent_text = agent_file.read_text(encoding="utf-8")

old_target = """文章頁：

- 新文章先更新 `blog/posts.json`，再補圖片。
- 圖片檔名建議含日期與主題，避免空白與特殊符號過多。"""

new_target = """文章頁：

- **新文章發布日期與圖片命名硬性規範**：新文章發布時，文章發布日期（`post.date`）、文章 ID（如 `YYYY-MM-DD-slug`）與封面圖片檔名（如 `blog/images/YYYY-MM-DD-slug.png`），一律以「**正式推上 GitHub 當日**」的實際日期為準，確保發布時間、ID 與圖片日期三者完全一致，嚴禁殘留舊草稿日期。
- 新文章先更新 `blog/posts.json`，再補圖片。
- 圖片檔名必須包含「與發布日相同的 YYYY-MM-DD 前綴」與英文主題 slug，避免空白與特殊符號。"""

if old_target in agent_text:
    agent_text = agent_text.replace(old_target, new_target, 1)
    agent_file.write_text(agent_text, encoding="utf-8")
    print("[✓] agent.md 已成功寫入文章發布日期硬性規範！")
else:
    print("[!] agent.md 未找到替換字串，請檢查。")

# 更新 project-worklog.md
worklog_entry = """

## 2026-08-25: 部落格發布日期規則確立、封面圖名同步與全站 SEO/AI 關鍵字審查優化

- **封面圖檔名與發布日同步**：將維生素篇封面圖片由 `2026-08-23-vitamins-book-notes.png` 重新命名為 `2026-08-25-vitamins-book-notes.png`，與文章發布日期完全一致。
- **寫入專案硬性規則**：在 `agent.md` 明確訂定「新文章發布一律以正式推上 GitHub 當日為發布日期（`post.date`），且封面圖檔名前綴必須與發布日相同（`YYYY-MM-DD-slug.png`）」。
- **分類與搜尋機制優化**：全站 11 篇衛教文章分類與關鍵字全面升級，文章內頁修復分類顯示（`.category-tag`），並完成全站 `sitemap.xml`、`llms.txt` 同步更新。
"""

worklog_text = worklog_file.read_text(encoding="utf-8")
worklog_file.write_text(worklog_text + worklog_entry, encoding="utf-8")
print("[✓] project-worklog.md 工作日誌已同步追加！")
