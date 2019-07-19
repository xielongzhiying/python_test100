# -*- coding: UTF-8 -*-
#输入一个奇数，然后判断最少几个 9 除于该数的结果为整数

n = int(input())
i = 10

while ( (i-1) % n != 0):
    i = i * 10

print(len(str(i-1)))