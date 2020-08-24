'''
    功能：下载妹子图主页图片
'''
import requests
from lxml import etree

headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.13 Safari/537.36',
    'Referer': 'https://www.mzitu.com/tag/ugirls/'
}

# 1. 请求妹子图拿到HTML数据
response = requests.get("https://www.mzitu.com/tag/ugirls/", headers=headers)

# 2. 抽取想要数据 图片链接、图片标题
html = etree.HTML(response.text) # 整理
src_list = html.xpath('//img[@class="lazy"]/@data-original')
alt_list = html.xpath('//img[@class="lazy"]/@alt')


i = 0
for src, alt in zip(src_list, alt_list):
    # 3. 下载图片
    response = requests.get(src, headers=headers)

    # 4. 保存图片
    fileName = ".\\iphone\\" + alt + ".jpg"
    print("正在保存图片文件：" + fileName)
    with open(fileName, "wb") as f:
        f.write(response.content)

    i += 1
    if i>10:
        break
