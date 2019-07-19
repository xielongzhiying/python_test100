# -*- coding: UTF-8 -*-
#有n个整数，使其前面各数顺序向后移m个位置，最后m个数变成最前面的m个数

n = int(input("n个数"))
m = int(input("后移m位"))
list = []

for i in range(n):
    list.append(input("data:"))

print(list)

for i in range(m):
    for j in range(n-m+1):
        list[i],list[i+j] = list[i+j],list[i]

print(list)