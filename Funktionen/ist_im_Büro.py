
imBuero = ["Mahmoud", "Johny", "Markus"]


def istImBuero(name):

    if name in imBuero:
        return True
    else:
        return False


print(istImBuero("Daniel"))
print(istImBuero("Klaus"))
print(istImBuero("Markus"))
print(istImBuero("Mahmoud"))
