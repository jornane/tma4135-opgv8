import numpy as np
import dft
import math

import oppgave3 as o3

def padmatrix(X, m, n):
	# this does weird things, don't use
	#B = np.zeros(shape=(m, n))
	B = []
	for a in range(0, m):
		B.append([])
		for b in range(0, n):
			B[a].append(0)
	i = len(X)
	j = len(X[0])

	k = int(m / 2 - i / 2)
	l = int(n / 2 - j / 2)
	print m, n, i, j, k, l
	# won't work without numpy
	#B[k:i+k, l:j+l] = X
	for a in range(0, i):
		for b in range(0, j):
			B[k+a][l+b] = X[a][b]
	return B

def decompress(X, m, n):
	i = len(X)
	j = len(X[0])
	B = padmatrix(X, m, n)
	return dft.invdft(B).real


#print padmatrix([[1,1],[1,1]], 6, 6)