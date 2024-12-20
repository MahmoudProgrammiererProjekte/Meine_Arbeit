class ToolsMitarbeiter:
    def __init__(self):
        self.name = None
        self.alter = None
        self.in_der_Firma_seit = None

    def eigenschaften(self):
        print(50*"-")
        print("Der Mitarbeiter: ", self.name,
              " ist so alt: ", self.alter)
        print("Der Mitarbeiter: ", self.name, "ist seit: ",
              self.in_der_Firma_seit, "in der Firma")
        print(50*"-")


avl_daniel = ToolsMitarbeiter()

avl_daniel.name = "Johny"
avl_daniel.alter = 29
avl_daniel .in_der_Firma_seit = "1.10.2018"


avl_mahmoud = ToolsMitarbeiter()
avl_mahmoud.name = "Mahmoud"
avl_mahmoud .alter = 27
avl_mahmoud.in_der_Firma_seit = "1. 9. 2022"

avl_daniel.eigenschaften()
avl_mahmoud.eigenschaften()
