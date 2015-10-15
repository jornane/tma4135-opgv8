import numpy as np
import math

def submatrix(X, i, j):
	m = len(X)
	n = len(X[0])
	k = m / 2 - i / 2
	l = n / 2 - j / 2
	return X[k:i+k, l:j+l]

#B = np.array([[1, 2, 3],
#              [4, 5, 6],
#              [7, 8, 9]])
#X = np.array([[1, 1, 1, 1, 1, 1],
#              [1, 1, 1, 1, 1, 1],
#              [1, 1, 5, 5, 1, 1],
#              [1, 1, 5, 5, 1, 1],
#              [1, 1, 1, 1, 1, 1],
#              [1, 1, 1, 1, 1, 1]])
#Y = np.array([[1, 1, 1, 1, 1, 1, 1],
#              [1, 1, 1, 1, 1, 1, 1],
#              [1, 1, 5, 5, 5, 1, 1],
#              [1, 1, 5, 5, 5, 1, 1],
#              [1, 1, 5, 5, 5, 1, 1],
#              [1, 1, 1, 1, 1, 1, 1],
#              [1, 1, 1, 1, 1, 1, 1]])

#print submatrix(B, 2, 2)
#print submatrix(X, 2, 2)
#print submatrix(Y, 1, 1)
#print submatrix(Y, 2, 2)
#print submatrix(Y, 3, 3)
#print submatrix(Y, 4, 4)
#print submatrix(Y, 5, 5)
