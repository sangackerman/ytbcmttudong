import undetected_chromedriver as uc
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
import random
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

options = Options()

options.add_argument('--profile-directory=Profile 24')

options.add_argument('--user-data-dir=C:\\Users\\ADMIN\\AppData\\Local\\Google\\Chrome\\User Data\\')

driver = uc.Chrome(executable_path="C:\Program Files\Google\Chrome\Application\chrome.exe", options=options)
driver.maximize_window()


with open('listvideo1.txt', 'r') as file:
    video_urls = file.readlines()
with open("listcmt.txt", "r") as file1, open("listcmt2.txt", "r") as file2, open("listcmt3.txt", "r") as file3:
    list1 = file1.readlines()
    list2 = file2.readlines()
    list3 = file3.readlines()

# Xáo trộn danh sách comment
random.shuffle(list1)
random.shuffle(list2)
random.shuffle(list3)

# Chọn một comment ngẫu nhiên từ mỗi danh sách
choice1 = random.choice(list1).strip()
choice2 = random.choice(list2).strip()
choice3 = random.choice(list3).strip()

# Kết hợp comment từ ba danh sách
combined_choice = choice1 + " " + choice2 + " " + choice3
time.sleep(random.uniform(2, 3))
for url in video_urls:
    # Mở trang video
    driver.get(url)

    # Đợi trang tải hoàn thành
    time.sleep(3)

    driver.execute_script("window.scrollBy(0,500)","")
    


    WebDriverWait(driver,100).until(EC.presence_of_element_located((By.XPATH,'//*[@id="simplebox-placeholder"]')))
# Click vào phần tử
    driver.find_element(By.XPATH,'//*[@id="simplebox-placeholder"]').click()
# Gửi comment kết hợp vào trường nhập liệu
    input_field = driver.find_element(By.XPATH, '//*[@id="contenteditable-root"]')
    input_field.send_keys(combined_choice)
    time.sleep(random.uniform(2, 3))
    driver.find_element(By.ID,'submit-button').click()
    time.sleep(random.uniform(3, 5))



