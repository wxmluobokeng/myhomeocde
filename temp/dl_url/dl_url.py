# -*- coding: utf-8 -*-
# @time :2020/7/28 12:50
# @Author:老萝卜
# @file:dl_url
# @Software:%{PRODUICT_NAME}


import requests
import time

headers={
    "user-agent":"Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36"

}

url="https://h5.clewm.net/?url=qr71.cn%2FoFLkgA%2FqaQuLyS&hasredirect=1"
response=requests.get(url,headers=headers)
time.sleep(1)
response.encoding=response.apparent_encoding
with open(".\\1.html","w",encoding="utf-8") as file:
    file.write(response.text)
