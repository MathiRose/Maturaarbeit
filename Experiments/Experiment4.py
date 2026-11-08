import pygame

from environement import game
from human import humanStr
from Minimax import MinimaxMitTiefe
from randomStr import randomStr
import QLearning

MinimaxTiefe = 3  #Standardsuchtiefe für Minimax (höher ist stärker, lässt das Fenster aber länger einfrieren)



def Menue():
    print("\nGegen welche KI möchtest du spielen?")
    print("  1) Zufall")
    print("  2) Minimax")
    print("  3) Q-Learning (trainiert)")

    while True:
        wahl = input("Deine Wahl (1-3): ").strip()
        if wahl in ("1", "2", "3"):
            break
        print("Bitte 1, 2 oder 3 eingeben.")

    if wahl == "1":
        return "Zufall", randomStr

    if wahl == "2":
        tiefe = input(f"Suchtiefe (1-7, Standard {MinimaxTiefe}): ").strip()
        tiefe = int(tiefe) if tiefe.isdigit() and 1 <= int(tiefe) <= 7 else MinimaxTiefe #ist tiefe eine zahl und ist tiefe zwischen 1 und 7
        return f"Minimax (Tiefe {tiefe})", MinimaxMitTiefe(tiefe)

    try:
        QLearning.loadQTable()
        print(f"Q-Tabelle geladen ({QLearning.TrainierteSpiele:,} Trainingsspiele)".replace(",", "'"))
    except FileNotFoundError:
        print("keine QTable.pkl gefunden - Q-Learning spielt mit einer zufälligen Q-Tabelle")
    return "Q-Learning", QLearning.QTrained


def Spielen(gegnerName, gegner):
    print(f"\nDu spielst gegen {gegnerName}.")
    print("Steuerung: Pfeiltasten links/rechts zum Verschieben, Leertaste zum Einwerfen.")
    beginnt = input("Möchtest du beginnen (gelb)? (j/n): ").strip().lower() != "n"

    mensch = 1 if beginnt else 2  #Spieler 1 ist gelb und beginnt

    if beginnt:
        result = game(humanStr, gegner)
    else:
        result = game(gegner, humanStr)

    if result[0] == 'draw':
        print("Unentschieden - das Brett ist voll.")
    elif result[1] == mensch:
        print("Du hast gewonnen!")
    else:
        print("Die KI hat gewonnen.")

    pygame.quit()  #Fenster schliessen, damit das nächste Spiel sauber startet


while True:
    name, gegner = Menue()
    Spielen(name, gegner)

    if input("\nNoch eine Partie? (j/n): ").strip().lower() == "n":
        break

print("Danke fürs Spielen!")

#this lets us test the KIs by hand and feel where they are still weak