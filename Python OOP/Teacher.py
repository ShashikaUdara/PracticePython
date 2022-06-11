from Person import *

class Teacher(Person):
	def set_subject(self, subject):
		self.subject = subject

	def get_subject(self):
		return self.subject;