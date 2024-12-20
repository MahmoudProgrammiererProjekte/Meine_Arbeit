import os

Verzeichnisinhalt = os.listdir()

if "mitarbeiter_liste.txt" not in Verzeichnisinhalt:
    liste_nicht_erstellt = input(
        "du hast noch keine mitarbeiter_liste.txt in deinem ordner.willst du eine erstellen? (ja / nein) ")
    if liste_nicht_erstellt == "nein":
        print("Ok dann nicht , tschüss ")
    if liste_nicht_erstellt == "ja":
        f = open("mitarbeiter_liste.txt", "w")
        f.close()
        with open("mitarbeiter_liste.txt", "r")as f:
            Datei_lesen = f.read()
        print("Das hier sind deine aktuellen mitarbeiter:")
        print(30*"-")
        print(Datei_lesen)
        print(30*"-")

        print("was willst du machen?",
              "\n> Infos zu bestemmten mitarbiter sehen[Gib den Namen vom mitarbeiter]", "\n> Neuen mitarbeiter hinzufügen [Gib ein:neu]", "\n> BEENDEN [x]")

        while (True):

            eingabe_prüfen = input(">> ")

            if eingabe_prüfen == "X":
                break
            if eingabe_prüfen == "neu":

                mitarbeiter_name = input("Name des neuen Mitarbeiter:")
                mitarbeiter_Alter = int(input("Alter des neuen Mitarbeiter:"))
                mitarbeiter_seit_wann = int(input(
                    "Mitarbeiter ist in der Firma seit:"))
                mitarbeiter_beruf = input("Beruf des neuen Mitarbeiter:")
                mitarbeiter_Haarfarbe = input(
                    "Haarfarbe des neuen Mitarbeiter:")
                mitarbeiter_Haustiere = input(
                    "Haustier des neuen Mitarbeiter:")

                with open("mitarbeiter_liste.txt", "a")as f:
                    name_mitarbeiter_einfügen = f.write(mitarbeiter_name)
                    komma_einfügen = f.write(",")
                    Alter_einfügen = f.write(str(mitarbeiter_Alter))
                    komma_einfügen = f.write(",")
                    mitarbeiter_seit_wann = f.write(str(mitarbeiter_seit_wann))
                    komma_einfügen = f.write(",")
                    mitarbeiter_beruf = f.write(mitarbeiter_beruf)
                    komma_einfügen = f.write(",")
                    mitarbeiter_Haarfarbe = f.write(mitarbeiter_Haarfarbe)
                    komma_einfügen = f.write(",")
                    mitarbeiter_Haustiere = f.write(mitarbeiter_Haustiere)
                    Neue_zeile_einfügen = f.write("\n")
                with open("mitarbeiter_liste.txt", "r")as f:
                    Datei_listen = f.readlines()

                    mitarbeioter_liste = []

                    for zeile in Datei_listen:
                        spliten = zeile.split(",")

                        neue_liste = mitarbeioter_liste.append(spliten[0])

                    print("Das hier sind deine aktuellen mitarbeiter:")
                    print(30*"-")
                    for schleife in mitarbeioter_liste:
                        print(schleife)
                        print(30*"-")

            if eingabe_prüfen != "neu":

                with open("mitarbeiter_liste.txt", "r")as f:
                    Datei_listen = f.readlines()
                    liste_leer = []
                    for zeile in Datei_listen:

                        liste_pro_zeile = zeile.split(",")

                        for eintrag in liste_pro_zeile:
                            xx = liste_leer.append(eintrag)

                    if eingabe_prüfen not in liste_leer:
                        print(30*"-")
                        print("mitarbeieter", eingabe_prüfen, "gibts nicht")
                        print(30*"-")

                    else:

                        class AVLToolsMitarbeiter:
                            def __init__(self, name_von_aufruf, alter_von_aufruf, datum_von_aufruf, beruf_von_aufruf, Haarfarbe_von_aufruf, Haustiere_von_aufruf):
                                self.name = name_von_aufruf
                                self.alter = alter_von_aufruf
                                self.datum = datum_von_aufruf
                                self.beruf = beruf_von_aufruf
                                self.haarfarbe = Haarfarbe_von_aufruf
                                self.Haustiere = Haustiere_von_aufruf

                            def eigenschaften(self):
                                print(50*"-")
                                print("Name", self.name)
                                print("Alter: ", self.alter)
                                print("Seit wann in der Firma", self.datum)
                                print("Beruf", self.beruf)
                                print("Haarfarbe", self.haarfarbe)
                                print("Haustiere", self.Haustiere)
                                print(50*"-")
                        with open("mitarbeiter_liste.txt", "r")as f:
                            Datei_listen = f.readlines()
                            liste_leer = []
                            for zeile in Datei_listen:

                                liste_pro_zeile = zeile.split(",")

                                for eintrag in liste_pro_zeile:
                                    xx = liste_leer.append(eintrag)

                            i = 0
                            neue_liste = []
                            for eingabe_index in liste_leer:
                                i = i+1
                                if eingabe_index == eingabe_prüfen:

                                    break
                            for eingabe_stelle in liste_leer[i-1:i+5]:

                                xxx = neue_liste.append(eingabe_stelle)

                            tmp_klasse = AVLToolsMitarbeiter(
                                neue_liste[0], neue_liste[1], neue_liste[2], neue_liste[3], neue_liste[4], neue_liste[5])

                            tmp_klasse.eigenschaften()

else:

    print("Du hast mitarbeiter_liste.txt schon in deinem ordner!!")

    with open("mitarbeiter_liste.txt", "r")as f:
        Datei_listen = f.readlines()
        print("\nDas hier sind deine aktuellen mitarbeiter:")
        print(30*"-")

        mitarbeioter_liste = []
        for zeile in Datei_listen:
            spliten = zeile.split(",")
            for erste_element in spliten:
                print(erste_element)
                break
        print(30*"-")

        print("was willst du machen?",
              "\n> Infos zu bestemmten mitarbiter sehen[Gib den Namen vom mitarbeiter]", "\n> Neuen mitarbeiter hinzufügen [Gib ein:neu]", "\n> BEENDEN [x]")

        while (True):

            eingabe_prüfen = input(">> ")

            if eingabe_prüfen == "X":
                break
            if eingabe_prüfen == "neu":

                mitarbeiter_name = input("Name des neuen Mitarbeiter:")
                mitarbeiter_Alter = int(input("Alter des neuen Mitarbeiter:"))
                mitarbeiter_seit_wann = int(input(
                    "Mitarbeiter ist in der Firma seit:"))
                mitarbeiter_beruf = input("Beruf des neuen Mitarbeiter:")
                mitarbeiter_Haarfarbe = input(
                    "Haarfarbe des neuen Mitarbeiter:")
                mitarbeiter_Haustiere = input(
                    "Haustiere des neuen Mitarbeiter:")

                with open("mitarbeiter_liste.txt", "a")as f:
                    name_mitarbeiter_einfügen = f.write(mitarbeiter_name)
                    komma_einfügen = f.write(",")
                    Alter_einfügen = f.write(str(mitarbeiter_Alter))
                    komma_einfügen = f.write(",")
                    mitarbeiter_seit_wann = f.write(str(mitarbeiter_seit_wann))
                    komma_einfügen = f.write(",")
                    mitarbeiter_beruf = f.write(mitarbeiter_beruf)
                    komma_einfügen = f.write(",")
                    mitarbeiter_Haarfarbe = f.write(mitarbeiter_Haarfarbe)
                    komma_einfügen = f.write(",")
                    mitarbeiter_Haustiere = f.write(mitarbeiter_Haustiere)
                    Neue_zeile_einfügen = f.write("\n")
                with open("mitarbeiter_liste.txt", "r")as f:
                    Datei_listen = f.readlines()

                    mitarbeioter_liste = []

                    for zeile in Datei_listen:
                        spliten = zeile.split(",")

                        neue_liste = mitarbeioter_liste.append(spliten[0])

                    print("Das hier sind deine aktuellen mitarbeiter:")
                    print(30*"-")
                    for schleife in mitarbeioter_liste:
                        print(schleife)
                        print(30*"-")

            if eingabe_prüfen != "neu":

                with open("mitarbeiter_liste.txt", "r")as f:
                    Datei_listen = f.readlines()
                    liste_leer = []
                    for zeile in Datei_listen:

                        liste_pro_zeile = zeile.split(",")

                        for eintrag in liste_pro_zeile:
                            xx = liste_leer.append(eintrag)

                    if eingabe_prüfen not in liste_leer:
                        print(30*"-")
                        print("mitarbeieter", eingabe_prüfen, "gibts nicht")
                        print(30*"-")

                    else:

                        class AVLToolsMitarbeiter:
                            def __init__(self, name_von_aufruf, alter_von_aufruf, datum_von_aufruf, beruf_von_aufruf, Haarfarbe_von_aufruf, Haustiere_von_aufruf):
                                self.name = name_von_aufruf
                                self.alter = alter_von_aufruf
                                self.datum = datum_von_aufruf
                                self.beruf = beruf_von_aufruf
                                self.haarfarbe = Haarfarbe_von_aufruf
                                self.Haustiere = Haustiere_von_aufruf

                            def eigenschaften(self):
                                print(50*"-")
                                print("Name", self.name)
                                print("Alter: ", self.alter)
                                print("Seit wann in der Firma", self.datum)
                                print("Beruf", self.beruf)
                                print("Haarfarbe", self.haarfarbe)
                                print("Haustiere", self.Haustiere)
                                print(50*"-")
                        with open("mitarbeiter_liste.txt", "r")as f:
                            Datei_listen = f.readlines()
                            liste_leer = []
                            for zeile in Datei_listen:

                                liste_pro_zeile = zeile.split(",")

                                for eintrag in liste_pro_zeile:
                                    xx = liste_leer.append(eintrag)

                            i = 0
                            neue_liste = []
                            for eingabe_index in liste_leer:
                                i = i+1
                                if eingabe_index == eingabe_prüfen:

                                    break
                            for eingabe_stelle in liste_leer[i-1:i+5]:

                                xxx = neue_liste.append(eingabe_stelle)

                            tmp_klasse = AVLToolsMitarbeiter(
                                neue_liste[0], neue_liste[1], neue_liste[2], neue_liste[3], neue_liste[4], neue_liste[5])

                            tmp_klasse.eigenschaften()
