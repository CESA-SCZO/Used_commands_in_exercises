# %% MATPLOTLIB
import matplotlib.pyplot as plt
   
plt.figure()
plt.subplot(1,2,1)
plt.imshow(image1)
plt.title('Nadpis prvniho podobrazku')
plt.xlabel('Popis osi x [jednotky]')
plt.ylabel('Popis osi y [jednotky]')
plt.subplot(1,2,2)
plt.hist(image1.ravel())
plt.title('Nadpis druheho podobrazku')
plt.xlabel('Popis osi x [jednotky]')
plt.ylabel('Popis osi y [jednotky]')
plt.show()
plt.close('all')

# %% NUMPY

import numpy as np

img_shape = np.shape(image)

# %% SKIMAGE
import skimage.io
img = skimage.io.imread('path_to_image')