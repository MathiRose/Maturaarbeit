from environement import board, placeChip, LegalMoves

def Minimax(board, player, depth):

    legalMoves = LegalMoves(board)

    if depth == 0:
        bestMove = float('-inf')

        for i in legalMoves:
            bestMove = max(bestMove, Value(placeChip(i, board, player)))

        return bestMove

    for i in legalMoves:
        new_board, new_player = placeChip(i, board, player)
        Minimax(new_board, new_player, depth-1)
        
    return M



def Value(board, player = 0):
 
    if board == 'win':
        return float('inf')
    
    if board == 'draw':
        return 0


    value = 0

    value += own_3_row * 5
    value -= enemy_3_row * 5

    value += own_2_row * 1
    value -= enemy_2_row * 1

    return value

    