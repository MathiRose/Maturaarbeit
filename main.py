from environement import game
from randomStr import randomStr
from human import humanStr
from Minimax import MinimaxStr
from QLearning import QTrained

import pickle

with open("QTable.pkl", "rb") as file:
    QTable = pickle.load(file)


result = game(humanStr, MinimaxStr)

if result[0] == 'win':
    print(f'Player {result[1]} won')

if result[0] == 'draw':
    print('Draw')