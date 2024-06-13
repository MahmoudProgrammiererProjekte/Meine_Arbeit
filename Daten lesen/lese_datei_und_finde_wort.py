with open('der_Pfad hier eingeben !!!', 'r')as f:
    variable = (f.read())

input = input(
    "Bitte gib ein Wort oder ein Satz und ich sag dir ob das in der Datei enthalten ist:")
if input in variable:
    print(40*"-")
    print("Dein Suchtext ist in der Datei enthalten!")
    print(40*"-")

else:
    print(30*"-")
    print("Nix gefunden!")
    print(30*"-")
