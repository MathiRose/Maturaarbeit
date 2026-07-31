from enum import Enum


BLACK = (0, 0, 0)
YELLOW = (255,255,0)
RED = (255,0,0)
WINDOW_HEIGHT = 800
WINDOW_WIDTH = 700
colour = YELLOW
board = [[BLACK] * 6 for _ in range(7)]


def game(str1, str2):

    global colour
    global board
    
    while True:
        if colour == YELLOW:
            str1()
            
        else:
            str2()



def placeChip(x):
    global colour
    global board
    
    
    for i in range(6):
        if board[x][i] == BLACK:
            board[x][i] = colour

            if checkWin() == True:
                Win()
                return
            
            if checkDraw() == True:
                print('draw')
                return

            if colour == YELLOW:
                colour=RED
            else:
                colour=YELLOW
            break


def checkWin():

    #check columns
    for column in board:
        for i in range(3):
            if column[i] != BLACK and column[i:i+4].count(column[i]) == 4:
                return True
            
    #check rows
    for i in range(4):
        for j in range(6):
            if board[i][j] != BLACK and [board[i+k][j] for k in range(4)].count(board[i][j]) == 4:
                return True
            
    #check diagonals
    #up-right
    for i in range(4):
        for j in range(3):
            if board[i][j] != BLACK and [board[i+k][j+k] for k in range(4)].count(board[i][j]) == 4:
                return True
            
    #up-left
    for i in range(4):
        for j in range(3):
            if board[i][j] != BLACK and [board[i-k+3][j+k] for k in range(4)].count(board[i][j]) == 4:
                return True


def Win():
    if colour == YELLOW:
        print('Yellow won')
    else:
        print('Red won')
    reset()
    

def checkDraw():
    for col in board:
        if BLACK in col:
            return
        
    return True
        

def reset():
    global colour
    global board
    colour = YELLOW
    board = [[BLACK] * 6 for _ in range(7)]


def LegalMoves():
    
    global board
    legalMoves = []
    
    for i in range(7):
        for j in range(6):
            if board[i][j] == BLACK:
                legalMoves.append([i])
                break

    return legalMoves