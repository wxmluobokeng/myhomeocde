'''
    下载 QQ：2604086068 服务器的photo
'''

import requests
from lxml import etree
import time
import os


dl_step=2

def dl_photo(url1, photo_path, maxnum, codeset):
    maxi = maxnum + dl_step
    max_num = maxnum
    errorcount = 0
    errorlist = []
    errlist = []
    print("beginnum=%d；maxi=%d" % (maxnum + 1, maxi))
    for i in range(maxnum + 1, maxi):
        filenname = "{}.jpg".format(i)
        if filenname in codeset:
            print("11111")
            continue
        url = url1 + filenname
        try:
            rect = requests.get(url, timeout=4)
            rect.raise_for_status()
            path = photo_path + "\\{}.jpg".format(i)
            with open(path, "wb") as file:
                file.write(rect.content)
                max_num = i
            codeset.add("{}.jpg".format(i))
            errorlist += errlist
            errlist.clear()
        except Exception as ex:
            print("出现如下异常：%s" % ex)
            print(i, ".jpg 下载失败", " :  ", url)
            if i > maxnum:
                errorcount += 1
                errlist.append(str(i))
        if errorcount > 20:
            break;
        if i % 10 == 0:
            print("已下载到{}:url={}".format(filenname, url))
            time.sleep(0.1)
    save_contents(photo_path, max_num, codeset)
    save_errlist(photo_path, errorlist)


def dl_err_photo(url1, photo_path, errlist):
    errorlist=errlist.copy()
    if len(errlist) > 0:
        for item in errorlist:
            filenname = "{}.jpg".format(item)
            url = url1 + filenname
            try:
                rect = requests.get(url, timeout=4)
                rect.raise_for_status()
                path = photo_path + "\\{}.jpg".format(item)
                with open(path, "wb") as file:
                    file.write(rect.content)
                errlist.remove(item)
                print("dl_err_photo:try:errlist=",errlist,item)
            except Exception as ex:
                print("出现如下异常：%s" % ex)
                print(item, ".jpg 下载失败", " :  ", url)
        save_errlist(photo_path, errlist)


def load_contents(photo_path):
    with open(photo_path + "\\contents.txt", "r", encoding='utf-8') as file:
        strlines = file.readlines()
    codeset = set()
    max_num = 0
    if len(strlines) > 0:
        max_num = int(strlines[0])
    for i in range(1, len(strlines)):
        item = strlines[i]
        if item.strip() != "":
            codeset.add(item.strip())
    return max_num, codeset


def load_errlist(photo_path):
    ret_list=[]
    filename = photo_path + "\\errorlist.txt"
    if os.path.exists(filename):
        with open(filename, "r", encoding='utf-8') as file:
            list1 = file.readlines()
        for item in list1:
            item.replace("\n","")
            if item.strip()!="":
                ret_list.append(item.strip())
    return ret_list


def save_contents(photo_path, max_num, codeset):
    strcode = str(max_num) + "\n" + "\n".join(codeset)
    # print(strcode)
    with open(photo_path + "\\contents.txt", "w+", encoding='utf-8') as file:
        file.truncate()
        file.write(strcode)


def save_errlist(photo_path, errlist):
    print("save_errlist:errlist=",errlist)
    if len(errlist) > 0:
        strcode = "\n".join(errlist) + "\n"
        # print(strcode)
        with open(photo_path + "\\errorlist.txt", "w+", encoding='utf-8') as file:
            file.truncate()
            file.write(strcode)
    else:
        with open(photo_path + "\\errorlist.txt", "w", encoding='utf-8') as file:
            file.write("")


def main():
    # path="e:/temp/sourcecode/QQ2604086068"
    # url = "http://101.200.72.108//static/zyx"
    # photo_path="E:\\temp\pythontest\\QQ2604086068_server\\static\\zyx"
    # photo_path="E:\\temp\pythontest\\QQ2604086068_server\\static\\zyx2"
    # photo_path="E:\\temp\pythontest\\QQ2604086068_server\\static\\ycc"
    # photo_path="E:\\temp\pythontest\\QQ2604086068_server\\static\\img"
    # maxnum,codeset = load_contents(photo_path)
    # 只下载2个列表
    # urllist = ["http://101.200.72.108//static/zyx/", "http://101.200.72.108//static/zyx2/"]
    # photopathlist = ["E:\\temp\pythontest\\QQ2604086068_server\\static\\zyx",
    #                  "E:\\temp\pythontest\\QQ2604086068_server\\static\\zyx2"]
    urllist = ["http://101.200.72.108/static/zyx/", "http://101.200.72.108/static/zyx2/",
               "http://101.200.72.108/static/ycc/", "http://101.200.72.108/static/img/",
               "http://101.200.72.108/static/img2/"]
    photopathlist = ["E:\\temp\pythontest\\QQ2604086068_server\\static\\zyx",
                     "E:\\temp\pythontest\\QQ2604086068_server\\static\\zyx2",
                     "E:\\temp\pythontest\\QQ2604086068_server\\static\\ycc",
                     "E:\\temp\pythontest\\QQ2604086068_server\\static\\img",
                     "E:\\temp\pythontest\\QQ2604086068_server\\static\\img2"]

    for url, photo_path in zip(urllist, photopathlist):
        errorlist = load_errlist(photo_path)
        print("errorlist=", errorlist)
        dl_err_photo(url, photo_path, errorlist)
        maxnum, codeset = load_contents(photo_path)
        dl_photo(url, photo_path, maxnum, codeset)


if __name__ == "__main__":
    main()
    # photo_path="E:\\temp\pythontest\\QQ2604086068_server\\static\\zyx"
    # errorlist = load_errlist(photo_path)
    # print("load_errlist:errorlist=",errorlist)
    # if len(errorlist)==0:
    #     errorlist+=["1","2","3","4","9000"]
    # url="http://101.200.72.108/static/zyx/"
    # dl_err_photo(url, photo_path, errorlist)

