# tuple() 將列表轉換為元祖
# syntax: tuple(seq)
# 參數：
#   seq --- 要轉換為元祖的序列

a = tuple([1,2,3,4])
print(type(a))

print(a)

b = tuple({1:2,3:4})
print(type(b))

print(b)

aList = [123, 'xyz', 'zara', 'abc']
aTuple = tuple(aList)

print("Tuple elements : {}".format(aTuple))