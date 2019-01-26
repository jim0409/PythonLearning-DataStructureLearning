class A(object):
    bar = 1
    def func1(self):
        print("foo")

    @classmethod
    def func2(cls, *args):
        print('func2') # <1> func2
        print(cls.bar) # <2> 1
        cls().func1() # 使用 A.func1() <3> foo
        print(*args)
    
    @classmethod
    def func3(cls, *args, **kwargs):
        # cls.func2()
        print("the arg input are {}".format(*args))
        for i in kwargs:
            print("the key, value of kwargs are {}, {}".format(i, kwargs[i]))


dict_data = {"key1": "value1", "key2": "value2"}
list_data = {1, 2}

A.func2(1, 2, 3, 4, "list", list_data, "dict", dict_data)

A.func3(1,a=dict_data)