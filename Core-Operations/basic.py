# load a color image
import cv2
from matplotlib import pyplot as plt
# import numpy as np

img = cv2.imread('query/query_01.bmp')

# For BGR image, it returns an array of Blue, Green, Red values.
px = img[100,100]
print(px)

# For grayscale image, just corresponding intensity is returned.
blue = img[100,100,0]
print(blue)

# modify the pixel values the same way
img[100,100] = [255,255,255]
print (img[100,100])

# accessing RED value
img.item(10,10,2)

# modifying RED value
img.itemset((10,10,2),100)
img.item(10,10,2)

# returns a tuple of number of rows, columns and channels
print(img.shape)

# Total number of pixels is accessed by
print(img.size)

# Image datatype is obtained by
print(img.dtype)

# ROI can be obtained using Numpy indexing. 
# Here selecting something and copying it to another region in the image
ball = img[100:500, 300:600]
img[200:600, 100:400] = ball

# Splitting and Merging Image Channels
b,g,r = cv2.split(img)
img = cv2.merge((b,g,r))

# to make all the red pixels to zero
img[:,:,2] = 0

plt.imshow(img, cmap = 'gray', interpolation = 'bicubic')
plt.xticks([]), plt.yticks([])  # to hide tick values on X and Y axis
plt.show()
