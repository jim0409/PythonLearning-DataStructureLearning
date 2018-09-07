# -*- coding: UTF-8 -*-

# iterator在python2與python3有不同的函數可以使用
# 在python2使用yield做iterate
# 1. iterator：迭代器是一種對象，迭代器抽象的是一個“數據流”，是只允許迭代一次的對象。
# 迭代器不斷調用next()
# 方法，則可以一次獲取下一個元素；當迭代器中沒有元素時，調用next()
# 方法拋出StopIteration異常。迭代器的__iter__()
# 方法返回迭代器自身；因此迭代器是可以迭代的
#
# 2. iterator protocol：迭代器協議指的是容器類需要包含一個特殊方法
# 如果一個容器提供了__iter__()
# 方法，並且該方法能返回一個能夠逐個訪問容器內所有元素的迭代器，則我們説該容器類實現了迭代器協議

a_list = [1, 2, 3]


def normalFunction(list):
    for i in a_list:
        print i


normalFunction(a_list)


def func():
    return 1


def gen():
    yield 1


print(type(func))  # <class 'function'>
print(type(gen))  # <class 'function'>

print(type(func()))  # <class 'int'>
print(type(gen()))  # <class 'generator'>


# 迭代器跟一般函數並無明顯不同，最大差別在於返回值。
# 一般函數以return返回，迭代器以yield返回。


# yield 表達式：如果函數中包含yield，則表示該函數是一個函數生成器（非普通函數）
# 實際上，yield只能用於定義生成器函數
def square():
    for x in range(7):
        yield x ** 2


square_gen = square()

for x in square_gen:
    if x > 3:
        print "break at x:{}".format(x)
        break
    print x

# 使用for循環調用iter()函數，獲取一個生成器；而後調用next()函數，將生成器中的下一個值賦予給下一個x；在執行循環。
# 此外，square_gen是有記憶性的。也就是說會紀錄上次迭代的位置，並且在下次執行後繼續執行下一個x。
genitor = square_gen.__iter__()
while True:
    x = genitor.next()
    print "continue x with {}".format(x)

# 生成器的方法
# 生成器有一些方法。调用这些方法可以控制对应的生成器函数；不过，若是生成器函数已在执行过程中，调用这些方法则会抛出 ValueError 异常。
#
# generator.next()：从上一次在 yield 表达式暂停的状态恢复，继续执行到下一次遇见 yield 表达式。
# 当该方法被调用时，当前 yield 表达式的值为 None，下一个 yield 表达式中的表达式列表会被返回给该方法的调用者。
# 若没有遇到 yield 表达式，生成器函数就已经退出，那么该方法会抛出 StopIterator 异常。
# generator.send(value)：和 generator.next() 类似，差别仅在与它会将当前 yield 表达式的值设置为 value。
# generator.throw(type[, value[, traceback]])：向生成器函数抛出一个类型为 type 值为 value 调用栈为 traceback 的异常，
# 而后让生成器函数继续执行到下一个 yield 表达式。其余行为与 generator.next() 类似。
# generator.close()：告诉生成器函数，当前生成器作废不再使用。


# refer
# 1. https://liam0205.me/2017/06/30/understanding-yield-in-python/
# 2. https://eastlakeside.gitbooks.io/interpy-zh/content/Generators/Generators.html
