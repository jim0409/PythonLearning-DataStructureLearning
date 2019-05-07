# -*- coding: utf-8 -*-

# # basestring() 函數 -- python2函數，python3已被移除
# 描述
# basestring()方法是str和unicode的超類(父類)，也是抽象類別。
# 因此不能被調用和實例化，但可以用來判斷一個對象是否為str或是unicode的實例。
# 例如:
#     isinstance(obj, basestring)
#     等價於
#     isinstance(obj, (str, unicode))

# syntax:
#     basestring()

# parameters:
#     None

# return_value:
#     None


print(isinstance("hello world", str))
# True

print(isinstance("hello world", basestring))
# True

print(isinstance("hello world", (str, unicode)))
# True
