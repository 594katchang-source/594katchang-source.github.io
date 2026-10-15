# 智慧餐食與份數分配器 (Meal Planner) 開發與驗證紀錄

- **工具名稱**：智慧餐食與份數分配器
- **訪問路徑**：[`teach/meal-planner/index.html`](file:///d:/@Codex/594katchang-source.github.io-main/teach/meal-planner/index.html)
- **索引卡片位置**：[`teach/index.html`](file:///d:/@Codex/594katchang-source.github.io-main/teach/index.html) 「1. 營養專區」第 2 位（熱量計算器之後、食物代換表之前）
- **關聯教具**：
  - 上游輸入：[`teach/daily-needs/`](file:///d:/@Codex/594katchang-source.github.io-main/teach/daily-needs/)（一鍵帶入目標熱量與三大比例）
  - 份數對照：[`teach/food-exchange/`](file:///d:/@Codex/594katchang-source.github.io-main/teach/food-exchange/)（六大類食物代換速查）
  - 示範食譜對接：[`teach/cook-database/`](file:///d:/@Codex/594katchang-source.github.io-main/teach/cook-database/)（275 道國健署與公信機構料理庫）

---

## 一、四大收合計算步驟與營養演算法落實

1. **步驟 1：建立營養總目標（預設收合）**：
   - 輸入目標熱量（支援 URL 參數 `?cal=1800&p=15&c=55&f=30` 動態填入）
   - 即時驗證蛋白質、醣類、脂肪比例總和為 100%
   - 透明展開三大營養素總克數與熱量除法算式
2. **步驟 2：鎖定「固定／剛性食物份數」（預設收合）**：
   - 輸入全脂乳品（預設 1 份）、水果類（預設 2 份）、蔬菜類（預設 3 份）
   - 清楚展開所扣除之蛋白質、醣類、脂肪
   - 精確計算剩餘待分配蛋白質、剩餘醣類與剩餘脂肪
3. **步驟 3：依序回推全穀與豆魚蛋肉，脂肪係數連動油脂堅果（預設收合）**：
   - `全穀份數 = 剩餘醣類 ÷ 15`（四捨五入至 0.5 份，自帶每份 2g 植物蛋白）
   - `肉類份數 = (剩餘蛋白質 - 全穀蛋白質) ÷ 7`（四捨五入至 0.5 份）
   - **三方案比較與油脂連動**：
     - **方案 1：低脂肉類（3g 脂）** ➔ 肉類帶入較少脂肪，油脂份數充足
     - **方案 2：中脂肉類（5g 脂）** ➔ 最常見家庭飲食，油脂份數適中
     - **方案 3：高脂肉類（10g 脂）** ➔ 肉自帶大量脂肪，油脂堅果嚴格限縮
   - 點選任一方案即時連動全日六大類總份數與餐次分配
4. **步驟 4：餐次分配（Meal Distribution）**：
   - 支援 2、3、4、5、6 餐智能分配
   - 分配原則：乳品固定安排於第一餐（早餐），其餘全穀、肉、菜、果、油依餐次平均分配至 0.5 份
   - 提供按鈕直達 [`teach/food-exchange/`](file:///d:/@Codex/594katchang-source.github.io-main/teach/food-exchange/)

---

## 二、智慧示範循環菜單（幾日示範菜單）

- 支援 **第 1 天、第 2 天、第 3 天** 分頁切換
- 自動讀取當前每餐分配之份數，換算具體食材與公克數：
  - **主食**：依份數計算出胚芽米飯碗數、烤全麥吐司片數、地瓜條數、南瓜碗數
  - **主菜**：對接 `cook-database` 國健署與衛生局示範料理（茶油時蔬蒸雞胸肉、清蒸鯛魚、香烤鮭魚、九層塔炒蛋等），並附帶連結
  - **配菜**：川燙炒時蔬克數（如 120g 約 0.8 碗）
  - **點心／好油／乳品**：水果、無調味堅果與鮮奶份量
