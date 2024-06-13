

erste_eingabe = input("Eingabe: ")
typ_variable = type(erste_eingabe)  # IMMER string

while (typ_variable != float):
    eingabe = input("gebe mir endlich zahl ")

    try:
        test123 = int(eingabe)
        fehler = False
    except:
        fehler = True

    if fehler == False:
        break
