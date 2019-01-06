# type() 在函數只有一個參數時返回對象的類型，三個參數時返回新的類型對象
# instance() 與 type() 區別:
#   type()不會認為子類別是父類類型，不考慮繼承關係
#   instance()會認為子類型與父類型類似，考慮繼承關係
# 如果要判斷兩個類型是否相同，用instance()
#
# syntax
# e.g   type(object)
#       type(name, bases, dict)
# 參數解釋:
# name   : 類的名稱
# bases  : 基礎的類型別
# dict   : 字典，定義類別內的空間變量

print("Print the type of number 1 : {}".format(type(1)))

print("Print the type of string 'runoob' : {}".format(type('runoob')))

print("Print the type of list [2] : {}".format(type([2])))

# print("Print the type of dcit {0:'zero'} : {}".format( type({0: 'zero'}) ) )
'''
Traceback (most recent call last):
  File "/Users/jimweng/PythonLearning-DataStructureLearning/BasicLangLearning/type_tutorial/type_main.py", line 21, in <module>
    print("Print the type of dcit {0:'zero'} : {}".format( type({0: 'zero'}) ) )
TypeError: unsupported format string passed to type.__format__
'''
print(str(type({0: 'zero'})))


class A:
    pass


class B(A):
    pass


print(isinstance(A(), A))  # 判斷A()是否與A同類型
print(type(A()) == A)     # 判斷A()是否與A同型別
print(isinstance(B(), A))  # 判斷B()是否與A同類型
print(type(B()) == A)     # 判斷B()是否與A同型別


# 自行定義型別
class X(object):
    a = 1


X = type('X', (object,), dict(a=1))  # 產生一個新的類型X
print(X)
