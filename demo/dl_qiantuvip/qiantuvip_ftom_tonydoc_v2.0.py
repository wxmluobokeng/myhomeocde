# -*- coding: utf-8 -*-
# @time :2020/7/21 14:26
# @Author:老萝卜
# @file:qiantuvip_ftom_tonydoc_v2.0
# @Software:%{PRODUICT_NAME}

'''
   项目简介： 下载百度文库VIP文章
   参考资料：掘金 lg_Tony博客文章 https://juejin.im/post/5f06d16e6fb9a07e6d70b48b
   版本说明： v1.0  --> v2.0
        1、将代码重写了一遍,
        2、增加调试信息
'''

import requests
from lxml import etree
import os
import time

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36",
    "Referer": "https://www.58pic.com/piccate/11-198-0.html"
}


def save_text(filename,data):
    with open(filename,"w",encoding="utf-8") as file:
        file.write(data)

# 请求网络;获取html
def get_requests(url):
    # 请求网络
    # html = requests.get(url, headers).content.decode('gbk')
    html = requests.get(url, headers)
    time.sleep(0.1)
    html.encoding=html.apparent_encoding
    # print(html)
    return html.text

# 提取详情页url
def get_parser_url(data):
    save_text(".\\1.html.txt",data)
    html = etree.HTML(data)
    # href_url_list = html.xpath('//div[@class="pic-box clearfix "]/div[@class="qtw-card"]/a/div/img/@src')
    # href_url_list = html.xpath('//div[@class="pic-box clearfix "]/div[@class="qtw-card"]/a/div/img/@data-original')
    href_url_list = html.xpath('//div[@class="pic-box clearfix "]/div[@class="qtw-card"]/a/@href')
    return href_url_list

# 提取url数据
def get_new_img_url(data):
    html = etree.HTML(data)
    # 提取图片的url
    url_list = html.xpath('//img[@class="show-area-pic"]/@src')
    # 提取图片的标题
    title_list = html.xpath('//img[@class="show-area-pic"]/@title')
    if len(url_list)>=1 and len(title_list)>=1:
        url=url_list[0]
        title=title_list[0]+'.png'
        print(url, title)
    else:
        url=""
        title=""
        print("len(url_list)=",len(url_list),url_list)
        print("len(title_list)=", len(title_list), title_list)
    # print(url,title)
    return url,title

# 保存
def save_file(url,file):
    try:
        file_name = './我创建的千图网/'+file
        img = requests.get(url,headers=headers).content
        time.sleep(0.1)
        with open (file_name,'wb') as save_img:
            save_img.write(img)
    except FileNotFoundError:
        pass



def main():
    # 网址
    url = 'https://www.58pic.com/piccate/11-0-0.html'
    html = get_requests(url)
    # save_text(".\\2.txt",html)
    href_url_list = get_parser_url(html)

    print(href_url_list)

    html = get_requests('http:' + href_url_list[0])
    save_text(".\\3.html",html)

    # 遍历
    for url_html in href_url_list:
        html = get_requests('http:' + url_html)
        img_url, img_title = get_new_img_url(html)
        if img_url!="" and img_title!="":
            save_file('http:'+img_url, img_title)
            print('正在下载{}'.format(img_title))


if __name__ == "__main__":
    main()