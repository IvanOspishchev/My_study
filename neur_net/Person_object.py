from Person_class import Person
from Home_class import Home
from Programmer_subclass import Programmer
from Journalist_subclass import Journalist

person_first = Programmer("Ivan", 27)
person_second = Journalist("Julia", 26)
house = Home("Starpetrovsky")

person_first.set_prog_exp(4)
person_second.set_exp(6)

house.settle_person(person_first)
house.settle_person(person_second)

person_first.description_of_person()
person_second.description_of_person()

house.description_of_home()

# person_first.test_static()
# person_second.test_class()
