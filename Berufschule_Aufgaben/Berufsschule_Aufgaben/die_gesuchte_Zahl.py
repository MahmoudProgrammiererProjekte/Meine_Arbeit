# Es soll ein Zahlenratespiel als Computerprogramm entwickelt werden.
#  Dabei wird vom Computer eine Zufallszahl zwischen 1 und 200 ermittelt. Anschließend soll der Benutzer versuchen, die Zahl mit so wenig Versuchen wie möglich zu erraten.
# Solange die Zahl nicht erraten wurde, soll dem Benutzer nach jedem Versuch angezeigt werden,
#  ob die gesuchte Zahl größer oder kleiner als die eingegebene Zahl ist. Sobald die Zahl erraten wurde soll eine entsprechende Erfolgsmeldung und die Anzahl der Rateversuche angezeigt werden.
# Entwerfen Sie einen
# Algorithmus für dieses Computerprogramm und stellen Sie diesen als PAP oder Struktogramm dar

die_zahl = 200
eingabe = ""
limited = 0
Maximal = 3


for zeichen in range(Maximal+1):
    if limited < Maximal:
        eingabe = int(input("errate die Zahl : "))
        if eingabe > 200:
            print("die gesuchte Zahl größer  als die eingegebene Zahl ")
        if eingabe < 200:
            print("die gesuchte Zahl kleiner  als die eingegebene Zahl ")

        limited += 1

    else:
        print("Deine 3 Male Verusche sind vorbei ")

    if eingabe == die_zahl:
        print("Die zahl ist RICHTIG!")
        break
