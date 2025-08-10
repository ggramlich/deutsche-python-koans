# 🤔 Koans zu Wahr und Falsch (True/False)
# Ersetze __ durch den richtigen Wert, sodass kein Fehler mehr auftritt.

__ = None  # Platzhalter – bitte ersetzen!

# ✅ True ist wahr
def ist_wahr(bedingung):
    if bedingung:
        return "wahr"
    else:
        return "falsch"
assert ist_wahr(True) == __, "Was gibt die Funktion zurück, wenn es wahr ist?"

# ❌ False ist falsch
assert ist_wahr(False) == __, "Was gibt die Funktion zurück, wenn es falsch ist?"

# ❌ None ist auch falsch
assert not __, "Ist None falsch?"

# ❌ 0 ist auch falsch
assert not __, "Ist 0 falsch?"

# ❌ Leere Listen, Mengen, Wörterbücher und Tupel sind falsch
assert not [], "Ist eine leere Liste falsch?"
assert not set(), "Ist eine leere Menge falsch?"
assert not {}, "Ist ein leeres Wörterbuch falsch?"
assert not (), "Ist ein leeres Tupel falsch?"

# ✅ Ein leerer String ist auch falsch
assert not "", "Ist ein leerer String falsch?"

# ✅ Alles andere ist wahr
assert bool(1), "Ist 1 wahr?"
assert bool((1,)), "Ist ein Tupel mit Inhalt wahr?"
assert bool("Python ist cool"), "Ist ein String mit Inhalt wahr?"
assert bool(" "), "Ist ein String mit Leerzeichen wahr?"
assert bool("0"), "Ist ein String mit '0' wahr?"
