# -*- coding: UTF-8 -*-
#输出 9*9 乘法口诀表

for i in range(1,10):
    for j in range(i,10):
        print(i,"*",j,"=",i*j ,end=" ")
    print("")
