class Person:

    __name = "n/a"
    __age = 0
    __address = "n/a"

    def __init__(self, n, a):
        self.__name = n
        self.__age = a

    def set_name (self, n):
        self.__name = n

    def name (self):
        return self.__name

    def set_age (self, a):
        self.__age = a

    def age (self):
        return self.__age

    def set_address (self, ad):
        self.__address = ad

    def address (self):
        return self.__address

    def description_of_person(self):
        print("|===================|")
        print("Hi! My name is ", self.__name)
        print("I'm ", self.__age, "years old.")
        print("My adress is ", self.__address)

    @staticmethod
    def test_static():
        print("I'm simple static method")

    @classmethod
    def test_class(cls):
        print("I'm just class method")
