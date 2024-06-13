
def liste_zählen(erste_eingabe, mitarbeiter_liste):
    if erste_eingabe in mitarbeiter_liste:
        input_zu_liste_fügen = input("Jetzt schreibe einen neuen Namen: ")
        for zähler in range(len(mitarbeiter_avl)):
            if erste_eingabe == mitarbeiter_avl[zähler]:

                mitarbeiter_avl.insert(zähler, input_zu_liste_fügen)
                return mitarbeiter_avl
    else:
        print(erste_eingabe, "ist nicht enthalten ")
        return mitarbeiter_avl


erste_name = input("Bitte schreibe einen Namen, der vielleicht im Büro ist: ")
mitarbeiter_avl = ["Daniel", "Markus", "Klaus", "Mahmoud", "Roland"]


print(liste_zählen(erste_name, mitarbeiter_avl))
