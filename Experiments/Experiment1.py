from evaluation import play
from QLearning import QTrained, train
from randomStr import randomStr
import random

"""
from QLearning import QTable
import pickle
with open("QTable.pkl", "rb") as file:
    QTable = pickle.load(file)
"""
    
#random.seed(100)
print("\nvor dem Training")
game_1 = play(randomStr, QTrained, 500)
game_2 = play(QTrained, randomStr, 500)
print(f"Gewinnrate: {(game_1[1]+game_2[0])/10}%")
print(f"Durchschnittliche Rechenzeit pro Zug in [ms]: {(game_1[2][1]+game_2[2][0])*500}")
for i in range(100):
    train(30000)
    print(f"\nnach {30*(i+1)}'000 Trainingsepisoden")
    game_1 = play(randomStr, QTrained, 500)
    game_2 = play(QTrained, randomStr, 500)
    print(f"Gewinnrate: {(game_1[1]+game_2[0])/10}%")
    print(f"Durchschnittliche Rechenzeit pro Zug in [ms]: {(game_1[2][1]+game_2[2][0])*500}\n")

#this shows us weather the Q-Learning-Str is actually getting better by training

from QLearning import QTable
import pickle
with open("QTable.pkl", "wb") as file:
    pickle.dump(QTable, file)
