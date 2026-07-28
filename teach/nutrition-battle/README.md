# 營養對戰教室

這是第二版多人同步活動頁，部署在 `/teach/nutrition-battle/`。

## 使用流程

1. 講師開啟 `/teach/nutrition-battle/`。
2. 選「我是講師，建立場次」。
3. 第一次使用時貼上 Firebase Web app config，設定只存於目前瀏覽器。
4. 選模式與題數，建立場次。
5. 投影 QR Code，學員掃碼進場。
6. 講師按「開始活動」，學生手機會看到同一題並以個人身分搶答。

## Firebase

工具使用 Firebase Realtime Database 與匿名登入。請在 Firebase Console 啟用 Anonymous Auth，再依頁面內的房間規則建議設定 `rooms/$room`。規則需要限制已登入使用者、房間建立者與個別玩家 UID，不能使用公開讀寫。

QR Code 由瀏覽器本機產生，完整加入網址不會送到 QR Code 第三方服務。Firebase Web app config 仍會放在本場加入網址中，這是目前讓學員掃碼後自動連線的必要資料，請搭配受限 Rules 與 Firebase 專案網域限制使用。
