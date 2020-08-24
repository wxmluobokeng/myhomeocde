'''
    功能:下载QQ表情包，网站：https://qq.yh31.com/，因网站内有些图片不全，未全部做出来
'''

import requests
from lxml import etree
import time
import os       #判断目录是否存在，创建目录

def check_filedir(filedir,para):
    dir_exist = 0
    if os.path.exists(filedir):
        dir_exist = 1
    elif para == 1:
        os.makedirs(filedir)
        dir_exist = 2
    return dir_exist

# 补齐网址
def additionalurl(url):
    str1=url[:7]
    newurl=url
    if str1!="https://":
        newurl="https://qq.yh31.com" + url
    return newurl

#根据列表中图片信息，下载并保存图片
def saveimg(filelist,filedir):
    num = len(filelist)
    if num == 0:
        print("没有需要下载的图片信息")
    else:
        print("开始下载图片，请等待......")
        i = 0
        for item in filelist:
            if (i+1)%10 == 0:
                print("共{}张图片需要下载，正在下载第{}张".format(num,i+1))
            url1 = item.encode('utf-8').decode('utf-8')
            # img_url = "https://qq.yh31.com" + url1
            img_url=additionalurl(url1)
            urlsplit = url1.split('/')
            # filename = ".\\image\\" + urlsplit[-1]
            filename = filedir + urlsplit[-1]
            img_content = requests.get(img_url).content
            time.sleep(0.1)
            with open(filename, "wb") as f:
                f.write(img_content)
            i +=1
        print("下载已完成，共下载{}张图片!".format(num))


#下载特定页面下的图片
def download_yh31meme(url,dirpath):
    response = requests.get(url)
    response.encoding = response.apparent_encoding      #确保汉字显示正确
    html = etree.HTML(response.text)
    filedir = getfiledir(html,dirpath)
    list1 = html.xpath("//div[@id='fontzoom']/p/img/@src")
    saveimg(list1,filedir)

    nextpage_url = check_mulpage(html)
    if nextpage_url != "" and  nextpage_url != url:
        print("进入下一页......")
        download_yh31meme(nextpage_url, dirpath)

def getfiledir(html,dirpath):
    titles = html.xpath("//div[@class='c_title_text']/text()")
    filedir = dirpath + titles[0]+"\\"
    result = check_filedir(filedir,1)
    return filedir


#判断是否有多页，如果有，返回下一页url，否则返回空
def check_mulpage(html):
    # list1=html.xpath("//div[@id='c_bot_fy']/span[@id='pe100_page_contentpage']/a[@text()='下一页']/@href")
    list1=html.xpath("//span[@id='pe100_page_contentpage']/a[contains(.//text(),'下一页')]/@href")
    # print("list1=",list1)
    ret_url=""
    if len(list1)>=1:
        ret_url=additionalurl(list1[0])
    return ret_url

#获取https://qq.yh31.com/主菜单
def get_mainmenu(url):
    response=requests.get(url)
    response.encoding = response.apparent_encoding
    html=etree.HTML(response.text)
    t = etree.tostring(html, encoding="utf-8", pretty_print=True)
    menu_names = html.xpath("//ul[@id='nav']/li/a/span/text()")
    menu_urls = html.xpath("//ul[@id='nav']/li/a/@href")
    # print("menu_names:",menu_names)
    # print("menu_urls:",menu_urls)
    dict_mainmenu = dict(zip(menu_names,menu_urls))
    # print(dict_mainmenu)
    return dict_mainmenu

def main():
    #下载“喜羊羊QQ表情”，并保存
    # url = "https://qq.yh31.com/zjbq/2920180.html"
    url = "https://qq.yh31.com/zjbq/2820131.html"
    # url = "https://qq.yh31.com/zjbq/2720113.html"

    dirpath=".\\image\\"
    download_yh31meme(url,dirpath)

    # #返回主菜单字典
    # url="https://qq.yh31.com/"
    # get_mainmenu(url)
    '''
        测试向不存在的目录写入文件，会报错
        filename = ".\\wxm\\1.txt"
        with open(filename, "w") as f:
            f.write("wxmwxm")
    '''
    '''
        # # 测试检测目录和创建目录
        # filedir = ".\\wxm\\wwww"            # 等价于  filedir = ".\\wxm\\wwww\\"
        # if os.path.exists(filedir):
        #     print("目录存在")
        # else:
        #         print("目录不存在")
        #         os.makedirs(filedir)
    '''

if __name__ == "__main__":
    main()