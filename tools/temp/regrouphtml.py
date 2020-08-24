#!D:\Program Files\Anaconda3
# -*- coding: utf-8 -*-
# @Time : 2020/8/10 19:22
# @Author : 老萝卜
# @File : regrouphtml.py
# @Software: PyCharm Community Edition

import requests

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.13 Safari/537.36",
    "Referer": "https://www.mzitu.com/"
}


def get_position(content, start_part, end_part, start):
    find_start = content.find(start_part, start)
    find_end = content.find(end_part, start)
    if find_end != -1:
        find_end += len(end_part)
    if find_start != -1 and find_end != -1:
        result = 0, find_start, find_end
    elif find_start != -1 and find_end == -1:
        result = 1, find_start, find_end
    elif find_start == -1 and find_end != -1:
        result = 2, find_start, find_end
    else:
        result = 3, find_start, find_end
    return result


def get_bodystr(html):
    ret, start, end = get_position(html, "<body", '</body>', 0)
    print(ret, start, end)
    if ret != 0:
        return 1, "非标准body，请检查\n" + html
    return 0, html[start:end]


def cut_javascript(content):
    str_list = []
    bgn = 0
    i = 0
    while True:
        ret, start, end = get_position(content, "<script", '</script>', bgn)
        if ret == 0:  # 有开头也有结尾
            if bgn != start and content[bgn:start].strip() != "":
                str_list.append(content[bgn:start].strip())
        elif ret == 3:  # 没有开头也没有结尾
            if content[bgn:].strip() != "":
                str_list.append(content[bgn:].strip())
            break
        elif ret == 2:  # 没有开头只有结尾
            print(f"请检查参数:{ret},{start},{end})")
            pass
        elif ret == 1:  # 有开头没有结尾
            print(f"请检查参数:{ret},{start},{end})")
            if content[bgn:start].strip() != "":
                str_list.append(content[bgn:start].strip())
            break
        else:
            print(f"不存在参数(get_position函数返回值超范围:{ret},{start},{end})")
            break
        bgn = end
    ret_str = "".join(str_list)
    return ret_str


def xpath_body__nojsp_str(content):
    ret_strlist = []
    tabnum = 0
    tab_con = 1  # 控制是否加1
    str_list = content.split("<")
    for item in str_list:
        if item.strip() == '':
            continue
        if item[0] == "/":
            tabnum = 0 if tabnum == 0 else tabnum - 1
            tab_con = 0
        elif item[0:7] == 'command':
            tab_con = 0
        elif item[0:6] == 'keygen':
            tab_con = 0
        elif item[:5] == "param" or item[:5] == "input" or item[0:5] == 'embed':
            tab_con = 0
        elif item[:4] == "meta" or item[:4] == "link" or item[:4] == "base" or item[:4] == "area":
            tab_con = 0
        elif item[:3] == "img" or item[:3] == "col":
            tab_con = 0
        elif item[:2] == "br" or item[:2] == "hr":
            tab_con = 0
        ret_strlist.append("\n" + "\t" * tabnum + '<' + item.strip())
        tabnum += 1 * tab_con
        tab_con = 1

    ret_str = "".join(ret_strlist)
    with open("3.txt", "a", encoding="utf-8") as file:
        file.write(content)
        file.write("\n\n" + "-" * 30)
        file.write(ret_str)
    return ret_str


def save_text(content, path):
    with open(path, "a", encoding="utf-8") as file:
        file.write(content)


def regrouphtml(html):
    end = 0
    start = html.find('<head>', end)
    html_head = html[0:start]
    end = html.find('</head>', end) + len('</head>')
    head_str = html[start:end]
    print(head_str)

    start = html.find('<body>', end)
    head_body = html[end:start]
    print(head_body)
    end = html.find("</body>", start) + len('</body>')
    body_str = html[start, end]
    body_html = html[end:]


if __name__ == "__main__":
    response = requests.get("https://www.mzitu.com/",headers=headers)
    response.encoding = response.apparent_encoding
#     str0 = '''<html>asdf<head>asdf<javascript>asdf</javascript>asdf</head>asdf<body><div>asdf<img asdf  asdf ><div><meta  qpwerqpweori >123<div>234234234</div></div>567<input ></div>	<script type="text/javascript" src="https://cdn.staticfile.org/jquery/1.8.3/jquery.min.js">
# 	</script>
#
# 	<script type="text/javascript" src="https://cdn.staticfile.org/jquery.lazyload/1.9.1/jquery.lazyload.min.js">
# 	</script>
#
# 	<script type="text/javascript" src="https://www.mzitu.com/static/pc/js.js?0501">
# 	</script>
#
# 	<script type="text/javascript" src="https://static.mediav.com/js/feed_ts.js">
# 	</script>
#
# 	<script type="text/javascript" src="https://www.mzitu.com/static/pc/box.js?0714">
# 	</script>
# </body>asdf</html>'''

    # str_list=str0.split("<")
    # print(str_list)

    ret,str1=get_bodystr(response.text)
    # ret, str1 = get_bodystr(str0)
    if ret == 0:
        str2 = cut_javascript(str1)
        print(str1)

        # str2="img"
        # print(str2[:4])

        str3 = xpath_body__nojsp_str(str2)
        print(str3)
        save_text(str3, "4.html")
        # regrouphtml(response.text)
        # regrouphtml(str0)

        # ret,body_str = get_bodystr(response.text)
        # if ret==0:
        #     save_text(body_str, "1.txt")
        #     body_str_nojsp=cut_javascript(body_str)
        #     save_text(body_str, "2.txt")
        #
        # else:
        #     print(body_str)


# import random
# for i in range(10):
#     print(random.randint(1,2))