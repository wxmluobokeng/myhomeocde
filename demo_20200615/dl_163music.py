#!D:\Program Files\Anaconda3
# -*- coding: utf-8 -*-
# @Time : 2020/8/1 16:01
# @Author : 老萝卜
# @File : dl_163music.py
# @Software: PyCharm Community Edition


'''
下载网易音乐
'''

import requests
from lxml import etree
import time
import os

headers={
    "user-agent":"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.13 Safari/537.36",
    "referer":"https://music.163.com/"
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


def save_text(filename,data):
    with open(filename,"w",encoding="utf-8") as file:
        file.write(data)


# 请求网络;获取html
def get_requests(url):
    # 请求网络
    html = requests.get(url, headers=headers)
    time.sleep(0.1)
    html.encoding=html.apparent_encoding
    # print(html)
    save_text(".\\1.html",html.text)
    return html.text

def get_parser_url(data):
    save_text(".\\2.html",data)
    html = etree.HTML(data)
    href_url_list = html.xpath('//div[@id="song-list-pre-cache"]/ul/li/a/@href')
    nametext_list = html.xpath('//div[@id="song-list-pre-cache"]/ul/li/a/text()')
    title=html.xpath("//h2[@class='f-ff2 f-brk']/text()")[0]
    print("href_url_list=",href_url_list)
    print("nametext_list=",nametext_list)
    print("title=",title)
    return title,href_url_list,nametext_list



def main():
    # url = "https://music.163.com/playlist?id=5136791969"
    # url = "https://music.163.com/playlist?id=3212113629"
    url="https://music.163.com/user/home?id=29879272"
    # url = "https://music.163.com/playlist?id=5136791969"

    html= get_requests(url)
    title,url_list,name_list=get_parser_url(html)
    path="e:\\temp\\pythontest\\网易云音乐\\"+title+"\\"
    checkmkdir(path)
    for item,name1 in zip(url_list,name_list):
        song_id=item.split("=")[-1]
        url_music="https://music.163.com/song/media/outer/url?id=%s"%song_id
        print(url_music)
        print(song_id,name1)
        music_content=requests.get(url_music,headers=headers)
        time.sleep(0.1)
        file_name=path+name1+".mp3"
        with open (file_name,'wb') as file:
            file.write(music_content.content)





if __name__ == "__main__":
    main()