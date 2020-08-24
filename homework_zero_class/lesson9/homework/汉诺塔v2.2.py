# -*- coding: utf-8 -*-
# @time :2020/7/23 20:20
# @Author:老萝卜
# @file:汉诺塔V2.2
# @Software:%{PRODUICT_NAME}
'''
版本更新说明： V2.1 --> v2.2
    1、优化显示排序
'''

'''
汉诺塔游戏，现在有ABC三根柱。要求：将A柱所有的圆盘放到C柱。在移动的过程中可以借助B柱。并且规定大圆盘不能放小圆盘上，每次只能移动一个盘子。用递归的方式来解决汉诺塔问题。
'''


def get_sortstr(a,b,c):
    a_key = list(a.keys())[0]
    b_key = list(b.keys())[0]
    c_key = list(c.keys())[0]
    l1=[a_key + " : " + "、".join(a[a_key]),b_key + " : " + "、".join(b[b_key]),c_key + " : " + "、".join(c[c_key])]
    l1.sort()
    str0=l1[0]+l1[1]+l1[2]
    return str0


def huanruota(level, a, b, c, flag1):
    if level == 1:
        a_key = list(a.keys())[0]
        c_key = list(c.keys())[0]
        a1 = a_key + "的"
        a2 = a[a_key][-1]
        v1 = a[a_key].pop(-1)
        c[c_key].append(v1)
        print(f"将 {a1} 圆盘{a2} 搬到 {c_key}， 调整后：{get_sortstr(a,b,c)}")
    else:
        huanruota(level - 1, a, c, b, True)
        a_key = list(a.keys())[0]
        c_key = list(c.keys())[0]
        a1 = a_key + "的"
        a2 = a[a_key][-1]
        v1 = a[a_key].pop(-1)
        c[c_key].append(v1)
        print(f"将 {a1} 圆盘{a2} 搬到 {c_key}，调整后 {get_sortstr(a,b,c)}")
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
