'''
    想法：将网页内容取下来
'''

import requests
from lxml import etree

def test1():
    url = 'https://wenku.baidu.com/view/6ae582845e0e7cd184254b35eefdc8d377ee14d9.html'
    content = requests.get(url)
    # print(content.text)
    with open('.\web1.txt',"w",encoding='utf-8') as f:
        f.write(content.text)

def test2():
    '''
        将整个页面保存到web_test2.txt中
    '''
    url = 'https://www.8yizw.com/21_21201/39243616.html'
    content = requests.get(url)
    content.encoding = content.apparent_encoding
    # print(content.text)
    with open('.\web_test2.txt',"w",encoding='utf-8') as f:
        f.write(content.text)

def test3():
    url = 'https://www.8yizw.com/21_21201/39243616.html'
    header = {
        "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36"
    }
    content = requests.get(url,headers=header)
    content.encoding = content.apparent_encoding
    html = etree.HTML(content.text)
    storys = html.xpath("//div[@id='content']/text()")
    print(type(storys),len(storys))
    for i,str0 in enumerate(storys):
        print(i," =",str0,"======")
    story = "\n".join(storys)
    print(story)
    with open('.\web_test3.txt',"w",encoding='utf-8') as f:
        f.write(story)

def test4():
    '''
        将整个页面保存到web_test2.txt中
    '''
    # url = 'https://www.mzitu.com/'
    url = 'https://www.mzitu.com/zhuanti/'

    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.13 Safari/537.36',
        'Referer': 'https://www.mzitu.com/tag/ugirls/'
    }
    content = requests.get(url,headers=headers)
    content.encoding = content.apparent_encoding
    # print(content.text)
    with open('.\web_test4_1.txt',"w",encoding='utf-8') as f:
        f.write(content.text)


def main():
    # test1()
    print()
    # print("test2()开始......")
    # test2()
    print("test3()开始......")
    test3()
    print("test4()开始......")
    test4()

# https://www.mzitu.com/

if __name__ == "__main__":
    main()
