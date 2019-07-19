# -*- coding: UTF-8 -*-
#从键盘输入一些字符，逐个把它们写到磁盘文件上，直到输入一个 # 为止


fielname = input("请输入文件名：")
f = open(fielname,"w")

context = input()

while (context != "#") :
    f.write(context)
    context = input()

f.close()
