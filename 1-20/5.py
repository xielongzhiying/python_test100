# -*- coding: UTF-8 -*-
#输入三个整数x,y,z，请把这三个数由小到大输出。

x = int(input("x:"))
y = int(input("y:"))
z = int(input("z:"))

list = [x,y,z]
list.sort()

print(list)