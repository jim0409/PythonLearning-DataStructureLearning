# 在python中，若要以動態配置產生連結串列的節點，必須先行自訂一個類別，
# 接著在該類別中定義一個指標欄位，用意在指向下一個連結點，及至少一個資料欄位。
# e.g. 
class student:
	def __init__(self):
		self.name = ''
		self.id = 0
		self.score = 0
		self.next = None

	def show_info(self):
		print("id: {}, name: {}, with score: {}".format(self.id, self.name, self.score))


# 當完成每個節點的宣告後，會以動態建立連結串列中的每個節點。
#
# 流程:
# 假設我們現在要新增一個節點至串列的尾端，且ptr指向串列的第一個節點，在程式上必須設計四個步驟
# 1.動態配置記憶體空間給節點使用
# 2.將原串列尾端的指標欄(next)指向新元素所在的記憶體位置
# 3.將ptr指標指向新節點的記憶體位置，表示這是新的串列尾端
# 4.由於新節點目前為串列最後一個元素，所以將他的指標欄(next)指向None

head = student()  # 建立串列首
head.next = None  # 目前無下個元素
ptr = head  # 設定存取指標位置
select = 0

while select != 2:
	print('(1)add (2)exit =>')
	try:
		select = int(input('please enter number 1 or 2 :'))
	except ValueError:
		print("enter an invalid value")
		print("please do again.")

	if select == 1:
		new_data = student()  # 新增下一個元素
		new_data.name = input("name :")
		new_data.id = input('id :')
		new_data.score = eval(input('english score :'))
		ptr.next = new_data  # 存取指標設定為新元素所在位置
		new_data.next = None  # 下一個元素的Next設定為None
		ptr = ptr.next

print(head)
print(head.show_info())
print(head.next)
print(head.next.show_info())

# (1)add(2)exit = >
# please enter number 1 or 2: 1
# name: jim
# id: 1
# english score: 2
# (1)add(2)exit = >
# please enter number 1 or 2: 2
# <__main__.student object at 0x10260c9b0 >
# id: 0, name: , with score: 0
# None
# <__main__.student object at 0x10260ca20 >
# id: 1, name: jim, with score: 2
# None
