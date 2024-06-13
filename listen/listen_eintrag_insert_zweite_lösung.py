
def liste_zählen(erste_eingabe, mitarbeiter_liste):
    if erste_eingabe in mitarbeiter_liste:
        input_zu_liste_fügen = input("Jetzt schreibe einen neuen Namen: ")
        for zähler in range(len(mitarbeiter_avl)):
            if erste_eingabe == mitarbeiter_avl[zähler]:
                mitarbeiter_avl.insert(zähler, input_zu_liste_fügen)
                print(mitarbeiter_avl)
                break
    else:
        print(erste_eingabe, "ist nicht enthalten!")


erste_name = input("Bitte schreibe einen Namen, der vielleicht im Büro ist: ")
mitarbeiter_avl = ["Daniel", "Markus", "Klaus", "Mahmoud", "Roland"]


liste_zählen(erste_name, mitarbeiter_avl)
