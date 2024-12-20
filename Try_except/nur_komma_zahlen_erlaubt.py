while (True):
    komma_zahl = input("gebe einen komma zahl : ")
    try:
        type_int = int(komma_zahl)
        ist_int = True
        continue

    except:
        ist_int = False

    try:
        Type_von_float = float(komma_zahl)
        ist_float = True
        break

    except:
        ist_float = False


while (True):

    zahl = input("gebe einen ganzen zahl : ")
    try:
        type_von_int = int(zahl)
        ist_int = True
        break

    except:
        ist_int = False

    try:
        type_von_int = float(zahl)
        ist_int = True
        continue

    except:
        float = False

print(30*"-")
print(type_von_int+Type_von_float)
print(30*"-")
