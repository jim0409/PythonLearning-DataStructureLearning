import sys

# 定義佇列的最大值
MAX = 5
queue = [0]*MAX

# 定義front以及rear用來確認佇列是否可以繼續被填充
# 這邊用意在控制兩端的位置來調整佇列的，先進先出
front = rear = -1

# 使用變數來控制接下來要實作的事情
choice = ''
while rear < MAX - 1 and choice != 'e':
    choice = input('a: store; d: delete; e: exit =>')

    # 如果輸入'a'，會取一開始宣告佇列的值rear+1=0,queue[0]='輸入的數字'
    if choice == 'a':
        val = int(input('please enter an number:'))
        rear += 1
        queue[rear] = val

    # 如果輸入'd'，會刪除祝列的第一筆值front+1=0,queue[0]=0
    elif choice == 'd':
        if rear > front:
            front += 1
            print('the delete number is {}'.format(queue[front]))
            queue[front] = 0

        else:
            print('the stack is empty')
            sys.exit(0)

    else:
        print()

print('----show all the element in the stack----')

if rear == MAX - 1:
    print('no more space in the stack')

elif front >= rear:
    print('the stack is empty')

while rear > front:
    front += 1
    print('{}'.format(queue[front]))
