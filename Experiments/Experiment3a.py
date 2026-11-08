from evaluation import play
from Minimax import MinimaxMitTiefe
from randomStr import randomStr
import QLearning
import matplotlib.pyplot as plt
import random

seed = input("Gib einen seed für den zufälligen Zahlengenerator ein (oder lasse leer für zufällig): ")
if seed:
    random.seed(seed)  # Set the seed for reproducibility

MinimaxTiefe = 3  #Tiefe 4 oder 5 sind stärker, machen den Vergleich aber deutlich langsamer
SpieleProMessung = 100  #Partien pro Strategie und Farbe, total also 2*SpieleProMessung
TrainingsspieleFallsKeineQTable = 100000  #falls noch keine QTable.pkl existiert



try:  #die trainierte Q-Tabelle laden, sonst wäre der Vergleich mit Q-Learning nicht fair
    QLearning.loadQTable()
    print(f"Q-Tabelle geladen ({QLearning.TrainierteSpiele:,} Trainingsspiele)".replace(",", "'"), flush=True)
except FileNotFoundError:
    print(f"keine QTable.pkl gefunden - trainiere {TrainingsspieleFallsKeineQTable:,} Spiele".replace(",", "'"), flush=True)
    QLearning.train(TrainingsspieleFallsKeineQTable)

Strategien = [
    ("Zufall", randomStr),  #dient als Referenz, weil z.B. remies eine gewinnrate unter 50% bringen könnte
    (f"Minimax (Tiefe {MinimaxTiefe})", MinimaxMitTiefe(MinimaxTiefe)),
    ("Q-Learning (trainiert)", QLearning.QTrained),
]

Gewinnraten = []
Namen = []

print(f"\n{'Strategie':<22} | {'Gewinnrate':>10} | {'Unentschieden':>13} | {'Niederlagen':>11} | {'Zeit pro Zug':>12}", flush=True)
for name, strategie in Strategien:
    #jede Strategie spielt SpieleProMessung Partien als Spieler 1 und als Spieler 2 gegen randomStr
    als_Spieler1 = play(strategie, randomStr, SpieleProMessung)
    als_Spieler2 = play(randomStr, strategie, SpieleProMessung)

    siege = als_Spieler1[0] + als_Spieler2[1]
    niederlagen = als_Spieler1[1] + als_Spieler2[0]
    remis = 2 * SpieleProMessung - siege - niederlagen
    rate = 100 * siege / (2 * SpieleProMessung)  # Gewinnrate in %
    zeit = (als_Spieler1[2][0] + als_Spieler2[2][1]) / 2 * 1000  # Rechenzeit pro Zug in [ms]

    Gewinnraten.append(rate)
    Namen.append(name)
    print(f"{name:<22} | {rate:>9.1f}% | {remis:>13} | {niederlagen:>11} | {zeit:>9.2f} ms", flush=True)

plt.bar(Namen, Gewinnraten)
plt.axhline(50, color="grey", linestyle="--", linewidth=1)  #50% entspricht dem Niveau von randomStr
plt.ylabel("Gewinnrate gegen randomStr in %")
plt.title("Vergleich der Strategien gegen die gleiche Referenz")
plt.ylim(0, 100)
plt.grid(alpha=0.3, axis="y")  #grid opacity
plt.show()

#this shows us how much stronger each strategy is than pure randomness
