from evaluation import play
from QLearning import QTrained, train
from randomStr import randomStr
import matplotlib.pyplot as plt
#import math
import random

"""
from QLearning import loadQTable
loadQTable()
"""
seed = input("Gib einen seed für den zufälligen Zahlengenerator ein (oder lasse leer für zufällig): ")
if seed:
    random.seed(seed)  # Set the seed for reproducibility

Gewinnraten = []

TrainingsSchritte = 20
EpisodenProSchritt = 10000
SpieleProMessung = 500


def Gewinnrate():
    #QTrained plays SpieleProMessung games as player 2 and as player 1, draws count as no win
    game_1 = play(randomStr, QTrained, SpieleProMessung)
    game_2 = play(QTrained, randomStr, SpieleProMessung)
    rate = 100 * (game_1[1] + game_2[0]) / (2 * SpieleProMessung) # gewinnrate in %
    zeit = (game_1[2][1] + game_2[2][0]) / 2 * 1000 #Durchschnittliche Rechenzeit pro Zug in [ms]
    return rate, zeit


rate, zeit, fehler = Gewinnrate()
Gewinnraten.append(rate)
print(f"nach 0 Trainingsepisoden: {rate:.1f}% ({zeit:.2f} ms pro Zug)", flush=True) #:.xf rounds to x decimal places

for i in range(TrainingsSchritte):
    train(EpisodenProSchritt)
    rate, zeit = Gewinnrate()
    Gewinnraten.append(rate)
    print(f"nach {(i+1) * EpisodenProSchritt:,} ".replace(",", "'"), f"Trainingsepisoden: {rate:.1f}% ({zeit:.2f} ms pro Zug)", flush=True)

plt.plot(range(0, TrainingsSchritte * EpisodenProSchritt, EpisodenProSchritt), Gewinnraten)
plt.xlabel("Trainingsepisoden")
plt.ylabel("Gewinnrate in %")
plt.title("Entwicklung der Gewinnrate")
plt.grid(alpha=0.3) #grid opacity
plt.show()

#this shows us how the Q-Learning-Str is getting better by training

"""
from QLearning import saveQTable
saveQTable()    #speichert die trainierte Q-Tabelle inkl. Anzahl Trainingsspiele in QTable.pkl
"""