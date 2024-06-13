import os
import re


def main():
    verzeichnis = r"der Pfad"
    suchbegriff = "(?i)^[*\s]*(?:Project|project)\s*[=: ]\s*(AR\S+)"
    alter_projektname = input("Enter the old project name: ")
    neuer_projektname = input("Enter the new project name: ")

    # Gehe durch alle Dateien im Verzeichnis und Unterordnern
    for verzeichnisname, unterverzeichnisse, dateien in os.walk(verzeichnis):
        for datei in dateien:
            dateipfad = os.path.join(verzeichnisname, datei)
            ersetze_projektname(dateipfad, suchbegriff,
                                alter_projektname, neuer_projektname)


def ersetze_projektname(dateipfad, suchbegriff, alter_projektname, neuer_projektname):
    try:
        with open(dateipfad, "r", encoding="utf-8") as dateiobjekt:
            zeilen = dateiobjekt.readlines()

    except UnicodeDecodeError:
        # Versuche eine andere Codierung, wenn UTF-8 fehlschlägt
        try:
            with open(dateipfad, "r", encoding="latin-1") as dateiobjekt:
                zeilen = dateiobjekt.readlines()
        except:
            # Gib eine Fehlermeldung aus, wenn keine passende Codierung gefunden werden kann
            print(f"Fehler beim Öffnen der Datei: {dateipfad}")
            return

    with open(dateipfad, "w", encoding="utf-8") as dateiobjekt:
        # Suche nach Zeilen, die mit den Suchbegriffen übereinstimmen
        for i, zeile in enumerate(zeilen):
            if re.search(suchbegriff, zeile) and alter_projektname in zeile:
                neue_zeile = zeile.replace(
                    alter_projektname, neuer_projektname)
                zeilen[i] = neue_zeile
        dateiobjekt.writelines(zeilen)


if __name__ == "__main__":
    main()
