from random import random
from evaluation import play
from environement import LegalMoves, placeChip, game
from QLearning import QLearningStr, QTrained

seed = input("Gib einen seed für den zufälligen Zahlengenerator ein (oder lasse leer für zufällig): ")
if seed:
    random.seed(seed)  # Set the seed for reproducibility

SpieleProSchritt = 1000
Schritte = 10

def Strategy(board, player): #simple strategy
    return placeChip(LegalMoves(board)[0], board, player)

def printgame(str1, str2): #modified version of game() that prints the board after each move, so that I can analyse play paterns

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
        print("Current board state:")
        for i in board:
            print(i)
        print("next player: ", player)


def Test():
    r = [0, 0]
    game1 = game(Strategy, QTrained)
    game2 = game(QTrained, Strategy)
    if game1[0] == 'win'and game1[1] == 2:
        r[0] = 1
    if game2[0] == 'win' and game2[1] == 1:
        r[1] = 1
    return r

print(f"Test 0: {Test()}")

for i in range(Schritte):
    play(Strategy, QLearningStr, SpieleProSchritt)
    play(QLearningStr, Strategy, SpieleProSchritt)
    print(f"Test {i+1}: {Test()}")

printgame(Strategy, QTrained)

