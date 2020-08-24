# -*- coding: utf-8 -*-
# @time :2020/7/11 11:01
# @Author:老萝卜
# @file:baidudoc_from_tonydoc_v1.0
# @Software:%{PRODUICT_NAME}

'''
   项目简介： 下载百度文库VIP文章
   参考资料：掘金 lg_Tony博客文章 https://juejin.im/post/5e7b6ae9e51d455c1d67afba
'''

import requests
import re

# 设置会话列表
session = requests.session()


# 请求网址
def get_content_url(url):
    return session.get(url).content.decode('gbk')           # <meta http-equiv="Content-Type" content="text/html; charset=gb2312">


def get_content_type(content):
    return re.findall(r"docType.*?\:.*?\'(.*?)\'\,", content)[0]



def get_content_doc(content):
    result = ''
    url_list = re.findall('(https.*?0.json.*?)\\\\x22}', content)
    # print(url_list)
    url_list = [addr.replace("\\\\\\/", "/") for addr in url_list]
    for url in url_list[:-5]:
        # content = fetch_url(url)       #无此函数
        y = 0
        txtlists = re.findall('"c":"(.*?)".*?"y":(.*?),', content)
        for item in txtlists:
            if not y == item[1]:
                y = item[1]
                n = '\n'
            else:
                n = ''
            result += n
            result += item[0].encode('utf-8').decode('unicode_escape', 'ignore')
    return result


def save_file(filename, content):
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(content)
        print('已保存为:' + filename)

def main():
    # url = input('请输入你要下载文库的URL地址：')
    url="https://wenku.baidu.com/view/2ad62e6e9fc3d5bbfd0a79563c1ec5da51e2d62d.html?fr=search"
    content = get_content_url(url)
    # print(content)
    content_type=get_content_type(content)
    print(content_type)
    content_str=get_content_doc(content)

if __name__ == "__main__":
    main()


