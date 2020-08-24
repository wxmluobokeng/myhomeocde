# -*- coding: utf-8 -*-
# @time :2020/7/23 23:01
# @Author:老萝卜
# @file:汉诺塔V2.3
# @Software:%{PRODUICT_NAME}
'''
版本更新说明：V2.2  --> v2.3  可定版
'''

'''
汉诺塔游戏，现在有ABC三根柱。要求：将A柱所有的圆盘放到C柱。在移动的过程中可以借助B柱。并且规定大圆盘不能放小圆盘上，每次只能移动一个盘子。用递归的方式来解决汉诺塔问题。
'''

count1 = 0  # 计数器

def move(num1, a, b, c):
    a_key = list(a.keys())[0]
    b_key = list(b.keys())[0]
    c_key = list(c.keys())[0]
    a2 = a[a_key].pop(-1)
    c[c_key].append(a2)
    l1 = sorted(
        [a_key + " : " + "、".join(a[a_key]), b_key + " : " + "、".join(b[b_key]), c_key + " : " + "、".join(c[c_key])])
    str0 = f"*******第{num1}次搬动：将 {a_key} 圆盘{a2} 搬到 {c_key} \n  搬动后：{l1[0]}\n{' '*10+l1[1]}\n{' '*10+l1[2]}"
    return str0


def huanruota(level, a, b, c):
    global count1
    if level == 1:
        count1 += 1
        print(move(count1, a, b, c))
    else:
        huanruota(level - 1, a, c, b)
        count1 += 1
        print(move(count1, a, b, c))
        huanruota(level - 1, b, a, c)


def main():
    while True:
        print("需要输入汉诺塔的层数数字，如9层，输入数字9，输入q表示放弃即既退出")
        level_str = input("请输入数字(1-9)或 q ：").strip()
        if level_str not in "123456789qQ" or len(level_str) > 1:
            print("请输入正确的数字，层数过大，系统会崩溃的！！！\n")
            continue
        elif level_str == "q" or level_str == "Q" or level_str == "":
            break
        level = int(level_str)
        list1 = []
        for i in range(level, 0, -1):
            list1.append(str(i))
        print("初始状态：A柱：" + "、".join(list1) + "\n" + " " * 10 + "B柱" + "\n" + " " * 10 + "C柱")
        huanruota(level, {"A柱": list1}, {"B柱": []}, {"C柱": []})
        print(f"☺☺☺  已按要求完成{level}层汉诺塔从A柱将所有的圆盘放到C柱 ☺☺☺\n")
        global count1
        count1 = 0


if __name__ == "__main__":
    main()
