#!D:\Program Files\Anaconda3
# -*- coding: utf-8 -*-
# @Time : 2020/8/2 10:48
# @Author : 老萝卜
# @File : dl_qianqianmusic.py
# @Software: PyCharm Community Edition

'''
百度音乐
'''

import requests
from lxml import etree
import time

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.13 Safari/537.36"
}

def save_text(filename,data):
    with open(filename,"w",encoding="utf-8") as file:
        file.write(data)


# 根据音乐下载地址，下载单个音乐
def dl_music(url,path,title):
    filename=path+title+".mp3"

    mp3=requests.get(url,headers=headers).content
    with open(filename,"wb") as file:
        file.write(mp3)


def getsong_id_title(url):
    response=requests.get(url,headers=headers)
    time.sleep(0.1)
    response.encoding=response.apparent_encoding
    save_text(".\\1.html",response.text)
    html=etree.HTML(response.text)
    song_dir=html.xpath("//div/h2/text()")
    song_titles=html.xpath("//a[contains(@href,'/song/')]/text()")[1:]
    song_ids=html.xpath("//a[contains(@href,'/song/')]/@href")[1:]
    print("song_dir=",song_dir)
    print("song_titles=",song_titles)
    print("song_ids=",song_ids)
    return song_titles,song_ids

def main():
    url="http://music.taihe.com/top"
    getsong_id_title(url)

if __name__ == "__main__":
    main()





