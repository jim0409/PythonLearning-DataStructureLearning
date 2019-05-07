# filter() 用於過濾序列，過濾掉不符合條件的元素，返回由符合條件元素組成的新列表
# 放入兩個參數，第一個為函數，第二個為序列。序列的每個元素作為參數傳遞給函數進行函數判斷
# 然後返回True或False，最後將返回True的元素放到新列表中。

# 備註：python2中返回的是list，python3返回的是iterator

#!/bin/bash

import math
def is_sqr(x):
    return math.sqrt(x) % 1 ==0

newlist = filter(is_sqr, range(1,101))

print(newlist) # 返回一個filter class

for i in newlist:
    print(i,end=',')