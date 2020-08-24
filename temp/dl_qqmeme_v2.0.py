'''
    功能:下载QQ表情包
'''

import requests
from lxml import etree
import time

url= "https://qq.yh31.com/zjbq/2920180.html"

response= requests.get(url)
html = etree.HTML(response.text)
# 打印解析内容str
t = etree.tostring(html, encoding="utf-8", pretty_print=True)
print(t.decode("utf-8"))

list1=html.xpath("//div[@id='fontzoom']/p/img/@src")

for item in list1:
    str1 =item.encode('utf-8').decode('utf-8')
    img_url = "https://qq.yh31.com"+str1
    print(type(str1),"pic_url:",img_url)
    list2=str1.split('/')
    filename=".\\image\\"+list2[-1]
    # print(list2[-1])
    img_content = requests.get(img_url).content
    time.sleep(0.1)
    with open(filename,"wb") as f:
        f.write(img_content)

