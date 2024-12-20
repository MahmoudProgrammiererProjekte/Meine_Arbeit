Variable = input("Schreibe mir einen Satz deiner Wahl auf: ")
satz_zeichen = len(Variable)

print(30*"-")


if satz_zeichen > 10:
    print("10+++")

if satz_zeichen < 10:
    print("10---")

if satz_zeichen == 10:
    print("!!! 10 !!!")


def anzahl_zeichen():
    print("Anzahl der Zeichen: "+str(satz_zeichen))


anzahl_zeichen()

print(30*"-")
