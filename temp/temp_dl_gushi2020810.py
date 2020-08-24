# -*- coding: utf-8 -*-
# @time :2020/8/10 12:44
# @Author:老萝卜
# @file:temp_dl_gushi2020810
# @Software:%{PRODUICT_NAME}

'''
    下载1-9年级必背古诗
    https://mp.weixin.qq.com/s/0b1bQFhBZU6n_J30pOp-3g
'''

import requests
from lxml import etree
import regrouphtml as arrangehtml



def get_page(url):
    html = requests.get(url).content.decode("utf-8")
    return html


def save_text(content, filepath):
    with open(filepath, "w", encoding="utf-8") as file:
        file.write(content)


def intercept_text(content):
    start_part = content.find(
        '<section style="max-width: 100%;box-sizing: border-box;font-family: -apple-system-font, BlinkMacSystemFont, &quot;Helvetica Neue&quot;, &quot;PingFang SC&quot;, &quot;Hiragino Sans GB&quot;, &quot;Microsoft YaHei UI&quot;, &quot;Microsoft YaHei&quot;, Arial, sans-serif;letter-spacing: 0.544px;white-space: normal;background-color: rgb(255, 255, 255);overflow-wrap: break-word !important;"><section style="margin-top: 2em;margin-right: auto;margin-left: auto;padding-top: 0.5em;padding-bottom: 0.5em;max-width: 100%;box-sizing: border-box;border-style: solid none none;border-top-width: 1px;border-top-color: rgb(204, 204, 204);font-size: 1em;font-family: inherit;font-weight: inherit;text-decoration: inherit;color: rgb(166, 166, 166);overflow-wrap: break-word !important;"><section style="margin-top: -1.2em;margin-right: 16px;margin-left: 16px;max-width: 100%;box-sizing: border-box;min-height: 1em;list-style-type: none;text-align: center;border-width: initial;border-style: none;border-color: initial;line-height: 1.4;overflow-wrap: break-word !important;"><span style="max-width: 100%;font-size: 16px;box-sizing: border-box !important;overflow-wrap: break-word !important;"><strong style="max-width: 100%;box-sizing: border-box !important;overflow-wrap: break-word !important;"><span style="padding: 8px 23px;max-width: 100%;border-color: rgb(172, 29, 16);color: rgb(255, 255, 255);font-family: inherit;font-weight: inherit;text-decoration: inherit;background-color: rgb(172, 29, 16);box-sizing: border-box !important;overflow-wrap: break-word !important;">部编版一年级（上）',
        0)
    end_part = content.find("伤心秦汉经行处，宫阙万间都做了土。兴，百姓苦；亡，百姓苦。</span></section>") + len(
        "伤心秦汉经行处，宫阙万间都做了土。兴，百姓苦；亡，百姓苦。</span></section>")
    result = content[start_part:end_part]
    print(type(result))
    return result


def get_text(content):
    # str_content = intercept_text(content)
    # print(type(str_content))
    # save_text(str_content, "3.txt")
    html=etree.HTML(content)

    # parser = etree.HTMLParser(encoding="utf-8")
    # selector = etree.parse('./data/lol_1.html', parser=parser)
    # result = etree.tostring(selector)
    # parser = etree.HTMLParser(encoding="utf-8")
    # html=etree.parse(str_content, parser=parser)
    # html = etree.fromstring(str_content)
    # text_list=html.xpath("//text()")
    # save_text("\n".join(text_list),"3.txt")


def get_songlist(content):
    pass


def down_save_song(pages):
    pass


def tempstr():
    str_list=[]
    str1=[str(i) for i in range(1,3)]
    str0='''江南可采莲，莲叶何1田田2，鱼戏莲叶间。
鱼戏莲叶东，鱼戏莲叶西，鱼戏莲叶南，鱼戏莲叶北。  '''
    end=0
    for i in str1:
        start=str0.find(i,end)
        str_list.append(str0[end:start])
        end=start+len(i)
    str_list.append(str0[end:])
    str2="".join(str_list)
    print(str2)

if __name__ == "__main__":
    if True:
        tempstr()
    else:
        url = "https://mp.weixin.qq.com/s/0b1bQFhBZU6n_J30pOp-3g"
        response = get_page(url)
        # save_text(html,"1-1.html")
        # get_text(html)
        # strlist=get_text(html)
        #
        # save_text("\n".join(strlist[1:]),"2.txt")
        ret,body_str=arrangehtml.get_bodystr(response)

        if ret==0:
            str2 = arrangehtml.cut_javascript(body_str)
            str3 = arrangehtml.xpath_body__nojsp_str(str2)
            save_text(str3, "2.html")

        html=etree.HTML(response)

        # text_list=html.xpath("//span/text()")[12:]

        text_list=html.xpath("//section//text()")[9:]
        text_list=text_list[:-32]
        # print(text_list)
        list1 ="\n".join(text_list)
        save_text(list1, "5.txt")
        # text_list=text_list[:-25]
        # text_list=text_list[:-25]
        # # print(text_list.index("【免费领取方式】"),len(text_list))
        # list1 ="\n".join(text_list)
        # save_text(list1, "5.txt")
        list2=list1.split("》\n（")
        list3="》（".join(list2)
        list4 = list3.split("\n）")
        list5 = "）".join(list4)
        list6=list5.split("\n★）")
        list7="★）".join(list6)

        list8=list7.replace("《","\n《")




        save_text(list8,"6.txt")




