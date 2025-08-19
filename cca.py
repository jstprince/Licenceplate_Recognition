from skimage import measure
from skimage.measure import regionprops
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import localization

label_image = measure.label(localization.binary_car_image)
fig, (ax1) = plt.subplots(1)

ax1.imshow(localization.binary_car_image, cmap='gray')

for region in regionprops(label_image):
    #draw rectangle around segmented region
    if region.area < 50:
        continue

    minr, minc, maxr, maxc = region.bbox

    rectBorder = patches.Rectangle((minc, minr), maxc - minc, maxr - minr, edgecolor = 'red', linewidth = 2, fill = False)
    ax1.add_patch(rectBorder)

    
plt.show()