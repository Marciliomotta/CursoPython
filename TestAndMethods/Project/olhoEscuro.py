import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt

img = cv.imread('044R_3.png', 0)
edges = cv.Canny(img, 40, 50)
kernel = np.ones((5, 5), np.uint8)

dilation = cv.dilate(edges, kernel, iterations=1)
suave_dilation = cv.medianBlur(dilation, 11)

closing = cv.morphologyEx(edges, cv.MORPH_CLOSE, kernel)
suave_closing = cv.medianBlur(closing, 11)

erosion = cv.erode(edges, kernel)

opening = cv.morphologyEx(edges, cv.MORPH_OPEN, kernel)

grad = cv.morphologyEx(edges, cv.MORPH_GRADIENT, kernel)

fig, ax = plt.subplots(ncols=8, figsize=(15, 5))
ax[0].imshow(edges, cmap='gray')
ax[0].set_title('Original')
ax[0].axis('off')

ax[1].imshow(dilation, cmap='gray')
ax[1].set_title('dilation Aplicado')
ax[1].axis('off')

ax[2].imshow(suave_dilation, cmap='gray')
ax[2].set_title('suave Aplicado')
ax[2].axis('off')

ax[3].imshow(closing, cmap='gray')
ax[3].set_title('closing Aplicado')
ax[3].axis('off')

ax[4].imshow(suave_closing, cmap='gray')
ax[4].set_title('suave Aplicado')
ax[4].axis('off')

ax[5].imshow(erosion, cmap='gray')
ax[5].set_title('erosion Aplicado')
ax[5].axis('off')

ax[6].imshow(opening, cmap='gray')
ax[6].set_title('opening Aplicado')
ax[6].axis('off')

ax[7].imshow(grad, cmap='gray')
ax[7].set_title('grad Aplicado')
ax[7].axis('off')

plt.show()