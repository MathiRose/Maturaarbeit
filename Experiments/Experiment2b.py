from evaluation import play
from Minimax import MinimaxMitTiefe
from randomStr import randomStr
import matplotlib.pyplot as plt
import random

seed = input("Gib einen seed für den zufälligen Zahlengenerator ein (oder lasse leer für zufällig): ")
if seed:
    random.seed(seed)  # Set the seed for reproducibility

Tiefen = [1, 2, 3, 4]  #jede Suchtiefe wird gegen die nächst kleinere Suchtiefe verglichen
SpieleProDuell = 10  #Partien pro Farbe, total also 2*SpieleProDuell Partien pro Duell
ZufallsZuege = 2  #Anzahl zufälliger Züge am Anfang jeder Partie, siehe MitZufallseroeffnung()



def MitZufallseroeffnung(strategie, zuege=ZufallsZuege):
    #Minimax ist deterministisch, ohne zufällige Eröffnung wären alle Partien einer Paarung identisch
    def Strategie(board, player):
        anzahlSteine = sum(1 for spalte in board for feld in spalte if feld != 0)
        if anzahlSteine < zuege:
            return randomStr(board, player)
        return strategie(board, player)
    return Strategie


def Duell(str1, str2, games):
    #die Hälfte der Partien beginnt str1, die andere Hälfte str2, damit der Anzugsvorteil ausgeglichen ist
    als_Spieler1 = play(str1, str2, games)  #str1 beginnt
    als_Spieler2 = play(str2, str1, games)  #str2 beginnt, str1 ist also Spieler 2

    siege1 = als_Spieler1[0] + als_Spieler2[1]
    siege2 = als_Spieler1[1] + als_Spieler2[0]
    remis = 2*games - siege1 - siege2

    zeit1 = (als_Spieler1[2][0] + als_Spieler2[2][1]) / 2 * 1000  #Rechenzeit von str1 pro Zug in [ms]
    zeit2 = (als_Spieler1[2][1] + als_Spieler2[2][0]) / 2 * 1000  #Rechenzeit von str2 pro Zug in [ms]
    return siege1, remis, siege2, zeit1, zeit2


Gewinnraten = []
Paare = []

# print("Achtung: Duelle zwischen zwei Minimax-Strategien dauern je nach Suchtiefe mehrere Minuten.\n", flush=True)

for tiefe in Tiefen[1:]:
    tiefer = MitZufallseroeffnung(MinimaxMitTiefe(tiefe))
    flacher = MitZufallseroeffnung(MinimaxMitTiefe(tiefe - 1))

    siege, remis, niederlagen, zeit_tief, zeit_flach = Duell(tiefer, flacher, SpieleProDuell)
    gewinnrate = 100 * siege / (2*SpieleProDuell) #in %

    Gewinnraten.append(gewinnrate)
    Paare.append(f"{tiefe} gegen {tiefe - 1}")

    print(f"Tiefe {tiefe} gegen Tiefe {tiefe - 1}: {siege:3} Siege, {remis:3} Remis, "
          f"{niederlagen:3} Niederlagen ({zeit_tief:.1f} ms vs {zeit_flach:.1f} ms pro Zug)", flush=True)

plt.bar(Paare, Gewinnraten)
plt.axhline(50, color="grey", linestyle="--", linewidth=1)  #50% bedeutet kein Unterschied  
plt.xlabel("Duell der Suchtiefen")
plt.ylabel("Gewinnrate der tieferen Suche in %")
plt.title("Bringt eine grössere Suchtiefe einen Vorteil?")
plt.ylim(0, 100)
plt.grid(alpha=0.3, axis="y")  #grid opacity
plt.show()

#this shows us that a larger depth is really stronger and not only slower
