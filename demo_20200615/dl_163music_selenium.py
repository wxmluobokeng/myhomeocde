#!D:\Program Files\Anaconda3
# -*- coding: utf-8 -*-
# @Time : 2020/8/17 22:37
# @Author : 老萝卜
# @File : dl_163music_selenium.py
# @Software: PyCharm Community Edition

from  selenium import webdriver
# 让浏览器在执行过程中等待加载数据
from selenium.webdriver.support.ui import WebDriverWait

import time

curdata_compact=time.strftime('%Y%m%d',time.localtime(time.time()))

def save_text(filename,data,oprtype="a",encode="utf-8"):
    with open(filename,oprtype,encoding=encode) as file:
        file.write(data)

driver = webdriver.Chrome()                               #chromedrive.exe保存在python目录下
url = "https://music.163.com/user/home?id=29879272"               #后花园网文-经典语录
driver.get(url)
WebDriverWait(driver,60)

save_text(f"{curdata_compact}.html",driver.page_source,"w")

# dom = driver.find_element_by_id("auto-id-dz9tZicfpN09Tv30")
songidstr=driver.find_elements_by_xpath("//div[@class='song']/div/div/span/a/@href")
songtitle=driver.find_elements_by_xpath("//div[@class='song']/div/div/span/a/b/text()")
print("songidstr=",songidstr)
print("songtitle=",songtitle)


driver.quit()