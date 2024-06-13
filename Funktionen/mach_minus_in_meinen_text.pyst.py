
def satz_zeichen(parameter):
    anzahl = ""
    for zeichen in parameter:
        anzahl += zeichen + "-"
    return anzahl


print(40*"-")

Variable = input("Schreibe mir einen Satz deiner Wahl auf: ")

print(30*"-")

print(satz_zeichen(Variable))

print(30*"-")
