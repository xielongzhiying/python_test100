# -*- coding: UTF-8 -*-
#判断101-200之间有多少个素数，并输出所有素数

def is_su(x):
    for i in range(2,x):
        if (x%i == 0) :
            return -1
    return 0

for i in range(101,201):
    if (is_su(i) == 0):
        print(i)