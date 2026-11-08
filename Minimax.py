from environement import placeChip, LegalMoves

d = 5

def MinimaxStr(board, player, depth = d):
    bestMove = float('-inf')
    x = LegalMoves(board)[0]
    for i in LegalMoves(board):
        new_state = placeChip(i, board, player)
        if type(new_state) == str:
            if new_state == 'win':
                return new_state
            else:
                value = 0

        else:
            value = -Minimax(*new_state, depth)

        if value > bestMove:
            bestMove = value
            x = i

    return placeChip(x, board, player)


def Minimax(board, player, depth, alpha = float('-inf'), beta = float('inf')): 

    if depth == 0:
        return Value(board, player)
    
    legalMoves = LegalMoves(board)
    bestMove = float('-inf')

    for i in legalMoves:
        new_state = placeChip(i, board, player)
        if type(new_state) == str:
            if new_state == 'win':
                return float('inf')
            else: #draw
                bestMove = max(bestMove,0) 
        else:   #new_state is a string, so it can't be unpacked into Minimax()
            bestMove = max(bestMove, -Minimax(*new_state, depth - 1, -beta, -alpha))

        alpha = max(alpha, bestMove)
        if alpha >= beta:
            break

    return bestMove



def Value(board, player):

    value = 0

    value += countOpenRows(board, player, 3) * 10 

    value += countOpenRows(board, player, 2) * 1
    return value


def countOpenRows(board, player, length): #berechnet eigene - gegnerische offene Reihen

    value = 0

    #check columns
    for column in board:
        for i in range(7 - length):
            if column[i] != 0 and column[i:i+length].count(column[i]) == length: #checks if the column is of the right length
                if i+length != 6 and column[i+length] == 0: #checks if the column is open, future for-loops follow similar structure
                    if player == column[i]:
                        value += 1
                    else:
                        value -= 1

    #check rows
    for i in range(8 - length):
        for j in range(6):
            if board[i][j] != 0 and [board[i+k][j] for k in range(length)].count(board[i][j]) == length: 
                if (i != 0 and board[i-1][j] == 0) or (i+length != 7 and board[i+length][j] == 0):
                    if player == board[i][j]:
                        value += 1
                    else:
                        value -= 1

    #check diagonals
    #up-right
    for i in range(8 - length):
        for j in range(7 - length):
            if board[i][j] != 0 and [board[i+k][j+k] for k in range(length)].count(board[i][j]) == length:
                if (i != 0 and j != 0 and board[i-1][j-1] == 0) or (i+length != 7 and j+length != 6 and board[i+length][j+length] == 0):
                    if player == board[i][j]:
                        value += 1
                    else:
                        value -= 1

    #up-left
    for i in range(8 - length):
        for j in range(7 - length):
            if board[i+length-1][j] != 0 and [board[i-k+length-1][j+k] for k in range(length)].count(board[i+length-1][j]) == length:
                if (i+length != 7 and j != 0 and board[i+length][j-1] == 0) or (i != 0 and j+length != 6 and board[i-1][j+length] == 0):
                    if player == board[i+length-1][j]:
                        value += 1
                    else:
                        value -= 1

    return value


def MinimaxMitTiefe(tiefe):
    #MinimaxStr hat die Suchtiefe als optionalen Parameter, evaluation.play übergibt aber nur (board, player)
    def Strategie(board, player):   
        return MinimaxStr(board, player, tiefe)
    return Strategie

