# -*- coding: UTF-8 -*-
#打印如下图形

for i in range(1,5):
    for j in range(1,5-i):
        print(end=" ")
    for k in range(1,2*i):
        print("*",end="")
    print("")

for i in range(1,4):
    for j in range(1,i+1):
        print(end=" ")
    for k in range(7-i*2,0,-1):
        print("*", end="")
    print("")