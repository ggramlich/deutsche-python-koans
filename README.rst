=======================
Deutsche Python Koans 🐍
=======================

Deutsche Python Koans ist ein interaktives Tutorial zum Erlernen der 
Programmiersprache Python durch das Lösen von Aufgaben. Diese Version ist 
speziell für deutschsprachige Lernende entwickelt und verwendet einfache, 
kindgerechte Sprache.

Die Aufgaben werden gelöst, indem du die fehlenden Teile von assert-Anweisungen 
ausfüllst. Zum Beispiel::

    assert 1 + 3 == __, "Was ergibt 1 + 3?"

Das kann gelöst werden, indem du den __ Teil durch den passenden Code ersetzt::

    assert 1 + 3 == 4, "Was ergibt 1 + 3?"


Diese Koans sind speziell für Anfänger und junge Lernende entwickelt:
- ✅ Einfache assert-Anweisungen (keine unittest-Bibliothek nötig)
- 🇩🇪 Komplett auf Deutsch
- 🎯 Kindgerechte, ermutigende Fehlermeldungen
- 🐍 Direkt in Thonny oder anderen Python-Umgebungen ausführbar


Projekt herunterladen
=====================

Du findest Deutsche Python Koans auf Github:

    https://github.com/ggramlich/deutsche-python-koans

Du kannst den Quellcode als zip herunterladen oder das Repository klonen::

    git clone https://github.com/ggramlich/deutsche-python-koans.git

Installation und Umgebung
=========================

**Empfohlene Option: Thonny verwenden**

Thonny ist eine besonders einfache Python-Umgebung für Einsteiger und Kinder. 
Du kannst Thonny direkt von https://thonny.org/ herunterladen und installieren. 
Python ist bereits enthalten – du musst nichts extra installieren!

**Alternative Option: Python manuell installieren und im Terminal ausführen**

Falls du lieber eine andere Umgebung nutzen möchtest, kannst du Python auch 
manuell installieren:

    http://www.python.org/download

Nach der Installation von Python stelle sicher, dass der Ordner mit der 
Python-Ausführungsdatei im Systempfad ist. Mit anderen Worten: Du musst 
Python von einer Kommandozeile aus ausführen können.

`python3` oder `python.exe` je nach Betriebssystem.

Bei Problemen kann das helfen:

    http://www.python.org/about/gettingstarted

Erste Schritte
==============

So startest du:
1. Thonny installieren: https://thonny.org/
2. Öffne Thonny.
3. Öffne eine der Koan-Dateien (z.B. ``about_asserts.py``).
4. Klicke auf "Ausführen" (F5).

Oder im Terminal:

    python3 koans/about_asserts.py

Diese Dateien verwenden einfache assert-Anweisungen und sind speziell für 
Lernende entwickelt. Sie können direkt in Thonny, IDLE oder anderen 
Python-Umgebungen ausgeführt werden - ohne zusätzliche Module!

**Empfohlene Reihenfolge:**

1. ``about_asserts.py`` - Grundlagen der assert-Anweisungen
2. ``about_integers.py`` - Rechnen mit Zahlen  
3. ``about_strings.py`` - Texte und Wörter
4. ``about_true_and_false.py`` - Wahr und Falsch
5. ``about_lists.py`` - Listen und Sammlungen
6. ``about_if_statements.py`` - Entscheidungen treffen
7. ``about_dictionaries.py`` - Wörterbücher
8. ``about_tuples.py`` - Unveränderliche Listen
9. ``about_sets.py`` - Einzigartige Sammlungen
10. ``about_functions.py`` - Eigene Funktionen schreiben
11. ``about_loops.py`` - Wiederholungen mit for
12. ``about_while_loops.py`` - Wiederholungen mit while

**Wenn ein assert fehlschlägt:**

    AssertionError: Was ergibt 1+2?

Du siehst eine freundliche Fehlermeldung, die dir hilft zu verstehen,
was du ergänzen sollst. Ersetze einfach das __ durch den richtigen Wert.

Wenn du dir nicht sicher bist, welcher Wert erwartet wird, kannst du
die Python-Kommandozeile verwenden. Öffne sie und teste::

    >>> 1 + 2
    3
    >>> type("Hallo")
    <class 'str'>

So findest du heraus, was der richtige Wert ist!


Die Koans ausführen
==================

**In Thonny:** Öffne einfach eine der Dateien und klicke auf "Ausführen" (F5).

**Im Terminal:** Eine einzelne Koan-Datei ausführen::

  $ python3 koans/about_strings.py

Alle Koans nacheinander bearbeiten::

  $ python3 koans/about_asserts.py
  $ python3 koans/about_integers.py
  $ python3 koans/about_strings.py
  $ python3 koans/about_lists.py
  $ python3 koans/about_dictionaries.py
  $ python3 koans/about_sets.py
  $ python3 koans/about_tuples.py
  $ python3 koans/about_true_and_false.py
  $ python3 koans/about_if_statements.py
  $ python3 koans/about_functions.py
  $ python3 koans/about_loops.py
  $ python3 koans/about_while_loops.py


Danksagungen und Inspiration
============================

Diese deutschen Koans basieren auf der Idee der originalen Python Koans 
von Greg Malcolm:

    http://github.com/gregmalcolm/python_koans

und der vereinfachten Version von Greg Loyse:

    https://github.com/arachnegl/python-koans

**Für Fortgeschrittene:** Nach dem Abschluss dieser deutschen Koans kannst 
du die englischen Original-Koans von Greg Malcolm ausprobieren. Sie verwenden 
das unittest-Framework und sind komplexer - perfekt um deine Kenntnisse zu 
vertiefen!

Diese deutsche Version wurde speziell entwickelt, um:
- 🇩🇪 Deutschsprachigen Lernenden den Einstieg zu erleichtern
- 🧒 Kindern und Jugendlichen Python näherzubringen  
- 🎯 Ohne zusätzliche Bibliotheken auszukommen
- 💬 Mit freundlichen, ermutigenden Nachrichten zu motivieren


Was du gelernt hast
===================

Nach dem Durcharbeiten aller Koans kennst du:

✅ **Grundlagen**: Variablen, Zahlen, Strings
✅ **Datenstrukturen**: Listen, Tupel, Dictionaries, Sets  
✅ **Kontrolle**: if-Anweisungen, Schleifen
✅ **Funktionen**: Eigene Funktionen schreiben
✅ **Debugging**: Mit assert-Anweisungen testen

**Nächste Schritte:** 
- Versuche eigene kleine Programme zu schreiben
- Schau dir die Original-Koans von Greg Malcolm an
- Lerne über Klassen und Objekte
- Erkunde Python-Bibliotheken wie matplotlib oder pandas

