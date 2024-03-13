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
import auto_login_to_website

class TestAutoLoginToWebsite(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
    def tearDown(self):
        self.driver.quit()
        
    def test_auto_login_to_website(self):
        max_retry = 3 # Maximum retry time
        retry_count = 0 # Current retry time

        while retry_count < max_retry:
            try:
                driver = self.driver
                # 晟景 Login page
                self.driver.get("https://elearning.visionbook.com.tw/login")
                
                # Find the email account and password field
                email_input = WebDriverWait(driver, 10).until(
                    EC.visibility_of_element_located((By.ID, "email"))
                )
                password_input = WebDriverWait(driver, 10).until(
                    EC.visibility_of_element_located((By.NAME, "password"))
                )
                
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
                self.assertIsNotNone(login_button)
                login_button.click()
                time.sleep(3)
                
                break
            except Exception as e:
                print("An error occurred during login: {}".format(e))
                retry_count += 1
                print("Retrying... (Attempt {}/{})".format(retry_count, max_retry))
                
                # Retry
                continue
    
    def test_get_cookies(self):
        time.sleep(2)
        driver = self.driver
        self.test_auto_login_to_website()
        cookies = driver.get_cookies()
        self.assertIsNotNone(cookies)
        
    
if __name__=='__main__':
    cov = coverage.Coverage()
    cov.start()
    unittest.main()
    cov.stop()
    cov.report()
    cov.save()