Variable = input("Schreibe mir einen Satz deiner Wahl auf: ")
satz_zeichen = len(Variable)
if satz_zeichen > 10:
    print(30*"-")
    print("10+++")
    print(30*"-")
if satz_zeichen < 10:
    print(30*"-")
    print("10---")
    print(30*"-")
if satz_zeichen == 10:
    print(30*"-")
    print("!!! 10 !!!")
    print(30*"-")
