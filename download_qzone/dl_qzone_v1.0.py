'''
    作者：老萝卜
    版本：1.0
    功能：爬取某个QQ空间的主面
        用lxml.etree解析
'''

import requests
from lxml import etree

url = "https://user.qzone.qq.com/192149641"
header = {
    "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.13 Safari/537.36",
    "Referer": "https://user.qzone.qq.com/192149641"
}

html = requests.get(url,header)
