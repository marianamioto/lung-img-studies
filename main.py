#!/usr/bin/env python

import sys

import matplotlib.pyplot as plt
import numpy as np
import pydicom

from scipy import ndimage as ndi
from skimage import morphology
from skimage.filters import sobel

DEBUG = False


def plot(pixel_array, title=None):
    fig, ax = plt.subplots(figsize=(12, 9))
    ax.imshow(pixel_array, cmap=plt.cm.gray, interpolation='nearest')
    ax.axis('off')
    if title:
        ax.set_title(title)
    plt.show()


def plot_results(original_image, result_image):
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(6, 3), sharex=True,
                                   sharey=True)
    ax1.imshow(original_image, cmap=plt.cm.gray, interpolation='nearest')
    ax1.axis('off')
    ax1.set_adjustable('box-forced')
    ax2.imshow(result_image, interpolation='nearest')
    ax2.axis('off')
    ax2.set_adjustable('box-forced')
    margins = dict(hspace=0.01, wspace=0.01, top=1, bottom=0, left=0, right=1)
    fig.subplots_adjust(**margins)
    plt.show()


def open_dicom_image(image_path):
    return pydicom.read_file(image_path)


def extract_markers(pixel_array):

    # When using watershed we need to have at least two different markers.
    #   Zero means not a marker.
    markers = np.zeros_like(pixel_array)
    markers[pixel_array < 700] = 1  # TODO: move to const
    markers[pixel_array > 800] = 2  # TODO: move to const
    return markers


def segment_lungs(pixel_array):

    img_gray_open = ndi.grey_opening(pixel_array, size=10, mode='wrap')
    if DEBUG:
        plot(img_gray_open, 'Gray Opening')

    elavation_map = sobel(img_gray_open)
    if DEBUG:
        plot(elavation_map, 'Elevation Map')

    markers = extract_markers(img_gray_open)
    if DEBUG:
        plot(markers, 'Markers')

    watersheded = morphology.watershed(elavation_map, markers)
    if DEBUG:
        plot(watersheded, 'Watershed')

    external_contour = ndi.binary_fill_holes(watersheded-1)
    if DEBUG:
        plot(external_contour, 'External Contour')

    watersheded_no_contour = (watersheded - external_contour)
    if DEBUG:
        plot(watersheded_no_contour, 'Watershed (No Contour)')

    holes_filled = ndi.binary_fill_holes(watersheded_no_contour-1)
    if DEBUG:
        plot(holes_filled, 'Watershed (No Contour + Holes Filled)')

    removed_noise = morphology.remove_small_objects(holes_filled, 300)
    if DEBUG:
        plot(removed_noise, 'Removed Noise')

    return removed_noise


def main():
    try:
        image_path = sys.argv[1]
    except IndexError:
        print('A DICOM image should be provided as single argument')
        sys.exit(1)

    dicom_image = open_dicom_image(image_path)
    if DEBUG:
        plot(dicom_image.pixel_array, 'Original')

    segmented_image = segment_lungs(dicom_image.pixel_array)
    if DEBUG:
        plot(segmented_image, 'Segmented Lungs')

    plot_results(dicom_image.pixel_array, segmented_image)


if __name__ == '__main__':
    main()
