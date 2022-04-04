class SortingAlgos:
	def __init__(self, arrNum):
		print("init : SortingAlgos")
		self.arrNum = arrNum

	def bubbleSort(self):
		for i in range(len(self.arrNum)-1):
			for j in range(len(self.arrNum)-1-i):
				if(self.arrNum[j] > self.arrNum[j+1]):
					temp = self.arrNum[j]
					self.arrNum[j] = self.arrNum[j+1]
					self.arrNum[j+1] = temp