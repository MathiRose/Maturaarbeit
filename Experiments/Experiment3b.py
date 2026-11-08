from evaluation import play
from Minimax import MinimaxMitTiefe
from randomStr import randomStr
import QLearning
import matplotlib.pyplot as plt
import random

seed = input("Gib einen seed für den zufälligen Zahlengenerator ein (oder lasse leer für zufällig): ")
if seed:
    random.seed(seed)  # Set the seed for reproducibility

MinimaxTiefe = 3  #Tiefe 4 oder 5 sind stärker, machen das Turnier aber deutlich langsamer
SpieleProDuell = 20  #Partien pro Paarung pro Farbe
ZufallsZuege = 2  #Anzahl zufälliger Züge am Anfang jeder Partie, siehe MitZufallseroeffnung()
TrainingsspieleFallsKeineQTable = 100000  #falls noch keine QTable.pkl existiert


def MitZufallseroeffnung(strategie, zuege=ZufallsZuege): #gleich wie 2b, können jedoch nicht importieren wegen main() code :(
    def Strategie(board, player):
        anzahlSteine = sum(1 for spalte in board for feld in spalte if feld != 0)
        if anzahlSteine < zuege:
            return randomStr(board, player)
        return strategie(board, player)
    return Strategie

def Duell(str1, str2, games): #gleich wie 2b
    als_Spieler1 = play(str1, str2, games)  #str1 beginnt
    als_Spieler2 = play(str2, str1, games)  #str2 beginnt, str1 ist also Spieler 2

    siege1 = als_Spieler1[0] + als_Spieler2[1]
    siege2 = als_Spieler1[1] + als_Spieler2[0]
    remis = 2*games - siege1 - siege2

    zeit1 = (als_Spieler1[2][0] + als_Spieler2[2][1]) / 2 * 1000  #Rechenzeit von str1 pro Zug in [ms]
    zeit2 = (als_Spieler1[2][1] + als_Spieler2[2][0]) / 2 * 1000  #Rechenzeit von str2 pro Zug in [ms]
    return siege1, remis, siege2, zeit1, zeit2


try:  #die trainierte Q-Tabelle laden, sonst wäre der Vergleich mit Q-Learning nicht fair
    QLearning.loadQTable()
    print(f"Q-Tabelle geladen ({QLearning.TrainierteSpiele:,} Trainingsspiele)".replace(",", "'"), flush=True)
except FileNotFoundError:
    print(f"keine QTable.pkl gefunden - trainiere {TrainingsspieleFallsKeineQTable:,} Spiele".replace(",", "'"), flush=True)
    QLearning.train(TrainingsspieleFallsKeineQTable)

Strategien = [ #gleich wie 3a
    ("Zufall", randomStr),
    (f"Minimax (Tiefe {MinimaxTiefe})", MitZufallseroeffnung(MinimaxMitTiefe(MinimaxTiefe))),
    ("Q-Learning (trainiert)", MitZufallseroeffnung(QLearning.QTrained)),
]

anzahl = len(Strategien)
punkte = [0] * anzahl  #1 Punkt für einen Sieg, 0.5 für ein Remis, 0 für eine Niederlage
siege = [0] * anzahl
remis = [0] * anzahl
niederlagen = [0] * anzahl
zeiten = [[] for _ in range(anzahl)]  #Rechenzeit pro Zug in jeder Paarung

print("\nRound-Robin-Turnier - jede Strategie spielt gegen jede andere:\n", flush=True)
for i in range(anzahl):
    for j in range(i + 1, anzahl):
        s_i, r, s_j, zeit_i, zeit_j = Duell(Strategien[i][1], Strategien[j][1], SpieleProDuell)

        punkte[i] += s_i + r / 2
        punkte[j] += s_j + r / 2
        siege[i] += s_i
        remis[i] += r
        niederlagen[i] += s_j
        siege[j] += s_j
        remis[j] += r
        niederlagen[j] += s_i
        zeiten[i].append(zeit_i)
        zeiten[j].append(zeit_j)

        print(f"{Strategien[i][0]} gegen {Strategien[j][0]}: "
              f"{s_i} Siege, {r} Unentschieden, {s_j} Niederlagen", flush=True)

print("\nRangliste (1 Punkt für Sieg, 0.5 für Unentschieden, 0 für Niederlage):\n", flush=True)
print(f"{'Rang':>4} | {'Strategie':<22} | {'Punkte':>6} | {'Punktequote':>11} | "
      f"{'S/U/N':>11} | {'Zeit pro Zug':>12}", flush=True)

rangliste = sorted(range(anzahl), key=lambda k: punkte[k], reverse=True) #range(anzahl) wird sortiert nach punkten, reverse --> von gross zu klein
for rang, k in enumerate(rangliste, start=1):
    spiele = siege[k] + remis[k] + niederlagen[k] # = SpieleProDuell * (anzahl -1)
    quote = 100 * punkte[k] / spiele  # Punktequote in %
    zeit = sum(zeiten[k]) / len(zeiten[k])  # Mittelwert über alle Paarungen in [ms]
    bilanz = f"{siege[k]}/{remis[k]}/{niederlagen[k]}"
    print(f"{rang:>4} | {Strategien[k][0]:<22} | {punkte[k]:>6.1f} | {quote:>10.1f}% | "
          f"{bilanz:>11} | {zeit:>9.2f} ms", flush=True)

Namen = [Strategien[k][0] for k in rangliste]
Quoten = [100 * punkte[k] / (siege[k] + remis[k] + niederlagen[k]) for k in rangliste]

plt.bar(Namen, Quoten)
plt.axhline(50, color="grey", linestyle="--", linewidth=1)  #50% bedeutet ausgeglichene Duelle
plt.ylabel("Punktequote im Turnier in %")
plt.title("Rangliste der Strategien (Round-Robin-Turnier)")
plt.ylim(0, 100)
plt.grid(alpha=0.3, axis="y")  #grid opacity
plt.show()

#this shows us which strategy is the strongest when they all play against each other
