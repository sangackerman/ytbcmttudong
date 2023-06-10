import undetected_chromedriver as uc
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
import random
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



profile_numbers = [17, 24]

for profile_number in profile_numbers:
    options = Options()
    options.add_argument(f'--profile-directory=Profile {profile_number}')
    options.add_argument('--user-data-dir=C:\\Users\\ADMIN\\AppData\\Local\\Google\\Chrome\\User Data\\')

    driver = uc.Chrome(executable_path="C:\Program Files\Google\Chrome\Application\chrome.exe", options=options)
    driver.maximize_window()
    # Thực hiện các thao tác cần thiết với trình duyệt ở profile hiện tại
    driver.get("https://youtu.be/bbgMhZRXp0s")
    time.sleep(2)
    driver.execute_script("window.scrollBy(0,500)","")


    for i in range (2):
 
      choicefile=open("listcmt.txt","r")
      linelist=[]
      for line in choicefile:
        linelist.append(line)
      choice=random.choice(linelist)
      WebDriverWait(driver,100).until(EC.presence_of_element_located((By.XPATH,'//*[@id="simplebox-placeholder"]')))
    
      driver.find_element(By.XPATH,'//*[@id="simplebox-placeholder"]').click()
      driver.find_element(By.XPATH,'//*[@id="contenteditable-root"]').send_keys(choice)

      time.sleep(random.randint(1,4))
      WebDriverWait(driver,100).until(EC.presence_of_element_located((By.ID,'submit-button')))
      driver.find_element(By.ID,'submit-button').click()
    
      time.sleep(3)
    # Chuyển đến trang chính của YouTube
    driver.get("https://www.youtube.com/")
    time.sleep(2)
    # Tìm và nhấp vào biểu tượng tài khoản
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="img"]')))
    driver.find_element(By.XPATH,'//*[@id="img"]').click()
    time.sleep(2)
    # Tìm và nhấp vào nút "Chuyển đổi tài khoản"
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH,'//*[@id="items"]/ytd-compact-link-renderer[3]')))
    driver.find_element(By.XPATH, '//*[@id="items"]/ytd-compact-link-renderer[3]').click()
    time.sleep(2)

    for i in range(1, 11):
    # Đợi cho tài khoản được tải lên
       account_selector = f'#contents > ytd-account-item-renderer:nth-child({i})'
       WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, account_selector)))
    
    # Chuyển đổi tài khoản
       driver.find_element(By.CSS_SELECTOR, account_selector).click()
       for i in range (2):
           choicefile=open("listcmt.txt","r")
           linelist=[]
           for line in choicefile:
            linelist.append(line)
           choice=random.choice(linelist)
           WebDriverWait(driver,100).until(EC.presence_of_element_located((By.XPATH,'//*[@id="simplebox-placeholder"]')))
    
           driver.find_element(By.XPATH,'//*[@id="simplebox-placeholder"]').click()
           driver.find_element(By.XPATH,'//*[@id="contenteditable-root"]').send_keys(choice)

           time.sleep(random.randint(1,4))
           WebDriverWait(driver,100).until(EC.presence_of_element_located((By.ID,'submit-button')))
           driver.find_element(By.ID,'submit-button').click()
    
           time.sleep(3)
    # Thực hiện các thao tác cần thiết trên tài khoản hiện tại

    
    time.sleep(2)

    # Sau khi hoàn thành, đóng trình duyệt hiện tại
    driver.quit()  




  
time.sleep(4)







