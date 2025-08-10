# 📦 Koans zu Listen
# Ersetze __ durch den richtigen Wert, sodass kein Fehler mehr auftritt.

__ = None  # Platzhalter – bitte ersetzen!

# 📦 Eine leere Liste
leere_liste = []
assert type(leere_liste) == list, "Ist 'leere_liste' vom richtigen Typ?"
assert len(leere_liste) == __, "Wie viele Elemente sind in der Liste?"

# 🍞 Liste mit Wörtern
noms = ["Erdnuss", "Butter", "und", "Marmelade"]
assert noms[0] == __, "Was steht an erster Stelle in der Liste?"
assert noms[3] == __, "Was steht an vierter Stelle in der Liste?"

# 📚 Slicing
assert noms[0:1] == __, "Was ergibt noms[0:1]?"
assert noms[0:2] == __, "Was ergibt noms[0:2]?"
assert noms[2:] == __, "Was kommt heraus, wenn du ab Index 2 ausschneidest?"
assert noms[:2] == __, "Was ergibt noms[:2]?"

# 🔢 Zahlenbereiche
assert list(range(3)) == __, "Was ergibt list(range(3))?"
assert list(range(3, 6)) == __, "Was ergibt list(range(3, 6))?"

# 🧰 Operationen mit Listen
ritter = ["du", "sollst", "vorbeigehen"]
ritter.insert(2, "nicht")
assert ritter == __, "Wie sieht ritter nach dem Einfügen aus?"
ritter.insert(0, "Arthur")
assert ritter == __, "Und jetzt?"

# 🧪 Stack-Operationen
stapel = [1, 2, 3]
stapel.append("letztes")
assert stapel == __, "Was steht alles im Stapel nach append?"
entfernt = stapel.pop()
assert entfernt == __, "Was wurde vom Stapel entfernt?"
assert stapel == __, "Wie sieht der Stapel jetzt aus?"
