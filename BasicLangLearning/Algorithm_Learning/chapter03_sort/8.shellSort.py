from chapter03_sort.show_data import show_data

data = [16, 25, 39, 27, 12, 8, 45, 63]


def shell(data):
    k = 1
    tmplen = len(data) // 2
    while tmplen != 0:
        for i in range(tmplen, len(data)):
            tmp = data[i]  # use tmp to store data
            j = i - tmplen

            while tmp < data[j] and j >= 0:  # insert sort
                data[j + tmplen] = data[j]
                j = j - tmplen

            data[tmplen] = tmp

        print('The %d time sorting is :' % k, end='')
        k += 1
        show_data(data)

        tmplen = tmplen // 2


print("The origin data is :")
show_data(data)

shell(data)
print("Data after sorting :")
show_data(data)
