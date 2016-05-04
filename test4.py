#!/usr/bin/env python

import matplotlib.pyplot as plt
import pydicom
import numpy


from skimage import data
from skimage.filters import threshold_otsu, threshold_adaptive, threshold_li

#ds = pydicom.read_file("/Users/Mariana/Desktop/IM-0001-0033-0001.dcm")
#image = ds.pixel_array

def segmentation(image):
    global_thresh = threshold_otsu(image)
    binary_global = image > global_thresh

    block_size = 255
    binary_adaptive = threshold_adaptive(image, block_size, offset=5)

    return binary_global, binary_adaptive

#fig, axes = plt.subplots(nrows=3, figsize=(7, 8))
#ax0, ax1, ax2 = axes
#plt.gray()

#ax0.imshow(image)
#ax0.set_title('Image')

#ax1.imshow(binary_global)
#ax1.set_title('Otsu')

#ax2.imshow(binary_adaptive)
#ax2.set_title('Adaptativo')

#for ax in axes:
#    ax.axis('off')

#plt.show()
