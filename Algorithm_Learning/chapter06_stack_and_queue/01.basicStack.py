MAXSTACK = 100  # define the max stack
global stack
stack = [None] * MAXSTACK  # claim the stack array
top = -1  # define the top of stack


# check whether this is an empty stack
def isEmpty():
    if top == -1:
        return True
    else:
        return False


# put data into stack
def push(data):
    global top
    global MAXSTACK
    global stack

    if top > MAXSTACK - 1:
        print('Stack has no more space to add data.')

    else:
        top += 1
        stack[top] = data  # put data into stack


# retrieve data from stack
def pop():
    global top
    global stack
    if isEmpty():
        print('The stack is Empty')

    else:
        print('The first bump out element is %d ' % stack[top])
        top = top - 1


# main process
i = 2
count = 0

while True:
    i = int(input('Add stack with 1, bump out with 0 and -1 to exit :'))
    if i == -1:
        break

    elif i == 1:
        value = int(input('please enter the element :'))
        push(value)

    elif i == 0:
        pop()

print("=================")
if top < 0:
    print('\nThe stack is Empty')

else:
    i = top
    while i > 0:
        print('The bump Number from stack is : %d' % (stack[i]))
        count += 1
        i = i - 1

    print

print('=================')
