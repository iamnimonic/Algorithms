import random

def inversionCount(arr):
	count = 0
	if len(arr) == 1:
		return 0
	else:
		for i in range(len(arr)):
			for j in range(i+1, len(arr)):
				if (arr[i] > arr[j]):
					count += 1
		return count 

if __name__ == "__main__":
	array = []
	array_size = random.randint(0,10)
	for i in range(array_size):
		elem = random.randint(0,10)
		array.append(elem)
	print("The array is : {} ".format(array))
	print("No of inversions are : {}".format(inversionCount(array)))