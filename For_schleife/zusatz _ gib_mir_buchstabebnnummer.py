alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
            'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


def buchstaben_nummer(buchstabe):
    for buchstabennummer in range(0, len(alphabet)):
        if buchstabe == alphabet[buchstabennummer]:
            return buchstabennummer + 1


eingabe = input("Schreibe einen Buchstaben a - z: ")
print(54*"-")


Variable = buchstaben_nummer(eingabe)
if Variable == None:
    print("Deine Eingabe \"" + eingabe +
          "\" ist kein Buchstabe aus dem Alphabet!")
else:
    print("Dein Buchstabe \"" + eingabe +
          "\" steht an Stelle:", Variable, "im Alphabet")
print(54*"-")
