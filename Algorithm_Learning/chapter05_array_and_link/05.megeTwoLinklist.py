# example: 單向串列的鏈結功能
import sys

import random


def concatlist(ptr1, ptr2):
	ptr = ptr1
	while ptr.next != None:
		ptr = ptr.next

	ptr.next = ptr2
	return ptr1


class employee:
	def __init__(self):
		self.num = 0
		self.salary = 0
		self.name = ''
		self.next = None


findword = 0
data = [[None] * 2 for row in range(12)]

namedata1 = ['Allen', 'Scott', 'Marry', 'Jon', 'Mark', 'Ricky', 'Lisa', 'Jasica', 'Hanson', 'Amy', 'Bob', 'Jack']
namedata2 = ['May', 'John', 'Michael', 'Andy', 'Tom', 'Jane', 'Yoko', 'Axel', 'Alex', 'Judy', 'Kelly', 'Lucy']

for i in range(12):
	data[i][0] = i + 1
	data[i][1] = random.randint(51, 100)

head1 = employee()
if not head1:
	print('Error!! failed to allocate memory!')
	sys.exit(0)

head1.num = data[0][0]
head1.name = namedata1[0]
head1.salary = data[0][1]
head1.next = None

ptr = head1
for i in range(1, 12):  # 建立第一組鏈結串列
	newnode = employee()
	newnode.num = data[i][0]
	newnode.name = namedata1[i]
	newnode.salary = data[i][1]
	newnode.next = None
	ptr.next = newnode
	ptr = ptr.next

for i in range(12):
	data[i][0] = i + 13
	data[i][1] = random.randint(51, 100)

head2 = employee()  # 建立第二組串列首
if not head2:
	print("Error! failed to allocate memory!")
	sys.exit(0)

head2.num = data[0][0]
head2.name = namedata2[0]
head2.salary = data[0][1]
head2.next = None

ptr = head2
for i in range(1, 12):  # 建立第二組鏈結串列
	newnode = employee()
	newnode.num = data[i][0]
	newnode.name = namedata2[i]
	newnode.salary = data[i][1]
	newnode.next = None
	ptr.next = newnode
	ptr = ptr.next

i = 0
ptr = concatlist(head1, head2)  # 將串列相連
print("The concatenate of two link are ")
while ptr != None:  # 列印串列資料
	print('[%2d %6s %3d] =>' % (ptr.num, ptr.name, ptr.salary), end='')

	i = i + 1
	if i >= 3:
		print()
		i = 0
	ptr = ptr.next
