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