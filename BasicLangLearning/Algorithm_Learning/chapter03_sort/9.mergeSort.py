list1 = [20, 45, 51, 88, 99999]
list2 = [98, 10, 23, 15, 99999]
list3 = []


def select_sort(data):
    size=len(data)
    for base in range(size):
        small = base
        for j in range(base + 1, size):
            if data[j] < data[small]:
                small = j
        data[small], data[base] = data[base], data[small]


def My_Merge(size1, size2):
    global list1
    global list2
    global list3

    index1 = 0
    index2 = 0

    for index3 in range(len(list1) + len(list2) - 2):
        if list1[index1] < list2[index2]:  # compare two values and store smaller one
            list3.append(list1[index1])

            index1 += 1
            print('Values from first list %d' % list3[index3])

        else:
            list3.append(list2[index2])
            index2 += 1
            print('Values from second list %d' % list3[index3])

        print('the merge result :', end='')
        for i in range(index3 + 1):
            print(list3[i], '', end='')
        print('\n')


def merge_srot():
    global list1
    global list2
    global list3

    # use select_sort, sort two list and merge
    # select_sort(list1, len(list1) - 1)
    # select_sort(list2, len(list2) - 1)
    select_sort(list1)
    select_sort(list2)

    print('the first list sorting result :', end='')
    for i in range(len(list1) - 1):
        print(list1[i], '', end='')

    print('the second list sorting result :', end='')
    for i in range(len(list2) - 1):
        print(list2[i], end='')

    print()

    My_Merge(len(list1) - 1, len(list2) - 1)

    for i in range(60):
        print('=', end='')

    print()

    print('The merge_sort result :', end='')
    for i in range(len(list1) + len(list2) - 2):
        print('%d\t' % list3[i], end='')


merge_srot()
