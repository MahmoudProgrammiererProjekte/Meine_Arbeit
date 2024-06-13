import os
import re

verzeichnis = r"der_Pfad hier eingeben !!!
suchbegriff = "(?i)^[*\s]*(?:Project|project)\s*[=: ]\s*(AR\S+)"
alter_projektname = input("Enter the old project name: ")
neuer_projektname = input("Enter the new project name: ")
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
                # Suche nach Zeilen, die mit dem Suchbegriff übereinstimmen und nicht von Backslashes umgeben sind
                # enumerate = aufzählen der Zielen
                for i, zeile in enumerate(zeilen):
                    if re.search(suchbegriff, zeile) and not zeile.strip().startswith("\\") and not zeile.strip().endswith("\\"):
                        passende_zeilen.append(
                            (dateipfad, i+1, zeile.strip()))

        except UnicodeDecodeError:
            # Versuche eine andere Codierung, wenn UTF-8 fehlschlägt
            try:
                with open(dateipfad, "r", encoding="latin-1") as dateiobjekt:
                    zeilen = dateiobjekt.readlines()
                    # Suche nach Zeilen, die mit dem Suchbegriff übereinstimmen und nicht von Backslashes umgeben sind
                    for i, zeile in enumerate(zeilen):
                        if re.search(suchbegriff, zeile) and not zeile.strip().startswith("\\") and not zeile.strip().endswith("\\"):
                            passende_zeilen.append(
                                (dateipfad, i+1, zeile.strip()))
            except:
                # Gib eine Fehlermeldung aus, wenn keine passende Codierung gefunden werden kann
                print(f"Fehler beim Öffnen der Datei: {dateipfad}")

# Drucke die gefundenen Zeilen und ersetze den alten Projektname durch den neuen Projektname
for zeile in passende_zeilen:
    alte_zeile = zeile[2]
    neue_zeile = alte_zeile.replace(alter_projektname, neuer_projektname)
    print(
        f"Datei: {zeile[0]}, Zeilennummer: {zeile[1]}, alte projektname: {alte_zeile.strip()}, neue projektname: {neue_zeile.strip()}")
