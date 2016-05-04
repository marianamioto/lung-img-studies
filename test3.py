#!/usr/bin/env python

import matplotlib
import matplotlib.pyplot as plt

import pydicom
import matplotlib.pyplot as plt
import numpy

from skimage.filters import threshold_otsu, threshold_adaptive
from skimage import exposure, img_as_ubyte

from test2 import contours

matplotlib.rcParams['font.size'] = 9

ds = pydicom.read_file("/Users/Mariana/Desktop/CT-01.dcm")
image = ds.pixel_array

#imgMtrx = imgMtrx.astype(float) / 255
#converte a imagem para 255
#image = image.astype(float) / 255

image = exposure.rescale_intensity(ds.pixel_array,
                                   in_range=(ds.pixel_array.min(),
                                             ds.pixel_array.max()))
image = img_as_ubyte(image)

#thresh = threshold_otsu(image)
#binary = image > thresh

block_size = 255
binary = threshold_adaptive(image, block_size, offset=5)

print(image.max())

#fig, (ax1, ax2, ax3) = plt.subplots(1, 3, figsize=(8, 2.5))
fig = plt.figure(figsize=(15, 4))
ax1 = plt.subplot(1, 3, 1, adjustable='box-forced')
ax2 = plt.subplot(1, 3, 2)
ax3 = plt.subplot(1, 3, 3, sharex=ax1, sharey=ax1, adjustable='box-forced')


ax1.imshow(image, cmap=plt.cm.gray)
ax1.set_title('Original')
ax1.axis('off')

ax2.hist(image)
ax2.set_title('Histograma')
#ax2.axvline(thresh, color='r')

ax3.imshow(binary, cmap=plt.cm.gray)
ax3.set_title('Binarizacao')
ax3.axis('off')

plt.show()
