def Btree_create(tree_deep, data):
    btree = [0]*pow(2, tree_deep)
    for i in range(1, len(data)):
        level = 1
        while btree[level] is not 0:
            if data[i] > btree[level]:
                level = level*2+1
            else:
                level = level*2

        btree[level] = data[i]
    return btree

def show_tree(tree, tree_deep):
    for i in range(0, tree_deep):
        for j in range(pow(2, i), pow(2, i+1)):
            print('[{}]'.format(tree[j]), end='')
        print()

data = [0, 9, 3, 4, 5]

tree = Btree_create(4, data)
show_tree(tree, 4)
