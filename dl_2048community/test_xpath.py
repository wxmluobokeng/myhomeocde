from lxml import etree

# import re

with open(".\\2.html", "r", encoding='utf-8') as file:
    myPage = file.read()
# myPage = '''<html>
#         <title>TITLE</title>
#         <body>
#         <h1>我的博客</h1>
#         <div>我的文章</div>
#         <div id="photos">
#          <img src="pic1.jpeg"/><span id="pic1">PIC1 is beautiful!</span>
#          <img src="pic2.jpeg"/><span id="pic2">PIC2 is beautiful!</span>
#          <p><a href="http://www.example.com/more_pic.html">更多美图</a></p>
#          <a href="http://www.baidu.com">去往百度</a>
#          <a href="http://www.163.com">去往网易</a>
#          <a href="http://www.sohu.com">去往搜狐</a>
#         </div>
#         <p class="myclassname">Hello,\nworld!<br/>-- by Adam</p>
#         <div class="foot">放在尾部的其他一些说明</div>
#         </body>
#         </html>'''

print(myPage)
# html = etree.fromstring(myPage)
html = etree.HTML(myPage)

# url_list = html.xpath("//tr[@class='tr3 t_one']/td[@class='tal']/a[@class='subject']/@href")
# author_list = html.xpath("//tr[@class='tr3 t_one']/td[@class='tal y-style']/a[@class='bl']")
# text_list = html.xpath("//tr[@class='tr3 t_one']/td[@class='tal']/a[@class='subject']")

url_list = html.xpath(
    "//tr[@class='tr3 t_one']/td[@class='tal']/a[@class='subject']/@href")  # 丢掉前5个
author_list = html.xpath(
    "//tr[@class='tr3 t_one']/td[@class='tal y-style']/a/text()")  # 丢掉前5个
oprtime2_list = html.xpath(
    "//tr[@class='tr3 t_one']/td[@class='tal y-style']/span/text()")  # 丢掉前5个
# # author_list = html.xpath("//tbody[@style='table-layout:fixed;']/tr[@class='tr3 t_one']/td[@class='tal y-style']/a[@class='bl']")[5:]            #丢掉前5个
text_list = html.xpath(
    "//tr[@class='tr3 t_one']/td[@class='tal']/a[@class='subject']")  # 丢掉前5个
# text_list = html.xpath("//tr[@class='tr3 t_one']/td[@class='tal y-style']/div[@class='f10 gray']")


print("url_list:", len(url_list), url_list)
print("author_list:", len(author_list), author_list)
print("text_list:", len(text_list), text_list)

i=0
for item in text_list:
    print(i,"   -  ",item.text)
    i+=1

