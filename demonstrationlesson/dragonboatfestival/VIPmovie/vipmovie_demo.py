'''
    作者：老萝卜
    日期：2020-06-27 晚
    功能：学习2020年"端午优质录播赠送"之 PythonVIP电影抓取_222610.wmv
    实现思路：
    1、找到想要下载的电影：电影地址，并且可在浏览器内播
        如果是VIP电影，用“全名解析”查看是否能插放，是否是ts流媒体方式
    2、用 https://jx.618g.com?url=网址   打开，找到 ts网址
    3、用代码方式实现批量下载
    4、或用命令方式下载:  ffmpeg -i m3u8网址 -acodec copy -vcodec copy xxxx.mp4
    4、或用命令方式下载:  ffmpeg -i m3u8网址 -vcodec copy -acodec copy xxxx.mp4

    附加知识点：
       多进程下载   Pool
       1、导入  from multiprocessing import Pool
       2、创建进程池;    pool = Pool(进程数量)
       3、进程调用:  pool.apply_async(函数名,args=(参数列表,))   #异步非阻塞
       4、关闭进程池：  pool.close()      # 关闭进程池，表示不能在往进程池中添加进程
       5、释放资源：    pool.join()       # 等待进程池中的所有进程执行完毕，必须在close()之后调用
'''

# 0.导入框架
import requests
from multiprocessing import Pool




def movie(i):
    # 1.确定url
    url = "https://iqiyi.cdn27-okzy.com/20200604/4501_5d4d8659/1000k/hls/40a42e275dd00%04d.ts"%i   #

    # 2.请求
    content = requests.get(url).content

    # 3.保存
    with open(".\\movie_result\\{}".format(url[-10:]),"wb") as file:
        file.write(content)


def main():
    count=2048
    pool = Pool(6)
    for i in range(count):
        pool.apply_async(movie,args=(i,))
        if (i+1) %  10 == 0:
            print("正在下载第%d个ts文件"%i)
    print("已完成%d个ts文件下载"%count)

    pool.close()
    print("已完成  pool.close() ")
    pool.join()
    print("已完成  pool.join() ")

if __name__ == "__main__":
    main()



