#!D:\Program Files\Anaconda3
# -*- coding: utf-8 -*-
# @Time : 2020/8/17 21:37
# @Author : 老萝卜
# @File : dl_163music_20200817.py
# @Software: PyCharm Community Edition

'''
下载网易音乐(因近期改版)
未成功
'''

import requests
from lxml import etree
import time
import os

curdata_compact=time.strftime('%Y%m%d',time.localtime(time.time()))


headers={
    "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.13 Safari/537.36",
    "Referer": "https://music.163.com/"
}

#在存的盘符上检查目录是否存，并创建
def checkmkdir(path):
    # print(os.getcwd())    #当前工作目当
    print("path=",path)
    if not os.path.exists(path):
        if path[-1]=="\\":
            len0=path[:-1].rfind("\\")
        else:
            len0 = path.rfind("\\")
        checkmkdir(path[:len0])
        os.mkdir(path)

def save_text(filename,data,oprtype="a",encode="utf-8"):
    with open(filename,oprtype,encoding=encode) as file:
        file.write(data)

# 请求网络;获取html
def get_requests(url):
    # 请求网络
    html = requests.get(url, headers=headers)
    print("html.apparent_encoding=",html.apparent_encoding)
    html.encoding=html.apparent_encoding
    return html.text

def get_parser_url(data):
    pass

def main():
    url="https://music.163.com/user/home?id=29879272"
    html= get_requests(url)
    save_text(f"{curdata_compact}.html",html,"w")

    pass

data={
    "params": "i9LY4rB8dZywf4ci4KuNDHxPAZLnewtHYUfiMCQMM5nBJcjvMGKveEg0EY1r76tEy1sx88205eeI5w9PQQO/iHaUHQ9XoUKFPOR1VLku5UIoJo1i3e3Wg1xC9r9QFzKWYFo/A+sfnfzrtP3Hrt3fk63mROb9l1XYJw4UpEJKCQyUKgxlITK6zJMpoA2RLWP8",
    "encSecKey": "7ef70a26d4f9979496cc8d9a8a31b04d6af3a4e230fb716ee3d836a6183093e1c2ab1a7068545060b8e6b2092eae8a8dc4e7893d9a5842f2a42cb47f496ba55f649b3d351ecce64b7e795a3d5cce5b18fab520ca8c28105174b930491e304c739ccefd418aeb0af4434f7cc71a7974e53fe1f02dca50720629c985ebc3bc2dba"
}

if __name__ == "__main__":
    # main()

    url="https://music.163.com/weapi/v1/play/record?csrf_token="
    response=requests.post(url,headers=headers,data=data)
    print(response.json())