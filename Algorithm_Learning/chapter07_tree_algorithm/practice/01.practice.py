def Btree_create(btree_deep, data):
    btree = [0]*pow(2, btree_deep)
    for i in range(1, len(data)):
        level = 1
        while btree[level] is not 0:
            if data[i] > btree[level]:  # if the max value is inside the tree, compare them with child tree
                level = level * 2 + 1

            else:
                level = level * 2

        btree[level] = data[i]
    return btree


# length = 9
data = [0, 6, 3, 5, 4, 7, 8, 9, 2]  # raw array
# btree = [0] * 16
btree_deep = 4
print('the origin content :')
for i in range(len(data)):
    print('[%2d]' % data[i], end='')

print('')
# Btree_create(btree, data, 9)
btree=Btree_create(btree_deep, data)

print('the btree content :')
for i in range(1, btree_deep):
    for j in range(pow(2, i-1), pow(2,i)):
        print('[{}]'.format(btree[j]), end='')
    print()

# for i in range(1, pow(2, btree_deep)):
#     print('[%2d]' % btree[i], end='')

print()
