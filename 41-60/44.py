# -*- coding: UTF-8 -*-
#两个 3 行 3 列的矩阵，实现其对应位置的数据相加，并返回一个新矩阵

X = [[12,7,3],
    [4 ,5,6],
    [7 ,8,9]]

Y = [[5,8,1],
    [6,7,3],
    [4,5,9]]

R = []

for i in range(3):
    R.append([])
for i in range(3):
    for j in range(3):
        R[i].append( X[i][j] + Y[i][j] )

print(R)