from environement import placeChip, LegalMoves
import random

QTable = {}  # Initialize an empty Q-table
DiscountFactor = -0.95 #negative because the next state is the opponents turn
Lernrate = 0.1
Exploration = 0.3


def QLearningStr(board, player):
    return


def QLearningExploration(board, player):
    action = random.choice(LegalMoves(board))
    state =  placeChip(action, board, player)

    if type(state) == str:
        if state == 'win':
            QTable[(board, player)][action] = float('inf') #might cause problem with averaging out Q-values
        else:
            QTable[(board, player)][action] = 0
        
    else:
        QObserved = Reward(state) + (DiscountFactor * max([Q(state,a) for a in LegalMoves(state[1])])) #Bellman Equation

        if (board, player) not in QTable:
                QTable[(board, player)] = {}

        if action not in QTable[(board, player)]:
            QTable[(board, player)][action] = 0

        TD_Error = QObserved - QTable[(board, player)][action]
    
    return state


def Q(state, action):
    global QTable

    if state not in QTable:
        QTable[state] = {}

    if action not in QTable[state]:
        QTable[state][action] = 0

    return QTable[state][action]



