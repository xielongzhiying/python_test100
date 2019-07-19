# -*- coding: UTF-8 -*-
#一个5位数，判断它是不是回文数。即12321是回文数，个位与万位相同，十位与千位相同

n = input()

if (n[0] == n[-1]) and (n[1] == n[-2]):
    print("yes")
else:
    print("no")