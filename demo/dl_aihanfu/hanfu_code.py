#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jun 13 17:12:00 2020

"""

import requests
from lxml import etree
import os
import re

def get_menu(url, heades):
    """
    根据每一页的网址
    获得每个链接对应的子网址
    params: url 网址
    """

    r = requests.get(url, headers=headers)
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
        r.encoding = r.apparent_encoding
        html = etree.HTML(r.text)
        html = etree.tostring(html)
        html = etree.fromstring(html)
        # 获得标题
        title = html.xpath(r'//*[@id="main_article"]/header/h1/text()')
        # 获得图片地址
        img = html.xpath(r'//div[@class="arc_body"]//figure/img/@src')
        # title 预处理 
        title = ''.join(title)
        title = re.sub(r'【|】', '', title)
        print(title)
        save_img(title, img, headers)
        
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

if __name__ == '__main__':
    """ 
    一页一页查找
    params : None
    """
    path = '/Users/****/汉服/'
    if not os.path.exists(path):
        os.mkdir(path)
        os.chdir(path)
    else:
        os.chdir(path)

    # url = 'http://www.aihanfu.com/zixun/tushang-1/'
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'
                             ' AppleWebKit/537.36 (KHTML, like Gecko)'
                             ' Chrome/81.0.4044.129 Safari/537.36'}
    for _ in range(1, 50):
        url = 'http://www.aihanfu.com/zixun/tushang-{}/'.format(_)
        for _ in get_menu(url, headers):
            get_page(_, headers)  # 获得一页
            
            
            
            
            
            
            
            
            
            
            
            