import SortingAlgos

class DataStructures:
	def __init__(self, name, date):
		print("init : DataStructures")
		self.name = name
		self.date = date

	def controllerFunctionforSorting(self):
		print('DataStructures : ', self.name, " - ", self.date)
		arrNum = [45,23,56,89,55,11,22,66,88,33,5,2,1,4,9,8,6,3,2,1]
		obj = SortingAlgos.SortingAlgos(arrNum)
		obj.bubbleSort()
		for x in arrNum:
			print(x)

		obj.quickSort(0, len(arrNum))
		for x in arrNum:
			print("-- ", x)


ds = DataStructures("Sorting Algos", "04/04/2022")
ds.controllerFunctionforSorting()