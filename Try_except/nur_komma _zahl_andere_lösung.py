
erster_input = input("gebe bitte einen ganzen zahl ein ")
try:
    fehler = False
    type_erster_input = int(erster_input)


except:
    fehler = True

if fehler:
    typey_von_fehler = type(erster_input)

    while typey_von_fehler != int:
        erster_input = input("bitte nur einen ganzen zahl ")

        try:
            type_von_int = int(erster_input)
            fehler = False

        except:
            fehler = True

        if fehler == False:

            zweiter_input = input("gebe mir bitte nur einen komma zahl ")
            try:
                type_zweiter_input = int(zweiter_input)
                fehler_meldung = True
                continue

            except:
                fehler_meldung = False

                try:

                    type_von_float = float(zweiter_input)
                    ja = True
                    print(30*"-")
                    print(type_von_float+type_von_int)
                    print(30*"-")
                    break

                except:
                    ja = False


else:

    while (True):
        neuer_input = input("gebe mir bitte einen komma zahl ")
        try:
            type_zweiter_input = int(neuer_input)
            nicht_geschaft = True
            continue

        except:
            nicht_geschaft = True

            try:
                float_zahl = float(neuer_input)
                schon = True
                print(30*"-")
                print(float_zahl+type_erster_input)
                print(30*"-")
                break

            except:
                schon = False
                continue
