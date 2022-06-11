from Person import *
from Teacher import *

man = Person("Udara", 31, "Kandy, Sri Lanka", "1112223330")
print(man.get_name())
print(man.get_age())
print(man.get_address())
print(man.get_phone())

tech = Teacher("Udari", 27, "Kandy, Sri Lanka", "1234567891")
print(tech.get_name())
print(tech.get_age())
print(tech.get_address())
print(tech.get_phone())

tech.set_subject("Maths")
print(tech.get_subject())