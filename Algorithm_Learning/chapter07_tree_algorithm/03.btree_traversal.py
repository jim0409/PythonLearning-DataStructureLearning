# # BAC, Inorder : left to root to right
# def inorder(ptr):
#     if ptr != None:
#         inorder(ptr.left)
#         print('[%2d]' % ptr.data, end='')
#         inorder(ptr.right)
# # ABC, Preorder : root to left to right
# def preorder(ptr):
#     if ptr != None:
#         print('[%2d]' % ptr.data, end='')
#         preorder(ptr.left)
#         preorder(ptr.right)
# # BCA, Postorder : left to right to root
# def postorder(ptr):
#     if ptr !=None:
#         postorder(ptr.left)
#         postorder(ptr.right)
#         print('[%2d]' % ptr.data, end='')

class tree:
    def __init__(self):
        self.data = 0
        self.left = None
        self.right = None


def inorder(ptr):  # inorder sub process
    if ptr != None:
        inorder(ptr.left)
        print('[%2d]' % ptr.data, end='')
        inorder(ptr.right)


def create_tree(root, val):  # claim a binary tree function
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


# main process
data = [5, 6, 24, 8, 12, 3, 17, 1, 9]
ptr = None
root = None
for i in range(9):
    ptr = create_tree(ptr, data[i])

print('--------------------------------')
print('the ordered result: ')
inorder(ptr)
print('')
