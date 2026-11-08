## Maturaarbeit
Meine Maturaarbeit in welcher ich selbstständig KI für Viergewinnt programmiere und vergleiche.

## Bedienungsanleitung
Zuerst müssen die Libs mit folgender Zeile instaliert werden: \
`python -m pip install -r requirements.txt`

Um eines der Experimente durchzuführen sollte man im projekt-folder folgende Codezeile eingeben, wobei man N mit der Nummer des Experiments ersetzen sollte. \
`python -m Experiments.ExperimentN`

# Trainingsparameter (QLearning.py)
- `Lernrate = 0.1` und `Exploration = 0.3` sind die Startwerte, exploration sinkt bis auf `MinExploration = 0.01`
- `DecayEpisoden = 150000` legt fest, nach wie vielen Trainingsspielen die Minimalwerte erreicht sind (danach bleiben sie konstant, damit sich die Q-Werte stabilisieren können)
- `DiscountFactor = -0.95` ist negativ, weil eine gute position für den Gegner eine schlechte für uns ist

# Q-Tabelle speichern und laden
`saveQTable("QTable.pkl")` speichert die Q-Tabelle zusammen mit der Anzahl Trainingsspiele, `loadQTable("QTable.pkl")` lädt beides wieder. 

## Experimente
# Experiment 1
Hier werde ich auf unterschiedliche Arten überprüfen ob QLearning tatsächlich lernt.
1a. zeigt wie sich die Gewinnrate vor und nach dem Training unterscheidet
1b. erstellt mit matplotlib ein Diagramm um die entwicklung der Spielstärke zu zeigen.
1c. zeigt dass QLearning ein einfaches Muster erkennen und dagegen ankommen kann.

# Experiment 2
Hier werde ich herausfinden wie die Performance von Minimax mit der Suchtiefe zusammenhängt.
2a. zeigt Gewinnrate und Rechenzeit pro Zug von Minimax gegen randomStr für verschiedene Suchtiefen (Tabelle + Diagramm)
2b. lässt verschiedene Suchtiefen direkt gegeneinander spielen, um zu zeigen dass tiefer suchen tatsächlich stärker macht und nicht nur langsamer

# Experiment 3
Hier werde ich die KI strategien vergleichen.
3a. vergleicht alle Strategien gegen dieselbe Referenz (randomStr), damit die Gewinnraten vergleichbar sind
3b. lässt alle Strategien in einem Round-Robin-Turnier gegeneinander spielen und erstellt daraus eine Rangliste

# Experiment 4 (optional)
Hier kann man selbstständig gegen die KIs antreten. Man wählt im Menü den Gegner (Zufall, Minimax inkl. Suchtiefe oder Q-Learning) und ob man selber beginnen möchte.
Steuerung: Pfeiltasten links/rechts zum Verschieben, Leertaste zum Einwerfen.

