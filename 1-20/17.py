# -*- coding: UTF-8 -*-
#输入一行字符，分别统计出其中英文字母、空格、数字和其它字符的个数。

text = input()

letter = 0
number = 0

for i in range(0,len(text)):
    if (text[i].isnumeric()):
        number += 1
    if (text[i].isalpha()):
        letter += 1
print("number:",number)
print("letter:",letter)