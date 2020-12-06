_author_ = 'kishnashenoy'

import boards

'''board = [
    [0,8,0,7,9,0,0,5,0],
    [3,0,5,0,0,8,0,4,0],
    [0,0,0,0,0,0,0,8,0],
    [0,0,1,0,7,0,0,0,4],
    [6,0,0,3,0,1,0,0,8],
    [9,0,0,0,8,0,0,1,0],
    [0,7,2,0,0,0,0,0,0],
    [0,2,4,5,0,0,8,9,1],
    [0,4,8,0,0,3,0,0,0],
]'''

#board = boards.unfinished

def complete(bo):
    find = find_empty(bo)
    if not find:
        return True
    else:
        row, col = find
    for i in range(1, 10):
        if correct(bo, i, (row, col)):
            bo[row][col] = i

            if complete(bo):
                return True

            bo[row][col] = 0

    return False

def correct(bo, num, pos):

    # checking the columns for repetition
    for i in range(len(bo[0])):
        if bo[pos[0]][i] == num and pos[1] != i:
            return False

    # checking the rows for repetition
    for i in range(len(bo)):
        if bo[i][pos[1]] == num and pos[0] != i:
            return False

    # checking boxes for repetition
    x_box = pos[1] // 3
    y_box = pos[0] // 3

    for i in range(y_box*3, y_box*3 + 3):
        for j in range(x_box*3, x_box*3 + 3):
            if bo[i][j] == num and (i, j) != pos:
                return False

    return True

'''def board_print(board):
    for i in range(len(board)):
        if i % 3 == 0 and i != 0:
            print('---------------------')

        for j in range(len(board[0])):
            if j % 3 == 0 and j != 0:
                print('|', end=" ")

            if j == 8:
                print(board[i][j])
            else:
                print(str(board[i][j]) + " ", end = "")'''

def find_empty(bo):
    for i in range(len(bo)):
        for j in range(len(bo[0])):
            if bo[i][j] == 0:
                return (i, j) # returns column, row
    return None

def is_valid(bo):
    for row in range(9):
        for col in range(9):
            if (bo[row][col] > 0):
                if not correct(bo, bo[row][col], (row, col)):
                    return False
    return True

def run():
    global board
    board = boards.unfinished
    for i in range(9):
        for j in range(9):
            board[i][j] = int(board[i][j])
    complete(board)
    return board


