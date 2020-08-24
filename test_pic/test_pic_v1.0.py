'''
  作者：老萝卜
  版本：v1.0
  时间：2020.6.12夜
  功能:
'''

import requests
import re

url = "https://image.baidu.com/search/index?tn=baiduimage&ipn=r&ct=201326592&cl=2&lm=-1&st=-1&fm=result&fr=&sf=1&fmq=1591979086808_R&pv=&ic=&nc=1&z=&hd=&latest=&copyright=&se=1&showtab=0&fb=0&width=&height=&face=0&istype=2&ie=utf-8&sid=&word=%E9%9D%92%E8%8B%B9%E6%9E%9C"

ua = {
    "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.13 Safari/537.36"
}
results = requests.get(url,headers=ua)
print(results.text)

lists = re.findall('<img class="layLoad" src="(*?)" data-spm-anchor-id="(*?)">',results,re.S)
print(lists)
# result = re.search('<li.*?active.*?singer="(.*?)">(.*?)</a>',html,re.S)
results = re.findall('<li.*?href="(.*?)".*?singer="(.*?)">(.*?)</a>', html, re.S)