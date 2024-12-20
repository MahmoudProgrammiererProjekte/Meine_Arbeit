gebe_mir_satz = input("gebe mir bitte einen satz deiner wahl ")
suchwort = input("gebe mir bitte ein wort das im satz enthalten ")


def such_wort_in_text(text, wort):
    woerter = text.split(wort)
    return len(woerter)-1


Nur_ein_wort = suchwort.split(" ")

while len(Nur_ein_wort) > 1:
    suchwort_ = input("NUR EIN WORT! ")
    split_suchwort = suchwort_.split(" ")
    if len(split_suchwort) == 1:
        woerter = gebe_mir_satz.split(suchwort_)
        print(40*"-")
        print("Dein wort", suchwort_, "kommt",
              len(woerter)-1, "mal im Text vor!")
        print(40*"-")
        break


Variabl = such_wort_in_text(gebe_mir_satz, suchwort)

print(40*"-")
print("Dein wort", suchwort, "kommt", Variabl, "mal im Text vor!")
print(40*"-")
