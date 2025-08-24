from skimage import measure 
from skimage.measure import regionprops
import matplotlib.pyplot as plt
import matplotlib.patches as patches 
import localization

label_image = measure.label(localization.binary_car_image)
# get the connected components from the binary image

plate_dimesions = (0.08*label_image.shape[0], 0.2*label_image.shape[0],0.15*label_image.shape[1],0.4*label_image.shape[1])
min_height, max_height, min_width, max_width = plate_dimesions
plate_objects_cordinates = []
plate_like_objects = []
fig, (ax1) = plt.subplots(1)
ax1.imshow(localization.binary_car_image, cmap='gray')