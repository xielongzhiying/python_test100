# -*- coding: UTF-8 -*-
#海滩上有一堆桃子，五只猴子来分。第一只猴子把这堆桃子平均分为五份，多了一个，这只猴子把多的一个扔入海中，拿走了一份。第二只猴子把剩下的桃子又平均分成五份，又多了一个，它同样把多的一个扔入海中，拿走了一份，第三、第四、第五只猴子都是这样做的，问海滩上原来最少有多少个桃子？

flag = 0

for i in range(10000):
    sum = i
    for j in range(5):
        if (sum%5 == 1):
            sum = (sum-1)/5*4
            flag += 1
        else:
            flag = 0
            break
    if ( flag == 5 ):
        print(i)
        break


