# -*- coding: UTF-8 -*-
#找到年龄最大的人，并输出

person = {"li": 18, "wang": 50, "zhang": 20, "sun": 22}
m = 'li'
for key in person.keys():
    if person[m] < person[key]:
        m = key

print('%s,%d' % (m, person[m]))