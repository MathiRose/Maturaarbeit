

def countRows(board, player, length): #berechnet eigene - gegnerische Reihen

    value = 0

    #check columns
    for column in board:
        for i in range(7 - length):
            if column[i] != 0 and column[i:i+length].count(column[i]) == length:
                if player == column[i]:
                    value += 1
                else:
                    value -= 1

    #check rows
    for i in range(8 - length):
        for j in range(6):
            if board[i][j] != 0 and [board[i+k][j] for k in range(length)].count(board[i][j]) == length:
                if player == board[i][j]:
                    value += 1
                else:
                    value -= 1

    #check diagonals
    #up-right
    for i in range(8 - length):
        for j in range(7 - length):
            if board[i][j] != 0 and [board[i+k][j+k] for k in range(length)].count(board[i][j]) == length:
                if player == board[i][j]:
                     value += 1
                else:
                    value -= 1

    #up-left
    for i in range(8 - length):
        for j in range(7 - length):
            if board[i+length-1][j] != 0 and [board[i-k+length-1][j+k] for k in range(length)].count(board[i+length-1][j]) == length:
                if player == board[i+length-1][j]:
                    value += 1
                else:
                    value -= 1

    return value
    

