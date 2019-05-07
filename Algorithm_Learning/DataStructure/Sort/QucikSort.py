#QuickSort
#http://jialin128.pixnet.net/blog/post/142927691
#generate a series of random number
import numpy as np
a = np.random.rand(10)
print(a)
#define the swap function
def quick_sort(list): #extra-place
    smaller = []
    bigger = []
    keylist = []

    if len(list) <= 1:
        return list

    else:
        key = list[0] #第一個數為key值
        for i in list:
            if i < key: #比key值小的數
                smaller.append(i)
            elif i > key: #比key值大的數
                bigger.append(i)
            else:
                keylist.append(i)

    smaller = quick_sort(smaller)
    bigger = quick_sort(bigger)
    return smaller + keylist + bigger

print(quick_sort(a))