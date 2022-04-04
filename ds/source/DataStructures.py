class DataStructures:
	def __init__(self, name, date):
		print("init : DataStructures")
		self.name = name
		self.date = date

	def controllerFunctionforSorting(self):
		print('DataStructures : ', self.name, " - ", self.date)


ds = DataStructures("Sorting Algos", "04/04/2022")
ds.controllerFunctionforSorting()