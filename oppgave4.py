import numpy as np
import math
import dft
import oppgave3 as o3

def compress(X, r):
	X = dft.dft(X)
	return o3.submatrix(X, math.ceil(len(X)*r), math.ceil(len(X[0])*r))
