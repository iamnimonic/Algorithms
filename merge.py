import numpy as np
import random

def mergeSort(arr):
	if len(arr) > 1:
		mid = len(arr)//2
		L = arr[:mid]
		R = arr[mid:]

		mergeSort(L)
		mergeSort(R)
		i = j = k = 0
		while i < len(L) and j < len(R):
			if L[i] < R[j]:
				arr[k] = L[i]
				i+=1
			else:
				arr[k] = R[j]
				j+=1
			k+=1
		while i < len(L):
			arr[k] = L[i]
			i+=1
			k+=1

		while j < len(R):
			arr[k] = R[j]
			j+=1
			k+=1
			
def printer(arr):
	print("{} : MergeSorted Array.".format(arr))

if __name__ == "__main__":
	array = []
	array_size = random.randint(0,10)
	for i in range(array_size):
		elem = random.randint(0,10)
		array.append(elem)
	print("{} : Unsorted Array.".format(array))
	mergeSort(array)
	printer(array)