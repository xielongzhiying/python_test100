# -*- coding: UTF-8 -*-
#有两个磁盘文件A和B,各存放一行字母,要求把这两个文件中的信息合并(按字母顺序排列), 输出到一个新文件C中

f1 = open("99-a","r")
a = f1.read()
f1.close()

f2 = open("99-b","r")
b = f2.read()
f2.close()

l = list(a+b)
l.sort()

f3 = open("99-c","w")
s = ""
f3.write(s.join(l))
f3.close()