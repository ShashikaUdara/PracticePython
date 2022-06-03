class Employee:
	empCount = 0

	def __init__(self, name, salary):
		self.name = name
		self.salary = salary
		Employee.empCount += 1

	def displayCount(self):
		print("The total employee count is %d" % Employee.empCount)

	def displayEmployee(self):
		print("Name: ", self.name, " - Salary: ", self.salary)

emp1 = Employee("Udara", 5000)
emp1.displayCount()
emp1.displayEmployee()

emp2 = Employee("Amal", 2000)
emp2.displayCount()
emp2.displayEmployee()

print("Employee.__doc__:", Employee.__doc__)
print("Employee.__name__:", Employee.__name__)
print("Employee.__module__:", Employee.__module__)
print("Employee.__bases__:", Employee.__bases__)
print("Employee.__dict__:", Employee.__dict__)

# destroing objects (garbage collection)
print(id(emp1))
print(id(emp2))
del emp1
del emp2
# print(id(emp1)) error because no such obj
# print(id(emp2)) error because no such obj