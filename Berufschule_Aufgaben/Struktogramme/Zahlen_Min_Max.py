
Zahlen_liste = []

while (True):
    Zahlen_eingeben = input(
        "gebe mir Zahlen und ich speichere die und gebe ende um das programm zu beenden :")
    if Zahlen_eingeben == "ende":
        break
    Zahlen_liste.append(Zahlen_eingeben)


Min = Zahlen_liste[0]
Max = Zahlen_liste[0]

for zahl in Zahlen_liste:
    if zahl < Min:
        Min = zahl

    if zahl > Max:

        Max = zahl

print(Min, Max)
