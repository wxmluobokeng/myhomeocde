#!D:\Program Files\Anaconda3
# -*- coding: utf-8 -*-
# @Time : 2020/7/19 21:45
# @Author : 老萝卜
# @File : get_dubandata_v1.0.py
# @Software: PyCharm Community Edition

'''
    功能：获取豆辨网电影信息
    知识点：
    1、selenium的应用：
    2、lxml.etree 解析xpath
    3、with open("文件名","a",encoding="utf-8") as file:      #文件追加，utf-8 编码
            file.write(content)
    缺陷：
    1、网页需要不断下拉才能加载数据，未实现，
    2、获取的数据未进一步解析
'''

from selenium import webdriver
import time
from lxml import etree

# 1、调用谷歌浏览器请求豆辨网
driver = webdriver.Chrome()
url = "https://movie.douban.com/typerank?type_name=%E5%89%A7%E6%83%85&type=11&interval_id=100:90&action="  # 豆辨网/排行榜/剧情
driver.get(url)
time.sleep(2)
response = driver.page_source
driver.close()
driver.quit()
# print(response)

# 抽取想要的数据
html = etree.HTML(response)
title_list = html.xpath('//span[@class="movie-name-text"]/a/text()')
data_list = html.xpath('//div[@class="movie-misc"]/text()')
rate_list = html.xpath('//span[@class="rating_num"]/text()')
comment_list = html.xpath('//span[@class="comment-num"]/text()')
for title, data, rate, comment in zip(title_list, data_list, rate_list, comment_list):
    content = title, data, rate, comment
    print(content)
    with open(".\\豆辨影评.txt", "a",encoding="utf-8") as file:
        file.write(str(content) + "\n")
