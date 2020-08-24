'''
    功能：下载小说
'''

import requests
from lxml import etree
import time
import pinyin

headers = {
    "user-agent":"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.13 Safari/537.36"
}

def filename_convert(filename_old):
    filename_new =filename_old.replace("<","˂")
    filename_new =filename_new.replace(">", "˃")
    filename_new =filename_new.replace("/", "／")
    filename_new =filename_new.replace("\\", "∖")
    filename_new =filename_new.replace("|", "│")
    filename_new =filename_new.replace(":", "：")
    filename_new =filename_new.replace("\"", "“")
    filename_new =filename_new.replace("*","×")
    filename_new=filename_new.replace("?", "？")
    return filename_new

def get_filename_jp(filename):
    filename_new = filename_convert(filename)
    result=pinyin.get_initial(filename_new, delimiter="").upper()
    return result

def letter_encrypt(str_old):
    len0 = len(str_old)
    if len0 == 0:
        str_new=""
    else:
        if len0 % 7 ==0:
            str_temp= str_old
        else:
            str_temp = str_old + " " * (7 - (len0 % 7))
        item = []
        item.append(str_temp[1::7])
        item.append(str_temp[4::7])
        item.append(str_temp[0::7])
        item.append(str_temp[5::7])
        item.append(str_temp[2::7])
        item.append(str_temp[6::7])
        item.append(str_temp[3::7])
        str_new="".join(item)
    return str_new

def letter_decrypt(str_old):
    len0 = len(str_old)
    if len0 == 0:
        str_new=""
    else:
        if len0 % 7 ==0:
            str_temp= str_old
        else:
            str_temp = str_old + " " * (7 - (len0 % 7))
        item = []
        item.append(str_temp[2::7])
        item.append(str_temp[0::7])
        item.append(str_temp[4::7])
        item.append(str_temp[6::7])
        item.append(str_temp[1::7])
        item.append(str_temp[3::7])
        item.append(str_temp[5::7])
        str_new="".join(item)
    return str_new


#下载文件
def dl_text(url,path,filename):
    '''
        下载文档内容
        :param url: 网址
        :param path: 文件名称
        :return:
    '''
    response = requests.get(url,headers=headers)
    response.encoding = response.apparent_encoding

    html = etree.HTML(response.text)

    storys = html.xpath("//div[@id='read_tpc']/font/text()")

    print("storys=",storys)
    storys1=[]
    for item in storys:
        storys1.append(letter_encrypt(item))

    print("storys1=",storys1)
    story = "\n".join(storys1)
    filepath = path + filename + ".txt"
    with open(filepath,"w",encoding='utf-8') as file:
        file.write(story)
    print("download {}".format(filename))
    time.sleep(0.1)

# 判断文件是否需要下载
def check_dlstory(url1,text,auth):
    '''
        判断文件是否需要下载(暂未实现)
    :param url1: 不完整url
    :param text: 标题
    :param auth:
    :return:
    '''
    url = "https://hjd.cdb3.xyz/2048/"+url1
    path = "e:\\temp\\pythontest\\2048comm\\wxxs\\sqyy\\"
    dl_text(url, path,text)

# 获取文件列表
def dl_storylist(url,path_type,firtpage):
    response = requests.get(url,headers=headers)
    response.encoding = response.apparent_encoding
    # with open(".\\html.txt",'w') as file:
    #     file.write(response.text)
    # list = response.text.split('<tr align="center" class="tr3 t_one">')
    html = etree.HTML(response.text)
    with open("e:\\temp\\pythontest\\2048comm\\wxxs\\sqyy\\html.txt","w",encoding='utf-8') as file:
        file.write(response.text)

    '''
    <tbody style="table-layout:fixed;">
                    <tr class="tr2">
                        <td style="width:2%" class="tac y-style"></td>
                        <td></td>
                        <script language="JavaScript">
                            var orderThreadsClass =
                            {
                                orderThreads : function(orderway)
                                {
                                    var orderway = orderway || 'lastpost';
                                    var form = document.createElement("form");
                                    form.action = "thread.php?fid=103&page=1&";
                                    form.method = "post";
                                    var h_type = this.createInput("hidden","type","0");
                                    var h_search = this.createInput("hidden","search","1000");
                                    var h_special = this.createInput("hidden","special","0");
                                    var h_orderway = this.createInput("hidden","orderway",orderway);
                                    var h_asc = this.createInput("hidden","asc","DESC");
                                    form.appendChild(h_type);
                                    form.appendChild(h_search);
                                    form.appendChild(h_special);
                                    form.appendChild(h_orderway);
                                    form.appendChild(h_asc);
                                    document.body.appendChild(form);
                                    setTimeout(function(){/*ie6*/form.submit();},0);
                                    return false;
                                },
                                createInput : function(type,name,value)
                                {
                                    var hidden = document.createElement("input");
                                    hidden.type = type;
                                    hidden.name = name;
                                    hidden.value = value;//↓
                                    return hidden;
                                }
                            }
                            function orderThreads(orderway)
                            {
                                orderThreadsClass.orderThreads(orderway);
                            }
                        </script>
                        <td style="width:120px;" class="y-style">作者</td>
                        <td style="width:80px" class="tal y-style">回复</td>
                        <td style="width:120px;" class="y-style">最后发表</td>
                    </tr>
                    <tr align="middle" class="tr3 t_one">
                        <td class="tac"><img src="images/wind/thread/anc.gif"/></td>
                        <th>&nbsp站点公告: <a href="notice.php?fid=#47" class="black">2020.6.14 地址發佈頁已更新，请尽快收藏.</a></th>
                        <td class="tal y-style"><a href="u.php?action=show&username=admin" class="bl">admin</a></td>
                        <td class="tal y-style"><a href="notice.php?fid=103#136">站点公告</a></td>
                        <td class="y-style f10">2019-05-02 08:15</td>
                    </tr>
                    <tr align="center" class="tr3 t_one">
                        <td><a title="开放主题" href="read.php?tid-2301176.html" target="_blank">⊙</a></td>
                        <td class="tal" id="td_2301176">[06-30]
                            <img src="images/wind/file/headtopic_3.gif" align="absmiddle" title="置顶帖标志"/>
                            <a  href="read.php?tid-2301176.html" target="_blank" id="a_ajax_2301176" class="subject">
                                <b><font color=#0000FF>本站推荐：抖音短视频平台 快速播放 高清体验 国产首发</font></b>
                            </a>&nbsp;
                        </td>
                        <td class="tal y-style">
                            <a href="u.php?action=show&uid=1225617" class="bl">當頭棒喝</a>
                            <div class="f10 gray">2020-06-30</div>
                        </td>
                        <td class="tal y-style f10 gray"><span class="s3">0</span></td>
                        <td class="tal y-style">
                            <a href="read.php?tid-2301176-page-e-fpage-1.html#a">當頭棒喝</a><br/>
                            <span class="f10 gray">2020-06-30 19:15</span>
                        </td>
                    </tr>        ......
        <tr align="center" class="tr3 t_one">
            <td><a title="开放主题" href="read.php?tid-2032556.html" target="_blank">⊙</a></td>    #第一列
            <td class="tal" id="td_2032556">[04-19]
                <a href="read.php?tid-2032556.html" target="_blank" id="a_ajax_2032556" class="subject">我到底是个怎样的女孩</a>&nbsp;
            </td>
            <td class="tal y-style">
                <a href="u.php?action=show&uid=74212" class="bl">wodelang</a>   #作者
                <div class="f10 gray">2020-04-19</div>                                              #发表时间
            </td>
            <td class="tal y-style f10 gray"><span class="s3">0</span></td>                         #回复数量
            <td class="tal y-style">                                                                #最后发表
                <a href="read.php?tid-2032556-page-e-fpage-1.html#a">wodelang</a><br/>              #发表人帐号
                <span class="f10 gray">2020-04-19 11:50</span>                                      #发表时间
            </td>
        </tr>
        ......
    '''

    if  firtpage:
        bgn_num1=6
        bgn_num2=14
    else:
        bgn_num1 = 0
        bgn_num2 = 0


    url_list = html.xpath("//tbody[@style='table-layout:fixed;']/tr[@class='tr3 t_one']/td[@class='tal']/a[@class='subject']/@href")[bgn_num1:]           #丢掉前5个
    oprname_list = html.xpath("//tbody[@style='table-layout:fixed;']/tr[@class='tr3 t_one']/td[@class='tal y-style']/a/text()")[bgn_num2:]             #丢掉前5个
    # author_list = html.xpath("//tbody[@style='table-layout:fixed;']/tr[@class='tr3 t_one']/td[@class='tal y-style']/a[@class='bl']")[6:]            #丢掉前5个
    text_list = html.xpath("//tbody[@style='table-layout:fixed;']/tr[@class='tr3 t_one']/td[@class='tal']/a[@class='subject']") [bgn_num1:]                 #丢掉前5个
    # text_list = html.xpath("//tr[@class='tr3 t_one']/td[@class='tal y-style']/div[@class='f10 gray']")

    author_list=oprname_list[0::2]
    lastopr_list=oprname_list[1::2]

    print("url_list:",len(url_list),url_list)
    print("author_list:",len(author_list),author_list)
    print("lastopr_list:",len(lastopr_list),lastopr_list)
    print("text_list:",len(text_list),text_list)
    #
    # i = 0
    for url1,text1 in zip(url_list,text_list):
        # print(url1)
        # print(text1.text)
        check_dlstory(url1,get_filename_jp(text1.text),"")



def dl_wenxuexinshang():
    url = "https://hjd.cdb3.xyz/2048/thread.php?fid-102.html"

    response = requests.get(url,headers=headers)
    response.encoding = response.apparent_encoding

    # print(response.text)

    html = etree.HTML(response.text)
    url_list = html.xpath("//tr[@class='f_one tr3']/th/h2/a/@href")
    text_list = html.xpath("//tr[@class='f_one tr3']/th/h2/a/text()")

    print(url_list)
    print(text_list)

    for url,text in zip(url_list,text_list):
        print("url=",url," ；text=",text)



def main():
    # 下载单个文件
    url = "https://hjd.cdb3.xyz/2048/read.php?tid=1960956"
    path = "e:\\temp\\pythontest\\2048comm\\wxxs\\sqyy\\"
    dl_text(url,path,"1")

if __name__ == "__main__":
    main()
    # dl_storylist("https://hjd.cdb3.xyz/2048/thread.php?fid-103-page-4.html",'rqyy',False)       #不是第一页
    # dl_storylist("https://hjd.cdb3.xyz/2048/thread.php?fid-103.html",'rqyy',True)             #第一页
    # str0="0123"
    # str1=letter_encrypt(str0)
    # str2=letter_decrypt(str1)
    # print(str0)
    # print(str1)
    # print(str2)
