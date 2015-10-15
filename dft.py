import numpy as np

def dft(b):
	return np.fft.fftshift(np.fft.fft2(b))

def invdft(c):
	return np.fft.ifft2(np.fft.ifftshift(c))

