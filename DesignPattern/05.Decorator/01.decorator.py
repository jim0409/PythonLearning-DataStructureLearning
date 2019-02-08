class foo(object):
    def f1(self):
        print('original f1')

    def f2(self):
        print('oroginal f2')


class foo_decorator(object):
    def __init__(self, decoratee):
        self.__decoratee = decoratee

    def f1(self):
        print('decorated f1')
        self.__decoratee.f1()

    def __getattr__(self, name):
        return getattr(self.__decoratee, name)


u = foo()
v = foo_decorator(u)

v.f1()
v.f2()
