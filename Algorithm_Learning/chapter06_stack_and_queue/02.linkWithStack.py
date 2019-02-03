# The benefit of making stack with link is dynamic changing the link led to good memory control

class Node:  # claim a link node
    def __init__(self):
        self.data = 0  # claim the data inside stack
        self.next = None  # claim the next link_node for stack data


top = None


def isEmpty():
    global top
    if (top == None):
        return 1

    else:
        return 0


# put specify data into stack
def push(data):
    global top
    new_add_node = Node()
    new_add_node.data = data  # set node_data with data
    new_add_node.next = top  # set node_next to the top of stack
    top = new_add_node  # set node to the top of stack


# retrieve the data from stack
def pop():
    global top
    if isEmpty():
        print("------------The stack is Empty------------")
        return -1

    else:
        ptr = top  # set pointer to the top of stack
        top = top.next  # set top as top.next
        temp = ptr.data  # retrieve data from data
        return temp  # return data to main process


# main process
while True:
    i = int(input('enter 1 to add more stack, 0 to pop out stack and -1 to exit :'))
    if i == -1:
        break

    elif i == 1:
        value = int(input('enter the element :'))
        push(value)

    elif i == 0:
        print('the pop out value is %d' % pop())

print('--------------------')
while (not isEmpty()):  # pop out value from the top of stack
    print('the ordered data from stack %d ' % pop())

print('====================')
