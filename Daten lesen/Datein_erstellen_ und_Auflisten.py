import os
eingabe = input(
    "Bitte gib mir den Namen einer Datei , die du erstellen willst ")

Verzeichnisinhalt = os.listdir()

if eingabe in Verzeichnisinhalt:
    print("Datei gibt es schon! ")

else:

    f = open(eingabe, "w")
    f.close()

    eingabe_2 = input(
        "Jetzt gibe einen Text ein ,den du in deine Datei schreiben willst: ")

    with open(eingabe, 'a')as f:

        variable = (f.write(eingabe_2))
