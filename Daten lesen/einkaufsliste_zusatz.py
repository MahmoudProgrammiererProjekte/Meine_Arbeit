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
        with open(eingabe, "r")as f:
            k = f.readlines()
        h = input("Füge Einträge zur liste hinzu (x = aufhören ): ")
        s = h+"\n"
        if s in k:
            print(h, "hast du schon in der liste! Brauchen wir nicht mir hinzufügen")
            continue
        if h == "x":
            break
        if s not in k:
            with open(eingabe, "a")as file:
                L = file.write(s)
            continue
else:
    print("Datei gibt es noch nicht.füge jetzt deine Einträge hinzu:")
    f = open(eingabe, "w")
    while (True):
        with open(eingabe, "r")as f:
            k = f.readlines()
        h = input("Füge Einträge zur liste hinzu (x = aufhören ): ")
        s = h+"\n"
        if s in k:
            print(h, "hast du schon in der liste! Brauchen wir nicht mir hinzufügen")
            continue

        if h == "x":
            break
        if s not in k:
            with open(eingabe, "a")as file:
                L = file.write(s)
            continue
with open(eingabe, 'r')as f:
    variable = f.read()
print(30*"-")
print(variable)
print(30*"-")
