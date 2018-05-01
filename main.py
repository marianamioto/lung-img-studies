#!/usr/bin/env python

import sys

import matplotlib.pyplot as plt
import numpy as np
import pydicom

from skimage import morphology
from skimage.measure import label


def plot_image(pixel_array, title=None):
    fig, ax = plt.subplots(figsize=(4, 3))
    ax.imshow(pixel_array, cmap=plt.cm.gray, interpolation='nearest')
    ax.axis('off')
    if title:
        ax.set_title(title)
    plt.show()


def open_dicom_image(image_path):
    return pydicom.read_file(image_path)


def extract_markers(pixel_array):
    levels = pixel_array.max()

    markers = np.zeros_like(pixel_array/levels)
    markers[pixel_array < 600] = 1  # TODO: move to const
    markers[pixel_array > 2800] = 0  # TODO: move to const
    return markers


def remove_small_holes(pixel_array):
    fill_lugs = label(pixel_array, return_num=False)
    return morphology.remove_small_holes(
        fill_lugs,
        500,  # TODO: move to const
        connectivity=1,
    )


def main():
    try:
        image_path = sys.argv[1]
    except IndexError:
        print('A DICOM image should be provided as single argument')
        sys.exit(1)

    dicom_image = open_dicom_image(image_path)

    markers = extract_markers(dicom_image.pixel_array)
    plot_image(markers, 'Markers')

    removed_small_holes = remove_small_holes(markers)
    plot_image(removed_small_holes, 'Removed Small Holes')


if __name__ == '__main__':
    main()
