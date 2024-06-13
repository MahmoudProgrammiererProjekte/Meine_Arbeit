def gib_mir_höchste_zahl(liste_mahmoud):
    größte_zahl = liste_mahmoud[0]
    for zähler in liste_mahmoud:
        if zähler > größte_zahl:
            größte_zahl = zähler

    return größte_zahl


zahlen_liste_1 = [1, 15, 30, 800, -23, 57000, 13, 0, 100]
zahlen_liste_2 = [1, 15, 10000000, 800, -23, 57000, 13, 1, 100]
zahlen_liste_3 = [-1, -15, -10000000, -800, -23, -75000, -13, -100]


grösste_zahl_liste1 = gib_mir_höchste_zahl(zahlen_liste_1)
print("Die größte zahl aus liste1 ist: ", grösste_zahl_liste1)
grösste_zahl_liste2 = gib_mir_höchste_zahl(zahlen_liste_2)
print("Die größte zahl aus liste1 ist: ", grösste_zahl_liste2)
grösste_zahl_liste3 = gib_mir_höchste_zahl(zahlen_liste_3)
print("Die größte zahl aus liste1 ist: ", grösste_zahl_liste3)
