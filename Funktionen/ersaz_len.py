
def satz_zeichen(parameter):
    anzahl = 0
    for zeichen in parameter:
        anzahl += 1
    return anzahl


print(40*"-")

Variable = input("Schreibe mir einen Satz deiner Wahl auf: ")

zeichen = satz_zeichen(Variable)

if zeichen > 10:
    print("10+++")
if zeichen < 10:
    print("10---")
if zeichen == 10:
    print("!!! 10 !!!")

print("Anzahl der Zeichen: ", satz_zeichen(Variable))
print(40*"-")
