# frozenset()返回一個凍結的集合，凍結後集合不能再添加或刪除任何元素
# syntax :
#       class frozenset([iterable])
# 參數:
#   返回新的frozenset對象，如果不提供任何參數，默認會生成空集合

a = frozenset(range(10)) # generate an unvariant set
print(a)

b = frozenset('runoob')
print(b)