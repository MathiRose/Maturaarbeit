from environement import game
from randomStr import randomStr
from human import humanStr

result = game(humanStr, randomStr)

if result[0] == 'win':
    print(f'Player {result[1]} won')

if result[0] == 'draw':
    print('Draw')