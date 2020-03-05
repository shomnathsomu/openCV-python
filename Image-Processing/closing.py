import cv2
from matplotlib import pyplot as plt
import numpy as np

img = cv2.imread('samples/new_011.jpg',0)
kernel = np.ones((5,5),np.uint8)
closing = cv2.morphologyEx(img, cv2.MORPH_CLOSE, kernel)

cv2.imwrite('1.png', closing)

plt.subplot(121),plt.imshow(img),plt.title('Original')
plt.xticks([]), plt.yticks([])
plt.subplot(122),plt.imshow(closing),plt.title('Blurred')
plt.xticks([]), plt.yticks([])
plt.show()
