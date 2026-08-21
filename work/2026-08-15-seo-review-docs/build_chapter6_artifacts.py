# -*- coding: utf-8 -*-
import sys, os, json, re, html
from pathlib import Path

sys.stdout.reconfigure(encoding='utf-8')

ROOT_REPO = Path(r"d:\@Codex\594katchang-source.github.io-main")
BASE = ROOT_REPO / "work" / "2026-08-21-seo-growth-strategy"
SOURCE_DIR = BASE / "source"
OUTPUT_DIR = BASE / "output"
REVIEW_DOCS_DIR = ROOT_REPO / "work" / "2026-08-15-seo-review-docs"

sys.path.insert(0, str(REVIEW_DOCS_DIR))
from build_review_docs import build_doc

body = r"""<p><strong>本篇整理書籍：</strong>《Nutrition Concepts &amp; Controversies》第 17 版<br><strong>本篇章節：</strong>第六章, The Proteins and Amino Acids（蛋白質與胺基酸：組織修復、肌力維持與飲食選擇）<br><strong>文章性質：</strong>章節整理發文，將原章節概念轉成台灣讀者可使用的蛋白質與肌力維持判讀方法。<br><strong>省時版本：</strong>蛋白質是構成人體肌肉、酵素、荷爾蒙、抗體與器官組織的關鍵基石。攝取重點不在於盲目狂喝乳清蛋白或大魚大肉，而在於「總量足夠、三餐均勻、優質來源、兼顧消化吸收與熱量平衡」。中高齡長輩為預防肌少症，每公斤體重建議攝取 1.0～1.2 公克以上蛋白質；健康成年人基本需求約為 0.8～1.0 公克/公斤。若有慢性腎臟病（CKD）、急性肝腎疾病、痛風急性發作或特殊代謝限制者，調整蛋白質前必須經醫師與營養師專業評估。</p>

<h2>蛋白質怎麼吃才能長肌肉、防肌少？先回答四個核心問題</h2>
<p>在健身增肌與高齡防衰的討論中，「蛋白質」常被過度簡化為「多吃肉」或「狂補蛋白粉」。第六章為我們建立了一套清晰的生理與飲食判讀邏輯：從胺基酸結構、人體蛋白質合成機制、消化吸收限制，一路延伸到餐桌上的食物品質與每日分配。唯有搞懂這四個問題，才能讓吃進去的蛋白質真正轉化為身體的力量。</p>
<table><thead><tr><th>關鍵問題</th><th>生理與營養判斷方向</th><th>具體生活落實做法</th></tr></thead><tbody><tr><td>每天到底需要吃多少？</td><td>依年齡、體重、活動量、生理狀態與腎功能計算克數</td><td>健康成人 0.8~1.0 g/kg；銀髮增肌 1.0~1.2+ g/kg</td></tr><tr><td>蛋白質是哪一種品質？</td><td>看必需胺基酸完整度（PDCAAS/DIAAS）與消化率</td><td>動物性蛋白質利用率高，植物性採互補搭配（豆+穀）</td></tr><tr><td>三餐是怎麼分配的？</td><td>單餐刺激肌肉蛋白質合成（MPS）有上限（約 20-30g）</td><td>避免集中在晚餐暴食，落實「早中晚三餐平均分配」</td></tr><tr><td>熱量與醣類吃夠了嗎？</td><td>熱量不足時，蛋白質會被拿去燃燒當作熱量耗損</td><td>維持適足醣類與油脂，發揮蛋白質保留效應（Protein-sparing）</td></tr></tbody></table>
<p>蛋白質是由 20 種胺基酸串聯而成，其中 9 種是人體無法自行合成、必須由食物提供的「必需胺基酸（Essential Amino Acids, EAA）」。單一高劑量補充單種胺基酸（如高劑量精胺酸或支鏈胺基酸 BCAA 膠囊）往往會競爭腸道吸收載體，反而不如從完整食物中攝取均衡的蛋白質來源。</p>

<h2>胺基酸結構、胜肽鍵與蛋白質的八大生理功能</h2>
<p>蛋白質在人體內絕非只有「肌肉」一項功能。從維持生命的酵素催化、免疫防護到酸鹼平衡，幾乎所有生理機能都離不開蛋白質的參與。若長期攝取不足，身體將被迫分解自身肌肉與器官組織以維持基本運作。</p>
<table><thead><tr><th>主要功能</th><th>生理機制說明</th><th>生活與健康意義</th></tr></thead><tbody><tr><td>身體結構建構</td><td>膠原蛋白、角蛋白、肌纖維建構肌肉、骨骼、皮膚與結締組織</td><td>傷口癒合、骨質強度、皮膚彈性與肌力維持</td></tr><tr><td>酵素催化反應</td><td>體內數千種化學反應（消化、能量代謝、DNA複製）皆由蛋白質酵素執行</td><td>代謝運作流暢、消化吸收功能正常</td></tr><tr><td>荷爾蒙調節</td><td>胰島素、昇糖素、甲狀腺素相關分子調節生理訊號</td><td>血糖穩定、代謝率調節與食慾控制</td></tr><tr><td>免疫抗體防護</td><td>免疫球蛋白（Antibodies）專一性結合病原體進行防禦</td><td>免疫力健全、降低感染與重症風險</td></tr><tr><td>體液與滲透壓平衡</td><td>血漿白蛋白（Albumin）維持血管內膠體滲透壓，防止水分滲出</td><td>蛋白質嚴重不足時會出現下肢水腫（如腹水、浮腫）</td></tr><tr><td>酸鹼緩衝平衡</td><td>蛋白質帶有正負電荷，能結合或釋放氫離子維持血液 pH 7.35-7.45</td><td>防止體液過酸或過鹼，維持生命穩定</td></tr><tr><td>物質運輸載體</td><td>血紅素運輸氧氣、脂蛋白運輸脂質、細胞膜通道運輸礦物質</td><td>全身氧氣供應、營養素運送與細胞膜訊號傳遞</td></tr><tr><td>能量供應備援</td><td>在醣類與脂肪極度匱乏或過量攝取時，脫去胺基轉化為葡萄糖或熱量</td><td>每公克提供 4 大卡，但燃燒蛋白質作為熱量極不經濟</td></tr></tbody></table>
<p>了解蛋白質的多功能性後，就能明白為何高齡長輩若長期蛋白質不足，最先出現的往往不只是體重減輕，還伴隨著走路變慢、免疫力低下、傷口不易癒合以及下肢水腫等全身性衰弱表徵。</p>

<h2>動物性 vs 植物性蛋白質：品質、消化率與「蛋白質互補法」</h2>
<p>評估蛋白質好不好，不能只看包裝上的「克數」，還要看「胺基酸評分」與「人體真消化率」。動物性蛋白質（肉、魚、蛋、奶）通常為完全蛋白質，含有足量且比例均衡的 9 種必需胺基酸；多數植物性蛋白質（黃豆除外）則可能缺乏某一種必需胺基酸（稱為第一限制胺基酸，如穀類缺離胺酸、豆類缺甲硫胺酸）。</p>
<table><thead><tr><th>食物類別</th><th>優勢與特色</th><th>限制胺基酸與注意事項</th><th>優質代表食物</th></tr></thead><tbody><tr><td>黃豆與豆製品</td><td>植物界少見的完全蛋白質，無膽固醇且富含大豆異黃酮</td><td>消化率略低於動物性，加工豆皮/油豆腐可能含高油</td><td>無糖豆漿、嫩豆腐、傳統板豆腐、毛豆、天貝</td></tr><tr><td>魚類與海鮮</td><td>富含優質蛋白與 Omega-3 脂肪酸，肉質細軟易吞嚥</td><td>需注意大型掠食魚類之重金屬汞累積風險</td><td>鯖魚、秋刀魚、鮭魚、鱸魚、文蛤、蝦仁</td></tr><tr><td>家禽與蛋類</td><td>雞蛋為生物價極高之完美蛋白；雞胸肉高蛋白低脂肪</td><td>烹調避免過度油炸與高溫焦化</td><td>雞蛋、雞胸肉、去皮雞腿、里肌肉</td></tr><tr><td>乳品類</td><td>富含乳清蛋白、酪蛋白與鈣質，有助骨質與肌肉合成</td><td>乳糖不耐者可選擇無乳糖鮮乳、優格或硬質起司</td><td>低脂鮮乳、無糖優格、希臘優格、切達起司</td></tr><tr><td>全穀雜糧與堅果</td><td>提供植物蛋白、膳食纖維、礦物質與健康油脂</td><td>為不完全蛋白（缺離胺酸），需與豆類搭配互補</td><td>燕麥、藜麥、糙米、黑豆、核桃、南瓜子</td></tr></tbody></table>
<p>素食者完全不用擔心長不出肌肉！透過經典的「蛋白質互補法（Protein Complementation）」，例如「黃豆飯（豆類補穀類之離胺酸）+ 糙米（穀類補豆類之甲硫胺酸）」或「全麥麵包夾花生醬」，在同一天內攝取多樣化植物來源，就能輕鬆獲得完整均衡的必需胺基酸。</p>

<h2>不同年齡與族群每日蛋白質需求計算指南</h2>
<p>人體的蛋白質需求並非一成不變，而是取決於年齡、肌肉量、活動型態與生理壓力。台灣衛福部國健署第八版 DRI 與國際高齡醫學權威指引（PROT-AGE Study Group / ESPEN）對不同族群給出了明確建議：</p>
<table><thead><tr><th>族群類別</th><th>建議攝取量 (g/kg/day)</th><th>60公斤體重每日總量</th><th>核心營養目標與臨床考量</th></tr></thead><tbody><tr><td>健康久坐成年人</td><td>0.8 ～ 1.0 g/kg</td><td>約 48 ～ 60 公克</td><td>維持氮平衡與日常細胞組織新陳代謝</td></tr><tr><td>規律耐力運動員</td><td>1.2 ～ 1.4 g/kg</td><td>約 72 ～ 84 公克</td><td>修復微損傷肌纖維，補充醣原合成輔助</td></tr><tr><td>肌力重訓與增肌族</td><td>1.6 ～ 2.2 g/kg</td><td>約 96 ～ 132 公克</td><td>最大化刺激肌肉蛋白質合成（MPS）</td></tr><tr><td>65歲以上健康長輩</td><td>1.0 ～ 1.2+ g/kg</td><td>約 60 ～ 75 公克</td><td>克服高齡「同化阻抗（Anabolic Resistance）」，預防肌少症</td></tr><tr><td>高齡急性/慢性發炎患者</td><td>1.2 ～ 1.5 g/kg</td><td>約 72 ～ 90 公克</td><td>對抗疾病消耗、維持免疫力與體力（需無嚴重腎病）</td></tr><tr><td>慢性腎臟病 (CKD 3-5期未洗腎)</td><td>0.6 ～ 0.8 g/kg (低蛋白)</td><td>約 36 ～ 48 公克</td><td>減輕腎臟含氮廢物過濾負擔，延緩腎功能惡化（遵醫囑）</td></tr></tbody></table>
<p>計算出每日總克數後，關鍵在於「如何換算成餐桌上的食物」：在台灣飲食代換中，一份「高生物價蛋白質」約含 7 公克純蛋白質（例如：雞蛋 1 顆、無糖豆漿 190ml、傳統豆腐 3 格約 80g、肉類/魚類生重約 35g 約掌心 1/3 大小）。一名 60 公斤的長輩每天需要 60-72 公克蛋白質，約等於每天需要攝取 8～10 份優質蛋白質食物。</p>

<h2>高齡防肌少三絕招：總量足、分散吃、補充白胺酸（Leucine）</h2>
<p>許多年長者常有「年紀大了要吃清淡、不要吃太多肉」的迷思，導致早餐只吃稀飯配醬菜、午餐吃陽春麵，所有蛋白質全擠在晚餐吃一條魚。這種吃法即使總量勉強達標，也無法有效刺激肌肉生長！</p>
<table><thead><tr><th>防肌少關鍵機制</th><th>科學原理與醫學證據</th><th>餐桌實戰指引</th></tr></thead><tbody><tr><td>絕招一：三餐平均分配</td><td>高齡者肌肉合成門檻高，每餐需達到 20-30g 蛋白質才能啟動肌肉合成開關</td><td>早餐：蛋+無糖豆漿；午餐：去皮雞腿+豆腐；晚餐：蒸魚+毛豆</td></tr><tr><td>絕招二：鎖定白胺酸 (Leucine)</td><td>白胺酸是刺激 mTOR 肌肉合成途徑的最關鍵必需胺基酸（觸發閾值約 2.5-3g）</td><td>優先選擇黃豆、黑豆、毛豆、鮭魚、雞肉、牛肉與乳清/酪蛋白</td></tr><tr><td>絕招三：搭配阻力抗阻運動</td><td>「營養 + 阻力運動」是逆轉肌少症的黃金組合，單靠吃無法長出強健肌力</td><td>每週進行 2-3 次彈力帶、深蹲、快走或啞鈴阻力訓練</td></tr></tbody></table>
<p>對於牙口退化或咀嚼吞嚥功能下降的長者，千萬不要直接減少蛋白質，而應善用「烹調軟化技巧」：選擇質地細軟的鱸魚、蒸蛋、鮮奶酪、嫩豆腐、毛豆泥，或透過絞肉加豆腐做成軟質肉丸，確保營養與吞嚥安全兼得。</p>

<h2>市售蛋白粉與胺基酸補充品大解密：乳清、大豆蛋白、BCAA 與膠原蛋白</h2>
<p>走進藥妝店與健身房，各式各樣的蛋白質補充品琳瑯滿目。到底誰才真正需要補充？不同成分又有何差異？</p>
<table><thead><tr><th>補充品種類</th><th>主要成分與吸收特性</th><th>最適合的使用對象</th><th>營養師的選購提醒</th></tr></thead><tbody><tr><td>濃縮/分離乳清蛋白 (Whey)</td><td>牛奶提煉，消化吸收速度極快，富含支鏈胺基酸與白胺酸</td><td>運動後即時修復、牙口不佳長輩、術後食慾不振者</td><td>乳糖不耐者宜選「分離乳清（Isolate）」；注意添加糖與香料</td></tr><tr><td>大豆分離蛋白 (Soy Protein)</td><td>純植物萃取完全蛋白，無乳糖、無膽固醇</td><td>純素食者、乳品過敏者、需要植物性營養補充者</td><td>吸收速率適中，可與豆漿或燕麥奶搭配飲用</td></tr><tr><td>支鏈胺基酸 (BCAA)</td><td>包含白胺酸、異白胺酸與纈胺酸三種胺基酸</td><td>高強度運動員、無法攝取足量完整蛋白質之特定族群</td><td>若日常總蛋白質已吃足，額外補充 BCAA 效益有限</td></tr><tr><td>膠原蛋白 (Collagen)</td><td>水解胜肽分子，富含甘胺酸、脯胺酸，缺乏色胺酸（不完全蛋白）</td><td>追求皮膚彈性、關節保養輔助者</td><td>不能當作「主要增肌蛋白質」來源，需搭配維生素 C 協同作用</td></tr></tbody></table>
<p>天然食物永遠是蛋白質的首選，因為原型食物同時帶來了鋅、鐵、維生素 B 群、鈣與健康脂質等協同營養素。補充品定位為「便利輔助工具」，適合在外食蛋白質嚴重不足、運動後不便備餐或長輩食量極小時適度補充。</p>

<h2>外食與超商增肌減脂蛋白質採買實戰攻略</h2>
<p>上班族與外食族最常抱怨「外食很難吃到優質蛋白質」。事實上，只要掌握超商與便當店的選食原則，就能輕鬆達標：</p>
<table><thead><tr><th>常見外食情境</th><th>常見蛋白質地雷（高油、低蛋白）</th><th>營養師推薦的高效益優質組合</th></tr></thead><tbody><tr><td>便利超商 (7-11 / 全家)</td><td>熱狗、包子、炸雞塊、菠蘿麵包</td><td>茶葉蛋 2 顆 + 無糖濃豆漿 + 舒肥雞胸肉 / 烤地瓜</td></tr><tr><td>傳統便當自助餐店</td><td>炸排骨、炸雞排、香腸、炸豆腐皮、三層肉</td><td>滷雞腿（去皮）/ 烤鯖魚 / 蒸魚 + 滷蛋 + 炒毛豆 / 豆腐</td></tr><tr><td>中式麵店小吃攤</td><td>肉燥乾麵（油多肉少）、貢丸湯、炸油豆腐</td><td>陽春麵加燙青菜 + 切豆干海帶 + 嘴邊肉 / 肝連肉 + 燙鮮蚵</td></tr><tr><td>火鍋店聚餐</td><td>炸豆皮、百頁豆腐、貢丸、五花牛/豬、沙茶醬</td><td>低脂板腱牛/雞肉片/鮮魚片 + 生豆包 + 嫩豆腐 + 雞蛋 + 和風醬</td></tr><tr><td>早餐店外食</td><td>鐵板麵加熱狗、培根蛋餅、含糖大冰奶</td><td>里肌肉蛋吐司（不抹沙拉醬）+ 無糖豆漿 / 鮮奶</td></tr></tbody></table>
<p>避開「假豆腐（百頁豆腐脂肪高達近 50%）」與「加工肉品（香腸、培根、火腿含高鈉與防腐劑）」，選擇看得見原型紋理的豆、魚、蛋、肉類，就能在享受美食的同時維持精實體態。</p>

<h2>七日蛋白質與肌力練習表：打造永續的增肌餐盤</h2>
<p>這份練習旨在幫助您建立終生受用的蛋白質攝取習慣。每天落實一個微小改變，一週後您就能精準掌握自身蛋白質攝取量與活力狀態。</p>
<table><thead><tr><th>練習週期</th><th>每日執行任務</th><th>自我檢核與達標標準</th></tr></thead><tbody><tr><td>第 1 日：盤點日常總量</td><td>記錄三餐與點心所有含蛋白質食物，計算一日總公克數</td><td>比對自身體重需求，確認總量是否有達到 1.0~1.2 g/kg</td></tr><tr><td>第 2 日：搶救貧乏早餐</td><td>確保早餐至少含有 20 公克優質蛋白質</td><td>落實「雞蛋 1 顆 + 無糖豆漿 1 杯（或低脂鮮乳）」</td></tr><tr><td>第 3 日：嘗試全植物蛋白餐</td><td>安排一餐以「黃豆/黑豆 + 毛豆 + 豆腐 + 糙米」為主力</td><td>體驗植物性蛋白質的清爽飽足感與高纖腸道舒適度</td></tr><tr><td>第 4 日：辨識假健康地雷</td><td>檢視日常飲食，揪出百頁豆腐、素肉加工品與高油炸麵衣</td><td>將加工品替換為傳統板豆腐、生豆包或烤魚</td></tr><tr><td>第 5 日：蛋白質三餐均分</td><td>將一日所需蛋白質平均分配於早、午、晚三餐</td><td>每餐蛋白質份量皆維持在 20～30 公克左右</td></tr><tr><td>第 6 日：結合阻力肌力訓練</td><td>在餐後進行 20 分鐘居家深蹲、靠牆靜蹲或彈力帶運動</td><td>感受肌肉微酸張力，促進胺基酸進入肌肉組織合成</td></tr><tr><td>第 7 日：建立長期採買清單</td><td>整理出最適合個人預算與口味的 5 大長青蛋白質食材</td><td>完成每週固定採買清單（如雞蛋、豆漿、鯖魚、豆腐、雞胸）</td></tr></tbody></table>

<h2>蛋白質飲食常見八大迷思與錯誤觀念</h2>
<table><thead><tr><th>常見迷思</th><th>盲點與潛在風險剖析</th><th>科學實證與正確修正做法</th></tr></thead><tbody><tr><td>迷思一：高蛋白飲食一定會傷腎</td><td>健康腎臟具有強大代謝適應力，無研究顯示正常高蛋白會損害正常腎臟</td><td>健康人多喝水即可；已有腎病者（CKD）則需嚴格遵從低蛋白飲食</td></tr><tr><td>迷思二：吃肉越多肌肉就長越大</td><td>單次肌肉合成有上限，多餘蛋白質只會轉化為熱量脂肪堆積或排出</td><td>搭配抗阻運動，並將蛋白質平均分配於三餐攝取</td></tr><tr><td>迷思三：百頁豆腐是優質減肥食品</td><td>百頁豆腐主要成分為大豆蛋白、沙拉油與修飾澱粉，油脂熱量極高</td><td>改選傳統板豆腐、嫩豆腐、無糖豆漿或天然毛豆</td></tr><tr><td>迷思四：素食者蛋白質一定吃不夠</td><td>只要懂得黃豆製品與全穀雜糧互補，素食完全能達到足量完全蛋白</td><td>每天攝取足夠天貝、毛豆、黑豆、豆腐與糙米藜麥</td></tr><tr><td>迷思五：喝大骨湯可以補蛋白質和鈣</td><td>大骨湯溶出的多為動物油脂與微量重金屬，蛋白質與鈣質極低</td><td>喝大骨湯不如直接吃肉、喝鮮奶、吃小魚乾與豆腐</td></tr><tr><td>迷思六：蛋白質只要晚餐一次吃夠就好</td><td>單餐超過 40g 蛋白質利用率遞減，無法彌補早午餐的肌肉分解狀態</td><td>落實早、中、晚三餐均勻分配（每餐 20-30g）</td></tr><tr><td>迷思七：膠原蛋白可以取代乳清增肌</td><td>膠原蛋白缺少必需胺基酸色胺酸，生物價低，無法有效刺激肌肉生長</td><td>增肌應以乳清、大豆蛋白、肉類、蛋奶為主；膠原蛋白僅作輔助</td></tr><tr><td>迷思八：老人家清淡飲食就是要少吃肉</td><td>高齡者吸收率下降且肌肉流失加速，少吃肉反而大幅增加肌少衰弱風險</td><td>質地細軟化（蒸蛋、鮮魚、豆腐、絞肉），維持高蛋白質攝取</td></tr></tbody></table>

<h2>Kat Chang 營養師的判讀</h2>
<p>從營養生理與臨床衛教的視角來看，我認為第六章傳遞的最核心精神是：<strong>「蛋白質是維持生命尊嚴與生活品質的基石，關鍵在於聰明選擇與均勻分配。」</strong></p>
<p>現代人面臨兩極化的蛋白質挑戰：年輕外食族常把高脂炸雞、加工熱狗當蛋白質，吃進過多飽和脂肪與鈉；而中高齡長輩卻因為害怕膽固醇或牙口退化，陷入極端清淡的陷阱，導致肌少症與衰弱悄悄上身。真正的實證營養學，不是教大家極端節食或狂吞補品，而是回歸日常餐桌——用一碗毛豆糙米飯、一條清蒸鱸魚、一顆水煮蛋與一杯豆漿，把優質胺基酸穩穩地送進細胞裡，守護一生的活動力與健康。</p>

<h2>腎臟病與特殊族群安全段落：先確認腎功能、代謝與用藥，再調整蛋白質</h2>
<p>本文內容旨在提供健康成年人與銀髮族建立實證蛋白質飲食原則。若您或家人屬於以下特殊健康狀況，在進行任何高蛋白飲食或大幅增加蛋白質攝取前，<strong>務必先諮詢主治醫師與臨床營養師進行個別化飲食計畫評估</strong>：</p>
<ol>
<li><strong>慢性腎臟病患者（CKD 第 3～5 期未洗腎者）</strong>：腎功能受損時，過多蛋白質代謝產生的含氮廢物（尿素氮 BUN）會加重腎臟負擔，加速腎功能惡化。此類患者必須遵從嚴格的「低蛋白飲食（0.6~0.8 g/kg/day）」，並優先選擇高生物價優質蛋白。</li>
<li><strong>洗腎（血液透析 / 腹膜透析）患者</strong>：洗腎過程會流失大量胺基酸，反而需要轉為「高蛋白飲食（1.2~1.4 g/kg/day）」，且需嚴格監控磷與鉀的攝取。</li>
<li><strong>肝硬化與肝昏迷（肝性腦病變）風險者</strong>：需由醫療團隊動態評估蛋白質耐受度與支鏈胺基酸（BCAA）之調配。</li>
<li><strong>急性痛風發作期患者</strong>：需避開高普林之濃肉汁、動物內臟與部分海鮮，以蛋類、乳品與適量豆製品為主要蛋白質來源，並補充足量水分。</li>
</ol>
<p>若日常出現泡泡尿持續不散、下肢嚴重水腫、食慾極度減退、不明原因疲憊或肌酸酐數值異常，請立即前往醫療院所腎臟科進行血液與尿液檢查。文章資訊不能取代正式醫療診斷與處方治療。</p>

<p>延伸閱讀：<a href="https://594katchang-source.github.io/blog/post.html?id=2026-08-13-nutrition-concepts-controversies-17e-guide">全書導讀</a>、<a href="https://594katchang-source.github.io/blog/post.html?id=2026-08-14-food-choices-human-health-guide">第一章食物選擇</a>、<a href="https://594katchang-source.github.io/blog/post.html?id=2026-08-15-nutrition-tools-standards-guidelines">第二章營養工具與標準</a>、<a href="https://594katchang-source.github.io/blog/post.html?id=2026-08-17-carbohydrates-food-guide">第四章碳水化合物與纖維</a>、<a href="https://594katchang-source.github.io/teach/nutritionranking/">NutriRank 食品營養排行榜</a>、<a href="https://594katchang-source.github.io/about.html">作者簡介</a>、<a href="https://594katchang-source.github.io/class.html">授課主題</a>。</p>

<h2>FAQ：蛋白質、肌少症與胺基酸常見問題</h2>
<h3>蛋白質吃太多會不會傷腎？</h3>
<p>對於腎功能正常的健康人，目前醫學研究並無證據顯示正常高蛋白質飲食（1.2~2.0 g/kg）會損害健康腎臟，只要補充足夠水分即可。但對於已有慢性腎臟病（CKD）者，過量蛋白質會加重代謝負擔，必須遵醫囑控制攝取量。</p>
<h3>植物性蛋白質（如黃豆、豆腐）增肌效果比肉類差嗎？</h3>
<p>不會。黃豆、黑豆、毛豆及其製品屬於完全蛋白質，消化利用率極高。只要搭配全穀雜糧（如黃豆飯、糙米）達到胺基酸互補，並確保一日總蛋白質與熱量達標，植物性蛋白質同樣能達到優異的增肌與維持肌力效果。</p>
<h3>長輩牙齒不好咬不動肉，該怎麼補足蛋白質？</h3>
<p>可善用食材軟化技巧：選擇質地軟嫩的清蒸鱸魚、蒸蛋、無糖豆漿、嫩豆腐、鮮奶、毛豆泥，或將肉類絞碎混合豆腐做成軟質肉丸。亦可在營養師指導下適度補充無添加糖之優質大豆蛋白或乳清蛋白飲品。</p>
<h3>喝大骨湯可以補蛋白質和鈣質嗎？</h3>
<p>無法。大骨熬湯溶出的主要為脂肪與極微量骨髓，蛋白質與鈣質含量極低，反而可能攝取過多飽和脂肪與微量重金屬。要補充蛋白質與鈣質，直接吃肉、喝鮮奶、吃小魚乾與傳統板豆腐才是真正有效的做法。</p>
<h3>運動後到底要不要立刻喝乳清蛋白？</h3>
<p>運動後 30-60 分鐘內補充「蛋白質（約 20-25g）+ 碳水化合物」有助於加速肌肉修復與肝醣回補。若能方便吃一頓包含正餐（如地瓜 + 茶葉蛋 + 豆漿），效果與蛋白粉相同；蛋白粉是外食不便時的高效便利選擇。</p>"""

text = re.sub(r"<script[\s\S]*?</script>", " ", body, flags=re.I)
text = re.sub(r"<style[\s\S]*?</style>", " ", text, flags=re.I)
text = re.sub(r"<[^>]+>", " ", text)
text = html.unescape(text)
visible_text_clean = re.sub(r"\s+", " ", text).strip()
char_count = len(visible_text_clean)
word_count = len(visible_text_clean.split())

data = {
    "reviewTitle": "第六章待審 SEO 草稿",
    "seoTitle": "蛋白質怎麼吃才能長肌肉、防肌少？從胺基酸、食物選擇到一日攝取計算的營養師判讀",
    "targetTerms": ["蛋白質怎麼吃", "蛋白質攝取量", "肌少症飲食", "植物性蛋白質", "乳清蛋白", "胺基酸"],
    "relatedTerms": ["白胺酸", "必需胺基酸", "蛋白質互補", "高齡增肌", "腎臟病蛋白質", "超商蛋白質", "外食增肌", "BCAA"],
    "searchIntent": "讀者想清楚理解不同年齡與生活型態下的每日蛋白質需求克數、優質蛋白質食物挑選、素食互補法、高齡防肌少技巧，並排除傷腎迷思與外食盲點。",
    "summary": "蛋白質是維持肌力、免疫與代謝的基石。本文依據最新實證營養學與高齡指引，深度拆解蛋白質需求計算、植物與動物蛋白品質、防肌少三絕招、外食增肌攻略與腎臟病安全限制，助您聰明吃出活力好體質。",
    "opening": "蛋白質是身體建造修復的關鍵基石，真正需要掌握的是「總量計算、三餐均勻、優質來源、兼顧熱量」。本文依《Nutrition Concepts & Controversies》第 17 版第六章，整理胺基酸功能、動物與植物蛋白互補、高齡防肌少白胺酸、市售補充品迷思與腎臟病限制。",
    "articleTitle": "蛋白質怎麼吃才能長肌肉、防肌少？從胺基酸、食物選擇到一日攝取計算",
    "bodyHtml": body,
    "seoDescription": "蛋白質怎麼吃才正確？搞懂每日蛋白質攝取量計算公式、植物性蛋白互補法、高齡防肌少三絕招與外食超商增肌攻略。由食品營養博士張雁雲（Kat Chang 凱特營養師）實證解析，守護肌肉與健康活力！",
    "category": "書籍連載",
    "tags": ["蛋白質", "肌少症", "胺基酸", "高齡營養", "增肌減脂", "植物性蛋白", "乳清蛋白", "Nutrition Concepts & Controversies"],
    "slug": "2026-08-21-proteins-amino-acids-sarcopenia-guide",
    "canonical": "https://594katchang-source.github.io/blog/post.html?id=2026-08-21-proteins-amino-acids-sarcopenia-guide",
    "internalLinks": [
        ["全書導讀", "https://594katchang-source.github.io/blog/post.html?id=2026-08-13-nutrition-concepts-controversies-17e-guide"],
        ["第一章食物選擇", "https://594katchang-source.github.io/blog/post.html?id=2026-08-14-food-choices-human-health-guide"],
        ["第二章營養工具與標準", "https://594katchang-source.github.io/blog/post.html?id=2026-08-15-nutrition-tools-standards-guidelines"],
        ["第四章碳水化合物與纖維", "https://594katchang-source.github.io/blog/post.html?id=2026-08-17-carbohydrates-food-guide"],
        ["NutriRank 食品營養排行榜", "https://594katchang-source.github.io/teach/nutritionranking/"],
        ["作者簡介", "https://594katchang-source.github.io/about.html"],
        ["授課主題", "https://594katchang-source.github.io/class.html"]
    ],
    "faq": [
        "蛋白質吃太多會不會傷腎？",
        "植物性蛋白質（如黃豆、豆腐）增肌效果比肉類差嗎？",
        "長輩牙齒不好咬不動肉，該怎麼補足蛋白質？",
        "喝大骨湯可以補蛋白質和鈣質嗎？",
        "運動後到底要不要立刻喝乳清蛋白？"
    ],
    "faqEntities": [
        {
            "question": "蛋白質吃太多會不會傷腎？",
            "answer": "對於腎功能正常的健康人，目前醫學研究並無證據顯示正常高蛋白質飲食（1.2~2.0 g/kg）會損害健康腎臟，只要補充足夠水分即可。但對於已有慢性腎臟病（CKD）者，過量蛋白質會加重代謝負擔，必須遵醫囑控制攝取量。"
        },
        {
            "question": "植物性蛋白質（如黃豆、豆腐）增肌效果比肉類差嗎？",
            "answer": "不會。黃豆、黑豆、毛豆及其製品屬於完全蛋白質，消化利用率極高。只要搭配全穀雜糧（如黃豆飯、糙米）達到胺基酸互補，並確保一日總蛋白質與熱量達標，植物性蛋白質同樣能達到優異的增肌與維持肌力效果。"
        },
        {
            "question": "長輩牙齒不好咬不動肉，該怎麼補足蛋白質？",
            "answer": "可善用食材軟化技巧：選擇質地軟嫩的清蒸鱸魚、蒸蛋、無糖豆漿、嫩豆腐、鮮奶、毛豆泥，或將肉類絞碎混合豆腐做成軟質肉丸。亦可在營養師指導下適度補充無添加糖之優質大豆蛋白或乳清蛋白飲品。"
        },
        {
            "question": "喝大骨湯可以補蛋白質和鈣質嗎？",
            "answer": "無法。大骨熬湯溶出的主要為脂肪與極微量骨髓，蛋白質與鈣質含量極低，反而可能攝取過多飽和脂肪與微量重金屬。要補充蛋白質與鈣質，直接吃肉、喝鮮奶、吃小魚乾與傳統板豆腐才是真正有效的做法。"
        },
        {
            "question": "運動後到底要不要立刻喝乳清蛋白？",
            "answer": "運動後 30-60 分鐘內補充「蛋白質（約 20-25g）+ 碳水化合物」有助於加速肌肉修復與肝醣回補。若能方便吃一頓包含正餐（如地瓜 + 茶葉蛋 + 豆漿），效果與蛋白粉相同；蛋白粉是外食不便時的高效便利選擇。"
        }
    ],
    "faqSchema": "建議公開正文完整呈現問題與答案後，使用 FAQPage 結構化資料，並和 BlogPosting 的 mainEntity 或 about 關係保持一致。FAQPage 只標記頁面上讀者看得到的問答。",
    "articleSchema": [
        "BlogPosting",
        "headline",
        "description",
        "author",
        "datePublished: 2026-08-21",
        "dateModified: 2026-08-21",
        "mainEntityOfPage",
        "image",
        "articleSection",
        "keywords",
        "about"
    ],
    "author": "張雁雲營養師，Kat Chang 凱特營養師，專長為高齡營養、疾病營養、精準營養與健康促進。",
    "sources": [
        ["第六章整理 DOCX", "D:/@Codex/書籍/2026-07-29-Nutrition-Concepts-Controversies-17e/output/chapter-06-proteins-amino-acids.docx", "第六章蛋白質、胺基酸、消化吸收、蛋白質品質與素食爭議核心概念"],
        ["第六章全文擷取檔", "D:/@Codex/書籍/2026-07-29-Nutrition-Concepts-Controversies-17e/process/chapter-06-source.txt", "PDF 第 212 至 251 頁、印刷頁第 188 至 227 頁的逐頁內容"],
        ["Cengage 第 17 版書籍頁", "https://www.cengage.com/c/nutrition-concepts-controversies-17e-sizer-whitney-wissmann/9798214450049/", "書籍版本、作者與章節背景核對"],
        ["衛福部國健署 DRI 第八版", "https://www.hpa.gov.tw/Pages/Detail.aspx?nodeid=4248&pid=12285", "國人蛋白質膳食營養素參考攝取量與各年齡層建議"],
        ["PROT-AGE Study Group 高齡蛋白質指引", "https://www.sciencedirect.com/science/article/pii/S1525861013003265", "高齡族群每日 1.0-1.2+ g/kg 蛋白質與肌少症預防指引"],
        ["ESPEN 高齡臨床營養指引", "https://www.clinicalnutritionjournal.com/article/S0261-5614(18)32432-4/fulltext", "歐洲臨床營養與代謝學會高齡營養與水合指引"],
        ["WHO 蛋白質與胺基酸需求技術報告", "https://www.who.int/publications/i/item/9241209356", "人體必需胺基酸需求量與蛋白質品質評估標準"],
        ["ISSN 運動蛋白質立場聲明", "https://jissn.biomedcentral.com/articles/10.1186/s12970-017-0177-8", "運動員與阻力訓練族群蛋白質攝取量與時機指引"]
    ],
    "originalClaims": [
        "把第六章的蛋白質生理與胺基酸結構轉成台灣長輩與外食族可執行的四問判讀法。",
        "結合 PROT-AGE 與 ESPEN 指引，明確指出高齡防肌少需達到 1.0~1.2+ g/kg 且三餐平均分配。",
        "用生活化餐桌食物拆解「蛋白質互補法」，破除素食長不出肌肉的迷思。",
        "建立七日增肌蛋白質練習表與外食超商採買攻略，提供具體克數與份量換算。",
        "嚴格標註慢性腎臟病（CKD 3-5 期）低蛋白飲食邊界，避免健康指引誤套用至腎病患者。"
    ],
    "pending": [
        "本稿供使用者人工審閱，尚未寫入 blog/posts.json，也未發布。",
        "正式發布前要以遠端 main 最新 SHA 做目標文章合併，並保留既有文章、圖片與 showOnHome 設定。",
        "發布後才可核對第六章公開 DOM、FAQPage、canonical、sitemap、站內連結、封面圖與 375px 版面。",
        "Search Console 尚未在本輪重新登入，本稿沒有曝光、點擊、點擊率、平均排名、熱門查詢或熱門頁面數據。",
        "本文提供一般營養教育，不能取代診斷、檢驗、藥物調整或個人化治療。"
    ],
    "wordCount": {
        "characters": char_count,
        "words": word_count
    },
    "sourcePageAudit": [
        "pdfPages: 212-251",
        "printedPages: 188-227",
        "pageMarkers: 40",
        "replacementCharacters: 0"
    ],
    "reviewDate": "2026-08-21",
    "authorBackground": "Kat Chang 凱特營養師，張雁雲營養師。專長為高齡營養、疾病營養、精準營養與健康促進。",
    "preset": "compact_reference_guide"
}

# 1. Save chapter-06-review.json
json_path = SOURCE_DIR / "chapter-06-review.json"
with open(json_path, "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)
print("Saved source/chapter-06-review.json")

# 2. Save chapter-06-review.html
html_page = f"""<!doctype html>
<html lang="zh-Hant">
<head>
<meta charset="utf-8">
<title>{data['seoTitle']}</title>
<meta name="description" content="{data['seoDescription']}">
<link rel="canonical" href="{data['canonical']}">
</head>
<body>
<article>
<h1>{data['articleTitle']}</h1>
{body}
</article>
</body>
</html>"""
html_path = SOURCE_DIR / "chapter-06-review.html"
with open(html_path, "w", encoding="utf-8") as f:
    f.write(html_page)
print("Saved source/chapter-06-review.html")

# 3. Save 04_chapter_06_proteins_amino_acids_seo_draft.md
sources_text = "\n".join([f"  - [{s[0]}]({s[1]}): {s[2]}" for s in data['sources']])
md_draft = f"""# {data['seoTitle']}

- **審閱日期**：{data['reviewDate']}
- **目標發布日期**：2026-08-21
- **文章分類**：{data['category']}
- **文章 Slug**：`{data['slug']}`
- **正文實際可見字數**：約 {char_count} 字
- **SEO 標題**：{data['seoTitle']}
- **SEO 描述**：{data['seoDescription']}
- **主要關鍵字**：{', '.join(data['targetTerms'])}
- **相關搜尋詞**：{', '.join(data['relatedTerms'])}
- **文章摘要**：{data['summary']}
- **權威來源支持**：
{sources_text}

---

# 正文內容（HTML 渲染預覽）

{body}
"""
with open(OUTPUT_DIR / "04_chapter_06_proteins_amino_acids_seo_draft.md", "w", encoding="utf-8") as f:
    f.write(md_draft)
print("Saved 04_chapter_06_proteins_amino_acids_seo_draft.md")

# 4. Generate Word docx
docx_out = OUTPUT_DIR / "chapter-06-proteins-amino-acids-seo-review.docx"
build_doc(data, docx_out)
print(f"Generated DOCX: {docx_out}")
print("=== Chapter 6 Suite Complete! ===")