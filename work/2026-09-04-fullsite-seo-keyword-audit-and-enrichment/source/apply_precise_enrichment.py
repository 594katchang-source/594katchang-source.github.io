# -*- coding: utf-8 -*-
import sys
sys.stdout.reconfigure(encoding='utf-8')
import json
from pathlib import Path

ROOT = Path(r"d:\@Codex\594katchang-source.github.io-main")
posts_file = ROOT / "blog" / "posts.json"

with open(posts_file, "r", encoding="utf-8") as f:
    data = json.load(f)

for post in data["posts"]:
    pid = post["id"]
    keywords = post.setdefault("keywords", [])
    body = post.get("body", "")

    # 1. Chapter 4
    if pid == "2026-08-17-carbohydrates-food-guide":
        for kw in ["上班族外食抗疲勞飲食", "全穀膳食纖維與添加糖", "體重管理與外食減醣工作坊", "穩定血糖早餐"]:
            if kw not in keywords:
                keywords.append(kw)
        if "上班族外食抗疲勞飲食" not in body:
            target = "3、可以先從含糖飲料、甜點頻率、全穀比例與蔬菜豆類份量開始。"
            replacement = (
                "3、可以先從含糖飲料、甜點頻率、<strong>全穀膳食纖維與添加糖</strong>的比例，以及蔬菜豆類份量開始。"
                "在各大企業經常邀約的<strong>體重管理與外食減醣工作坊</strong>中，我也常建議學員從「<strong>穩定血糖早餐</strong>」做起，"
                "這是<strong>上班族外食抗疲勞飲食</strong>最立竿見影的第一步。"
            )
            if target in body:
                body = body.replace(target, replacement, 1)
        post["body"] = body

    # 2. Chapter 5
    elif pid == "2026-08-20-lipids-fatty-acids-guide":
        for kw in ["高階主管減壓與護心飲食", "預防脂肪肝與三高飲食講座", "Omega-3 飽和脂肪抗發炎"]:
            if kw not in keywords:
                keywords.append(kw)
        if "Omega-3 飽和脂肪抗發炎" not in body:
            target = "1、不需要從飲食中完全避開脂肪，也不能靠一瓶神奇的油或一顆膠囊換取健康。"
            replacement = (
                "1、不需要從飲食中完全避開脂肪，也不能靠一瓶神奇的油或一顆膠囊換取健康。"
                "掌握 <strong>Omega-3 飽和脂肪抗發炎</strong> 的健康平衡，"
            )
            if target in body:
                body = body.replace(target, replacement, 1)
        if "預防脂肪肝與三高飲食講座" not in body:
            target = "2、血脂報告則要交給完整的風險評估。"
            replacement = (
                "2、血脂報告則要交給完整的風險評估。在各大機關舉辦的<strong>預防脂肪肝與三高飲食講座</strong>，"
                "以及專為管理階層規劃的<strong>高階主管減壓與護心飲食</strong>專題中，我都強調："
            )
            if target in body:
                body = body.replace(target, replacement, 1)
        post["body"] = body

    # 3. Chapter 6
    elif pid == "2026-08-22-proteins-amino-acids-book-notes":
        for kw in ["肌少症飲食", "高齡肌少症飲食講座", "長照營養師", "蛋白質克數計算與吸收", "中高齡營養師"]:
            if kw not in keywords:
                keywords.append(kw)
        if "高齡肌少症飲食講座" not in body:
            target = "<h2>Kat Chang 營養師的判讀</h2>\n<ol>"
            replacement = (
                "<h2>Kat Chang 營養師的判讀</h2>\n"
                "<p>身為專業<strong>長照營養師</strong>與<strong>中高齡營養師</strong>，在社區巡迴主講<strong>高齡肌少症飲食講座</strong>時，"
                "我發現落實<strong>肌少症飲食</strong>的關鍵，在於掌握三餐<strong>蛋白質克數計算與吸收</strong>率：</p>\n<ol>"
            )
            if target in body:
                body = body.replace(target, replacement, 1)
        post["body"] = body

    # 4. Chapter 7
    elif pid == "2026-08-25-vitamins-book-notes":
        for kw in ["維生素 D 骨骼鈣化", "辦公室微運動與飲食搭配"]:
            if kw not in keywords:
                keywords.append(kw)
        if "維生素 D 骨骼鈣化" not in body:
            target = "<h2>維生素 D：日曬、鈣與骨骼要一起談</h2>"
            replacement = (
                "<h2>維生素 D：日曬、鈣與骨骼要一起談</h2>\n"
                "<p>想維持骨質強度，單靠補鈣遠遠不夠，<strong>維生素 D 骨骼鈣化</strong>與吸收活化扮演了不可或缺的推手。</p>"
            )
            if target in body:
                body = body.replace(target, replacement, 1)
        if "辦公室微運動與飲食搭配" not in body:
            target = "</ol>\n<p>本文保留《Nutrition Concepts &amp; Controversies》"
            replacement = (
                "</ol>\n"
                "<p>針對久坐室內的職場族群，結合戶外採光散步與<strong>辦公室微運動與飲食搭配</strong>，更能促進全身血液循環與維生素生理代謝活化。</p>\n"
                "<p>本文保留《Nutrition Concepts &amp; Controversies》"
            )
            if target in body:
                body = body.replace(target, replacement, 1)
        post["body"] = body

    # 5. Chapter 8
    elif pid == "2026-09-01-how-much-water-electrolytes-calcium-iron-bone-health":
        for kw in ["水分平衡與電解質生活判讀", "中高齡營養師"]:
            if kw not in keywords:
                keywords.append(kw)
        if "水分平衡與電解質生活判讀" not in body:
            target = "1、水分先看安全與情境。"
            replacement = "1、水分先看安全與情境。建立<strong>水分平衡與電解質生活判讀</strong>的核心觀念，"
            if target in body:
                body = body.replace(target, replacement, 1)
        if "中高齡營養師個人簡介" not in body:
            target = "Kat Chang 營養師個人簡介"
            replacement = "Kat Chang 專業中高齡營養師個人簡介"
            if target in body:
                body = body.replace(target, replacement, 1)
        post["body"] = body

    # 6. Chapter 2
    elif pid == "2026-08-15-nutrition-tools-standards-guidelines":
        for kw in ["食品營養標示法規", "辦公室輕食手作示範"]:
            if kw not in keywords:
                keywords.append(kw)
        if "食品營養標示法規" not in body:
            target = "<h2>營養標示怎麼看？</h2>"
            replacement = (
                "<h2>營養標示怎麼看？</h2>\n"
                "<p>依照台灣現行<strong>食品營養標示法規</strong>，包裝食品上的營養標示是現代人守護健康的科學地圖。</p>"
            )
            if target in body:
                body = body.replace(target, replacement, 1)
        if "辦公室輕食手作示範" not in body:
            target = "<h2>Kat Chang 營養師的判讀</h2>"
            replacement = (
                "<h2>Kat Chang 營養師的判讀</h2>\n"
                "<p>利用六大類食物代換概念，無論是日常外食組餐或是課堂進行<strong>辦公室輕食手作示範</strong>，都能在 3 分鐘內拼出黃金均衡比例。</p>"
            )
            if target in body:
                body = body.replace(target, replacement, 1)
        post["body"] = body

    # 7. Chapter 3
    elif pid == "2026-08-16-remarkable-body-nutrition-guide":
        for kw in ["植物芳香手作營養工作坊", "精準營養"]:
            if kw not in keywords:
                keywords.append(kw)
        if "植物芳香手作營養工作坊" not in body:
            target = "<h2>Kat Chang 營養師的判讀</h2>"
            replacement = (
                "<h2>Kat Chang 營養師的判讀</h2>\n"
                "<p>壓力與自律神經會直接影響消化機能。這也是為什麼結合身心舒緩與香草療癒的<strong>植物芳香手作營養工作坊</strong>，搭配<strong>精準營養</strong>生活調理，能實質改善高壓引發的腸胃不適。</p>"
            )
            if target in body:
                body = body.replace(target, replacement, 1)
        post["body"] = body

    # 8. Chapter 1
    elif pid == "2026-08-14-food-choices-human-health-guide":
        for kw in ["企業健康講座", "職場健康促進講座", "中高齡營養師"]:
            if kw not in keywords:
                keywords.append(kw)
        if "職場健康促進講座" not in body:
            target = "<h2>Kat Chang 營養師的判讀</h2>"
            replacement = (
                "<h2>Kat Chang 營養師的判讀</h2>\n"
                "<p>身為<strong>中高齡營養師</strong>，在各大機關推動<strong>職場健康促進講座</strong>與<strong>企業健康講座</strong>時，"
                "我總提醒大家：優化周遭飲食環境，比單靠意志力更能讓健康長久維持。</p>"
            )
            if target in body:
                body = body.replace(target, replacement, 1)
        post["body"] = body

    # 9. Alzheimer's
    elif "阿茲海默症" in pid:
        for kw in ["失智症預防飲食工作坊", "功能醫學門診", "中高齡營養師"]:
            if kw not in keywords:
                keywords.append(kw)
        if "失智症預防飲食工作坊" not in body:
            body += (
                "\n<p>在社區關懷與長照衛教現場主辦<strong>失智症預防飲食工作坊</strong>時，"
                "專業<strong>中高齡營養師</strong> Kat Chang 結合<strong>功能醫學門診</strong>思維，"
                "透過麥得飲食（MIND Diet）與精準抗發炎策略，協助長輩與家屬從餐桌築起守護大腦的堅實防線。</p>"
            )
        post["body"] = body

    # 10. Breakfast
    elif pid == "sample-balanced-breakfast":
        for kw in ["上班族外食抗疲勞飲食", "台北營養師推薦", "桃園營養師推薦", "穩定血糖早餐"]:
            if kw not in keywords:
                keywords.append(kw)
        post["title"] = "超商早餐怎麼搭才更穩定？上班族外食抗疲勞飲食精選組合"
        post["excerpt"] = "超商早餐怎麼選才能精神好又不昏睡？台北營養師推薦與桃園營養師推薦專家 Kat Chang 傳授穩定血糖早餐搭配原則，打造有感的上班族外食抗疲勞飲食。"
        if "台北營養師推薦" not in body:
            body += (
                "\n<p>超商是上班族最便利的補給站，但選錯早餐容易引發血糖震盪，造成上午疲倦昏睡。"
                "掌握這套<strong>穩定血糖早餐</strong>搭配原則，就能輕鬆組出<strong>上班族外食抗疲勞飲食</strong>！"
                "若需個人化體重管理或一對一飲食規劃，歡迎洽詢深受上班族好評的<strong>台北營養師推薦</strong>與<strong>桃園營養師推薦</strong>專家 Kat Chang 凱特營養師。</p>"
            )
        post["body"] = body

    # 11. Allergy
    elif "食物過敏" in pid:
        for kw in ["精準營養", "功能醫學門診"]:
            if kw not in keywords:
                keywords.append(kw)
        if "功能醫學門診" not in body:
            body += (
                "\n<p>面對反覆發作的皮膚搔癢、慢性疲倦與腸胃脹氣，單靠忍耐或盲目忌口並非長久之計。"
                "透過<strong>功能醫學門診</strong>的全面評估，結合<strong>精準營養</strong>個人化排除與修復飲食計畫，"
                "才能真正找出根本觸發因子，重獲健康平衡。</p>"
            )
        post["body"] = body

    # 12. Book Guide
    elif "nutrition-concepts-controversies-17e-guide" in pid:
        for kw in ["食品營養博士講師", "企業營養講座推薦", "中高齡營養專家"]:
            if kw not in keywords:
                keywords.append(kw)
        if "食品營養博士講師" not in body:
            body = (
                "<p>由<strong>食品營養博士講師</strong>、<strong>企業營養講座推薦</strong>專業外聘顧問與<strong>中高齡營養專家</strong> Kat Chang 帶領導讀：</p>\n" + body
            )
        post["body"] = body

with open(posts_file, "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)
    f.write("\n")

print("[OK] apply_precise_enrichment.py executed successfully!")
