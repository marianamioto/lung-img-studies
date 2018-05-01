#!/usr/bin/env python

import PIL
import pydicom
import skimage

from pydicom.contrib.pydicom_PIL import show_PIL
from skimage import exposure, img_as_ubyte

def display(ds):
    image_array = exposure.rescale_intensity(ds.pixel_array,
                                             in_range=(ds.pixel_array.min(),
                                                       ds.pixel_array.max()))
    image = PIL.Image.fromarray(img_as_ubyte(image_array), 'L')
    image.show()

if __name__ == "__main__":
    ds = pydicom.read_file("/Users/Mariana/Desktop/MIP-80364/IM-0001-0009-0001.dcm")
    display(ds)
