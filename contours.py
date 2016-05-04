#!/usr/bin/env python
""" Esta funcao chama a find_contours da biblioteca measure do pacote skimage
por enquanto(na qualificacao) ela precisa de 3 parametros
image
level
fully_connected
ela retorna uma lista com todos os contornos que o metodo find_contours consegue
encontrar na imagem """

import skimage
import numpy as np

import pydicom
import skimage
import numpy as np

from skimage import measure, data, io, filters


def contours_segm(image, level, max):
    contours = measure.find_contours(image, level, fully_connected='high')
    # print(contours[0][0])
    #for contour in contours:
      #  for x, y in contour:
       #     image[x][y] = max
    return contours


if __name__ == "__main__":
    ds=pydicom.read_file("/Users/Mariana/Desktop/IM-0001-0033-0001.dcm")
    image = ds.pixel_array
    level = ds.pixel_array.mean()
    max = ds.pixel_array.max()
    contours_segm(image, level, max)
