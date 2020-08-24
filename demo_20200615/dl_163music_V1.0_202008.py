# -*- coding: utf-8 -*-
# @time :2020/8/18 15:03
# @Author:老萝卜
# @file:dl_163music_V1.0_202008
# @Software:%{PRODUICT_NAME}

'''
        2020年8月中旬，网易云音乐改版升级，原songid无法直接获取，通过加密码法进行了加密
'''

import requests
import re
import time
import os

sysdatetime_compact = time.strftime('%Y%m%d%H%M%S', time.localtime(time.time()))
sysdate_compact = time.strftime('%Y%m%d', time.localtime(time.time()))

headers = {
    "user-agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.125 Safari/537.36",
    "referer": "https://music.163.com/",
    "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
    'Host': 'music.163.com',
}

title_re=r"<h2.*?>(.*?)</h2>"
reti = r'"/song\?id=\d+"\S+</a>'

url = "https://music.163.com/#/discover/artist/cat?id=1001"


# 在存的盘符上检查目录是否存，并创建
def checkmkdir(path):
    # print(os.getcwd())    #当前工作目当
    print("path=", path)
    if not os.path.exists(path):
        if path[-1] == "\\":
            len0 = path[:-1].rfind("\\")
        else:
            len0 = path.rfind("\\")
        checkmkdir(path[:len0])
        os.mkdir(path)


def save_text(filename, data, oprtype="a", encode="utf-8"):
    with open(filename, oprtype, encoding=encode) as file:
        file.write(data)


# 请求网络;获取html
def get_requests(url):
    # 请求网络
    html = requests.get(url, headers=headers)
    time.sleep(0.1)
    html.encoding = html.apparent_encoding
    # print(html)
    return html.text

def xpath_songid(songstrlist):
    songlist=[]
    for item in songstrlist:
        item1=item.split('">')
        song_id=re.sub('"/song\?id=',"",item1[0])
        song_name=re.sub('</a>',"",item1[1])
        url_song = "https://music.163.com/song/media/outer/url?id=%s" % song_id
        songlist.append((song_id, song_name))
        # songlist.append((url_song, song_name))
    return songlist

def main():
    # url = "https://music.163.com/discover/artist/cat?id=1001"6460
    url = "https://music.163.com/artist?id=10559"
    url = "https://music.163.com/artist?id=6460"
    url = "https://music.163.com/artist?id=6459"
    url = "https://music.163.com/artist?id=6468"
    # response=get_requests(url)

    s = requests.session()
    # response = s.get(url, headers=headers, timeout=30).content
    responsetext = s.get(url, headers=headers, timeout=30).text
    save_text(f"music.163.com.{sysdate_compact}.html", responsetext, "w")
    title=re.findall(title_re,responsetext)[0]
    pipei = re.findall(reti, responsetext)
    # print(title)
    # print(pipei)
    file_dir=f"e:\\temp\\pythontest\\163music\\{title}\\"
    checkmkdir(file_dir)
    songlist=xpath_songid(pipei)
    print(file_dir)
    print("songlist=",songlist)






if __name__ == "__main__":
    main()
