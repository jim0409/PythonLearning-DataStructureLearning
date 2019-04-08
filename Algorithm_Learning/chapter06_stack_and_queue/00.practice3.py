class node:
    def __init__(self):
        self.name = ''
        self.score = 0
        self.next = None

front = node()
rear = node()
front = None
rear = None

def enqueue(name, score):
    global front
    global rear
    new_data = node()
    new_data.name = name
    new_data.score = score
    if rear == None:
        front = new_data
    else:
        rear.next = new_data
    
    rear = new_data
    new_data.next = None

def dequeue():
    global front
    global rear
    if front == None:
        print('the queue is empty!')
        rear = None
    
    else:
        print('name {} with grade {}'.format(front.name, front.score))
        front = front.next


def show():
    global front
    global rear
    ptr = front
    if ptr == None:
        print('the queue is empty')
        rear = None
    
    else:
        while ptr != None:
            print('name {} grade {}'.format(ptr.name, ptr.score))
            ptr = ptr.next

choice=''
while True:
    choice = input('s: save; r: retrieve; d: display; e: exit =>')
    if choice == 'e':
        break
    if choice == 's':
        name = input('name:')
        score = int(input('score:'))
        enqueue(name, score)
    elif choice == 'r':
        dequeue()
    else:
        show()