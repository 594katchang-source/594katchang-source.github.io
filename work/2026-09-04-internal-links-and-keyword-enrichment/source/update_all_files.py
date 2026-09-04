# -*- coding: utf-8 -*-
import sys
sys.stdout.reconfigure(encoding='utf-8')
import json
from pathlib import Path

ROOT = Path(r"d:\@Codex\594katchang-source.github.io-main")

# 1. Update Chapter 8 in blog/posts.json
posts_path = ROOT / "blog" / "posts.json"
posts_data = json.loads(posts_path.read_text(encoding="utf-8"))
for post in posts_data["posts"]:
    if "water-electrolytes" in post["id"]:
        target_str = "若已有骨質疏鬆或脆弱性骨折，營養要跟治療計畫一起安排，不能取代藥物與醫療追蹤。</p>"
        replacement = (
            "若已有骨質疏鬆或脆弱性骨折，營養要跟治療計畫一起安排，不能取代藥物與醫療追蹤。</p>\n"
            "<p><strong>延伸閱讀與骨骼肌肉系統關聯：</strong>想深入了解維生素 D 與骨骼鈣化機轉，可參考 "
            "<a href=\"https://594katchang-source.github.io/blog/post.html?id=2026-08-25-vitamins-book-notes\">Chapter 7 維生素怎麼吃？從脂溶性、水溶性到補充品風險</a>；"
            "若想精確掌握支撐骨骼結構與肌力的蛋白質需求量，請閱讀 "
            "<a href=\"https://594katchang-source.github.io/blog/post.html?id=2026-08-22-proteins-amino-acids-book-notes\">Chapter 6 蛋白質與胺基酸：從身體功能、食物品質到植物性飲食</a>。"
            "若有慢性病、長照或特定醫療限水需求，歡迎參考 "
            "<a href=\"https://594katchang-source.github.io/about.html\">Kat Chang 營養師個人簡介</a> 預約一對一專業諮詢。</p>"
        )
        if target_str in post["body"] and "延伸閱讀與骨骼肌肉系統關聯" not in post["body"]:
            post["body"] = post["body"].replace(target_str, replacement, 1)
            print("[OK] posts.json Ch8 body updated successfully!")
        else:
            print("[INFO] Target string already updated or not found in Ch8 body")
        break

posts_path.write_text(json.dumps(posts_data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

# Add keywords and FAQ to Chapter 8
for post in posts_data["posts"]:
    if "water-electrolytes" in post["id"]:
        if "骨質疏鬆" not in post.get("keywords", []):
            post["keywords"].append("骨質疏鬆")
        post["faq"] = [
            {
                "question": "Q1：每天一定要喝 2000 ml 的水嗎？",
                "answer": "沒有適用所有人的單一數字。飲品、食物水分、氣溫、流汗、活動、年齡、疾病與藥物都會改變需求。健康成人可用國民健康署 6 至 8 杯水的建議做生活起點，再依情境調整。心臟、腎臟、肝臟疾病或醫師交代限水者，依個人計畫執行。"
            },
            {
                "question": "Q2：瓶裝水一定比自來水好嗎？",
                "answer": "包裝形式本身不代表營養或安全性一定較高。應看來源、合格標示、保存、開封後使用時間與飲用環境。需要礦物質時，也要看產品標示，不能只看「礦泉水」三個字。"
            },
            {
                "question": "Q3：喝咖啡會讓身體脫水嗎？",
                "answer": "咖啡含有水分，咖啡因也可能影響排尿與睡眠。一般人應把重點放在總量、個人反應、糖與奶精，以及是否因喝咖啡而少喝水。心悸、焦慮、睡眠差、孕期或有特定疾病者，請個別確認攝取量。"
            },
            {
                "question": "Q4：覺得疲倦就吃鐵劑，會比較快恢復嗎？",
                "answer": "疲倦單獨出現，無法證明缺鐵。月經量、飲食、腸胃道出血、慢性病與檢驗結果都要一起看。鐵劑應在確認需求後使用，並放在幼兒拿不到的地方。"
            },
            {
                "question": "Q5：吃鈣片就能預防骨質疏鬆嗎？",
                "answer": "鈣是骨骼所需營養素，單靠鈣片不能處理所有骨折風險。骨骼需要鈣、維生素 D、蛋白質、活動、肌力、平衡與適當醫療評估。已有骨質疏鬆、骨折史或長期用藥者，應詢問是否需要 DXA、藥物或營養補充。"
            }
        ]
        break

posts_path.write_text(json.dumps(posts_data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
print("[OK] posts.json Chapter 8 updated cleanly!")
