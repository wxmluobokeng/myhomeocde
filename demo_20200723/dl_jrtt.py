#!D:\Program Files\Anaconda3
# -*- coding: utf-8 -*-
# @Time : 2020/7/24 22:55
# @Author : 老萝卜
# @File : dl_jrtt.py
# @Software: PyCharm Community Edition

from selenium import webdriver
from lxml import etree
import time

# headers = {
#     "user-agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.13 Safari/537.36",
#     "referer": "https://www.toutiao.com/ch/news_tech/",
#     "x-requested-with": "XMLHttpRequest"
# }
headers = {
    "user-agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.13 Safari/537.36",
    }

url = "https://www.toutiao.com/"

driver = webdriver.Chrome()
driver.get(url)
driver.implicitly_wait(20)  # 隐性等待10秒,确保节点完全加载出来，用户感觉不到
# time.sleep(3)       # 延迟等待，

driver.find_element_by_link_text("科技").click()  # 定位到超链接上面的文本信息
time.sleep(20)

for i in range(3):
    js = "var q = document.documentElement.scrollTop=" + str(i * 500)
    driver.execute_script(js)  # 执行代码
    time.sleep(2)

html = driver.page_source

doc = etree.HTML(html)  # 构造解析对象
contents = doc.xpath("//div[@class='wcommonFeed']/ul/li")

for item in contents:
    title = item.xpath("div/div[1]/div/div[1]/a/text()")
    print(title)
time.sleep(100)
driver.quit()
