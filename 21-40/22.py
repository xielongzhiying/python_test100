# -*- coding: UTF-8 -*-
#两个乒乓球队进行比赛，各出三人。甲队为a,b,c三人，乙队为x,y,z三人。已抽签决定比赛名单。有人向队员打听比赛的名单。a说他不和x比，c说他不和x,z比，请编程序找出三队赛手的名单。


for i in "xyz" :
    for j in "xyz" :
        for k in "xyz" :
            if ( i != j ) and ( i != k ) and ( j != k) and ( i != "x") and (k == "y"):
                print("a--"+i,"b--"+j,"c--"+k)
