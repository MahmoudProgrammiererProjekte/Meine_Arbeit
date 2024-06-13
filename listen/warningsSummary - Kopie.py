import os
Verzeichnisinhalt = os.listdir(
    "Der Pfad bitte hier ")
Datein_liste = []
zeilen_die_wir_brauchen = []
for jede_datei in Verzeichnisinhalt:
    if ".err" in jede_datei:
        Datein_liste.append(jede_datei)
for jede_err_datei in Datein_liste:
    die_fahrt = "Der Pfad bitte hier" + jede_err_datei
    with open(die_fahrt, "r")as f:
        datei_zu_liste = f.readlines()
    for jede_zeile in datei_zu_liste:
        if "ctc W" in jede_zeile:
            zeilen_die_wir_brauchen.append(jede_zeile)
for jede_err_zeile in zeilen_die_wir_brauchen:
    with open("Der Pfad bitte hier", "a")as f:
        datei_zu_liste = f.write(jede_err_zeile)
