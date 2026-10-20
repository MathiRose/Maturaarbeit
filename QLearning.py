from environement import placeChip, LegalMoves, game
from randomStr import randomStr
import random

QTable = {}  # Initialize an empty Q-table
DiscountFactor = -0.95 #negative because the next state is the opponents turn
Lernrate = 0.1
Exploration = 0.3


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

    state = placeChip(action, board, player)

    canonicalBoard, canonicalAction = Canonicalize(board, action)
    s = State(canonicalBoard, player)
    initializeQTable(s, canonicalAction)
    
    if type(state) == str:
        if state == 'win':
            QTable[s][canonicalAction] = 100
        else:
            QTable[s][canonicalAction] = 0
            
    else:
        QObserved = (DiscountFactor * max([Q(state,a) for a in LegalMoves(state[0])])) #Bellman Equation - Reward is 0 except for win (which is handled above)
    
        TD_Error = QObserved - QTable[s][canonicalAction]
    
        QTable[s][canonicalAction] += Lernrate * TD_Error
        
    return state


def Q(state, action):
    b, canonicalAction = Canonicalize(state[0], action)
    s = State(b, state[1])
    initializeQTable(s, canonicalAction)
    return QTable[s][canonicalAction]


def initializeQTable(state, action):
    global QTable

    if state not in QTable:
        QTable[state] = {}

    if action not in QTable[state]:
        QTable[state][action] = random.random()  # Initialize with a random float 0.0 <= X < 1.0


def State(board, player): #lists can't be contained in dictionary keys, so I need to convert the board into a tuple
    return (tuple(tuple(column) for column in board), player)


def MirrorBoard(board):
    return board[::-1] #mirrors the board


def Canonicalize(board, action): #maps a board and action onto the canonical (mirrored) representation
    canonicalBoard = cannonicalBoard(board)
    if canonicalBoard == board:
        return canonicalBoard, action
    else:
        return canonicalBoard, 6-action


def cannonicalBoard(board): 
    if str(board) > str(MirrorBoard(board)): #if player 1 has more chips on the board than player 2, mirror the board
        return MirrorBoard(board)
    else:
        return board


def train(games = 10000):
    for i in range(games):        #play games between the two strategies
        game(QLearningStr, QLearningStr)


"""
Board = cannonicalBoard([[0, 0, 0, 0, 0, 0], 
                        [0, 0, 0, 0, 0, 0], 
                        [0, 0, 0, 0, 0, 0], 
                        [0, 0, 0, 0, 0, 0], 
                        [1, 0, 0, 0, 0, 0], 
                        [0, 0, 0, 0, 0, 0], 
                        [0, 0, 0, 0, 0, 0]])

player = 2
state = State(Board, player)
action = 3

initializeQTable(state, action)
QTable[state][action] = 5
Moved1 = QMove(action, Board, player)
QTable[State(*Moved1)][action] = 10000
Moved2 = QMove(action, Board, player)
Moved3 = QMove(action, *Moved2)

print(Q(state, action))
print(Q(Moved1, action))
print(Q(Moved2, action))
print(Q(Moved3, action))
print(QTable)
print(Moved3)
"""
