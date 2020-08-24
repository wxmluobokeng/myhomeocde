'''
    下载 QQ：2604086068  python 服务器的源码
'''

import requests
from lxml import etree

def savefile(url,title):
    rect = requests.get(url)
    rect.encoding = rect.apparent_encoding
    path = "e:/temp/sourcecode/QQ2604086068/"+title
    with open(path,"w",encoding='utf-8') as file:
        file.write(rect.text)


def load_contents():
    with open("e:/temp/sourcecode/QQ2604086068/contents.txt","r",encoding='utf-8') as file:
        strlines = file.readlines()
    codeset = set()
    for item in strlines:
        if item.strip() !="":
            codeset.add(item.strip())
    return codeset

def save_contents(codeset):
    strcode = "\n".join(codeset)
    # print(strcode)
    with open("e:\\temp\\sourcecode\\QQ2604086068\\contents.txt","w+",encoding='utf-8') as file:
        file.truncate()
        file.write(strcode)

def main():
    # path="e:/temp/sourcecode/QQ2604086068"
    url = "http://101.200.72.108:5000/py"
    url_1 = "http://101.200.72.108:5000"

    response = requests.get(url)
    response.encoding = response.apparent_encoding

    print(response.text)
    html = etree.HTML(response.text)

    titles = html.xpath("//a/text()")
    urls = html.xpath("//a/@href")

    print(titles)
    print(urls)

    codeset = load_contents()

    for title,url in zip(titles,urls):
        if len(url)<=2:
          continue
        # print(type(title.strip()))
        str0 = title.strip()
        if str0 in codeset:
            print("11111")
            continue

        url1 = url_1 + url
        savefile(url1,title.strip())
        print("保存代码：",title.strip())
        codeset.add(title.strip())


    if len(codeset)>0:
        save_contents(codeset)


if __name__ == "__main__":
    main()

    range(6)