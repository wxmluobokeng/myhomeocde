# This Python file uses the following encoding: utf-8
import random

def encipher(str,typeid):
    result = ""
    if typeid==1:
        result = encipher_type1(str)
    elif typeid==2:
        pass
    elif typeid == 3:
        pass
    elif typeid == 4:
        pass
    elif typeid == 5:
        pass
    elif typeid == 6:
        pass
    elif typeid == 7:
        pass
    else:
        pass
    return result

def encipher_type1(str):
    len0 = len(str)
    # 对字符串进行切片
    strlist1 = []
    strlist1.append(str[0::7])
    strlist1.append(str[1::7])
    strlist1.append(str[2::7])
    strlist1.append(str[3::7])
    strlist1.append(str[4::7])
    strlist1.append(str[5::7])
    strlist1.append(str[6::7])

    # print(strlist1)
    len1 = int(len0 / 7)
    if (len0 %  7) != 0:
        len1 += 1
        for i in range(7):
            if len(strlist1[i]) < len1:
                strlist1[i] +=" "
        # print(len0,"  ",len1)

    # for i in range(7):
    #     print(strlist[i],"===")

    # random.shuffle(li)   # 将列表随机打乱
    line_sort = [0,1,2,3,4,5,6]
    random.shuffle(line_sort)
    print(line_sort)

    strlist2 = []
    for i in range(7):
        strlist2.append(strlist1[line_sort[i]])

    print(strlist2)
    result = "".join(strlist2)
    print(result)






if __name__ == "__main__":
    str0 = "央视网消息（新闻联播）：中共中央政治局6月29日下午就“深入学习领会和贯彻落实新时代党的组织路线”举行第二十一次集体学习。中共中央总书记习近平在主持学习时强调，组织建设是党的建设的重要基础。党的组织路线是为党的政治路线服务的。我们党要长期执政、永葆活力，团结带领全国各族人民沿着中国特色社会主义道路实现中华民族伟大复兴，最重要的是把党建设得更加坚强有力。新时代党的组织路线为加强党的组织建设提供了科学遵循，为增强党的创造力、凝聚力、战斗力提供了重要保证。我们要毫不动摇坚持和完善党的领导、继续推进党的建设新的伟大工程，贯彻落实好新时代党的组织路线，不断把党建设得更加坚强有力。"
    str0 = "abcdefghijklmnopqrstuvwxyz!@"
    encipher(str0,1)
    # list1 = []
    # list1.append([1,2,3])
    # list1.append([4,5,6])
    # print(list1)