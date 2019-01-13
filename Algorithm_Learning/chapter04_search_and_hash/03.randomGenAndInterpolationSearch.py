import random

val = 1
data = [0]*50
for i in range(50):
    data[i] = val
    val = val + random.randint(1, 5)

def interpolation_search(data,val):
    low = 0
    high = 49
    print('Searching ... ')
    while low <= high and val != -1:
        mid = low + int((val-data[low])* (high-low)/(data[high]-data[low])) # 內插法公式
        if val == data[mid]:
            return mid
        elif val < data[mid]:
            print('%d value is located between %d[%3d] and mid value %d[%3d], looking for left hand side' \
                    %(val, low+1, data[low], mid+1, data[mid]))
            high = mid - 1
        
        elif val > data[mid]:
            print('%d value is located between %d[%3d] and mid value %d[%3d], looking for right hand side'
                  % (val, mid+1, data[mid], high+1, data[high]))
            low = mid + 1
    return -1


while True:
    num = 0
    val = int(input('please enter an number between 1-150, and -1 for ending ... :'))
    if val == -1:
        break
    num = interpolation_search(data, val)
    if num == -1:
        print("value [%3d] is not found "%val)
    else:
        print("value [%2d] is found at position [%3d]"%(num+1, data[num]))

print("show data")
for i in range(5):
    for j in range(10):
        print("%3d-%-3d"%(i*10+j+1, data[i*10+j]),end='')
    print()