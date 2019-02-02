# 單向鏈結串列刪除節點的情境
# 1.刪除串列的第一個節點: 把串列指標首指向第二個節點
# top=head
# head=head.next

# 2.刪除串列後的最後一個節點: 指向最節點ptr的指標，直接指向None
# ptr.next = tail
# ptr.next = None

# 3.刪除串列內的中間節點: 刪除節點的前一個節點的指標，指向要刪除節點的下一個節點
# Y=ptr.next
# ptr.next=Y.next


import sys


class employee:
	def __init__(self):
		self.num = 0
		self.salary = 0
		self.name = ''
		self.next = None


def del_ptr(head, ptr):
	top = head
	if ptr.num == head.num:  # 情形一：刪除點在串列首
		print("enter and breadk")
		head = head.next
		print('already delete the [%d] member %s ($: %d)' % (ptr.num, ptr.name, ptr.salary))

	else:
		while top.next != ptr:  # 找到刪除點的前一個位置
			top = top.next

		if ptr.next == None:  # 刪除在串列尾的節點
			top.next = None
			print('already delete the [%d] member %s ($: %d)' % (ptr.num, ptr.name, ptr.salary))

		else:
			top.next = ptr.next  # 刪除在串列中的任一節點
			print('already delete the [%d] member %s ($: %d)' % (ptr.num, ptr.name, ptr.salary))

	return head  # 回傳串列


def main():
	namedata = ['Allen', 'Scott', 'Marry', 'Jon', 'Mark', 'Ricky', 'Lisa', 'Jasica', 'Hanson', 'Amy', 'Bob', 'Jack']

	data = [[1001, 32367], [1002, 24388], [1003, 27556], [1007, 31299],
			[1012, 42660], [1014, 25676], [1018, 44145], [1043, 52182],
			[1031, 32769], [1037, 21100], [1041, 32196], [1046, 25776]]

	print("member [id salary] [id salary] [id salary] [id salary]")
	print("------------------------------------------------------")

	for i in range(3):
		for j in range(4):
			print('%2d [%3d] ' % (data[j * 3 + i][0], data[j * 3 + i][1]), end='')
		print()

	head = employee()  # 建立串列首
	if not head:
		print('Error! failed to allocate memory!')
		sys.exit(0)

	head.num = data[0][0]
	head.name = namedata[0]
	head.salary = data[0][1]
	head.next = None

	ptr = head
	for i in range(1, 12):  # 建立串列
		newnode = employee()
		newnode.num = data[i][0]
		newnode.name = namedata[i]
		newnode.salary = data[i][1]
		newnode.next = None
		ptr.next = newnode
		ptr = ptr.next

	while (True):
		findword = int(input('please enter the delete member id, or enter -1 to exit process: '))
		if findword == -1:  # 迴圈中斷條件
			break
		else:
			ptr = head
			find = 0
			while ptr != None:
				if ptr.num == findword:
					ptr = del_ptr(head, ptr)
					find = find + 1
					head = ptr
					print(type(ptr))
				ptr = ptr.next
			if find == 0:
				print("####### empty result #######")

		ptr = head
		print('\tid\tmember name\tsalary')  # print out the data
		print('=========================')
		while (ptr != None):
			print('\t[%2d]\t[%-10s]\t[%3d]' % (ptr.num, ptr.name, ptr.salary))
			ptr = ptr.next


main()
