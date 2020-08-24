'''

'''

# from selenium import webdriver
import requests
import time

url = "https://i3.vzan.cc/upload/video/mp4/20200619/51e89a1c527f48dc99356a615b930890.mp4"

# driver = webdriver.Chrome()
# driver.get(url)
stream = requests.get(url).content
time.sleep(5)
filename=".\\stream\\1.mp4"
with open(filename, "wb") as f:
    f.write(stream)
print("下载完成")