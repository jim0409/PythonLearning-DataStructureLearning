import random

val = 0
data = [0] * 80

for i in range(80):
    data[i] = random.randint(1, 150)

while val != -1:
    find = 0
    val = int(input('Please enter an number you want to search(-1 ~ 150): '))
    for i in range(80):
        if data[i] == val:
            print('At %3d, find the value [%3d].' % (i + 1, data[i]))
            find += 1

        if find == 0 and val != -1:
            print('Did not find value [%3d].' % val)

print('Data content: ')
for i in range(10):
    for j in range(8):
        print('%2d[%3d]' % (i * 8 + j + 1, data[i * 8 + j]), end='')
    print('')
