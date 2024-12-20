import os
import re

passende_dateien = []
passende_Endungen = []


def main():
    projektpfad = input("Gib mir Projekt pfad: ")
    alter_projektname = input("Gib mir alten Projektnamen: ")

    # Gehe durch alle Dateien im Verzeichnis und Unterordnern
    for verzeichnisname, unterverzeichnisse, dateien in os.walk(projektpfad):
        for datei in dateien:
            # Überprüfe nur Textdateien
            dateipfad = os.path.join(verzeichnisname, datei)
            try:
                with open(dateipfad, "r", encoding="utf-8") as dateiobjekt:
                    inhalt = dateiobjekt.read()

                # Suche nach dem alten Projektnamen im Inhalt der Datei
                if alter_projektname in inhalt:
                    # Extrahiere den Pfad ab "dev"
                    index = dateipfad.find("\\dev\\")
                    dateipfad_ab_dev = dateipfad[index + 5:]
                    passende_dateien.append(dateipfad_ab_dev)

            except UnicodeDecodeError:
                # Versuche eine andere Codierung, wenn UTF-8 fehlschlägt
                try:
                    with open(dateipfad, "r", encoding="latin-1") as dateiobjekt:
                        inhalt = dateiobjekt.read()

                        # Suche nach dem alten Projektnamen im Inhalt der Datei
                        if alter_projektname in inhalt:
                            # Extrahiere den Pfad ab "dev"
                            index = dateipfad.find("\\dev\\")
                            dateipfad_ab_dev = dateipfad[index + 5:]
                            passende_dateien.append(dateipfad_ab_dev)

                except:
                    # Gib eine Fehlermeldung aus, wenn keine passende Codierung gefunden werden kann
                    print(f"Fehler beim Öffnen der Datei: {dateipfad}")

    # Drucke die gefundenen Dateipfade
    if passende_dateien:
        #print("Gefundene Dateien: ")
        for dateipfad in passende_dateien:
            pass
            # print(dateipfad)

    else:
        print("Keine passenden Dateien gefunden.")


if __name__ == "__main__":
    main()


for element in passende_dateien:
    if '.' in element and element.rsplit('.', 1)[1] != '':
        erweiterung = '.' + element.rsplit('.', 1)[1]
    if erweiterung not in passende_Endungen:
        passende_Endungen.append(erweiterung)

print(passende_Endungen)

finaler_string = ""
for x in passende_Endungen:
    finaler_string += "\"" + x + "\"" + " \"#\" \"/* */\" "

print(finaler_string + "\"EOV\"")

# Die Endungen die für uns wichtig sind (ARE9452,ARE9338)
# ['.txt', '.mk', '.py', '.h', '.c', '.log', '.html', '.lsl', '.grl', '.gpp', '.bat', '.dpa',
# '.dcf', '.xml', '.pl', '.cmm', '.t32', '.project ,.a2l,.dcf,.mak]

".txt" "#" ".mk" "#" "/* */" ".py" "#" "''' '''"


# '.dcf', '.xml', '.pl', '.cmm', '.t32', '.project ,.a2l,.dcf,.mak]

# C:\projects\u28u42\AIT0029_Projektstart\CP_1_2\dev\PrjCfg>python
#  c:\TEMP\cleanDelivery.py
# ".h" "//" "/* */" ".c" "//" "/* */" ".pl" "\#" "" ".mk" "\#" "" "EOV"
# sC:\projects\u28u42\AIT0029_Projektstart\CP_1_2\dev\PrjCfg
