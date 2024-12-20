def oft_printen(string, zahl_für_printen):
    if type(zahl_für_printen) != int:

        print("es geht Nur mit zahlen,ein text wird nicht akzeptiert ")
        return

    if zahl_für_printen < 1:
        print(zahl_für_printen,
              "ist zu wenig ! Ich hab gesagt 1-9!")

    for string_zahl in range(zahl_für_printen):
        if zahl_für_printen > 9:
            print(zahl_für_printen, "ist zu viel! Ich hab gesagt 1-9!")
            break
        else:

            print(string_zahl+1, "-", string)


fehler_passiert = False

Eingabe_von_string = input("Bitte gib mir irgendeinen String: ")


try:
    wie_oft_printen = int(input("Bitte gib mir eine Zahl von 1-9: "))
except:
    fehler_passiert = True

if fehler_passiert:
    print(53*"-")
    print("es geht Nur mit zahlen,ein text wird nicht akzeptiert ")
    print(53*"-")
else:
    print(50*"-")
    oft_printen(Eingabe_von_string, wie_oft_printen)
    print(50*"-")
