from __future__ import print_function
from StructurePractice.module1.func1 import BeImportFunc as test

class BeImportedClass(object):
    def __init__(self,c1):
        self.__c1 = c1
    def printC1(self):
        return print(self.__c1)
    def upgradeC1(self):
        self.__c1 = test(self.__c1,self.__c1,self.__c1)
        return 0
        # return

# testValue = test(1,2,3)
