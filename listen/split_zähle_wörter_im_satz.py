
def such_wort_in_text(text, wort):
    woerter = text.split(wort)
    print(woerter)
    return len(woerter)-1


gebe_mir_satz = input("gebe mir bitte einen satz deiner wahl ")
suchwort = input("gebe mir bitte ein wort das im satz enthalten ")


Variabl = such_wort_in_text(gebe_mir_satz, suchwort)

print(40*"-")
print("Dein wort", suchwort, "kommt", Variabl, "mal im Text vor!")
print(40*"-")


# -----------------------------------------------------------------------------
#            zweite Lösung ohne Len()!
# ------------------------------------------------------------------------------
# def such_wort_in_text(text, wort):
#     zahl = 0
#
#     woerter = text.split(wort)
#
#     for schleife in woerter:
#         zahl = zahl + 1
#
#     return zahl-1
#
#
# gebe_mir_satz = input("gebe mir bitte einen satz deiner wahl ")
# suchwort = input("gebe mir bitte ein wort das im satz enthalten ")
# Variabl = such_wort_in_text(gebe_mir_satz, suchwort)
#
# print(40*"-")
# print("Dein wort", suchwort, "kommt", Variabl, "mal im Text vor!")
# print(40*"-")
