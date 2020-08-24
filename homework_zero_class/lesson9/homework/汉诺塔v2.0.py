# -*- coding: utf-8 -*-
# @time :2020/7/23 20:20
# @Author:老萝卜
# @file:汉诺塔V2.0
# @Software:%{PRODUICT_NAME}
'''
版本升级说明： V1.1 --> V2.0
    1、显示搬动顺序
    2、采用字典对柱名和盘号进行存储
    3、显示搬动后各柱盘号
'''

'''
汉诺塔游戏，现在有ABC三根柱。要求：将A柱所有的圆盘放到C柱。在移动的过程中可以借助B柱。并且规定大圆盘不能放小圆盘上，每次只能移动一个盘子。用递归的方式来解决汉诺塔问题。
'''


# def get_string(a, b, c):
#     a_key = list(a.keys())[0]
#     c_key = list(b.keys())[0]
#     c_key = list(c.keys())[0]
#     a_str = a_key + " : " + "、".join(a[a_key])
#     b_str = b_key + " : " + "、".join(b[b_key])
#     c_str = c_key + " : " + "、".join(c[c_key])
#
#     a_int = 0 if a_str[0] == "A" else 1 if a_str[0] == "B" else 2
#     b_int = 0 if b_str[0] == "A" else 1 if b_str[0] == "B" else 2
#     c_int = 0 if c_str[0] == "A" else 1 if c_str[0] == "B" else 2
#
#     # li=["","",""]
#     # l1[a_int]=a_str
#     # l1[b_int]=b_str
#     # l1[c_int]=c_str
#     # str0="、".join(l1)
#
#     return str0


def huanruota(level, a, b, c, flag1):
    # print(f"------------------{flag1}-----------------")
    # print("a=",a)
    # print("b=",b)
    # print("c=",c)
    # print("---------------------")
    if level == 1:
        a_key = list(a.keys())[0]
        c_key = list(c.keys())[0]
        a1 = a_key + "的"
        a2 = a[a_key][-1]
        v1 = a[a_key].pop(-1)
        c[c_key].append(v1)
        print(f"将 {a1} 圆盘{a2} 搬到 {c_key}， 调整后：{a},{b},{c}")
    else:
        huanruota(level - 1, a, c, b, True)
        a_key = list(a.keys())[0]
        c_key = list(c.keys())[0]
        a1 = a_key + "的"
        a2 = a[a_key][-1]
        v1 = a[a_key].pop(-1)
        c[c_key].append(v1)
        print(f"将 {a1} 圆盘{a2} 搬到 {c_key}，调整后 {a},{b},{c}")
        huanruota(level - 1, b, a, c, False)


def main():
    while True:
        print("需要输入汉诺塔的层数数字，如9层，输入数字9，输入q表示放弃即既退出")
        level_str = input("请输入数字(1-9)或 q ：").strip()
        if level_str not in "123456789qQ" or len(level_str) > 1:
            print("请输入正确的数字，层数过大，系统会崩溃的！！！\n")
            continue
        elif level_str == "q" or level_str == "Q":
            break
        level = int(level_str)
        list1 = []
        for i in range(level, 0, -1):
            list1.append(str(i))

        huanruota(level, {"A柱": list1}, {"B柱": []}, {"C柱": []}, "start")


if __name__ == "__main__":
    main()
