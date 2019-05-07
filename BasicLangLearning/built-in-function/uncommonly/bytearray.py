# bytearray() 方法返回一個新字節數列。這個數列裡面的元素是可變的，並且每個元素的值範圍: 0 <= x < 250
# syntax: class bytearray([source[,encoding[,errors]]])
# 參數: 
# 如果source為整數，則返回一個長度為source的初始化數列
# 如果source為字符串，則按照指定的encoding將字符串轉換為字節序列
# 如果source為可迭代類型，則元素必須為[0, 255]中的整數
# 如果source為與buffer接口一致的對象，則此對象也可以被用於初始化bytearray
# 如果沒有輸入任何參數，默認就是初始化數組為0個元素
# 返回值:
# 返回新字節序列

print(bytearray())

print(bytearray([1,2,3]))

print(bytearray('runoob', 'utf-8'))
