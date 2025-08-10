# 🗂️ Koans zu Dictionaries (Wörterbüchern)
# Ersetze __ durch den richtigen Wert, sodass kein Fehler mehr auftritt.

__ = None  # Platzhalter – bitte ersetzen!

# 📦 Ein leeres Wörterbuch
leeres_dict = dict()
assert type(leeres_dict) == dict, "Ist 'leeres_dict' vom richtigen Typ?"
assert leeres_dict == {}, "Ist das Wörterbuch wirklich leer?"
assert len(leeres_dict) == __, "Wie viele Einträge sind im Wörterbuch?"

# 📚 Wörterbuch mit Übersetzungen
babel_fisch = {'eins': 'one', 'zwei': 'two'}
assert len(babel_fisch) == __, "Wie viele Wörter sind im Wörterbuch?"

# 🔍 Zugriff auf Werte
assert babel_fisch['eins'] == __, "Was bedeutet 'eins'?"
assert babel_fisch['zwei'] == __, "Was bedeutet 'zwei'?"

# ✏️ Wert ändern
babel_fisch['eins'] = 'uno'
erwartet = {'eins': __, 'zwei': 'two'}
assert babel_fisch == erwartet, "Wie sieht das Wörterbuch jetzt aus?"

# 🔄 Reihenfolge ist egal
dict1 = {'eins': 'one', 'zwei': 'two'}
dict2 = {'zwei': 'two', 'eins': 'one'}
assert dict1 == dict2, "Sind die Wörterbücher gleich?"

# 🗝️ Schlüssel und Werte
assert len(babel_fisch.keys()) == __, "Wie viele Schlüssel gibt es?"
assert len(babel_fisch.values()) == __, "Wie viele Werte gibt es?"
assert 'eins' in babel_fisch.keys() == __, "Gibt es 'eins' als Schlüssel?"
assert 'two' in babel_fisch.values() == __, "Gibt es 'two' als Wert?"
assert 'uno' in babel_fisch.keys() == __, "Gibt es 'uno' als Schlüssel?"
assert 'two' in babel_fisch.values() == __, "Gibt es 'two' als Wert?"
