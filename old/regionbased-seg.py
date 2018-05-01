import dicom
import numpy as np
import matplotlib.pyplot as plt

from skimage.filters import sobel
from skimage.morphology import watershed
from scipy import ndimage as ndi
from skimage.color import label2rgb

ds=dicom.read_file("/home/mioto/Desktop/CT-7358-0014.dcm")
image = ds.pixel_array


elevation_map = sobel(image/4096.)

plt.imshow(elevation_map, cmap=plt.cm.gray, interpolation='nearest')

plt.show()

markers = np.zeros_like(image)

markers[image < 2000] = 2

markers[image > 1600] = 1

plt.imshow(markers, cmap=plt.cm.gray, interpolation='nearest')

plt.show()

segmentation = watershed(elevation_map, markers)
segmentation = ndi.binary_fill_holes(segmentation - 1)
labeled_lung, _ = ndi.label(segmentation)
image_label_overlay = label2rgb(labeled_lung, image=image)

fig, axes = plt.subplots(1, 2, figsize=(8, 3), sharey=True)
axes[0].imshow(image, cmap=plt.cm.gray, interpolation='nearest')
axes[0].contour(segmentation, [0.5], linewidths=1.2, colors='y')
axes[1].imshow(image_label_overlay, interpolation='nearest')


plt.show()

