#!/usr/bin/env python

import matplotlib
import pydicom
import matplotlib.pyplot as plt

from skimage.filters import threshold_otsu, threshold_adaptive
from skimage import exposure, img_as_ubyte

matplotlib.rcParams['font.size'] = 9

ds = pydicom.read_file("/Users/Mariana/Desktop/CT-01.dcm")
image = ds.pixel_array

image = exposure.rescale_intensity(ds.pixel_array,
                                   in_range=(ds.pixel_array.min(),
                                             ds.pixel_array.max()))
image = img_as_ubyte(image)

thresh = threshold_otsu(image)
binary = image > thresh

block_size = 255
# binary = threshold_adaptive(image, block_size, offset=5)

print(image.max())

fig = plt.figure(figsize=(15, 4))
ax1 = plt.subplot(1, 3, 1, adjustable='box-forced')
ax2 = plt.subplot(1, 3, 2)
ax3 = plt.subplot(1, 3, 3, sharex=ax1, sharey=ax1, adjustable='box-forced')


ax1.imshow(image, cmap=plt.cm.gray)
ax1.set_title('Original')
ax1.axis('off')

ax2.hist(image)
ax2.set_title('Histograma')
ax2.axvline(thresh, color='r')

ax3.imshow(binary, cmap=plt.cm.gray)
ax3.set_title('Binarizacao')
ax3.axis('off')

plt.show()
