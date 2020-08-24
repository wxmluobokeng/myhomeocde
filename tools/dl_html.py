# -*- coding: utf-8 -*-
# @time :2020/7/22 11:17
# @Author:老萝卜
# @file:dl_html
# @Software:%{PRODUICT_NAME}

import requests
import time

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36",
    "Referer": "https://www.58pic.com/piccate/11-198-0.html"
}

def get_requests(url,headers=headers):
    # 请求网络
    # html = requests.get(url, headers).content.decode('gbk')
    html = requests.get(url, headers)
    time.sleep(0.1)
    html.encoding=html.apparent_encoding
    # print(html)
    return html.text


def save_html(filename,data):
    with open(filename,"w",encoding="utf-8") as file:
        file.write(data)
    return filename

def main():
    # todaytime = time.strftime("%Y%m%d%H%M%S", time.localtime(time.time()))

    filepath="e:\\temp\\temp\\%s.html"%time.strftime("%Y%m%d%H%M%S", time.localtime(time.time()))
    url=input("请输入要保存的url：").strip()
    if url!="":
        filepath1=input("请输入要保存文件路径(含文件名)：").strip()
        if filepath1=="":
            filepath1=filepath
        print("url=",url,"\n","filename=",filepath1)
        content=get_requests(url)
        print("content:\n",content)
        filename=save_html(filepath1,content)
        print("刚刚下载保存的文件是: ",filename)




if __name__ == "__main__":
    main()