#!/usr/bin/env python

import pydicom
import skimage
import numpy as np
import os

from skimage import measure, filters

from utils import display


def contours(ds):
    level = ds.pixel_array.mean()
    # print(level)
    contours = measure.find_contours(ds.pixel_array, level)
    # print(contours)
    for contour in contours:
        for x, y in contour:
            ds.pixel_array[x][y] = ds.pixel_array.max()

PathDicom = "/Users/Mariana/Desktop/ILDdatabase/ILD_DB_txtROIs/3"

lstFilesDCM = []
for dirName, subdirList, fileList in os.walk(PathDicom):
    for filename in fileList:
        if ".dcm" in filename.lower():
            lstFilesDCM.append(os.path.join(dirName, filename))

for fileDCM in lstFilesDCM:
    ds = pydicom.read_file(fileDCM)
    contours(ds)
    display(ds)
