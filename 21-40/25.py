# -*- coding: UTF-8 -*-
#求1+2!+3!+...+20!的和

def deff(n):
    sum = 1
    for i in range(1,n+1):
        sum *= i
    return sum

sum = 0
for i in range(1,21):
    sum += deff(i)

print(sum)