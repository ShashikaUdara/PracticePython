from Person import *

class Employee(Person):
	empCount = 0

	def set_salary(self, salary):
		self.salary = salary

	def displayCount(self):
		print("The total employee count is %d" % Employee.empCount)

	def displayEmployee(self):
		print("Name: ", self.name, " - Salary: ", self.salary)


# emp1 = Employee("Udara", 31, "Kandy, SL", "0711234123")
# emp1.displayCount()
# emp1.displayEmployee()

# emp2 = Employee("Amal", 39, "Melbon, Aus", "0982342345")
# emp2.displayCount()
# emp2.displayEmployee()

# print("Employee.__doc__:", Employee.__doc__)
# print("Employee.__name__:", Employee.__name__)
# print("Employee.__module__:", Employee.__module__)
# print("Employee.__bases__:", Employee.__bases__)
# print("Employee.__dict__:", Employee.__dict__)

# # destroing objects (garbage collection)
# print(id(emp1))
# print(id(emp2))
# del emp1
# del emp2
# print(id(emp1)) error because no such obj
# print(id(emp2)) error because no such obj