from selenium import webdriver
from time import sleep
import os
from selenium.webdriver.firefox.options import Options as FirefoxOptions
tkhoan = 'C:\\Users\\ADMIN\\Documents\\code\\tk'
chrome_option = webdriver.ChromeOptions()
chrome_option.add_argument("user-data-dir="+tkhoan)
driver =  webdriver.Chrome('./chromedriver', chrome_options = chrome_option)

sleep(1)
driver.get('https://www.pinterest.co.uk/')
sleep(5)
print('ff')
try:

	driver.find_element_by_xpath("/html/body/div[1]/div/div[1]/div/div/div/div/div/div[1]/div/div/div[1]/div/div[2]/div[2]/button/div/div").click()
	sleep(2)
	driver.find_element_by_id("email").send_keys('msangm2018@gmail.com')
	sleep(2)
	driver.find_element_by_id("password").send_keys('msangm123')
	sleep(2)
	driver.find_element_by_xpath("/html/body/div[1]/div/div[1]/div[2]/div/div/div/div/div/div[4]/form/div[7]/button/div").click()
	sleep(5)

except:
	print('loi')
	pass


//*[@id="contents"]/ytd-account-item-renderer[6]



