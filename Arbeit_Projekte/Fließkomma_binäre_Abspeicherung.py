import os
import struct
import sys


def Wandeln_DZ_ieee_754(decimal_number):
    tabelle = ""
    for x in range(31, -1, -1):
        tabelle += "|" + str(x).rjust(2)

    # Umwandlung in IEEE 754-Format (einfache Präzision)
    binary_representation = struct.pack('f', decimal_number)
    hex_representation = struct.unpack('I', binary_representation)[0]

    # Ausgabe des binären und hexadezimalen Werts
    binDar = format(hex_representation, '032b')
    print(binDar)
    print("--------------------------------")
    binStr = ""

    for x in str(binDar):
        binStr += "|" + x.rjust(2)

    return tabelle + "\n" + binStr + "\n"


if __name__ == "__main__":
    os.system("cls")

    if len(sys.argv) != 2:
        print("Nicht genug Argumente")
        sys.exit(1)

    decimal_number = float(sys.argv[1])
    ergebnis = Wandeln_DZ_ieee_754(decimal_number)
    print(ergebnis)
