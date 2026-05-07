# 營養對戰教室

這是第二版多人同步活動頁，部署在 `/info/nutrition-battle/`。

## 使用流程

1. 講師開啟 `/info/nutrition-battle/`。
2. 選「我是講師，建立場次」。
3. Firebase Web app config 已內建。
4. 選模式與題數，建立場次。
5. 投影 QR Code，學員掃碼進場。
6. 講師按「開始活動」，學生手機會看到同一題並以個人身分搶答。

## Firebase

目前使用 Firebase 專案 `realtime-database-2fcbb`。若建立場次失敗，請確認 Realtime Database 規則允許讀寫 `rooms`：

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
