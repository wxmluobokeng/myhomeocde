'''
   功能：下载妹子图每日更新
   日期：2020-6-19
   新增功能：按月获取
'''

import requests
from lxml import etree



def print_lxml_etree__Element(etree__Element):
    text = ""
    for node in etree__Element.itertext():
        text += node.strip()
    return text


headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.13 Safari/537.36',
    'Referer': 'https://www.mzitu.com/tag/ugirls/'
}

# 1. 请求妹子图拿到HTML数据
response = requests.get("https://www.mzitu.com/all/", headers=headers)
# print("保存返回的html:1.txt")
# with open(".\\1.txt", "w") as f:
#     f.write(response.text)

# 2. 抽取想要数据 图片链接、图片标题
html = etree.HTML(response.text)    # 整理

year_list = html.xpath('//div[@class="year"]')
ul_list = html.xpath('//ul[@class="archives"]')                     # 得到年份并的列表
print("ul_list列表元素个数：{}".format(len(ul_list)))
# month_list1 = ul_list[0].xpath('//li/p[@class="month"]/em')
# 为什么取出来数据都是一相的？
# print("month_list1列表元素个数：个数：{}；第1个：{}；第2个：{}；第3个：{}；第4个：{}".format(len(month_list1),
#                                                                    month_list1[0].text,month_list1[1].text,
#                                                                    month_list1[47].text,month_list1[48].text))
#
# month_list2 = ul_list[1].xpath('//li/p[@class="month"]/em')
# print("month_list2列表元素个数：{}；第1个：{}；第2个：{}；第3个：{}；第4个：{}".format(len(month_list2),
#                                                                 month_list2[0].text,month_list2[1].text,
#                                                                 month_list2[2].text,month_list2[3].text))
#
# month_list3 = ul_list[2].xpath('//li/p[@class="month"]/em')
# print("month_list3列表元素个数：{}；第1个：{}；第2个：{}；第3个：{}；第4个：{}".format(len(month_list3),
#                                                                 month_list3[0].text,month_list3[1].text,
#                                                                 month_list3[2].text,month_list3[3].text))
# day_list_0 = ul_list[0].xpath('//li/p[@class="url"]/text()')        # 取第一个年份2020年 日期列表
# print("ul_list[0]中日期列表元素个数：{}".format(len(day_list_0)))
url_lsit_0 = ul_list[0].xpath('//li/p[@class="url"]/a[@target="_blank"]/text()')
print("ul_list[0]中链接列表元素个数：{}".format(len(url_lsit_0)))
day_list_1 = ul_list[1].xpath('//li/p[@class="url"]/text()')
# url_lsit_0 = day_lists0[1].xpath('//a[@target="_blank"]/text()')
print("ul_list[1]中日期列表元素个数：{}".format(len(day_list)
url_lsit=html.xpath('//ul[@class="archives"]/li/p[@class="url"]/a[@target="_blank"]/text()')
print("html中链接列表元素个数：{}".format(len(url_lsit_0)))

# day_lists0 = ul_list[0].xpath('//li/p[@class="url"]')
# print(len(day_lists0),day_lists0)
# # day_list_0 = day_lists0.text
# # day_list_0 = day_lists0.text()
# day_list_0 = ul_list[0].xpath('//li/p[@class="url"]/text()')
# print(day_list_0)
# url_lsit_0 = day_lists0[0].xpath('//a[@target="_blank"]/text()')
# print("ul_list[0]日期个数：{},简介个数:{}".format(len(day_list_0),len(url_lsit_0)))
# print("day_list[0]的信息：1.日期：信息[{},{}]；2.日期：信息[{},{}]；3.日期：信息[{},{}]".format(day_list_0[0],url_lsit_0[0],
#                                                                            day_list_0[1],url_lsit_0[1],day_list_0[2],url_lsit_0[2]))
#
#
# day_lists1 = ul_list[1].xpath('//li/p[@class="url"]')
# print(len(day_lists1),day_lists1)
# day_list_1 = ul_list[1].xpath('//li/p[@class="url"]/text()')
# url_lsit_1 = day_lists1[1].xpath('//a[@target="_blank"]/text()')
# print("ul_list[1]日期个数：{},简介个数:{}".format(len(day_list_1),len(url_lsit_1)))
# print("day_list[1]的信息：1.日期：信息[{},{}]；2.日期：信息[{},{}]；3.日期：信息[{},{}]".format(day_list_1[0],url_lsit_1[0],
#                                                                            day_list_1[1],url_lsit_1[1],day_list_1[2],url_lsit_1[2]))

# # print(type(html))
# # # print(type(response.text),response.text)
# # src_list = html.xpath('//img[@class="lazy"]/@data-original')
# # alt_list = html.xpath('//img[@class="lazy"]/@alt')
#
# # list1 = html.xpath('//div[@class="year"]')
# #           //ul[@class="archives"]/li/p[@class="month"]
# # print("1",type(list1[0]))
# #
# # str1 = print_lxml_etree__Element(list1[0])
# #
# # print("str1=",str1)
# #
# # for item in list1:
# #     if item.text == "2020年":
# #         aaa = item.xpath("//p[@class='month']")
# #         print("aaa=",aaa[0].text)
# # #  print(list)
# # print(list1[0].text)
# # # with open(".\\2.txt", "w") as f:
# # #     f.write(response.text)
#
#
# # src_list = html.xpath('//a/@href')
# alt_list = html.xpath('//a')
# alt_list = html.xpath('//div[@class="year"]')
# # aaa = html.xpath('//div[@class="year"]')
# # aaa = html.xpath('//ul[@class="archives"]/p')
# # aaa = html.xpath('//ul[@class="archives"]/*')
#
#
# # aaa = html.xpath('//p[@class="url"]')
#
#
# # bbb= aaa[0].xpath("//a[@href]")
# # aaa = html.xpath('//[tag="2020年"]')
#
# # for item in  aaa:
# #     bbb = item.xpath("//a[@target='_blank']")
# #     for ccc in bbb:
# #         print(type(ccc),ccc.text)
#         # print(ccc[0].get_attribute("href"))
# #     # print_lxml_etree__Element(item)
# #     # print(i,item.xpath("/li"))
# # print("aaa",aaa)
# # print("aaa",aaa)
#
# aaa = html.xpath('//a[@target="_blank"]/text()')
# bbb = html.xpath('//a[@target="_blank"]/@href')
# print(aaa)
# print(bbb)
#

#
# i = 0
# for item1,item2 in zip(aaa,bbb):
#     # 3. 下载图片
#     response = requests.get(item2, headers=headers)
#     html1 = etree.HTML(response.text)  # 整理
#     # print("保存返回的html:1.txt")
#     # with open(".\\1.txt", "w") as f:
#     #     f.write(response.text)
#     # break
#
#     src = html1.xpath('//img[@class="blur"]/@src')
#     alt= html1.xpath('//img[@class="blur"]/@alt')
#     # if alt[0] != item1:
#     #     print(i,alt[0],item1)
#
#     pic_content = requests.get(src[0], headers=headers).content
#     # 4. 保存图片
#     fileName = ".\\iphone\\" + alt[0] + ".jpg"
#     print("正在保存图片文件：" + fileName)
#     with open(fileName, "wb") as f:
#         f.write(pic_content)
#
#     i += 1
#
#     if  i>10:
#         break