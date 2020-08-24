# -*- coding: utf-8 -*-
# @time :2020/8/17 9:56
# @Author:老萝卜
# @file:dl_vmgirls_pic
# @Software:%{PRODUICT_NAME}

'''
    爬取https://www.vmgirls.com/所有图片

'''

import time
import requests
from lxml import etree
import os
import json
import threading

# 设置线程锁：设置线程最大数量
thread_lock = threading.BoundedSemaphore(value=6)

basepath_picsave = "e:\\temp\\pythontest\\vmgirls\\"

headers = {
    "user-agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.125 Safari/537.36"
}

sysdatetime = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
sysdate = time.strftime('%Y-%m-%d', time.localtime(time.time()))
systime = time.strftime('%H:%M:%S', time.localtime(time.time()))
sysdatetime_compact = time.strftime('%Y%m%d%H%M%S', time.localtime(time.time()))


# 保存文本内容
def save_html(content, path, oprtye="a", encode="utf-8"):
    with open(path, oprtye, encoding=encode) as file:
        file.write(content)


# 第一步，请求网络  -  获取网络返回的数据
def get_page(url, encode="utf-8"):
    html = requests.get(url, headers=headers).content.decode(encode)  # 需要打开网站的编码格式，把拿到的数据进行解码，否m则出现乱码
    return html


# 解析数据首页
def xpath_toppage(response):
    pageslist = []
    html = etree.HTML(response)
    # a_list=html.xpath("/a")
    # # 将<a></a>信息保存
    # temp_list=[]
    # for item in a_list:
    #     str0=etree.tostring(item,encoding="utf-8").decode("utf-8")
    #     temp_list.append(str0)
    # temp_str="\n".join(temp_list)
    # save_html(temp_str,"page_a_content.txt","w")
    urllist = html.xpath("//a[@class='media-content']/@href")
    for url in urllist:
        newurl = "https://www.vmgirls.com/" + url
        if newurl not in pageslist:
            pageslist.append(newurl)
    return pageslist


# 创建目录
def createdir(dir_name):
    if not os.path.exists(dir_name):
        os.mkdir(dir_name)


# 解析每个人的页面
def xpath_pages(response):
    pagelist = []
    html = etree.HTML(response)
    title = html.xpath("//h1[@class='post-title h3']/text()")[0]
    author = html.xpath("//a[@class='author-popup']/text()")
    # urllist=html.xpath("//a[class='nc-light-gallery-item']/@href")
    urllist = html.xpath(f"//a[@title='{title}']/@href")
    # print("author=",author)
    # print("urllist=",urllist)
    savepath = basepath_picsave + title + "\\"
    createdir(savepath)
    return (savepath, urllist)


def download_save(filepath, url):
    req = requests.get(url, headers=headers)
    with open(filepath, "wb") as file:
        file.write(req.content)
    thread_lock.release()  # 释放线程锁


def savejson(data, filepath, oprtype="a", encode="utf-8"):
    with open(filepath, oprtype, encoding=encode) as fjson:
        json.dump(data, fjson, )


def main():
    url = "https://www.vmgirls.com/"
    response = get_page(url)
    save_html(response, f".\\www.vmgirls.com.{sysdate}.html", "w")
    if response == "":
        print("网页打开失败")
        return
    pageslist = xpath_toppage(response)
    # print("pageslist=",pageslist)
    picurllist = []
    for picsurl in pageslist:
        resp = get_page(picsurl)
        save_html(resp, "1.html", "w")
        picpath, urllist = xpath_pages(resp)
        # print("urllist=",urllist)
        for picurl in urllist:
            filename = picpath + picurl.split("/")[-1]
            picurl1 = "https://www.vmgirls.com/" + picurl
            picurllist.append((filename, picurl1))
            # print("picurllist=", picurllist)
            # print("(filename,picurl1)=",filename,picurl1)

    # print("picurllist=",picurllist)

    # temp_str="\n".join(picurllist)
    # save_html(temp_str,"urllist","w")
    savejson(picurllist, f"picurllist_{sysdatetime_compact}.json", "w")
    # with open("picurllist.json","r") as fjson:
    #     data=json.load(fjson)
    #     print("data=",data)


    numbers = 0
    for filepath, pic_url in picurllist:
        numbers += 1
        print("正在下载第{}张图片：{}".format(numbers,filepath))
        # 上锁   监控线程数
        thread_lock.acquire()
        # 设置线程
        tony = threading.Thread(target=download_save, args=(filepath, pic_url))
        # 启动线程
        tony.start()


if __name__ == "__main__":
    main()
