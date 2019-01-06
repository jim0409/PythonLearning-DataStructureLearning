# xrange() 語法與range相同。但是返回值不同。range()返回一個值，xrange()返回一個生成器
# syntax: xrange(stop)
#         xrange(start, stop[ ,step])
# 參數:
#   start --- 計數從start開始，默認是從0開始。例如xrange(5)等價於xrange(0, 5)
#   stop --- 計數到stop結束，但不包括stop。例如: xrange(0, 5)是[0, 1, 2, 3, 4]但是不含5
#   step --- 步長，默認為1。例如xrange(0, 5)等價於xrange(0, 5, 1)
# 返回值:
#   返回一個生成器

# 備註：Python3的range及xrange --- xrange只有存在Python2



#!/bin/bash
print(xrange(8))
print(list(xrange(8)))

print(xrange(3,5))
print(list(xrange(3,5)))

print(xrange(0, 6, 2))
print(list(xrange(0, 6, 2)))