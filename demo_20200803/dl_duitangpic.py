#!D:\Program Files\Anaconda3
# -*- coding: utf-8 -*-
# @Time : 2020/8/9 17:01
# @Author : 老萝卜
# @File : dl_duitangpic.py
# @Software: PyCharm Community Edition

'''
  学习20200803 逻辑教育Tony老师的《Python爬虫提升数据下载的速度及优化》
  主要知识点:
  1、纯手工爬取 "堆糖"网站的图片
  2、利用线程提升下载速度
  3、模块化思维分解各功能模块
'''

# 网站下载url分析
'''
    分析网站： https://www.duitang.com/search/?kw=%E6%9D%A8%E5%B9%82&type=feed
    页面会动态数据加载:
        打开检查/newwork/XHR,随着鼠标向滚动，会出现不断有新数据下载
        选中一条，打开headers，复制 requests url, 
        https://www.duitang.com/napi/blog/list/by_search/?kw=%E6%9D%A8%E5%B9%82&type=feed&include_fields=top_comments%2Cis_root%2Csource_link%2Citem%2Cbuyable%2Croot_id%2Cstatus%2Clike_count%2Clike_id%2Csender%2Calbum%2Creply_count%2Cfavorite_blog_id&_type=&start=24&_=1596964485958
        在浏览器中找开，会发现:出现很json数据,
        通过观察，会发现 此url加入了很多关键字，通过 & 分隔，删除部分内容后，不会改变核心内容
        limit=24 
        total=3600
        next_start=48
        可修改为:
        https://www.duitang.com/napi/blog/list/by_search/?kw=%E6%9D%A8%E5%B9%82&start=0&limit=1000 
        尝试留下最核心的，建议加上limit参数，设大一点，可以得到网站最大限制
        将上面url放到浏览器中，可以得到新的json数据
        limit=100
        total=3600
        next_start=100
        如果将上面url的start改为100，https://www.duitang.com/napi/blog/list/by_search/?kw=%E6%9D%A8%E5%B9%82&start=100&limit=1000 
        则得到
         limit=100
        total=3600
        next_start=200
        由此可发现，我们能改变start，把3600条数据全拿回来
'''

# 设置线程
'''
   1、导入线程:import threading      # threading模块 是python内置模块
   2、定义线程锁;  thread_lock=threading.BoundedSemaphore(value=最大线程数)   # 最大设置10个线程,启动10个就不再启新线程，直到前面有线程释放
   3、上锁： thread_lock.acquire()
   4、设置线程参数：线程变量名=threading.Thread(target=待启动的函数,args=待启动函数的参数列表)
   5、启动线程：线程变量名.start()
   6、在待启动的函数体内，结束函数，需要释放线程锁：thread_lock.release()
   一般，3-5，会放在一个循环中，待处理函数不要依赖关系
   
'''

import requests
import threading


# 设置线程锁：设置线程最大数量
thread_lock=threading.BoundedSemaphore(value=10)

# 修改之后的url
# url="https://www.duitang.com/napi/blog/list/by_search/?kw=%E6%9D%A8%E5%B9%82&start=0&limit=1000"

# # html=requests.get(url).text
# html=requests.get(url).content.decode("utf-8")          # 需要打开网站的编码格式，把拿到的数据进行解码，否则会出现乱码
# print(html)


# 第一步，请求网络  -  获取网络返回的数据
def get_page(url):
    html = requests.get(url).content.decode("utf-8")  # 需要打开网站的编码格式，把拿到的数据进行解码，否m则出现乱码
    return html


# 第二步：确定要抓取的数据
def pages_all():
    # 容器
    pages = []
    # 修改之后的url
    url = "https://www.duitang.com/napi/blog/list/by_search/?kw=%E6%9D%A8%E5%B9%82&start={}&limit=1000"
    # 循环
    for index in range(0, 2600, 100):  # 从前面解析得知，有3600张，每次最大100张，故从0 开始，每次间隔100，直到3600
        # 格式化字符串
        url_new = url.format(index)
        # print(url_new)
        # 调用第一步
        page = get_page(url_new)
        # 添加元素
        pages.append(page)
        # print(pages)
    return pages


# 第三步：解析此url  ——  提取数据
# "path":"https://c-ssl.duitang.com/uploads/item/202007/11/20200711134331_tgynd.jpg"
# start_part='"path":"'     # url开始部分
# end_part='"'              # url结束
def pic_url(pages):
    url_all_new=[]
    for page in pages:
        urls=find_all_page(page,'"path":"','"')
        # print(urls)
        # 直接全部保存
        url_all_new.extend(urls)
    return url_all_new

# 第四步：解析数据
def find_all_page(page, start_part, end_part):
    all_str=[]
    end = 0
    # 循环 ----- 向下查找
    while page.find(start_part, end) != -1:  # 从开始位置找起始标志，找不到为-1
        start = page.find(start_part, end) + len(start_part)  # 计算出url起始位置
        end = page.find(end_part, start)
        # 切片 截取
        url_str = page[start:end]
        # print(url_str)
        all_str.append(url_str)
    return all_str


# 第五步：保存数据
def download_save(url,name):
    req=requests.get(url)
    path="e:\\temp\\pythontest\\duitang\\"+"杨幂\\"+str(name)+".jpg"       # 建一个目录保存下载的图片
    with open(path,"wb") as file:
        file.write(req.content)
    # 释放线程锁
    thread_lock.release()

if __name__ == "__main__":
    pages = pages_all()
    url_all_new=pic_url(pages)
    numbers=0
    for item in url_all_new:
        numbers+=1
        print("正在下载第{}张图片".format(numbers))
        # download_save(item,numbers)
        # 上锁   监控线程数
        thread_lock.acquire()
        # 设置线程
        tony=threading.Thread(target=download_save,args=(item,numbers))
        # 启动线程
        tony.start()

