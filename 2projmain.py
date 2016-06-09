#!/usr/bin/env python

import pydicom
import PIL
import numpy as np


from test4 import segmentation
from contours import contours_segm
from skimage import exposure, img_as_ubyte
from getRNU import getRNU
from getFiles import getFiles
from skimage.filters import sobel
import matplotlib.pyplot as plt
from skimage import morphology

from skimage.color import label2rgb
from scipy import ndimage as ndi

from skimage.measure import label

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
    ##########################################################################

    # binary_global, binary_adaptive = segmentation(image)

    # contour_global = contours_segm(binary_global, level, max)

    # contour_adaptive = contours_segm(binary_adaptive, level, max)


    # escreve o contorno na imagem
    # for contour in contour_global:
    #    for x, y in contour:
    #        image[x][y] = max

    # display(image)

    # RNU
    # print(getRNU(image, binary_adaptive))

    ##########################################################################

    elevation_map = sobel(image/255.)

    markers = np.zeros_like(image/255.)
    markers[image < 600] = 1
    markers[image > 2800] = 0

    segmentation = morphology.watershed(elevation_map, markers)

    fig, ax = plt.subplots(figsize=(4, 3))
    ax.imshow(markers, cmap=plt.cm.gray, interpolation='nearest')
    ax.axis('off')
    ax.set_title('markers')
    plt.show()

    # plt.imsave(fileDCM, segmentation, format = 'png', cmap = plt.cm.gray)

    #treament for small holes in markers

    # fill_lungs = ndi.binary_fill_holes(markers)
    fill_lungs = label(markers, return_num=False )
    lungs_cleaned = morphology.remove_small_holes(fill_lungs, 500,
                                                        connectivity=1)

    fig, ax = plt.subplots(figsize=(4, 3))
    ax.imshow(lungs_cleaned, cmap=plt.cm.gray, interpolation='nearest')
    ax.axis('off')
    ax.set_title('Removing small holes')
    plt.show()



    segmentation = ndi.binary_fill_holes(segmentation-1)
    labeled_image, _ = ndi.label(lungs_cleaned)
    image_label_overlay = label2rgb(labeled_image, image=image, bg_label = 0,
                                        bg_color=(1, 0, 0))


    # fig, ax = plt.subplots(figsize=(4, 3))
    # ax.imshow(image_label_overlay, cmap=plt.cm.gray, interpolation='nearest')
    # ax.axis('off')
    # ax.set_title('Filling the holes')
    # plt.show()

    # labeled_image, _ = ndi.label(markers)
    # image_label_overlay = label2rgb(labeled_image, image=image, bg_label = 0,
    #                                   bg_color=(1, 0, 0))

    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(6, 3), sharex=True,
                                    sharey=True)
    ax1.imshow(image, cmap=plt.cm.gray, interpolation='nearest')
    ax1.contour(lungs_cleaned, [0.5], linewidths=1.2, colors='y')
    ax1.axis('off')
    ax1.set_adjustable('box-forced')
    ax2.imshow(image_label_overlay, interpolation='nearest')
    ax2.axis('off')
    ax2.set_adjustable('box-forced')
    margins = dict(hspace=0.01, wspace=0.01, top=1, bottom=0, left=0, right=1)
    fig.subplots_adjust(**margins)

    plt.show()
