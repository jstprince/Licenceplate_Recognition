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

#regionprops creates a list of properties of all the labled regions 

for region in regionprops(label_image):
    if region.area < 50:
        continue
    minr, minc, maxr, maxc = region.bbox
    region_height = maxr - minr
    region_width = maxc - minc

    if region_height >= min_height and region_height <= max_height and region_width >= min_width and region_width <= max_width and region_width > region_height:
        plate_like_objects.append(localization.binary_car_image[minr:maxr,minc:maxc])
        
        plate_objects_cordinates.append((minr,minc,maxr,maxc))

        rectBorder = patches.Rectangle((minc, min), maxc - minc, maxr - minr, edgecolor = 'red', linewidth = 2, fill = False)
        ax1.add_patch(rectBorder)

plt.show()