# matrix multiplication using Divide and Conquer Paradigm
# intro to Strassen's algorithm (1969)

# so, I've just finished watching the lecture and I've reached to a conclusion that Straussen's algorithm uses 7 product that subs the general divide and conquer approach for matrix 
# multiplication of time complexity O(n^3)
# In this script I'll generate two random 2x2 matrices and multiply them using the initial algo

import random

def matrix_generation(n):
	# generation of an empty nxn matrix
	brac = 0
	matrix = []
	no_of_rows = n
	no_of_cols = n
	while brac < n:
		matrix.append([])
		brac+=1
	
	# populating the matrix
	for row in range(no_of_rows):
		for col in range(no_of_cols):
			matrix[row].append(random.randint(0,10))
	

	


	return matrix

print(matrix_generation(4))
