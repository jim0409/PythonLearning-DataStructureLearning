# -*- coding: UTF-8 -*-
# 關於'下一個'yield表達柿


def f123():
    yield 1
    yield 2
    yield 3


for item in f123():  # 1, 2, and 3, will be printed
    print(item)


def f13():
    yield 1
    while False:
        yield 2
    yield 3


for item in f13():  # 1 and 3, will be printed
    print(item)


# 使用 send() 方法與生成器函數通信
def func():
    x = 1
    while True:
        y = (yield x)
        x += y


print "================"
geniter = func()
print geniter.next()  # 1
print geniter.send(3)  # 4
print geniter.send(10)  # 14

# yield 的好处
# Python 的老用户应该会熟悉 Python 2 中的一个特性：内建函数 range 和 xrange。其中，
# range 函数返回的是一个列表，而 xrange 返回的是一个迭代器。
#
# 在 Python 3 中，range 相当于 Python 2 中的 xrange；而 Python 2 中的 range 可以用 list(range()) 来实现。


# Python 之所以要提供这样的解决方案，是因为在很多时候，我们只是需要逐个顺序访问容器内的元素。
# 大多数时候，我们不需要「一口气获取容器内所有的元素」。比方说，顺序访问容器内的前 5 个元素，可以有两种做法：
#
# 获取容器内的所有元素，然后取出前 5 个；
# 从头开始，逐个迭代容器内的元素，迭代 5 个元素之后停止。
