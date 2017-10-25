#http://www.openbookproject.net/thinkcs/python/english2e/ch18.html
class Node:
    def __init__(self, cargo=None, next=None):
        self.cargo = cargo
        self.next  = next

    def __str__(self):
        return str(self.cargo)

node =Node("test")
print(node)

node1=Node(1)
node2=Node(2)
node3=Node(3)
# This code creates three nodes, but we don’t have a list yet because the nodes are not linked. The state diagram looks like this:
# To link the nodes, we have to make the first node refer to the second and the second node refer to the third:
node1.next=node2
node2.next=node3

# To pass the list as a parameter, we only have to pass a reference to the first node. For example, the function print_list takes a single node as an argument. Starting with the head of the list, it prints each node until it gets to the end:
def print_list(node):
    while node:
        print(node)
        node = node.next
    print("---")

print_list(node1)

def print_backward(list):
    if list == None: return
    head = list
    tail = list.next
    print_backward(tail)
    print(head)

print_backward(node1)

