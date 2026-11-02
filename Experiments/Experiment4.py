from environement import game
from human import humanStr
from Minimax import MinimaxStr


result = game(humanStr, MinimaxStr)  #play a game between a human and the minimax strategy, human is player 1

if result[0] == 'win':
    print(f'Player {result[1]} won')
elif result[0] == 'draw':
    print('Draw')