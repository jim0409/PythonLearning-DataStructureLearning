# iter() 用來生成迭代器的函數
# syntax: iter(object[, sentinel])
# 參數：
#   object -- 支持迭代的集合對象
#   sentinel -- 如果傳遞了第二個參數，則參數object必須是一個可調用的對象(如，函數)，此時iter創建一個迭代器對象(object)
#               每次調用這個迭代氣對象的__next__()方法時，都會調用object
# 返回值：
#   返回一個迭代器對象(object)

lst = [1,2,3]
for i in iter(lst):
    print(i)

print(iter(lst))

a = iter(lst)

print(a.__next__)