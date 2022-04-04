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

	def quickSort(self, low, high):
		if(low < high):
			pi = SortingAlgos.partition(self.arrNum, low, high)
			SortingAlgos.quickSort(self, low, pi-1)
			SortingAlgos.quickSort(self, pi+1, high)


	def partition(arrNum, low, high):
		pivote = arrNum[high-1]
		i = low - 1

		for j in range(high-low+1):
			if(arrNum[j+low] <= pivote):
				i += 1
				temp = arrNum[j+low]
				arrNum[j+low] =arrNum[i]
				arrNum[i]  = temp
		i += 1
		temp = arrNum[j+low]
		arrNum[j+low] = arrNum[i]
		arrNum[i]  =temp

		return i