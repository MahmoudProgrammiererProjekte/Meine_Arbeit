import os
import re


def main():
    projektpfad = input("Gib mir Projekt pfad: ")
    alter_projektname = input("Gib mir alten Projektnamen: ")

    passende_dateien = []

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
        print("Gefundene Dateien: ")
        for dateipfad in passende_dateien:
            print(dateipfad)
        # Füge die gefundenen Pfade zu der Textdatei hinzu

    else:
        print("Keine passenden Dateien gefunden.")


if __name__ == "__main__":
    main()
