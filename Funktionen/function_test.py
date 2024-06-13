# Beispiel - Datei für
# 1. Funktion
# 2. String
# 3. Listen (String = Liste aus Buchstaben/Zahlen/Sonderzeichen)
# 4. For ... in >> Gehe durch jedes Element einer Liste durch


def len_mahmoud(funktionsparameter_string):
    # Hier eine Zahl, die wir verwenden können
    anzahl = 0
    print("ANZAHL vor FOR:", anzahl)
    for zeichen in funktionsparameter_string:
        anzahl += 1  # Gleiche wie: anzahl = anzahl + 1
        print("Anzahl in FOR: ", anzahl, "bei Buchstabe: ", zeichen)

    return anzahl


# --------------------------------------------------
# HIER STARTET DEIN PROGRAMM!
# --------------------------------------------------
string1 = input("Gib einen Satz: ")


print("Anzahl mit unserer Funktion ausgerechnet = ", len_mahmoud(string1))
print("Anzahl mit len ausgerechnet = ",                         len(string1))
