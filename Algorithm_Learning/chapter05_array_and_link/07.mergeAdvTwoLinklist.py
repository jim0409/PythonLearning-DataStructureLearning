import sys
import random


def concate(ptr1, ptr2):
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


namedata1 = ['Allen', 'Scott', 'Marry', 'Jon', 'Mark', 'Ricky', 'Lisa', 'Jasica', 'Hanson', 'Amy', 'Bob', 'Jack']
namedata2 = ['May', 'John', 'Michael', 'Andy', 'Tom', 'Jane', 'Yoko', 'Axel', 'Alex', 'Judy', 'Kelly', 'Lucy']


def gen_salary_data():
	data = [[None] * 2 for row in range(12)]
	# print(data) # [[None, None], [None, None], [None, None], [None, None], [None, None], [None, None], [None, None], [None, None], [None, None], [None, None], [None, None], [None, None]]
	for i in range(12):
		data[i][0] = i + 1
		data[i][1] = random.randint(51, 100)
	return data


def allocate_link(namedata):
	data = gen_salary_data()
	head = employee()
	if not head:
		print('Error!! failed to allocate memory!')
		sys.exit(0)

	head.num = data[0][0]
	head.name = namedata[0]
	head.salary = data[0][1]
	head.next = None

	ptr = head
	for i in range(1, 12):  # 建立第一組鏈結串列
		newnode = employee()
		newnode.num = data[i][0]
		newnode.name = namedata[i]
		newnode.salary = data[i][1]
		newnode.next = None
		ptr.next = newnode
		ptr = ptr.next

	return head


def dump_link_data(link_ptr):
	i = 0
	while link_ptr != None:
		print('[%2d %6s %3d] =>' % (link_ptr.num, link_ptr.name, link_ptr.salary), end='')

		i = i + 1
		if i >= 3:
			print()
			i = 0
		link_ptr = link_ptr.next


def main():
	ptr1 = allocate_link(namedata1)
	# dump_link_data(ptr1)
	ptr2 = allocate_link(namedata2)
	# dump_link_data(ptr2)
	link_ptr = concate(ptr1, ptr2)

	dump_link_data(link_ptr)


if __name__ == '__main__':
	main()
