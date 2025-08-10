# 👫 Koans zu Tupeln
# Ersetze __ durch den richtigen Wert, sodass kein Fehler mehr auftritt.

__ = None  # Platzhalter – bitte ersetzen!

# 👫 Ein Tupel erstellen
drei = (1, 2, 5)
assert drei[2] == __, "Was steht an dritter Stelle?"

# 👫 Tupel sind unveränderlich
try:
    drei[2] = "drei"
except TypeError as ex:
    fehler = ex.args[0]
assert "object does not support item assignment" in fehler, "Was passiert beim Ändern?"

# 👫 Tupel können nicht erweitert werden
try:
    drei.append("boom")
except Exception as ex:
    fehler = type(ex)
assert fehler == __, "Welcher Fehler kommt?"

# 👫 Tupel können durch Umwandlung geändert werden
liste = list(drei)
liste.append("boom")
drei = tuple(liste)
assert drei == __, "Wie sieht das Tupel jetzt aus?"

# 👫 Tupel mit nur einem Element
assert type((1,)) == __, "Was ist der Typ von (1,)?"
assert ("Hallo Komma!", ) == __, "Wie sieht ein Tupel mit einem String aus?"

# 👫 Tupel aus einem String
assert tuple("Überraschung!") == __, "Was ergibt tuple aus einem String?"

# 👫 Leere Tupel
assert () == __, "Wie sieht ein leeres Tupel aus?"
assert tuple() == __, "Wie sieht ein leeres Tupel aus?"

# 👫 Tupel können verschachtelt sein
lat = (37, 14, 6, "N")
lon = (115, 48, 40, "W")
ort = ("Area 51", lat, lon)
assert ort == __, "Wie sieht das verschachtelte Tupel aus?"

# 👫 Tupel als Datensätze
orte = [
    ("Illuminati HQ", (38, 52, 15.56, "N"), (77, 3, 21.46, "W")),
    ("Stargate B", (41, 10, 43.92, "N"), (1, 49, 34.29, "W")),
]
orte.append(("Cthulu", (26, 40, 1, "N"), (70, 45, 7, "W")))
assert orte[2][0] == __, "Wie heißt der dritte Ort?"
assert orte[0][1][2] == __, "Was steht an dritter Stelle der Koordinaten?"
