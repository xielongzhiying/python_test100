# -*- coding: UTF-8 -*-
#有一个已经排好序的数组。现输入一个数，要求按原来的规律将它插入数组中

L = [1,3,5,7,9]

n = int(input())

for i in range(len(L)):
    if ( n < L[i] ):
        L.insert(i,n)
        break
    elif ( n > L[i]) and ( n < L[i+1] ):
        L.insert(i+1,n)
        break
    else:
        L.append(n)
        break
print(L)


