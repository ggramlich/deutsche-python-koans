# 🔁 Koans zu while-Schleifen
# Ersetze __ durch den richtigen Wert, sodass kein Fehler mehr auftritt.

__ = None  # Platzhalter – bitte ersetzen!

# 🔢 Rückwärts zählen
zahlen = ""
index = 3
while index > 0:
    index = index - 1
    zahlen = zahlen + str(index)
assert zahlen == __, "Wie sieht die Zahlenreihe aus?"

# 🔢 Rückwärts zählen (andere Reihenfolge)
zahlen = ""
index = 3
while index > 0:
    zahlen = zahlen + str(index)
    index = index - 1
assert zahlen == __, "Wie sieht die Zahlenreihe aus?"

# 🔍 Ersten Index eines Buchstabens finden
satz = "Herr der Ringe"
index = 0
while not satz[index] == "R":
    index = index + 1
assert index == __, "An welcher Stelle steht 'R'?"

# 🔍 Ersten Index eines Vokals finden
vokale = "aeiou"
satz = "Pdrlso"
index = 0
while not satz[index] in vokale:
    index = index + 1
assert index == __, "An welcher Stelle steht der erste Vokal?"
