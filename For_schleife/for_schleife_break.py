Password = "12356"
eingabe = ""
limited = 0
Maximal = 3


for zeichen in range(Maximal+1):
    if limited < Maximal:
        eingabe = input("Bitte Passwort eingeben: ")
        limited += 1

    else:
        print("Deine 3 Male Verusche sind vorbei ")

    if eingabe == Password:
        print("Das Passwort ist RICHTIG!")
        break
