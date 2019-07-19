# -*- coding: UTF-8 -*-
#一个整数，它加上100后是一个完全平方数，再加上168又是一个完全平方数，请问该数是多少？

import math

for i in range(-100,100000):
    if (math.modf(math.sqrt(i+100))[0] == 0) and (math.modf(math.sqrt(i+100+168))[0] == 0):
        print(i)