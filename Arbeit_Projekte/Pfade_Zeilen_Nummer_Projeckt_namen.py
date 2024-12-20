import os
import re

verzeichnis = r"der_pfad"
#alter_projektname = input("Enter the old project name: ")
alter_projektname = "ARE9452"
# suchbegriff = "(?i)^[*\s]*(?:Project|project)\s*[=: ]\s*(AR\S+)"
suchbegriff = alter_projektname
neuer_projektname = "Test"
# neuer_projektname = input("Enter the new project name: ")

passende_zeilen = []

# Gehe durch alle Dateien im Verzeichnis und Unterordnern
for verzeichnisname, unterverzeichnisse, dateien in os.walk(verzeichnis):
    for datei in dateien:
        # Überprüfe nur Textdateien
        # if datei.endswith(("config.py", ".mk", ".c", ".h", ".html", ".arxml", "xml", ".lsl", ".grl", ".gpp", ".a2l", ".cmm")):
        dateipfad = os.path.join(verzeichnisname, datei)
        try:
            with open(dateipfad, "r", encoding="utf-8") as dateiobjekt:
                zeilen = dateiobjekt.readlines()

            # Suche nach Zeilen, die mit den Suchbegriffen übereinstimmen
            for i, zeile in enumerate(zeilen):
                if re.search(suchbegriff, zeile) and alter_projektname in zeile and not zeile.strip().startswith("\\") and not zeile.strip().endswith("\\"):
                    passende_zeilen.append((dateipfad, i+1, zeile))

        except UnicodeDecodeError:
            # Versuche eine andere Codierung, wenn UTF-8 fehlschlägt
            try:
                with open(dateipfad, "r", encoding="latin-1") as dateiobjekt:
                    zeilen = dateiobjekt.readlines()
                    # Suche nach Zeilen, die mit den Suchbegriffen übereinstimmen
                for i, zeile in enumerate(zeilen):
                    if re.search(suchbegriff, zeile) and not zeile.strip().startswith("\\") and not zeile.strip().endswith("\\"):
                        passende_zeilen.append((dateipfad, i+1, zeile))
            except:
                # Gib eine Fehlermeldung aus, wenn keine passende Codierung gefunden werden kann
                print(f"Fehler beim Öffnen der Datei: {dateipfad}")

# Drucke die gefundenen Zeilen und ersetze den alten Projektname durch den neuen Projektname
for zeile in passende_zeilen:
    alte_zeile = zeile[2]
    neue_zeile = alte_zeile.replace(alter_projektname, neuer_projektname)
    print(
        f"Datei: {zeile[0]}")
