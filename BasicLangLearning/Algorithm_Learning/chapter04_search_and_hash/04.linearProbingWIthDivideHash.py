import random

INDEXBOX = 10
MAXNUM = 7

def print_data(data, max_number): # 列印陣列副程式
    print('\t', end='')
    for i in range(max_number):
        print('[%2d]'%data[i], end='')
    print()

def create_table(num, index): # 建立雜湊表副程式
    tmp = num%INDEXBOX  # 雜湊函數=資料%INDEXBOX
    while True:
        if index[tmp] == -1: # 如果資料對應的位置是空的，則直接存入資料
            index[tmp]=num
            break
        else:
            tmp = (tmp+1)%INDEXBOX

# 主程式
index=[None]*INDEXBOX
data=[None]*MAXNUM

print("origin array value:")
for i in range(MAXNUM): # 起始資料值
    data[i] = random.randint(1, 20)

for i in range(INDEXBOX): # 清除雜湊表
    index[i] = -1

print_data(data, MAXNUM) # 列印起始資料

print("array value:")
for i in range(MAXNUM): # 建立雜湊表
    create_table(data[i], index)
    print('\t\t %2d=>' % data[i], end='') # 列印單一元素的雜湊表位置
    print_data(index, INDEXBOX)

print("finish array")
print_data(index, INDEXBOX) # 列印最後完成結果