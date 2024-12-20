import os
import re

verzeichnis = r"der_Pfad hier eingeben !!!"
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
        with open(dateipfad, "r", encoding="utf-8") as dateiobjekt:
            zeilen = dateiobjekt.readlines()
            # Suche nach Zeilen, die mit den Suchbegriffen übereinstimmen
            for i, zeile in enumerate(zeilen):
                if re.search(suchbegriff, zeile) and not zeile.strip().startswith("\\") and not zeile.strip().endswith("\\"):
                    passende_zeilen.append((dateipfad, i+1, zeile))

# Drucke die gefundenen Zeilen und ersetze den alten Projektname durch den neuen Projektname
for zeile in passende_zeilen:
    alte_zeile = zeile[2]
    neue_zeile = alte_zeile.replace(alter_projektname, neuer_projektname)
    print(
        f"Datei: {zeile[0]}, Zeilennummer: {zeile[1]}, alte Zeile: {alte_zeile.strip()}, neue Zeile: {neue_zeile.strip()}")
