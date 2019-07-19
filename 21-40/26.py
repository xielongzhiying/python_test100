# -*- coding: UTF-8 -*-
#利用递归方法求5!

def deff(n):
    if (n == 1):
        return 1
    else:
        return deff(n-1)*n

print(deff(5))