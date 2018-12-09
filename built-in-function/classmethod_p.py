class A(object):
    bar = 1
    def func1(self):
        print("foo")
    @classmethod
    def func2(cls,*arg):
        print('func2') # <1> func2
        print(cls.bar) # <2> 1
        cls().func1() # 使用 A.func1() <3> foo
        print(*arg)

A.func2(1)