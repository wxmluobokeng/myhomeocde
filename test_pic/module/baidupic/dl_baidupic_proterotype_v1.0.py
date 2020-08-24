#!D:\Program Files\Anaconda3
# -*- coding: utf-8 -*-
# @Time : 2020/7/26 17:03
# @Author : 老萝卜
# @File : dl_baidupic_proterotype_v1.0.py
# @Software: PyCharm Community Edition

import requests
import re
import time

numPicture = 10
filepath="e:\\temp\\pythontest\\pic\\baidu_seach\\"
keyword = input("请输入需要查找的关键字（仅限单个关键词）：").strip()

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.13 Safari/537.36"
}

url = "http://image.baidu.com/search/flip?tn=baiduimage&ie=utf-8&word=" + keyword + "&pn="

try:
    response = requests.get(url, headers=headers, timeout=10)
except:
    print('网络错误，请调整网络后重试')
else:
    pic_url = re.findall('"objURL":"(.*?)",', response.text, re.S)  # 先利用正则表达式找到图片url
    num = 1
    for each in pic_url:
        print('正在下载第' + str(num + 1) + '张图片，图片地址:' + str(each))
        try:
            if each is not None:
                pic = requests.get(each, timeout=7)
            else:
                continue
        except BaseException:
            print('错误，当前图片无法下载')
            continue
        else:
            string = filepath + keyword + '_' + str(num) + '.jpg'
            fp = open(string, 'wb')
            fp.write(pic.content)
            fp.close()
            num += 1
        if num >= numPicture:
            break
