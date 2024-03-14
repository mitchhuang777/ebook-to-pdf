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
import unittest
import coverage

# Login to website
def auto_login_to_website():
    
    max_retry = 3 # Maximum retry time
    retry_count = 0 # Current retry time

    while retry_count < max_retry:
        try:
            driver = webdriver.Chrome()
            # 晟景 Login page
            driver.get("https://elearning.visionbook.com.tw/login")
            
            # Find the email account and password field
            email_input = driver.find_element(By.ID, "email")
            password_input = driver.find_element(By.NAME, "password")
            
            # Open account.txt file
            with open('account.txt', 'r') as file:
                lines = file.readlines()
            # Get the username & password
            username = lines[0].strip()
            password = lines[1].strip()
            # Send the email account & password
            email_input.send_keys(username)
            password_input.send_keys(password)

            # Find the login button and click
            login_button = driver.find_element(By.XPATH, '//*[@id="wrapper"]/section/div/div/div/div/form/div/div[3]/button')
            login_button.click()
            
            break
        except Exception as e:
            print("An error occurred during login: {}".format(e))
            retry_count += 1
            print("Retrying... (Attempt {}/{})".format(retry_count, max_retry))
            # Continue to try
            continue
        
    return driver

# Get user cookies and download jpg file, then convert to pdf file
def get_user_cookies(driver):
    # driver = auto_login_to_website()
    time.sleep(2)
    cookies = driver.get_cookies()
    
    formatted_cookies = {cookie['name']: cookie['value'] for cookie in cookies}
    
    session = requests.Session()
    for cookie in cookies:
        session.cookies.set(cookie['name'], cookie['value'])
    
    page_id = 1
    with open('log.txt', 'w') as log_file:
        # Clear log.txt
        pass
    
    with open('url.txt', 'r') as file:
        lines = file.readlines()
        
    url = lines[0].strip()
    
    with open('log.txt', 'w') as log_file:
        while True:
            # Print the ongoing downloading page...
            print(f'Downloading page {page_id}')
            formatted_url = url.format(page_id=page_id)
            # Opne the website
            try:
                driver.get(formatted_url)
            
            except Exception as e:
                log_file.write(f'Cannot get{page_id}, may because is the final page')
                break

            # Get Cookies
            cookies = driver.get_cookies()

            # Add the cookies into the session
            for cookie in cookies:
                session.cookies.set(cookie['name'], cookie['value'])

            # Download picture
            response = session.get(formatted_url)
            
            pdf_directory = 'pdf'
            
            # If pdf/ directory not exists, create it!
            if not os.path.exists(pdf_directory):
                os.makedirs(pdf_directory)
            
            try:
                # Save the jpg into the pdf file folder
                with open(f'pdf/{page_id}.jpg', 'wb') as image_file:
                    image_file.write(response.content)

                # Convert jpg to the pdf file
                img = Image.open(f'pdf/{page_id}.jpg')
                img.save(f'pdf/{page_id}.pdf', 'PDF')
                os.remove(f'pdf/{page_id}.jpg')

                # Write the download result into log
                log_file.write(f'Page {page_id} downloaded and converted to PDF successfully\n')
                page_id += 1
            
            except Exception as e:
                print(f"Cannot get {page_id}, due to final page")
                os.remove(f'pdf/{page_id}.jpg')
                
                break

def natural_sort_key(s):
    import re
    return [int(text) if text.isdigit() else text.lower() for text in re.split(r'(\d+)', s)]

# Merge pdf file
def merge_pdf_file():
    pdf_merger = PdfMerger()
    output_pdf_path = 'result.pdf'
    
    # Get /pdf/ all pdf file, and sorted by file name
    pdf_files = sorted(os.listdir('pdf'), key=natural_sort_key)
    for pdf_file in pdf_files:
        print(pdf_file)
    
    # Merge all pdf file
    with tqdm(total=len(pdf_files), desc='Merging PDFs', unit='page') as pbar:
        for pdf_file in pdf_files:
            pdf_merger.append(os.path.join('pdf', pdf_file))
            pbar.update(1)
    
    # Save it
    with open(output_pdf_path, 'wb') as output_pdf:
        pdf_merger.write(output_pdf) 
        
driver = auto_login_to_website()
get_user_cookies(driver)
merge_pdf_file()