# -*- coding: UTF-8 -*-
#求一个3*3矩阵主对角线元素之和

array = []

for i in range(0,3):
    for j in range(0,3):
        array.append([])
        array[i].append(int(input("number")))

sum = 0
for i in range(0,3):
    sum += array[i][i]

print(sum)