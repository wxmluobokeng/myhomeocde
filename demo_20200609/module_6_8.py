'''
    作者：老萝卜
    版本：1.0
    功能：爬  2019世界大学学术排名
'''

# 1、导入框架
import requests
from lxml import html
from html.parser import HTMLParser


# 2、确定url 地址
url = "http://www.zuihaodaxue.cn/ARWU2019.html"
# 1.2添加 ua
ua = {"User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.13 Safari/537.36"}
#
# 3、发起请求
# result = requests.get(url).content.decode()
result = requests.get(url,headers = ua).content.decode()
# print(result)

# 4、提取数据( xpath , 正则)
dom = html.etree.HTML(result)
strs = dom.xpath("//tr[contains(@class,'alt')]")[:10]
# print(strs)

for str in strs:
    # 转换成字符串(bytes类型)  ,类似 将 进行html实体转义
    tree_one = html.tostring(str)
    # b表示bytes (对象类型）
    # print(type(tree_one),tree_one)

    tree_two = HTMLParser().unescape(tree_one.decode("utf-8"))
    print(type(tree_two),tree_two)


# 5、保存


