from evaluation import play
from QLearning import QTrained, train
from randomStr import randomStr
import random

"""
from QLearning import loadQTable
loadQTable()
"""
TrainingsSchritte = 20
EpisodenProSchritt = 10000
SpieleProMessung = 500

seed = input("Gib einen seed für den zufälligen Zahlengenerator ein (oder lasse leer für zufällig): ")
if seed:
    random.seed(seed)  # Set the seed for reproducibility

print("\nvor dem Training")
game_1 = play(randomStr, QTrained, SpieleProMessung)
game_2 = play(QTrained, randomStr, SpieleProMessung)
print(f"Gewinnrate: {(game_1[1]+game_2[0])/10}%")
print(f"Durchschnittliche Rechenzeit pro Zug in [ms]: {(game_1[2][1]+game_2[2][0])/2*1000}\n")
for i in range(TrainingsSchritte):
    train(EpisodenProSchritt)
    print(f"\nnach {(EpisodenProSchritt/1000)*(i+1)}'000 Trainingsepisoden")
    game_1 = play(randomStr, QTrained, SpieleProMessung)
    game_2 = play(QTrained, randomStr, SpieleProMessung)
    print(f"Gewinnrate: {(game_1[1]+game_2[0])/10}%")
    print(f"Durchschnittliche Rechenzeit pro Zug in [ms]: {(game_1[2][1]+game_2[2][0])/2*1000}\n")

#this shows us weather the Q-Learning-Str is actually getting better by training

"""
from QLearning import saveQTable

saveQTable()    #speichert die trainierte Q-Tabelle inkl. Anzahl Trainingsspiele in QTable.pkl
"""
