from sys import argv

if len(argv) <= 1:
    print("du hast keine Argumente an das python file gegeben")


else:
    print("Hir deine Argumente: ")
    print(20*"-")
    Argumente = argv
    del Argumente[0]
    for argument in Argumente:
        print(argument)
    print(20*"-")
