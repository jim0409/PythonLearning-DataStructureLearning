from chapter03_sort.show_data import show_data
from chapter03_sort.inputarr import inputarr


def radix(data, size):
    n = 1  # where n is an odd number
    while n < 100:
        tmp = [[0] * 100 for row in range(10)]  # set an tmp array tmp_array[0~9] = 0

        for i in range(size):
            m = (data[i] // n) % 10  # mod(m) is n
            tmp[m][i] = data[i]  # store data[i] in tmp_array

        k = 0
        for i in range(10):
            for j in range(size):
                if tmp[i][j] != 0:  # without initial value 0, every none-zero value is
                    data[k] = tmp[i][j]  # what we need

                    k += 1

        print('After %d th time sorting: ' % n, end='')

        show_data(data)
        n = 10 * n


def main():
    data=[0]*100
    size=int(input("Please enter an number :"))
    print('The origin data is ')
    inputarr(data,size)

    show_data(data)

    radix(data,size)


main()
