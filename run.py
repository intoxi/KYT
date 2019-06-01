
class Person():

    def __init__(self):
        self.name = "Tomek"
        self.surname = "Kowalski"
        self.age = 25

class Employe(Person):

    def __init__(self):
        super().__init__()
        self.position = "Programer"
        self.specialization = "Python"

class Client(Person):

    def __init__(self):
        super().__init__()
        self.ordered = "Website"

pracownik = Employe()
print(pracownik.name)
print(pracownik.position)


klient = Client()
print(klient.name)
print(klient.ordered)