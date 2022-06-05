class Person:
	def __init__(self, name, age, address, phone):
		self.name = name
		self.age = age
		self.address = address
		self.phone = phone

	def get_name(self):
		return self.name

	def get_age(self):
		return self.age

	def get_address(self):
		return self.address

	def get_phone(self):
		return self.phone

man = Person("Udara", 31, "Kandy, Sri Lanka", "1112223330")
print(man.get_name())
print(man.get_age())
print(man.get_address())
print(man.get_phone())