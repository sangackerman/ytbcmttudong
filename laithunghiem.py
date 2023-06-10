import undetected_chromedriver as uc
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
import random
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException


with open('listvideo1.txt', 'r') as file:
    video_urls = file.readlines()
with open("listcmt.txt", "r") as file1, open("listcmt2.txt", "r") as file2, open("listcmt3.txt", "r") as file3:
    list1 = file1.readlines()
    list2 = file2.readlines()
    list3 = file3.readlines()

with open("so.txt", "r") as file:
    numbers = file.read().split()

profile_numbers = [int(number) for number in numbers]
time.sleep(random.uniform(1, 3))

for profile_number in profile_numbers:
    print(profile_number)
    options = Options()
    options.add_argument(f'--profile-directory=Profile {profile_number}')
    options.add_argument('--user-data-dir=C:\\Users\\ADMIN\\AppData\\Local\\Google\\Chrome\\User Data\\')
    options.add_argument('--headless')

    #options.add_argument("--mute")
    driver = uc.Chrome(executable_path="C:\Program Files\Google\Chrome\Application\chrome.exe", options=options)
    time.sleep(random.uniform(1,2))
    driver.maximize_window()

    driver.get("https://www.youtube.com/")
    time.sleep(random.uniform(2, 3))
    
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="img"]')))
    driver.find_element(By.XPATH,'//*[@id="img"]').click()
    time.sleep(random.uniform(2, 3))
    # Tìm và nhấp vào nút "Chuyển đổi tài khoản"
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH,'//*[@id="items"]/ytd-compact-link-renderer[3]')))
    driver.find_element(By.XPATH, '//*[@id="items"]/ytd-compact-link-renderer[3]').click()
    time.sleep(random.uniform(2, 3))
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, '#contents > ytd-account-item-renderer:nth-child(1)')))
    
    # Chuyển đổi tài khoản
    driver.find_element(By.CSS_SELECTOR, '#contents > ytd-account-item-renderer:nth-child(1)').click()
    time.sleep(random.uniform(2, 3))
    
    
    for url in video_urls:
        driver.get(url)
        random.shuffle(list1)
        random.shuffle(list2)
        random.shuffle(list3)

# Chọn một comment ngẫu nhiên từ mỗi danh sách
        choice1 = random.choice(list1).strip()
        choice2 = random.choice(list2).strip()
        choice3 = random.choice(list3).strip()

# Kết hợp comment từ ba danh sách
        combined_choice = choice1 + " " + choice2 + " " + choice3
       
    # Đợi trang tải hoàn thành
        time.sleep(random.uniform(3, 4))
        driver.execute_script("window.scrollBy(0,500)","")
        time.sleep(random.uniform(3, 4)) 
       
        try:
            WebDriverWait(driver, 8).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="simplebox-placeholder"]')))
            driver.find_element(By.XPATH, '//*[@id="simplebox-placeholder"]').click()
        # Other actions to perform when the element is found
            time.sleep(random.uniform(1, 2))
            input_field = driver.find_element(By.XPATH, '//*[@id="contenteditable-root"]')
            input_field.send_keys(combined_choice)
            time.sleep(random.uniform(2, 3))
            driver.find_element(By.ID, 'submit-button').click()
            time.sleep(random.uniform(3, 4))
        except:
            print("Element not clickable within 8 seconds. Closing and reopening the browser.")
            #driver.quit()
            #time.sleep(random.uniform(2, 3))
            break
            
        
      
    
    #driver.get("https://www.youtube.com/")
    #time.sleep(random.uniform(2, 3))
   
    # Tìm và nhấp vào biểu tượng tài khoản
    #WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="img"]')))
    #driver.find_element(By.XPATH,'//*[@id="img"]').click()
    #time.sleep(random.uniform(2, 3))
    # Tìm và nhấp vào nút "Chuyển đổi tài khoản"
    #WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH,'//*[@id="items"]/ytd-compact-link-renderer[3]')))
    #driver.find_element(By.XPATH, '//*[@id="items"]/ytd-compact-link-renderer[3]').click()
    #time.sleep(random.uniform(2, 3))



    for i in range(2, 9):
            time.sleep(random.uniform(2, 3))
            driver.get("https://www.youtube.com/")
        
            time.sleep(random.uniform(2, 3))
    # Tìm và nhấp vào biểu tượng tài khoản
            WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="img"]')))
            driver.find_element(By.XPATH,'//*[@id="img"]').click()
            time.sleep(random.uniform(3, 4))
    # Tìm và nhấp vào nút "Chuyển đổi tài khoản"
            WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH,'//*[@id="items"]/ytd-compact-link-renderer[3]')))
            driver.find_element(By.XPATH, '//*[@id="items"]/ytd-compact-link-renderer[3]').click()
            time.sleep(random.uniform(2, 3))


            account_selector = f'#contents > ytd-account-item-renderer:nth-child({i})'
        
            try:
                WebDriverWait(driver, 8).until(EC.presence_of_element_located((By.CSS_SELECTOR, account_selector)))
                print(f"Element {i} found")
            except TimeoutException:
                print(f"Element {i} not found")
                break
            driver.find_element(By.CSS_SELECTOR, account_selector).click()
            time.sleep(random.uniform(2, 3))


        
            for url in video_urls:
    
                driver.get(url)
                random.shuffle(list1)
                random.shuffle(list2)
                random.shuffle(list3)

# Chọn một comment ngẫu nhiên từ mỗi danh sách
                choice1 = random.choice(list1).strip()
                choice2 = random.choice(list2).strip()
                choice3 = random.choice(list3).strip()

# Kết hợp comment từ ba danh sách
                combined_choice = choice1 + " " + choice2 + " " + choice3
                
                time.sleep(random.uniform(3, 4))
                driver.execute_script("window.scrollBy(0,500)","")
                time.sleep(random.uniform(3, 4))
                
                    
                try:
                    WebDriverWait(driver, 8).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="simplebox-placeholder"]')))
                    driver.find_element(By.XPATH, '//*[@id="simplebox-placeholder"]').click()
        # Other actions to perform when the element is found
                    time.sleep(random.uniform(1, 2))
                    input_field = driver.find_element(By.XPATH, '//*[@id="contenteditable-root"]')
                    input_field.send_keys(combined_choice)
                    time.sleep(random.uniform(2, 3))
                    driver.find_element(By.ID, 'submit-button').click()
                    time.sleep(random.uniform(3, 4))
                except:
                    print("Element not clickable within 8 seconds. Closing and reopening the browser.")
                    #driver.quit()
                    #time.sleep(random.uniform(2, 3))
                    break

                
        
                
    driver.quit()  

driver.quit()








    