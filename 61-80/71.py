# -*- coding: UTF-8 -*-
#编写input()和output()函数输入，输出5个学生的数据记录

L = []

def input_st(st):
    s = []
    s.append(input("number"))
    s.append(input("name"))
    s.append(int(input("score")))
    s.append(int(input("score")))
    st.append(s)

def output_st(st):
    for i in range(len(st)):
        print(st[i][0],end='  ')
        print(st[i][1])
        print(st[i][2])
        print(st[i][3])

for i in range(2):
    input_st(L)

output_st(L)