MAXSIZE = 10  # define the maxsize of queue

front = -1  # point to the vertex of queue
rear = -1  # point to the bottom of queue


class Node:
    def __init__(self, x):
        self.x = x
        self.next = None  # point to the next pointer


class GraphLink:
    def __init__(self):
        self.first = None
        self.last = None

    def my_print(self):
        current = self.first
        while current != None:
            print('[%d]' % current.x, end='')
            current = current.next
        print()

    def insert(self, x):
        newNode = Node(x)
        if self.first == None:
            self.first = newNode
            self.last = newNode

        else:
            self.last.next = newNode
            self.last = newNode


# store data into queue
def enqueue(value):
    global MAXSIZE
    global rear
    global queue
    if rear >= MAXSIZE:
        return
    rear += 1
    queue[rear] = value


# retrieve data from queue
def dequeue():
    global front
    global queue
    if front == rear:
        return -1
    front += 1
    return queue[front]


# wide to deep searching
def bfs(current):
    global front
    global rear
    global Head
    global run
    enqueue(current)  # store the vertex node into queue
    run[current] = 1  # for passing point, set value as 1
    print('[%d]' % current, end='')  # print out all the passing points
    while front != rear:  # check whether the queue is empty
        current = dequeue()  # retrieve the vertex of queue
        tempnode = Head[current].first  # record the ahead point

        # print('{}'.format(tempnode))
        # print('{}'.format(tempnode.first))

        while tempnode != None:
            if run[tempnode.x] == 0:
                enqueue(tempnode.x)
                run[tempnode.x] = 1  # record the passing point
                print('[%d]' % tempnode.x, end='')
            tempnode = tempnode.next


# claim edge graph array
Data = [[0] * 2 for row in range(20)]

Data = [[1, 2], [2, 1], [1, 3], [3, 1], [2, 4], [4, 2], [2, 5], [5, 2], [3, 6], [6, 3], [3, 7], [7, 3], [4, 5], [5, 4],
        [6, 7], [7, 6], [5, 8], [8, 5], [6, 8], [8, 6]]

run = [0] * 9  # record the passing point
queue = [0] * MAXSIZE
# Head = [GraphLink] * 9
Head = [None] * 9

print('the grpah content in the content:')  # print out the neighbor content of the graph
for i in range(1, 9):  # totally 8 vertex
    run[i] = 0  # set all the vertex as 0
    print('vertex %d =>' % i, end='')
    Head[i] = GraphLink()
    for j in range(20):
        if Data[j][0] == i:  # if the start point and queue
            DataNum = Data[j][1]
            Head[i].insert(DataNum)
    Head[i].my_print()  # print the graph content

print('wide to deep access vertex :')  # print out the wdie to deep vertex
bfs(1)
print()
