from chapter03_sort.show_data import show_data

data = [16, 25, 39, 27, 12, 8, 45, 63]


def select(data):
    for i in range(len(data) - 1):
        for j in range(i + 1, 8):
            if data[i] > data[j]:
                data[i], data[j] = data[j], data[i]

    print()


print("Raw data is ")
show_data(data)

select(data)
print("Data after sorting ")
show_data(data)
