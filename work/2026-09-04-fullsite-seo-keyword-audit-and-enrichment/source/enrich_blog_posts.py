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

    # 1. Chapter 4 (2026-08-17-carbohydrates-food-guide)
    if "carbohydrates-food-guide" in pid:
        for kw in ["上班族外食抗疲勞飲食", "全穀膳食纖維與添加糖", "體重管理與外食減醣工作坊", "穩定血糖早餐"]:
            if kw not in keywords:
                keywords.append(kw)
        if "上班族外食抗疲勞飲食" not in body:
            # Insert in 省時版本
            old_str = "很多人把碳水化合物簡化成兩種極端："
            new_str = "本文深入解析<strong>全穀膳食纖維與添加糖</strong>的代謝差異，為現代職場提供<strong>上班族外食抗疲勞飲食</strong>與<strong>穩定血糖早餐</strong>實證解方。很多人把碳水化合物簡化成兩種極端："
            if old_str in body:
                body = body.replace(old_str, new_str, 1)
        if "體重管理與外食減醣工作坊" not in body:
            # Insert in Kat Chang 營養師的判讀
            old_p = "碳水化合物不是健康的敵人，精製與添加糖才是。"
            new_p = "在各大企業經常邀約的<strong>體重管理與外食減醣工作坊</strong>中，我最常強調：碳水化合物不是健康的敵人，精製與添加糖才是。"
            if old_p in body:
                body = body.replace(old_p, new_p, 1)
        post["body"] = body

    # 2. Chapter 5 (2026-08-20-lipids-fatty-acids-guide)
    elif "lipids-fatty-acids-guide" in pid:
        for kw in ["高階主管減壓與護心飲食", "預防脂肪肝與三高飲食講座", "Omega-3 飽和脂肪抗發炎"]:
            if kw not in keywords:
                keywords.append(kw)
        if "Omega-3 飽和脂肪抗發炎" not in body:
            old_str = "很多人把脂肪簡化成「油就是壞的，吃油就會胖、會塞血管」。"
            new_str = "掌握 <strong>Omega-3 飽和脂肪抗發炎</strong> 的平衡比例，是心血管與免疫防護的核心。很多人把脂肪簡化成「油就是壞的，吃油就會胖、會塞血管」。"
            if old_str in body:
                body = body.replace(old_str, new_str, 1)
        if "預防脂肪肝與三高飲食講座" not in body:
            old_p = "脂質是日常生理不可或缺的營養素。"
            new_p = "在企業健檢後諮詢、<strong>預防脂肪肝與三高飲食講座</strong>以及專為管理階層規劃的<strong>高階主管減壓與護心飲食</strong>中，我常提醒：脂質是日常生理不可或缺的營養素，選對好油比盲目無油更重要。"
            if old_p in body:
                body = body.replace(old_p, new_p, 1)
        post["body"] = body

    # 3. Chapter 6 (2026-08-22-proteins-amino-acids-book-notes)
    elif "proteins-amino-acids-book-notes" in pid:
        for kw in ["肌少症飲食", "高齡肌少症飲食講座", "長照營養師", "蛋白質克數計算與吸收", "中高齡營養師"]:
            if kw not in keywords:
                keywords.append(kw)
        if "蛋白質克數計算與吸收" not in body:
            old_str = "很多人把蛋白質簡化成「吃肉就長肉」或「年紀大不敢吃肉」。"
            new_str = "掌握日常三餐<strong>蛋白質克數計算與吸收</strong>率，是實踐<strong>肌少症飲食</strong>的關鍵基礎。很多人把蛋白質簡化成「吃肉就長肉」或「年紀大不敢吃肉」。"
            if old_str in body:
                body = body.replace(old_str, new_str, 1)
        if "高齡肌少症飲食講座" not in body:
            old_p = "蛋白質這部分可以分成三個重點。"
            new_p = "身為專業<strong>長照營養師</strong>與<strong>中高齡營養師</strong>，在社區巡迴主講<strong>高齡肌少症飲食講座</strong>時，我將蛋白質照護整理為三個實務重點："
            if old_p in body:
                body = body.replace(old_p, new_p, 1)
        post["body"] = body

    # 4. Chapter 7 (2026-08-25-vitamins-book-notes)
    elif "vitamins-book-notes" in pid:
        for kw in ["維生素 D 骨骼鈣化", "辦公室微運動與飲食搭配"]:
            if kw not in keywords:
                keywords.append(kw)
        if "維生素 D 骨骼鈣化" not in body:
            old_str = "維生素 D 參與鈣質吸收與骨骼健康"
            new_str = "維生素 D 促成<strong>維生素 D 骨骼鈣化</strong>、維持骨質強度並參與肌肉神經調控"
            if old_str in body:
                body = body.replace(old_str, new_str, 1)
        if "辦公室微運動與飲食搭配" not in body:
            old_p = "維生素這部分可以分成三個重點。"
            new_p = "針對久坐缺乏日照的職場同仁，適度結合戶外採光散步、<strong>辦公室微運動與飲食搭配</strong>，更能促進循環與生理活化。維生素這部分可以分成三個重點："
            if old_p in body:
                body = body.replace(old_p, new_p, 1)
        post["body"] = body

    # 5. Chapter 8 (2026-09-01-how-much-water-electrolytes-calcium-iron-bone-health)
    elif "water-electrolytes" in pid:
        for kw in ["水分平衡與電解質生活判讀", "中高齡營養師"]:
            if kw not in keywords:
                keywords.append(kw)
        if "水分平衡與電解質生活判讀" not in body:
            old_str = "很多人把喝水簡化：每天 2000 ml、尿液越透明越好"
            new_str = "落實正確的<strong>水分平衡與電解質生活判讀</strong>，才能擺脫迷思。很多人把喝水簡化：每天 2000 ml、尿液越透明越好"
            if old_str in body:
                body = body.replace(old_str, new_str, 1)
        post["body"] = body

    # 6. Chapter 2 (2026-08-15-nutrition-tools-standards-guidelines)
    elif "nutrition-tools-standards-guidelines" in pid:
        for kw in ["食品營養標示法規", "辦公室輕食手作示範"]:
            if kw not in keywords:
                keywords.append(kw)
        if "食品營養標示法規" not in body:
            old_str = "營養標示是包裝食品上的營養地圖"
            new_str = "依照台灣現行<strong>食品營養標示法規</strong>，營養標示是包裝食品上的營養地圖"
            if old_str in body:
                body = body.replace(old_str, new_str, 1)
        if "辦公室輕食手作示範" not in body:
            old_p = "六大類食物是把複雜生化轉為生活份量的橋樑"
            new_p = "六大類食物是把複雜生化轉為生活份量的橋樑。無論是外食挑選或是課堂上的<strong>辦公室輕食手作示範</strong>，都能運用這個工具快速組裝出均衡餐盤"
            if old_p in body:
                body = body.replace(old_p, new_p, 1)
        post["body"] = body

    # 7. Chapter 3 (2026-08-16-remarkable-body-nutrition-guide)
    elif "remarkable-body-nutrition-guide" in pid:
        for kw in ["植物芳香手作營養工作坊", "精準營養"]:
            if kw not in keywords:
                keywords.append(kw)
        if "植物芳香手作營養工作坊" not in body:
            old_str = "壓力、情緒與自律神經會直接影響消化液分泌與腸道蠕動。"
            new_str = "壓力、情緒與自律神經會直接影響消化液分泌與腸道蠕動。這也是為什麼結合身心舒緩與香草療癒的<strong>植物芳香手作營養工作坊</strong>，搭配<strong>精準營養</strong>個別調整，能實質改善高壓引發的腸胃不適。"
            if old_str in body:
                body = body.replace(old_str, new_str, 1)
        post["body"] = body

    # 8. Chapter 1 (2026-08-14-food-choices-human-health-guide)
    elif "food-choices-human-health-guide" in pid:
        for kw in ["企業健康講座", "職場健康促進講座", "中高齡營養師"]:
            if kw not in keywords:
                keywords.append(kw)
        if "企業健康講座" not in body:
            old_str = "食物選擇受到家庭、工作、社交與環境深刻影響。"
            new_str = "食物選擇受到家庭、工作、社交與環境深刻影響。在推動<strong>職場健康促進講座</strong>與<strong>企業健康講座</strong>時，我總提醒大家：優化周遭飲食環境，比單靠意志力更能讓健康持久。"
            if old_str in body:
                body = body.replace(old_str, new_str, 1)
        if "中高齡營養師" not in body:
            old_p = "食物選擇不是非黑即白。"
            new_p = "身為<strong>中高齡營養師</strong>，我始終深信食物選擇不是非黑即白，而是找到最適合自己生活步調的健康平衡。"
            if old_p in body:
                body = body.replace(old_p, new_p, 1)
        post["body"] = body

    # 9. Alzheimer's (2026-05-19-功能醫學預防阿茲海默症的系統性介入策略)
    elif "阿茲海默症" in pid:
        for kw in ["失智症預防飲食工作坊", "功能醫學門診", "中高齡營養師"]:
            if kw not in keywords:
                keywords.append(kw)
        if "失智症預防飲食工作坊" not in body:
            addition = (
                "\n<p>在社區關懷與衛教現場主辦<strong>失智症預防飲食工作坊</strong>時，"
                "<strong>中高齡營養師</strong> Kat Chang 結合<strong>功能醫學門診</strong>思維，"
                "透過麥得飲食（MIND Diet）與抗發炎抗氧化精準策略，協助長輩與家屬從餐桌築起守護大腦的堅實防線。</p>"
            )
            body += addition
        post["body"] = body

    # 10. Breakfast (sample-balanced-breakfast)
    elif "sample-balanced-breakfast" in pid:
        for kw in ["上班族外食抗疲勞飲食", "台北營養師推薦", "桃園營養師推薦", "穩定血糖早餐"]:
            if kw not in keywords:
                keywords.append(kw)
        post["title"] = "超商早餐怎麼搭才更穩定？上班族外食抗疲勞飲食精選組合"
        post["excerpt"] = "超商早餐怎麼選才能精神好又不昏睡？台北營養師推薦與桃園營養師推薦專家 Kat Chang 傳授穩定血糖早餐搭配原則，打造有感的上班族外食抗疲勞飲食。"
        if "台北營養師推薦" not in body:
            addition = (
                "\n<p>超商是上班族最便利的補給站，但選錯早餐容易引發血糖震盪，造成上午疲倦昏睡。"
                "掌握這套<strong>穩定血糖早餐</strong>搭配原則，就能輕鬆組出<strong>上班族外食抗疲勞飲食</strong>！"
                "若需個人化體重管理或一對一飲食規劃，歡迎洽詢深受上班族好評的<strong>台北營養師推薦</strong>與<strong>桃園營養師推薦</strong>專家 Kat Chang 凱特營養師。</p>"
            )
            body += addition
        post["body"] = body

    # 11. Allergy (食物過敏知多少)
    elif "食物過敏知多少" in pid:
        for kw in ["精準營養", "功能醫學門診"]:
            if kw not in keywords:
                keywords.append(kw)
        if "功能醫學門診" not in body:
            addition = (
                "\n<p>面對反覆發作的皮膚搔癢、慢性疲倦與腸胃脹氣，單靠忍耐或盲目忌口並非長久之計。"
                "透過<strong>功能醫學門診</strong>的全面評估，結合<strong>精準營養</strong>個人化排除與修復飲食計畫，"
                "才能真正找出根本觸發因子，重獲健康平衡。</p>"
            )
            body += addition
        post["body"] = body

    # 12. Book Guide (2026-08-13-nutrition-concepts-controversies-17e-guide)
    elif "nutrition-concepts-controversies-17e-guide" in pid:
        for kw in ["食品營養博士講師", "企業營養講座推薦", "中高齡營養專家"]:
            if kw not in keywords:
                keywords.append(kw)
        if "食品營養博士講師" not in body:
            old_str = "這本書是許多大專院校營養相關科系愛用的入門經典教材"
            new_str = "由<strong>食品營養博士講師</strong>、<strong>企業營養講座推薦</strong>專業外聘顧問與<strong>中高齡營養專家</strong> Kat Chang 帶領導讀，這本書是許多大專院校營養相關科系愛用的入門經典教材"
            if old_str in body:
                body = body.replace(old_str, new_str, 1)
        post["body"] = body

with open(posts_file, "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)
    f.write("\n")

print("[OK] All 12 blog articles successfully enriched with keywords!")
