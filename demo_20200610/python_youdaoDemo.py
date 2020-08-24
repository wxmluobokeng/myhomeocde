'''
    作者：老萝卜
    版本：V1.0
    日期：2020.6.11
    功能：爬 有道翻译
'''

# 0、导入框架
import requests
import time
import random
import hashlib
from lxml import etree

# 1、确定url
# url = 'http://fanyi.youdao.com/translate_o?smartresult=dict&smartresult=rule'
url = 'http://fanyi.youdao.com/?keyfrom=dict2.top'

# 1.2 反爬虫 ua
headers = {
    "Content-Type":"application/x-www-form-urlencoded; charset=UTF-8",
    "Referer":"http://fanyi.youdao.com/?keyfrom=dict2.top",
    "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.13 Safari/537.36",
    "Cookie":"OUTFOX_SEARCH_USER_ID = -168489976@10.169.0.84;OUTFOX_SEARCH_USER_ID_NCOO = 1204064070.781045;DICT_UGC = be3af0da19b5c5e6aa4e17bd8d90b28a |;JSESSIONID = abcbgkm3yxFkjh9iIZcnx;_ntes_nnid = 6c34074f4819a90566660ac766f38f5f, 1594553723839;___rl__test__cookies = 1594557101278"
}

# "salt": "15945571012835",
# "sign": "47eb17fed03186cd359a7f8d5458b053",
# "ts": "1594557101283",
# "bv": "df206627864145d2af89bee79eb0964c",


# i: 菠萝                                                 #待翻译的词
# from: AUTO
# to: AUTO
# smartresult: dict
# client: fanyideskweb
# salt: 15945571012835                                      #
# sign: 47eb17fed03186cd359a7f8d5458b053                    #
# ts: 1594557101283                                         # 时间戳
# bv: df206627864145d2af89bee79eb0964c                      # 浏览器md5加密  是固定的
# doctype: json
# version: 2.1
# keyfrom: fanyi.web
# action: FY_BY_REALTlME




def get_data(e):
    r = str(int(time.time() * 1000))
    random_num = random.randint(1, 9)
    i = r + str(random_num)
    print(r, i)
    str_sign = "fanyideskweb" + e + i + "mmbP%A-r6U3Nw(n]BjuEU"
    md5_str = hashlib.md5()
    print(md5_str)
    md5_str.update(str_sign.encode())
    # md5_str,digest()  # 16位md5
    sign = md5_str.hexdigest()  # 32位md5
    # data = {
        # "i": e,
        # "from": "AUTO",
        # "to": "AUTO",
        # "smartresult": "dict",
        # "client": "fanyideskweb",
        # "salt": i,
        # "sign": sign,
        # "ts": r,
        # "bv": "df206627864145d2af89bee79eb0964c",
        # "doctype": "json",
        # "version": "2.1",
        # "keyfrom": "fanyi.web",
        # "action": "FY_BY_REALTlME"
    data={
        "i":"学习",
        "from":"AUTO",
        "to":"AUTO",
        "smartresult":"dict",
        "client":"fanyideskweb",
        "salt":"15945649688529",
        "sign":"0645321962cacd907412e175228614d5",
        "ts":"1594564968852",
        "bv":"df206627864145d2af89bee79eb0964c",
        "doctype":"json",
        "version":"2.1",
        "keyfrom":"fanyi.web",
        "action":"FY_BY_CLICKBUTTION"
    }
    return data


data_new = get_data("菠萝")
print(data_new)
# 3、请求
response = requests.post(url, data=data_new, headers=headers)

# 4、解析数据
# print(type(result), result.text)
html=etree.HTML(response.text)
print(response.text)
result=html.xpath("//div[@id='transTarget']/p/span/text()")
print(result)

# 4、保存数据
