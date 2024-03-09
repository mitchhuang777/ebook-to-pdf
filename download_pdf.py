from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from PyPDF2 import PdfMerger
from tqdm import tqdm
from PIL import Image
import requests
import time
import os
import urllib.request

# os.chdir("download_pdf")

# 初始化webdriver
driver = webdriver.Chrome()

try:
    # 前往登入頁面
    driver.get("https://elearning.visionbook.com.tw/login")

    # 找到帳號和密碼輸入框，並輸入相應的帳號和密碼
    email_input = driver.find_element(By.ID, "email")
    password_input = driver.find_element(By.NAME, "password")
    
    username = "Your User Name"
    password = 'Your Password'
    
    # 輸入您的帳號和密碼
    email_input.send_keys(username)
    password_input.send_keys(password)

    # 找到登入按鈕，並點擊
    login_button = driver.find_element(By.XPATH, '//*[@id="wrapper"]/section/div/div/div/div/form/div/div[3]/button')
    login_button.click()
    
    # time.sleep(30)
    time.sleep(2)
    
    cookies = driver.get_cookies()
    formatted_cookies = {cookie['name']: cookie['value'] for cookie in cookies}
    
    session = requests.Session()
    for cookie in cookies:
        session.cookies.set(cookie['name'], cookie['value'])
        
    total_page = 145
    
    with open('log.txt', 'w') as log_file:
        # 循环1到10
        for page_id in range(1, total_page):
            # 打印正在下载的页面编号到控制台
            print(f'Downloading page {page_id}')

            # 打开网页
            # driver.get(f'https://elearning.visionbook.com.tw/protect/ebook/english/112EQ401E/112EQ401E/files/page/{page_id}.jpg')
            driver.get(f'https://elearning.visionbook.com.tw/protect/ebook/english/00VEQ410E/VEQ410E/files/page/{page_id}.jpg')

            # 获取Cookie
            cookies = driver.get_cookies()

            # 将Cookie添加到Session中
            for cookie in cookies:
                session.cookies.set(cookie['name'], cookie['value'])

            # 下载图片
            response = session.get(f'https://elearning.visionbook.com.tw/protect/ebook/english/00VEQ410E/VEQ410E/files/page/{page_id}.jpg')
            # response = session.get(f'https://elearning.visionbook.com.tw/protect/ebook/english/112EQ401E/112EQ401E/files/page/{page_id}.jpg')
            
            # 保存图片到pdf文件夹
            with open(f'pdf/page_{page_id}.jpg', 'wb') as image_file:
                image_file.write(response.content)

            # 打开下载的JPEG图片并转换为PDF
            img = Image.open(f'pdf/page_{page_id}.jpg')
            img.save(f'pdf/page_{page_id}.pdf', 'PDF')

            # 写入下载结果到log.txt
            log_file.write(f'Page {page_id} downloaded and converted to PDF successfully\n')
    driver.quit()    
    
finally:
    # 關閉瀏覽器
    driver.quit()
    
# 合并PDF文件
pdf_merger = PdfMerger()
output_pdf_path = 'merged_pdf.pdf'
with tqdm(total=10, desc='Merging PDFs', unit='page') as pbar:
    for page_id in range(1, total_page):
        pdf_merger.append(f'pdf/page_{page_id}.pdf')
        pbar.update(1)

# 保存合并后的PDF文件
with open(output_pdf_path, 'wb') as merged_pdf_file:
    pdf_merger.write(merged_pdf_file)

# 打印合并结果到log.txt
with open('log.txt', 'a') as log_file:
    log_file.write('PDF files merged successfully\n')
