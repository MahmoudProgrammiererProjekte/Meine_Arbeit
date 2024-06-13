# Start

# Eingabe: Jahr
Jahr = int(input("Jahr :"))

# Jahr Mod 4 == 0
Mod = Jahr % 4
# nein
if Mod != 0:
    print("kein Schaltjahr")

# Jahr ist durch 4 teilbar ?
# ja
else:
    Division = Jahr % 100
# Jahr ist durch 100 teilbar ?
# nein
    if Division != 0:
        print("Schaltjahr")
# ja
    else:

        # Jahr ist durch 400 teilbar ?
        Division_400 = Jahr % 400

# nein
        if Division_400 != 0:
            print("kein schaltjahr")
# ja
        else:
            print("Schaltjahr")
