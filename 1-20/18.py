# -*- coding: UTF-8 -*-
#求s=a+aa+aaa+aaaa+aa...a的值，其中a是一个数字。例如2+22+222+2222+22222(此时共有5个数相加)，几个数相加由键盘控制

a = int(input("a:"))
n = int(input("n:"))
sum = 0

def plus(a,n):
    number = 0
    for i in range(0,n):
        number += a * 10**i
    return number

for i in range(1,n+1):
    sum += plus(a,i)
print(sum)