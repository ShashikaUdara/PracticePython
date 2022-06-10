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