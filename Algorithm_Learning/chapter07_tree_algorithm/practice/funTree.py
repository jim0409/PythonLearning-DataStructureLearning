def Btree_create(tree_deep, data):
    btree = [0]*pow(2, tree_deep)       # 因為deep是4，所以產生2^4個0在一維array作為btree，內容:[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

    for i in range(1, len(data)):       # 從data的第一個值開始讀取到最後一個值
        level = 1                       # 設定一個level常數，控制deep的層級

        while btree[level] is not 0:    # 當該層級的btree不是0的時候執行以下;0則直接賦予該位置值 ==> btree[level]= data[i]
            if data[i] > btree[level]:  # 1.判斷data對應值是否大於該內容的值 
                level = level*2+1       # 2.是的話就將該值放在右邊(level*2+1)，否則放在左邊(level)
            else:
                level = level*2
        btree[level] = data[i]          # 賦予該btree[level]值

    return btree

def show_tree(tree, tree_deep):
    for i in range(0, tree_deep):
        for j in range(pow(2, i), pow(2, i+1)):
            print('[{}]'.format(tree[j]), end='')
        print()

data = [0, 9, 3, 4, 5]

tree = Btree_create(4, data)
show_tree(tree, 4)
