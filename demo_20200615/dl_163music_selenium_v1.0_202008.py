#!D:\Program Files\Anaconda3
# -*- coding: utf-8 -*-
# @Time : 2020/8/18 19:37
# @Author : 老萝卜
# @File : dl_163music_selenium_v1.0_202008.py
# @Software: PyCharm Community Edition\

'''
        2020年8月中旬，网易云音乐改版升级，原songid无法直接获取，通过加密码法进行了加密
        本模块功能：通过查找歌手的方式，获取 歌手id
'''

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import re
import time
import os

sysdata_compact = time.strftime("%Y%m%d",time.localtime(time.time()))

headers = {
    'Referer': 'http://music.163.com/',
    'Host': 'music.163.com',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.75 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
}

def save_text(filename,data,oprtype="a",encode="utf-8"):
    with open(filename,oprtype,encoding=encode) as file:
        file.write(data)




find = "邓紫棋"
find = "张学友"
find = "张雨生"
find = "郑智化"

# 打开selenium,启动谷歌浏览器
try:
    chrome_options = Options()
    # chrome_options.add_argument("--window-size=1920,1080")
    # 无头模式启动
    print("-1")
    chrome_options.add_argument('--headless')
    print("-2")
    # 谷歌文档提到需要加上这个属性来规避bug
    chrome_options.add_argument('--disable-gpu')
    print("-3")
    driver = webdriver.Chrome(chrome_options=chrome_options)
except:
    print("chrome加截失败")
    pass

print("0")

# 打开网易云，找到查找框，输入待查找 歌星姓名,并回车
driver.get("https://music.163.com/")
time.sleep(0.2)
driver.find_element_by_id("srch").send_keys(find)
driver.find_element_by_id("srch").send_keys(Keys.ENTER)
time.sleep(0.2)

print("1")

# 切换到 名叫 g_iframe 的 frame框架中，找到"单曲"菜单项，并点击加载
driver.switch_to.frame("g_iframe")
menu_danqu=driver.find_element_by_xpath("/html/body/div[3]/div/div[2]/ul/li[1]/a/em")
menu_danqu.click()
time.sleep(0.5)

print("2")

# 找到"歌手"菜单项，并点击加载
menu_geshou=driver.find_element_by_xpath("/html/body/div[3]/div/div[2]/ul/li[2]/a/em")
menu_geshou.click()
time.sleep(0.5)

print("3")

# 找到"歌手"，并点击加载
geshou = driver.find_element_by_xpath("//span[@class='msk']")           #  如果有多个，找到第一个就返回
geshou.click()


print("4")

# 得到当前url，取url中的数字，除163外，另一个就是歌手id
urlnow = driver.current_url
give = re.findall("\d+", urlnow)
give.remove("163")
artistid = give[0]  # 歌手id提取出来了

print("5")

# # 调试用，确保浏览器窗口打开
# while True:
#     str0=input("请输入q 退出：")
#     if str0=="q":
#         break
driver.quit()

print("歌id：\n",artistid)



