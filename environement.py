from enum import Enum



def game(str1, str2):

    game = True
    player = 1
    board = [[0] * 6 for _ in range(7)]
    
    while True:
        if player == 1:
            state = str1(board, 1)
            if type(state) == str:
                return [state, 1]
            
            board, player = state
            
        else:
            state = str2(board, 2)  
            if type(state) == str:
                return [state, 2]
            
            board, player = state



def placeChip(x, board, player):

    new_board = [row.copy() for row in board] #else the board variable gets edited directly
    
    for i in range(6):
        if new_board[x][i] == 0:
            new_board[x][i] = player

            if checkWin(new_board) == True:
                return 'win'
            
            if checkDraw(new_board) == True:
                return 'draw'

            if player == 1:
                return new_board, 2
            else:
                return new_board, 1
            


def checkWin(board):

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
    


def checkDraw(board):
    for col in board:
        if 0 in col:
            return False
        
    return True
        

def LegalMoves(board):
    
    legalMoves = []
    
    for i in range(7):
        for j in range(6):
            if board[i][j] == 0:
                legalMoves.append(i)
                break

    return legalMoves