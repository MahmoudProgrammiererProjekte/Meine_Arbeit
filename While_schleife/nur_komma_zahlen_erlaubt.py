while (True):
    komma_zahl = input("gebe einen komma zahl : ")
    try:
        type_inp = int(komma_zahl)
        ist_int = True
        continue
    except:
        ist_int = False

    try:
        type_inp = float(komma_zahl)
        ist_float = True
        break
    except:
        ist_float = False
        # >> KEIN FLOAT FANG VON VORNE AN (WHILE)!


# DIESE WHILE IST DAZU DA UM RAUSZUFINDEN OB ES WIRKLICH float() IST
# while (True):
#    inp = input("dsdsd: ")
#    try:
#        type_inp = int(inp)
#        ist_int = True
#        continue
#    except:
#        ist_int = False
#
#    try:
#        type_inp = float(inp)
#        ist_float = True
#        break
#    except:
#        ist_float = False
#        # >> KEIN FLOAT FANG VON VORNE AN (WHILE)!
#
#
#print("FLOAT AUSGEGEBEN SUPER!")
