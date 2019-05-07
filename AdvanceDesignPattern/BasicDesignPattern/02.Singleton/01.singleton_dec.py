def Singleton(cls):
    _instance = {}

    def _singleton(*args, **kwargs):
        if cls not in _instance:
            _instance[cls] = cls(*args, **kwargs)
        return _instance[cls]

    return _singleton


# use singleton base on decorator
@Singleton
class A(object):
    a = 1

    def __init__(self, x=0):
        self.x = x


a1 = A(2)
a2 = A(3)

print(a1.x)
print(a1)
print(a2.x)
print(a2)

'''
2
<__main__.A object at 0x7f5180059a20>
2
<__main__.A object at 0x7f5180059a20>
'''
