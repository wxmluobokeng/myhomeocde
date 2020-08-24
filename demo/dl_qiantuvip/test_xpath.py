from lxml import etree

# import re

with open(".\\1.html", "r", encoding='utf-8') as file:
    myPage = file.read()

print(myPage)
# html = etree.fromstring(myPage)
html = etree.HTML(myPage)

# url_list = html.xpath("//tr[@class='tr3 t_one']/td[@class='tal']/a[@class='subject']/@href")
# author_list = html.xpath("//tr[@class='tr3 t_one']/td[@class='tal y-style']/a[@class='bl']")
# text_list = html.xpath("//tr[@class='tr3 t_one']/td[@class='tal']/a[@class='subject']")

url_list = html.xpath(
    '//div[@class="pic-box clearfix "]/div[@class="qtw-card"]/a/div/img/@src')  # 丢掉前5个
url_list1 = html.xpath(
    '//div[@class="pic-box clearfix"]/div[@class="qtw-card"]')  # 丢掉前5个
# url_list2 = html.xpath(
#     '//div[@class="pic-box clearfix"]/div[@class="qtw-card"]/a/div/img/@src')  # 丢掉前5个
# url_list3 = html.xpath(
#     '//div[@class="pic-box clearfix"]/div[@class="qtw-card"]/a/div/img/@href')  # 丢掉前5个



print("url_list:", len(url_list), url_list)
print("url_list1:", len(url_list1), url_list1)
i=0
# for item in text_list:
#     print(i,"   -  ",item.text)
#     i+=1

