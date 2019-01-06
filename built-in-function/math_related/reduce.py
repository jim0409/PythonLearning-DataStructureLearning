# reduce()函數會對參數序列中元素進行累積。函數將一個數據集合(list或set)中的所有數據進行操作
# 用傳給reduce中的函數function(有兩個參數)先對集合中的第1 & 2個元素進行操作，得到的結果
# 在與第三個數據用function函數運算，最後得到一個結果
# syntax: reduce(function, iterable[, initializer])
# 參數：
# function -- 函數，兩個input參數
# iterable -- 可以迭代的對象
# initializer -- 可選，初始參數

from functools import reduce

def add(x, y):
    return x + y

print(reduce(add, range(1,101)))

# 用lambda func
print(reduce(lambda x, y: x+y, [1,2,3,4,5]))

# 搜尋頻率最高字詞
sentences = ['The Deep Learning textbook is a resource intended to help students and practitioners enter the field of machine learning in general and deep learning in particular. ']
word_count = reduce(lambda a, x: a+x.count("learning"), sentences, 0)
print(word_count)

print("where the answer is the same as {}".format(sentences[0].count("learning")))