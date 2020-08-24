# -*- coding: utf-8 -*-
# @time :2020/7/23 13:23
# @Author:老萝卜
# @file:dl_aihanfu_tushang_v1.0
# @Software:%{PRODUICT_NAME}

import requests
from lxml import etree
import re
import os
import time


def save_html(data):
    filename = "e:\\temp\\temp\\%s.html" % time.strftime("%Y%m%d%H%M%S", time.localtime(time.time()))
    with open(filename,"w",encoding="utf-8") as file:
        file.write(data)
    print(filename)
    return filename


def get_menu(url, heades):
    """
    根据每一页的网址
    获得每个链接对应的子网址
    params: url 网址
    """

    r = requests.get(url, headers=heades)
    if r.status_code == 200:
        r.encoding = r.apparent_encoding
        html = etree.HTML(r.text)
        html = etree.tostring(html)
        html = etree.fromstring(html)
        # 查找每个子网址对应的链接, 然后返回
        children_url = html.xpath('//div[@class="news_list"]//article/figure/a/@href')
        for _ in children_url:
            yield _

def get_page(url, headers):
    """
    根据子页链接，获得图片地址，然后打包下载
    params: url 子网址
    """
    r = requests.get(url, headers=headers)
    if r.status_code == 200:
        save_html(r)
        time.sleep(1)
        r.encoding = r.apparent_encoding
        save_html(r)
        html = etree.HTML(r.text)
        html = etree.tostring(html)
        html = etree.fromstring(html)
        time.sleep(1)
        save_html(r)
        # 获得标题
        title = html.xpath(r'//*[@id="main_article"]/header/h1/text()')
        # 获得图片地址
        img = html.xpath(r'//div[@class="arc_body"]//figure/img/@src')
        # title 预处理
        title = ''.join(title)
        title = re.sub(r'【|】', '', title)
        print(title)
        # save_img(title, img, headers)

def save_img(title, img, headers):
    """
    根据标题创建子文件夹
    下载所有的img链接，选择更改质量大小
    params： title : 标题
    params:  img :  图片地址
    """
    if not os.path.exists(title):
        os.mkdir(title)
    # 下载
    for i, j in enumerate(img):  # 遍历该网址列表
        r = requests.get(j, headers=headers)
        if r.status_code == 200:
            with open(title + '//' + str(i) + '.png', 'wb') as fw:
                fw.write(r.content)
        print(title, '中的第', str(i), '张下载完成!')

def get_maxpage(url,headers):
    response=requests.get(url,headers)
    response.encoding=response.apparent_encoding
    html=etree.HTML(response.text)
    list_page=html.xpath("//div[@class='pagination']/div/li/a/text()")
    if list_page[-1]=="下一页" and list_page[-3]=="···":
        ret_maxpage=int(list_page[-2])
    else:
        ret_maxpage=0
    return ret_maxpage

def get_dlpicnum():
    return 1,2

def main():
    headers={
        "User-Agent":"Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36",
        "Referer":"http://www.aihanfu.com/zixun/tushang-2/"
    }
    url_bas="http://www.aihanfu.com/zixun/tushang-"
    url=url_bas+"1/"
    max_page=get_maxpage(url,headers)
    if max_page>0:
        # print(max_page)
        startpage,endpage=get_dlpicnum()
        for i in range(startpage,endpage):
            url = 'http://www.aihanfu.com/zixun/tushang-{}/'.format(i)
            menu_list=get_menu(url, headers)
            for item in get_menu(url, headers):
                print("main:item=",item)
                if (item=="http://www.aihanfu.com/wen/8519/"):
                    get_page(item, headers)  # 获得一页


    else:
        print("获取最大页数出错!")


if __name__ =="__main__":
    main()
