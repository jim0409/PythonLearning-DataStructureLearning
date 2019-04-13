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
        while current is not None:
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

# 改寫search
def search(ptr, val):
    ptr_r = ptr
    while ptr_r is not None:
        if ptr_r.data == val:
            print('success find the value {}'.format(val))
            return ptr_r
        else:
            if val > ptr_r.data:
                ptr_r = ptr_r.right
            else:
                ptr_r = ptr_r.left
                

# def search(ptr, val):  # search btree subprocess
#     i = 1
#     while True:
#         if ptr is None:  # return None if doesn't find
#             return None

#         if ptr.data == val:  # node value equal to the searching value
#             print('take %3d times to search' % i)
#             return ptr

#         elif ptr.data > val:  # node value is bigger than search value
#             ptr = ptr.left

#         else:
#             ptr = ptr.right
#         i += 1


# main process
arr = [7, 1, 4, 2, 8, 13, 12, 11, 15, 9, 5]
ptr = None
print('the origin array content')
for i in range(11):
    ptr = create_tree(ptr, arr[i])  # create a binary tree
    print('[%2d]' % arr[i], end='')

print()
while True:
    data = int(input('please enter num to search :'))
    if search(ptr, data) != None:  # searching in btree
        print('the value [%3d] is inside the btree.' % data)

    else:
        print('the value [%3d] is not in btree.' % data)
