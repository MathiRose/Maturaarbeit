import random
from environement import placeChip, LegalMoves, board

def randomStr():
    print(board)
    placeChip(random.choice(LegalMoves(board)))
