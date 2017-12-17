class Node(object):
    def __init__(self, data,prev=None, next=None):
        self.data = data
        self.prev = prev
        self.next = next
    def __str__(self):
        return str(self.data)

class LinkedList(object):
    def __init__(self):
        self.head = None
        self.size = 0
    def append(self, data):
        if not self.head:
            n = Node(data)
            self.head = n
            return
        else:
            n = self.head

            while n.next != None:
                n = n.next

            new_node = Node(data)
            n.next = new_node
            return

    def isEmpty(self):
        return not self.head
    def printList(self):
        n = self.head
        while n:
            print (str(n))
            n = n.next

ll = LinkedList()

def print_backward(list):
    if list == None: return
    head = list
    tail = list.next
    print_backward(tail)
    print(head)

elems = [1, 2, 3, 54, 6]
for elem in elems:
    ll.append(elem)

ll.printList()
print("---")
print("---")
