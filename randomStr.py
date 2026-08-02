import random
from environement import placeChip, LegalMoves, board

def randomStr():
    placeChip(random.choice(LegalMoves(board)))
