import random
from environement import placeChip, LegalMoves

def randomStr(board, player):
    return placeChip(random.choice(LegalMoves(board)), board, player)
