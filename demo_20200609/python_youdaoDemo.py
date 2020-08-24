'''
    作者：老萝卜
    版本：V1.0
    日期：2020.6.11
    功能：爬 有道翻译
'''

# 1、导入框架
import requests

# 2、确定url
url = 'http://fanyi.youdao.com/translate_o?smartresult=dict&smartresult=rule'

# 3、请求
result = requests.post(url)

# 4、解析数据
print(result)

# 4、保存数据
