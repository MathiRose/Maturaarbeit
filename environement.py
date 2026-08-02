from enum import Enum


WINDOW_HEIGHT = 800
WINDOW_WIDTH = 700
player = 1
board = [[0] * 6 for _ in range(7)]


def game(str1, str2):

    global player
    global board
    
    while True:
        if player == 1:
            str1()
            
        else:
            str2()



def placeChip(x):
    global player
    global board
    
    
    for i in range(6):
        if board[x][i] == 0:
            board[x][i] = player

            if checkWin() == True:
                Win()
                return
            
            if checkDraw() == True:
                print('draw')
                return

            if player == 1:
                player=2
            else:
                player=1
            break


def checkWin():

    #check columns
    for column in board:
        for i in range(3):
            if column[i] != 0 and column[i:i+4].count(column[i]) == 4:
                return True
            
    #check rows
    for i in range(4):
        for j in range(6):
            if board[i][j] != 0 and [board[i+k][j] for k in range(4)].count(board[i][j]) == 4:
                return True
            
    #check diagonals
    #up-right
    for i in range(4):
        for j in range(3):
            if board[i][j] != 0 and [board[i+k][j+k] for k in range(4)].count(board[i][j]) == 4:
                return True
            
    #up-left
    for i in range(4):
        for j in range(3):
            if board[i][j] != 0 and [board[i-k+3][j+k] for k in range(4)].count(board[i][j]) == 4:
                return True


def Win():
    if player == 1:
        print('Yellow won')
    else:
        print('Red won')
    reset()
    

def checkDraw():
    for col in board:
        if 0 in col:
            return
        
    return True
        

def reset():
    global player
    global board
    player = 1
    board = [[0] * 6 for _ in range(7)]


def LegalMoves(state):
    
    legalMoves = []
    
    for i in range(7):
        for j in range(6):
            if state[i][j] == 0:
                legalMoves.append(i)
                break

    return legalMoves