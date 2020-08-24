# -*- coding: utf-8 -*-
# @time :2020/7/23 18:20
# @Author:老萝卜
# @file:汉诺塔V1.0
# @Software:%{PRODUICT_NAME}

'''
汉诺塔游戏，现在有ABC三根柱。要求：将A柱所有的圆盘放到C柱。在移动的过程中可以借助B柱。并且规定大圆盘不能放小圆盘上，每次只能移动一个盘子。用递归的方式来解决汉诺塔问题。
'''

def huanruota(level,a,b,c):
    if level==1:
         print(f"将层圆盘从 {a} 搬到 {c}")
    else:
        huanruota(level-1,a,c,b)
        print(f"将圆盘从 {a} 搬到 {c}")
        huanruota(level-1,b,a,c)



def main():
    while True:
        print("需要输入汉诺塔的层数数字，如9层，输入数字9，输入q表示放弃即既退出")
        level_str=input("请输入数字(1-9)或 q ：").strip()
        if level_str not in "123456789qQ" or len(level_str)>1:
            print("请输入正确的数字，层数过大，系统会崩溃的！！！\n")
            continue
        elif level_str=="q" or level_str=="Q":
            break
        level= int(level_str)
        huanruota(level,"A柱","B柱","C柱")

if __name__=="__main__":
    main()
