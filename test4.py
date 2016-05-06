#!/usr/bin/env python

import pydicom

from skimage.filters import threshold_otsu, threshold_adaptive


def segmentation(image):
    global_thresh = threshold_otsu(image)
    binary_global = image > global_thresh

    block_size = 255
    binary_adaptive = threshold_adaptive(image, block_size, offset=5)

    return binary_global, binary_adaptive


if __name__ == "__main__":
    ds = pydicom.read_file("/Users/Mariana/Desktop/CT-0015.dcm")
    image = ds.pixel_array
    segmentation(image)
