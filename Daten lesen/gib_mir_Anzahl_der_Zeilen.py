input = input("Bitte gib mir den Namen von einer Datei im aktuellen Ordner: ")


def zeilen_anzahl(dateiname):

    fehler_meldung = True

    try:

        with open(dateiname, 'r')as f:
            variable = (f.read())
    except:
        fehler_meldung = False

    if fehler_meldung == True:

        Anzahl = variable.count('\n')+1
        print(50*"-")
        print(dateiname, " hat ", Anzahl, "Zeilen!")
        print(50*"-")

    else:
        print(50*"-")
        print("Datei gibst nicht!")
        print(50*"-")


zeilen_anzahl(input)


# input = input("Bitte gib mir den Namen von einer Datei im aktuellen Ordner: ")
#
#
# def zeilen_anzahl(dateiname):
#     global kann_öffnen
#     kann_öffnen = True
#     try:
#         with open(dateiname, 'r')as f:
#             variable = (f.read())
#
#     except:
#         kann_öffnen = False
#
#     if kann_öffnen == True:
#         Anzahl = variable.count("\n") + 1
#     else:
#         Anzahl = -1
#
#     return Anzahl
#
#
# anzahl_zeilen = zeilen_anzahl(input)
#
#
# if anzahl_zeilen == -1:
#     print("Datei gibts nicht")
# else:
#     print(50*"-", "\nDeine Datei", input, "hat",
#           anzahl_zeilen, "Zeilen\n", 50*"-")
#
