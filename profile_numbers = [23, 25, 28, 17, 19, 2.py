#profile_numbers = [25, 28, 17, 19, 12, 9, 13, 14, 30, 26] 31 32 

25
28
17
19
12
9
13
14
30
26
31
32

















import random





# Đọc danh sách comment từ hai tệp tin
with open("listcmt.txt", "r") as file1, open("listcmt2.txt", "r") as file2:
    list1 = file1.readlines()
    list2 = file2.readlines()

# Xáo trộn danh sách comment
random.shuffle(list1)
random.shuffle(list2)

# Kết hợp ngẫu nhiên mỗi dòng từ hai danh sách
combined_list = []
for cmt1, cmt2 in zip(list1, list2):
    combined_list.append(cmt1.strip() + " " + cmt2.strip())

# In ra danh sách kết hợp
for cmt in combined_list:
    print(cmt)




        except TimeoutException:
        # Actions to perform when the element is not found
            print("Element not found. Closing and reopening browser.")
            driver.quit()
            time.sleep(2)
        # Reopen the browser and navigate to the previous URL
            driver = webdriver.Chrome()  # Replace with the appropriate webdriver
            driver.get(url)    
    


            for url in video_urls:
    
                driver.get(url)
                for i in range(2, 9):
                    time.sleep(random.uniform(2, 3))
                    driver.get("https://www.youtube.com/")
                    WebDriverWait(driver, 8).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="simplebox-placeholder"]')))
                    driver.find_element(By.XPATH, '//*[@id="simplebox-placeholder"]').click()
        # Other actions to perform when the element is found
                    time.sleep(random.uniform(1, 2))
                    input_field = driver.find_element(By.XPATH, '//*[@id="contenteditable-root"]')
                    input_field.send_keys(combined_choice)
                    time.sleep(random.uniform(2, 3))
                    driver.find_element(By.ID, 'submit-button').click()
                    time.sleep(random.uniform(4, 5))    





                try:
                    WebDriverWait(driver, 8).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="simplebox-placeholder"]')))
                    driver.find_element(By.XPATH, '//*[@id="simplebox-placeholder"]').click()
        # Other actions to perform when the element is found
                    time.sleep(random.uniform(1, 2))
                    input_field = driver.find_element(By.XPATH, '//*[@id="contenteditable-root"]')
                    input_field.send_keys(combined_choice)
                    time.sleep(random.uniform(2, 3))
                    driver.find_element(By.ID, 'submit-button').click()
                    time.sleep(random.uniform(4, 5))
                except:
                    print("Element not clickable within 8 seconds. Closing and reopening the browser.")
                    driver.quit()
                    time.sleep(random.uniform(2, 3))

                    
                    driver.get(url)
                    continue
        
