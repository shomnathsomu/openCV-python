import cv2
# import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('samples/query_01.bmp')

blur = cv2.bilateralFilter(img,10,175,175)
# cv2.imwrite('1.jpg', blur)

plt.subplot(121),plt.imshow(img),plt.title('Original')
plt.xticks([]), plt.yticks([])
plt.subplot(122),plt.imshow(blur),plt.title('Blurred')
plt.xticks([]), plt.yticks([])
plt.show()
