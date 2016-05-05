#!/usr/bin/env python

import pydicom
import numpy
import PIL
import matplotlib.pyplot as plt
import skimage
import os


from test4 import segmentation
from contours import contours_segm
from pydicom.contrib.pydicom_PIL import show_PIL
from skimage import exposure, img_as_ubyte
from getRNU import getRNU
from getFiles import getFiles


def display(image):
    image_array = exposure.rescale_intensity(image,
                                               in_range=(image.min(),
                                                         image.max()))
    image_pil = PIL.Image.fromarray(img_as_ubyte(image_array), 'L')
    image_pil.show()

#abre imagem no diretorio especificado
#ds = pydicom.read_file("/Users/Mariana/Desktop/CT-01.dcm")
#image = ds.pixel_array
#level = 0 #ds.pixel_array.mean()
#max = ds.pixel_array.max()

#abre exame no diretorio especificado e armazena em uma lista os nomes de exames
#PathDicom = "/Users/Mariana/Desktop/ILDdatabase/ILD_DB_txtROIs/3"

lstFilesDCM = []
#for dirName, subdirList, fileList in os.walk(PathDicom):
   # for filename in fileList:
       # if ".dcm" in filename.lower():
           # lstFilesDCM.append(os.path.join(dirName,filename))

lstFilesDCM = getFiles()
for fileDCM in lstFilesDCM:
    ds=pydicom.read_file(fileDCM)
    image = ds.pixel_array
    level = 0 #ds.pixel_array.mean()
    max = ds.pixel_array.max()


    binary_global, binary_adaptive = segmentation(image)

    contour_global = contours_segm(binary_global, level, max)

    contour_adaptive = contours_segm(binary_adaptive, level, max)

#print(contour_global)
#print(level, max, ds.pixel_array.min())

    for contour in contour_adaptive:
        for x, y in contour:
            image[x][y] = max


    display(image)

#getRNU
#getRNU(image, binary_adaptive)
    #RNU
    print(getRNU(image, binary_adaptive))


#fig, axes = plt.subplots(1, 3, figsize=(20, 4))
#ax0, ax1, ax2 = axes
#plt.gray()


#ax0.imshow(image)
#ax0.set_title('Imagem Resultante')

#ax1.imshow(binary_global)
#ax1.set_title('Metodo Otsu')

#ax2.imshow(binary_adaptive)
#ax2.set_title('Metodo Adaptativo')

#for ax in axes:
 #   ax.axis('off')

#plt.show()
