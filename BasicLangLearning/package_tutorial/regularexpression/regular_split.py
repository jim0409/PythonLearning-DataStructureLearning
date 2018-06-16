# split方法按照能夠匹配的字串將字符串分割後返回列表
# syntax:
#   re.split(pattern, string[, maxsplit=0, flags=0])
# par:
#   pattern : 匹配的正則表達式
#   string  : 要匹配的字符串
#   maxsplit: 分隔次數，maxsplit=1 分隔一次，默認為0，不限制次數
#   flags   : 標誌位，用於控制正則表達式的匹配方式，
#             如：是否區分大小寫。多行匹配等等。

import re

m = re.split('\W+', 'runoob, runoob, runoob.')
print(m)

m1 = re.split('(\W+)', ' runoob, runoob, runoob.')
print(m1)

m2 = re.split('\W+', ' runoob, runoob, runoob.', 1)
print(m2)

