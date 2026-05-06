# 營養對戰教室

這是第二版多人同步活動頁，部署在 `/info/nutrition-battle/`。

## 使用流程

1. 講師開啟 `/info/nutrition-battle/`。
2. 選「我是講師，建立場次」。
3. 第一次使用需貼上 Firebase Web app config。
4. 選模式與題數，建立場次。
5. 投影 QR Code，學員掃碼進場。
6. 講師按「開始活動」，學生手機會看到同一題並以個人身分搶答。

## 需要 Firebase 的原因

GitHub Pages 是靜態網站，本身不能儲存多人即時狀態。紅藍隊名單、同題同步、搶答先後與分數都需要即時資料庫。

建議使用 Firebase Realtime Database，初期教學可使用下列規則：

```json
{
  "rules": {
    "rooms": {
      "$room": {
        ".read": true,
        ".write": true
      }
    }
  }
}
```

正式長期使用時，建議再加入匿名登入與更嚴格的資料規則。
