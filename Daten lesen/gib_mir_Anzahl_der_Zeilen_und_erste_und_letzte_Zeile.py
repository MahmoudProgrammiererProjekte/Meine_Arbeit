input = input("Bitte gib mir den Namen von einer Datei im aktuellen Ordner: ")


def zeilen_anzahl(dateiname):
    global kann_öffnen
    kann_öffnen = True
    try:
        with open(dateiname, 'r')as f:
            variable = (f.read())

    except:
        kann_öffnen = False

    if kann_öffnen == True:
        Anzahl = variable.count("\n") + 1
    else:
        Anzahl = -1

    return Anzahl


def gibmirErsteundLetzteZeileVonDatei(Dateiname):
    try:
        datei_geöffnet = True
        with open(Dateiname, 'r') as f:
            variable = (f.readlines())
    except:
        datei_geöffnet = False
    if datei_geöffnet == True:
        print(variable[0].strip())
        print(variable[-1])
        print(50*"-")
    else:
        print("Die Datei kann nicht geöffnet werden!")
        print(40*"-")


anzahl_zeilen = zeilen_anzahl(input)
if anzahl_zeilen == -1:
    print(40*"-")
    print("Datei gibts nicht!")

else:
    print(50*"-", "\nDeine Datei", input, "hat",
          anzahl_zeilen, "Zeilen")


gibmirErsteundLetzteZeileVonDatei(input)
