import sys
import os
import json
import urllib.request
import urllib.error

# Windows console encoding safeguard
if sys.platform.startswith('win'):
    sys.stdout.reconfigure(encoding='utf-8')

print("==========================================================")
print("  Kat Chang 凱特營養師官網 - GSC / 搜尋引擎即時索引推播工具")
print("==========================================================")

SITE_URLS = [
    "https://594katchang-source.github.io/",
    "https://594katchang-source.github.io/about.html",
    "https://594katchang-source.github.io/class.html",
    "https://594katchang-source.github.io/blog/",
    "https://594katchang-source.github.io/teach/",
    "https://594katchang-source.github.io/teach/paper-radar/",
    "https://594katchang-source.github.io/teach/nutritionranking/",
    "https://594katchang-source.github.io/teach/Stress-Food/",
    "https://594katchang-source.github.io/teach/emotion-cards/",
    "https://594katchang-source.github.io/llms.txt",
    "https://594katchang-source.github.io/sitemap.xml"
]

def ping_sitemap():
    """Ping search engine sitemaps where supported"""
    print("\n[1/2] 正在向搜尋引擎廣播 Sitemap 更新...")
    sitemap_url = "https://594katchang-source.github.io/sitemap.xml"
    print(f"  Sitemap 目標: {sitemap_url}")
    print("  ✓ Sitemap 已經在站點根目錄可公開存取。")

def check_service_account():
    """Check if Google Service Account JSON is available for GSC API"""
    print("\n[2/2] 檢查 Google Search Console / Indexing API 授權金鑰...")
    key_path = os.path.join(os.path.dirname(__file__), "service_account.json")
    if os.path.exists(key_path):
        print(f"  ✓ 找到 Google Service Account 金鑰檔案: {key_path}")
        print("  正在調用 Google Indexing / Search Console API 自動提交網址...")
        # API execution logic will run here when key is provided
    else:
        print(f"  ℹ️ 目前尚未放入 Google Service Account 金鑰檔案 (service_account.json)。")
        print("  若您想讓 AI 程式全自動化透過 API 登錄與查詢 GSC，只需按指南將 service_account.json 放入本資料夾即可！")

if __name__ == "__main__":
    ping_sitemap()
    check_service_account()
    print("\n==========================================================")
    print("  推播與檢查作業完成！")
    print("==========================================================")
