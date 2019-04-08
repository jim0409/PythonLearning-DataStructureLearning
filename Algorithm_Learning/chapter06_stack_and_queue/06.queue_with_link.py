class student:
    def __init__(self):
        self.name = ' ' * 20
        self.score = 0
        self.next = None


front = student()
rear = student()
front = None
rear = None


def enqueue(name, score):
    global front
    global rear
    new_data = student()  # allocate memory for new element
    new_data.name = name
    new_data.score = score
    if rear == None:  # if rear is None means it is the first element
        front = new_data

    else:
        rear.next = new_data  # put new element into tail of the stack

    rear = new_data  # put rear to the new element whereas the tail of the stack
    new_data.next = None  # no more new element after


def dequeue():  # pop out the queue data
    global front
    global rear
    if front == None:
        print('the queue is empty!')
        rear = None

    else:
        print('name %s\tgrade %d\t' % (front.name, front.score))
        front = front.next  # move the front element to the next


def show():  # display the queue data
    global front
    global rear
    ptr = front
    if ptr == None:
        print('the queue is empty!')
        rear = None

    else:
        while ptr != None:  # check queue from front to rear
            print('name %s\tgrade %d\t' % (ptr.name, ptr.score))
            ptr = ptr.next


select = 0
while True:
    select = int(input('1.save 2.retrieve 3.display 4.exit =>'))
    if select == 4:
        break
    if select == 1:
        name = input('name:')
        score = int(input('score:'))
        enqueue(name, score)
    elif select == 2:
        dequeue()
    else:
        show()
