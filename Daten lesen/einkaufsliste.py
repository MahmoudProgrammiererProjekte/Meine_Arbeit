import os
eingabe = input(
    "Bitte gib mir den Namen einer einkaufliste , die du erstellen oder weiterführen willst: ")
Verzeichnisinhalt = os.listdir()

if eingabe in Verzeichnisinhalt:

    print("Datei gibt es schon.hier die Einträge: ")
    print(30*"-")

    with open(eingabe, 'r')as f:
        variable = (f.read())
    print(variable)
    print(30*"-")

    while (True):
        eingeben1 = input(
            "Füge Einträge zur einkaufskliste dazu (x = Aufhören): ")
        with open(eingabe, 'a')as f:
            variable = f.write(eingeben1)
        with open(eingabe, 'a')as f:
            variable = f.write("\n")

        if eingeben1 == "x":
            with open(eingabe, 'r')as f:
                lines = f.readlines()

                del lines[-1]
                with open(eingabe, 'w')as f:
                    for Datei_lesen in lines:
                        f.write(Datei_lesen)
                print(30*"-")

                break


else:
    print("Datei gibt es noch nicht.füge jetzt deine Einträge hinzu:")
    f = open(eingabe, "w")

    while (True):

        eingabe_2 = input(
            "Füge Einträge zur einkaufskliste dazu (x = Aufhören): ")

        with open(eingabe, 'a')as f:
            variable = f.write(eingabe_2)
        with open(eingabe, 'a')as f:
            variable = f.write("\n")

        if eingabe_2 == "x":
            with open(eingabe, 'r')as f:
                lines = f.readlines()
                del lines[-1]
                with open(eingabe, 'w')as f:
                    for Datei_lesen in lines:
                        f.write(Datei_lesen)

            print(30*"-")

            break

with open(eingabe, 'r')as f:
    variable = (f.read())
print(variable)
print(30*"-")
