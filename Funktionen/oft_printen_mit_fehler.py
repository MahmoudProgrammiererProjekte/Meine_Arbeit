def oft_printen(string, zahl_für_printen):
    zahl = 0
    for string_zahl in range(zahl_für_printen):
        zahl += 1

        if zahl_für_printen > 9:
            print(zahl_für_printen,
                  " ist zu viel! Ich hab gesagt 1-9!")
            break
        else:
            print(zahl, "-", string)


Eingabe_von_string = input("Bitte gib mir irgendeinen String: ")
wie_oft_printen = int(input("Bitte gib mir eine Zahl von 1-9: "))
print(50*"-")
oft_printen(Eingabe_von_string, wie_oft_printen)
print(50*"-")
