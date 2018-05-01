#!/usr/bin/env python

import sys

import matplotlib.pyplot as plt
import numpy as np
import pydicom

from scipy import ndimage as ndi
from skimage import morphology
from skimage.color import label2rgb
from skimage.feature import canny
from skimage.filters import sobel
from skimage.measure import label


def single_gray_plot(pixel_array, title=None):
    fig, ax = plt.subplots(figsize=(12, 9))
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

    # When using watershed we need to have at least two different markers.
    #   Zero means not a marker.
    markers = np.zeros_like(pixel_array)
    markers[pixel_array < 700] = 1  # TODO: move to const
    markers[pixel_array > 800] = 2  # TODO: move to const
    # markers[pixel_array > 2000] = 3  # TODO: move to const
    return markers


def remove_small_holes(pixel_array):
    #fill_lungs = label(
    #    pixel_array,
    #    return_num=False,
    #)
    #single_gray_plot(fill_lungs)
    return morphology.remove_small_holes(
        pixel_array,
        500,  # TODO: move to const
    )


def label_features(cleaned_image, original_image):
    labeled_image, _ = ndi.label(cleaned_image)
    return label2rgb(
        labeled_image,
        image=original_image,
        bg_label=0,
        bg_color=(1, 0, 0),
    )


def apply_watershed(pixel_array):
    elavation_map = sobel(pixel_array)
    single_gray_plot(elavation_map, 'Elevation Map')

    # markers = remove_small_holes(pixel_array)
    # single_gray_plot(markers, 'Markers no holes')

    markers = extract_markers(pixel_array)
    single_gray_plot(markers, 'Markers')

    segmentation = morphology.watershed(elavation_map, markers)
    single_gray_plot(segmentation, 'watershed')

    bin_filled = ndi.binary_fill_holes(segmentation - 1)
    seg_minus_filled = (segmentation - bin_filled)
    single_gray_plot(seg_minus_filled, 'seg - filled')

    single_gray_plot(morphology.convex_hull_object(seg_minus_filled - 1), 'convex_hull_image')
    single_gray_plot(remove_small_holes(morphology.dilation(seg_minus_filled -1)), 'dilation')



def main():
    try:
        image_path = sys.argv[1]
    except IndexError:
        print('A DICOM image should be provided as single argument')
        sys.exit(1)

    dicom_image = open_dicom_image(image_path)
    single_gray_plot(dicom_image.pixel_array)

    segmented_image = apply_watershed(dicom_image.pixel_array)
    single_gray_plot(segmented_image)

    # plot_results(
    #     dicom_image.pixel_array,
    #     removed_small_holes,
    #     features_labeled,
    # )


if __name__ == '__main__':
    main()
