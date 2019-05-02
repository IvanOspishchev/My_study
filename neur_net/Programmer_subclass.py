from Person_class import Person

class Programmer(Person):

    __prog_exp = 0

    def set_prog_exp(self, px):
        self.__prog_exp = px

    def prog_exp(self):
        return self.__prog_exp

    def description_of_person(self):
     super().description_of_person()
     print("I'm programmer my exp is ", self.__prog_exp, "months")
