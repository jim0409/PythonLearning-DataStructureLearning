a = 1

def aplus1():
    global a
    a = a+ 1
    print("a = a + 1")

def aprint():
    global a
    print(a)

aplus1()
aprint()
# 不使用decorator就必須要額外呼叫函數

def use_plus1(func):
    def a_plus1():
        global a
        a = a + 1
        print("a = a + 1")
        return func()
    return a_plus1

@use_plus1
@use_plus1
def a_print():
    global a
    print(a)

a_print()
# 使用decorator可以在函數前面使用`@`提前宣告該函數的before動作

def use_plus_x(var_x):
    def decorator(func):
        def wrapper(*args, **kwargs):
            global a
            a = a + int(var_x)
            print("a = a + {}".format(int(var_x)))
            return func(*args)
        return wrapper
    return decorator

@use_plus_x(var_x=1)
@use_plus_x(var_x='2')
def a_print_x():
    global a
    print(a)

a_print_x()
# 同時decorator函數也可以傳送參數值進入 *注意:最內層調用的函數只能為最外層看到的var_x



# refer : https://foofish.net/python-decorator.html
# import logging

# # Function Version
# def use_logging(func):
#     def wrapper():
#         logging.warn("%s is running" % func.__name__)
#         return func()
#     return wrapper

# @use_logging
# def foo():
#     print("i am foo")

# foo()

# # Parameterzied
# def use_logging(level):
#     def decorator(func):
#         def wrapper(*args, **kwargs):
#             if level == "warn":
#                 logging.warn("%s is running" % func.__name__)
#                 logging.warn("%s" % func.__doc__)
#             elif level == "info":
#                 logging.info("%s is running" % func.__name__)
#             return func(*args)
#         return wrapper
#     return decorator

# @use_logging(level="warn")
# def foo(name='foo'):
#     """
#     foo.__doc__ is ...
#     """
#     print("i am %s" % name)
# foo()

# # Class Version
# class Foo(object):
#     def __init__(self, func):
#         self._func = func

#     def __call__(self):
#         print('class decorator runing')
#         self._func()
#         print('class decorator ending')

# @Foo
# def bar():
#     print('bar')

# bar()
