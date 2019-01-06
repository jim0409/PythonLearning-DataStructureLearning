# super()用於類別的繼承，調用父類別的一個方法
# super是用來解決多重繼承問題的，直接用類別名稱，調用父類別在使用單繼承的時候沒問題，
# 但是如果使用多繼承，會涉及到查找順序(MRO)，重複調用(鑽石繼承)等種種問題
# MRO就是累的方法解析順序表，其實也就是繼承父類方法時的順序表
# syntax: super(type[, object-or-type])
# 參數:
#   type --- 類
#   object-or-type -- 類，一般是self


class FooParent(object):
    def __init__(self):
        self.parent = 'I\'m the parent.'
        print('Parent')

    def bar(self, message):
        print("%s from Parent" % message)


class FooChild(FooParent):
    def __init__(self):
        # super(FooChild,self) 首先找到 FooChild 的父类（就是类 FooParent），然后把类B的对象 FooChild 转换为类 FooParent 的对象
        super(FooChild, self).__init__()
        print('Child')

    def bar(self, message):
        super(FooChild, self).bar(message)
        print('Child bar fuction')
        print(self.parent)


if __name__ == '__main__':
    fooChild = FooChild()
    fooChild.bar('HelloWorld')
