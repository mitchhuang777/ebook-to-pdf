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
- 打開`url.txt`，替換成你要下載的網址(查詢電子書url請看底下方式)
- 執行main.py `python main.py` `python3 main.py`
- 最後會生成`result.pdf`，就是下載好的電子書了

## 查詢Google瀏覽器版本
1. 打開Google瀏覽器
2. 在瀏覽器的搜尋欄位中輸入`chrome://settings/` 並按下Enter鍵
3. 左下角點選`關於 Chrome`
4. 就會看到版本是`1xx.x.xxxx.xxx`

## 查詢電子書url
1. 登入後，點選`我的書籍`，或是登入後在瀏覽器輸入`https://elearning.visionbook.com.tw/member/ebook`
![image](https://github.com/mitchhuang777/ebook-to-pdf/assets/79703512/d9995b93-4446-426f-9a2a-9ddad5e8e1b1)

2. 點選你要下載的電子書，複製電子書網址

![image](https://github.com/mitchhuang777/ebook-to-pdf/assets/79703512/cbf80840-a163-4343-aaf5-42efb392a23d)

3. 接著在網址後面加上/files/page/1.jpg，如果有類似跳轉到png檔案的頁面就代表網址沒錯
![image](https://github.com/mitchhuang777/ebook-to-pdf/assets/79703512/47a51612-e0a4-4a66-b1f2-679ccb193565)

4. 接著把打開`url.txt`，把`1`的地方改成`{page_id}`，url的格式會長這樣子，`https://elearning.visionbook.com.tw/protect/ebook/english/00VEQ410E/VEQ410E/files/page/{page_id}.jpg`
5. 儲存檔案即可

## Unittest覆蓋率

| Name   | Stmts   | Miss   | Cover |
|-------|-------|-------|-------|
| test_main.py | 57 | 41 | 28% |


## ☕ Donation
如果你認為這個專案不錯的話，可以點擊下方的連結支持我，謝謝您的支持💖

[Buy me a coffee](https://www.buymeacoffee.com/huangmitch)
