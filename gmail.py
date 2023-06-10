import undetected_chromedriver as uc
from selenium.webdriver.chrome.options import Options
import time

options = Options()

options.add_argument('--profile-directory=Profile 26')

options.add_argument('--user-data-dir=C:\\Users\\ADMIN\\AppData\\Local\\Google\\Chrome\\User Data\\')

driver = uc.Chrome(executable_path="C:\Program Files\Google\Chrome\Application\chrome.exe", options=options)
driver.get("https://gmail.com/")

time.sleep(50)
