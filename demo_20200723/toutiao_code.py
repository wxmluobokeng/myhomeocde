#!D:\Program Files\Anaconda3
# -*- coding: utf-8 -*-
import requests
from urllib.parse import urlencode  # 构造url
import time
import os
from hashlib import md5
from lxml import etree
from bs4 import BeautifulSoup
import re
from multiprocessing.pool import Pool


def get_page(offset):
    global headers
    # headers
    headers = {
        'cookie': 'WEATHER_CITY=%E5%8C%97%E4%BA%AC; csrftoken=6ae2b955b45e59a749e6dc65446acbff; ttcid=9b098a659aa54ff399b6ae76bb252b1e27; SLARDAR_WEB_ID=eb1c77c9-a873-4dbb-8c4c-ac124db1cd6c; UM_distinctid=171fd3813a87ed-0be1183a73772d-30607c00-13c680-171fd3813a9e50; sso_auth_status=d824cbb6753cb805f8a44b6c02e6ec7b; sso_uid_tt=5e677205437e3399c080159feb6a5898; sso_uid_tt_ss=5e677205437e3399c080159feb6a5898; toutiao_sso_user=d91c1fbc6b932a9a5c2fa9a111a50069; toutiao_sso_user_ss=d91c1fbc6b932a9a5c2fa9a111a50069; passport_auth_status=81fc37a1830449af18032d4b4796a32b%2C09dffc241bb0f3ec6c656177e0cc0bb6; sid_guard=4dabbd1e48fd80ecdc0973fdce2d1b0c%7C1590904063%7C5184000%7CThu%2C+30-Jul-2020+05%3A47%3A43+GMT; uid_tt=0115b2ab6e9821b54e26ce6c41059d92; uid_tt_ss=0115b2ab6e9821b54e26ce6c41059d92; sid_tt=4dabbd1e48fd80ecdc0973fdce2d1b0c; sessionid=4dabbd1e48fd80ecdc0973fdce2d1b0c; sessionid_ss=4dabbd1e48fd80ecdc0973fdce2d1b0c; _ga=GA1.2.904277146.1590904500; tt_webid=6833011630063027725; tt_webid=6833011630063027725; CNZZDATA1272960458=2004357243-1589089930-https%253A%252F%252Fwww.baidu.com%252F%7C1590932876; __tasessionId=m5pjsml5i1592026825367; s_v_web_id=kbd7o0e4_ERp4SO3y_dOQY_4tb4_8sbP_0AbZGAADrqJ8; tt_scid=eAuATFNHP-crXarEGEJsNDrcAI27CwfojNjh89EE6DQrHcqy2CfAC-YNcpkuMcSv1796',
        'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36',
        'referer': 'https://www.toutiao.com/search/?keyword=%E7%BE%8E%E5%A5%B3',
        'x-requested-with': 'XMLHttpRequest'
    }
    # 加入参数
    params = {
        'aid': ' 24',
        'app_name': ' web_search',
        'offset': offset,
        'format': ' json',
        'keyword': ' 美女',
        'autoload': ' true',
        'count': ' 20',
        'en_qc': ' 1',
        'cur_tab': ' 1',
        'from': ' search_tab',
        'pd': ' synthesis',
        'timestamp': int(time.time())
    }
    url = 'https://www.toutiao.com/api/search/content/?' + urlencode(params)  # 构造url
    url = url.replace('=+', '=')  # 网址根本不一样
    try:
        r = requests.get(url, headers=headers, params=params)
        r.content.decode('utf-8')
        if r.status_code == 200:
            print("r.json()=",r.json())
            return r.json()  # 返回json格式 因为全是字典类型
    except requests.ConnectionError as e:
        print(e)


def get_image(json):  # 获取图片
    if json.get('data'):  # 如果这个存在
        for item in json.get('data'):
            if item.get('title') is None:
                continue  # 如果标题是空值
            title = item.get('title')  # 获取标题
            if item.get('article_url') == None:
                continue
            url_page = item.get('article_url')
            print("url_page=",url_page)
            rr = requests.get(url_page, headers=headers)

            if rr.status_code == 200:
                with open(".\\rr.html", "a+", encoding="utf-8") as file:
                    file.write(rr.text)
                    file.write("\n\n-*20\n\n")
                pat = '<script>var BASE_DATA = .*?articleInfo:.*?content:(.*?)groupId.*?;</script>'
                print("pat=",pat)
                match = re.search(pat, rr.text, re.S)
                print("match=",match)
                if match != None:
                    result = re.findall(r'img src=\\"(.*?)\\"', match.group(), re.S)
                    print("result=",result)
                    yield {
                        'title': title,
                        'image': result
                    }
            else:
                print("rr.status_code=",rr.status_code)


def save_image(content):
    print("len(content)=",len(content),"content=",content)
    # path = '/Users/xx_zheng/work/公众号素材/头条/'  # 目录
    path = 'e:\\temp\\pythontest\\头条\\公众号素材\\'  # 目录
    if not os.path.exists(path):  # 创建目录
        os.mkdir(path)
        os.chdir(path)
    else:
        os.chdir(path)
    # ------------------------------------------

    if not os.path.exists(content['title']):  # 创建单个文件夹
        if '\t' in content['title']:  # 以title为标题创建单个文件夹
            title = content['title'].replace('\t', '')  # 去除特殊符号 不然创建不了文件名称
            os.mkdir(title + '//')
            os.chdir(title + '//')
            print(title)
        else:
            title = content['title']
            os.mkdir(title + '//')  # 创建文件夹
            os.chdir(title + '//')
            print(title)
    else:  # 如果存在
        if '\t' in content['title']:  # 以title为标题创建单个文件夹
            title = content['title'].replace('\t', '')  # 去除特殊符号 不然创建不了文件名称
            os.chdir(title + '//')
            print(title)
        else:
            title = content['title']
            os.chdir(title + '//')
            print(title)
    for q, u in enumerate(content['image']):  # 遍历图片地址列表
        print("u=", u)
        u = u.encode('utf-8').decode('unicode_escape')

        # 先编码在解码 获得需要的网址链接
        #  开始下载
        r = requests.get(u, headers=headers)
        print("u=",u)
        if r.status_code == 200:
            # file_path = r'{0}/{1}.{2}'.format('美女', q, 'jpg')  # 文件的名字和地址，用三目运算符来调试文件夹的名字
            # hexdisgest() 返回十六进制图片
            with open(str(q) + '.jpg', 'wb') as fw:
                fw.write(r.content)
                print(f'该系列----->下载{q}张')
        else:
            print("图片下载失败：status_code=",status_code)


def main(offset):
    json = get_page(offset)
    get_image(json)
    for content in get_image(json):
        try:
            # print(content)
            save_image(content)
        except FileExistsError and OSError:
            print('创建文件格式错误，包含特殊字符串:')
            continue


if __name__ == '__main__':
    # pool = Pool()
    # groups = [j * 20 for j in range(8)]
    # pool.map(main, groups)  # 传offset偏移量
    # pool.close()
    # pool.join()
    main(1)