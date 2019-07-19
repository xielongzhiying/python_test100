# -*- coding: UTF-8 -*-
#有一分数序列：2/1，3/2，5/3，8/5，13/8，21/13...求出这个数列的前20项之和

def fin(n):
    if (n ==1):
        return 1
    if (n ==2):
        return 1
    return fin(n-2)+fin(n-1)

sum = 0

for i in range(1,21):
    sum += fin(i+2)/fin(i+1)

print(sum)