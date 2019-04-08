# allow queue to add or delete data from poles
# use condition: data need to add by one of them also can be retrieve from both

class Node:
    def __init__(self):
        self.data = 0
        self.next = None


front = Node()
rear = Node()
front = None
rear = None


# define the method to store data
def enqueue(value):
    global front
    global rear
    node = Node()  # claim an new node
    node.data = value
    node.next = None

    # check whether the queue is empty
    if rear is None:
        front = node  # new another node as the first node

    else:
        rear.next = node  # put the node at the bottom of stack

    rear = node  # point the new node to the bottom of stack


# define the method to retrieve data
def dequeue(action):
    global front
    global rear
    # retrieve data front top
    if front is not None and action == 1:
        if front == rear:
            rear = None

        value = front.data  # retrieve data from top
        front = front.next  # point the next node
        return value

    # retrieve data from bottom
    elif rear is not None and action == 2:
        startNode = front  # record the value of front
        value = rear.data  # retrieve the data from bottom

        # looking for the penultimate value from the bottom of Node
        tempNode = front
        while front.next != rear and front.next != None:
            front = front.next
            tempNode = front
        front = startNode  # record the front point from bottom of queue
        rear = tempNode  # record the bottom point from bottom of queue

        # while the next line is the bottom of the whole queue
        # retireve dat from front and rear and point to None
        if front.next is None or rear.next is None:
            front = None
            rear = None
        return value

    else:
        return -1


print('build dequeue with link')
print('-----------------------')

ch = 'a'
while True:
    ch = input('a.save data, d.retrieve data, e.exit : ')
    if ch == 'e':
        break

    elif ch == 'a':
        item = int(input('add new element :'))
        enqueue(item)

    elif ch == 'd':
        temp = dequeue(1)
        print('the double queue from fornt is : %d ' % temp)
        temp = dequeue(2)
        print('the double queue from rear is : %d ' % temp)

    else:
        break
