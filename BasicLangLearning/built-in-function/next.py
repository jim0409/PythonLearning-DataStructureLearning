# next() 返回迭代器的下一個項目
# syntax: next(iterator[, default])
# 參數:
#   iterator --- 可迭代的對象
#   default --- 可選，用於設置在沒有下一個元素時返回該默認值，
#               如果不設置，又沒有下一個元素，則觸發StopIteration異常。
# 返回值:
#   返回對象幫助信息

#!/usr/bin/python
# -*- coding: UTF-8 -*-

# 首先获得Iterator对象:
it = iter([1, 2, 3, 4, 5])
# 循环:
while True:
    try:
        # 获得下一个值:
        x = next(it)
        print(x)
    except StopIteration:
        # 遇到StopIteration就退出循环
        break
