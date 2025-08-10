# 🔁 Koans zu Schleifen
# Ersetze __ durch den richtigen Wert, sodass kein Fehler mehr auftritt.

__ = None  # Platzhalter – bitte ersetzen!

# 🔁 Alle Wörter groß schreiben
satz = ["fisch", "und", "pommes"]
ergebnis = []
for wort in satz:
    ergebnis.append(wort.upper())
assert ergebnis == [__, __, __], "Wie sieht die Liste aus?"

# 🏰 Ritter und Antworten
runde_tafel = [
    ["Lancelot", "Blau"],
    ["Galahad", "Ich weiß nicht!"],
    ["Robin", "Blau! Ich meine Grün!"],
    ["Arthur", "Ist das eine afrikanische oder eine europäische Schwalbe?"],
]
ergebnis = []
for ritter, antwort in runde_tafel:
    ergebnis.append(f"Teilnehmer: '{ritter}' Antwort: '{antwort}'")
assert ergebnis[0] == __, "Was steht an erster Stelle?"
assert ergebnis[1] == __, "Was steht an zweiter Stelle?"
assert ergebnis[2] == __, "Was steht an dritter Stelle?"
assert ergebnis[3] == __, "Was steht an vierter Stelle?"

# 🧑‍🎤 Wer ist nach 1941 geboren?
pythons = [
    ("John Cleese", 1939),
    ("Terry Gilliam", 1940),
    ("Eric Idle", 1943),
    ("Michael Palin", 1943),
]
spaeter_geboren = []
for name, jahr in pythons:
    if jahr > 1941:
        spaeter_geboren.append(name)
assert spaeter_geboren == __, "Wer ist nach 1941 geboren?"

# 🔢 while-Schleife: Zahlen addieren
i = 1
summe = 1
while i <= 10:
    summe = summe + i
    i = i + 1
assert summe == __, "Was ist die Summe?"

# 🔁 while mit break
i = 1
summe = 1
while True:
    if i > 10:
        break
    summe = summe + i
    i = i + 1
assert summe == __, "Was ist die Summe?"

# 🔁 while mit continue
i = 0
ergebnis = []
while i < 10:
    i = i + 1
    if (i % 2) == 0:
        continue
    ergebnis.append(i)
assert ergebnis == __, "Welche Zahlen sind im Ergebnis?"
