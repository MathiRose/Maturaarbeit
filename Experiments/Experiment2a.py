from evaluation import play
from Minimax import MinimaxMitTiefe
from randomStr import randomStr
import matplotlib.pyplot as plt
import random

seed = input("Gib einen seed für den zufälligen Zahlengenerator ein (oder lasse leer für zufällig): ")
if seed:
    random.seed(seed)  # Set the seed for reproducibility

Tiefen = [1, 2, 3, 4, 5]  #ab Tiefe 6 wird ein einzelnes Spiel bereits mehrere Sekunden lang
SpieleProMessung = 100  #Partien pro Suchtiefe und Farbe


def Messung(tiefe):
    #Minimax spielt SpieleProMessung Partien als Spieler 1 und als Spieler 2, Remis zählen nicht als Sieg
    game_1 = play(MinimaxMitTiefe(tiefe), randomStr, SpieleProMessung)
    game_2 = play(randomStr, MinimaxMitTiefe(tiefe), SpieleProMessung)

    siege = game_1[0] + game_2[1]
    niederlagen = game_1[1] + game_2[0]
    remis = 2 * SpieleProMessung - siege - niederlagen
    gewinnrate = 100 * siege / (2 * SpieleProMessung)  # Gewinnrate in %
    zeit = (game_1[2][0] + game_2[2][1]) / 2 * 1000  # Durchschnittliche Rechenzeit pro Zug in [ms]
    return gewinnrate, remis, niederlagen, zeit


Gewinnraten = []
Zeiten = []

print(f"{'Tiefe':>5} | {'Gewinnrate':>10} | {'Remis':>5} | {'Niederlagen':>11} | {'Zeit pro Zug':>12}", flush=True) # :>5 --> rechtsbündig, 5 Zeichen lang (formatierung)
for tiefe in Tiefen:
    rate, remis, niederlagen, zeit = Messung(tiefe)
    Gewinnraten.append(rate)
    Zeiten.append(zeit)
    print(f"{tiefe:>5} | {rate:>9.1f}% | {remis:>5} | {niederlagen:>11} | {zeit:>9.2f} ms", flush=True) # 1f --> fixpointnotation (eine Zahl nach Komma)

fig, achse_1 = plt.subplots()
achse_1.plot(Tiefen, Gewinnraten, marker="o", color="tab:blue") ## marker=o zeichnet kreise an Datenpunkten
achse_1.set_xlabel("Suchtiefe")
achse_1.set_ylabel("Gewinnrate gegen randomStr in %", color="tab:blue")
achse_1.set_ylim(0, 105)
achse_1.set_xticks(Tiefen)
achse_1.grid(alpha=0.3)  #grid opacity

achse_2 = achse_1.twinx()  #zweite y-Achse für die Rechenzeit
achse_2.plot(Tiefen, Zeiten, marker="s", color="tab:red")
achse_2.set_ylabel("Rechenzeit pro Zug in [ms] (logarithmisch)", color="tab:red")
achse_2.set_yscale("log")

plt.title("Minimax: Spielstärke und Rechenzeit in Abhängigkeit der Suchtiefe")
plt.show()

#this shows us that minimax can beat randomStr and how time per turn scales exponentially
