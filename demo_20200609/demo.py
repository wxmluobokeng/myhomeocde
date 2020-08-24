'''
   模拟演示：用10次从1000人中，找出感染病毒的那一个人
'''

import random
import pandas as pd

def create_people(n):
    people= [list(range(n)),[0 for i in range(n)]]
    return people

def random_coronavirus(people,n):
    coronavirus = random.randint(0,n)
    people[1][coronavirus] = 1
    print("coronavirus num= ",coronavirus)
    return people


def check_coronavirus(people,num1):
    result = 0
    if len(people[1])<=2:
        if people[1][0]==1:
            result = people[0][0]
        else :
            result = people[0][1]
    else:
        # print(len(people),num1)
        people1=[people[0][:num1],people[1][:num1]]
        people2=[people[0][num1:],people[1][num1:]]
        # print(len(people1),len(people2))
        # print(people1,people2)
        if sum(people1[1])==1:
            people=people1
        else:
            people = people2
        count1 = len(people[1])//2
        result = check_coronavirus(people,count1)
    return result

def main():
    n = 1000
    for i in range(100):
        people = create_people(n)
        affectone_people = random_coronavirus(people,n)
        result = check_coronavirus(affectone_people,len(affectone_people[1])//2)
        print("经检测发现编号为{}的人员感染病毒!".format(result))


if __name__ == "__main__":
    main()
