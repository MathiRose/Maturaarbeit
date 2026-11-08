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
