#!/src/bin/env python


import numpy
import pydicom

from skimage.filters import threshold_otsu


def getRNU(image, binary):

    row, colum = image.shape
    foreground_pixels = []
    for x in range(row):
        for y in range(colum):
            if binary[x][y] != 0:
                foreground_pixels.append((x, y))

    foreground = [image[x][y] for x, y in foreground_pixels]

    # variances
    foreground_variance = numpy.var(foreground)
    total_variance = numpy.var(image)

    # areas
    foreground_area = float(len(foreground))
    total_area = float(len(image.flat))

    return (foreground_area/total_area) * (foreground_variance/total_variance)


if __name__ == '__main__':
    ds = pydicom.read_file("/Users/Mariana/Desktop/CT-0015.dcm")
    image = ds.pixel_array
    thresh = threshold_otsu(image)
    binary = image > thresh
    print(getRNU(image, binary))
