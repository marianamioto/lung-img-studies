#!/usr/bin/env python

:import pydicom
import numpy
import pylab
import os
from matplotlib import pyplot, cm


def getnamefiles(PathDicom):
    lstFilesDCM = []
    for dirName, subdirList, fileList in os.walk(PathDicom):
        for filename in fileList:
            if ".dcm" in filename.lower():
                lstFilesDCM.append(filename)

    return lstFilesDCM

PathDicom = "/Users/Mariana/Desktop"
lstFileDCM = getnamefiles()

for fileDCM in lstFileDCM:
    #chamo as funcoes de processamento
