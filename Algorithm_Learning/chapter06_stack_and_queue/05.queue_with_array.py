# # In Python, List is used as array data structure
# list1 = [1, 2, 3]
# print(type(list1)) # <class 'list'>
#
# list2 = [[1, 2], [3, 4]]
# print(type(list2)) # <class 'list'>
#

import sys

MAX = 10
queue = [0] * MAX
front = rear = -1
choice = ''
while rear < MAX - 1 and choice != 'e':
    choice = input('enter [a] to store an num \t [d] to pop out an num \t [e] to exit process :')
    if choice == 'a':
        val = int(input('please enter an number :'))
        rear += 1
        queue[rear] = val

    elif choice == 'd':
        if rear > front:
            front += 1
            print('the num del is %d ' % (queue[front]))
            queue[front] = 0

        else:
            print('the stack is empty')
            sys.exit(0)

    else:
        print()

print('--------------')
print('show all the element in the stack')

if rear == MAX - 1:
    print('no more space in stack')

elif front >= rear:
    print('no')
    print('the stack is empty')

else:
    while rear > front:
        front += 1
        print('[%d]' % queue[front], end='')
    print()
    print('--------------')

print()
