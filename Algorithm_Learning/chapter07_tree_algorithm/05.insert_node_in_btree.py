class tree:
    def __init__(self):
        self.data = 0
        self.left = None
        self.right = None


def create_tree(root, val):  # claim a binary tree create func
    newnode = tree()
    newnode.data = val
    newnode.left = None
    newnode.right = None
    if root == None:
        root = newnode
        return root

    else:
        current = root
        while current != None:
            backup = current
            if current.data > val:
                current = current.left

            else:
                current = current.right

        if backup.data > val:
            backup.left = newnode

        else:
            backup.right = newnode

    return root


def search(ptr, val):  # subprocess for btree search
    while True:
        if ptr == None:  # return None if doesn't find searching value
            return None

        if ptr.data == val:
            return ptr

        elif ptr.data > val:  # if the node value is bigger than searching value
            ptr = ptr.left

        else:
            ptr = ptr.right


def inorder(ptr):  # inorder subprocess
    if ptr != None:
        inorder(ptr.left)
        print('[%2d]' % ptr.data, end='')
        inorder(ptr.right)


# main process
arr = [7, 1, 4, 2, 8, 13, 12, 11, 15, 9, 5]
ptr = None
print('[print the origin array content]')

for i in range(11):
    ptr = create_tree(ptr, arr[i])  # build a btree
    print('[%2d]' % arr[i], end='')
print()

while True:
    data = int(input('please enter value you want to search :'))
    if search(ptr, data) != None:  # search value in btree
        print('the value [%3d] is in the btree' % data)

    else:
        ptr = create_tree(ptr, data)
        inorder(ptr)
        print()
