# still exit bug ...

global gueen
global number
EIGHT = 8  # define the maximum of stack size
queen = [None] * 8  # allocate 8 place for queen

number = 0  # calculate the total solution of set


# define the place to put queen
# calculate the final result
def print_table():
    global number
    x = y = 0
    number += 1
    print('')
    print('The 8 queen question_%d_th solution \t ' % number)
    for x in range(EIGHT):
        for y in range(EIGHT):
            if x == queen[y]:
                print('<q>', end='')

            else:
                print('<->', end='')

        print('\t')
    input('\n..press any button to continue..\n')


# test whether the location (row, col) would be attack by other queens
# if attacked return 1 else return 0
def attack(row, col):
    global queen
    i = 0
    atk = 0
    offset_row = offset_col = 0
    while atk != 1 and i < col:
        offset_col = abs(i - col)
        offset_row = abs(queen[i] - row)

        # determine whether the two queens are in the diagonal
        if queen[i] == row or offset_row == offset_col:
            atk = 1

        i = i + 1
    return atk


def decide_position(value):
    global queen
    i = 0
    while i < EIGHT:
        if attack(i, value) != 1:
            queen[value] = i
            if value == 7:
                print_table()
            else:
                decide_position(value + 1)

        i = i + 1


# main process
decide_position(0)
