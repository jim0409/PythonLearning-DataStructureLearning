from chapter03_sort.show_data import show_data
from chapter03_sort.inputarr import inputarr

def quick(d, size, lf, rg):
    # the first value is d[lf]
    if lf < rg:  # order data from left to right
        lf_idx = lf + 1
        while d[lf_idx] < d[lf]:
            if lf_idx + 1 > size:
                break

            lf_idx += 1

        rg_idx = rg

        while d[rg_idx] > d[lf]:
            rg_idx -= 1

        while lf_idx < rg_idx:
            d[lf_idx], d[rg_idx] = d[rg_idx], d[lf_idx]
            lf_idx += 1

            while d[lf_idx] < d[lf]:
                lf_idx += 1

            rg_idx -= 1
            while d[rg_idx] > d[lf]:
                rg_idx -= 1

        d[lf], d[rg_idx] = d[rg_idx], d[lf]

        for i in range(size):
            print('%3d' % d[i], end='')
        print()

        quick(d, size, lf, rg_idx - 1)  # Us rg_idx as a middle point to divide with recursive
        quick(d, size, rg_idx + 1, rg)


def main():
    data = [0] * 100
    size = int(input('Please enter a array array size (under 100) :'))
    inputarr(data, size)

    print('The origin data you enter was :')
    show_data(data)

    print('The sorting process was :')
    quick(data, size, 0, size - 1)

    print("Data after sorting :")
    show_data(data)


main()
