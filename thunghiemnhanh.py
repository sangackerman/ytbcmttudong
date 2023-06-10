import time
import random
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

# Đọc tệp tin "so.txt" và trích xuất các số
with open("so.txt", "r") as file:
    numbers = file.read().split()

# Chuyển các số từ chuỗi sang kiểu dữ liệu số nguyên
profile_numbers = [int(number) for number in numbers]

for profile_number in profile_numbers:
    options = Options()
    options.add_argument(f'--profile-directory=Profile {profile_number}')
    options.add_argument('--user-data-dir=C:\\Users\\ADMIN\\AppData\\Local\\Google\\Chrome\\User Data\\')
    
    driver = webdriver.Chrome(executable_path="C:\Program Files\Google\Chrome\Application\chromedriver.exe", options=options)
    time.sleep(random.uniform(1, 2))
    driver.maximize_window()

    # Làm điều gì đó với driver (ví dụ: điều hướng đến một trang web, tương tác với các phần tử)

    driver.quit()  # Đóng driver sau khi hoàn thành

