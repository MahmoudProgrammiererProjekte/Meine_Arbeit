
def gleicherInput(parameter):
    Schleife = ""

    while Schleife != parameter:
        Schleife = input("Neuer Input: ")
    return "RICHTIG!"


variable = input("Erster Input: ")
print(20*"-")
print(gleicherInput(variable))
print(20*"-")
