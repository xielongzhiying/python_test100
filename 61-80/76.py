# -*- coding: UTF-8 -*-
#编写一个函数，输入n为偶数时，调用函数求1/2+1/4+...+1/n,当输入n为奇数时，调用函数1/1+1/3+...+1/n

n = int(input())

def ou( n ):
    sum = 0
    for i in range(2,n+1,2):
        sum += 1/i
    return sum

def ji( n ):
    sum = 0
    for i in range(1,n+1,2):
        sum += 1/i
    return sum

if ( n % 2 == 0 ):
    print(ou(n))
else:
    print(ji(n))
