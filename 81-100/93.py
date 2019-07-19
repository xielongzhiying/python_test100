# -*- coding: UTF-8 -*-
#时间函数举例

import time

start = time.clock()
for i in range(10000):
    print(i)
end = time.clock()
print('different is %6.3f' % (end - start))