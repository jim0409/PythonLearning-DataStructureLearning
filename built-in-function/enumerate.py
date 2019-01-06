# enumerate()函數用於將一個可遍歷的數據對象(如列表，元組或字符串)組合為一個索引序列，同時列出數據和數據下標，一般用在for循環中。
# syntax: enumerate(sequence, [start=0])
# 參數：
#   sequence -- 一個序列 迭代器 或其他支持迭代的對象
#   start -- 下標起始位置
# 返回值
#   返回enumerate(枚舉)對象。

seasons = ['Spring', 'Summer', 'Fall', 'Winter']
print("If there is not type for enumerate, it will return object only : {}".format(enumerate(seasons)))
print("Return a list with seasons enumerator : {}".format(list(enumerate(seasons))))

for i in seasons:
    print(i)

for i, element in enumerate(seasons):
    print(i,element)
