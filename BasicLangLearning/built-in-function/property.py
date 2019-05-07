# property()函數的作用是在新的類別中返回屬性。並且在裝飾法中，表示該屬性不能被更改。
# syntax: class property([fget[, fset[, doc]]])
# 參數
#   fget -- 獲取屬性值的函數
#   fset -- 設置屬性值的函數
#   fdel -- 刪除屬性值的函數
#   doc  -- 屬性描述信息

# 定義一個可控屬性的x
class C(object):
    def __init__(self):
        self._x = None

    def getx(self):
        """
        The doc of getx
        """
        return self._x

    def setx(self, value):
        self._x = value

    def delx(self):
        del self._x

    x = property(getx, setx, delx, "I'm the 'x' property.")

# 當C的物件被創作出來時c = C()
# ，如果呼叫物件下的成員x。會觸發getx, setx 以及 delx
# 如果給定doc參數，其將會成為這個成員的doc_string，
# 否則property函數就會複製fget函數的docstring(如果有在fget裡定義的話)

c =C()
print("For the class member x's doc is : {}".format(C.x.__doc__))
print("However, instance in C as c will have no doc for x.__doc.__ : {}".format(c.x.__doc__))

# set x as value 123
c.setx(123)
# set x as value 123456
c.x = 123456 # x 物件可以被任意賦予值

print("After setting value for x : {}".format(c.getx()))

print("===========================")

# 將Property以裝飾法的方法應用在class裡面
class Parrot(object):
    def __init__(self):
        self._voltage = 100000

    @property
    def voltage(self):
        """Get the current voltage."""
        return self._voltage

ap = Parrot()
# ap.voltage = 1231313  # return error: AttributeError: can't set attribute
print("Note that voltage in Parrot is not callalbe : {}".format(callable(ap.voltage)))
print("The value of ap is : {}".format(ap.voltage))

print("===========================")

# C2和C相同，但是精簡了x的寫法
class C2(object):
    def __init__(self):
        self._x = None

    @property
    def x(self):
        """I'm the 'x' property in C2."""
        return self._x

    # 如果註解該函數，則不能對x任意進行賦予值
    @x.setter
    def x(self, value):
        self._x = value

    # 如果註解該函數，則不能對x賦予值任意進行刪除
    @x.deleter
    def x(self):
        del self._x


c2 = C2()
print("For the class member x's doc is : {}".format(C2.x.__doc__))
print("However, instance in C2 as c2 will have no doc for x.__doc.__ : {}".format(c2.x.__doc__))

# 透過定義x.setter: x物件可以被任意賦予值
setattr(c2, 'x', 123456) # 等同c2.x = 123456
print("After setattr the value of c2.x is : {}".format(c2.x))

# 與 x.deleter: 可以刪除x物件的賦予值
del c2.x
print("After delete x, c2 has no more x : {}".format(hasattr(c2,"x")))
