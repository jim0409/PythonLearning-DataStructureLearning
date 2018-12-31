from show_data import show_data

data = [16, 25, 39, 27, 12, 8, 45, 63]
def insert(data):
    for i in range(1,len(data)):
        tmp=data[i]
        no=i-1
        while no>=0 and tmp<data[no]:
            data[no+1]=data[no]
            no-=1
            data[no+1]=tmp

print("The origin data is ")
show_data(data)

print("Data after sorting ")
insert(data)
show_data(data)
