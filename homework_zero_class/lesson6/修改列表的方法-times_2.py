# -*- coding: utf-8 -*-
# @time :2020/7/15 15:38
# @Author:老萝卜
# @file:修改列表的方法-times_2
# @Software:%{PRODUICT_NAME}



hero = ['钢铁侠','绿巨人','蜘蛛侠']

# s.append() 向列表最后添加元素
print('修改前:',hero)
# hero[3] = 'b' # IndexError: list assignment index out of range
hero.append('绿帽侠')

print('修改后:',hero)

hero = ['钢铁侠','绿巨人','蜘蛛侠']

# s.insert() 向列表中指定的位置插入一个元素 第一个参数 要插入的位置  第二个参数 要插入的元素
hero.insert(2,'绿帽侠') # ['钢铁侠', '绿巨人', '绿帽侠', '蜘蛛侠']

# s.extend() 使用新的序列来扩展当前的序列

hero.extend(['黑寡妇','蚁人'])
print('修改后:',hero)
hero = ['钢铁侠','绿巨人','蜘蛛侠']
hero += ['黑寡妇','蚁人']


# 清空列表
hero.clear()

hero = ['钢铁侠','绿巨人','蜘蛛侠']
# print('修改前:',hero)
# s.pop() 根据索引删除并返回执行的元素

r = hero.pop() # 不传递索引默认删除最后一个
print(r)

#　s.remove() 删除指定值的元素
r = hero.remove('绿巨人')
print(r)

# s.reverse() 用来反转列表
hero = ['钢铁侠','绿巨人','蜘蛛侠']
hero.reverse()
print('修改后:',hero)
# s.sort() 用来对列表中的元素进行排序
lst = list('absgwggewerlanb')
print('修改前:',lst)
lst.sort(reverse=True)
print('修改后:',lst)