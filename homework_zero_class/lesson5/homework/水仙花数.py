#!D:\Program Files\Anaconda3
# -*- coding: utf-8 -*-
# @Time : 2020/7/11 21:32
# @Author : 老萝卜
# @File : 水仙花数.py
# @Software: PyCharm Community Edition

print("1000以内的水仙花数如下：")
i = 0
while i < 1000 - 1:
    i += 1

    if i < 10:
        mi = 1
    elif i < 100:
        mi = 2
    else:
        mi = 3
    num1 = i % 10
    num2 = i // 10 % 10
    num3 = i // 100
    if i == num1 ** mi + num2 ** mi + num3 ** mi:
        print(f'{i}={num3} ** {mi} + {num2} ** {mi} + {num1} ** {mi}')

print("请问您想求的几位水仙花数：如3位数（100 -- 999）的水仙花数，就输入： 3 ")
while True:         # 循环输入，直到不想测试时，输入
    str_mi = input("请输入您想求的几位水仙花数(1-9之间,q表示退出)： ").strip()
    if str_mi == "q" or str_mi == "Q":
        break
    elif  len(str_mi) != 1 or not (str_mi in "123456789"):         #输入超过1位或不是1-9 ，提示重新输入
        print("请重新输入1-9或q表示退出")
        # print(len(str_mi))
        # print((str_mi in "123456789"))
        continue
    else:
        pass
    mi = int(str_mi)
    num_start = 10 ** (mi - 1)      # 计算起始值
    num_end = 10 ** mi              # 计算最大值+1

    # print(num_start,num_end)
    print_str = []
    i = num_start
    while i < num_end:
        j = 0
        numlist = []            # 存放每个数位上的值
        while j < mi:           # 从个位开始取
            j += 1
            numlist.append(i % (10 ** j) // (10 ** (j - 1)))    # 取第j位上的值 ：先 除 10**j 取余，去掉高位，再整除 10**（j-1）,
        # print(numlist)
        numlist.reverse()   #每个数位上的数倒序，即换成从高位到低位
        num1 = 0
        for item in numlist:
            num1 += item ** mi
        # print(numlist,num1,i)
        if i == num1:
            temp_list = []      #  存放每个数位上打印值，因为每位输出 加上 + ，个位上就会多个 +
            temp_list.append(f"{i} = ")
            for item in numlist:
                temp_list.append(f"{item} ** {mi}")
            print_str.append(temp_list[0]+" + ".join(temp_list[1:]))
        i += 1
    else:
        int0 = len(print_str)
        if int0==0:
            print(f"您想要的{mi}位水仙花数不存在！")
        else:
            print(f"您想要的{mi}位水仙花数有 {int0} 个，分别如下：")
            for k,item in enumerate(print_str):
                print("%4d ： "%(k+1),item)
    print()

