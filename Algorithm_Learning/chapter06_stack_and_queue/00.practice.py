# 使用link list來製作stack時，必須要考慮到。stack的性質是FirstInLastOut
# 所以最先放入(push)到stack的data勢必最後才能取出(pop)
top = None

# 定義一個可以用來儲存的stack的基礎單元
class Node:
    def __init__(self):
        self.value = 0
        self.name = ''
        self.next = None

# 定義一個確認top是否為empty的函數
def isEmpty():
    global top
    if (top == None):
        return 1
    return 0


# 定義放入stack用的函數
def push(value, name):
    global top
    new_node_data = Node()
    new_node_data.value = value
    new_node_data.name = name
    new_node_data.next = top
    top = new_node_data
    print('successful to push data into stacks with name: {} and value: {}'.format(new_node_data.name, new_node_data.value))


# 定義一個取出stack內容物的函數
def pop():
    global top
    if isEmpty():
        print("the stack is Empty")
        return -1
    
    else:
        ptr = top
        top = top.next
        temp = "name: {}/ value: {}".format(ptr.name, ptr.value)
        return temp

# main process
while True:
    i = int(input('enter:\n 1) to add more stack\n 0) to pop out stack\n-1) to exit\n==>'))
    if i == -1:
        break
    
    elif i == 1:
        try:
            value = int(input('enter the push value(default 0) :') or 0)
            name = str(input('please enter the name(default usr):') or 'usr')
            push(value, name)
        except:
            print("something wrong while you push data to stacks")
    
    elif i == 0:
        print('the pop out value is {}'.format(pop()))

while(not isEmpty()):
    print('the ordered data from stack {}'.format(pop()))