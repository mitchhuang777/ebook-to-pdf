# 📖 全自動黑科技電子書下載狂魔

## 免責聲明
- 本軟體僅供教學研究使用，切勿以任何非法方式使用本軟體
- 使用本程式時，仍應遵守中華民國著作權法之規定。若有侵權之疑慮，使用者應自行承擔因侵犯版權所引起之一切法律責任

## 簡介
將[晟景](https://www.visionbook.com.tw/home)電子書下載，然後儲存至電腦上，並輕鬆轉換為PDF檔

## 開發緣由
每次電子書都只能在網頁上閱讀，這其實相當不方便，無論是想做筆記，還是想在其他筆記軟體上開啟，都顯得非常麻煩。於是，我開發了「全自動黑科技電子書下載狂魔」。這款工具能夠輕鬆地將擬購買過的電子書下載到電腦上，並轉換成PDF檔案，這樣無論是做筆記還是考台大，就會變得輕而易舉

## 使用方式
- 把`ebook-to-pdf`檔案下載到你的電腦上
- 安裝所需套件 `pip install -r requirement.txt` 或是 `pip3 install -r requirement.txt`
- 接著下載對應你Google 瀏覽的ChromeDriver，[下載網址](https://googlechromelabs.github.io/chrome-for-testing/) (查詢Google瀏覽器版本請看底下方式)
- 打開`account.txt`，把`YOURACCOUNT`和`YOURPASSWORD`替換成晟景的帳號和密碼(帳號就是你在網頁登入時的帳號)
- 執行main.py `python main.py` `python3 main.py`

## 查詢Google瀏覽器版本
1. 打開Google瀏覽器
2. 在瀏覽器的搜尋欄位中輸入`chrome://settings/` 並按下Enter鍵
3. 左下角點選`關於 Chrome`
4. 就會看到版本是`1xx.x.xxxx.xxx`

## Unittest覆蓋率

| Name   | Stmts   | Miss   | Cover |
|-------|-------|-------|-------|
| test_main.py | 57 | 41 | 28% |


## ☕ Donation
如果你認為這個專案不錯的話，可以點擊下方的連結支持我，謝謝您的支持💖

[Buy me a coffee](https://www.buymeacoffee.com/huangmitch)
