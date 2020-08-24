#!D:\Program Files\Anaconda3
# -*- coding: utf-8 -*-
# @Time : 2020/8/22 16:52
# @Author : 老萝卜
# @File : test_json_douban.py
# @Software: PyCharm Community Edition

import requests
import json

headers={
    "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.13 Safari/537.36",
    "Referer": "https://movie.douban.com/typerank?type_name=%E5%89%A7%E6%83%85&type=11&interval_id=100:90&action="
}

def main():
    str_num = input("请输入想取排行前多少名？n= ")
    try:
        num=int(str_num)
        if num<=0:
            num/0
    except:
        print("输入数值有误，无法获取")
        return
    start= num if num<20 else 20

    for i in range(start,num+1,20):
        url = "https://movie.douban.com/j/chart/top_list?type=11&interval_id=100%3A90&action=&start="+str(i)+"&limit=20"
               # "https://movie.douban.com/j/chart/top_list?type=11&interval_id=100%3A90&action=&start=20&limit=20"
               # "https://movie.douban.com/j/chart/top_list?type=11&interval_id=100%3A90&action=&start=20&limit=20"
        print(url)
        param={
            "type": "11",
            "interval_id": "100:90",
            "action":"",
            "start": f"{i}",
            "limit": "20"
        }
        # url="https://movie.douban.com/j/chart/top_list?type=11&interval_id=100%3A90&action=&start=40&limit=20"
        print(param)

        response=requests.get(url,headers=headers,params=param)
        list_data=response.json()
        fp =open("豆瓣.json","a",encoding="utf-8")
        json.dump(list_data,fp=fp,ensure_ascii=False)



if __name__=="__main__":
    main()