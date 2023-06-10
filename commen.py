from bdb import Breakpoint
from sys import breakpointhook
from time import sleep
from unicodedata import name
import webbrowser
import undetected_chromedriver as uc
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import random
from selenium import webdriver
import string
import pyperclip

options = uc.ChromeOptions()
options.add_argument('user-data-dir=C:\\Users\\ADMIN\\Documents\\code\\luu')
driver = uc.Chrome(options=options,use_subprocess=True)
wait =WebDriverWait(driver,10)
url = 'https://www.youtube.com/watch?v=4MPTyddsS00'
driver.get(url)
sleep(5)
driver.execute_script("window.scrollBy(0,500)","")

for i in range(102):
    choicefile = open("listcmt.txt", "r")
    linelist = []
    for line in choicefile:
        linelist.append(line)
    choice = random.choice(linelist)
    WebDriverWait(driver, 100).until(EC.presence_of_element_located((By.XPATH,'//*[@id="simplebox-placeholder"]')))
    driver.find_element(By.XPATH, '//*[@id="simplebox-placeholder"]')
    driver.find_element(By.XPATH, '//*[@id="contenteditable-root"]'
                    ).send_keys(choice)
    # sleep(200)

    driver.find_element(By.ID, 'submit-button').click()

    sleep(1)

