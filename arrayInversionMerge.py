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
	return (arr)

def inversionCount(arr):
	if len(arr) == 1:
		return 0
	else:
		mid = len(arr)//2
		L = arr[:mid]
		R = arr[mid:]

		i = j = k = 0
		inversionCount = 0
		while  i < len(L) and j < len(R):
			if L[i] < R[j]:
				arr[k] = L[i]
				i+=1
			elif L[i] == R[j]:
				arr[k] = L[i]
				i+=1
			else:
				arr[k] = R[j]
				j+=1
				inversionCount += (mid - i)
				print(str(inversionCount) + "inv count")
			k+=1

		print(inversionCount)
		print(arr)
		return("{} : left sub-array\n{} : right sub-array".format((mergeSort(L)), (mergeSort(R))))




if __name__ == "__main__":
	array = []
	array_size = random.randint(0,10)
	for i in range(array_size):
		elem = random.randint(0,10)
		array.append(elem)
	print("The array is : {} ".format(array))
	print("{}".format(inversionCount(array)))
	# print("No of inversions are : {}".format(inversionCount(array)))