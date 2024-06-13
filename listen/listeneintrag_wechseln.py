# listeneintrag_wechseln.py
import sys

mitarbeiter_avl = ["Daniel", "Markus", "Klaus", "Mahmoud", "Roland"]
erste_name = sys.argv[1]  # Erste Eingabe als Parameter übergeben

if erste_name in mitarbeiter_avl:
    neuer_input = sys.argv[2]  # Zweite Eingabe als Parameter übergeben
    for zähler in range(len(mitarbeiter_avl)):
        if erste_name == mitarbeiter_avl[zähler]:
            mitarbeiter_avl.insert(zähler, neuer_input)
            print(mitarbeiter_avl)
            print(zähler)
            break
else:
    print(erste_name, "ist nicht enthalten!")
