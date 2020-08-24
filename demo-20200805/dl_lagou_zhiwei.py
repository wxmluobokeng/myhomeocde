#!D:\Program Files\Anaconda3
# -*- coding: utf-8 -*-
# @Time : 2020/8/13 21:24
# @Author : 老萝卜
# @File : dl_lagou_zhiwei.py
# @Software: PyCharm Community Edition


'''
  学习20200805 逻辑教育Tony老师的《深入剖析招聘网站反爬机制突破网站封锁》
  功能：爬取拉勾网、职位招聘 信息
  主要知识点:
  1、UA、防盗链、长连接、cookie等headers  反爬
  2、session 会话
  3、json 数据
'''

# 反爬分析
'''
    1、网站的目标
    2、分析 - 哪些数据是需要抓取的  
    3、保存 -- ｛根据数据类型保存 ： 小说(txt)  - 工厂报价信息（excel ）｝
    
    https://www.lagou.com/jobs/list_python?px=new&city=%E6%AD%A6%E6%B1%89#order  打开网页显示的地址，但这个地址是转换后的地址，无法直接访问到数据
    通过开发者模式，分析 network / XHR ，会发现  positionAjax.json?px=.....   的 preview  content/ positionResult / result 里面有我们相要的数据
    打开 positionAjax.json?px=...... 的 headers 的 requests Url为
    https://www.lagou.com/jobs/positionAjax.json?px=new&city=%E6%AD%A6%E6%B1%89&needAddtionalResult=false
    Request Method 是 POST
    Form Data是
        first: true
        pn: 1
        kd: python
        
    Get 请求：从服务器直接获取数据，有参数放在url 中 
    Post请求：向服务器发送携带的数据，才能获取数据
    直接访问，连接成功，但会提示访问太频繁，并显示你的IP地址，实际上服务器知道你是爬虫，不是浏览器访问，变相拒绝了你的请求，
    加上post data数据再访问一下,还是同样的效果
    解决办法是伪装成浏览器,用 UA ,发现还是不行，
    通守尝试防盗链、cookie发现都不能成功,(
    cookie是有时效性，实际上，在本网站没什么 ，可以去掉也可保留
    
    通地session会话，保存无法记录信息
    变量tony = requests.session()
    tony.headers.updata(headers)
    content=tony.post(url,data=data)
    result=content.json()       本网站采用json方式保存数据
    现在可能拿得到，也可能拿不到，需要增加一个长连接
    再访问就没问题了
    拿到json数据后，需要一层一层剥到想要的数据列表
    用for 循环遍历取到每个数据项
    
    
    
    
    
    
    
    
    
    
    
    
    

    
'''
import requests

url = "https://www.lagou.com/jobs/positionAjax.json?px=new&city=%E6%AD%A6%E6%B1%89&needAddtionalResult=false"
# 第一步请求
# req=requests.post(url)
# print(req.text)
# # {"status":false,"msg":"您操作太频繁,请稍后再访问","clientIp":"27.17.174.211","state":2408}

data={
    "first": "true",
    "pn": "1",
    "kd": "python"
}

# req=requests.post(url,data=data)
# print(req.text)
# # {"status":false,"msg":"您操作太频繁,请稍后再访问","clientIp":"27.17.174.211","state":2402}

# headers = {
#     "user-agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.13 Safari/53"
# }
# req=requests.post(url,data=data,headers=headers)
# print(req.text)
# # {"status":false,"msg":"您操作太频繁,请稍后再访问","clientIp":"27.17.174.211","state":2402}

# headers={
#     "user-agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.13 Safari/53",
#     # 防盗链：这个请求是从什么地方来的，这个url地址是可以有效的访问地址
#     "referer": "https://www.lagou.com/jobs/list_python?labelWords=&fromSearch=true&suginput=",
#     # cookie : 登录网站时何存在本地的一些状态，有时效性
#     "cookie": "user_trace_token=20200813210619-7ae4ae83-6a74-4bdc-a1b4-d82ef0194beb; _ga=GA1.2.38146609.1597323980; LGUID=20200813210624-dfb32f81-b53a-4121-9887-c2bf60b23820; JSESSIONID=ABAAAECABIEACCA6B31B97A4F5926C7252CA1BA2FD33931; WEBTJ-ID=20200813210713-173e7ee7d6f282-0debac0ac05a9f-6b131b7e-1049088-173e7ee7d704d9; _gid=GA1.2.1844246331.1597324034; RECOMMEND_TIP=true; index_location_city=%E6%AD%A6%E6%B1%89; sajssdk_2015_cross_new_user=1; X_MIDDLE_TOKEN=679ecd274998caaa1db1d4d7b658eb51; _gat=1; LGSID=20200813223758-9221a3ce-7acf-4bc8-ad7a-f14f023586b1; PRE_UTM=m_cf_cpc_baidu_pc; PRE_HOST=www.baidu.com; PRE_SITE=https%3A%2F%2Fwww.baidu.com%2Fbaidu.php%3Fsc.Kf0000K5cNxA6dzipU1cMOQsnEK6IYubhvD%5FUxJG9ivj197T%5FPxXKbh%5FoycE%5Fl%5FrexE2gFemseyMpIcMF5D5KMp2w885QETuO6SIox74pKoCiS7SlCsb9YdCFSyfx4B8%5FBsgn1JI9J%5FL6SHxmURAxAj2-1JCEqa9RU0KTJugJY2uL9-tL7%5Fe6k1hpZEm0CTwNEuG3OMOj7jdInzS2DA49Wwl4MDZ.DY%5FNR2Ar5Od663rj6tJQrGvKD77h24SU5WudF6ksswGuh9J4qt7jHzk8sHfGmYt%5FrE-9kstVerQKz33X8M-eXKBqM764mTT5QNstVLHYS5HvTo5Huk3G4T5MY3IMo9vUt5M8se5gjlSXZ1tT5ot%5FrSEj4e%5Fr1I9qx9sSX1j%5Fose59yFWkvyyyurzE-oo4phgT85R%5FnYQAS1kL20.U1Yk0ZDqs2v4VnL3ErUy%5F0Kspynqn0KY5TaV8UHPSQ1hdo00pyYqnWcd0ATqUvNsT100Iybqmh7GuZN%5FUfKspyfqnHm0mv-b5HnLnfKVIjYknjD4g1DsnHIxnH0YP-t1nHcsg1nvnjD0pvbqn0KzIjY4nHT0mhbqnHRdg1Ddr7tznjwxnWDL0AdW5HDsnj7xnH6dnj01P16LnNtknjFxnH0zg100TgKGujYs0Z7Wpyfqn0KzuLw9u1Ys0A7B5HKxn0K-ThTqn0KsTjYknW0kPWcLPWnL0A4vTjYsQW0snj0snj0s0AdYTjYs0AwbUL0qn0KzpWYs0Aw-IWdsmsKhIjYs0ZKC5H00ULnqn0KBI1Ykn0K8IjYs0ZPl5fK9TdqGuAnquj6VuLG8TsKGuAnqiD4K0Zw9ThI-IjYvndtsg1Ddn0KYIgnqPWnvrjbdn1RsPHmvPjf3PWDLnsKzug7Y5HDdrHT1nWbYP1f1rHT0Tv-b5yDkmvf1myDdnj0sPjT3mW00mLPV5HRkPDfvfW64nY77P1cYwDR0mynqnfKsUWYs0Z7VIjYs0Z7VT1Ys0Aw-I7qWTADqn0KlIjYs0AdWgvuzUvYqn7tsg1Kxn7ts0Aw9UMNBuNqsUA78pyw15HKxn7tYn104nHcvg1fdPjcsP1Ixn0Ksmgwxuhk9u1Ys0AwWpyfqn0K-IA-b5iYk0A71TAPW5H00IgKGUhPW5H00Tydh5H00uhPdIjYs0A-1mvsqn0KlTAkdT1Ys0A7buhk9u1Yk0Akhm1Ys0AwWmvfq0Zwzmyw-5HTvnjcsn6KBuA-b5HRvPjckP1mYnDD3wH-APRD4wjTvrHuKfWujf1R4wRwa0AqW5HD0mMfqn0KEmgwL5H00ULfqnfKETMKY5HcWnan1c1cWnH0sPWR3njRLc1cYnj0WnWfsna3snj0snj0Wninzc10WQinsQW0znjb4PBnsQWbsnWnsn0K3TLwd5HDsPHmvPWcs0Z7xIWYsQWb1g108njKxna3sn7tsQWf4g108nHNxna31nsKBTdqsThqbpyfqn0KWThnqPjfzn1R%26xst%3DTjYknW0kPWcLPWnL0ycqPHmYnWDLPWfsfH97rRmdfH-DP1m4Pb7aPbPjPH-7wDcKT1YknHmdrH01rHf4njmLPWn4nj0vP7tznWNxn07L5TaV8UHPSQ1hdo0KTHL0oUhY1xBt4Vps0gRqnH0dPWmvnW0KIjYkPHbLn1c4PjTY0ydk5H0an0cV0yPC5yuWgLKW0HnvP1mvPWfYrH6%26word%3D%26ck%3D1093.1.67.384.152.384.152.1%26shh%3Dwww.baidu.com%26sht%3D78000241%5F11%5Fhao%5Fpg%26us%3D1.0.1.0.1.0.0%26wd%3D%26bc%3D110101; PRE_LAND=https%3A%2F%2Fwww.lagou.com%2Flanding-page%2Fpc%2Fsearch.html%3Futm%5Fsource%3Dm%5Fcf%5Fcpc%5Fbaidu%5Fpc%26m%5Fkw%3Dbaidu%5Fcpc%5Fhz%5Fd66764%5Fa6033e%5F%25E6%258B%2589%25E5%258B%25BE%25E7%25BD%2591%25E5%2585%25BC%25E8%2581%258C%26bd%5Fvid%3D7694426012673110969; Hm_lvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1597323981,1597324034,1597329473,1597329497; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%22173e7ef5115326-09525481dc7094-6b131b7e-1049088-173e7ef5116419%22%2C%22%24device_id%22%3A%22173e7ef5115326-09525481dc7094-6b131b7e-1049088-173e7ef5116419%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E7%9B%B4%E6%8E%A5%E6%B5%81%E9%87%8F%22%2C%22%24latest_referrer%22%3A%22%22%2C%22%24latest_referrer_host%22%3A%22%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC_%E7%9B%B4%E6%8E%A5%E6%89%93%E5%BC%80%22%7D%7D; TG-TRACK-CODE=index_search; X_HTTP_TOKEN=dd715dc143651924846923795158bb06af1e2e70e0; Hm_lpvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1597329644; LGRID=20200813224048-9c0b98f6-b85c-4dd1-b981-1d6961e1c741; SEARCH_ID=cefbf44e563244cf9b52450fda7e3d4d"
# }
# req=requests.post(url,data=data,headers=headers)
# print(req.text)
# # {"status":false,"msg":"您操作太频繁,请稍后再访问","clientIp":"27.17.174.211","state":2402}

headers={
    "user-agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.13 Safari/53",
    # 防盗链：这个请求是从什么地方来的，这个url地址是可以有效的访问地址
    "referer": "https://www.lagou.com/jobs/list_python?labelWords=&fromSearch=true&suginput=",
    # 长连接
    "content-type": "application/x-www-form-urlencoded; charset=UTF-8"
}

# 容器  --  会话列表
tony = requests.session()
# 刷新 headers
tony.headers.update(headers)
# 偷梁换柱 ： 通地访问 防盗链 ，得到访问信息
tony.get("https://www.lagou.com/jobs/list_python?labelWords=&fromSearch=true&suginput=")
# 第一步请求网络
content=tony.post(url,data=data)
result=content.json()
print(result)
result_info=result["content"]["positionResult"]["result"]

for item in result_info:
    print(item["positionName"],item["companyFullName"],item["salary"])
print(result_info)
