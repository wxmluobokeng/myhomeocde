#!D:\Program Files\Anaconda3
# -*- coding: utf-8 -*-
# @Time : 2020/7/26 10:39
# @Author : 老萝卜
# @File : initial_parameter.py
# @Software: PyCharm Community Edition



from lxml import etree

# 起始页面
start_url = "www.23jj.com"

# 最大页码 或 想下载的页数(从第1页开始，不大于最大页码)
maxpage = 2

# 图片保存路径
directory = "e:\\temp\\pythontest\\pic\\"    # 图片保存目录


def get_pageurls(base_url, startpage=1, endpage=2):
    '''
    生成起始页面列表
    :param base_url:    基础页面,最起码带 http://，也可以不用
    :param startpage:   开始页码
    :param endpage:     结束页码(不包含 )
    :return:            返回需要起始页面的列表
    '''
    # 例：
    # https://www.23jj.com/
    # https://www.23jj.com/page/2
    # https://www.23jj.com/page/3
    # page_urls = [self.base_url + '/page/{}'.format(page) for page in range(1, maxpage)]  # 生成每一页的url ，不同网页需要重构,www.23jj.comm 案例


    page_urls = [base_url.base_url + '/page/{}'.format(page) for page in range(startpage, endpage)]
    return page_urls


# 主页面解析：生成每个子页面url 算法实现
def get_urls(base_url, content):
    '''
    生成下载信息页面列表
    :param base_url:    基础页面,最起码带 http://，也可以不用
    :param content:     访问起始页面返回的html内容
    :return:            返回下载信息页面url列表
    '''
    # codes = html.xpath("/html/body/div[2]/div[1]/ul/li/a/@href")
    # urls = [self.base_url + code for code in codes]
    html = etree.HTML(content)
    codes = html.xpath("/html/body/div[2]/div[1]/ul/li/a/@href")
    urls = [base_url + code for code in codes]
    return urls


def get_ldmsg(base_url, content):
    '''
    解析下载页面的信息
    :param base_url:    基础页面,最起码带 http://，也可以不用
    :param content:     访问下载页面返回的html内容
    :return:            返回下载页面url和标题信息
    '''
    # html = etree.HTML(response.text)
    # url = html.xpath('//*[@id="content"]/a/img/@src')[0]
    # title = html.xpath('/html/body/div[2]/div[1]/h2/text()')[0]
    # pic_url = 'https:' + url
    html = etree.HTML(content)
    url = html.xpath('//*[@id="content"]/a/img/@src')[0]
    title = html.xpath('/html/body/div[2]/div[1]/h2/text()')[0]
    pic_url = 'https:' + url
    return pic_url, title


def get_next_ldurl(base_url, html):
    '''
    解析下一页的页面url
    :param base_url:    基础页面,最起码带 http://，也可以不用
    :param html:        待解析的html
    :return:            需要下一页的下载信息页面url
    '''
    # if html.xpath('//*[@id="page"]/a[last()]/text()')[0] == '下一页':
    #     code = html.xpath('//*[@id="page"]/a[last()]/@href')[0]
    #     self.get_pic_url(self.base_url + code)
    # html = etree.HTML(content)
    if html.xpath('//*[@id="page"]/a[last()]/text()')[0] == '下一页':
        return base_url + html.xpath('//*[@id="page"]/a[last()]/@href')[0]
    return ""
