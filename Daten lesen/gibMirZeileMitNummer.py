
input_ = input("Bitte gib mir den Namen von einer Datei im aktuellen Ordner: ")

try:
    Datei_geöffnet = True
    with open(input_, 'r')as f:
        speicher = (f.read())

except:
    print(30*"-")
    print("Datei gibst nicht!")
    print(30*"-")
    Datei_geöffnet = False

if Datei_geöffnet == True:
    Anzahl = speicher.count('\n')+1
    print(50*"-")
    print(input_, " hat ", Anzahl, "Zeilen!", "\n")

    try:
        er_hat_zahl_gegeben = True
        print("Bitte nenne mir eine Zahl von 1-", (Anzahl-1))
        neuer_input = int(input("gebe mir bitte die zahl: "))

    except:
        print("Ich habe gesagt zahl zwischen 1-", (Anzahl-1))
        er_hat_zahl_gegeben = False

    if er_hat_zahl_gegeben == True:
        with open(input_, 'r')as f:
            liste_zahl = (f.readlines())

        try:
            zahl_kleiner_als_text = True
            print(liste_zahl[neuer_input])
            print(50*"-")

        except:
            print(50*"-")
            print("Die zahl größer als  Text zeilen!")
            print(50*"-")
            zahl_kleiner_als_text = False
