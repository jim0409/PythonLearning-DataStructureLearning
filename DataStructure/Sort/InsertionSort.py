#Insertion Sort (反向變換)
#正常Insertion是從最後一個元素即 a[len(a)-1]開始比較, 這邊是使用第一個元素進行比較!即 a[0]
#要注意加入元素時加入break跳出, 避免重複加入不必要的元素。
#generate a series of random number
import numpy as np
a = np.random.rand(10)
print(a)

b=[]
b.insert(0,a[0])
# print(len(b))
startCrit = True
while startCrit:
    for index in range(1,len(a)):
        for i in range(0,len(b)):
            if b[i] >= a[index]:
                b.insert(i,a[index])
                break
        if len(b) <= index :
            b.insert(len(b),a[index])

    print("finish sort")
    startCrit = False

print(b)
