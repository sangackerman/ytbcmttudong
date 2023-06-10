from selenium import webdriver
driver = webdriver.Chrome("C:\\Users\\ADMIN\\Documents\\code\\chromedriver.exe")
driver.get('https://facebook.com')
driver.find_element_by_xpath('/html/body/div[1]/div[1]/div[1]/div/div/div/div[2]/div/div[1]/form/div[1]/div[1]/input') .send_keys ('msangm2009@gmail.com')
driver.find_element_by_xpath('/html/body/div[1]/div[1]/div[1]/div/div/div/div[2]/div/div[1]/form/div[1]/div[2]/div/input') .send_keys ('trungkien1201')
driver.find_element_by_xpath('/html/body/div[1]/div[1]/div[1]/div/div/div/div[2]/div/div[1]/form/div[2]/button') .click()
