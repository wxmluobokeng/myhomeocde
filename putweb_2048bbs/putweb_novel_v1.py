'''
     功能：爬取小说
     版本：2.0
     主要实现：通过lxml 的 etree  xpath 解析
                from lxml import etree
'''

# 1、导入框架
import requests
from lxml import etree

def analyze_model(block,xpsth_str):
    list = block.xpath(xpsth_str)
    return list

# 2、输入url
url = "http://kuihua2020.com/v/2/renqishunv/"
# headers ={
#     "User-Agent":"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.13 Safari/537.36",
#     "Referer": "http://kuihua2020.com/"
# }
headers ={
    "User-Agent":"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.13 Safari/537.36"
}

referer = "http://kuihua2020.com/"              #网站链接用的是相对链接，需要拼接

# 3、获取数据
response = requests.get(url,headers=headers)
# print(response.text)

# 4、分析数据
html = etree.HTML(response.text)    # 整理

href1=html.xpath('//a/@href')
text1=html.xpath('//a/text()')
# print(href1,text1)


for href,text in zip(href1,text1):
    print(href[-5:],text)