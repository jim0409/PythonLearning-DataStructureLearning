#SelectionSort
#在處理temp2的時候必須要先把它歸零, 才能夠確保下次跌代的時候滿足進入if條件才進行互換。
#generate a series of random number
import numpy as np
a = np.random.rand(10)
print(a)
#define the swap function
def swap(value1,value2):
    temp = value2
    value2 = value1
    value1 = temp
    return value1,value2

startCrit = True
while startCrit:
    for index in range(0,len(a)-1):
        temp = a[index]
        temp2 = 0
        for i in range(index+1,len(a)):
            if  a[i] < temp:
                temp=a[i]
                temp2=i
            # print("index = {}, i = {}".format(index,i))
        if index < temp2:
            a[index],a[temp2]=swap(a[index],a[temp2])
    print("finish sort")
    startCrit = False

print(a)