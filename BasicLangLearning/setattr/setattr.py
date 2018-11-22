# setattr() 函數對應函數 getattr()，用於設置屬性值，該屬性值必須存在
# http://www.runoob.com/python/python-func-setattr.html
# syntax
# setattr(object, name, value)
# e.g. setattr(a, 'bar', 5)

class A(object):
    bar = 1

a = A()
b = getattr(a, 'bar')

print("Valued b with value a.bar {}".format(b))

# redefine a.bar as 5
setattr(a, 'bar', 5)

print("Now that a.bar 's value would be {}".format(a.bar))
print("Check again that b's value would not be effected {}".format(b))
