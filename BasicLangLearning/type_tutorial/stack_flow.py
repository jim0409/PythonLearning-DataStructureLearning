# https: // stackoverflow.com/questions/22609272/python-typename-bases-dict

class Base1:
    pass
class Base2:
    pass

class Foo(Base1, Base2):
    bar = 'baz'

    def spam(self):
         return 'ham'

def spam(self):
    return str(self)

body = {'bar': 'baz', 'spam': spam}

Foo = type('Foo', (Base1, Base2), body)

print(Foo)
print(Foo.bar)
print(Foo.spam({0:'1'}))
print(Foo.spam("test"))