# -*- coding: UTF-8 -*-
#时间函数举例

import time

start = time.time()
for i in range(3000):
    print(i)
end = time.time()

print(end - start)