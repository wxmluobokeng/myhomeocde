# -*- coding: utf-8 -*-
# @time :2020/8/6 9:21
# @Author:老萝卜
# @file:dl_nipic_fengjin
# @Software:%{PRODUICT_NAME}

import requests
from lxml import etree
import time


headers={
    "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.105 Safari/537.36"
}


def get_url(url):
    html = requests.get(url, headers=headers)
    html.encoding=html.apparent_encoding
    return html.text

def html_xpath(html,strlist_xpath):
    ret_list=[]
    for str_xpath in strlist_xpath:
        # print("str_xpath=",str_xpath)
        itemlist= html.xpath(str_xpath)
        # print("itemlist=",itemlist)
        # print("len(itemlist)=",len(itemlist))
        ret_list.append(itemlist)
    # print("ret_list=",ret_list)
    return ret_list

def dl_nipic_singlepage(url,strlist_xpath,titlenum):
    response=get_url(url)
    # print(response)
    html = etree.HTML(response)
    item=html_xpath(html,strlist_xpath)
    if item[titlenum][-1]=="下一页":
        for i in range(len(strlist_xpath)):
            item[i]= item[i][:-1]
    # print(item)
    return item

def init_dyadicarray(count):
    ret_list=[]
    for i in range(count):
        ret_list.append([])
    return ret_list

def item_assignment(list1,list2,num1):
    for i in range(num1):
        list1[i]+=list2[i]


def dl_nipic_morepage(url_base,bgnpage,endpage,strlist_xpath,titlenum):
    '''
    下载昵图网图片（多页列表页面）
    :param url_base:不带页码的url，加上页码即为访问页面
    :param bgnpage:开始页面
    :param endpage:结束页面（包含）
    :param strlist_xpath:xpath解析字符串列表
    :return:
    '''
    listnum=len(strlist_xpath)                          # 需要解析字段数量
    ret_list=init_dyadicarray(listnum)                  # 初始化空列表
    for i in range(bgnpage,endpage+1):
        url=url_base+str(i)                             # 生成访问页面
        item=dl_nipic_singlepage(url,strlist_xpath,titlenum)     # 获取单个页面下载列表及title
        item_assignment(ret_list,item,listnum)          # 合并到总列表中
        if i% 100==0:
            print(f"解析到第{i}页了")
        time.sleep(0.1)
    rename_repeat_title(ret_list[titlenum])             # 对title所在列进行重命名
    print(ret_list)


def rename_repeat_title(title_list):
    '''
    对重复名称进行重命名：只有一个不改变，第二个名称后加_1,第三个加_2,以此类推
    :param title_list: 有重复名称列表
    :return: 名称-数量的字典，数量从0开始
    '''
    # 备份列表，进行操作，不删除不影响
    # list_temp=title_list.copy()
    # set1=set()
    # dict={}
    # for i,item in enumerate(list_temp):
    #     if item not in set1:
    #         set1.add(item)
    #         dict[item]=0
    #     else:
    #         dict[item] += 1
    #         title_list[i]=title_list[i]+"_%d"%dict[item]
    # print(title_list)
    set1=set()      # 定义空集合，存放不重名元素
    dict={}         # 定义空字典，存放各元素数量
    for i,item in enumerate(title_list):
        if item not in set1:
            set1.add(item)
            dict[item]=0
        else:
            dict[item] += 1
            title_list[i]=title_list[i]+"_%d"%dict[item]
    # print(title_list)
    return dict


def main():
    # url="http://www.nipic.com/photo/jingguan/ziran/index.html"
    # url_base="http://www.nipic.com/photo/jingguan/ziran/index.html?page="
    # response=get_url(url)
    # print(response)
    # html = etree.HTML(response)
    # # respense = requests.get(url, headers=headers)
    # # respense.encoding = respense.apparent_encoding
    # # print(respense.text)
    # # html=etree.HTML(respense.text)
    #
    # strlist_xpath=["//ul[@class='new-search-result-box clearfix']/li[@class='new-works-box fl']/a/@href","//ul[@class='new-search-result-box clearfix']/li[@class='new-works-box fl']/a/@title"]
    #
    # item=html_xpath(html,strlist_xpath)
    # for i in range(len(strlist_xpath)):
    #     item[i]= item[i][:-1]
    # print(item)

    url_base="http://www.nipic.com/photo/jingguan/ziran/index.html?page="
    strlist_xpath=["//ul[@class='new-search-result-box clearfix']/li[@class='new-works-box fl']/a/@href","//ul[@class='new-search-result-box clearfix']/li[@class='new-works-box fl']/a/@title"]
    dl_nipic_morepage(url_base,1,500,strlist_xpath,1)

    # # 测试 重名
    # list1=[[1,2,3],["a","a","a","b","c","a","a","a","a","a","a","a","b","c","d"]]
    # print("改前list1=", list1)
    # rename_repeat_title(list1[1])
    # print("改后list1=",list1)

    # # 赋值测试
    # listnum=2
    # ret_list = init_dyadicarray(listnum)
    # print("ret_list=",ret_list)
    # item=[[1,2,3,4,5],["a","b","c","d","e"]]
    # item_assignment(ret_list,item,listnum)
    # print(ret_list)
    # print("ret_list=",ret_list)
    # item=[[6,7,8,9],["h","i","j","k"]]
    # item_assignment(ret_list,item,listnum)
    # print("ret_list=",ret_list)


if __name__ == "__main__":
    main()