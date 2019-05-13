# 使用gspread把資料寫到google sheet
1. 在google api網址註冊https://console.developers.google.com/cloud-resource-manager
2. 先創建憑證，OAuth2.0
3. 創建完憑證，建立一個API_json給google sheet用
4. 在GoogleDrive的google sheet下，創建一個google表單，命名為TestGithubCommit
5. 點選表單的Share，把表單分享給API_json裡面的email
6. 執行程式，每5秒會寫一筆資料到表單

# refer
https://city.shaform.com/zh/2016/03/19/gspread/