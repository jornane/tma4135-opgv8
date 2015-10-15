import imagestuff
import matplotlib.pyplot as plt
import dft
import numpy as np

import oppgave4 as o4
import oppgave6 as o6

img = imagestuff.readpgm('lena.pgm')
m = len(img)
n = len(img[0])
img = o4.compress(img, .3)
#imagestuff.showimage(dft.invdft(img).real)
img = o6.decompress(img, m, n)
imagestuff.showimage(img)
