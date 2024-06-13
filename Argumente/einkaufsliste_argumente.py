from sys import argv
import os


if len(argv) >= 2:
    Verzeichnisinhalt = os.listdir()

    if argv[1] in Verzeichnisinhalt:

        print(30*"-")

        if len(argv) > 2:

            listen_leer = []
            for durch_liste in argv:
                listen_leer.append(durch_liste+"\n")
            del listen_leer[0]
            del listen_leer[0]

            with open(argv[1], "r")as f:
                s = f.readlines()

            kh = []
            for schleife in listen_leer:
                if schleife not in kh:
                    kh.append(schleife)

            for schleife in kh:
                if schleife not in s:
                    with open(argv[1], "a")as f:
                        h = f.write(schleife)

            print(
                argv[1], " gibt es schon und nach deinem neuen hinzufügen schaut die Liste so aus:")

            with open(argv[1], "r")as f:
                lesen = f.read()
            print(lesen)
            print(30*"-")

        if len(argv) == 2:
            print(
                argv[1], " gibt es schon. Du hast aber hier keine Argumente gegeben. Auch hier die Liste:")
            with open(argv[1], "r")as f:
                lesen = f.read()

            print(lesen)
            print(30*"-")

    else:
        if len(argv) == 2:

            f = open(argv[1], "w")
            f.close()

            print(30*"-")
            print(argv[1], " wurde neu erstellt und hat gar keine Einträge")

        if len(argv) > 2:

            listen_leer = []
            for durch_liste in argv:
                listen_leer.append(durch_liste+"\n")
            del listen_leer[0]
            del listen_leer[0]
            with open(argv[1], "w")as f:
                for j in listen_leer:
                    file = f.write(j)
            with open(argv[1], "r")as f:
                liste = f.readlines()

            leer = []
            for argumente in liste:
                if argumente not in leer:
                    leer.append(argumente)

                    with open(argv[1], "w")as f:
                        for j in leer:
                            file = f.write(j)

            print(
                argv[1], " wurde nue erstellt und nach deinem neuen hinzufügen schaut die Liste so aus:")
            print(30*"-")
            with open(argv[1], "r")as f:
                f = f.read()
            print(f)
            print(30*"-")
