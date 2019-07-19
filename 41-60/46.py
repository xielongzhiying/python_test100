# -*- coding: UTF-8 -*-
#求输入数字的平方，如果平方运算后小于 50 则退出

n = int(input())

while (n*n >= 50):
    print(n*n)
    n = int(input())