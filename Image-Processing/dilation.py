import cv2
from matplotlib import pyplot as plt
import numpy as np

img = cv2.imread('samples/new_011.jpg',0)
kernel = np.ones((5,5),np.uint8)
dilation = cv2.dilate(img,kernel,iterations = 1)

# cv2.imwrite('1.png', dilation)

plt.subplot(121),plt.imshow(img),plt.title('Original')
plt.xticks([]), plt.yticks([])
plt.subplot(122),plt.imshow(dilation),plt.title('Blurred')
plt.xticks([]), plt.yticks([])
plt.show()
