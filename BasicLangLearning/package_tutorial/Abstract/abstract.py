from abc import ABCMeta, abstractmethod


class IStream(object):  # python2 method
    # class IStream(metaclass=ABCMeta): #python3 method
    @abstractmethod
    def read(self, maxbytes=-1):
        # print('interface')
        pass

    @abstractmethod
    def write(self, data):
        pass


class SocketStream(IStream):
    def read(self, maxbytes=-1):
        print('inherent')
        pass

    def write(self, data):
        pass


class SocketStream2(IStream):
    def read(self, maxbytes=-1):
        print('inherent2')
        pass

    def write(self, data):
        pass


a = SocketStream()
a.read()

b = SocketStream2()
b.read()
