#CountingSort
#適合使用時機. 多個重複的數字在集合中。
#generate a series of random number from 1 to 9
import numpy as np
a = np.random.random_integers(low=1,high=10,size=10)
print(a)
countArray = np.random.random_integers(low=0,high=0,size=10)

for index in range(1,len(a)):
    # print(index)
    countArray[index]=list(a).count(index)  #在這邊因為考量ArraySize所以沒有針對countArray做index -1 的動作~
                                            #利用list.count的功能計算數字出現的次數
sortArray=[]
for index in range(1,10):
    if countArray[index] !=0:
        temp = countArray[index]            #使用temp來存取要複寫的次數
        while temp > 0:
            sortArray.insert(len(sortArray),index)
            temp = temp -1

print(sortArray)