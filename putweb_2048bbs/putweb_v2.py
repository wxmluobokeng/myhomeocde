'''
     功能：爬取主页
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
url = "http://kuihua2020.com/"
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
print(response.text)

# 4、分析数据
html = etree.HTML(response.text)    # 整理

# lis1 = html.xpath('//li')
# # print(type(lis1),lis1)
# for li in lis1:
#     # dds = li.xpath("//a[@target='_blank']/text()")
#     # dds = li.xpath("//dd/a")            #无数据
#     # dds = li.xpath("/dd")               #无数据
#     dds = li.xpath("//dd")
#     print(type(dds),dds)
#
#     href1=dds[0].xpath('//a[@target="_blank"]/@href')
#     text1=dds[0].xpath('//a[@target="_blank"]/text()')
#     # print(type(dds),dds)
#     # print(href1,text1)

# list1 = html.xpath("//li/d")
# list2 = html.xpath("//li/dd/a/text()")
# # list1 = html.xpath("//li/dd/a/@href")
# # list2 = html.xpath("//li/dd/a/text()")
# print("list1:",list1)
# print("list2:",list2)


href1=html.xpath('//a[@target="_blank"]/@href')
text1=html.xpath('//a[@target="_blank"]/text()')
print(href1,text1)

# 5、保存数据



driver.quit()