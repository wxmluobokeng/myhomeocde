'''
    功能：下载小说
'''

import requests
from lxml import etree
import time

headers = {
    "user-agent":"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.13 Safari/537.36"
}

#下载文件
def dl_text(url,path,filename):
    '''
        下载文档内容
        :param url: 网址
        :param path: 文件名称
        :return:
    '''
    response = requests.get(url,headers=headers)
    response.encoding = response.apparent_encoding

    # print(response.text)

    html = etree.HTML(response.text)

    storys = html.xpath("//div[@id='read_tpc']/font/text()")
    story = "\n".join(storys)
    filepath = path + filename + ".txt"
    with open(filepath,"w",encoding='utf-8') as file:
        file.write(story)
    print("download {}".format(filename))
    time.sleep(0.1)

# 判断文件是否需要下载
def check_dlstory(url1,text,auth):
    '''
        判断文件是否需要下载(暂未实现)
    :param url1: 不完整url
    :param text: 标题
    :param auth:
    :return:
    '''
    url = "https://hjd.cdb3.xyz/2048/"+url1
    path = "e:\\temp\\pythontest\\2048comm\\wxxs\\sqyy\\"
    dl_text(url, path,text)

# 获取文件列表
def dl_storylist(url,path_type):
    response = requests.get(url,headers=headers)
    response.encoding = response.apparent_encoding
    # with open(".\\html.txt",'w') as file:
    #     file.write(response.text)
    # list = response.text.split('<tr align="center" class="tr3 t_one">')
    html = etree.HTML(response.text)
    url_list = html.xpath("//tr[@class='tr3 t_one']/td[@class='tal']/a[@class='subject']/@href")
    author_list = html.xpath("//tr[@class='tr3 t_one']/td[@class='tal y-style']/a[@class='bl']")
    text_list = html.xpath("//tr[@class='tr3 t_one']/td[@class='tal']/a[@class='subject']")
    # text_list = html.xpath("//tr[@class='tr3 t_one']/td[@class='tal y-style']/div[@class='f10 gray']")

    print("url_list:",len(url_list),url_list)
    print("author_list:",len(author_list),author_list)
    print("text_list:",len(text_list),text_list)

    i = 0
    for url,text1,author in zip(url_list,text_list,author_list):
        i +=1
        # print("url=",url," ；text=",text1.text)
        if i<=6:
            continue

        # print(url)
        # print(text)
        check_dlstory(url,text1.text,author)



def dl_wenxuexinshang():
    url = "https://hjd.cdb3.xyz/2048/thread.php?fid-102.html"

    response = requests.get(url,headers=headers)
    response.encoding = response.apparent_encoding

    # print(response.text)

    html = etree.HTML(response.text)
    url_list = html.xpath("//tr[@class='f_one tr3']/th/h2/a/@href")
    text_list = html.xpath("//tr[@class='f_one tr3']/th/h2/a/text()")

    print(url_list)
    print(text_list)

    for url,text in zip(url_list,text_list):
        print("url=",url," ；text=",text)



def main():
    # 下载单个文件
    url = "https://hjd.cdb3.xyz/2048/read.php?tid=1960956"
    path = "e:\\temp\\pythontest\\2048comm\\wxxs\\sqyy\\"
    dl_text(url,path,"处男第一次交给了美熟女老师")

if __name__ == "__main__":
    # main()
    dl_storylist("https://hjd.cdb3.xyz/2048/thread.php?fid-103.html",'人妻意淫')

