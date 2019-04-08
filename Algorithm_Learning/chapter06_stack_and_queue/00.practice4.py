class Node:
    def __init__(self):
        self.data = 0
        self.next = None


front = Node()
rear = Node()

front = None
rear = None


def enqueue(value):
    global front
    global rear
    new_data = Node()
    new_data.data = value
    new_data.next = None

    if rear is None:
        front = new_data

    else:
        rear.next = new_data

    rear = new_data


def dequeue(action):
    global front
    global rear

    if front is not None and action == 1:
        if front == rear:
            rear = None

        value = front.data
        front = front.next
        return value

    elif rear is not None and action == 2:
        startNode = front
        value = rear.data

        tempNode = front
        while front.next != rear and front.next != None:
            front = front.next
            tempNode = front

        front = startNode
        rear = tempNode

        if front.next is None or rear.next is None:
            front = None
            rear = None
        return value

    else:
        return -1


def show():
    global front
    ptr = front
    while ptr is not None:
        print(ptr.data)
        ptr = ptr.next


ch = 'a'
while True:
    ch = input('s. Save data; r1. retrieve data from front; r2. retrieve data from rear; e. exit : ') or 's'
    if ch == 'e':
        break
    
    elif ch == 's':
        item = int(input('add new element: ') or 0)
        enqueue(item)
    
    elif ch == 'r1':
        temp = dequeue(1)
        print('the dequeue value from front is {}'.format(temp))

    elif ch == 'r2':
        temp = dequeue(2)
        print('the dequeue value from rear is {}'.format(temp))

    elif ch == 'rr':
        temp = dequeue(1)
        print('the dequeue value from front is {}'.format(temp))
        temp = dequeue(2)
        print('the dequeue value from rear is {}'.format(temp))
    
    elif ch == 'show':
        show()

    else:
        break