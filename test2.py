#!/usr/bin/env python

import PIL
import pydicom
import skimage
import numpy as np

from skimage import measure, data, io, filters

from utils import display

from scipy.ndimage import gaussian_filter

#adicione seu filtro aqui:

def contours(ds):
    level = ds.pixel_array.mean()
    #print(level)
    contours = measure.find_contours(ds.pixel_array, level)
    #print(contours)
    for contour in contours:
        for x, y in contour:
            ds.pixel_array[x][y] = ds.pixel_array.max()

def filterSobel(ds):
    image = ds.pixel_array  # or any NumPy array!
    edges = filters.sobel(image)
    io.imshow(edges)
    io.show()



if __name__ == "__main__":
    ds=pydicom.read_file("/Users/Mariana/Desktop/IM-0001-0033-0001.dcm")
    contours(ds)
    display(ds)
    #filterSobel(ds)
