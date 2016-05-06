#!/usr/bin/env python
"""Esta funcao realiza um contorno simples da imagem"""
import pydicom
from skimage import measure
from utils import display

# adicione seu filtro aqui:


def contours(ds):
    level = ds.pixel_array.mean()
    # print(level)
    contours = measure.find_contours(ds.pixel_array, level)
    # print(contours)
    for contour in contours:
        for x, y in contour:
            ds.pixel_array[x][y] = ds.pixel_array.max()


if __name__ == "__main__":
    ds = pydicom.read_file("/Users/Mariana/Desktop/CT-0015.dcm")
    contours(ds)
    display(ds)
