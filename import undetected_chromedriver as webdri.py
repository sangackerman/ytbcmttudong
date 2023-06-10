import undetected_chromedriver as uc
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
import random
from selenium.webdriver.common.by import By
options = Options()

options.add_argument('--profile-directory=Profile 24')

options.add_argument('--user-data-dir=C:\\Users\\ADMIN\\AppData\\Local\\Google\\Chrome\\User Data\\')

driver = uc.Chrome(executable_path="C:\Program Files\Google\Chrome\Application\chrome.exe", options=options)
driver.maximize_window()

driver.get("https://www.youtube.com/")

time.sleep(random.randint(5,10))





