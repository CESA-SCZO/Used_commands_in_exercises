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

image = np.zeros_like(image)
image = np.ones(x_size, y_size)
img_shape = np.shape(image)
vector = np.linspace(start = start, stop = stop, num = num)

spectrum = amplitude_spectrum * np.exp(1j*phase_spectrum)
spectrum_1 = np.log(np.fft.fftshift(np.abs(np.fft.fft2(image))))
spectrum_2 = np.fft.fftshift(np.angle(np.fft.fft2(image)))
image = np.real(np.fft.ifft2(spectrum))

# %% SCIPY
import scipy
image = scipy.signal.convolve2d(image, impulse_response, mode = 'mode_type')
filtered_image = scipy.signal.medfilt2d(image, kernel_size = size_of_the_kernel)
mat = scipy.io.loadmat('path_to_mat_file').get('label')
gaussian_filter = scipy.ndimage.gaussian_filter(input = dirac_impulse, sigma = sigma)


# %% SKIMAGE
import skimage
image = skimage.io.imread('path_to_image')
gs_image = skimage.color.rgb2gray(image)
float_img = skimage.img_as_float(image)
image = skimage.transform.rotate(image,angle)
equalised_image = skimage.exposure.equalize_hist(image)
equalised_image = skimage.exposure.equalize_adapthist(image, clip_limit = limit)
