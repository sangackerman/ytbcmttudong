import undetected_chromedriver as uc
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
import random
from selenium.webdriver.common.by import By
options = Options()

options.add_argument('--profile-directory=Profile 24')

options.add_argument('--user-data-dir=C:\\Users\\ADMIN\\AppData\\Local\\Google\\Chrome\\User Data\\')

driver = uc.Chrome(executable_path="C:\Program Files\Google\Chrome\Application\chrome.exe", options=options)
driver.maximize_window()



time.sleep(random.randint(5,10))
# Lấy danh sách bình luận từ tệp tin
def get_comments():
    with open('listvideo.txt', 'r') as file:
        comments = file.readlines()
    return comments

# Lấy danh sách video từ tệp tin
def get_videos():
    with open('listvideo.txt', 'r') as file:
        videos = file.readlines()
    return videos

# Bình luận vào video
def comment_on_video(video_url, comment):
    driver.get(video_url)
    time.sleep(10)

    driver.execute_script("window.scrollBy(0,500)","")

    comment_box = driver.find_element(By.XPATH, '//*[@id="contenteditable-root"]')
    # Thay đổi id của ô nhập bình luận thực tế
    comment_box.send_keys(comment)
    comment_box.send_keys(Keys.RETURN)
    
# Lấy danh sách bình luận và video
comments = get_comments()
videos = get_videos()

# Bình luận vào từng video

for video in videos:
    video_url = video.strip()
    for comment in comments:
        comment_text = comment.strip()
        comment_on_video(video_url, comment_text)

# Đóng trình duyệt
driver.quit()





