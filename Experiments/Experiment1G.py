from evaluation import play
from QLearning import QTrained, train
from randomStr import randomStr
import matplotlib.pyplot as plt
import random

"""
from QLearning import QTable
import pickle
with open("QTable.pkl", "rb") as file:
    QTable = pickle.load(file)
"""
#random.seed(100)

Gewinnraten = []

game_1 = play(randomStr, QTrained, 500)
game_2 = play(QTrained, randomStr, 500)
Gewinnraten.append((game_1[1]+game_2[0])/10)

for i in range(30):
    train(20000)
    game_1 = play(randomStr, QTrained, 500)
    game_2 = play(QTrained, randomStr, 500)
    Gewinnraten.append((game_1[1]+game_2[0])/10)

plt.plot(range(0, len(Gewinnraten)*20000, 20000), Gewinnraten)
plt.xlabel("Trainingsepisoden")
plt.ylabel("Gewinnrate")
plt.title("Entwicklung der Gewinnrate")
plt.show()

print(f"Durchschnittliche Rechenzeit pro Zug in [ms]: {(game_1[2][1]+game_2[2][0])*500}") #nur die Rechenzeit der Letzten 100 Spiele, aber spielt keine Rolle

#this shows us how the Q-Learning-Str is getting better by training


from QLearning import QTable
import pickle
with open("QTable.pkl", "wb") as file:
    pickle.dump(QTable, file)