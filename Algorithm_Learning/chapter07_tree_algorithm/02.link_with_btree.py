class tree:
    def __init__(self):
        self.data = 0
        self.left = None
        self.right = None


def create_tree(root, val):  # define a function to create binary tree
    newnode = tree()
    newnode.data = val
    newnode.left = None
    newnode.right = None

    if root is None:
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


data = [5, 6, 24, 8, 12, 3, 17, 1, 9]
ptr = None
root = None
for i in range(9):
    ptr = create_tree(ptr, data[i])  # build a binary tree

print('left btree')
root = ptr.left
while root is not None:
    print('%d' % root.data)
    root = root.left

print('-------------------')

print('right btree')
root = ptr.right
while root is not None:
    print('%d' % root.data)
    root = root.right
print()
