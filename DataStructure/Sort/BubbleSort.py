#Bubble Sort

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
# while startCrit:
#     for index in range(0, len(a)-1):
#         for i in range(0,len(a)-index-1):
#             if a[i]>a[i+1] :
#                 a[i],a[i+1]=swap(a[i],a[i+1])
#     print("finish sort")
#     startCrit = False
#
# print(a)

while startCrit:
   startCrit = False
   for i in range(0,len(a)-1):
        if a[i]>a[i+1] :
            a[i],a[i+1]=swap(a[i],a[i+1])
            startCrit=True
print("finish sort")

print(a)