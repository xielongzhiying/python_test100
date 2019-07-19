# -*- coding: UTF-8 -*-
#输入某年某月某日，判断这一天是这一年的第几天？

list = [31,28,31,30,31,30,31,31,30,31,30,31]

year = int(input("year:"))
month = int(input("month:"))
day = int(input("day:"))
days = 0

if (year % 400 == 0) or ((year % 4 == 0) and (year % 100 != 0)):
    leap = 1
else:
    leap = 0

for i in range(1,month):
    days = days + list[i-1]

print( days + day + leap)



