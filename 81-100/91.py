# -*- coding: UTF-8 -*-
#时间函数举例

import time
print (time.ctime(time.time()))
print (time.asctime(time.localtime(time.time())))
print (time.asctime(time.gmtime(time.time())))