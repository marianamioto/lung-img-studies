#!/usr/bin/env python

import sys

import matplotlib.pyplot as plt
import numpy as np
import pydicom

from scipy import ndimage as ndi
from skimage import morphology
from skimage.color import label2rgb
from skimage.measure import label


def single_gray_plot(pixel_array, title=None):
    fig, ax = plt.subplots(figsize=(4, 3))
    ax.imshow(pixel_array, cmap=plt.cm.gray, interpolation='nearest')
    ax.axis('off')
    if title:
        ax.set_title(title)
    plt.show()


def plot_results(original_image, cleaned_image, features_labeled_image):
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(6, 3), sharex=True,
                                   sharey=True)
    ax1.imshow(original_image, cmap=plt.cm.gray, interpolation='nearest')
    ax1.contour(cleaned_image, [0.5], linewidths=1.2, colors='y')
    ax1.axis('off')
    ax1.set_adjustable('box-forced')
    ax2.imshow(features_labeled_image, interpolation='nearest')
    ax2.axis('off')
    ax2.set_adjustable('box-forced')
    margins = dict(hspace=0.01, wspace=0.01, top=1, bottom=0, left=0, right=1)
    fig.subplots_adjust(**margins)
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


def label_features(cleaned_image, original_image):
    labeled_image, _ = ndi.label(cleaned_image)
    return label2rgb(
        labeled_image,
        image=original_image,
        bg_label=0,
        bg_color=(1, 0, 0),
    )


def main():
    try:
        image_path = sys.argv[1]
    except IndexError:
        print('A DICOM image should be provided as single argument')
        sys.exit(1)

    dicom_image = open_dicom_image(image_path)

    markers = extract_markers(dicom_image.pixel_array)
    single_gray_plot(markers, 'Markers')

    removed_small_holes = remove_small_holes(markers)
    single_gray_plot(removed_small_holes, 'Removed Small Holes')

    features_labeled = label_features(removed_small_holes,
                                      dicom_image.pixel_array)
    single_gray_plot(features_labeled)

    plot_results(
        dicom_image.pixel_array,
        removed_small_holes,
        features_labeled,
    )


if __name__ == '__main__':
    main()
