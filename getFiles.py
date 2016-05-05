#!/usr/bin/env python

import os

def getFiles():
    PathDicom = "/Users/Mariana/Desktop/ILDdatabase/ILD_DB_txtROIs/3"

    lstFilesDCM = []
    for dirName, subdirList, fileList in os.walk(PathDicom):
        for filename in fileList:
            if ".dcm" in filename.lower():
                lstFilesDCM.append(os.path.join(dirName,filename))

    return lstFilesDCM
