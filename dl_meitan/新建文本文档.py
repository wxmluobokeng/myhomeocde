import requests
from lxml import etree
import csv

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.13 Safari/537.36",
    "Referer": "https://bj.meituan.com/meishi/",
    "Remote Address": "103.37.152.3:443",
    "Cookie": "IJSESSIONID=okzf9t1ie7kq1xx9gh90amkrh; iuuid=B54E9A637390FFA55F24EF8954ADA9969FB53A1C701760B05136E84998580661; cityname=%E6%AD%A6%E6%B1%89; _lxsdk_cuid=1735d90518744-060cde8273760c-6b131b7e-100200-1735d905188c8; _lxsdk=B54E9A637390FFA55F24EF8954ADA9969FB53A1C701760B05136E84998580661; webp=1; __utma=74597006.1092488506.1595002607.1595002607.1595002607.1; __utmc=74597006; __utmz=74597006.1595002607.1.1.utmcsr=m.baidu|utmccn=m.baidu|utmcmd=organic|utmcct=100001; ci3=1; backurl=http://i.meituan.com/account/?cevent=imt%2Fhomepage%2Fmine; _hc.v=64af396d-9a7e-3a8f-9a91-214c1a785386.1595002650; latlng=30.66136,114.222195,1595003366371; i_extend=C_b1Gimthomepagecategory1394H__a; wm_order_channel=mtib; utm_source=60030; au_trace_key_net=default; openh5_uuid=B54E9A637390FFA55F24EF8954ADA9969FB53A1C701760B05136E84998580661; service-off=0; client-id=41ea1dbc-e69a-480a-b8b2-e079453ac1d8; cssVersion=249f1798; _lx_utm=utm_source%3D60030; uuid=a91b3a09fcec48739aa5.1595005109.1.0.0; mtcdn=K; lat=39.907335; lng=116.476967; ci=1; rvct=1%2C10; __mta=175937821.1595083691965.1595083691965.1595083691965.1; _lxsdk_s=17362a2a4dd-997-3a0-3d%7C%7C1"
}
url = 'https://bj.meituan.com/meishi/b14/'

reponse = requests.get(url,headers=headers)
re = etree.HTML(reponse.text)
res = re.xpath('//div/div[@class="list"]/ul[@class="list-ul"]/li')
for li in res:
    all = li.xpath('./div[@class="img"]/a/text()')
    all_href = requests.get(all)
    all_hrefs = etree.HTML(all_href.text)
    all_hrefss = all_hrefs.xpath('//div[@class="d-left"]/div')
    for div in all_hrefss:
        name = div.xpath('./div[@class="name"]/text()')
        address = div.xpath('./div[@class="address"]/p[0]/text()')
        phone = div.xpath('./div[@class="address"]/p[1]/text()')
        time = div.xpath('./div[@class="address"]/p[2]/text()')

    with open('meituan.csv','w',encoding='utf-8') as f:
        f.write(name,address,phone,time)