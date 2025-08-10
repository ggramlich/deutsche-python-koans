# 🤔 Koans zu if-Anweisungen
# Ersetze __ durch den richtigen Wert, sodass kein Fehler mehr auftritt.

__ = None  # Platzhalter – bitte ersetzen!

# 🟢 Was passiert, wenn die Bedingung wahr ist?
ergebnis = "original"
if True:
    ergebnis = "aktualisiert"
assert ergebnis == __, "Was steht jetzt in 'ergebnis'?"

# 🔴 Was passiert, wenn die Bedingung falsch ist?
ergebnis = "original"
if False:
    ergebnis = "aktualisiert"
assert ergebnis == __, "Was steht jetzt in 'ergebnis'?"

# 🟢 else-Zweig bei True
ergebnis = "original"
if True:
    ergebnis = "True-Zweig"
else:
    ergebnis = "False-Zweig"
assert ergebnis == __, "Welcher Zweig wurde ausgeführt?"

# 🔴 else-Zweig bei False
ergebnis = "original"
if False:
    ergebnis = "True-Zweig"
else:
    ergebnis = "False-Zweig"
assert ergebnis == __, "Welcher Zweig wurde ausgeführt?"

# 🅰️ Ist ein Buchstabe ein Vokal?
vokale = "aeiou"
buchstabe = "f"
if buchstabe in vokale:
    ergebnis = "ist Vokal"
else:
    ergebnis = "kein Vokal"
assert ergebnis == __, "Ist 'f' ein Vokal?"
