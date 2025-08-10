# 📝 Koans zu Strings
# Ersetze __ durch den richtigen Wert, sodass kein Fehler mehr auftritt.

__ = None  # Platzhalter – bitte ersetzen!

# 📝 Ein String mit Anführungszeichen
text = "Hallo, Welt."
assert type(text) == __, "Welcher Typ ist das?"

# 🔢 String aus einer Zahl
text = str(123)
assert type(text) == __, "Welcher Typ ist das?"

# ➕ Strings verbinden
text = "Hallo, " + "Welt"
assert text == __, "Was ergibt die Verbindung?"

# ➕ Ursprüngliche Strings bleiben erhalten
hallo = "Hallo, "
dort = "Welt"
verbunden = hallo + dort
assert hallo == __, "Was steht in 'hallo'?"
assert dort == __, "Was steht in 'dort'?"
assert verbunden == __, "Was steht in 'verbunden'?"

# 🔢 Länge eines Strings
kurz = "hi"
assert len(kurz) == __, "Wie lang ist der String?"

# 🧩 String zerlegen
text = "Wurst Ei Käse"
worte = text.split()
assert worte == [__, __, __], "Was sind die Wörter?"

# 🧩 Strings zusammenfügen
worte = ["Jetzt", "ist", "die", "Zeit"]
assert " ".join(worte) == __, "Was ergibt das Zusammenfügen?"

# 🧩 Variablen einfügen
wert1 = "eins"
wert2 = 2
text = f"Die Werte sind {wert1} und {wert2}"
assert text == __, "Was steht im Text?"

# 🔠 Groß- und Kleinschreibung
assert "guido".capitalize() == __, "Was ergibt .capitalize()?"
assert "guido".upper() == __, "Was ergibt .upper()?"
assert "TimBot".lower() == __, "Was ergibt .lower()?"
assert "guido van rossum".title() == __, "Was ergibt .title()?"
assert "ToTaLlY aWeSoMe".swapcase() == __, "Was ergibt .swapcase()?"

# 🧩 Teil eines Strings
text = "Speck, Salat und Tomate"
assert text[7:10] == __, "Was steht zwischen Index 7 und 10?"

# 🧩 Einzelnes Zeichen
text = "Birnen, Salat und Tomate"
assert text[1] == __, "Was steht an zweiter Stelle?"

# 🔍 Enthält der String ein anderes Wort?
text = "Birnen, Salat und Tomate"
ist_salat_drin = "Salat" in text
assert ist_salat_drin == __, "Ist 'Salat' im Text?"
ist_hund_drin = "Hund" in text
assert ist_hund_drin == __, "Ist 'Hund' im Text?"
