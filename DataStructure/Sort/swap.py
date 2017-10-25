#define the swap function
class swap:
    def __init__(self,value1,value2):
        self.__value1 = value1
        self.__value2 = value2
        self.__temp = 0
    def swap(self):
        self.__temp = self.__value2
        self.__value2 = self.__value1
        self.__value1 = self.__temp
        return self.__value1,self.__value2

# a=swap(10,12)
# a=a.swap()
# print(a)