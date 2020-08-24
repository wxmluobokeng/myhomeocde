'''
    作者：老萝卜
    日期：2020-06-28 晚
    功能：
    实现思路：
    1、找到图片网址
    2、用bs4进行解析
    3、用 urllib 下载图片

    存在问题：
    1、图片类型未动态获取
    2、图片总页码未获取
    3、文件名含特殊字符时，会出现异常
    4、描述相同时，文件会同名
'''

import requests
from bs4 import BeautifulSoup
from urllib.request import urlretrieve
import time


def down_girlimg(url,path):
    # url = "https://www.buxiuse.com/?cid=2&page=3"
    header = {
        'user-agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.13 Safari/537.36'
    }
    html = requests.get(url,headers = header).content
    # print(html.text)
    soup = BeautifulSoup(html, 'html.parser')
    girls = soup.find_all("img")
    # print(girls)
    for i,girl in enumerate(girls):
        girl_url = girl.get("src")
        image_name = girl.get("alt")   # 文件名可能会出现异常
        urlretrieve(girl_url,path+"\\%s.jpg"%image_name)

def main():
    cid = 2
    cid_name = "大胸妹"
    pagenum = 207+1
    for i in range(1,pagenum):        #应解析出此页码
        url = "https://www.buxiuse.com/?cid=%d&page=%d"%(cid,i)
        path = r"E:\temp\pythontest\buxiuse\%s"%cid_name
        print(i,url,path)
        print("正在下载第 %d 页图片，请稍等....."%i)
        down_girlimg(url,path)
        time.sleep(0.1)                 #降低爬取频次
    print("已完成 %s %d页图片下载"%(cid_name,pagenum-1))


if __name__ == "__main__":
    main()

