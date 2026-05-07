import { initializeApp } from "https://www.gstatic.com/firebasejs/10.12.5/firebase-app.js";
import { getDatabase, ref, set, update, onValue, get, runTransaction, serverTimestamp } from "https://www.gstatic.com/firebasejs/10.12.5/firebase-database.js";

const DEFAULT_FIREBASE_CONFIG = {
  apiKey: "AIzaSyBFPjEXxNp5-UPqApClA1FaACD4UE6aRT0",
  authDomain: "realtime-database-2fcbb.firebaseapp.com",
  databaseURL: "https://realtime-database-2fcbb-default-rtdb.firebaseio.com",
  projectId: "realtime-database-2fcbb",
  storageBucket: "realtime-database-2fcbb.firebasestorage.app",
  messagingSenderId: "7723390214",
  appId: "1:7723390214:web:a227cd5d88b9f01274fa87"
};

const q = (text, options, answer, explain) => ({ text, options, answer, explain });
const banks = {
  classify: { label: "第一模式：食物分類", questions: [
    q("地瓜在食物代換表中主要屬於哪一類？", ["蔬菜類", "全穀雜糧類", "水果類", "豆魚蛋肉類"], 1, "地瓜富含澱粉，代換時歸全穀雜糧類。"),
    q("毛豆、黃豆、黑豆與豆腐、豆漿主要屬於哪一類？", ["豆魚蛋肉類", "水果類", "蔬菜類", "油脂堅果類"], 0, "黃豆、黑豆、毛豆及其製品是植物性蛋白質來源。"),
    q("南瓜代換時主要屬於哪一類？", ["蔬菜類", "全穀雜糧類", "乳品類", "水果類"], 1, "南瓜含澱粉較多，代換時常歸全穀雜糧類。"),
    q("一杯 240 毫升鮮奶主要歸在哪一類？", ["乳品類", "豆魚蛋肉類", "水果類", "油脂堅果類"], 0, "鮮奶、保久乳、無糖優格都屬乳品類。"),
    q("杏仁果、花生、腰果主要歸在哪一類？", ["水果類", "豆魚蛋肉類", "油脂與堅果種子類", "蔬菜類"], 2, "堅果種子含油脂，份量要控制。"),
    q("雞蛋、魚肉、雞肉共同屬於哪一類？", ["乳品類", "豆魚蛋肉類", "全穀雜糧類", "蔬菜類"], 1, "蛋、魚、海鮮、禽肉、畜肉都屬豆魚蛋肉類。"),
    q("紅豆、綠豆在代換概念中較接近哪一類？", ["乳品類", "全穀雜糧類", "豆魚蛋肉類", "油脂堅果類"], 1, "紅豆、綠豆澱粉比例較高，常歸全穀雜糧類。"),
    q("大番茄作為料理時常歸為哪一類？", ["蔬菜類", "水果類", "乳品類", "全穀雜糧類"], 0, "大番茄常作蔬菜類。"),
    q("馬鈴薯應該和哪一類食物互相代換？", ["水果", "乳品", "全穀雜糧", "豆魚蛋肉"], 2, "馬鈴薯富含澱粉。"),
    q("豆干、豆腐、無糖豆漿主要提供什麼？", ["蛋白質", "維生素 C", "單純油脂", "酒精"], 0, "黃豆製品是重要蛋白質來源。"),
    q("白飯、麵、吐司主要屬於哪一類？", ["全穀雜糧類", "蔬菜類", "乳品類", "水果類"], 0, "主食類食物主要提供醣類。"),
    q("玉米在食物代換時比較接近哪一類？", ["水果類", "全穀雜糧類", "豆魚蛋肉類", "乳品類"], 1, "玉米含澱粉，歸全穀雜糧類。"),
    q("芋頭、山藥、蓮藕代換時多歸在哪一類？", ["全穀雜糧類", "蔬菜類", "水果類", "油脂類"], 0, "根莖類中澱粉高者常歸全穀雜糧類。"),
    q("青江菜、菠菜、高麗菜主要屬於哪一類？", ["蔬菜類", "水果類", "全穀雜糧類", "乳品類"], 0, "這些都是常見蔬菜。"),
    q("蘋果、香蕉、芭樂主要屬於哪一類？", ["水果類", "蔬菜類", "乳品類", "豆魚蛋肉類"], 0, "水果類提供維生素、礦物質及醣類。"),
    q("起司若以乳製品角度代換，主要屬於哪一類？", ["乳品類", "水果類", "蔬菜類", "全穀雜糧類"], 0, "起司是乳製品，但脂肪含量也需留意。"),
    q("豬肉、牛肉、雞肉主要屬於哪一類？", ["豆魚蛋肉類", "全穀雜糧類", "水果類", "油脂類"], 0, "肉類提供蛋白質。"),
    q("鮭魚、虱目魚、蝦仁主要屬於哪一類？", ["豆魚蛋肉類", "乳品類", "蔬菜類", "水果類"], 0, "魚和海鮮都歸豆魚蛋肉類。"),
    q("酪梨在份量控制上常需要注意哪一類營養？", ["油脂", "酒精", "乳糖", "咖啡因"], 0, "酪梨脂肪含量較高。"),
    q("苦茶油、橄欖油、沙拉油主要屬於哪一類？", ["油脂類", "乳品類", "水果類", "豆魚蛋肉類"], 0, "烹調油屬油脂類。"),
    q("無糖優格通常歸在哪一類？", ["乳品類", "油脂類", "蔬菜類", "全穀雜糧類"], 0, "無糖優格由乳品製成。"),
    q("黑芝麻、葵瓜子、核桃主要歸在哪一類？", ["油脂與堅果種子類", "水果類", "乳品類", "蔬菜類"], 0, "種子與堅果油脂較高。"),
    q("米粉、冬粉、麵線多歸在哪一類？", ["全穀雜糧類", "蔬菜類", "水果類", "豆魚蛋肉類"], 0, "這些主成分多為澱粉。"),
    q("豌豆仁在代換時常比豌豆莢更接近哪一類？", ["全穀雜糧類", "乳品類", "水果類", "油脂類"], 0, "豌豆仁澱粉含量較高。"),
    q("菇類、海帶、木耳通常歸為哪一類？", ["蔬菜類", "乳品類", "全穀雜糧類", "水果類"], 0, "菇類、藻類、木耳常作蔬菜類。"),
    q("豆皮、豆包主要屬於哪一類？", ["豆魚蛋肉類", "水果類", "蔬菜類", "全穀雜糧類"], 0, "豆製品屬豆魚蛋肉類，但油脂量也要注意。"),
    q("果汁即使無加糖，主要仍應看作哪一類？", ["水果類", "蔬菜類", "豆魚蛋肉類", "乳品類"], 0, "果汁來自水果，但較不如完整水果有飽足感。"),
    q("花椰菜、甜椒、小黃瓜主要屬於哪一類？", ["蔬菜類", "水果類", "全穀雜糧類", "乳品類"], 0, "這些都是非澱粉蔬菜。"),
    q("饅頭、蘿蔔糕、飯糰主要屬於哪一類？", ["全穀雜糧類", "油脂類", "乳品類", "蔬菜類"], 0, "主成分多為米麵澱粉。"),
    q("培根、香腸雖然是肉品，分類上仍屬哪一類但應少吃？", ["豆魚蛋肉類", "水果類", "乳品類", "蔬菜類"], 0, "加工肉品屬豆魚蛋肉類，但鈉和脂肪常較高。")
  ]},
  portion: { label: "第二模式：我的餐盤份量", questions: [
    q("「每天早晚一杯奶」的一杯約是多少？", ["120 毫升", "190 毫升", "240 毫升", "500 毫升"], 2, "我的餐盤一杯乳品約 240 毫升。"),
    q("每餐水果建議大約是多少？", ["一個拳頭大", "一掌心", "一茶匙", "半個餐盤"], 0, "口訣是每餐水果拳頭大。"),
    q("蔬菜份量和水果相比，哪個較符合口訣？", ["菜比水果少一點", "菜比水果多一點", "不用吃菜", "只吃水果"], 1, "口訣是菜比水果多一點。"),
    q("飯和蔬菜的份量關係，哪個最接近？", ["飯跟蔬菜一樣多", "飯比菜多三倍", "完全不吃飯", "只有飯不用菜"], 0, "口訣是飯跟蔬菜一樣多。"),
    q("每餐豆魚蛋肉類大約是多少？", ["一掌心", "一茶匙", "兩大碗", "一整盤"], 0, "口訣是豆魚蛋肉一掌心。"),
    q("堅果種子每餐建議約是多少？", ["一茶匙", "一飯碗", "一拳頭", "半盤"], 0, "口訣是堅果種子一茶匙。"),
    q("切塊水果一份常用哪個方式估量？", ["標準碗八分滿", "一大鍋", "一茶匙", "一片起司"], 0, "切塊水果可用標準碗八分滿估一份。"),
    q("豆魚蛋肉類建議優先選擇哪一組？", ["加工肉品", "豆類、魚海鮮、蛋、禽畜肉", "培根熱狗", "肥肉"], 1, "少加工，優先豆類、魚類與海鮮。"),
    q("蔬菜一份熟菜大約是多少？", ["半碗", "三大碗", "一茶匙", "一杯奶"], 0, "熟蔬菜常以半碗估一份。"),
    q("堅果一天合計大約可以抓哪個概念？", ["約一湯匙", "約十碗", "完全不需要", "越多越好"], 0, "堅果健康但油脂高。"),
    q("我的餐盤中，蔬菜大約應占餐盤多少？", ["比四分之一多一些", "整盤都是飯", "只有一口", "完全不用"], 0, "蔬菜份量應比水果多，接近餐盤的一大部分。"),
    q("全穀雜糧每餐口訣是？", ["飯跟蔬菜一樣多", "飯比肉多十倍", "完全不吃飯", "飯只吃一茶匙"], 0, "我的餐盤強調飯跟蔬菜一樣多。"),
    q("一份水果若用奇異果估，大約可抓幾顆？", ["約 2 顆小型", "10 顆", "半顆米粒", "一整袋"], 0, "水果以一拳頭或一份量概念估算。"),
    q("一份水果若用香蕉估，較合理的是？", ["小型香蕉 1 根", "5 根", "只吃皮", "一茶匙"], 0, "一根小香蕉約可作一份水果估量。"),
    q("一份水果若用葡萄估，較接近哪個份量？", ["約 13 顆", "1 顆", "100 顆", "一湯鍋"], 0, "葡萄可用顆數協助估量。"),
    q("乳品一天建議幾次較符合口訣？", ["早晚各一次", "一週一次", "完全不用", "一次喝三公升"], 0, "口訣是每天早晚一杯奶。"),
    q("豆魚蛋肉一掌心，掌心大約不包含哪個部位？", ["整隻手臂", "手掌心", "手掌厚度", "手掌大小"], 0, "掌心法不是用整隻手臂估。"),
    q("如果餐盤上蔬菜很少，最適合怎麼調整？", ["增加一份青菜", "再加含糖飲料", "把水果全拿掉", "只吃肉"], 0, "蔬菜量通常要比水果多一些。"),
    q("堅果種子一茶匙約可想成什麼？", ["少量點綴", "整碗當主食", "越多越好", "取代所有蔬菜"], 0, "堅果油脂高，少量即可。"),
    q("一杯乳品約 240 毫升，最接近哪個容器？", ["一般馬克杯一杯", "水桶一桶", "一茶匙", "一飯粒"], 0, "一般杯裝約 240 毫升可作估量。"),
    q("外食便當若飯很多菜很少，較好的調整是？", ["飯少一點、菜多一點", "只喝湯", "再加炸物", "把菜丟掉"], 0, "讓飯和菜的比例更接近我的餐盤。"),
    q("一餐魚肉已吃一掌心，豆魚蛋肉類應如何處理？", ["大致足夠，不必無限加", "再吃十掌心", "完全不算", "改喝含糖飲料"], 0, "豆魚蛋肉以一掌心作估量。"),
    q("熟青菜半碗若不夠，可用哪個原則？", ["菜比水果多一點", "菜越少越好", "只吃水果", "只吃飯"], 0, "每餐蔬菜應比水果多。"),
    q("水果拳頭大比較適合何時使用？", ["估每餐水果量", "估烹調油", "估鹽巴", "估酒精"], 0, "水果可用拳頭大小估量。"),
    q("我的餐盤口訣中，白開水較好的角色是？", ["取代含糖飲料", "取代所有食物", "越甜越好", "只在生病喝"], 0, "日常飲水以白開水為佳。"),
    q("若早餐沒有乳品，可怎麼補足？", ["晚餐或點心補無糖乳品", "改喝含糖飲料", "不用管", "只吃炸物"], 0, "可用無糖乳品補足每日乳品。"),
    q("一份熟蔬菜半碗，生菜通常需要怎樣？", ["體積較大才接近", "一片就很多", "完全不能吃", "只能榨汁"], 0, "生菜含水多、體積蓬鬆，估量時通常體積較大。"),
    q("我的餐盤較鼓勵哪種主食選擇？", ["糙米、地瓜等全穀雜糧", "只吃糖果", "只喝奶茶", "完全不吃任何主食"], 0, "主食可優先選全穀雜糧。"),
    q("如果水果已吃一拳頭，接著最需要注意什麼？", ["不要把果汁當無限量", "再喝一大桶果汁", "完全不吃蔬菜", "只吃餅乾"], 0, "水果也有醣量，份量仍要掌握。"),
    q("餐盤中豆魚蛋肉的份量和蔬菜相比通常應？", ["約一掌心，不是最大區塊", "比蔬菜大很多", "完全沒有", "只剩加工肉"], 0, "豆魚蛋肉是重要蛋白質，但蔬菜也要足量。")
  ]},
  rainbow: { label: "第三模式：彩虹食物", questions: [
    q("紅色彩虹食物哪一組最適合？", ["小番茄、紅甜椒、西瓜", "白飯、白吐司", "牛奶、起司", "雞蛋、豆腐"], 0, "紅色蔬果常含茄紅素等植化素。"),
    q("哪一個橘黃色食物也常歸全穀雜糧類代換？", ["南瓜", "芭樂", "牛奶", "豆腐"], 0, "南瓜含澱粉，代換時歸全穀雜糧類。"),
    q("深綠色蔬菜哪一組最適合？", ["菠菜、地瓜葉、青江菜", "香蕉、芒果", "鮮奶、優格", "核桃、花生"], 0, "深綠色蔬菜是彩虹飲食重要來源。"),
    q("紫色全穀或蔬果哪一組較適合？", ["紫米、茄子、葡萄", "白飯、白麵條", "雞肉、魚肉", "牛奶、豆漿"], 0, "紫色食物也能進餐盤。"),
    q("想讓一餐更像彩虹，最好的做法是？", ["固定只吃一種顏色", "多選不同顏色", "完全不吃菜", "只喝含糖飲料"], 1, "彩虹飲食強調不同顏色輪流吃。"),
    q("白色或淺色食物中，哪個是蔬菜類？", ["白蘿蔔", "白吐司", "白飯", "奶粉"], 0, "白蘿蔔是蔬菜類。"),
    q("彩虹全穀雜糧哪一組較符合？", ["糙米、紫米、玉米、地瓜", "火腿、熱狗", "起司、鮮奶", "白開水、茶"], 0, "全穀雜糧也可以有顏色變化。"),
    q("為什麼不能只用顏色判斷食物類別？", ["同色食物可能分屬不同類別", "顏色淡一定不健康", "紅色都算水果", "綠色都算蔬菜"], 0, "分類仍要看主要營養特性。"),
    q("黃色水果的例子哪一個較適合？", ["木瓜", "豆腐", "白飯", "雞肉"], 0, "木瓜可作為橘黃色水果例子。"),
    q("綠色食物中，哪一個也是豆魚蛋肉類的豆類代表？", ["毛豆", "白吐司", "葡萄", "起司"], 0, "毛豆是綠色豆類食物，也是植物性蛋白質來源。"),
    q("橘色蔬菜哪一組最合適？", ["胡蘿蔔、南瓜、橘甜椒", "白飯、冬粉", "鮮奶、起司", "雞胸肉、魚肉"], 0, "橘黃色蔬菜可提供不同植化素。"),
    q("綠色水果哪一個較常見？", ["奇異果", "白飯", "豆腐", "雞蛋"], 0, "奇異果是綠色水果例子。"),
    q("紫色蔬菜哪一個最適合？", ["茄子", "白吐司", "牛奶", "豆漿"], 0, "茄子是紫色蔬菜。"),
    q("紅色全穀雜糧可想到哪一個？", ["紅藜", "白開水", "雞蛋", "鮮奶"], 0, "紅藜可作為彩色全穀雜糧例子。"),
    q("黑色或深色食物哪一組較像彩虹飲食的一部分？", ["黑木耳、黑豆、黑芝麻", "白糖、白開水", "奶油、糖霜", "熱狗、培根"], 0, "深色食物也能增加飲食多樣性。"),
    q("藍紫色水果哪一個最適合？", ["藍莓", "豆腐", "高麗菜", "白飯"], 0, "藍莓是藍紫色水果。"),
    q("黃色全穀雜糧哪一個較適合？", ["玉米", "牛奶", "魚肉", "小黃瓜"], 0, "玉米屬全穀雜糧類，也帶黃色。"),
    q("紅色蔬菜哪個例子最好？", ["紅甜椒", "白蘿蔔", "香菇", "山藥"], 0, "紅甜椒是紅色蔬菜。"),
    q("白色蔬菜哪一組較適合？", ["白花椰菜、白蘿蔔、洋蔥", "白飯、吐司、麵條", "牛奶、起司、優格", "雞肉、魚肉、蛋"], 0, "白色蔬菜也能提供不同營養。"),
    q("如果今天只吃綠色蔬菜，彩虹原則還缺什麼？", ["其他顏色輪流搭配", "只要更多白飯", "只要喝飲料", "完全不用變化"], 0, "彩虹飲食重點是多色多樣。"),
    q("紅色水果哪個最適合？", ["草莓", "豆干", "白飯", "花生"], 0, "草莓是紅色水果。"),
    q("橘黃色水果哪一組較適合？", ["木瓜、芒果、橘子", "青江菜、菠菜", "牛奶、優格", "魚、肉、蛋"], 0, "木瓜、芒果、橘子可代表橘黃色水果。"),
    q("綠色蔬菜哪一組較適合？", ["花椰菜、菠菜、青椒", "葡萄、藍莓", "白飯、麵", "雞蛋、肉"], 0, "綠色蔬菜可多樣輪替。"),
    q("紫色全穀雜糧哪一個較適合？", ["紫米", "鮮奶", "豆腐", "白蘿蔔"], 0, "紫米是紫色全穀雜糧。"),
    q("彩虹飲食的主要目的之一是？", ["增加食物多樣性", "只吃單一食物", "完全不吃蔬果", "只看熱量不看種類"], 0, "多色食物可幫助攝取不同營養。"),
    q("哪一組同時包含全穀、蔬菜、水果的彩虹搭配？", ["紫米飯、菠菜、木瓜", "熱狗、薯條、汽水", "奶油、糖果、餅乾", "白飯、白麵、白吐司"], 0, "全穀、蔬菜、水果都能做彩虹變化。"),
    q("綠色豆類食物哪一個也能加入彩虹概念？", ["毛豆", "白糖", "奶油", "可樂"], 0, "毛豆可代表綠色豆類食物。"),
    q("紅色蔬果常被提到的植化素是？", ["茄紅素", "咖啡因", "酒精", "乳糖"], 0, "番茄、西瓜等紅色蔬果常含茄紅素。"),
    q("深綠色蔬菜通常鼓勵怎麼吃？", ["輪流搭配不同種類", "完全不吃", "只榨汁不吃菜", "只吃一小口"], 0, "不同深綠色蔬菜可輪流選。"),
    q("彩虹餐盤最好的描述是？", ["每天多色、多類、適量", "只吃紅色", "只吃肉", "只喝飲料"], 0, "彩虹飲食仍要兼顧種類與份量。")
  ]}
};

const state = { role: "landing", room: "", uid: localStorage.getItem("nutrition_uid") || crypto.randomUUID(), config: null, db: null, roomData: null, selectedCount: 10, sound: true, celebratedKey: "" };
localStorage.setItem("nutrition_uid", state.uid);
const el = (id) => document.getElementById(id);
const screens = ["landingScreen", "setupScreen", "hostScreen", "studentScreen"];
const params = new URLSearchParams(location.search);
function show(id){ screens.forEach((screen)=>el(screen).classList.toggle("active", screen===id)); }
function encodeConfig(config){ return btoa(unescape(encodeURIComponent(JSON.stringify(config)))).replaceAll("+","-").replaceAll("/","_").replaceAll("=",""); }
function decodeConfig(value){ const padded=value.replaceAll("-","+").replaceAll("_","/")+"===".slice((value.length+3)%4); return JSON.parse(decodeURIComponent(escape(atob(padded)))); }
function loadConfig(){ const embedded=window.NUTRITION_FIREBASE_CONFIG||DEFAULT_FIREBASE_CONFIG; if(params.get("cfg")) return {...embedded,...decodeConfig(params.get("cfg"))}; const saved=localStorage.getItem("nutrition_firebase_config"); return saved?{...embedded,...JSON.parse(saved)}:embedded; }
function initFirebase(config){ if(state.db) return state.db; state.config=config; state.db=getDatabase(initializeApp(config)); return state.db; }
function roomRef(path=""){ return ref(state.db, `rooms/${state.room}${path?`/${path}`:""}`); }
function randomRoomCode(){ return Math.random().toString(36).slice(2,6).toUpperCase(); }
function shuffle(items){ return [...items].map((item)=>({item,sort:Math.random()})).sort((a,b)=>a.sort-b.sort).map(({item})=>item); }
function playTone(kind){ if(!state.sound) return; const audio=new AudioContext(); const gain=audio.createGain(); const osc=audio.createOscillator(); const freq={join:520,buzz:760,right:920,wrong:160,next:440,award:1040}[kind]||440; osc.frequency.value=freq; osc.type=kind==="wrong"?"sawtooth":"sine"; gain.gain.setValueAtTime(.001,audio.currentTime); gain.gain.exponentialRampToValueAtTime(.12,audio.currentTime+.02); gain.gain.exponentialRampToValueAtTime(.001,audio.currentTime+.22); osc.connect(gain).connect(audio.destination); osc.start(); osc.stop(audio.currentTime+.24); }
function playVictory(){ ["right","next","buzz","award","right"].forEach((kind,index)=>setTimeout(()=>playTone(kind),index*150)); }
function renderModeOptions(){ el("modeSelect").innerHTML=Object.entries(banks).map(([key,bank])=>`<option value="${key}">${bank.label}（${bank.questions.length} 題庫）</option>`).join(""); }
async function createRoom(){ try{ const config=loadConfig(); if(!config) return show("setupScreen"); el("hostBuzz").textContent="正在建立場次..."; initFirebase(config); state.room=randomRoomCode(); state.celebratedKey=""; const mode=el("modeSelect").value; const count=Math.max(1,Math.min(60,Number(el("customCount").value||state.selectedCount))); const bank=banks[mode].questions; const order=shuffle(bank.map((_,index)=>index)).slice(0,Math.min(count,bank.length)); await set(roomRef(),{code:state.room,mode,requestedCount:count,order,index:-1,status:"lobby",scores:{red:0,blue:0},buzz:null,answer:null,createdAt:serverTimestamp()}); listenRoom(); const joinUrl=`${location.origin}${location.pathname}?room=${state.room}&cfg=${encodeConfig(config)}`; el("roomCode").textContent=state.room; el("qrCode").src=`https://api.qrserver.com/v1/create-qr-code/?size=240x240&data=${encodeURIComponent(joinUrl)}`; el("startRound").disabled=false; el("endRoom").disabled=false; playTone("join"); }catch(error){ el("hostBuzz").textContent=`建立場次失敗：${error?.message||error}`; } }
async function startRound(){ await update(roomRef(),{status:"playing",index:0,buzz:null,answer:null}); el("nextQuestion").disabled=false; playTone("next"); }
async function nextQuestion(){ const data=state.roomData; if(!data) return; const next=(data.index??-1)+1; if(next>=data.order.length){ await update(roomRef(),{status:"ended",buzz:null}); playVictory(); } else { await update(roomRef(),{index:next,buzz:null,answer:null,status:"playing"}); playTone("next"); } }
async function endRoom(){ await update(roomRef(),{status:"ended",buzz:null}); playVictory(); }
async function joinRoom(){ try{ const config=loadConfig(); if(!config) return show("setupScreen"); initFirebase(config); state.room=el("joinCode").value.trim().toUpperCase(); const name=el("studentName").value.trim()||`學員${Math.floor(Math.random()*90+10)}`; el("studentBuzz").textContent="正在加入場次..."; const snapshot=await get(roomRef()); if(!snapshot.exists()){ el("studentBuzz").textContent="找不到這個場次，請確認代碼。"; return; } await runTransaction(roomRef("players"),(players)=>{ players=players||{}; const list=Object.values(players); const redCount=list.filter((player)=>player.team==="red").length; const blueCount=list.filter((player)=>player.team==="blue").length; const team=redCount===blueCount?(Math.random()>.5?"red":"blue"):redCount<blueCount?"red":"blue"; players[state.uid]={name,team,joinedAt:Date.now()}; return players; }); el("joinPanel").classList.add("hidden"); el("studentGame").classList.remove("hidden"); listenRoom(); playTone("join"); }catch(error){ el("studentBuzz").textContent=`加入失敗：${error?.message||error}`; } }
async function buzzMe(){ const me=state.roomData?.players?.[state.uid]; if(!me||state.roomData?.buzz||state.roomData?.answer||state.roomData?.status!=="playing") return; await runTransaction(roomRef("buzz"),(current)=>current||{uid:state.uid,name:me.name,team:me.team,at:Date.now()}); playTone("buzz"); }
async function answerQuestion(choice){ const data=state.roomData; const me=data?.players?.[state.uid]; if(!me||data?.buzz?.uid!==state.uid||data?.answer) return; const question=currentQuestion(data); const correct=choice===question.answer; const otherTeam=me.team==="red"?"blue":"red"; const scores=data.scores||{red:0,blue:0}; if(correct) scores[me.team]=(scores[me.team]||0)+10; else scores[otherTeam]=(scores[otherTeam]||0)+5; await update(roomRef(),{scores,answer:{uid:state.uid,name:me.name,team:me.team,choice,correct,explain:question.explain}}); playTone(correct?"right":"wrong"); }
function currentQuestion(data){ if(!data||data.index<0) return null; return banks[data.mode].questions[data.order[data.index]]; }
function listenRoom(){ onValue(roomRef(),(snapshot)=>{ state.roomData=snapshot.val(); if(state.role==="host") renderHost(); if(state.role==="student") renderStudent(); }); }
function maybeCelebrate(data){ const key=`${state.room}:${data.status}:${data.scores?.red||0}:${data.scores?.blue||0}`; if(data.status==="ended"&&state.celebratedKey!==key){ state.celebratedKey=key; playVictory(); } }
function championInfo(scores={}){ const red=scores.red||0; const blue=scores.blue||0; if(red===blue) return {team:"tie",label:"雙方平手",className:"tie"}; return red>blue?{team:"red",label:"紅隊冠軍",className:"red"}:{team:"blue",label:"藍隊冠軍",className:"blue"}; }
function reviewQuestions(data){ return (data.order||[]).map((questionIndex,index)=>({number:index+1,question:banks[data.mode].questions[questionIndex]})); }
function renderFinale(data,prefix){ const champion=championInfo(data.scores); const red=data.scores?.red||0; const blue=data.scores?.blue||0; el(`${prefix}Round`).textContent="活動結束"; el(`${prefix}Question`).innerHTML=`<div class="champion-card ${champion.className}"><div class="fireworks" aria-hidden="true"><span></span><span></span><span></span><span></span></div><p>頒獎時間</p><strong>${champion.label}</strong><small>紅隊 ${red} 分　藍隊 ${blue} 分</small></div>`; const answers=el(`${prefix}Answers`); answers.classList.add("final-review"); answers.innerHTML=reviewQuestions(data).map(({number,question})=>`<article class="review-item"><p>第 ${number} 題</p><h3>${escapeHtml(question.text)}</h3><strong>答案：${escapeHtml(question.options[question.answer])}</strong><span>${escapeHtml(question.explain)}</span></article>`).join(""); el(`${prefix}Buzz`).textContent=champion.team==="tie"?"今天兩隊表現一樣精彩，可以一起討論答題策略。":`${champion.label}，掌聲鼓勵！`; }
function renderHost(){ const data=state.roomData; if(!data) return; maybeCelebrate(data); el("hostRedScore").textContent=data.scores?.red||0; el("hostBlueScore").textContent=data.scores?.blue||0; renderRoster(data.players||{}); el("startRound").disabled=data.status!=="lobby"; el("nextQuestion").disabled=data.status!=="playing"||!data.answer; if(data.status==="ended") return renderFinale(data,"host"); const question=currentQuestion(data); el("hostRound").textContent=data.index>=0?`第 ${data.index+1} 題 / ${data.order.length}`:`等待學員加入：${banks[data.mode].label}`; el("hostQuestion").textContent=question?question.text:"學員掃描 QR Code 後，名字會出現在隊伍名單。"; renderAnswers(el("hostAnswers"),question,data.answer,false); el("hostBuzz").textContent=buzzText(data); }
function renderRoster(players){ const red=[]; const blue=[]; Object.values(players).forEach((player)=>(player.team==="red"?red:blue).push(`<li>${escapeHtml(player.name)}</li>`)); el("redRoster").innerHTML=red.join(""); el("blueRoster").innerHTML=blue.join(""); }
function renderStudent(){ const data=state.roomData; const me=data?.players?.[state.uid]; if(!data||!me) return; maybeCelebrate(data); el("studentTeam").className=`student-team ${me.team}`; el("studentTeam").textContent=`${me.name}，你是${me.team==="red"?"紅隊":"藍隊"}`; el("studentRedScore").textContent=data.scores?.red||0; el("studentBlueScore").textContent=data.scores?.blue||0; if(data.status==="ended") return renderFinale(data,"student"); const question=currentQuestion(data); el("studentRound").textContent=data.index>=0?`第 ${data.index+1} 題 / ${data.order.length}`:"等待講師開始"; el("studentQuestion").textContent=question?question.text:"請看講台畫面，等待講師開始。"; el("buzzMe").disabled=data.status!=="playing"||Boolean(data.buzz)||Boolean(data.answer); renderAnswers(el("studentAnswers"),question,data.answer,data.buzz?.uid===state.uid&&!data.answer); el("studentBuzz").textContent=buzzText(data); }
function renderAnswers(container,question,answer,clickable){ container.classList.remove("final-review"); if(!question){ container.innerHTML=""; return; } container.innerHTML=""; question.options.forEach((option,index)=>{ const button=document.createElement("button"); button.className="answer"; button.type="button"; button.textContent=option; button.disabled=!clickable; if(answer&&index===question.answer) button.classList.add("correct"); if(answer&&answer.choice===index&&!answer.correct) button.classList.add("wrong"); if(clickable) button.addEventListener("click",()=>answerQuestion(index)); container.appendChild(button); }); }
function buzzText(data){ if(data.answer) return `${data.answer.name} 已作答：${data.answer.correct?"答對":"答錯"}。${data.answer.explain}`; if(data.buzz) return `${data.buzz.name}（${data.buzz.team==="red"?"紅隊":"藍隊"}）搶到答題權。`; if(data.status==="playing") return "開放搶答。"; return "等待講師開始。"; }
function escapeHtml(value){ return String(value).replace(/[&<>"']/g,(char)=>({"&":"&amp;","<":"&lt;",">":"&gt;",'"':"&quot;","'":"&#039;"})[char]); }
function setupEvents(){ el("hostEntry").addEventListener("click",()=>{state.role="host";show(loadConfig()?"hostScreen":"setupScreen");}); el("studentEntry").addEventListener("click",()=>{state.role="student";show(loadConfig()?"studentScreen":"setupScreen");}); el("saveConfig").addEventListener("click",()=>{try{const config=JSON.parse(el("firebaseConfig").value);localStorage.setItem("nutrition_firebase_config",JSON.stringify(config));show(state.role==="student"?"studentScreen":"hostScreen");}catch{alert("Firebase 設定不是有效 JSON。");}}); el("skipConfig").addEventListener("click",()=>show(state.role==="student"?"studentScreen":"hostScreen")); document.querySelectorAll(".segmented button").forEach((button)=>{button.addEventListener("click",()=>{document.querySelectorAll(".segmented button").forEach((item)=>item.classList.remove("active"));button.classList.add("active");state.selectedCount=button.dataset.count==="custom"?Number(el("customCount").value):Number(button.dataset.count);el("customCount").style.display=button.dataset.count==="custom"?"block":"none";if(button.dataset.count!=="custom") el("customCount").value=state.selectedCount;});}); el("createRoom").addEventListener("click",createRoom); el("startRound").addEventListener("click",startRound); el("nextQuestion").addEventListener("click",nextQuestion); el("endRoom").addEventListener("click",endRoom); el("joinRoom").addEventListener("click",joinRoom); el("buzzMe").addEventListener("click",buzzMe); el("soundToggle").addEventListener("click",()=>{state.sound=!state.sound;el("soundToggle").textContent=state.sound?"音效":"靜音";}); }
function boot(){ renderModeOptions(); document.querySelector("[data-count='10']").classList.add("active"); el("customCount").style.display="none"; setupEvents(); const config=loadConfig(); if(params.get("room")){ state.role="student"; state.room=params.get("room").toUpperCase(); el("joinCode").value=state.room; show(config?"studentScreen":"setupScreen"); } }
boot();
