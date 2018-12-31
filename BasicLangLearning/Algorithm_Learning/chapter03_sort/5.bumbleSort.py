from chapter03_sort.show_data import show_data

data = [16, 25, 39, 27, 12, 8, 45, 63]
print("Show raw data : ")

for i in range(len(data) - 1, -1, -1):
    for j in range(i):
        if data[j] > data[j + 1]:
            data[j], data[j + 1] = data[j + 1], data[j]

    print("The %d sorting result is :" % (8 - i), end='')

    show_data(data)

print("After sorting ___ data :")
show_data(data)
