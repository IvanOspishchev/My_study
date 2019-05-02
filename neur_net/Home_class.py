from Person_class import Person

class Home:

    __address = "n/a"
    __list_of_residents = ['n/a']

    def __init__(self, a):
        self.__address = a

    def set_address(self, a):
        self.__address = a

    def address(self):
        return self.__address

    def settle_person(self, p):
        if isinstance(p, Person):
            self.__list_of_residents.append(p)
            p.set_address(self.__address)

    def evect_person(self, p):
        self.__list_of_residents.remove(p)
        p.set_adress("n/a")

    def description_of_home(self):
        print("|=============|")
        print("# Address of this house is ", self.__address)
        print("# List of residents: ")
        for p in self.__list_of_residents:
            if isinstance(p, Person):
                print("# - ", p.name())
