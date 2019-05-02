from Person_class import Person

class Journalist(Person):

    __exp = 0

    def set_exp(self, ex):
        self.__exp = ex

    def exp(self):
        return self.__exp

    def description_of_person(self):
        super().description_of_person()
        print("I'm journalist my exp", self.__exp, "years")