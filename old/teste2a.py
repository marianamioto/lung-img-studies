#!/usr/bin/env python
import PIL
import dicom
import skimage
import numpy as np

from skimage import measure, data, io, filters
from scipy.ndimage import gaussian_filter

  #adicione seu filtro aqui:

def contours(ds):
    level = ds.pixel_array.mean()
    contours = measure.find_contours(ds.pixel_array, level)

    for contour in contours:
        for x, y in contour:
            ds.pixel_array[x][y] = ds.pixel_array.max()


if __name__ == "__main__":
    ds=dicom.read_file("/Users/Mariana/Desktop/CT-01.dcm")
    contours(ds)
