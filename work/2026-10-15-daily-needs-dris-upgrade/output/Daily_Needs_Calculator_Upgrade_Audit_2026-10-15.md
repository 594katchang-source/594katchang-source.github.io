# 每日營養需求計算器升級與 DRIs 第八版檢核紀錄

- **執行日期**：2026-10-15
- **對應頁面**：[`teach/daily-needs/index.html`](file:///d:/@Codex/594katchang-source.github.io-main/teach/daily-needs/index.html)
- **官方標準依據**：[衛生福利部國民健康署《國人膳食營養素參考攝取量》第八版總表](https://www.hpa.gov.tw/Pages/ashx/GetFile.ashx?lang=c&type=2&sid=a309f81456b9416ea458a6e9025546a4)

---

## 一、本次依指示落實之四大改動

### 1. BMR 代謝公式回歸 Mifflin-St Jeor 臨床公式
- **男性**：`10 × 體重(kg) + 6.25 × 身高(cm) - 5 × 年齡(歲) + 5`
- **女性**：`10 × 體重(kg) + 6.25 × 身高(cm) - 5 × 年齡(歲) - 161`
- **特點**：在現代臨床營養學中相較於 1919 年舊版公式具有更高可靠度與準確度，避免基礎代謝率被虛高估算。

### 2. 國健署 DRIs 第八版關鍵 6 大營養素對照落實
1. **膳食纖維 (Dietary Fiber)**：
   - 19–50 歲：男 34g，女 27g
   - 51–70 歲：男 32g，女 25g
   - 71 歲以上：男 30g，女 24g
2. **維生素 D (Vitamin D)**：
   - 1–50 歲：10 μg (400 IU)
   - 51 歲以上熟齡長輩：15 μg (600 IU)
3. **鎂 (Magnesium)**：
   - 19–50 歲：男 380 mg，女 320 mg
   - 51–70 歲：男 360 mg，女 310 mg
   - 71 歲以上：男 350 mg，女 300 mg
4. **鐵 (Iron)**：
   - 19–50 歲：男 10 mg，育齡女性 15 mg
   - 51 歲以上：男 10 mg，停經後女性 10 mg
5. **鋅 (Zinc)**：
   - 成年與長輩：男 15 mg，女 12 mg
6. **鉀 (Potassium)**：
   - 成年與長輩：男 2,800 mg (2.8g)，女 2,500 mg (2.5g)

### 3. 公式算式解析橫式條列呈現
- 步驟 1、步驟 2、步驟 3 全面改為**滿寬橫幅卡片**（`.formula-row-card`），摒棄先前的三直欄並排。
- 每一項目的 `• ` 強制換行在最開頭（`.formula-line`）。
- 計算後的最後結果數值採用專屬色彩膠囊高亮（`.highlight-num.green`、`.highlight-num.blue`、`.highlight-num.coral`、`.highlight-num.amber`），清晰突出。

### 4. 專有名詞標準化
- 全站統一名詞為「**三大巨量營養素**」（無任何「宏量」殘留）。
- 嚴格維持無單一食物份數標記，僅標示克數與熱量大卡。

---

## 二、驗證結果
- HTML 語法與 JavaScript 代碼執行無誤。
- 各年齡層與性別（如 30 歲女性 vs 68 歲男性）之 DRIs 數值與 Mifflin-St Jeor 算式輸出均精確吻合官方總表。
