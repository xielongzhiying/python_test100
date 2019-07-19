# -*- coding: UTF-8 -*-
#斐波那契数列

def fin(x):
    if (x == 0) :
        return 0
    elif (x == 1) :
        return 1
    else :
        return fin(x-1)+fin(x-2)

print(fin(6))
    