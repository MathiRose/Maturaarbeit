from environement import placeChip, LegalMoves, game
import random

QTable = {}  # Initialize an empty Q-table
DiscountFactor = -0.95 #negative because the next state is the opponents turn
Lernrate = 0.1
Exploration = 0.3


"""
import pickle

with open("QTable.pkl", "rb") as file:
    QTable = pickle.load(file)
"""


def QTrained(board, player):
    return placeChip(max([(Q((board, player), a), a) for a in LegalMoves(board)])[1], board, player) #max with tuple as input returns tuple with highest first value


def QLearningStr(board, player):
    randomValue = random.random()
    if randomValue < Exploration:
        return QLearningExploration(board, player)
    else:
        return QMove(max([(Q((board, player), a), a) for a in LegalMoves(board)])[1], board, player) #max with tuple as input returns tuple with highest first value


def QLearningExploration(board, player):
    action = random.choice(LegalMoves(board))
    return QMove(action, board, player)


def QMove(action, board, player):
    b = cannonicalBoard(board)
    state =  placeChip(action, board, player)
    s = State(b, player)
    initializeQTable(s, action)
    
    if type(state) == str:
        if state == 'win':
            QTable[s][action] = 100
        else:
            QTable[s][action] = 0
            
    else:
        QObserved = (DiscountFactor * max([Q(state,a) for a in LegalMoves(state[0])])) #Bellman Equation - Reward is 0 except for win (which is handled above)
    
        TD_Error = QObserved - QTable[s][action]
    
        QTable[s][action] += Lernrate * TD_Error
        
    return state


def Q(state, action):
    s = State(cannonicalBoard(state[0]), state[1])
    initializeQTable(s, action)
    return QTable[s][action]


def initializeQTable(state, action):
    global QTable

    if state not in QTable:
        QTable[state] = {}

    if action not in QTable[state]:
        QTable[state][action] = 0


def State(board, player): #lists can't be contained in dictionary keys, so I need to convert the board into a tuple
    return (tuple(tuple(column) for column in board), player)


def MirrorBoard(board):
    return board[::-1] #mirrors the board


def cannonicalBoard(board): 
    if str(board) > str(MirrorBoard(board)): #if player 1 has more chips on the board than player 2, mirror the board
        return MirrorBoard(board)
    else:
        return board


def train(games = 10000):
    for i in range(games):        #play games between the two strategies
        game(QLearningStr, QLearningStr)


