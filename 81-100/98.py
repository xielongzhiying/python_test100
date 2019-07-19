# -*- coding: UTF-8 -*-
#从键盘输入一个字符串，将小写字母全部转换成大写字母，然后输出到一个磁盘文件"test"中保存

n = input()
n = n.upper()
f = open("98","w")
f.write(n)
f.close()