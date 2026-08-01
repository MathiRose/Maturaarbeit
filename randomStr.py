import random
from environement import placeChip, LegalMoves

def randomStr():
    placeChip(random.choice(LegalMoves()))
