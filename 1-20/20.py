# -*- coding: UTF-8 -*-
#一球从100米高度自由落下，每次落地后反跳回原高度的一半；再落下，求它在第10次落地时，共经过多少米？第10次反弹多高

list = []
h = 100
l = h

for i in range(0,11):
    list.append(h)
    h = h / 2

for i in range(1,10):
    l += list[i] * 2

print(l)
print(list[10])


