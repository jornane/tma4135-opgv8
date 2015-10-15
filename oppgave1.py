import imagestuff
import matplotlib.pyplot as plt

img = imagestuff.readpgm('lena.pgm')
imagestuff.showimage(img)

fig = plt.figure()
ax = fig.add_subplot(111)
ax.plot(range(0,len(img[100])), img[100], color='black', label='thingy')
plt.show()
