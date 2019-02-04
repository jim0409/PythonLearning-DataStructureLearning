def heap(data, size):
    for i in range(int(size / 2), 0, -1):  # create a stack tree node
        ad_heap(data, i, size - 1)
    print()
    print('the stack contain:', end='')
    for i in range(1, size):  # show the origin content in stack
        print('[%2d]' % data[i], end='')
    print('\n')
    for i in range(size - 2, 0, -1):  # order the stack
        data[i + 1], data[1] = data[1], data[i + 1]  # swap top and bottom
        ad_heap(data, 1, i)  # handle the left nodes
        print('in process ...', end='')
        for j in range(1, size):
            print('[%2d]' % data[j], end='')
        print()


def ad_heap(data, i, size):
    j = 2 * i
    tmp = data[i]
    post = 0
    while j <= size and post == 0:
        if j < size:
            if data[j] < data[j + 1]:  # looking for the maximum node
                j += 1

        if tmp >= data[j]:  # if root is bigger, end the whole process
            post = 1

        else:
            data[int(j / 2)] = data[j]  # if root is smaller, continue
            j = 2 * j

    data[int(j / 2)] = tmp  # set root as father node


def main():
    data = [0, 5, 6, 4, 8, 3, 2, 7, 1]
    size = 9
    print('the origin array:', end='')
    for i in range(1, size):
        print('[%2d]' % data[i], end='')
    heap(data, size)  # build a stack tree
    print('the resutl after ordered:', end='')
    for i in range(1, size):
        print('[%2d]' % data[i], end='')
    print()

main()
