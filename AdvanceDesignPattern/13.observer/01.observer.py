class Publisher:
    def __init__(self):
        self.observers = []

    # 增加新的訂閱者
    def add(self, observer):
        if observer not in self.observers:
            self.observers.append(observer)
        else:
            print('Failed to add: {}'.format(observer))
    
    # 刪除既有的訂閱者
    def remove(self, observer):
        try:
            self.observers.remove(observer)
        except ValueError:
            print('Failed to remove: {}'.format(observer))
    
    # 推送廣播給既有的訂閱者
    def notify(self):
        [o.notify(self) for o in self.observers]


# 關注的事件，此處定義是DefaultFormatter
class DefaultFormatter(Publisher):
    def __init__(self, name):
        Publisher.__init__(self)
        self.name = name
        self._data = 0

    def __str__(self):
        return "{}: '{}' has data = {}".format(
            type(self).__name__, self.name, self._data)

    # 定義data這個方法，讓物件可以看到_data的值
    @property
    def data(self):
        return self._data

    # 使用setter這個裝飾法，提供外界修改data的值
    @data.setter
    def data(self, new_value):
        try:
            self._data = int(new_value)
        except ValueError as e:
            print('Error: {}'.format(e))
        else:
            self.notify()


# --------------------------------訂閱區-----------------------------------
class HexFormatter:
    def notify(self, publisher):
        print("{}: '{}' with publisher data {}, has now hex data = {}".format(
            type(self).__name__, publisher.name, publisher.data, hex(publisher.data)))


class BinaryFormatter:
    def notify(self, publisher):
        print("{}: '{}' with publisher data {}, has now bin data = {}".format(
            type(self).__name__, publisher.name, publisher.data, bin(publisher.data)))
# ------------------------------------------------------------------------

def main():
    df = DefaultFormatter('test1')
    print(df)
    print()
    hf = HexFormatter()
    df.add(hf)
    df.data = 3
    print(df)
    print()
    bf = BinaryFormatter()
    df.add(bf)
    df.data = 21
    print(df)
    print()
    df.remove(hf)
    df.data = 40
    print(df)
    print()
    df.remove(hf)
    df.add(bf)

    df.data = 'hello'
    print(df)
    print()
    df.data = 15.8
    print(df)


if __name__ == '__main__':
    main()
