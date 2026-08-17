from environement import game
from randomStr import randomStr
from human import humanStr
from Minimax import MinimaxStr

result = game(humanStr, humanStr)

if result[0] == 'win':
    print(f'Player {result[1]} won')

if result[0] == 'draw':
    print('Draw')