import re
import urllib.request

def getdate():
    for i in range(26700,26716):
        url="http://www.risfond.com/case/fmcg/%d"%(i)
        html=urllib.request.urlopen(url).read().decode("utf-8")
        page_list=re.findall('<div class="sc_d_c">(.*?)<span class="sc_d_con">(.*?)</span></div>',html)
        print(page_list)
items=getdate()

# main1=200
