from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time
import csv
import pandas as pd
import numpy as np
import getpass
import random
import undetected_chromedriver as uc
import os

# Open the web browser


driver = webdriver.Chrome("C:\\Users\\ADMIN\\Documents\\code\\chromedriver.exe")
driver.get("https://www.youtube.com")


# Login to YouTube
username = input("Enter your YouTube username: ")
password = getpass.getpass("Enter your YouTube password: ")
time.sleep(2)
login_button = driver.find_element_by_xpath('/html/body/ytd-app/div[1]/div/ytd-masthead/div[4]/div[3]/div[2]/ytd-button-renderer/yt-button-shape/a/yt-touch-feedback-shape/div/div[2]')
login_button.click()
time.sleep(2)
email_field = driver.find_element_by_name("identifier")
email_field.send_keys(username)
next_button = driver.find_element_by_xpath('/html/body/div[1]/div[1]/div[2]/div/c-wiz/div/div[2]/div/div[1]/div/form/span/section/div/div/div[1]/div/div[1]/div/div[1]/input')
next_button.click()
time.sleep(2)
password_field = driver.find_element_by_name("password")
password_field.send_keys(password)
next_button = driver.find_element_by_xpath('//*[@id="passwordNext"]/div/button/span')
next_button.click()

# Read the video and comment files
video_list = []
with open('listvideo.txt', 'r') as file:
    reader = csv.reader(file)
    for row in reader:
        video_list.append(row[0])

comment_list = []
with open('listcomment.txt', 'r') as file:
    reader = csv.reader(file)
    for row in reader:
        comment_list.append(row[0])

# Loop through the videos and add comments
for video in video_list:
    # Navigate to the video page
    driver.get(video)

    # Add a comment to the video
    comment_box = driver.find_element_by_xpath('//*[@id="placeholder-area"]')
    comment_box.click()
    time.sleep(2)
    comment_box = driver.find_element_by_xpath('//*[@id="contenteditable-root"]')
    comment = random.choice(comment_list)
    comment_box.send_keys(comment)
    time.sleep(2)
    post_button = driver.find_element_by_xpath('//*[@id="submit-button"]')
    post_button.click()
    time.sleep(2)

    # Save the profile details
    profile_data = pd.DataFrame({'Username': [username], 'Video': [video], 'Comment': [comment]})
    profile_data.to_csv('profile.csv', mode='a', header=not os.path.exists('profile.csv'), index=False)

# Close the browser
driver.quit()
