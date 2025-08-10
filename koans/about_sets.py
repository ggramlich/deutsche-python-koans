# 🧺 Koans zu Mengen (Sets)
# Ersetze __ durch den richtigen Wert, sodass kein Fehler mehr auftritt.

__ = None  # Platzhalter – bitte ersetzen!

# 🧺 Mengen machen Listen einzigartig
highlanders = [
    "MacLeod", "Ramirez", "MacLeod", "Matunas",
    "MacLeod", "Malcolm", "MacLeod"
]
einzigartige = set(highlanders)
assert einzigartige == __, "Welche Namen sind einzigartig?"

# 🧺 Leere und gefüllte Mengen
assert {1, 2, 3} == __, "Wie sieht eine gefüllte Menge aus?"
assert set() == __, "Wie sieht eine leere Menge aus?"

# 🧺 Mengen aus Zeichen
assert {"12345"} == __, "Was ergibt eine Menge mit einem String?"
assert set("12345") == __, "Was ergibt eine Menge aus einzelnen Zeichen?"

# 🧺 Sortierte Menge
assert sorted(set("12345")) == __, "Wie sieht die sortierte Menge aus?"

# ➕➖ Mengen-Operationen
schotten = {"MacLeod", "Wallace", "Willie"}
krieger = {"MacLeod", "Wallace", "Leonidas"}
assert schotten - krieger == __, "Was bleibt übrig?"
assert schotten | krieger == __, "Was ergibt die Vereinigung?"
assert schotten & krieger == __, "Was ergibt die Schnittmenge?"
assert schotten ^ krieger == __, "Was ergibt die symmetrische Differenz?"

# 🔍 Ist etwas in der Menge?
assert 127 in {127, 0, 1} == __, "Ist 127 in der Menge?"
assert "kuh" not in set("apocalypse now") == __, "Ist 'kuh' in der Menge?"

# 🔎 Teilmengen vergleichen
assert set("kuchen") <= set("kirschkuchen") == __, "Ist 'kuchen' eine Teilmenge?"
assert set("kuchen").issubset(set("kirschkuchen")) == __, "Ist 'kuchen' eine Teilmenge?"
assert set("kuchen") > set("torte") == __, "Ist 'kuchen' größer als 'torte'?"
