#!/usr/bin/env python

import matplotlib
import matplotlib.pyplot as plt
import dicom
import numpy
from skimage.data import camera

from skimage.filters import threshold_otsu

from teste2a import contours

matplotlib.rcParams['font.size'] = 9

ds = dicom.read_file("/Users/Mariana/Desktop/CT-0015.dcm")
image = ds.pixel_array
thresh = threshold_otsu(image)
binary = image > thresh

fig, (ax1, ax2, ax3) = plt.subplots(1, 3, figsize=(8, 2.5))
fig = plt.figure(figsize=(8, 2.5))
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
ax3.set_title('Threshold')
ax3.axis('off')

plt.show()
