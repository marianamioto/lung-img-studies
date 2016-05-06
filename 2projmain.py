#!/usr/bin/env python

import pydicom
import PIL

from test4 import segmentation
from contours import contours_segm
from skimage import exposure, img_as_ubyte
from getRNU import getRNU
from getFiles import getFiles


def display(image):
    image_array = exposure.rescale_intensity(image,
                                               in_range=(image.min(),
                                                         image.max()))
    image_pil = PIL.Image.fromarray(img_as_ubyte(image_array), 'L')
    image_pil.show()

lstFilesDCM = []
lstFilesDCM = getFiles()
for fileDCM in lstFilesDCM:
    ds=pydicom.read_file(fileDCM)
    image = ds.pixel_array
    level = 0 # ds.pixel_array.mean() esse level precisa ser estudado
    max = ds.pixel_array.max()


    binary_global, binary_adaptive = segmentation(image)

    contour_global = contours_segm(binary_global, level, max)

    contour_adaptive = contours_segm(binary_adaptive, level, max)


    # escreve o contorno na imagem
    for contour in contour_global:
        for x, y in contour:
            image[x][y] = max
    display(image)

    # RNU
    print(getRNU(image, binary_adaptive))
