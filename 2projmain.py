#!/usr/bin/env python

import pydicom
import numpy

import matplotlib.pyplot as plt

from test4 import segmentation

ds = pydicom.read_file("/Users/Mariana/Desktop/IM-0001-0033-0001.dcm")
image = ds.pixel_array

binary_global, binary_adaptive = segmentation(image)

fig, axes = plt.subplots(nrows=3, figsize=(20, 24))
ax0, ax1, ax2 = axes
plt.gray()

ax0.imshow(image)
ax0.set_title('Image')

ax1.imshow(binary_global)
ax1.set_title('Li  thresholding')

ax2.imshow(binary_adaptive)
ax2.set_title('Adaptive thresholding')

for ax in axes:
    ax.axis('off')

plt.show()
