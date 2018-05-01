#!/usr/bin/env python

import pydicom
import PIL
import numpy as np

from skimage import exposure, img_as_ubyte

#from test4 import segmentation
#from contours import contours_segm

from getRNU import getRNU
from getFiles import getFiles
from skimage.filters import sobel
import matplotlib.pyplot as plt
from skimage import morphology
from skimage.morphology import watershed


from skimage.color import label2rgb
from scipy import ndimage as ndi

from skimage.measure import label

lstFilesDCM = []
lstFilesDCM = getFiles()

for fileDCM in lstFilesDCM:
    ds=pydicom.read_file(fileDCM)
    image = ds.pixel_array
    #couting number of gray levels 
    greylevels = np.unique(image)
    levels = np.unique(greylevels).shape[0]
    #calcula mapa de elevação 
    elevation_map = sobel(image / int(levels))
    #montagem das mascaras 
    markers = np.zeros_like(image / int(levels))
    markers[image < 600] = 1
    markers[image > 2800] = 0
   
    fig, ax = plt.subplots(figsize=(4, 3))
    ax.imshow(markers, cmap=plt.cm.gray, interpolation='nearest')
    ax.axis('off')
    ax.set_title('markers')
    plt.show()
    #tratamento para unir buracos grandes adjacentes 


    #tratamento de limpeza de pequenos buracos nas mascaras

    #fill_lungs = ndi.binary_fill_holes(markers)
    #fill_lungs = label(markers, return_num=False )
    #lungs_cleaned = morphology.remove_small_holes(fill_lungs, 500,
                                                        #connectivity=1)

    #fig, ax = plt.subplots(figsize=(4, 3))
    #ax.imshow(lungs_cleaned, cmap=plt.cm.autumn, interpolation='nearest')
    #ax.axis('off')
    #ax.set_title('Removing small holes')
    #plt.show()

    #aplicando transformada de watershed
    segmentation = watershed(elevation_map, markers)
    segmentation = ndi.binary_fill_holes(segmentation - 1)
    labeled_lung, _ = ndi.label(segmentation)
    image_label_overlay = label2rgb(labeled_lung, image=image)

    fig, axes = plt.subplots(1, 2, figsize=(8, 3), sharey=True)
    axes[0].imshow(image, cmap=plt.cm.gray, interpolation='nearest')
    axes[0].contour(segmentation, [0.5], linewidths=1.2, colors='y')
    axes[1].imshow(image_label_overlay, interpolation='nearest')


    plt.show()
