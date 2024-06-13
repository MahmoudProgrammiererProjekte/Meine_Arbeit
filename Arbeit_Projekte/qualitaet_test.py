import sys
import os


def main():
    if len(sys.argv) != 3:
        print("Die Argumente Sind nicht genug")
        return

    verzeichnis = sys.argv[1]
    Neue_textdatei = sys.argv[2]

    passende_dateien = []
    for ordner, unterordner, dateien in os.walk(verzeichnis):
        for datei in dateien:
            dateiname, erweiterung = os.path.splitext(datei)
            if erweiterung in [".c", ".h", ".lsl", ".ld"]:
                passende_dateien.append(os.path.join(ordner, datei))

    passende_dateien_mit_if0 = []
    passende_dateien_mit_TODO = []

    for datei in passende_dateien:
        try:
            with open(datei, "r", encoding="utf-8") as f:
                for num, zeile in enumerate(f, start=1):
                    if "#if 0" in zeile:
                        pfad = datei.replace(verzeichnis, "", 1)
                        passende_dateien_mit_if0.append(
                            (pfad, num, zeile.strip()))
                    pruefeTODO(zeile, num, datei, verzeichnis,
                               passende_dateien_mit_TODO, Neue_textdatei)

        except UnicodeDecodeError:
            with open(datei, "r", encoding="latin-1") as f:
                for num, zeile in enumerate(f, start=1):
                    if "#if 0" in zeile:
                        pfad = datei.replace(verzeichnis, "", 1)
                        passende_dateien_mit_if0.append(
                            (pfad, num, zeile.strip()))
                    pruefeTODO(zeile, num, datei, verzeichnis,
                               passende_dateien_mit_TODO, Neue_textdatei)

        except:
            print(f"fehler beim datei öffnen : {datei}")
    with open(Neue_textdatei, "w") as f:
        f.write("\"#if 0\" found in:\n\n")
        for pfad, num, zeile in passende_dateien_mit_if0:
            f.write(f"{pfad} Zeile: {num} Inhalt: {zeile}\n")
            f.write(f"{pfad}zeile:{num} inhalt:{zeile} ")
    with open(Neue_textdatei, "a") as f:
        f.write("\n\n\"TODO\" found in:\n\n")
        for pfad, num, zeile in passende_dateien_mit_TODO:
            f.write(f"{pfad} Zeile: {num} Inhalt: {zeile}\n")


def pruefeTODO(zeile, num, datei, verzeichnis, passende_dateien_mit_TODO, Neue_textdatei):
    if "todo" in zeile.lower() or "TODO" in zeile.lower() or "ToDO" in zeile.lower() or "to-do" in zeile.lower():
        pfad = datei.replace(verzeichnis, "", 1)
        passende_dateien_mit_TODO.append(
            (pfad, num, zeile.strip()))


if __name__ == "__main__":
    main()
