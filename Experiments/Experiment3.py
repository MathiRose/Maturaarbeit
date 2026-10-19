"""
print(play(randomStr, QLearningStr, 10000))
print(play(randomStr, QLearningStr, 10000))
print(play(randomStr, QLearningStr, 10000))
print(play(randomStr, QLearningStr, 10000))
print(play(randomStr, QLearningStr, 10000))
print(play(randomStr, QLearningStr, 10000))

with open("QTable.pkl", "wb") as file:
    pickle.dump(QTable, file)

"""

print(play(randomStr, MinimaxStr, 100))