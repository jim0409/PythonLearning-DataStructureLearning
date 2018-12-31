import random

val = 0
data = [0] * 80

for i in range(80):
    data[i] = random.randint(1, 15)


def bin_search(data, val):
    low = 0
    high = 49
    while low <= high and val != -1:
        mid = int((low + high) / 2)
        if val < data[mid]:
            print('%d is between %d[%3d] and %d[%3d] from left hand side.' \
                  % (val, low + 1, data[low], mid + 1, data[mid]))
            high = mid - 1

        elif val > data[mid]:
            print('%d is between %d[%3d] and %d[%3d] from right hand side.' \
                  % (val, mid + 1, data[mid], high + 1, data[high]))
            low = mid + 1

        else:
            return mid

    return -1


while True:
    num = 0
    val = int(input("Please enter a search value within 1~150(and -1 for ending) :"))
    if val == -1:
        break

    num = bin_search(data, val)
    if num == -1:
        print('Did not find value [%3d]' % val)
    else:
        print('At %3d, find the value [%3d].' % (num + 1, data[num]))

print('Data content: ')
for i in range(5):
    for j in range(10):
        print('%3d-%-3d' % (i * 10 + j + 1, data[i * 10 + j]), end='')

    print()
