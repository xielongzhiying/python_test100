# -*- coding: UTF-8 -*-
#利用递归函数调用方式，将所输入的5个字符，以相反顺序打印出来

def out(s):
    if (len(s) <= 1):
        print(s)
    else:
        print(s[-1])
        out(s[:-1])

s = input()
out(s)