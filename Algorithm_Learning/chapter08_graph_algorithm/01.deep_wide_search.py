class list_node:
    def __init__(self):
        self.val = 0
        self.next = None


head = [list_node()] * 9

run = [0] * 9


def dfs(current):  # deep priority func
    run[current] = 1
    print('[%d]' % current, end='')
    ptr = head[current].next
    while ptr != None:
        if run[ptr.val] == 0:  # if ptr doesn't reach vertex
            dfs(ptr.val)  # recursive func
        ptr = ptr.next


# claim a edge array
data = [[1, 2], [2, 1], [1, 3], [3, 1], [2, 4], [4, 2], [2, 5], [5, 2], [3, 6], [6, 3], [3, 7], [7, 3], [4, 8], [8, 4],
        [5, 8], [8, 5], [6, 8], [8, 6], [8, 7], [7, 8]]

"""
1 -- 2 --- 4 --|
  |     |      |
  |     -- 5 --|
  |            8
  -- 3 --- 6 --| 
        |      |
        -- 7 --|
"""

for i in range(1, 9):  # set 8 vertex point
    run[i] = 0  # set every point as unreachable
    head[i] = list_node()
    head[i].val = i  # init every point's value
    head[i].next = None
    ptr = head[i]  # set ptr as head
    for j in range(20):  # calculate 20 edge line
        print("start loop with (i, j) in ({}, {})".format(i, j))
        if data[j][0] == i:  # if start_pt is equal to the hed, concatenate it with vertex queue
            newnode = list_node()
            newnode.val = data[j][1]
            newnode.next = None
            while True:
                print("add new node to head[{}] with value {}".format(
                    i, data[j][1]))
                ptr.next = newnode  # add new node
                ptr = ptr.next
                if ptr.next == None:
                    break

# print out the graph within the graph
print('the edge queue within the graph:')
for i in range(1, 9):
    ptr = head[i]
    print('vertext %d =>' % ptr.val, end='')

    # 不打印出節點，只打印出該節點能夠遍佈的點
    while ptr.next != None:
        print('[%d]' % ptr.next.val, end='')
        ptr = ptr.next
    print()
print('move to vertextt from deep')  # print out the path
dfs(1)
print()
