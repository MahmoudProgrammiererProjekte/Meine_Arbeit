eingabe_1 = input("Bitte gib mir eine gerade Zahl: ")

try:
    eingabe_zu_int = int(eingabe_1)
    fehler_aufgetreten = False

except:
    fehler_aufgetreten = True

if fehler_aufgetreten:

    print(30*"-")
    print("du hast keinen zahl gegeben")
    print(30*"-")

else:
    print(50*"-")
    print("Super du hast mir eine ganze Zahl gegeben!")
    print("Hier ich rechne deine Zahl mal 9999: " +
          eingabe_1 + " * 9999 = ", eingabe_zu_int * 9999)
    print(50*"-")
