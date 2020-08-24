#!D:\Program Files\Anaconda3
# -*- coding: utf-8 -*-
# @Time : 2020/7/18 22:20
# @Author : 老萝卜
# @File : dl_meitanmeishi_v1.0.py
# @Software: PyCharm Community Edition
'''

    爬取美团美食商家信息
'''

import requests
from lxml import etree
from selenium import webdriver
import time

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.13 Safari/537.36",
    "Referer": "https://bj.meituan.com/meishi/",
}

mysession = requests.session()
mysession.headers.update(headers)
mysession.get("https://bj.meituan.com/meishi/")


# def get_list(url):
#     response = mysession.get(url, headers=headers)
#     response.encoding = response.apparent_encoding
#     time.sleep(2)
#     with open(".\\url1.html", "w", encoding="utf-8") as file:
#         file.write(response.text)
#     html = etree.HTML(response.text)
#     url_list = html.xpath("//li[@class='clear btm']/div/a/@href")
#     url_str = "\n".join(url_list)
#     with open(".\\url2.txt", "w", encoding="utf-8") as file:
#         file.write(url_str)
#     time.sleep(2)

# def get_list(url):
#     response = requests.get(url, headers=headers)
#     response.encoding = response.apparent_encoding
#     with open(".\\url1.html", "w", encoding="utf-8") as file:
#         file.write(response.text)
#     html = etree.HTML(response.text)
#     url_list = html.xpath("//li[@class='clear btm']/div/a/@href")
#     url_str = "\n".join(url_list)
#     with open(".\\url2.txt", "w", encoding="utf-8") as file:
#         file.write(url_str)
#     time.sleep(2)

def get_list(url):
    print(url)
    driver = webdriver.Chrome()

    driver.get(url)

    time.sleep(4)

    with open(".\\url1.html", "w", encoding="utf-8") as file:
        file.write(driver.page_source)
    time.sleep(3)
    url_list = driver.find_element_by_xpath("//li[@class='clear btm']/div/a/@href")
    url_str = "\n".join(url_list)
    with open(".\\url2.txt", "w", encoding="utf-8") as file:
        file.write(url_str)
    driver.close()
    driver.quit()

def get_cityabbr(cityname):
    pass


def get_totalpage(url):
    pass


def main():
    # 获取地区
    # city_abbr = get_cityabbr("北京")
    city_abbr = "bj"

    # 获取总页数
    url_firstpage = "https://%s.meituan.com/meishi/" % city_abbr
    # totalpage = get_totalpage(url_firstpage)
    # totalpage = 67
    totalpage = 1
    for i in range(totalpage):
        url = "https://%s.meituan.com/meishi/pn%d/" % (city_abbr, i + 1)
        get_list(url)
    pass


if __name__ == "__main__":
    main()
